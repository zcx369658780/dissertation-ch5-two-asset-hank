# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Household numerical foundation — largely closed

Accepted scientific/numerical components now include:

- D1 finite-domain/boundary law;
- D2 consumed-total-drift conservative generator;
- D3 regularized adjustment-cost KKT;
- lower-`a` zero-kink multiplier law;
- interior-liquid zero-drift `Z`;
- lower-b complete branch coverage;
- one-axis interior-`a` zero-drift switching;
- simultaneous two-axis zero-drift switching;
- corrected V0/Q0;
- direct V0->V1;
- V1/Q1;
- Q1 topology and source-free KFE diagnostics;
- direct V1->V2;
- complete V2/P2/u2/Q2.

The local corrected-selector closure phase has therefore reached a complete checkpoint 2.

## Checkpoint 2 — complete but nonconverged

Accepted:

- `B2=0.006582827785543588`
- `D2=0.05439336697877817`
- D2/Q2 PASS
- no exact cycle
- approximate period-2/3 windows not yet available.

This is the first complete nonlinear checkpoint after V1 under the fully adopted multidimensional switching law.

## Current stage — bounded nonlinear continuation

Active task:

`tasks/CH5_MP4C_2018_KFE_D123_CHECKPOINT2_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919.md`.

The route may continue through at most V6, under fixed `Delta=1000` and the Owner convergence/cycle law.

The purpose is to determine whether the now-complete corrected household HJB:

- converges;
- enters an exact or authorized approximate cycle;
- exposes another scientific selector/D2 issue;
- or remains nonconverged through checkpoint 6.

No terminal KFE is run inside this continuation task.

## After HJB convergence

Once a primary HJB convergence candidate is accepted:

1. same-value final D1/D2 legality confirmation;
2. one-closed-class topology gate;
3. pin-free/source-free homogeneous terminal KFE;
4. dense GESVD rank/nullity and nonnegative mass;
5. conditional household fixed-point acceptance at frozen prices/calibration.

Only after household closure may the deferred multi-province production/capital/labor/market-clearing route reopen.

## Downstream project stages

Still downstream:

- multi-province production replacement;
- bilateral capital/labor network closure;
- market clearing and GE;
- annual calibration;
- dynamics/shocks/IRFs;
- welfare/causal interpretation;
- dissertation Results.

Capital/labor K1/C1/K1B/K2 routes remain deferred, not abandoned.
