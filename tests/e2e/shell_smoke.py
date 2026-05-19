#!/usr/bin/env python3
"""End-to-end smoke test for the WASM bottom-shell.

What it covers:
  1. shell.html loads and the bar DOM mounts.
  2. xsofy/startup fires; title + quest populate.
  3. xsofy/stats fires; HP/depth/turn populate.
  4. A D-pad tap injects a key (player moves; turn increments).
  5. Portrait viewport collapses the layout: hint row drops, touch
     controls render.
  6. Resize wake: landscape→portrait re-renders without a keypress
     (rows recount, term/size updates via SAB).
  7. Font cycle persists via localStorage and the wake refits.

Prereqs (matches CLAUDE.md "Local WASM serve" notes):
  - The let-go fork on expmt/js-bridge must be built once: cd ../let-go && go build
  - WASM bundle and sidecars must be present in dist/:
        lg -w dist main.lg
        cp dev/serve.json dev/shell.html dist/
  - A trusted-cert HTTPS dev server on https://localhost:8000:
        npx --yes serve@latest dist -l 8000 \\
          --ssl-cert /tmp/xsofy_certs/localhost+4.pem \\
          --ssl-key  /tmp/xsofy_certs/localhost+4-key.pem
  - Playwright Chromium: uv run --with playwright python -m playwright install chromium

Run:
  uv run --with playwright python tests/e2e/shell_smoke.py
  # or override URL: XSOFY_URL=https://192.168.1.169:8000/ uv run ...

Exit code 0 on full pass, 1 on any failure.
"""
import os
import sys
import time
from playwright.sync_api import sync_playwright

URL = os.environ.get("XSOFY_URL", "https://localhost:8000/")

# --- assertion helpers ------------------------------------------------------

_failed = []

def expect(cond, label):
    """Soft-assert: record the failure and continue so we get a full report."""
    if cond:
        print(f"  ok  {label}")
    else:
        print(f"  FAIL {label}")
        _failed.append(label)

def visible_rows(page):
    """Read the visible terminal buffer, clipped to t.cols (avoids zombie
    cells past the new cols on a resized terminal)."""
    return page.evaluate("""() => {
        const t = window._lgTerm;
        const buf = t.buffer.active;
        const out = [];
        for (let y = 0; y < t.rows; y++) {
            const line = buf.getLine(y);
            out.push(line ? line.translateToString(true).slice(0, t.cols) : '');
        }
        return { cols: t.cols, rows: t.rows, lines: out };
    }""")

def boot_past_title(page):
    """Click + press space until xsofy/startup fires. Title screen blocks
    on a single key; WASM boot has variable timing (3–11s)."""
    for _ in range(12):
        evts = page.evaluate("() => (window.__caught ||= [], window.__caught.slice())")
        if any(e["type"] == "xsofy/startup" for e in evts):
            return True
        page.click("#terminal", timeout=5000)
        time.sleep(0.2)
        page.keyboard.press(" ")
        time.sleep(1.5)
    return any(e["type"] == "xsofy/startup" for e in page.evaluate("() => window.__caught.slice()"))

# --- the test ---------------------------------------------------------------

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # Boot directly into portrait — most of the assertions live here.
    ctx = browser.new_context(
        ignore_https_errors=True,
        viewport={"width": 375, "height": 812},
    )
    ctx.add_init_script("""
        window.__caught = [];
        ['xsofy/boot', 'xsofy/startup', 'xsofy/stats'].forEach(n => {
          window.addEventListener(n, e => window.__caught.push({type: n, detail: e.detail}));
        });
    """)
    page = ctx.new_page()
    page.on("console", lambda m: print(f"  [console.{m.type}] {m.text}") if m.type == "error" else None)
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_selector("#xsofy-shell", timeout=15000)
    time.sleep(3)
    assert boot_past_title(page), "boot never produced xsofy/startup"
    time.sleep(2)

    print("\n--- DOM + event smoke ---")
    info = page.evaluate("""() => ({
        shell:  !!document.getElementById('xsofy-shell'),
        title:  document.getElementById('xs-title')?.textContent,
        quest:  document.getElementById('xs-quest')?.textContent,
        hp:     document.getElementById('xs-hp')?.textContent,
        depth:  document.getElementById('xs-depth')?.textContent,
        turn:   document.getElementById('xs-turn')?.textContent,
        btns:   document.querySelectorAll('#xsofy-shell button').length,
        lgKey:  typeof window._lgKey,
        lgWake: typeof window._lgWake,
        lgSet:  typeof window._lgSetFontSize,
    })""")
    expect(info["shell"], "shell #xsofy-shell mounted")
    expect(info["btns"] >= 14, f"shell exposes a D-pad+actions button set (got {info['btns']})")
    expect(info["title"] and info["title"] != "—", f"title populated ({info['title']!r})")
    expect(info["hp"] and info["hp"] != "·", f"hp populated ({info['hp']!r})")
    expect(info["depth"] == "1", f"depth = 1 ({info['depth']!r})")
    expect(info["lgKey"] == "function", "_lgKey is exposed")
    expect(info["lgWake"] == "function", "_lgWake is exposed")
    expect(info["lgSet"] == "function", "_lgSetFontSize is exposed")

    print("\n--- D-pad input ---")
    # Use wait ('.') rather than a movement key: directional moves can land
    # on hazards (deep water, lava) which open a confirm-prompt screen and
    # suspend turn advancement until y/n. wait is unconditional.
    turn_before = int(info["turn"])
    page.evaluate("() => window._lgKey('.')")
    time.sleep(1.5)
    turn_after = int(page.evaluate("() => document.getElementById('xs-turn').textContent"))
    expect(turn_after > turn_before, f"_lgKey('.') advanced turn ({turn_before} -> {turn_after})")

    print("\n--- Portrait layout ---")
    touch_display = page.evaluate(
        "() => getComputedStyle(document.querySelector('#xsofy-shell .touch')).display"
    )
    expect(touch_display == "grid", f".touch is grid in portrait ({touch_display!r})")
    snap = visible_rows(page)
    bottom = next((r for r in reversed(snap["lines"]) if r.strip()), "")
    # Task 3 (2026-05-18): when gw<67 the hint is dropped to free a row.
    # On a 375px portrait viewport at fontSize 14, cols ≈ 42 ≪ 67.
    expect("yuhjklbn:move" not in bottom,
           f"keybind hint dropped on narrow portrait (bottom row={bottom!r})")
    expect(snap["cols"] < 67, f"portrait cols < 67 ({snap['cols']})")

    print("\n--- Resize wake (landscape -> portrait) ---")
    ctx2 = browser.new_context(
        ignore_https_errors=True,
        viewport={"width": 1280, "height": 800},
    )
    ctx2.add_init_script("""
        window.__caught = [];
        ['xsofy/startup','xsofy/stats'].forEach(n => {
          window.addEventListener(n, e => window.__caught.push({type:n, detail:e.detail}));
        });
    """)
    page2 = ctx2.new_page()
    page2.goto(URL, wait_until="networkidle", timeout=30000)
    page2.wait_for_selector("#xsofy-shell", timeout=15000)
    time.sleep(3)
    assert boot_past_title(page2), "landscape boot never produced xsofy/startup"
    time.sleep(2)
    pre_cols = page2.evaluate("() => window._lgTerm.cols")
    pre_rows = page2.evaluate("() => window._lgTerm.rows")
    expect(pre_cols > 67, f"landscape cols > 67 ({pre_cols})")

    page2.set_viewport_size({"width": 375, "height": 812})
    time.sleep(2.5)  # resize -> _lgWake -> game-loop wakes -> re-renders
    post_cols = page2.evaluate("() => window._lgTerm.cols")
    post_rows = page2.evaluate("() => window._lgTerm.rows")
    expect(post_cols < pre_cols, f"cols shrank on resize ({pre_cols} -> {post_cols})")
    expect(post_rows != pre_rows, f"rows changed on resize ({pre_rows} -> {post_rows})")
    # The wake should have triggered render-full at the new dims — verify by
    # looking for the log/messages region (xsofy writes "You ..." messages
    # there once the player has moved past the title sequence).
    post_snap = visible_rows(page2)
    has_content = any(("@" in r or "You " in r or "yuhjklbn" in r) for r in post_snap["lines"])
    expect(has_content, "rendered content visible after resize wake")
    ctx2.close()

    print("\n--- Hold-to-repeat ---")
    # Hold the WAIT button for ~1s. With repeat enabled (default), expect
    # ~5 fires: 1 immediate + (1000-250)/150 ≈ 5 repeats. Don't pin a tight
    # window — Playwright timing slop is ~50ms.
    turn_pre = int(page.evaluate("() => document.getElementById('xs-turn').textContent"))
    page.evaluate("""() => {
        const btn = document.querySelector('.pad button[data-key="."]');
        const r = btn.getBoundingClientRect();
        btn.dispatchEvent(new PointerEvent('pointerdown', {bubbles:true, clientX:r.x+5, clientY:r.y+5}));
    }""")
    time.sleep(1.0)
    page.evaluate("() => window.dispatchEvent(new PointerEvent('pointerup', {bubbles:true}))")
    time.sleep(0.5)
    turn_post = int(page.evaluate("() => document.getElementById('xs-turn').textContent"))
    fires = turn_post - turn_pre
    expect(3 <= fires <= 9, f"hold WAIT for 1s repeated ({fires} fires; expected ~5)")

    # Toggle OFF, hold again — should fire exactly once.
    page.evaluate("""() => {
        const t = document.getElementById('xs-repeat-toggle');
        t.dispatchEvent(new PointerEvent('pointerdown', {bubbles:true}));
    }""")
    time.sleep(0.2)
    state = page.evaluate("() => document.getElementById('xs-repeat-state').textContent")
    expect(state == "off", f"toggle flipped to off ({state!r})")

    turn_pre = int(page.evaluate("() => document.getElementById('xs-turn').textContent"))
    page.evaluate("""() => {
        const btn = document.querySelector('.pad button[data-key="."]');
        const r = btn.getBoundingClientRect();
        btn.dispatchEvent(new PointerEvent('pointerdown', {bubbles:true, clientX:r.x+5, clientY:r.y+5}));
    }""")
    time.sleep(1.0)
    page.evaluate("() => window.dispatchEvent(new PointerEvent('pointerup', {bubbles:true}))")
    time.sleep(0.5)
    turn_post = int(page.evaluate("() => document.getElementById('xs-turn').textContent"))
    expect(turn_post - turn_pre == 1, f"with repeat OFF, single fire only ({turn_post - turn_pre})")

    persisted = page.evaluate("() => localStorage.getItem('xsofy/auto-repeat')")
    expect(persisted == "0", f"toggle state persisted ({persisted!r})")

    # Reset to on so subsequent runs don't carry surprise state if the
    # context were ever reused.
    page.evaluate("""() => {
        const t = document.getElementById('xs-repeat-toggle');
        t.dispatchEvent(new PointerEvent('pointerdown', {bubbles:true}));
    }""")

    print("\n--- Font cycle ---")
    pre_size = page.evaluate("() => document.getElementById('xs-font-px')?.textContent")
    pre_rows = page.evaluate("() => window._lgTerm.rows")
    page.evaluate("""() => {
        const b = document.getElementById('xs-font-cycle');
        b.dispatchEvent(new PointerEvent('pointerdown', {bubbles: true}));
    }""")
    time.sleep(2.0)
    post_size = page.evaluate("() => document.getElementById('xs-font-px')?.textContent")
    post_rows = page.evaluate("() => window._lgTerm.rows")
    persisted = page.evaluate("() => localStorage.getItem('xsofy/font-size')")
    expect(pre_size != post_size, f"font size advanced ({pre_size} -> {post_size})")
    expect(persisted == post_size, f"font size persisted to localStorage ({persisted!r})")
    expect(pre_rows != post_rows,
           f"row count changed -> refit + wake re-rendered ({pre_rows} -> {post_rows})")

    browser.close()

print()
if _failed:
    print(f"FAILED ({len(_failed)}):")
    for f in _failed:
        print(f"  - {f}")
    sys.exit(1)
print("PASS")
sys.exit(0)
