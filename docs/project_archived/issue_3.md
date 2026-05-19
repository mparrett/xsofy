# Issue 3 — Interactive Input Unavailable / reload loop on Firefox mobile + Safari

**Resolved 2026-05-19** — PR open at
[mparrett/let-go fix/coi-bootstrap-safari-firefox](https://github.com/mparrett/let-go/tree/fix/coi-bootstrap-safari-firefox)
against `nooga/let-go:main`. Two commits, `wasm.go` only, +28/−4.
Verified on Chrome (macOS), iOS Safari, macOS Firefox via a minimal
upstream-equivalent stack. See
`docs/upstream-crossing-quest.html` for the full narrative.

Upstream: https://github.com/nooga/xsofy/issues/3

## What users see

On Android Firefox (and macOS Safari per comment) the published GitHub Pages
build flashes between `Interactive Input Unavailable` and `loading...`
indefinitely. The page never reaches the title screen.

## Root cause (confirmed)

This is the same COI bootstrap failure documented in
`docs/project_notes/bugs.md` (2026-05-17), seen from the production hosting
path instead of local dev. Two compounding bugs in the let-go WASM template
that generates xsofy's `dist/`:

1. **`coi-serviceworker.js` sets `Cross-Origin-Embedder-Policy: credentialless`.**
   `credentialless` is Chrome-only. Safari and Firefox treat the header as
   unset → `crossOriginIsolated` stays `false` → `SharedArrayBuffer` is not
   exposed → `term/read-key` bails → page shows the error UI.

2. **The boot shim does `register(...).then(() => location.reload())` with no
   loop guard.** Because (1) means isolation never activates, every reload
   re-enters the same path and reloads again. That is exactly the
   "flashes between error and loading rapidly" symptom in the screenshot.

Localhost masks both: `http://localhost` is an exempted secure context, so
isolation appears to work without the SW even doing anything correct.

## Fixes already made in our fork

Both fixes landed on `~/projects-new/3p/let-go` branch `expmt/js-bridge`,
scoped to `wasm.go` (the template that emits `index.html` + the SW into the
build output):

- `f3ed218` — fix: guard COI service worker against reload loops, unregister when redundant
  - Adds a `sessionStorage['_lgCoiTried']` guard so the SW is registered at
    most once per tab; failed isolation no longer reload-loops.
  - When the page is *already* cross-origin-isolated (server sent the
    headers — e.g. our `dev/serve.json` path), unregister any lingering SW
    so it can't intercept future fetches with stale logic.

- `44812e9` — fix: COI service worker passes through server headers, uses require-corp
  - SW only fills in `COOP`/`COEP` when the response doesn't already carry
    them (prevents clobbering correct server-sent headers).
  - When the SW does inject `COEP`, uses `require-corp` instead of
    `credentialless`. `require-corp` is accepted by Safari, Firefox, and
    Chrome; `credentialless` is Chrome-only.

Net effect: 1 file changed in let-go, ~15 lines added across both commits.

## Assessment

The fixes are correct in scope and confirmed against the failure modes in
this issue. Verification still pending **before** opening upstream:

- [ ] Rebuild xsofy with the patched let-go (`lg -w dist main.lg`) and load
      `dist/index.html` on:
  - [ ] Android Firefox (the reporter's environment) — should boot once,
        reload at most once, then stay on the title screen.
  - [ ] iOS Safari and macOS Safari — same.
  - [ ] Desktop Chrome — regression check, isolation should still activate.
- [ ] Confirm recovery path: a client with the *old* (broken) SW already
      registered should self-heal on next visit. The new SW's
      `skipWaiting` + `clients.claim` swap it in; the HTML's
      auto-unregister branch then removes it once headers isolate the
      page. If self-heal doesn't trigger, document the "clear site data"
      escape hatch in the issue reply.
- [ ] Check that the GitHub Pages deploy workflow
      (`.github/workflows/deploy-pages.yml`) doesn't pin a let-go version
      that would need bumping in lockstep with the upstream merge.

## Proposed upstream PR shape

**Target repo:** `nooga/let-go` (NOT `nooga/xsofy`). xsofy's `dist/` is
generated; the template lives in let-go's `wasm.go`. Patching xsofy's
`dist/` directly would be overwritten on the next build.

**Branch/title:** `fix/coi-bootstrap-safari-firefox` —
"fix: COI bootstrap works on Safari/Firefox + no reload loops"

**Contents:** cherry-pick `f3ed218` and `44812e9` onto `main`. Two commits,
single file, ~15 lines. No API change, no behavioral change on Chrome,
strict improvement on Safari/Firefox.

**PR description should include:**
- Link back to `nooga/xsofy#3` as the user-visible symptom.
- Brief table of which browser accepts which COEP value.
- The "clear site data" recovery hint for clients stuck with the old SW.
- Confirmation that the existing `dev/serve.json`-style header path keeps
  working (the SW no longer clobbers it — that's commit 2).

**Out of scope (do not bundle):**
- The viewport meta tag commit (`6f4f17d`) — unrelated to this issue.
- The `_lgEmit` / shell slot / `_lgSetFontSize` / `_lgTerm` commits —
  those are xsofy-specific bridge work, not COI fixes.
- Touching xsofy itself. Once let-go merges, the next xsofy build picks up
  the fix.

## Reply to file on the issue (after upstream merge)

> Confirmed the cause is in the WASM template's COI bootstrap, not xsofy
> itself. Patch up at nooga/let-go#NNN. If you're hit by this and want to
> recover without waiting for a redeploy, clear site data for the page
> host once — the broken service worker will unregister itself on the
> next load.
