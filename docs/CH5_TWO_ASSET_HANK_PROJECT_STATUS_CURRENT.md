# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`Q0_TWO_ZERO_DRIFT_SINKS_ATTRIBUTED__V1_POLICY_REMAP_Q1_TOPOLOGY_DIAGNOSTIC_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted scientific checkpoint

Owner-adopted D1/D2/D3 corrected semantics、lower-a zero-kink multiplier handling、interior zero-liquid Z switching、Option-A 800-cell complete policy map、accepted Q0 conservative generator以及一次 direct HJB step V1均继续有效。Source-faithful/production paths remain frozen。

## Q0 recurrent-class attribution accepted

Candidate `2723c475943f7e6a767a940a9a52bad7b9c25e6f` is accepted by `docs/CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_ACCEPTANCE_20260916.md`.

Accepted Q0 has two exact recurrent productivity pairs:

- flats `5,405` at asset node `(i_b,i_a)=(5,0)`, `(b,a)=(-0.1578947368421053,0)`;
- flats `6,406` at asset node `(i_b,i_a)=(6,0)`, `(b,a)=(0.2105263157894739,0)`.

At all four states, interior-liquid Z sets `g_b=0` exactly and active lower-a zero-kink handling sets `g_a=0` exactly. There are no asset outgoing rates; only the two-way productivity rate `1/3` remains. The two Q0 closed classes are therefore exact-zero-asset-drift sinks produced jointly by Z + lower-a state constraint + zero-kink handling, not by b-boundary behavior or a nonzero asset cycle.

The accepted basin partition is A-only 12 states, B-only 560 states, both-reachable 228 states, neither 0. This is Q0 graph topology only, not economic multiple equilibria.

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_V1_POLICY_REMAP_AND_Q1_RECURRENT_TOPOLOGY_DIAGNOSTIC_20260916.md`。

The smallest next diagnostic is one V1 policy remap and one Q1 D2 assembly/topology audit. It tests whether the two exact Q0 sinks persist after the already accepted single direct HJB step. No further HJB solve, nonlinear continuation, KFE stationary-mass solve, SVD/eigen/nullspace, MATLAB or downstream call is authorized.

A Q1 topology result remains a post-step policy diagnostic only. It is not HJB convergence, joint HJB-KFE fixed point, stationary economic equilibrium, production readiness or Results authority.