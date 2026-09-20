# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`RUN004_31_PROVINCE_HOUSEHOLD_AND_ADOPTED_KFE_ACCEPTED__RAW_NEXT_PAYOFF_REDUCTION_ORDER_GUARD_FAIL__INTEGRATION_ONLY_REPLAY_ACTIVE`

Results eligibility=`FALSE`。

## Accepted run004 household result

Candidate:

`af770c1fb787098569df2a25471cdc8101eda3a3`.

Acceptance:

`docs/CH5_MP4C_RUN004_31PROVINCE_HOUSEHOLD_KFE_PASS_RAW_NEXT_PAYOFF_REDUCTION_ORDER_GUARD_ACCEPTANCE_20260920.md`.

Under the Owner-adopted unique-closed-class KFE:

- Beijing implementation parity PASS;
- household HJB PASS: 31/31;
- terminal KFE PASS: 31/31;
- stationary aggregates PASS: 31/31;
- household batch PASS.

Accepted household-batch identity:

`8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05`.

Run004 household/KFE science is accepted and is not to be rerun for the immediate successor.

## Integration blocker

The one run004 integration turn reached labor, K1A, C1, all 31 firms, wage, monetary and fiscal operations, then stopped at:

`FAIL__RAW_NEXT_PAYOFF_SAME_S_IDENTITY`.

The failed guard required bitwise equality between:

- BLAS `raw_ra0 @ S`; and
- separately ordered `np.sum(raw_ra0[:,None] * S, axis=0)`.

The formulas are mathematically the same adopted destination-by-origin payoff aggregation but may differ in floating-point reduction order.

Therefore the failure is an engineering/numerical guard defect. The integration turn itself is not yet accepted because the downstream accounting block and next-state persistence were not completed.

## Active successor

`tasks/CH5_MP4C_RUN004_CANONICAL_SAME_S_RAW_NEXT_PAYOFF_REPAIR_AND_INTEGRATION_ONLY_REPLAY_20260920.md`.

The successor binds the accepted run004 household batch, performs no household HJB/KFE/aggregate science, and replays exactly one integration turn.

Canonical payoff evaluation:

`rah_i = math.fsum(float(raw_ra0[j]) * float(S[j,i]) for j in range(31))`

with ascending destination index.

Same-S acceptance is based on exact raw-ra0/S provenance and deterministic product-term construction, not bitwise equality to a different reduction implementation.

Turn 2, K1B, K2, GE and Results remain closed.
