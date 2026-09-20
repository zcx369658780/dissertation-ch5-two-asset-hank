# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`HOUSEHOLD_HJB_KFE_FIXED_POINT_CANDIDATE_ACCEPTED__CORRECTED_AGGREGATE_ADAPTER_BINDING_ACTIVE__OUTER_RUNTIME_BLOCKED`

Results eligibility=`FALSE`。

## Accepted conditional household fixed point

Reviewer accepted Builder candidate `e8aec1d2138b2cfa3c0896f4f5d95430478c635f`.

Acceptance:

`docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_ACCEPTANCE_20260920.md`.

Checkpoint-11 HJB:

- B11 `5.456747553811425e-11`
- D11 `5.4012647243695255e-08`
- D2 PASS
- primary convergence PASS.

Terminal same-Q11 KFE:

- exactly one closed communicating class, size 320;
- dense GESVD rank/nullity `799/1`;
- `||Q11.T@p||inf=1.9114484300919443e-16`;
- normalized source-free mass PASS;
- no pin/source/clipping/retry.

Stationary-mass artifact:

`1DD70201EAC5EED0AE768362D99A76736276BFB4D5E6AF0D8DBDB4E9D6FE7D16`.

This closes the household HJB-KFE gate only for the frozen corrected price/calibration object.

## Active task

`tasks/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_20260920.md`

The task is zero-solver: bind source aggregate semantics, compute one deterministic aggregate receipt from accepted checkpoint-11 p/policies, and prepare an opt-in corrected household adapter fixture. Existing production/default outer routes must remain unchanged.

## Remaining scientific gate before outer runtime

The K1A payoff-return re-audit remains controlling:

`K1A_PAYOFF_RETURN_REAUDIT_ACCEPTED__CLIPPED_RA_TRANSITIONAL_ONLY__RAW_RA0_SOURCE_CONSISTENT_CANDIDATE__OWNER_PERIOD_NUMERAIRE_FREEZE_REQUIRED_BEFORE_RUNTIME_CHANGE`.

No new K1B or outer-loop scientific runtime may change the household payoff-return law until Owner freezes the period/numeraire/payoff contract.

Historical K1A KFE observations remain diagnostic only; they are not retroactively upgraded by the new corrected household closure.

Production default, market clearing, GE, annual dynamics, IRFs, welfare and Results remain closed.
