# Perf lane map, as of 2026-09-15 04:42 UTC

Perf, bench, ratchet, and CI-timeline issues and PRs Matt touched in nooga/let-go and nooga/xsofy

Counts as of 2026-09-15 04:42 UTC: 175 nodes, 393 references. Edges are `#`-references in bodies and comments; the **related** column is the same data. Interactive map: `~/projects-new/3p/joint-xsofy/perf-lane-map/index.html`.

## CI timeline & runners

Start here: #581 (CI audit tracker; item 6 is the timeline legs); #876 (where runner time goes (61% timeline); cadence lever)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#236](https://github.com/nooga/let-go/pull/236) | PR | merged | 2026-06-15 | mparrett | ci(perf-timeline): add workflow_dispatch for historical backfill | #238, #564, #597 |  |
| [#238](https://github.com/nooga/let-go/pull/238) | PR | merged | 2026-06-16 | mparrett | ci(perf-timeline): resolve dispatch ref in a script step (support short SHAs) | #236, #597 |  |
| [#319](https://github.com/nooga/let-go/pull/319) | PR | merged | 2026-06-23 | mparrett | ci(pages): add workflow_dispatch trigger |  |  |
| [#363](https://github.com/nooga/let-go/pull/363) | PR | merged | 2026-06-29 | nnunley | ci(perf): arm64 timeline leg + auto-backfill of release tags | #573, #583, #597 | letgo-ci-waste-review |
| [#528](https://github.com/nooga/let-go/issues/528) | issue | open | 2026-07-16 | mparrett | Epic: Maintenance debt — retire superseded mechanisms, reduce process weight | #464, #531, #544, #574, #575, #581 | ecosystem-health-audit-2026-07, letgo-simplification-audit |
| [#565](https://github.com/nooga/let-go/pull/565) | PR | merged | 2026-07-18 | mparrett | ci(perf-timeline): per-OS concurrency groups, rebase-retry publish, skip docs-only commits | #561, #573 | letgo-timeline-count-interaction, letgo-typeinfer-perf-audit |
| [#573](https://github.com/nooga/let-go/pull/573) | PR | merged | 2026-07-18 | mparrett | ci(perf-timeline): revert -count to 3 — a count-4 ubuntu leg measures 104 min, past the 90 | #363, #561, #565, #581, #583, #651, #876, #882 | feedback-unwrap-bold-lead-ins, letgo-651-baseline-seed-answer, letgo-ci-waste-review |
| [#581](https://github.com/nooga/let-go/issues/581) | issue | open | 2026-07-19 | mparrett | CI: coverage gaps, a 3× stdlib compile per PR, and gates documented as CI-run that aren&#x27;t | #522, #528, #573, #583, #876, #878, #882 | ecosystem-health-audit-2026-07, letgo-ci-waste-review |
| [#583](https://github.com/nooga/let-go/pull/583) | PR | merged | 2026-07-20 | mparrett | ci(perf-timeline): raise the macos-14 leg timeout to 150 min | #363, #561, #573, #581, #878 | letgo-ci-cost-cadence-2026-09, letgo-ci-waste-review, letgo-v1120-wasm-gosum-regression |
| [#693](https://github.com/nooga/let-go/issues/693) | issue | open | 2026-08-06 | mparrett | ci: run the `benchmark/` suite in a label-opt-in lane | #597, #644, #655, #656, #686 | feedback-verify-status-before-acting, letgo-reduce-shadow-656 |
| [#732](https://github.com/nooga/let-go/pull/732) | PR | closed | 2026-08-12 | nnunley | build: gate binaries by directory, and run the binary check on push | #733 |  |
| [#733](https://github.com/nooga/let-go/pull/733) | PR | merged | 2026-08-12 | nnunley | build: move build outputs into build/, promote lg into bin/ | #649, #732 |  |
| [#740](https://github.com/nooga/let-go/pull/740) | PR | merged | 2026-08-13 | nnunley | ci(perf): freeze a per-release baseline on every tag, and fix the Pages publish race | #445, #597, #651, #663, #684, #752 | feedback-verify-status-before-acting, letgo-684-baseline-reseed |
| [#752](https://github.com/nooga/let-go/issues/752) | issue | open | 2026-08-18 | mparrett | pages.yml redeploys on any Perf Timeline conclusion, not only success | #597, #740 |  |
| [#876](https://github.com/nooga/let-go/pull/876) | PR | open | 2026-09-14 | mparrett | docs(ci): report where Actions runner time goes | #445, #573, #581, #597, #651, #705, #877, #878, #882 | gh-actions-usage-query-method, letgo-ci-90s-target-and-go127, letgo-ci-cost-cadence-2026-09 |
| [#877](https://github.com/nooga/let-go/pull/877) | PR | merged | 2026-09-14 | mparrett | ci(tinygo): fetch the pinned wasmtime asset instead of curl\|bash | #876 | letgo-ci-cost-cadence-2026-09 |
| [#878](https://github.com/nooga/let-go/pull/878) | PR | open | 2026-09-14 | mparrett | ci(perf): raise the ubuntu perf capture cap to 120 minutes | #581, #583, #597, #876 | letgo-ci-90s-target-and-go127, letgo-ci-cost-cadence-2026-09, letgo-timeline-leg-stoptimer-overhead |

## Ratchet, baselines & gates

Start here: #445 (why a single-shot A/B cannot gate); #663 (Norman's measurement-status issue; the ratchet is not consulted); #705 (three gaps that let the gate report green)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#278](https://github.com/nooga/let-go/pull/278) | PR | merged | 2026-06-20 | mparrett | perf-page: relative-% timeline charts |  |  |
| [#328](https://github.com/nooga/let-go/pull/328) | PR | merged | 2026-06-24 | mparrett | ci(perf): same-runner A/B microbenchmark check on PRs | #597 |  |
| [#329](https://github.com/nooga/let-go/pull/329) | PR | merged | 2026-06-24 | mparrett | perf-page: CPU-tier filter and selectable baseline; release-baseline recapture | #597 |  |
| [#330](https://github.com/nooga/let-go/pull/330) | PR | merged | 2026-06-24 | mparrett | perf(bench-ratchet): add named -profile with a curated pr-fast profile |  |  |
| [#333](https://github.com/nooga/let-go/pull/333) | PR | merged | 2026-06-25 | mparrett | perf(bench-ratchet): retune pr-fast to count 3 / benchtime 500ms |  |  |
| [#334](https://github.com/nooga/let-go/pull/334) | PR | merged | 2026-06-25 | mparrett | ci(perf): use the pr-fast profile for the PR benchmark gate |  |  |
| [#369](https://github.com/nooga/let-go/pull/369) | PR | merged | 2026-06-30 | nnunley | chore: remove accidentally-committed perf-page binary + gitignore it |  |  |
| [#373](https://github.com/nooga/let-go/pull/373) | PR | merged | 2026-07-01 | mparrett | docs(perf): document the perf label / PR-time A/B workflow |  |  |
| [#386](https://github.com/nooga/let-go/pull/386) | PR | merged | 2026-07-03 | mparrett | perf(ci): wasm A/B benchmark gate (perf-wasm label) |  |  |
| [#401](https://github.com/nooga/let-go/pull/401) | PR | closed | 2026-07-07 | nnunley | perf(tooling): byte-level .lg-caller allocation attribution (LG_ALLOC_ATTR=1) | #399, #402, #403 |  |
| [#445](https://github.com/nooga/let-go/issues/445) | issue | open | 2026-07-12 | mparrett | perf-pr A/B is ungateable as a single shot; median-of-N makes it a real gate | #517, #559, #560, #597, #686, #705, #720, #740, #876 | letgo-684-baseline-reseed, letgo-ci-cost-cadence-2026-09, letgo-micro-opt-audit |
| [#517](https://github.com/nooga/let-go/pull/517) | PR | merged | 2026-07-15 | mparrett | perf(ci): interleaved repeat A/B as an informational shadow check | #445 | letgo-core-boot-unify-520, perf-repeat-ab-shadow-check, workspace-simplification-workstream |
| [#552](https://github.com/nooga/let-go/pull/552) | PR | merged | 2026-07-17 | nooga | bench: VM-vs-AOT comparison — lower fixtures to native Go, drop joker/go-joker/gloat/fenne | #554, #578, #582 | feedback-outbound-plain-not-figurative, ir-compile-bytecode-vs-native, letgo-loop-fusion-440 |
| [#561](https://github.com/nooga/let-go/pull/561) | PR | merged | 2026-07-18 | nnunley | perf(bench-ratchet): robust sampling — warmup-discarding median + anchor-drift warning | #558, #564, #565, #570, #573, #583, #597, #651, #663 | letgo-651-baseline-seed-answer, letgo-ci-waste-review, letgo-timeline-count-interaction |
| [#564](https://github.com/nooga/let-go/pull/564) | PR | merged | 2026-07-18 | nnunley | perf: recapture baseline with warmup-discarding median sampling (stacks on #561) | #236, #464, #558, #561, #570, #571, #597, #651, #684, #705, #709 | feedback-dont-relitigate-reviewers-own-pr, letgo-651-baseline-seed-answer, letgo-micro-opt-audit |
| [#570](https://github.com/nooga/let-go/pull/570) | PR | merged | 2026-07-18 | nnunley | fix(bench-ratchet): report out-of-scope baseline entries as one line, not MISSING rows (st | #561, #564 |  |
| [#578](https://github.com/nooga/let-go/pull/578) | PR | merged | 2026-07-19 | nooga | bench: refresh results on post-#552 main; update README benchmark section | #552, #558, #559, #560, #563, #567, #568, #569, #571, #582 |  |
| [#579](https://github.com/nooga/let-go/pull/579) | PR | merged | 2026-07-19 | nnunley | perf(ir): re-emit ordinary var loads instead of copying them; add lowering-shape ratchet | #574, #575, #580, #613, #618 | letgo-ir-locals-register-map, letgo-self-comment-smell-audit |
| [#582](https://github.com/nooga/let-go/pull/582) | PR | merged | 2026-07-19 | mparrett | bench: document the two AOT mechanisms behind the results table | #552, #578 |  |
| [#597](https://github.com/nooga/let-go/issues/597) | issue | open | 2026-07-21 | mparrett | perf-page: capture the release reference per machine tier so &quot;% vs v1.8.0&quot; is comparable a | #236, #238, #328, #329, #363, #445, #561, #564, #651, #663, #684, #693, #705, #740, #752, #791, #795, #876, #878, #879, #880 | letgo-684-baseline-reseed, letgo-ci-90s-target-and-go127, letgo-ci-cost-cadence-2026-09 |
| [#621](https://github.com/nooga/let-go/pull/621) | PR | merged | 2026-07-22 | mparrett | bench(compiler): distinguish execution entry modes | #619 | letgo-gloat-fib-probe-618-619 |
| [#651](https://github.com/nooga/let-go/issues/651) | issue | open | 2026-07-30 | nnunley | perf(bench-ratchet): seed docs/perf/baseline.json from CI timeline snapshots (retire the l | #561, #564, #573, #597, #663, #684, #740, #876 | feedback-unwrap-bold-lead-ins, letgo-651-baseline-seed-answer, letgo-684-baseline-reseed |
| [#655](https://github.com/nooga/let-go/pull/655) | PR | merged | 2026-07-30 | mparrett | bench: compare against a pinned-release baseline | #639, #656, #663, #693 | feedback-reviewdecision-is-stale-aggregate, feedback-verify-status-before-acting, letgo-perf-lanes-design-note |
| [#659](https://github.com/nooga/let-go/issues/659) | issue | open | 2026-07-31 | mparrett | The AOT-compilable benchmark fixtures are not on `main` |  |  |
| [#660](https://github.com/nooga/let-go/issues/660) | issue | open | 2026-07-31 | mparrett | Lowering falls back to bytecode silently, and only the bench harness notices | #425, #554, #596, #598, #681 |  |
| [#663](https://github.com/nooga/let-go/issues/663) | issue | open | 2026-07-31 | nnunley | Performance measurement status: ratchet is not consulted; startup regressed 5ms -&gt; 9ms unn | #464, #561, #580, #597, #651, #655, #705, #720, #740 | feedback-read-reviewer-corrections-before-architecture-pages, feedback-unwrap-bold-lead-ins, feedback-verify-status-before-acting |
| [#677](https://github.com/nooga/let-go/pull/677) | PR | merged | 2026-08-04 | nnunley | build: single-source Go toolchain via go.mod toolchain directive |  | letgo-645-invoke-regression, letgo-nnunley-commit-convention, letgo-perf-ab-toolchain-confound |
| [#684](https://github.com/nooga/let-go/pull/684) | PR | merged | 2026-08-05 | mparrett | perf(bench-ratchet): seed the baseline from a window, reduced in ratio space | #564, #597, #651, #740, #780, #781 | feedback-dont-relitigate-reviewers-own-pr, letgo-684-baseline-reseed, letgo-wiki-population-workstream |
| [#705](https://github.com/nooga/let-go/issues/705) | issue | open | 2026-08-09 | mparrett | Three gaps that let the perf gate report green through a regression | #445, #464, #564, #597, #663, #706, #708, #709, #722, #876 | letgo-ci-cost-cadence-2026-09, letgo-pr-followup-mining-ledger, perf-repeat-ab-shadow-check |
| [#708](https://github.com/nooga/let-go/pull/708) | PR | merged | 2026-08-09 | mparrett | ci(perf-repeat): post the shadow-check report as a sticky PR comment | #705, #706, #709, #715 | letgo-generated-artifact-gate-lane, perf-repeat-ab-shadow-check |
| [#709](https://github.com/nooga/let-go/pull/709) | PR | closed | 2026-08-09 | mparrett | probe(vm): comment-only control for the repeat A/B noise floor | #564, #691, #705, #706, #708 | perf-repeat-ab-shadow-check |
| [#715](https://github.com/nooga/let-go/pull/715) | PR | merged | 2026-08-11 | mparrett | ci(perf): paginate sticky-comment lookup in both lanes | #708 | letgo-generated-artifact-gate-lane |
| [#780](https://github.com/nooga/let-go/pull/780) | PR | merged | 2026-08-23 | nnunley | build: bench-ratchet infrastructure — deterministic rebaseline, Go 1.26.5 baseline, pre-pu | #684, #781, #791, #794, #883 | letgo-generated-sums-fake-conflicts, letgo-nooga-reviews-as-comments |
| [#791](https://github.com/nooga/let-go/issues/791) | issue | open | 2026-09-04 | nnunley | bench-ratchet: IRCompile and InitFromLGB regressed since the #780 baseline (#727 allocs, # | #597, #723, #727, #730, #780, #794, #795 |  |
| [#795](https://github.com/nooga/let-go/pull/795) | PR | open | 2026-09-04 | nnunley | tooling: add bench-baton, a machine-quiescence lease for benchmarks | #597, #791 | letgo-ci-cost-cadence-2026-09 |
| [#879](https://github.com/nooga/let-go/pull/879) | PR | open | 2026-09-14 | mparrett | feat(perf-page): page-wide CPU filter for the timeline views | #597, #880 | letgo-ci-cost-cadence-2026-09 |
| [#880](https://github.com/nooga/let-go/pull/880) | PR | open | 2026-09-14 | mparrett | feat(perf-page): add a Timeline explorer page | #597, #879 | letgo-ci-90s-target-and-go127 |
| [#882](https://github.com/nooga/let-go/pull/882) | PR | open | 2026-09-15 | mparrett | bench(vm): hoist per-iteration setup out of the vector benchmark loops | #573, #581, #876, #883, #884 | letgo-timeline-leg-stoptimer-overhead |
| [#883](https://github.com/nooga/let-go/issues/883) | issue | open | 2026-09-15 | mparrett | bench-ratchet: deterministic bars come from profiles captured a month apart | #780, #882 | letgo-ratchet-stale-baseline-min, letgo-timeline-leg-stoptimer-overhead |
| [#884](https://github.com/nooga/let-go/issues/884) | issue | open | 2026-09-15 | mparrett | pkg/vm: BenchmarkConsCreation measures an empty loop | #882 | letgo-timeline-leg-stoptimer-overhead |

## VM hot paths & call ABI

Start here: #464 (micro-opt epic (8 PRs merged)); #722 (the boxed variadic call ABI is the wall)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#210](https://github.com/nooga/let-go/pull/210) | PR | merged | 2026-06-11 | nnunley | feat(vm,ir): ExecContext threading — explicit dynamic-binding + scope context, delete goid | #211, #220 |  |
| [#211](https://github.com/nooga/let-go/issues/211) | issue | closed | 2026-06-11 | mparrett | Follow-up to #210: lock-free dynamic-var deref — a design fork (A: copy-on-write vs B: act | #210, #220 |  |
| [#220](https://github.com/nooga/let-go/pull/220) | PR | merged | 2026-06-13 | mparrett | perf(vm): lock-free dynamic-var deref via persistent frame-list binding stack | #210, #211 |  |
| [#224](https://github.com/nooga/let-go/pull/224) | PR | merged | 2026-06-15 | nnunley | perf(vm): cut redundant value hashing on the lowering hot path |  |  |
| [#304](https://github.com/nooga/let-go/pull/304) | PR | merged | 2026-06-22 | mparrett | perf(rt): subs without materializing the whole string to runes | #303 |  |
| [#371](https://github.com/nooga/let-go/pull/371) | PR | merged | 2026-07-01 | nnunley | Multi-arity direct calls + self-host coalesce fix, os/exec* streaming, VM Box fast-path |  |  |
| [#385](https://github.com/nooga/let-go/pull/385) | PR | closed | 2026-07-03 | mparrett | perf(vm): monomorphic inline cache for protocol dispatch |  |  |
| [#396](https://github.com/nooga/let-go/pull/396) | PR | merged | 2026-07-07 | nnunley | perf(vm): box-free KeywordLookup fast path (-4% native suite allocs) | #395, #397, #399 |  |
| [#397](https://github.com/nooga/let-go/pull/397) | PR | merged | 2026-07-07 | nnunley | perf(vm): chunked ArrayVectorSeq (growing-from-1) + orderless maps + alloc-free symbol par | #395, #396, #437, #464 | letgo-loop-fusion-440 |
| [#399](https://github.com/nooga/let-go/pull/399) | PR | closed | 2026-07-07 | nnunley | perf(rt): Range fast path in reduce + set via transient — series close (-48% suite allocs  | #396, #401 |  |
| [#402](https://github.com/nooga/let-go/pull/402) | PR | merged | 2026-07-07 | nnunley | perf(rt/ir): stop (nth string i) allocating the rune slice; O(1) registry emptiness check  | #401, #403 |  |
| [#442](https://github.com/nooga/let-go/pull/442) | PR | merged | 2026-07-11 | mparrett | perf(rt): close timeout channels from one shared timer daemon |  | feedback-jj-escalation-only, letgo-tinygo-pr522-round2, xsofy-determinism-hash-width |
| [#464](https://github.com/nooga/let-go/issues/464) | issue | open | 2026-07-13 | nnunley | Epic: Runtime performance &amp; concurrency | #397, #503, #522, #528, #544, #559, #560, #563, #564, #567, #568, #569, #571, #619, #644, #663, #705 | letgo-micro-opt-audit, letgo-simplification-audit, lgb-compression-lgbz |
| [#544](https://github.com/nooga/let-go/pull/544) | PR | merged | 2026-07-17 | mparrett | fix(vm): synchronize BoxedTypes cache and Boxed.Hash() lazy cache | #464, #522, #528 | letgo-simplification-audit |
| [#559](https://github.com/nooga/let-go/pull/559) | PR | merged | 2026-07-18 | mparrett | perf(vm): use the transient growth reserve in assocTransient inserts | #445, #464, #560, #578 | letgo-micro-opt-audit |
| [#560](https://github.com/nooga/let-go/pull/560) | PR | merged | 2026-07-18 | mparrett | perf(vm): lock-free fast path for realized LazySeq access | #445, #464, #559, #578 | letgo-micro-opt-audit |
| [#563](https://github.com/nooga/let-go/pull/563) | PR | merged | 2026-07-18 | mparrett | perf(vm): gate lookup-stats noters on an atomic before the mutex | #464, #578 | letgo-micro-opt-audit |
| [#567](https://github.com/nooga/let-go/pull/567) | PR | merged | 2026-07-18 | mparrett | perf(vm): typed Keyword/Int fast paths at the top of valueEquiv | #464, #578 | letgo-micro-opt-audit |
| [#568](https://github.com/nooga/let-go/pull/568) | PR | merged | 2026-07-18 | mparrett | perf(vm): box-free keyword lookup in protocol method dispatch | #464, #578 | letgo-micro-opt-audit |
| [#569](https://github.com/nooga/let-go/pull/569) | PR | merged | 2026-07-18 | mparrett | perf(vm): strconv.Itoa and plain concat for Int/Keyword String() | #464, #578 | letgo-micro-opt-audit |
| [#571](https://github.com/nooga/let-go/pull/571) | PR | merged | 2026-07-18 | mparrett | perf(vm): divide-free fast path for checkedMulInt overflow guard | #464, #564, #578 | letgo-micro-opt-audit |
| [#612](https://github.com/nooga/let-go/pull/612) | PR | merged | 2026-07-22 | nnunley | perf(ir): catalog-driven op dispatch — generated OpByKeyword string switch (§1/§2/§2b) | #618 |  |
| [#613](https://github.com/nooga/let-go/pull/613) | PR | merged | 2026-07-22 | nnunley | perf(rt): direct-call natives for the hot clojure.core surface | #579, #580, #618, #627, #639 |  |
| [#618](https://github.com/nooga/let-go/pull/618) | PR | closed | 2026-07-22 | mparrett | feat(vm): OP_CALL_SELF for non-tail self-recursive defn calls | #579, #612, #613, #619, #620, #644, #645, #646, #700 | letgo-gloat-fib-probe-618-619 |
| [#619](https://github.com/nooga/let-go/pull/619) | PR | closed | 2026-07-22 | mparrett | perf(vm): reuse frames per bytecode call tree | #464, #618, #620, #621, #644 | letgo-gloat-fib-probe-618-619 |
| [#620](https://github.com/nooga/let-go/issues/620) | issue | open | 2026-07-22 | nnunley | Design: constant-space tail calls on the explicit-frame VM (closures, multi-arity, apply) | #425, #618, #619, #644, #645, #646, #691, #720, #722 | feedback-search-the-mechanism-not-the-symptom, letgo-645-invoke-regression, letgo-boundary-abi-program |
| [#644](https://github.com/nooga/let-go/issues/644) | issue | open | 2026-07-29 | mparrett | vm: `Frame.Run` is Go-recursive — deep lg→lg recursion aborts the process | #425, #464, #618, #619, #620, #639, #645, #649, #656, #686, #691, #693, #700, #720, #726 | letgo-645-invoke-regression, perf-lane-map-inventory |
| [#645](https://github.com/nooga/let-go/pull/645) | PR | merged | 2026-07-29 | mparrett | vm: make direct bytecode calls non-recursive with an explicit frame chain | #618, #620, #644, #646, #656, #686, #691, #700, #706, #719, #720, #722, #730 | feedback-no-merging-unapproved-prs, feedback-search-the-mechanism-not-the-symptom, feedback-verify-authorship-before-attributing |
| [#646](https://github.com/nooga/let-go/issues/646) | issue | open | 2026-07-29 | mparrett | perf(vm): re-evaluate static self-call shortcut after shared frame transitions | #618, #620, #645, #700 | letgo-645-invoke-regression |
| [#656](https://github.com/nooga/let-go/issues/656) | issue | closed | 2026-07-30 | mparrett | `reduce` is 1.75x slower than v1.12.2 — bisected to #639 | #531, #639, #644, #645, #655, #686, #693, #700 | letgo-pr-followup-mining-ledger, letgo-reduce-shadow-656 |
| [#667](https://github.com/nooga/let-go/pull/667) | PR | merged | 2026-08-01 | nnunley | refactor(ir): catalog-driven form-head dispatch with load-time coherence check |  | letgo-nnunley-commit-convention |
| [#686](https://github.com/nooga/let-go/pull/686) | PR | merged | 2026-08-05 | mparrett | perf(rt): restore reduce&#x27;s ArrayVector and Range fast paths | #445, #531, #639, #644, #645, #656, #691, #693, #700, #720 | letgo-645-invoke-regression, letgo-reduce-shadow-656 |
| [#691](https://github.com/nooga/let-go/pull/691) | PR | closed | 2026-08-06 | mparrett | probe(vm): revert #645 to measure the explicit frame chain&#x27;s cost | #620, #639, #644, #645, #686, #700, #709 | letgo-645-invoke-regression |
| [#700](https://github.com/nooga/let-go/issues/700) | issue | open | 2026-08-08 | mparrett | vm: bytecode invoke is ~1.7x costlier since #645 (explicit frame chain) | #618, #639, #644, #645, #646, #656, #686, #691, #706, #719, #720, #722, #723, #726, #727, #730, #794 | letgo-645-invoke-regression, letgo-boundary-abi-program, perf-lane-map-inventory |
| [#706](https://github.com/nooga/let-go/pull/706) | PR | closed | 2026-08-09 | mparrett | vm: drop leaveFrame&#x27;s unused *Frame parameter to unpin f from memory | #645, #700, #705, #708, #709, #719, #720, #723, #730 | letgo-645-invoke-regression, letgo-boundary-abi-program |
| [#719](https://github.com/nooga/let-go/pull/719) | PR | merged | 2026-08-11 | mparrett | perf(vm): keep defer scaffolding out of the dispatch hot path | #645, #649, #700, #706, #720, #722, #723, #726, #730 | feedback-no-merging-unapproved-prs, feedback-verify-status-before-acting, letgo-645-invoke-regression |
| [#720](https://github.com/nooga/let-go/issues/720) | issue | closed | 2026-08-11 | mparrett | vm: PreparedCall — resolve once, reuse one frame for per-element callback invokes | #445, #620, #644, #645, #663, #686, #700, #706, #719, #722, #723, #726, #727, #730, #794 | letgo-645-invoke-regression, letgo-boundary-abi-program, perf-lane-map-inventory |
| [#721](https://github.com/nooga/let-go/issues/721) | issue | open | 2026-08-12 | mparrett | ir: CSE merges var reads across set! — :mutated-vars only ever contains nil |  | letgo-boundary-abi-program |
| [#722](https://github.com/nooga/let-go/issues/722) | issue | open | 2026-08-12 | mparrett | perf: the boxed variadic call ABI keeps being the wall — name it, instrument it, give it f | #620, #639, #645, #700, #705, #719, #720 | letgo-boundary-abi-program, letgo-pure-xxh3-aot-tinygo-probe |
| [#723](https://github.com/nooga/let-go/pull/723) | PR | merged | 2026-08-12 | mparrett | perf(vm): move cold error arms out of the dispatch loop | #700, #706, #719, #720, #726, #727, #791 | feedback-no-merging-unapproved-prs, letgo-645-invoke-regression, letgo-boundary-abi-program |
| [#726](https://github.com/nooga/let-go/pull/726) | PR | merged | 2026-08-12 | mparrett | perf(vm,rt): add PreparedCall for per-element callback loops; adopt in some | #644, #700, #719, #720, #723 | feedback-no-merging-unapproved-prs, letgo-645-invoke-regression, letgo-boundary-abi-program |
| [#727](https://github.com/nooga/let-go/pull/727) | PR | merged | 2026-08-12 | mparrett | perf(rt): adopt PreparedCall in reduce&#x27;s fold loops | #641, #700, #720, #723, #791, #794 | feedback-check-concurrent-session-ownership, feedback-no-merging-unapproved-prs, letgo-645-invoke-regression |
| [#730](https://github.com/nooga/let-go/pull/730) | PR | merged | 2026-08-12 | mparrett | perf(vm): remove the runLoop hop; make leaveFrame parameter-free | #645, #700, #706, #719, #720, #791 | feedback-check-concurrent-session-ownership, feedback-no-merging-unapproved-prs, letgo-645-invoke-regression |
| [#794](https://github.com/nooga/let-go/pull/794) | PR | merged | 2026-09-04 | nnunley | perf(vm): make PrepareCall allocation-free for native fold loops | #700, #720, #727, #780, #791 | letgo-wiki-population-workstream |

## IR / AOT lowering

Start here: #425 (AOT native-entry / self-contained gogen)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#97](https://github.com/nooga/let-go/issues/97) | issue | open | 2026-05-27 | nnunley | Roadmap: Go-package interop (lg-gen, smart wrappers, Mode B AOT lowering) | #596, #741 | letgo-596-lg-compile-plan |
| [#235](https://github.com/nooga/let-go/pull/235) | PR | merged | 2026-06-15 | nnunley | perf(ir): thread typeinfer state + preserve [:dtype T]; complete numeric typing (contagion |  |  |
| [#239](https://github.com/nooga/let-go/pull/239) | PR | closed | 2026-06-16 | nnunley | fix(ir): close four gogen self-AOT lowering gaps (nth-non-int, free-vars, identifier mungi |  |  |
| [#274](https://github.com/nooga/let-go/issues/274) | issue | open | 2026-06-19 | nnunley | Flat index-RPN-direct bytecode representation (Level 2: drop block-args at the source) |  | letgo-ir-locals-register-map |
| [#285](https://github.com/nooga/let-go/pull/285) | PR | merged | 2026-06-20 | nnunley | perf-tooling(fanout): gate on lg→go expansion ratio + portable os/ls walk |  |  |
| [#344](https://github.com/nooga/let-go/pull/344) | PR | merged | 2026-06-27 | nnunley | feat(ir): build args once in build-call — eliminate dead duplicate call nodes (#258) |  |  |
| [#357](https://github.com/nooga/let-go/issues/357) | issue | closed | 2026-06-29 | mparrett | AOT lowering: float param constrained only by float arithmetic is typed `int` → non-compil | #356, #425, #438, #446, #534, #599 | ir-compile-bytecode-vs-native, letgo-aot-numeric-lowering-landed, letgo-aot-pathtrace-spike-math-gap |
| [#395](https://github.com/nooga/let-go/pull/395) | PR | merged | 2026-07-07 | nnunley | chore(perf): re-baseline ir-stress corpus after upstream drift (2347 -&gt; 2366) | #396, #397 |  |
| [#403](https://github.com/nooga/let-go/pull/403) | PR | merged | 2026-07-07 | nnunley | perf(ir/typeinfer): worklist membership via in-place transient-map flags (−1GB cloneAndSet | #401, #402, #404 |  |
| [#404](https://github.com/nooga/let-go/pull/404) | PR | merged | 2026-07-07 | nnunley | feat(ir-stress): tool-maintained coverage baseline — make ir-stress-rebaseline | #403 |  |
| [#425](https://github.com/nooga/let-go/issues/425) | issue | open | 2026-07-09 | nnunley | AOT native-entry: generate the Go entry frame, self-contain `gogen`, and stop the silent p | #357, #424, #438, #502, #503, #534, #554, #596, #607, #620, #644, #652, #660, #735 | feedback-read-reviewer-corrections-before-architecture-pages, letgo-aot-split, letgo-gogen-self-contain-425 |
| [#434](https://github.com/nooga/let-go/pull/434) | PR | merged | 2026-07-10 | nnunley | perf(ir): transducer-fusion foundation — data-driven pass list + remove arity-1 + transduc |  |  |
| [#437](https://github.com/nooga/let-go/pull/437) | PR | merged | 2026-07-10 | nnunley | chore(perf): refresh ir-stress and benchmark baselines after upstream drift | #397 |  |
| [#438](https://github.com/nooga/let-go/pull/438) | PR | merged | 2026-07-11 | nnunley | feat(native-bridge): //lg native-primitive generation — drain hot trampolines (IRCompile − | #357, #425, #534 | letgo-core-boot-unify-520, plan9-support-workstream |
| [#440](https://github.com/nooga/let-go/pull/440) | issue | merged | 2026-07-11 | nnunley | feat(ir): loop-fusion (deforestation) — pass, enabled, comp-chains + into |  | letgo-loop-fusion-440 |
| [#446](https://github.com/nooga/let-go/pull/446) | PR | merged | 2026-07-12 | nnunley | feat(ir): deterministic lowered tree — densify + work-unit typeinfer guard | #357 | letgo-error-stack-review-sweep |
| [#531](https://github.com/nooga/let-go/issues/531) | issue | open | 2026-07-16 | nnunley | Consolidate the spread-out native-behavior mechanisms (registration + interop emitters) | #528, #554, #656, #686 | feedback-read-reviewer-corrections-before-architecture-pages, letgo-reduce-shadow-656, letgo-simplification-audit |
| [#534](https://github.com/nooga/let-go/issues/534) | issue | closed | 2026-07-16 | mparrett | AOT lowering drops the int→float coercion in mixed int/float arithmetic | #357, #425, #438 | letgo-aot-numeric-lowering-landed |
| [#554](https://github.com/nooga/let-go/issues/554) | issue | closed | 2026-07-18 | mparrett | AOT lowering: a fully-typed fn signature gets no boxed wrapper or override registration | #425, #531, #552, #596, #599, #653, #660 | cljgo-benchmark-arms-race, letgo-aot-return-hint-findings |
| [#558](https://github.com/nooga/let-go/pull/558) | PR | merged | 2026-07-18 | mparrett | perf(ir): move inferred types to a positional side table — ~100x faster type writes | #561, #564, #574, #575, #578, #601 | letgo-lgbdump-void-strip, letgo-micro-opt-audit, letgo-typeinfer-perf-audit |
| [#574](https://github.com/nooga/let-go/issues/574) | issue | open | 2026-07-18 | nnunley | Epic: IR normalization + execution-form cleanup (EPIC-017) | #528, #558, #575, #579 | ecosystem-health-audit-2026-07, feedback-read-reviewer-corrections-before-architecture-pages, letgo-ir-locals-register-map |
| [#575](https://github.com/nooga/let-go/issues/575) | issue | open | 2026-07-18 | nnunley | Epic: block interface as shared liveness metadata + block-arg erasure (EPIC-018) | #528, #558, #574, #579 | letgo-ir-locals-register-map |
| [#580](https://github.com/nooga/let-go/pull/580) | PR | merged | 2026-07-19 | nnunley | feat(ir): *ir-compile-strict* + a bytecode-path coverage census (70.7% vs the 99.5% we wer | #579, #601, #613, #663 | letgo-ir-locals-register-map, letgo-lgbdump-void-strip, letgo-nnunley-commit-convention |
| [#596](https://github.com/nooga/let-go/issues/596) | issue | open | 2026-07-20 | mparrett | CLI: a first-class AOT compile command | #425, #554, #607, #658, #660, #735, #741, #97 | feedback-read-reviewer-corrections-before-architecture-pages, letgo-596-lg-compile-plan, letgo-aot-return-hint-findings |
| [#598](https://github.com/nooga/let-go/issues/598) | issue | closed | 2026-07-21 | mparrett | AOT lowering: `(defn f ^long [args] …)` — the idiomatic return-hint position — silently dr | #599, #660, #661, #662 | letgo-aot-return-hint-findings |
| [#599](https://github.com/nooga/let-go/issues/599) | issue | closed | 2026-07-21 | mparrett | AOT lowering: returns stay boxed (`vm.Value` + `rt.AddValue`) even for recursive int fns — | #357, #554, #598, #661, #662 | cljgo-benchmark-arms-race, letgo-599-typed-returns, letgo-aot-return-hint-findings |
| [#627](https://github.com/nooga/let-go/pull/627) | PR | closed | 2026-07-23 | nnunley | fix(rt): resolve ns alias in LookupOrRegisterNSNoLoad | #613, #639, #640, #641 | letgo-nnunley-native-hoist-stack |
| [#639](https://github.com/nooga/let-go/pull/639) | PR | merged | 2026-07-27 | nnunley | feat(rt): hoist 222 clojure.core primitives to named //lg:native decls | #613, #627, #640, #641, #644, #655, #656, #686, #691, #700, #722 | feedback-verify-authorship-before-attributing, letgo-645-invoke-regression, letgo-bisect-requires-clean-xfd |
| [#640](https://github.com/nooga/let-go/pull/640) | PR | merged | 2026-07-27 | nnunley | feat: per-package //lg:native registrar surface (migrate corefns) | #627, #639, #641 | letgo-nnunley-commit-convention, letgo-nnunley-native-hoist-stack |
| [#641](https://github.com/nooga/let-go/pull/641) | PR | merged | 2026-07-27 | nnunley | feat(build): provenance dependency manifest + selective regeneration | #627, #639, #640, #649, #727 | feedback-unwrap-bold-lead-ins, letgo-596-lg-compile-plan, letgo-generated-sums-workstream |
| [#649](https://github.com/nooga/let-go/pull/649) | PR | merged | 2026-07-30 | nnunley | perf(ir/lower): tail-call fusion — :return of a single-use :call → TAIL_CALL | #641, #644, #650, #719, #733 | letgo-boundary-abi-program |
| [#650](https://github.com/nooga/let-go/pull/650) | PR | merged | 2026-07-30 | nnunley | perf(ir): retain *runtime-defn-ir-cache* for only the current ns | #649 | letgo-nnunley-commit-convention |
| [#653](https://github.com/nooga/let-go/pull/653) | PR | merged | 2026-07-30 | mparrett | fix(aot): register a boxed override for typed-return fns (#554) | #554 | cljgo-benchmark-arms-race, feedback-go-pr-prepush-gate |
| [#661](https://github.com/nooga/let-go/pull/661) | PR | merged | 2026-07-31 | mparrett | fix(ir): treat a return-hinted arity vector as one arity (#598) | #598, #599, #662 | letgo-599-typed-returns, letgo-aot-return-hint-findings |
| [#662](https://github.com/nooga/let-go/pull/662) | PR | merged | 2026-07-31 | mparrett | feat(ir): seed self-recursive calls from a declared return type (#599) | #598, #599, #661 | letgo-599-typed-returns |
| [#666](https://github.com/nooga/let-go/pull/666) | PR | merged | 2026-08-01 | nnunley | refactor(ir): consolidate function-needs-rt? via per-op contribution rules |  | letgo-nnunley-commit-convention |
| [#681](https://github.com/nooga/let-go/pull/681) | PR | merged | 2026-08-05 | nnunley | test(parity): gate complete-corpus strict capability and engine output | #660 |  |
| [#735](https://github.com/nooga/let-go/pull/735) | PR | merged | 2026-08-12 | mparrett | feat(aot): embed the AOT compile driver as the lg.compiler namespace | #425, #502, #596, #781 | feedback-falsify-your-regression-test, feedback-read-reviewer-corrections-before-architecture-pages, letgo-596-lg-compile-plan |
| [#741](https://github.com/nooga/let-go/pull/741) | PR | merged | 2026-08-13 | mparrett | refactor(build): extract the generated-module scaffolding into pkg/gomod | #596, #97 | feedback-verify-status-before-acting, letgo-596-lg-compile-plan |

## Startup, footprint & targets

Start here: #503 (footprint & constrained targets epic)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [#303](https://github.com/nooga/let-go/pull/303) | PR | merged | 2026-06-22 | mparrett | feat(lg): add -cpuprofile and -memprofile flags | #304 |  |
| [#331](https://github.com/nooga/let-go/pull/331) | PR | merged | 2026-06-24 | nnunley | feat(lg): LG_CPUPROFILE/LG_MEMPROFILE env fallback for profiling builds |  |  |
| [#356](https://github.com/nooga/let-go/pull/356) | PR | merged | 2026-06-29 | nnunley | perf(startup): recover cold-start regression (16ms → 5.1ms) | #357, #360, #503 | ir-compile-bytecode-vs-native, letgo-core-boot-unify-520 |
| [#360](https://github.com/nooga/let-go/pull/360) | PR | closed | 2026-06-29 | nnunley | perf(diagnostics): env-gated startup decode + lookup stats | #356 |  |
| [#390](https://github.com/nooga/let-go/pull/390) | PR | closed | 2026-07-05 | mparrett | go.mod: lower toolchain floor to go 1.24 |  | letgo-toolchain-floor |
| [#392](https://github.com/nooga/let-go/pull/392) | PR | open | 2026-07-05 | nnunley | glplat: minimal GL platform layer (experiment) — GLFW/OpenGL backend, font primitives, scr | #744, #874 | letgo-744-glplat-default-deps-gate, letgo-glplat-audio-spike, letgo-glplat-ebiten-backend-spike |
| [#424](https://github.com/nooga/let-go/pull/424) | PR | merged | 2026-07-09 | mparrett | Runtime-only build: execute precompiled bytecode, no compiler linked | #425, #503, #652 | letgo-aot-split, letgo-core-boot-unify-520, lgb-compression-lgbz |
| [#502](https://github.com/nooga/let-go/pull/502) | PR | merged | 2026-07-14 | mparrett | feat(lgbgen): compress the embedded core bundle (default off) | #425, #503, #652, #735 | lgb-compression-lgbz |
| [#503](https://github.com/nooga/let-go/issues/503) | issue | open | 2026-07-14 | mparrett | Epic: Footprint &amp; constrained targets | #356, #424, #425, #464, #502, #522, #652 | lgb-compression-lgbz |
| [#522](https://github.com/nooga/let-go/pull/522) | PR | merged | 2026-07-16 | mparrett | feat: TinyGo support: small-footprint WASM and native builds | #464, #503, #544, #581, xsofy#192 | ecosystem-health-audit-2026-07, letgo-tinygo-pr522-round2, xsofy-determinism-hash-width |
| [#601](https://github.com/nooga/let-go/pull/601) | PR | merged | 2026-07-21 | mparrett | feat(scripts): lgbdump.lg — canonical .lgb dump for diffing bundles | #558, #580 | letgo-lgbdump-void-strip |
| [#607](https://github.com/nooga/let-go/issues/607) | issue | open | 2026-07-21 | nnunley | AOT lower-vm: embedded VM-fallback bundle rejected by its own runtime — `unsupported capab | #425, #596, #608 | cljgo-benchmark-arms-race, letgo-capmask-skew-607 |
| [#608](https://github.com/nooga/let-go/pull/608) | PR | merged | 2026-07-21 | mparrett | feat(bytecode): actionable hint on capability-mask reject | #607 | feedback-verify-status-before-acting, letgo-capmask-skew-607 |
| [#652](https://github.com/nooga/let-go/issues/652) | issue | open | 2026-07-30 | mparrett | AOT binaries link the entire core — every binary sits on a ~13 MB floor | #424, #425, #502, #503, #658 | cljgo-benchmark-arms-race, feedback-read-reviewer-corrections-before-architecture-pages, letgo-652-binary-floor-nohttp |
| [#658](https://github.com/nooga/let-go/pull/658) | PR | merged | 2026-07-31 | mparrett | build: add `lg_no_http` to drop `net/http` from the runtime (#652) | #596, #652 | letgo-652-binary-floor-nohttp |
| [#744](https://github.com/nooga/let-go/pull/744) | PR | open | 2026-08-14 | mparrett | glplat: Ebitengine backend behind -tags glplat_ebiten (stacked on #392) | #392, #874 | letgo-744-glplat-default-deps-gate, letgo-glplat-audio-spike, letgo-glplat-ebiten-backend-spike |
| [#781](https://github.com/nooga/let-go/pull/781) | PR | merged | 2026-08-23 | nnunley | perf(bytecode): compact lazy var metadata | #684, #735, #780 | letgo-generated-sums-fake-conflicts, letgo-wiki-population-workstream |
| [#859](https://github.com/nooga/let-go/pull/859) | PR | merged | 2026-09-12 | mparrett | fix(vm): make Int 64 bits wide on every host | #860, xsofy#192 | feedback-pulse-claim-drops-notes, letgo-aot-tinygo-lowerer-int64, letgo-ci-no-runs-traps |
| [#860](https://github.com/nooga/let-go/pull/860) | PR | merged | 2026-09-12 | mparrett | fix(rt): register the xxh3 namespace on TinyGo wasm builds | #859, xsofy#192 | letgo-int64-probe-2026-09-11 |
| [#874](https://github.com/nooga/let-go/pull/874) | PR | open | 2026-09-13 | mparrett | docs(design): propose the glplat host-capability seam and backend contract | #392, #744 | letgo-744-glplat-default-deps-gate |

## xsofy: render perf

Start here: xsofy#147 (render emit performance epic)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [xsofy#108](https://github.com/nooga/xsofy/pull/108) | PR | merged | 2026-07-01 | mparrett | perf: gate :lights cache invalidation on real terrain mutation |  |  |
| [xsofy#145](https://github.com/nooga/xsofy/pull/145) | PR | merged | 2026-07-08 | mparrett | perf(render): elide redundant SGR escapes in the map render | xsofy#146, xsofy#147, xsofy#149 |  |
| [xsofy#146](https://github.com/nooga/xsofy/pull/146) | PR | merged | 2026-07-08 | mparrett | perf(render): skip frame-to-frame unchanged cells (appearance diff) | xsofy#145, xsofy#147, xsofy#149 |  |
| [xsofy#147](https://github.com/nooga/xsofy/issues/147) | issue | open | 2026-07-08 | mparrett | Epic: Render emit performance | xsofy#145, xsofy#146, xsofy#148, xsofy#149 |  |
| [xsofy#148](https://github.com/nooga/xsofy/pull/148) | PR | merged | 2026-07-08 | mparrett | tool: lighttest — interactive lighting + render-perf testbed | xsofy#147 |  |
| [xsofy#149](https://github.com/nooga/xsofy/pull/149) | PR | merged | 2026-07-08 | mparrett | perf(render): synchronized output (DEC 2026) across all frame renders | xsofy#145, xsofy#146, xsofy#147 | feedback-check-stack-before-delete-branch |
| [xsofy#180](https://github.com/nooga/xsofy/pull/180) | PR | open | 2026-07-25 | mparrett | Top-down perf: cull never-seen cells (22x), plus frame timing and two input fixes |  |  |

## xsofy: bench & determinism

Start here: xsofy#130 (native engine benchmark + shared xsofy.perf core)

| # | type | state | opened | author | title | related | notes |
|---|---|---|---|---|---|---|---|
| [xsofy#98](https://github.com/nooga/xsofy/issues/98) | issue | open | 2026-06-30 | mparrett | Balance: distributions shift check vs 2026-05-30 sweep |  |  |
| [xsofy#111](https://github.com/nooga/xsofy/pull/111) | PR | closed | 2026-07-02 | mparrett | Native engine benchmark + shared xsofy.perf core |  |  |
| [xsofy#125](https://github.com/nooga/xsofy/issues/125) | issue | open | 2026-07-03 | mparrett | Dungeon generation: performance profiling + tuning legibility |  |  |
| [xsofy#130](https://github.com/nooga/xsofy/pull/130) | PR | merged | 2026-07-05 | mparrett | bench: native engine benchmark + shared xsofy.perf core |  |  |
| [xsofy#153](https://github.com/nooga/xsofy/pull/153) | PR | merged | 2026-07-11 | mparrett | feat(console): (replay) + (bench) commands (Layer 2) |  |  |
| [xsofy#186](https://github.com/nooga/xsofy/pull/186) | PR | merged | 2026-08-12 | mparrett | bench: sample turns in microseconds instead of whole milliseconds |  |  |
| [xsofy#192](https://github.com/nooga/xsofy/pull/192) | PR | closed | 2026-09-06 | mparrett | feat(hash): back the seed hash with murmur3 so the game builds for TinyGo | #522, #859, #860 | gh-actions-diagnosis-traps, letgo-int64-probe-2026-09-11, letgo-pure-xxh3-aot-tinygo-probe |
| [xsofy#194](https://github.com/nooga/xsofy/pull/194) | PR | open | 2026-09-12 | mparrett | perf(hash): encode salt terms into an accumulator |  | detpath-alloc-analysis-2026-09-12 |
