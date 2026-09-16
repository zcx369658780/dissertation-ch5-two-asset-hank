# Chapter 5 MP4C 2018 KFE D1-D3 active-equality canonicalization and ten-cell reexecution

Date: 2026-09-16

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Verdict

`FAIL__ONE_OR_MORE_PANEL_CELLS_NOT_SELECTED_ADMISSIBLE`

The two authorized implementation defects were repaired before scientific
execution. Active equalities now retain their raw floating residual and
prospective arithmetic bound while handing exact `0.0` to strict D2 only when the
face is active and the raw residual is inside that bound. Complete selector
comparison receipts are durably written before D2.

The fresh exact ten-cell panel then ran once. Seven cells returned one selected
admissible policy and passed strict D2. Cells 4, 8 and 10 returned
`NO_ADMISSIBLE_POLICY`; D2 was therefore not run for those cells. The panel is not
a scientific PASS. No cell was repeated and no post-freeze scientific code was
changed.

## Authority and Git identity

- Fresh-fetched live `origin/main`: `87b445c5a656eaca5146b55bbdde7ab24f70574d`.
- Branch: `codex/ch5-mp4c-2018-kfe-d123-selector-active-equality-reexecution-20260916`.
- Scientific-code freeze commit: `1ec6a0b6972db18edee18c2852caa589afc8a047`.
- Authority: `CH5_MP4C_2018_KFE_D123_OWNER_ADOPTED_20260916`.
- The final evidence/report candidate SHA and remote readback are reported in the
  Builder handoff because a commit cannot embed its own SHA without changing it.

## Repair map

- `selector.py`: records `ActiveEqualityReceipt(face, raw_residual,
  arithmetic_bound, canonical_drift, marker)`; canonicalizes only selected active
  face equalities inside the unchanged prospective bound; rejects an active
  residual outside the bound; preserves inactive/slack drift; records both
  canonical-policy Hamiltonian and raw-arithmetic Hamiltonian.
- `run_panel.py`: uses the fresh evidence root, persists cell identity, freeze
  identity, full selector result/comparison set, counters and budget
  postconditions before D2; D2 success or exception is appended afterward.
  Early-stop paths retain post-freeze hashes, terminal results, ledger and
  manifest.
- Focused tests cover upper-`b` and upper-`a` active equality, outside-bound
  rejection, inactive upper-face `nextafter(0,+1)` strict D2 rejection, unchanged
  lower-bound identity, and forced D2 failure after durable selector receipt.

D2's zero-tolerance outward-face rejection was not changed. No generic small
drift rule exists and no inactive/slack face is canonicalized.

## Synthetic preflight

Before the first real selector call:

- focused selector/receipt/D1-D3/call725/generator command: `35 passed in 1.19s`;
- `py_compile`: PASS for the corrected-diagnostic namespace and changed tests;
- `git diff --check`: PASS;
- exact panel binder test: 10/10 identities and accepted hashes passed without a
  real selector evaluation;
- independent read-only review: GO for the single frozen panel execution.

Synthetic tests consumed zero real selector evaluations and zero scientific
roots.

## Exact panel and outcomes

Rows are zero-based `(b,a,z)` indices with F-order flat identity. The panel was
not remapped to the later practical grid.

| Cell | Object / row | Index | Outcome | Roots | Selected active faces | D2 |
|---:|---|---|---|---:|---|---|
| 1 | M143_FINAL / 0 | `(0,0,0)` | `SELECTED_ADMISSIBLE` | 4 | none | PASS |
| 2 | M143_FINAL / 19 | `(19,0,0)` | `SELECTED_ADMISSIBLE` | 4 | upper-b | PASS |
| 3 | M143_FINAL / 380 | `(0,19,0)` | `SELECTED_ADMISSIBLE` | 4 | upper-a | PASS |
| 4 | M143_FINAL / 399 | `(19,19,0)` | `NO_ADMISSIBLE_POLICY` | 0 | none selected | NOT RUN |
| 5 | M143_FINAL / 400 | `(0,0,1)` | `SELECTED_ADMISSIBLE` | 4 | none | PASS |
| 6 | M143_FINAL / 419 | `(19,0,1)` | `SELECTED_ADMISSIBLE` | 4 | upper-b | PASS |
| 7 | M143_FINAL / 780 | `(0,19,1)` | `SELECTED_ADMISSIBLE` | 4 | upper-a | PASS |
| 8 | M143_FINAL / 799 | `(19,19,1)` | `NO_ADMISSIBLE_POLICY` | 0 | none selected | NOT RUN |
| 9 | MATLAB step52 / 799 | `(19,19,1)` | `SELECTED_ADMISSIBLE` | 4 | upper-a | PASS |
| 10 | MATLAB step57 / 379 | `(19,18,0)` | `NO_ADMISSIBLE_POLICY` | 3 | none selected | NOT RUN |

The source identities remained the accepted M143/step52/step57 hashes
`4EAA6695...CCE63`, `AA9DB066...2FA3`, and `81AC0E3F...77DDA`; the scalar
binding remained `A40D088C...8F6`.

## Active-equality evidence

| Cell | Face | Raw residual | Prospective bound | Final drift | Marker |
|---:|---|---:|---:|---:|---|
| 2 | upper-b | `2.162339589068668e-16` | `2.13729558062671e-13` | `0.0` | `ACTIVE_EQUALITY_CANONICAL_ZERO` |
| 3 | upper-a | `0.0` | `2.58412176102066e-13` | `0.0` | `ACTIVE_EQUALITY_CANONICAL_ZERO` |
| 6 | upper-b | `1.2854029906445e-15` | `3.10580230666064e-13` | `0.0` | `ACTIVE_EQUALITY_CANONICAL_ZERO` |
| 7 | upper-a | `0.0` | `3.80743207161796e-13` | `0.0` | `ACTIVE_EQUALITY_CANONICAL_ZERO` |
| 9 | upper-a | `0.0` | `1.39537359665428e-11` | `0.0` | `ACTIVE_EQUALITY_CANONICAL_ZERO` |

Every receipt also preserves the raw and canonical Hamiltonian fields. All five
active equalities were inside the unchanged prospective bound. No slack face was
canonicalized.

## Selected-policy and D2 summary

| Cell | `c` | `l` | `d` | `g_b` | `g_a` | Hamiltonian |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 8.2948571736139 | 0.714175777691523 | 5.67720070070132e-06 | 0.754636518344415 | 5.67720070070132e-06 | -0.131702405510584 |
| 2 | 9.02612392036544 | 0.690443530631453 | 5.09078156843646e-06 | 0.0 | 5.09078156843646e-06 | -0.128844663752761 |
| 3 | 7.05167796065541 | 0.762099528883245 | -0.81 | 3.27386849591854 | 0.0 | -0.108624956836515 |
| 5 | 9.04084698388255 | 0.760353775704991 | 6.33282086290456e-06 | 6.67384586105094 | 6.33282086290456e-06 | -0.0611641710466671 |
| 6 | 13.6103973440818 | 0.645581434770132 | 1.3251454612951e-05 | 0.0 | 1.3251454612951e-05 | -0.0855370334233056 |
| 7 | 9.43555781852702 | 0.747467513975478 | -0.81 | 6.67488729170585 | 0.0 | -0.0600755698436259 |
| 9 | 329.031790466325 | 0.180552792643322 | -0.81 | -324.417798454515 | 0.0 | -0.00604159518385748 |

For all seven selected cells, D2 minimum offdiagonals were nonnegative,
diagonal construction error was `0`, `max(abs(Q@1))` was at or below its
prospective arithmetic bound, and coordinate errors were at floating-point scale.
Cells 4, 8 and 10 had no selected drift, so D2 correctly reported
`NOT_RUN_NO_SELECTED_POLICY`.

## Fail-closed cells

Cells 4 and 8 each evaluated 12 candidates over four active sets and three
transfer regimes. No scalar root was invoked. Their rejection receipts contain:

- `q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR` (4 candidates);
- `UPPER_B_ACTIVE_HAS_NO_Q_B_POSITIVE_MULTIPLIER_DOMAIN` (4);
- `ACTIVE_A_EQUALITY_NOT_ZERO_KINK` (2);
- `ACTIVE_A_EQUALITY_WRONG_TRANSFER_SIGN` (2).

Cell 10 evaluated seven candidates over two active sets and six regime attempts,
with three converged roots. Its comparison set retained derivative-direction,
transfer-KKT/sign, and upper-b primal-feasibility rejections; none was admissible.
These are panel-local fail-closed selector findings. They do not establish HJB or
KFE behavior and do not authorize a derivative floor, cap, new tolerance,
calibration change or retry.

## Receipt ordering, freeze, manifest and ledger

Each cell receipt records
`SELECTOR_RECEIPT_DURABLE_BEFORE_D2`, the complete comparison set, cell and
scientific-code freeze identity, cumulative counters, and five explicit budget
postconditions. All budget postconditions are true.

`post_execution_freeze_check.json` reports that all corrected-diagnostic Python
hashes match the pre-execution freeze. The manifest seals 14 non-manifest JSON
entries totaling `461702` bytes; independent readback verified every entry byte
count and SHA-256.

| Category | Calls |
|---|---:|
| corrected real-cell selector evaluations | 10 |
| scalar root invocations | 31 |
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

## Exact changed paths

Implementation and tests:

- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/run_panel.py`
- `tests/test_mp4c_2018_kfe_d123_tiny_real_cell_selector.py`
- `tests/test_mp4c_2018_kfe_d123_receipt_ordering.py`

Evidence paths under
`reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916/`:

- `cell_01_M143_corner_000.json`
- `cell_02_M143_corner_019.json`
- `cell_03_M143_corner_380.json`
- `cell_04_M143_corner_399.json`
- `cell_05_M143_corner_400.json`
- `cell_06_M143_corner_419.json`
- `cell_07_M143_corner_780.json`
- `cell_08_M143_corner_799.json`
- `cell_09_MATLAB_step52_row799.json`
- `cell_10_MATLAB_step57_row379.json`
- `pre_execution_freeze.json`
- `post_execution_freeze_check.json`
- `panel_results.json`
- `execution_ledger.json`
- `manifest.json`

This report is the only documentation path added by the task.

## Limitations and next gate

The authorized repairs worked for the previously blocked Cell 2 handoff and for
all selected active equalities. The panel nevertheless fails because three cells
have no admissible selected policy. This does not establish HJB convergence, KFE
existence/nonnegativity/uniqueness, production replacement, GE/annual/shock/IRF
validity, or Results eligibility. Results eligibility remains `FALSE`.

The only next gate is independent Reviewer disposition of this fail-closed
candidate. This Builder task does not merge main, publish a successor, repair the
three failed cells or rerun the panel.
