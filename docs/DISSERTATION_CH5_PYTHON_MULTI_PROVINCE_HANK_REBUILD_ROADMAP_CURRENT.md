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

The 安徽 F0364 positive-domain-intersection selector repair is accepted and preserves all 1,227 accepted predecessor selected-policy identities.

Fresh repaired K1B turn4 is accepted with 31/31 HJB/KFE and one frozen-share K1B/C1 integration.

Accepted turn5 objects:

- input file SHA `10CDFE998FBC95F09DA682F5389F268A1569A5FEB345D61470B3E8AA415D01D1`
- share SHA `2BDF7B8226C8404DB9C7FFEEE3F72F7AE9CA1305905460A4E2430AABEA4D3B06`
- rah SHA `5CAF9166D85198E6923FFCD5A1F92D278C8A1C6CB924E8DD1B843F875E91D88E`.

Active task:

`tasks/CH5_MP4C_K1B_TURN5_TURN6_BOUNDED_CONTINUATION_DIAGNOSTIC_20260921.md`.

The task executes a bounded two-turn continuation, turn5 and turn6, then prepares turn7 and stops before turn7 household.

## Route after the active task

If both turns PASS, Reviewer will have four consecutive complete K1B-active turns (turn3-turn6) and can design a dedicated fixed-point/convergence diagnostic without changing economics.

If a new failure occurs, stop at the exact first scientific object and resolve it before any longer path.

No convergence claim is authorized by the current task itself.

K2, production-default replacement, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
