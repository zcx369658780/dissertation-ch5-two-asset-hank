# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`CORRECTED_TURN2_RUN005_ACCEPTED__K1B_TURN3_LAGGED_RAW_RA0_ACTIVATION_SAFETY_GATE_ACTIVE`

Results eligibility=`FALSE`。

## Latest accepted runtime

Accepted candidate:

`45e2e1f0f50c8e681d13e4e22fba4b50a90c8aad`

Acceptance:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_ACCEPTANCE_20260921.md`

Turn2 result:

- 31/31 household HJB/KFE PASS;
- 380 direct HJB updates;
- 6 one-halving relaxation events;
- 31/31 terminal unique-closed-class KFE PASS;
- exactly one K1A/C1 integration PASS;
- national private-capital residual 0;
- raw turn3 payoff candidate persisted;
- turn3 household not run.

## Route transition

The corrected turn1+turn2 prefix satisfies the roadmap prerequisite for reopening K1B.

K1B remains gated before household runtime.

## Active task

`tasks/CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_20260921.md`

The task is zero-science.

It will construct the exact turn3 K1B lagged-return foreign-share plan and household raw-payoff candidate from completed-turn2 raw ra0, with beta_distance=2, beta_return=.5, fixed theta and no smoothing.

No HJB/KFE, firm or integration runtime is authorized.
