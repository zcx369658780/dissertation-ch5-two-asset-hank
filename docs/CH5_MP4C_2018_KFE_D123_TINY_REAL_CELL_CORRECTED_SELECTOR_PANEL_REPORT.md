# Chapter 5 MP4C 2018 KFE D1-D3 tiny real-cell corrected selector panel

Date: 2026-09-16

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Verdict

`FAIL__POST_FREEZE_SELECTOR_D2_ZERO_TOLERANCE_MISMATCH__STOPPED_WITHOUT_RETRY`

The exact panel identity was recovered and frozen, and the first real cell returned
one selected admissible D1/D3 policy that also passed the D2 assembler check. The
second selector evaluation returned, but its post-selection D2 check rejected a
positive upper-`b` drift of `2.162339589068668e-16`. The selector had admitted that
residual under its prospective floating-point equality bound, whereas the accepted
D2 assembler rejects every strictly outward closed-face drift at zero sign
tolerance. This is a frozen scientific-code contract mismatch, not evidence about
the remaining eight cells and not an adverse-numerics retry opportunity.

Execution stopped immediately. No selector/scientific-code file was patched, no
cell was repeated, and cells 3--10 were not called. Therefore the required
ten-cell scientific PASS is not established.

## Git and authority identity

- Fresh-start live `origin/main`: `c525d6671519f6a62608ba3b02211010f2327e56`.
- Branch: `codex/ch5-mp4c-2018-kfe-d123-tiny-real-cell-corrected-selector-panel-20260916`.
- Corrected authority: `CH5_MP4C_2018_KFE_D123_OWNER_ADOPTED_20260916`.
- Candidate SHA is assigned by the final commit and verified by remote readback;
  the commit cannot embed its own SHA without changing that SHA.

## Exact panel identity and provenance

Rows are zero-based and use the accepted `(b,a,z)` F-order mapping. No cell was
remapped to the later `I=20,J=160` practical grid.

| Ordinal | Panel object | Source row | `(b_index,a_index,z_index)` | F-flat | Source SHA-256 | Execution |
|---:|---|---:|---|---:|---|---|
| 1 | MATLAB M143_FINAL corner | 0 | `(0,0,0)` | 0 | `4EAA6695A07F8C32B42515631D1AF95AD48190990627934D7895EC7EFC9CCE63` | completed |
| 2 | MATLAB M143_FINAL corner | 19 | `(19,0,0)` | 19 | same M143 source | selector called; D2 terminal failure |
| 3 | MATLAB M143_FINAL corner | 380 | `(0,19,0)` | 380 | same M143 source | not executed after stop |
| 4 | MATLAB M143_FINAL corner | 399 | `(19,19,0)` | 399 | same M143 source | not executed after stop |
| 5 | MATLAB M143_FINAL corner | 400 | `(0,0,1)` | 400 | same M143 source | not executed after stop |
| 6 | MATLAB M143_FINAL corner | 419 | `(19,0,1)` | 419 | same M143 source | not executed after stop |
| 7 | MATLAB M143_FINAL corner | 780 | `(0,19,1)` | 780 | same M143 source | not executed after stop |
| 8 | MATLAB M143_FINAL corner | 799 | `(19,19,1)` | 799 | same M143 source | not executed after stop |
| 9 | MATLAB trajectory step52 | 799 | `(19,19,1)` | 799 | `AA9DB0664FB0476AFA097C9716AAC88EB56F5779EC1A1346EEA27ED406D12FA3` | not executed after stop |
| 10 | MATLAB trajectory step57 | 379 | `(19,18,0)` | 379 | `81AC0E3F06E8D268C05E4E78B67F64FD6351FC55924282DB4DD44FF99EA77DDA` | not executed after stop |

The M143, step52 and step57 byte counts are respectively `213246`, `213238` and
`211918`. All match `reports/call725_boundary_generator_repair_spec_20260907/consumed_inputs.json`.
The shared scalar binding is `2732` bytes with SHA-256
`A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`.
The pre-execution freeze receipt records every consumed state, post-boundary and
raw directional derivative, effective return, wage, rate and D3 parameter for all
ten cells.

## Selector implementation map

The implementation is confined to the accepted isolated namespace:

- `panel.py` binds the exact three accepted MAT objects, verifies byte/hash
  receipts, resolves zero-based F-order rows, and constructs the frozen cell inputs.
- `selector.py` enumerates at most four geometric face-active sets and three
  transfer regimes, uses D3's `s(a)=max(a,a_bar)` cost/subgradient, checks derivative
  direction, domain, primal feasibility, multipliers, complementarity, KKT and
  Hamiltonian comparison, and counts at most one scalar root per active-set/regime.
- `run_panel.py` freezes scientific-code hashes before call 1, executes cells in
  preregistered order, persists per-cell/cumulative receipts, invokes the accepted
  D2 total-drift assembler only as a post-selection admissibility check, and stops
  on an unhandled post-freeze defect.

There is no generic optimizer, derivative floor, transfer cap, clipping, projection,
damping, drift repair, tolerance fitting or production-path import. Prospective
residual bounds use a fixed gamma-n arithmetic form. The failure demonstrates that
an equality residual admitted by that bound cannot be passed unchanged into D2's
exact closed-face sign contract.

## Synthetic preflight

Before the first real selector call:

- RED: the focused test initially failed at collection because the new selector
  API did not exist.
- GREEN/final focused command: the new selector/panel tests plus the accepted
  D1-D3, call725 repair-spec and generator contract tests returned `29 passed in
  0.91s`.
- `py_compile`: PASS for every file under the corrected-diagnostic namespace and
  the new focused test.
- `git diff --check`: PASS.
- Panel binding test: 10/10 identities resolved and all accepted hashes matched;
  this test read arrays but did not call the real selector.

Synthetic selector evaluations are tests, not real-cell scientific evaluations.

## Per-cell scientific evidence

### Cell 1 — M143_FINAL row0 `(0,0,0)`

Outcome: `SELECTED_ADMISSIBLE`. Four scalar-root invocations were consumed across
the 4 active sets x 3 regimes; root failures in rejected candidates were retained
and not retried.

| Object | Value |
|---|---:|
| `c` | `8.294857173613904` |
| `l` | `0.714175777691523` |
| `d` | `5.677200700701319e-06` |
| cost | `3.279832786611368e-05` |
| `g_b` | `0.754636518344415` |
| `g_a` | `5.677200700701319e-06` |
| utility | `-0.1426712450267497` |
| Hamiltonian | `-0.1317024055105844` |
| `q_b` | `0.014533900246829623` |
| `q_a` | `0.181011027601961` |
| transfer branch | positive |
| active constraints | none; both lower faces slack/inward |
| lower-`b` slack | `0.754636518344415` |
| lower-`a` slack | `5.677200700701319e-06` |
| multipliers/complementarity residuals | all `0` |
| transfer KKT residual | `0` |

The D2 assembler accepted the selected total drifts. Minimum offdiagonal was
`1.0786681331332507e-05`; diagonal construction error was `0`; `max(abs(Q@1))`
was `7.846235597006035e-17` below the prospective arithmetic bound
`2.7288969855846118e-15`; liquid/illiquid coordinate errors were
`1.1102230246251565e-16` and `0`.

### Cell 2 — M143_FINAL row19 `(19,0,0)`

The second real selector call occurred and brought cumulative counts to two selector
evaluations and eight scalar-root invocations. Before its selector result was
persisted, the immediate D2 check raised `ClosedFaceOutwardDriftError` at the
upper-`b` face for `g_b=2.162339589068668e-16`. The terminal receipt preserves the
cell identity, all bound inputs, exception type and exact value. Because persistence
was sequenced after the D2 check, the full second selector comparison set was not
durably written; it is `UNAVAILABLE_AFTER_FROZEN_EXECUTION_FAILURE` and was not
reconstructed by a repeated call.

Outcome: `SCIENTIFIC_CODE_DEFECT_OR_UNHANDLED_NUMERICS_AFTER_FREEZE`.

### Cells 3--10

Outcome: `NOT_EXECUTED_AFTER_POST_FREEZE_STOP`. No scientific inference is made
for these cells.

## D1/D2/D3 findings

- D1/D3: cell 1 has one selected KKT-consistent, direction-consistent, jointly
  closed-face-feasible policy. Cell 2 cannot be certified because the D2 handoff
  exposed a sign-contract mismatch before its complete receipt was persisted.
- D2: cell 1 passes conservative total-drift assembly. Cell 2 is rejected exactly
  as the accepted D2 contract requires; no outward drift was clipped or repaired.
- Ten-cell acceptance: FALSE. A result from one cell cannot be generalized to the
  eight unexecuted cells.

## Frozen-code-after-first-call proof

`pre_execution_freeze.json` records SHA-256 for all nine Python files in the
corrected-diagnostic namespace before call 1. A read-only comparison after the
terminal stop returned `matches=true` for every file, including selector
`6EEA855DA34F995249A7E0529872CFE3A5FC463B4A07312020DBC70FADA8886D`,
panel binder `F532BD92A5022274DCDE23CD5754C0E38E8CD98E13004F06BD42195DD396A786`,
and runner `08B2E824EDEC4DBC3AEB37943979A21E24592CD35CB41FEA60984DF047D40924`.
No scientific-code write occurred after call 1.

## Exact call ledger

| Category | Calls |
|---|---:|
| corrected real-cell selector evaluations | 2 |
| scalar root invocations | 8 |
| adverse-numerics retries | 0 |
| HJB policy maps/iterations/direct solves | 0 |
| KFE solves | 0 |
| outer loop | 0 |
| firm block | 0 |
| wage/return recalculation | 0 |
| MATLAB processes | 0 |
| GE | 0 |
| annual/downstream production | 0 |
| shock | 0 |
| IRF | 0 |
| Results | 0 |

The two attempted selector evaluations both count. The D2 sparse assembler check
is the task-authorized pure post-evaluation admissibility check, not a KFE solve.

## Evidence

Evidence root:
`reports/ch5_mp4c_2018_kfe_d123_tiny_real_cell_selector_panel_20260916/`.

The fail-closed manifest seals four entries, `45259` bytes total: the complete cell1
receipt, cell2 terminal receipt, exact ledger, and pre-execution freeze. No
`panel_results.json` or normal post-execution receipt exists because the runner
stopped at the frozen defect instead of pretending the panel completed.

## Limitations and next gate

This failure is not grid instability, HJB/KFE nonconvergence, recalibration evidence,
or a finding about all ten cells. It establishes only that the frozen selector-to-D2
handoff did not implement one exact closed-face sign contract consistently and that
the failure receipt ordering did not preserve the full second selector result.

HJB convergence, a KFE stationary density, production replacement, GE/annual/shock/
IRF validity and Results eligibility remain unestablished. Results eligibility is
`FALSE`.

The only next gate is independent Reviewer disposition of this candidate and, if
explicitly authorized in a fresh exact task, repair of the selector/D2 equality-sign
contract plus durable pre-D2 selector receipt ordering before any new panel run.
This task publishes no successor and authorizes no retry.

## Publication readback and worktree status

The exact candidate SHA, non-force remote readback and final clean-worktree status
are reported in the Builder handoff after commit/push; they cannot be embedded in
the commit without changing the object being identified.
