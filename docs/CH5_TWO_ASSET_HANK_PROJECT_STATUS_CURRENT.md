# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`Q0_KFE_TWO_CLOSED_CLASSES_ACCEPTED__STRUCTURAL_ATTRIBUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted scientific checkpoint

Owner-adopted D1/D2/D3 corrected semantics、lower-a zero-kink multiplier handling、interior zero-liquid Z switching、Option-A 800-cell complete policy map、accepted Q0 conservative generator以及一次 direct HJB step均继续有效。Source-faithful/production paths remain frozen。

## Q0 KFE operator result

The bounded source-free Q0 validation rerun candidate `132b2657c61e0707a5fff96b936b5a62a78dbb2e` is accepted as valid fail-closed evidence by `docs/CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_FAIL_CLOSED_ACCEPTANCE_20260916.md`.

Accepted Q0 passes construction identity, bounded sparse reaggregation, `Q0@1`, nonnegative offdiagonals and exact-zero closed-face outward flux. The exact-positive directed graph has 2318 edges, 400 SCCs of size 2, exactly two closed communicating classes of size 2 each, and 796 transient states. Because the finite conservative generator has more than one closed class, Q0 does not satisfy the frozen structural uniqueness requirement. GESVD and stationary-mass solving were correctly not executed.

This is structural nonuniqueness of the invariant stationary space for the accepted V0-policy operator Q0. It is not evidence of economic multiple equilibria, nonlinear HJB nonexistence, corrected fixed-point multiplicity, production readiness or Results authority.

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_20260916.md`。

The task must map both closed classes to exact F-order grid states and accepted cell receipts, identify selected policies/drifts and outgoing rates, recover the SCC condensation/reachability basins, and determine whether closure is caused by exact zero asset drifts, state-constraint/boundary behavior, deterministic policy-flow topology, or a mixed mechanism.

Allowed runtime is structural only: accepted Q0 load <=1, graph audit <=1, SCC decomposition <=1, condensation/reachability analysis <=1, accepted receipt reads <=800. GESVD/nullspace/stationary-mass solve, `Q0.T@p`, selector/root/policy-map/D2/HJB/V1-remap/MATLAB/downstream calls are all zero.
