# Chapter 5 Python 多省份两资产 HANK 路线

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Corrected household foundation

Accepted:

1. corrected D1/D2/D3 and adopted boundary/switching law;
2. checkpoint-11 HJB convergence;
3. same-Q11 unique source-free invariant mass;
4. exact Ct/Lt/At/Bt/AtTax aggregation;
5. opt-in corrected household aggregate adapter;
6. Owner Option-B raw-ra0 payoff authority.

## Raw-payoff safety gates accepted

Two bounded safety layers are now accepted:

- global Path-B LOW/MEDIAN/HIGH raw payoff one-step panel;
- exact 31-province Path-B completed-turn-1 raw payoff one-step cross-section.

The latter covers all exact province-labelled payoff values from the accepted historical Path-B turn-1 raw counterfactual.

These are fixed-price safety results, not convergence results.

## Timing clarification

The historical Path-B `turn=1 static_raw_S_transpose_ra0` object is generated from completed-turn-1 firm raw returns.

Under the adopted lagged timing, it belongs to the next household iteration.

Therefore the corrected integrated route must not start turn 1 from that vector.

It must start from the accepted turn-1 initialization state, solve the corrected household block, produce corrected turn-1 firms, and only then create:

`rah_next_raw = raw_ra0_turn1 @ S`.

## Current stage

Active task:

`tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_KFE_AND_K1A_C1_ONE_TURN_INTEGRATION_20260920.md`.

The task attempts:

1. exact 31-province accepted initial-state binding;
2. source-native numerical initial arrays;
3. corrected HJB convergence for every province;
4. terminal source-free KFE for every province;
5. corrected household aggregates;
6. one K1A beta2 / C1 / source-faithful-labor / firm turn;
7. exact raw next-household payoff construction.

No second turn is allowed.

## Route after this task

If PASS:

1. accept the first internally consistent corrected multi-province turn;
2. inspect the resulting exact turn-2 state and raw payoff vector;
3. authorize a separately bounded turn-2 corrected household/integration continuation;
4. only after a bounded multi-turn corrected prefix may K1B `beta_return=.5` attractiveness feedback reopen;
5. K2 remains later.

If FAIL:

stop at the exact province/HJB/KFE/integration object. Do not restore clipping, retune Delta or modify the corrected household law merely to obtain a pass.

Production-default replacement, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
