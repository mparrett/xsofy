# xsofy shell and deploy map, as of 2026-09-15 05:02 UTC

Shell, mobile, input, and deploy issues and PRs Matt touched in nooga/xsofy

Counts as of 2026-09-15 05:02 UTC: 69 nodes, 168 references. Edges are `#`-references in bodies and comments; the **related** column is the same data. Interactive map: `/Users/matt/projects-new/3p/joint-xsofy/pr-wip/workstream-map-republish/xsofy-map/index.html`.

## Mobile & touch UI

Start here: #128 (Epic: mobile and responsive shell)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#3](https://github.com/nooga/xsofy/issues/3) | issue | closed | 2026-05-14 | Chris-Bitler | Interactive Input Unavailable error on Android firefox mobile |  |  |
| [#22](https://github.com/nooga/xsofy/issues/22) | issue | closed | 2026-05-22 | mparrett | Mobile/responsive support | #128, #78, #84 |  |
| [#56](https://github.com/nooga/xsofy/issues/56) | issue | closed | 2026-06-02 | nnunley | Responsive UI event loop: composable, replay-safe input + cosmetic animation | #58, #61, #68, #69, #82, #84 |  |
| [#68](https://github.com/nooga/xsofy/pull/68) | PR | merged | 2026-06-06 | nnunley | Responsive UI event loop: poll-based run-loop for animated screens (#56) | #56, #61, #69 |  |
| [#83](https://github.com/nooga/xsofy/issues/83) | issue | closed | 2026-06-22 | mparrett | Browser: resize / orientation / visualViewport fit | #114, #116, #143, #78, #84 |  |
| [#112](https://github.com/nooga/xsofy/pull/112) | PR | closed | 2026-07-02 | mparrett | Responsive camera + narrow-terminal rendering | #116, #121, #128, #129, #139 |  |
| [#113](https://github.com/nooga/xsofy/pull/113) | PR | closed | 2026-07-02 | mparrett | Mobile touch shell + browser HUD bridge | #114, #116, #121, #122, #128, #129, #139 |  |
| [#114](https://github.com/nooga/xsofy/pull/114) | PR | closed | 2026-07-02 | mparrett | Debounced resize / orientation / visualViewport re-fit (#83) | #113, #116, #122, #128, #129, #139, #83 |  |
| [#116](https://github.com/nooga/xsofy/pull/116) | PR | closed | 2026-07-02 | mparrett | [preview only · do not merge] mobile stack integration (#111–#115, #119–#123) + #124 title | #112, #113, #114, #121, #122, #128, #129, #139, #83 |  |
| [#121](https://github.com/nooga/xsofy/pull/121) | PR | closed | 2026-07-02 | mparrett | Drop redundant HP/depth from the browser chrome | #112, #113, #116, #128, #129, #139 |  |
| [#122](https://github.com/nooga/xsofy/pull/122) | PR | closed | 2026-07-02 | mparrett | Reflow title and death screens on resize / font change | #113, #114, #116, #128, #129, #139 |  |
| [#127](https://github.com/nooga/xsofy/pull/127) | PR | closed | 2026-07-04 | mparrett | shell: horizontal split layout for phone landscape | #128, #129, #139 |  |
| [#128](https://github.com/nooga/xsofy/issues/128) | issue | closed | 2026-07-05 | mparrett | Epic: Mobile and responsive shell | #112, #113, #114, #116, #121, #122, #126, #127, #129, #131, #132, #133, #134, #135, #136, #137, #138, #139, #143, #150, #152, #154, #155, #156, #22, #44 |  |
| [#131](https://github.com/nooga/xsofy/pull/131) | PR | merged | 2026-07-05 | mparrett | render: responsive camera + narrow-terminal rendering | #128 |  |
| [#132](https://github.com/nooga/xsofy/pull/132) | PR | merged | 2026-07-05 | mparrett | topbar: narrow-width in-grid HP/status bar | #128, #197, #44 |  |
| [#133](https://github.com/nooga/xsofy/pull/133) | PR | merged | 2026-07-05 | mparrett | screens/reflow: reflow title and death screens on resize | #128 |  |
| [#134](https://github.com/nooga/xsofy/pull/134) | PR | merged | 2026-07-05 | mparrett | bridge: ui-bridge HUD channels + startup/stats wiring | #128, #135 |  |
| [#135](https://github.com/nooga/xsofy/pull/135) | PR | merged | 2026-07-05 | mparrett | feat(mobile): blank client-shell scaffold (structure + hooks) | #128, #134, #136, #143, #154, #155 |  |
| [#136](https://github.com/nooga/xsofy/pull/136) | PR | closed | 2026-07-05 | mparrett | fit: debounced re-fit + letterbox the grid | #128, #135, #137, #143, #154, #155 |  |
| [#137](https://github.com/nooga/xsofy/pull/137) | PR | merged | 2026-07-05 | mparrett | feat(mobile): touch shell redesign — portrait + landscape | #128, #136, #150, #154, #155, #156, #197, #44 |  |
| [#138](https://github.com/nooga/xsofy/pull/138) | PR | merged | 2026-07-05 | mparrett | screens/nudge-guard: ignore the shell&#x27;s resize nudge on modal reads | #128, #143, #197 |  |
| [#143](https://github.com/nooga/xsofy/pull/143) | PR | merged | 2026-07-08 | mparrett | shell: portrait readiness: aspect cap + letterbox + resize nudge | #128, #135, #136, #138, #152, #154, #197, #83 |  |
| [#152](https://github.com/nooga/xsofy/pull/152) | PR | closed | 2026-07-11 | mparrett | fix(shell): portrait cap uses dvh, not vh (clears the iOS URL bar) | #128, #143, #154 |  |
| [#155](https://github.com/nooga/xsofy/pull/155) | PR | closed | 2026-07-12 | mparrett | feat(mobile): touch controls, OPTIONS panel, diagnostics + theming | #128, #135, #136, #137, #154, #156 |  |
| [#156](https://github.com/nooga/xsofy/pull/156) | PR | closed | 2026-07-12 | mparrett | feat(mobile): touch relayout — 4-row grid, mirrored, persistent y/n + keyset row | #128, #137, #155 |  |
| [#167](https://github.com/nooga/xsofy/pull/167) | PR | merged | 2026-07-22 | mparrett | shell: add &#x27;off&#x27; to the force-touch cycle (auto/force/off) | #197 |  |
| [#173](https://github.com/nooga/xsofy/pull/173) | PR | merged | 2026-07-23 | mparrett | feat(shell): mobile keypad rearrangement + font touch-ups | #168, #197 |  |

## Input & keys

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#61](https://github.com/nooga/xsofy/pull/61) | PR | merged | 2026-06-05 | mparrett | fix(title): WASM-safe input poll via key-pending? (deploy regression) | #56, #59, #60, #68 |  |
| [#76](https://github.com/nooga/xsofy/pull/76) | PR | merged | 2026-06-09 | mparrett | feat(input): add Ctrl-C as a confirm-quit alias for Esc |  |  |
| [#82](https://github.com/nooga/xsofy/issues/82) | issue | open | 2026-06-22 | mparrett | TUI: non-blocking modal/menu input | #56, #84 |  |
| [#85](https://github.com/nooga/xsofy/pull/85) | PR | merged | 2026-06-22 | mparrett | fix(play): repaint on idle terminal resize, not just on keypress | #86 |  |
| [#158](https://github.com/nooga/xsofy/pull/158) | PR | open | 2026-07-13 | mparrett | feat(input): bind Plan 9 arrow-key runes (fixes down-arrow in alacritty9) | #197 |  |

## Deploy, Pages & releases

Start here: #58 (why Pages deploys from tags, not main); #197 (release prep for the first tag since v0.0.2)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#44](https://github.com/nooga/xsofy/issues/44) | issue | open | 2026-05-30 | metalivedev | Need game release version number in web version for bug reporting | #100, #128, #132, #137, #57, #58, #59, #63 |  |
| [#57](https://github.com/nooga/xsofy/pull/57) | PR | merged | 2026-06-04 | mparrett | ci: pin let-go to v1.9.0; add @latest matrix cell for upstream drift smoke | #126, #44, #58 |  |
| [#58](https://github.com/nooga/xsofy/issues/58) | issue | closed | 2026-06-04 | mparrett | ci: deploy Pages from version tags instead of main | #44, #56, #57, #59, #60 |  |
| [#59](https://github.com/nooga/xsofy/pull/59) | PR | merged | 2026-06-04 | mparrett | ci: deploy Pages from version tags instead of main | #44, #58, #60, #61 |  |
| [#60](https://github.com/nooga/xsofy/pull/60) | PR | merged | 2026-06-04 | mparrett | ci: add browser smoke gate (Part C-lite) before Pages deploy | #58, #59, #61 |  |
| [#63](https://github.com/nooga/xsofy/pull/63) | PR | merged | 2026-06-05 | nnunley | Repro test infra: Layer-1 runtime smoke + ?seed= browser bridge | #44, #69 |  |
| [#65](https://github.com/nooga/xsofy/pull/65) | PR | merged | 2026-06-05 | nnunley | Headless-browser e2e gate (boot + seeded regression) | #69 |  |
| [#69](https://github.com/nooga/xsofy/pull/69) | PR | merged | 2026-06-06 | nnunley | Land the determinism + replay + repro/e2e stack onto main (#63–#66, then #67/#68) | #56, #63, #65, #68 |  |
| [#77](https://github.com/nooga/xsofy/pull/77) | PR | merged | 2026-06-13 | nooga | Publish Homebrew formula to shared tap |  |  |
| [#100](https://github.com/nooga/xsofy/issues/100) | issue | closed | 2026-06-30 | mparrett | Prepare release v0.0.2 | #102, #103, #105, #106, #107, #44 |  |
| [#102](https://github.com/nooga/xsofy/pull/102) | PR | merged | 2026-06-30 | mparrett | ci: ship the xsofy client shell (rune font + ?font=system), not let-go&#x27;s generic shell | #100, #103, #106, #95, #96 |  |
| [#103](https://github.com/nooga/xsofy/pull/103) | PR | closed | 2026-06-30 | mparrett | ci(pages): branch-based publishing + per-PR previews | #100, #102, #106 |  |
| [#106](https://github.com/nooga/xsofy/pull/106) | PR | merged | 2026-06-30 | mparrett | ci(pages): branch-based publishing + per-PR previews | #100, #102, #103 |  |
| [#107](https://github.com/nooga/xsofy/pull/107) | PR | merged | 2026-07-01 | mparrett | docs: add CHANGELOG + release-notes config (v0.0.2) | #100 |  |
| [#117](https://github.com/nooga/xsofy/pull/117) | PR | closed | 2026-07-02 | mparrett | [canary · do not merge] Pages deploy sanity check (off #108) |  |  |
| [#118](https://github.com/nooga/xsofy/pull/118) | PR | merged | 2026-07-02 | mparrett | ci(pages): recreate the root CNAME if it&#x27;s ever dropped |  |  |
| [#129](https://github.com/nooga/xsofy/pull/129) | PR | merged | 2026-07-05 | mparrett | build-info: build-info.json generator shared by make and CI | #112, #113, #114, #116, #121, #122, #127, #128 |  |
| [#163](https://github.com/nooga/xsofy/pull/163) | PR | merged | 2026-07-20 | mparrett | ci: cache the lg binary and Playwright browsers; align Go with the deploy | #191 |  |
| [#195](https://github.com/nooga/xsofy/pull/195) | PR | open | 2026-09-14 | mparrett | fix(build): pin let-go to v1.12.2 so the web bundle boots | #196, #197 |  |
| [#196](https://github.com/nooga/xsofy/issues/196) | issue | open | 2026-09-14 | mparrett | The deploy-floor CI lane never builds or boots the bundle it certifies | #195, #197 |  |
| [#197](https://github.com/nooga/xsofy/issues/197) | issue | open | 2026-09-14 | mparrett | Release prep: align on scope for the first tag since v0.0.2 | #132, #137, #138, #139, #143, #150, #154, #158, #167, #168, #173, #191, #195, #196 |  |

## Web shell & host

Start here: #84 (Epic: player interaction ergonomics)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#31](https://github.com/nooga/xsofy/pull/31) | PR | merged | 2026-05-26 | mparrett | tools: fix patch_wasm_coi splice on bundles with UTF-8 source |  |  |
| [#78](https://github.com/nooga/xsofy/pull/78) | PR | merged | 2026-06-17 | mparrett | build(wasm): client-owned shell via lg -w -w-shell none | #22, #79, #80, #83, #84 |  |
| [#79](https://github.com/nooga/xsofy/pull/79) | PR | merged | 2026-06-19 | mparrett | feat(shell): Fairfax HD as the single terminal font (fixes rune cell-advance drift) | #78, #80, #84 |  |
| [#80](https://github.com/nooga/xsofy/pull/80) | PR | merged | 2026-06-21 | mparrett | fix(tools): reactivate WASM patch scripts against current let-go glue | #78, #79 |  |
| [#84](https://github.com/nooga/xsofy/issues/84) | issue | open | 2026-06-22 | mparrett | Epic: Player interaction ergonomics | #22, #56, #78, #79, #82, #83 |  |
| [#86](https://github.com/nooga/xsofy/pull/86) | PR | merged | 2026-06-22 | mparrett | fix(shell): debounced re-fit on rotate + visualViewport, not just resize | #85 |  |
| [#93](https://github.com/nooga/xsofy/pull/93) | PR | merged | 2026-06-25 | mparrett | xsofy workbench: static, server, and wasm |  |  |
| [#95](https://github.com/nooga/xsofy/pull/95) | PR | merged | 2026-06-29 | mparrett | Fix the web-font measurement race that twitches the terminal | #102, #96 |  |
| [#96](https://github.com/nooga/xsofy/pull/96) | PR | merged | 2026-06-29 | mparrett | Add ?font=system to render the terminal in the platform mono | #102, #95 |  |
| [#105](https://github.com/nooga/xsofy/pull/105) | PR | merged | 2026-06-30 | mparrett | fix(wasm): keep the COI service worker when it&#x27;s the isolation source | #100 |  |
| [#126](https://github.com/nooga/xsofy/issues/126) | issue | closed | 2026-07-03 | mparrett | Dev: wire onEmit in the shell so ?dump-replay= surfaces the replay code on web | #128, #150, #57 |  |
| [#139](https://github.com/nooga/xsofy/pull/139) | PR | merged | 2026-07-05 | mparrett | title-moat: keep decorative runes off the title text | #112, #113, #114, #116, #121, #122, #127, #128, #197 |  |
| [#150](https://github.com/nooga/xsofy/pull/150) | PR | merged | 2026-07-09 | mparrett | feat(shell): replay link in the config pane (#126) | #126, #128, #137, #154, #197 |  |
| [#154](https://github.com/nooga/xsofy/pull/154) | PR | merged | 2026-07-11 | mparrett | feat(shell): bind the #app host mount (let-go #378) | #128, #135, #136, #137, #143, #150, #152, #155, #197 |  |
| [#168](https://github.com/nooga/xsofy/pull/168) | PR | open | 2026-07-22 | mparrett | demo(shell): WebGL renderer + post-process shader overlay (CRT, water, mode7) - DEMO/POC | #173, #197 |  |
| [#191](https://github.com/nooga/xsofy/pull/191) | PR | open | 2026-09-06 | mparrett | build(wasm): emit main.wasm externally and boot it with instantiateStreaming | #163, #197 |  |
