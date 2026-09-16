# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Accepted route

The frozen source-faithful reference and separately governed corrected successor remain distinct. Owner adopted D1 upper numerical state constraints, D2 consumed-total-drift conservative assembly, and D3 regularized-cost-consistent KKT for the corrected diagnostic target. Static implementation is accepted.

Historical derivative-panel failures are attributed and closed. Owner selected source-native Option A `hjb100_initialization.mat:v0` as the first corrected one-step seed for provenance/path-dependence reasons.

## KFE-D2C-B first Option-A attempt — fail closed accepted

The first full-map attempt stopped at F-order Cell `(0,0,0)` with `NO_ADMISSIBLE_POLICY` after one selector call / four roots; D2 and direct HJB solve were not reached.

Reviewer accepted the execution record but found a specific selector omission. At active lower-`a`, `a=0`, zero transfer, the accepted KKT law permits `q_a=p_a+lambda_a`, `lambda_a>=0`, while the selector forced `q_a=p_a`. The legal multiplier domain must be intersected with the D3 zero-kink interval. For Cell 0 that intersection is nonempty, so the observed failure is an implementation/enumeration defect rather than Option-A/HJB nonexistence evidence.

## KFE-D2C-B-R1 — active: lower-a zero-kink multiplier repair + fresh Option-A reexecution

Active task:
`tasks/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_20260916.md`

Repair only the active lower-a zero-kink shadow/multiplier representation under the already accepted D1/D3 law. Keep slack faces, upper-a, nonzero-transfer branches, D2 zero-tolerance semantics, Option-A seed, grid, calibration and production paths unchanged.

After focused preflight and code freeze, rerun Option A once from Cell 0 with a fresh one-map budget: <=800 selectors, <=264 roots, D2<=1 only after all 800 cells pass, sparse direct HJB solve<=1 only after D2 passes, retries=0. First failed cell stops. No V1 selector map or nonlinear continuation.

## KFE-D2D — later corrected KFE validation

Even a successful one-step HJB experiment does not establish nonlinear HJB convergence or stationary-density validity. Corrected KFE mass/nonnegativity/uniqueness requires a later exact task.

## KFE-D3 — later production closure

Corrected multi-province production replacement, steady state, GE/annual/dynamics/IRF and Results remain downstream gates with separate evidence and authority.

Capital/labor K1/C1/K1B/K2 routes remain deferred, not abandoned, behind the current household/KFE integration blocker.
