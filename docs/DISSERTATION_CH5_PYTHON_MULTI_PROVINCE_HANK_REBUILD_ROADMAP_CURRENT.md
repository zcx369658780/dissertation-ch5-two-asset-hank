# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Household corrected numerical foundation

The corrected household route has now reached complete accepted checkpoints through checkpoint 10.

Accepted numerical/scientific closure includes D1/D2/D3, boundary KKT, lower-`a` zero-kink, liquid-`Z`, one-axis interior-`a` switching, simultaneous two-axis switching, repaired lower-b branch representation, fixed nonlinear update law and accepted cycle rules.

Local selector-law design is no longer the primary bottleneck.

## Current nonlinear state

Checkpoint 10 is complete and D2-valid:

- `B10=3.874510913493001e-08`
- `D10=5.8692895192891115e-06`.

It does not satisfy the frozen convergence thresholds `1e-8 / 1e-7`.

No exact, period-2 or period-3 cycle is detected.

The recent trajectory is strongly approaching the frozen thresholds, but trend is diagnostic only.

## Current stage

Active task:

`tasks/CH5_MP4C_2018_KFE_D123_CHECKPOINT10_TO_CHECKPOINT12_BOUNDED_NONLINEAR_CONTINUATION_20260920.md`.

At most updates 11-12 may be consumed.

If primary convergence occurs, continuation stops immediately and the next independent gate is terminal household topology/KFE validation.

## Remaining household closure

After an accepted HJB convergence candidate:

1. confirm same-value final D1/D2 legality;
2. prove exactly one closed communicating class;
3. solve source-free homogeneous KFE on the same Q*;
4. verify `Q*.T p*=0`;
5. dense GESVD rank/nullity;
6. nonnegative normalized stationary mass;
7. accept only a conditional household fixed point at frozen prices/calibration.

Only after household closure may the deferred multi-province production/capital/labor/market-clearing route reopen.

GE, annual calibration/dynamics, shocks, IRFs, welfare and Results remain downstream.
