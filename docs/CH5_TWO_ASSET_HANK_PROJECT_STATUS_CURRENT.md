# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`CORRECTED_Q0_KFE_DESIGN_ACCEPTED__BOUNDED_SOURCE_FREE_OPERATOR_VALIDATION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoint

The corrected Option-A route has an accepted complete 800-cell policy map, one passing conservative Q0 D2 generator, and one passing direct HJB step V1. This remains one-step diagnostic evidence only.

Zero-science design candidate `494dfc741dbf494a5b367b3abe99234a5708df4c` is accepted by `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_ACCEPTANCE_20260916.md`.

The accepted design freezes Q0, not a V1 remap, as the next operator-level KFE diagnostic object. A Q0 KFE PASS would establish only an invariant mass for the accepted V0 policy operator; it would not establish nonlinear HJB convergence, a joint fixed point, stationary economic equilibrium, production readiness, or Results authority.

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_20260916.md`。

The task authorizes exactly one pin-free source-free stationary-mass validation of the accepted Q0 using `Q0.T @ p = 0`, one exact-positive-edge SCC decomposition, and one full dense `scipy.linalg.svd(..., lapack_driver="gesvd")`. No row replacement, pin, RHS/source injection, clipping, tolerance tuning, iterative eigensolver, retry, V1 remap, HJB, selector, D2 reassembly, MATLAB or downstream call is authorized.

PASS requires one closed communicating class, numerical rank 799/nullity 1, second-smallest singular value above the frozen prospective threshold, source-free residual and normalization within prospective arithmetic bounds, and nonnegative mass within the frozen arithmetic allowance.

Production replacement remains unauthorized; Results eligibility remains `FALSE`.
