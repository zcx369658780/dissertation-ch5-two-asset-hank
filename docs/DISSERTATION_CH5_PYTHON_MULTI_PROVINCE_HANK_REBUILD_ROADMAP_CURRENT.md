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

The first complete K1B-active turn3 remains accepted.

A second bounded K1B-active turn4 was attempted and stopped at the first scientific failure before integration.

Accepted failed evidence:

- candidate `cc8f1ba22aa2b010325dce6e6c282802f5157c10`
- 安徽 checkpoint4 / F0364
- outcome `NO_ADMISSIBLE_POLICY`
- 11/31 provinces completed HJB/KFE
- no turn4 integration
- no turn5 candidate
- no production-source change or scientific retry.

Active task:

`tasks/CH5_MP4C_K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC_20260921.md`.

The task is zero-science and classifies the 安徽 F0364 mapped-q_b interval/domain issue under the already accepted negative-ratio interior-a switching authority.

## Route after the active task

If the forensic confirms a guard false negative, Reviewer may authorize a narrow interior-b selector implementation correction plus exact historical compatibility and bounded failure-cell/turn4 replay.

If the forensic confirms scientific infeasibility, turn4 remains blocked and the route returns to scientific design rather than numerical rescue.

If Owner authority is genuinely ambiguous, stop for Owner decision.

No beta/payoff/smoothing/labor/Delta/tolerance/solver change is allowed merely to obtain convergence.

K2, production-default replacement, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
