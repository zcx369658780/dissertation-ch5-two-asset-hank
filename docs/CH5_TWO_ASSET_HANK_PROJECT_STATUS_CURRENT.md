# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`V1_REMAP_Q1_SINGLE_CLOSED_CLASS_ACCEPTED__Q1_SOURCE_FREE_KFE_VALIDATION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted scientific checkpoint

Owner-adopted D1/D2/D3 corrected semantics、lower-a zero-kink multiplier handling、interior zero-liquid Z switching、Option-A 800-cell V0 map、accepted Q0、一次 direct HJB step V1，以及 Q0 two-sink structural attribution均继续有效。Source-faithful/production paths remain frozen。

## V1 remap / Q1 topology accepted

Builder candidate `368d58c96a9e6068fd4f7b36cca0f433d7f2ec3a` is accepted by `docs/CH5_MP4C_2018_KFE_D123_V1_POLICY_REMAP_Q1_TOPOLOGY_ACCEPTANCE_20260916.md`.

Accepted V1 remap completed 800/800 `SELECTED_ADMISSIBLE` cells, used 408 total roots including 160 interior-Z roots, and assembled Q1 once under the unchanged D2 law. Q1 passed construction/conservation/coordinate-action/closed-face checks and has SHA-256 `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E`.

Q1 exact-positive topology has exactly one closed communicating class `[5,6,405,406]`; all 800 states can reach it. The two separate Q0 sinks do not persist: flat 405 becomes forward-liquid directional and flat 6 becomes backward-liquid directional, joining the four recurrent states into one class; flats 5 and 406 retain Z/zero drift.

This remains one-step policy/operator evidence only. It does not establish nonlinear HJB convergence, joint HJB-KFE fixed point, stationary economic equilibrium, production readiness or Results authority.

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_20260916.md`。

Perform one bounded, pin-free, source-free stationary-mass validation of exact accepted Q1 using `Q1.T @ p = 0`, one SCC verification and one full dense `gesvd`. No row replacement/pin/source RHS, retries, solver substitutions, iterative eigensolver, selector/root/policy-map, D2 reassembly, HJB/V2/nonlinear continuation, MATLAB or downstream call is authorized.

A future Q1 KFE PASS would validate only the invariant mass of this accepted one-step V1-policy operator Q1. Production replacement and Results remain unauthorized.