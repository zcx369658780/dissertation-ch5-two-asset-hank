# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`CORRECTED_INITIAL_TURN_FULLY_CLOSED__TURN2_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_ACTIVE`

Results eligibility=`FALSE`。

## Fully accepted corrected initial turn

Acceptance:

`docs/CH5_MP4C_CORRECTED_INITIAL_TURN_FULL_CLOSURE_ACCEPTANCE_20260920.md`.

Accepted initial-turn chain:

- 31/31 corrected household HJB PASS;
- 31/31 Owner-adopted unique-closed-class KFE PASS;
- 31/31 stationary aggregate blocks PASS;
- one 31-province household batch PASS;
- source-faithful labor PASS;
- K1A `beta_distance=2`, `beta_return=0` PASS;
- C1 residual GovInv PASS;
- 31 firm evaluations PASS;
- canonical same-S raw payoff PASS.

Accepted household batch identity:

`8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05`.

Accepted turn-2 raw payoff identity:

`D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`.

Accepted turn-2 entering state authority:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json`

with 31 rows in exact province order.

## Active turn-2 task

`tasks/CH5_MP4C_CORRECTED_OPTIONB_TURN2_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260920.md`.

The task uses the exact completed-turn-1 / entering-turn-2 state, solves all 31 turn-2 corrected household HJB/KFE blocks, aggregates them, executes one turn-2 K1A/C1/firm integration, constructs a canonical raw payoff for a possible turn 3, and stops.

It does not establish outer convergence and does not run turn 3.

K1B, K2, GE and Results remain closed.
