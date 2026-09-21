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

Turn3 remains the latest complete K1B-active PASS.

Turn4 run001 stopped at 安徽 checkpoint4 / F0364 before integration. The subsequent zero-science forensic is accepted and classifies the failure as an implementation false negative caused by the whole-mapped-q_b-interval positivity guard.

Accepted forensic candidate:

`790350270d4ec07d61cc1765c042f2fd33b82b3c`.

Accepted repair scope is narrow: interior-b/interior-a strict crossing with finite negative nonzero R may use the positive-domain intersection of the mapped q_b interval and branch-local liquid-shadow membership. Active liquid faces, ratio zero, positive-ratio behavior and all equations/tolerances remain unchanged.

Active task:

`tasks/CH5_MP4C_K1B_TURN4_ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR_HISTORICAL_PARITY_AND_REEXECUTION_20260921.md`.

The task first implements the narrow selector repair, then requires exact historical selected-policy identity parity over 1,227 accepted maps. Only after parity may one fresh bounded turn4 reexecution occur.

## Route after the active task

If parity fails, stop and protect accepted predecessor science.

If parity passes but fresh turn4 fails, stop at the exact new first scientific failure.

If turn4 passes, inspect the second complete K1B-active turn and turn5 candidate before considering any longer outer-path diagnostic.

K2, production-default replacement, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
