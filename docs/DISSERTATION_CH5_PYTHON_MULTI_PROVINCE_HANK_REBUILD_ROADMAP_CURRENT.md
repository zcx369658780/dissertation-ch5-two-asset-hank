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

The first complete K1B-active corrected turn3 is accepted.

Accepted turn3 runtime candidate:

`1143cd8eb6e7722d7588107a0d69f68e8dd06df7`.

Turn3 produced:

- 31/31 HJB/KFE PASS;
- one frozen-share K1B/C1 integration;
- completed-turn3 raw ra0 SHA `1C587932F4E8471209663D2262DB1BB308857EEEA1198D7868E4721CFB031E8F`;
- deterministic turn4 K1B input/share candidate.

Accepted turn4 entering objects:

- share SHA `5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`;
- rah SHA `7DE65A71206F52AB3D2DA98D6D01C43A8A69D8B2C423BE49A15D5D287C434BE9`.

Active task:

`tasks/CH5_MP4C_K1B_TURN4_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921.md`.

The task executes one further bounded K1B-active turn4, prepares turn5, and stops before turn5 household.

## Route after the active task

If turn4 PASS:

1. accept or reject the second consecutive K1B-active turn based on the frozen HJB/KFE/accounting/timing gates;
2. inspect the cross-turn panel for numerical behavior without using improvement direction as a pass condition;
3. decide whether the evidence is sufficient to design a bounded multi-turn K1B continuation/fixed-point diagnostic, or whether another isolated issue must be resolved first;
4. K2 remains later and requires separate scientific authority.

If turn4 FAIL:

stop at the exact first failing scientific object. Do not change beta values, payoff law, smoothing, labor route, Delta, tolerance or solver to obtain a pass.

Production-default replacement, full outer fixed point, K2, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
