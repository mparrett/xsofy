#!/usr/bin/env python3
"""Per-turn perf sampler.

Listens for xsofy/perf events (emitted by the game-loop on every :game
iteration; see xsofy/ui_bridge.lg :: emit-perf and main.lg). Prints a
small summary so you can characterize the engine's bottlenecks under a
known workload.

This is a profiling probe, NOT a regression test. Numbers vary by host
(CPU, browser, build mode), so it asserts nothing — it just dumps stats
and you read them.

Two workloads run:
  1. 20 discrete _lgKey('.') presses with a small gap. Models a player
     tapping deliberately. Surfaces per-turn variance (fire spread,
     entity AI spikes, etc).
  2. Hold WAIT for 2.0s. Models the hold-to-repeat path. Surfaces the
     STEADY-state rate the engine can sustain and the gap between
     attributed work (update+render) and wall-clock-between-turns
     (i.e. xterm canvas paint + bridge + SAB busy-wait).

Prereqs (same as shell_smoke.py): dev server on https://localhost:8000
with the latest bundle in dist/.

Run:
  uv run --with playwright python tests/e2e/perf_sample.py
  XSOFY_URL=https://192.168.x.x:8000/ uv run ...
"""
import os
import time
from playwright.sync_api import sync_playwright

URL = os.environ.get("XSOFY_URL", "https://localhost:8000/")

def summarize(label, samples):
    if not samples:
        print(f"  {label}: no samples")
        return
    upds = [s['update'] for s in samples]
    rens = [s['render'] for s in samples]
    tots = [s['total']  for s in samples]
    print(f"  n={len(samples)} ({label})")
    print(f"    update ms : min={min(upds):3} avg={sum(upds)//len(upds):3} max={max(upds):3}")
    print(f"    render ms : min={min(rens):3} avg={sum(rens)//len(rens):3} max={max(rens):3}")
    print(f"    total  ms : min={min(tots):3} avg={sum(tots)//len(tots):3} max={max(tots):3}")
    if len(samples) >= 2:
        gaps = [samples[i+1]['at'] - samples[i]['at'] for i in range(len(samples)-1)]
        avg_gap = sum(gaps) // len(gaps)
        print(f"    wall gap  : min={min(gaps):3} avg={avg_gap:3} max={max(gaps):3}  (~{1000//max(avg_gap,1)} Hz)")
        avg_work = sum(tots) // len(tots)
        print(f"    untracked : ~{max(0, avg_gap - avg_work)} ms/turn (xterm canvas + bridge + SAB busy-wait)")

def boot(p):
    """Spawn a fresh context and walk past the title screen."""
    ctx = p.chromium.launch(headless=True)
    c = ctx.new_context(ignore_https_errors=True, viewport={'width':375,'height':812})
    c.add_init_script("""
        window.__perf = [];
        window.addEventListener('xsofy/perf', e => window.__perf.push({...e.detail, at: performance.now()|0}));
    """)
    page = c.new_page()
    page.goto(URL, wait_until='networkidle', timeout=30000)
    page.wait_for_selector('#xsofy-shell', timeout=15000)
    time.sleep(4)
    for _ in range(10):
        page.click('#terminal'); page.keyboard.press(' '); time.sleep(1)
        if page.evaluate("() => document.querySelectorAll('.xterm-rows > div')[7]?.textContent?.match(/yuhjklbn|HP/)"):
            break
    time.sleep(2)
    page.evaluate("() => window.__perf = []")
    return ctx, page

with sync_playwright() as p:
    # Each workload gets its own fresh boot — prior runs alter world state
    # (enemies wander, fire spreads, player on a hazard tile), which would
    # confound the next sample.
    print(f"\n--- 20 discrete '.' (WAIT) presses, 50ms apart ---")
    ctx, page = boot(p)
    for _ in range(20):
        page.evaluate("() => window._lgKey('.')")
        time.sleep(0.05)
    time.sleep(2)
    summarize("discrete", page.evaluate("() => window.__perf.slice()"))
    ctx.close()

    print(f"\n--- HOLD WAIT for 2.0s (auto-repeat at 10 Hz) ---")
    ctx, page = boot(p)
    page.evaluate("""() => {
        const btn = document.querySelector('.pad button[data-key="."]');
        const r = btn.getBoundingClientRect();
        btn.dispatchEvent(new PointerEvent('pointerdown', {bubbles:true, clientX:r.x+5, clientY:r.y+5}));
    }""")
    time.sleep(2.0)
    page.evaluate("() => window.dispatchEvent(new PointerEvent('pointerup', {bubbles:true}))")
    time.sleep(1.0)
    summarize("held-repeat", page.evaluate("() => window.__perf.slice()"))
    ctx.close()

    print(f"\n--- AUTOEXPLORE for 4.0s (engine-driven, no input bottleneck) ---")
    ctx, page = boot(p)
    page.evaluate("() => window._lgKey('x')")
    time.sleep(4.0)
    page.evaluate("() => window._lgKey('\\u001b')")  # cancel autoexplore
    time.sleep(1.0)
    summarize("autoexplore", page.evaluate("() => window.__perf.slice()"))
    ctx.close()
print()
