# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`OPTION_A_FIRST_CELL_FAIL_CLOSED_ACCEPTED__LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_REEXECUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoints

Owner-adopted D1/D2/D3 corrected diagnostic bundle、isolated static implementation、historical ten-cell fail-closed evidence、Cells 4/8/10 algebraic attribution、corrected-HJB one-step design/input binding，以及 Owner 对 Option A seed 的采用均继续有效。Source-faithful/production paths remain frozen。

## Newly accepted Option A first-cell evidence

Builder candidate `ef05a6c52c3cbe42d8e5404b6f51f0aa7c635d9e` is accepted as valid fail-closed evidence by `docs/CH5_MP4C_2018_KFE_D123_OPTION_A_FIRST_CELL_SELECTOR_OMISSION_ACCEPTANCE_20260916.md`.

The run stopped at F-order Cell `(0,0,0)` after one selector evaluation / four roots, with D2=0 and HJB solve=0. The failure is not accepted as evidence against Option A or corrected-HJB existence.

Reviewer identified a specific selector omission under the already adopted KKT law: for active lower-`a` at `a=0` and zero transfer, the selector forced `q_a=p_a` and therefore `lambda_a=0`, instead of allowing the legal lower-face multiplier set `q_a=p_a+lambda_a`, `lambda_a>=0`, intersected with the D3 kink interval `q_a/q_b in [1-chi_0,1+chi_0]`.

For the failed Cell 0, `p_a=0`, `q_b=0.023046602641887657`, so the kink interval `[0.020741942377698892,0.025351262906076425]` has a nonempty intersection with `q_a>=0`. This is a selector implementation/enumeration defect, not a new economic law or seed failure.

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_20260916.md`。

The only authorized behavior repair is the active lower-`a` zero-kink multiplier representation. Slack faces, upper-`a`, nonzero-transfer branches, D2 zero-tolerance semantics, seed, grid, calibration and production paths must remain unchanged.

After synthetic preflight and code freeze, rerun Option A from Cell 0 with a fresh one-map budget: <=800 real selector evaluations, <=264 scalar roots, D2<=1 only after all 800 cells pass, sparse direct HJB solve<=1 only after D2 passes, retries=0. KFE/MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results remain 0.
