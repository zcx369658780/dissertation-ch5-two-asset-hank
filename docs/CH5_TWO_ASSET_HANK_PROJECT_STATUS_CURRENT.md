# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`RAW_RA0_31_PROVINCE_FIXED_PRICE_CROSS_SECTION_ACCEPTED__CORRECTED_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_ACTIVE`

Results eligibility=`FALSE`。

## Accepted corrected household foundation

Still accepted:

- corrected D1/D2/D3 household law;
- checkpoint-11 HJB convergence;
- same-Q11 unique source-free KFE;
- stationary Ct/Lt/At/Bt/AtTax mapping;
- opt-in corrected aggregate adapter;
- Owner Option-B raw-ra0 payoff law.

## Accepted raw-payoff safety progression

Accepted candidate:

`d0e3cdc27f11d6d7bb0a0ec32299e0f00f90fcda`.

Acceptance:

`docs/CH5_MP4C_K1A_RAW_RA0_PATH_B_TURN1_31_PROVINCE_FIXED_PRICE_ONE_STEP_CROSS_SECTION_ACCEPTANCE_20260920.md`.

All 31 exact Path-B turn-1-generated raw portfolio payoff values pass one corrected fixed-price policy/D2/direct-update step under common checkpoint-11 non-payoff inputs.

Important timing clarification: the accepted CSV turn-1 raw payoff is a completed-turn-1 / next-household payoff counterfactual, not entering turn-1 household payoff.

## Active task

`tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_KFE_AND_K1A_C1_ONE_TURN_INTEGRATION_20260920.md`.

The task starts from accepted outer-turn-1 initial states, solves all 31 corrected household HJB-KFE fixed points, aggregates them, then executes exactly one K1A-beta2 / C1 / source-faithful-labor / firm turn.

After firms return, it constructs:

`rah_next_raw = raw_ra0_turn1 @ S`

for future turn 2.

Turn 2 itself is not authorized.

K1B, K2, GE and Results remain closed.
