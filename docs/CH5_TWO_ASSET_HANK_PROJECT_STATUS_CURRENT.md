# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`KFE_D123_FAILED_CELL_ATTRIBUTION_ACCEPTED__CORRECTED_HJB_ONE_STEP_DESIGN_BINDING_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoints

Owner-adopted D1/D2/D3 corrected diagnostic bundle and isolated static implementation remain accepted. Source-faithful/production paths remain frozen. The full ten-cell corrected-selector reexecution remains accepted as fail-closed evidence: Cells 1,2,3,5,6,7,9 selected admissible policies and passed strict D2; Cells 4,8,10 returned `NO_ADMISSIBLE_POLICY`.

## Newly accepted failed-cell attribution

Builder candidate `602a96e6bb7a65cea5895fc1d6ee1887f7e5a0b5` is accepted by `docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_ACCEPTANCE_20260916.md`.

Accepted classification: `ATTRIBUTED_STRUCTURAL_INCOMPATIBILITY_OF_FROZEN_DERIVATIVE_INPUTS`.

- Cells 4/8: frozen upper-b inward derivative is negative; both slack and active upper-b cases imply `q_b<=p_b^B<0`, incompatible with `q_b=c^{-gamma}>0`.
- Cell 10: active-upper-b negative/backward-a liquid-equality root lies below the derivative-direction switch, so the equality root has positive `g_a` and is inconsistent with backward-a. No second direction-valid root exists under the accepted monotonicity argument.
- No mathematically legal frozen-contract selector branch was omitted.

These are incompatibilities of historical MATLAB-faithful derivative states with the corrected D1-D3 target, not economic nonexistence, corrected-HJB nonexistence, HJB convergence failure, or KFE failure. The same historical-derivative panel must not be rerun.

## Active gate

Current active task: `tasks/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_ZERO_SCIENCE_20260916.md`.

This task is zero-science. It must bind a unique repository-authorized starting value/seed, grid/domain, prices/calibration, derivative construction, corrected policy-map semantics, D2 generator, one-step HJB equation, finite scientific-call budget, stop conditions, and evidence contract before any corrected-target HJB execution is authorized.

If no unique scientifically defensible seed/input contract exists under current authority, the task must fail closed rather than choosing an initialization because it is numerically convenient.

Real selector/root/HJB/KFE/MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results calls all remain zero in the active task.
