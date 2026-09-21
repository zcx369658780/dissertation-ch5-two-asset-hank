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

Accepted corrected prefix now contains two complete corrected K1A/C1 turns. The K1B turn3 zero-science activation safety gate is also accepted.

Accepted K1B turn3 objects:

- frozen destination-by-origin share-plan SHA:
  `4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`;
- entering raw household payoff SHA:
  `CEEFE34C16BA0DFDE9FA0C5590DFBB89084475BD88A8496EC18FEEBA7CB674D2`;
- completed-turn2 raw-ra0 attractiveness source:
  `B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951`.

Active task:

`tasks/CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921.md`.

The task executes exactly one K1B-active corrected turn3 and stops before turn4 household execution.

## Route after the active task

If PASS:

1. accept the first complete K1B-active corrected turn;
2. inspect the turn3 raw-return pressure, capital redistribution and C1 accounting without using their direction as a pass criterion;
3. review the deterministic turn4 K1B input/share candidate;
4. decide whether one further bounded K1B continuation is needed to assess numerical behavior before any longer outer path;
5. K2 remains later and requires separate scientific authority.

If FAIL:

stop at the first exact household/KFE/integration/timing object. Do not restore clipped household payoff, change beta values, add smoothing, retune Delta/tolerance or substitute solver merely to obtain PASS.

Production-default replacement, full outer fixed point, K2, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
