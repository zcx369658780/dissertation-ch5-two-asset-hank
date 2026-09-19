# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`V3_CELL100_LOWER_B_NEGATIVE_FORWARD_A_PRE_SCREEN_FALSE_NEGATIVE_ATTRIBUTED__MINIMAL_REPAIR_AND_CHECKPOINT3_REEXECUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted continuation result

Reviewer accepted Builder candidate `d2b0d62ff7a7c9c094bb70d6eaf8bef88f8e449a`.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT2_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_ACCEPTANCE_20260919.md`.

Accepted complete checkpoint 2 remains the last complete nonlinear checkpoint.

The exact `V2->V3` direct solve passes:

- V3 SHA `4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF`
- residual infinity norm `1.4391265956703592e-14`
- backward error `2.439151619375125e-16`.

The V3 map first fails at cell100 before P3/u3/Q3 is formed.

## Reviewer attribution

The V3 cell100 seven-candidate census omits an authority-backed active lower-b negative-transfer / forward-`a` branch.

The omission is caused by the existing 513-point log viability screen spanning from the lower-b shadow floor to `sys.float_info.max`. At V3 cell100 the legal forward-`a` negative interval is:

`(0.012601561934698366,0.015751950034835593)`.

The first two screen points are approximately:

`0.005156057482672656`, `0.020837512395988838`.

Thus the complete legal interval is skipped.

Static algebra also proves the missing branch's active liquid equality has exactly one root inside its legal interval.

This is an implementation filtering false negative under already-adopted lower-b/D3/upwind authority, not a new scientific law.

## Active task

`tasks/CH5_MP4C_2018_KFE_D123_V3_CELL100_LOWER_B_NEGATIVE_FORWARD_A_PRE_SCREEN_REPAIR_AND_CHECKPOINT3_REEXECUTION_20260919.md`.

The task minimally repairs lower-b negative branch representation and performs one fresh policy map from the already accepted V3 field. It does not rerun V2->V3 and does not continue to V4.

If the V3 map completes, it may assemble one Q3 and evaluate checkpoint-3 B3/D3/stability/cycle metrics.

Production, terminal KFE, GE and Results remain closed.
