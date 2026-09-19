# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Household corrected operator status

The corrected household numerical law now includes accepted D1/D2/D3, all adopted switching laws, and the repaired active lower-b negative branch representation.

Complete accepted nonlinear checkpoints now include checkpoint 1, checkpoint 2 and checkpoint 3.

Checkpoint 3:
- complete V3/P3/u3/Q3;
- D2 PASS;
- `B3=0.1291770476282596`;
- `D3=0.05315900863346279`;
- nonconverged.

## Current stage — bounded nonlinear continuation

Active task:

`tasks/CH5_MP4C_2018_KFE_D123_CHECKPOINT3_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919.md`.

The route may consume updates 4-6 only.

Its purpose is to determine whether the accepted corrected operator:

- converges;
- enters an exact/authorized approximate cycle;
- exposes another selector/D2 issue;
- or remains nonconverged through checkpoint 6.

The B3 increase is not itself a terminal rule.

## After an HJB convergence candidate

A separate terminal household gate will require:

1. same-value D1/D2 legality;
2. one closed communicating class;
3. source-free homogeneous KFE;
4. dense GESVD rank/nullity;
5. nonnegative normalized stationary mass.

Only after that conditional household fixed point may the deferred multi-province production/capital/labor/market-clearing route reopen.

Production, GE, dynamics, IRF, welfare and Results remain downstream.
