# MP4C call-725 same-input multi-iteration trajectory

Date: 2026-09-07. Task: `CH5_MP4C_CALL725_MULTI_ITERATION_TRAJECTORY`.

**Diagnostic completion: COMPLETE.**
**Scientific verdict: TRAJECTORY_DIVERGENCE_WITH_COMMON_STATE_PARITY_PASS.**
Convergence is separate: MATLAB converged at update 143; Python did not converge
within 500 updates. Neither converged by the unchanged production ceiling of 100.
This report is a Builder submission, not Reviewer acceptance or annual/Results evidence.

## Authority and actual workspace

Verified remote: `git@github.com:zcx369658780/dissertation-ch5-two-asset-hank.git`.
After fetch, live main was `373264625f0f9580575cda5a36d7a70b371a040b` and the
current rule index designated this exact task. The branch was created from that
fresh main in `D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`:
`codex/ch5-call725-multi-iteration-trajectory-20260907`.
The accepted first-iteration and docs-sync branches were retained. No original
main-checkout files, its 70 untracked files, or Zotero repository files were touched.

Evidence root: `D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001`.
The four scientific invocation subdirectories are `matlab_trajectory`,
`python_trajectory`, `matlab_replay`, and `python_replay`. Each has its own
worker ledger and durable stage outputs, and a sibling process receipt/log and
exact runtime-source snapshot. Large MAT/NPZ outputs remain outside Git.

## Frozen computation and state schema

The authoritative initialization MAT and scalar binding were direct-loaded and
hash-verified against `1718984C…07BB81` and `A40D088C…4808F6`, respectively;
full identities are in `frozen_identities.json`. Python export blob remains
`9e7dc9556a2b76811e78f89999abecc045886106`; protected HJB and consumed MATLAB
FOC/cost helper hashes match the accepted contract. Launch revalidated these
identities, then copied byte-verified Python/FOC/cost dependencies into each
invocation snapshot. The Python import-root change binds that frozen snapshot.
No production export or protected source was edited.

The accepted one-step source-extracted wrappers supplied the scientific bodies.
Exact scientific-body comparisons pass after removing only the added ledger write
and indentation. Changes add the outer loop, per-step filenames, counters,
capture/stop handling, and remove unreachable post-loop work. Original scientific
expressions, operator assembly and direct solvers remain unchanged.

Only V is mutable loop-carried scientific state: `V=v; v=updated` in MATLAB,
`old=v1.copy()` in Python. `l0`, grids, switch matrix and scalar binding are fixed.
Derivatives, policies and operators are recomputed by the accepted evaluator each
step. Source attribution: Python export lines 524–559 and protected MATLAB HJB
loop lines 113–260, interpreted through the already accepted source-extracted
evaluator. `state_schema.json` records this mapping. All 643 completed trajectory
steps were checked: incoming V equals the previous saved V1 exactly, and immutable
arrays remain exact. No native initialization or extra post-loop policy evaluation ran.

Each trajectory stops on its original strict `statistic < 1e-7`, nonfinite/fatal
failure, or the diagnostic maximum 500. Updates 101 onward are explicitly marked
diagnostic continuation; production `maxit=100` was not changed.

## Earliest differences and shared-iteration coverage

Both fresh first steps match their corresponding accepted persisted first-step
evidence. The two fresh first steps also pass cross-language comparison.
All 143 iterations present on both sides were compared in causal stage order,
including downstream stages after the first discrepancy. MATLAB was not advanced
beyond its convergence point to match Python's longer trajectory.

| Event | First iteration | Evidence |
| --- | ---: | --- |
| Newly generated scientific object exceeds frozen bound | 2 | consumption, 519 material entries |
| Updated V1 exceeds frozen bound | 3 | 24 entries; max absolute difference `3.816946758661288e-13` |
| Incoming old/V0 exceeds frozen bound | 4 | inherited trajectory-state difference |
| Consumed categorical label differs | 24 | transfer label, one coordinate |
| Mathematical sparse support differs | 24 | BB, one support coordinate |

At iteration 2, incoming V and equivalent derivatives still pass the frozen
continuous bound; passing does not mean bitwise identity. Consumption's maximum
absolute difference is `1.3500311979441904e-11`, or `28.813768104363252` times its
frozen bound. The maximum occurs at zero-based `(b,a,z)=(10,8,1)`, physical
`(1.6842105263157894, 4.2105263157894735, 1.3)`.
Both select the backward liquid branch. Their consumed derivatives are
`0.0036797040769951063` and `0.003679704077001133`, differing by
`6.026863036412422e-15`. Pure arithmetic on these persisted operands,
`max(vb,1e-6)**(-1/2)`, reproduces consumption
`16.485174666484216` versus `16.485174666470716`.
The local absolute slope is about `2240.01`. This explains why a derivative
difference within the absolute machine bound can exceed the consumption bound.
Source locations are accepted MATLAB wrapper consumption lines 44–51 and frozen
Python `consumption_from_vb` lines 126–129 / branch use lines 273–300.

Raw-vb pre/post-boundary fields remain distinct: primary comparisons use
post-boundary vb, with defined raw interior quotient domains retained as diagnostics.
The five Python mask views come from consumed labels and are explicitly not
independently captured masks. Exact labels, shape/F-order, sparse support with
only exact stored zeros removed, and the unchanged `128*eps64` continuous rule
were used throughout. Sparse comparisons never expand operators into dense matrices.

## Conditional common-state replay

One matched replay pair was run from the exact MATLAB pre-step checkpoint for
iteration 2. Its saved `initial_value` was relabeled `v0`; `b`, `ah`, `z`, `l0`
were retained. The new common-state MAT was read back with exact array equality,
hashed, and loaded by both evaluators. Neither independent trajectory was reset
or overwritten. The replay executes exactly one update on each side.

All **38 cross-language field comparisons pass**, including exact incoming V,
consumed labels and equivalent branch views. Maximum scaled difference across
fields is `0.125`; no field exceeds 1. Consumption maximum absolute difference
is `3.552713678800501e-15`; V1 is `4.440892098500626e-15`.
Residual/backward-error diagnostics are finite on both sides.

This supports propagation/state-history sensitivity at the earliest observed
trajectory break. It does not establish that every later common-state step would
pass, nor prove complete multi-iteration algorithmic or economic equivalence.
No production formula repair is supported by this particular replay.

## Convergence and numerical diagnostics

| Language | Statistic at 100 | Final updates | Final statistic | Converged |
| --- | ---: | ---: | ---: | --- |
| MATLAB | `0.015407653120767195` | 143 | `1.0492009705487249e-8` | yes, diagnostic continuation only |
| Python | `0.23388538498461742` | 500 | `0.008617352704437531` | no |

All captured stage values remained finite. Per-step M/RHS/statistic identities
pass on both sides. Residuals were computed from stored M/RHS/vec_F(V1), without
condition-estimation or diagnostic solves. The largest normwise backward errors
are `1.9032196186959857e-16` (MATLAB) and `3.8469301515688204e-16` (Python).
These small backward errors do not establish convergence or economic admissibility.

Absolute residuals become large when intermediate operators are large:
MATLAB's peak residual is `0.0018557927401558622` at step 57
(`||M||inf=1.329422689765389e13`); Python's is `99888.39357064449` at step 32
(`||M||inf=7.935207415974971e20`). The corresponding backward errors are
`6.753710831286794e-17` and `5.652860284583403e-17`. Full extrema, scales,
warnings and step evidence are retained; finite values are not described as
well-conditioned. No regularization, tolerance change or solver substitution occurred.

## Actual budget and checks

| Language | Trajectory invocations / updates / solves | Common-state invocations / updates / solves | Total invocations / solves | Engineering retries |
| --- | --- | --- | --- | ---: |
| MATLAB | 1 / 143 / 143 | 1 / 1 / 1 | 2 / 144 | 0 |
| Python | 1 / 500 / 500 | 1 / 1 / 1 | 2 / 501 | 0 |

All four scientific processes exited 0. Replay `MAX_UPDATES` denotes its single
permitted update, not an attempt to converge. Historical calls remain consumed
in their original tasks. Native-init, KFE, distribution/aggregation, GE, annual,
R/PLM, shock/IRF and Results calls are zero in this task. MATLAB checkcode was one
static-only process, separate from the two scientific MATLAB invocations.

Six focused tests pass: scientific-body preservation on both sides, state/stop
and persistence order, Python parse/trace newline, exact synthetic MAT/sparse IO,
and sparse support checks that prohibit dense expansion. MATLAB checkcode exited 0.
An initial test selected the wrong serialization occurrence in the predecessor
source; its range was corrected before science. An initial read used the Windows
default text codec; explicit UTF-8 fixed it before science. Neither consumed
scientific budget. A read-only helper reviewed instrumentation/analysis code;
its advice is not scientific acceptance. No unrelated regression suite ran.

## Deliverables and next bounded question

Allowed changes consist of the trajectory wrapper/generator/launcher, sparse
analysis and postprocessing utilities, one focused test file, this report, and
small summaries under `reports/call725_multi_iteration_trajectory_20260907/`.
The finite manifest binds inputs, runtime snapshots, full local artifact inventory,
ledgers, comparisons and report. The final Git commit and remote branch readback
are returned after publication; main is not merged by Builder.

The next useful question is the later policy-switch/operator-growth propagation,
especially around the first categorical/support split at step 24, and why the
exact-initialization Python trajectory remains unconverged at 500. A future task
can prioritize stored evidence before authorizing another selected common-state
probe. This report does not authorize that task or a production change.
