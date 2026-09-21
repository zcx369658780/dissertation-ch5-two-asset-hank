# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`.

状态：

`ANHUI_F0364_FALSE_NEGATIVE_ACCEPTED__NARROW_REPAIR_PARITY_TURN4_REEXECUTION_ACTIVE`

Results eligibility=`FALSE`.

## Last complete K1B-active turn

Turn3 candidate:

`1143cd8eb6e7722d7588107a0d69f68e8dd06df7`

remains accepted with 31/31 HJB/KFE and one K1B/C1 integration.

## Turn4 run001 accepted failure

Candidate:

`cc8f1ba22aa2b010325dce6e6c282802f5157c10`

failed first at 安徽 checkpoint4 / F0364 with `NO_ADMISSIBLE_POLICY`. Eleven provinces completed HJB/KFE; integration and turn5 preparation did not run.

## Accepted 安徽 F0364 forensic

Candidate:

`790350270d4ec07d61cc1765c042f2fd33b82b3c`

Acceptance:

`docs/CH5_MP4C_K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FALSE_NEGATIVE_ACCEPTANCE_20260921.md`

Classification:

`TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_GUARD_FALSE_NEGATIVE_CONFIRMED`.

Accepted exact arithmetic:

- d_z `-5.840722762648187`
- R `-0.3330414721146172`
- mapped q_b interval `[-0.000267101992455363, 0.0016097854371494127]`
- positive-domain intersection `(0,0.0016097854371494127]`
- unique admissible backward q_b `0.0015039676061569449`
- q_a `-0.0005008835855672058`
- g_a `0`
- g_b `-17.978717494437753`
- KKT residual `0`.

Earliest causal source exit is the whole-interval guard:

`if implied_q_b_interval[0] <= 0.0: return None`.

## Active task

`tasks/CH5_MP4C_K1B_TURN4_ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR_HISTORICAL_PARITY_AND_REEXECUTION_20260921.md`

The task may change only `selector.py`, implement the accepted interior-b negative-R positive-domain-intersection correction, prove focused 安徽/Beijing parity and exact historical policy identity parity over 1,227 accepted checkpoint maps, then and only then rerun one fresh bounded turn4.

Turn5 household, K2, long outer path, GE and Results remain closed.
