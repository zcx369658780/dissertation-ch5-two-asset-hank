# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`CORRECTED_HJB_OPTION_A_LOWER_A_KINK_REPAIR_ACCEPTED__CELL5_LIQUID_DIRECTION_CONFLICT_ATTRIBUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoints

Owner-adopted D1/D2/D3 corrected diagnostic bundle、isolated static implementation、historical ten-cell fail-closed selector evidence、failed-cell algebraic attribution、corrected-HJB one-step design/input binding，以及 Option A seed adoption均继续有效。Source-faithful/production paths remain frozen。

## Option A reexecution checkpoint

Builder candidate `054ba005a351d279f98b243bd2891225872ba86e` is accepted as valid fail-closed evidence by `docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_REPAIR_OPTION_A_REEXECUTION_FAIL_CLOSED_ACCEPTANCE_20260916.md`.

The authorized active lower-`a` zero-kink multiplier omission is repaired. Fresh Option A execution confirms Cells 0–4 are `SELECTED_ADMISSIBLE`, including Cell 0 with `q_a=lambda_a=0.020741942377698892` and marker `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`.

The first new failure occurs at F-order flat index 5, coordinate `(5,0,0)`, state `b=-0.1578947368421053,a=0,z=.8`. The repaired lower-a zero-kink candidates are valid on the a side, but the frozen liquid finite-difference branches cross direction:
- backward liquid derivative gives `g_b=3.3967923469887262>0`;
- forward liquid derivative gives `g_b=-0.009203423814039269<0`.
Both are rejected by the unchanged derivative-direction contract. This does not yet establish whether the corrected contract is incomplete at an interior liquid switching point or whether the Option A derivative state is structurally incompatible.

Runtime: 6 real selector evaluations, 4 scalar roots, retries=0, D2=0, direct HJB solve=0, KFE/MATLAB/downstream=0.

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_CELL5_LIQUID_DIRECTION_SWITCH_ALGEBRAIC_ATTRIBUTION_ZERO_SCIENCE_20260916.md`.

This task is zero science. It must determine from frozen equations/source/receipts whether Cell 5 requires an already-authorized zero-drift/switching Hamiltonian branch, whether the selector omitted a mathematically legal interior liquid branch, or whether the frozen Option A derivative pair is itself incompatible with the current corrected selector contract. No selector/root/HJB/KFE/MATLAB/model call, repair, rerun, tolerance/floor/cap/grid/calibration change is authorized.
