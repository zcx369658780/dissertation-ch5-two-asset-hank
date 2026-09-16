# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Accepted route

The frozen source-faithful reference and separately governed corrected successor remain distinct. Owner-adopted corrected semantics include D1 upper numerical state constraints, D2 consumed-total-drift conservative assembly, D3 regularized-cost-consistent KKT, active lower-a zero-kink multiplier handling, and interior zero-liquid Z switching.

## KFE-D2C-D — completed and accepted

Candidate `9a4eb0e5ec3627743596daa9b991436d2124efa9` completed the accepted V0 800-cell policy map, Q0 D2 assembly and one direct HJB step V1.

## KFE-D2D — Q0 route resolved

Q0 source-free uniqueness failed structurally because its graph contained two exact zero-asset-drift recurrent productivity pairs at lower-a nodes `(5,0)` and `(6,0)`. This was attributed to the conjunction of interior-liquid Z and lower-a zero-kink handling. It was explicitly not interpreted as economic multiple equilibria.

## KFE-D2E-A — completed and accepted

Candidate `368d58c96a9e6068fd4f7b36cca0f433d7f2ec3a` performed one fresh V1 policy remap and one Q1 assembly/topology audit.

Accepted results:
- 800/800 cells `SELECTED_ADMISSIBLE`;
- 408 total roots, 160 interior-Z roots;
- Q1 D2 PASS;
- Q1 SHA-256 `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E`;
- exact-positive graph has one closed class `[5,6,405,406]`;
- all 800 states can reach it;
- the two separate Q0 sinks do not persist because flats 405 and 6 gain opposite liquid directional edges while flats 5 and 406 retain Z/zero drift.

This is still one-step policy/operator topology evidence, not HJB convergence.

## KFE-D2E-B — active: Q1 source-free invariant-mass validation

Active task:
`tasks/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_20260916.md`

Validate exact accepted Q1 under the already accepted pin-free/source-free KFE contract: `Q1.T @ p = 0`, one structural audit, one SCC verification, one dense `gesvd`, one normalized candidate and one source-free residual evaluation.

PASS requires structural single-class uniqueness, numerical rank 799/nullity 1, second-smallest singular value above prospective threshold, normalized nonnegative mass and bounded source-free residual. No row replacement/pin/source injection, retry, alternative eigensolver, policy remap, D2 reassembly, HJB/V2/nonlinear continuation, MATLAB or downstream work is authorized.

## KFE-D2F — conditional later route

Only after independent acceptance of Q1 invariant-mass evidence may Reviewer design a bounded nonlinear HJB continuation / fixed-point convergence route. Neither Q1 topology nor Q1 KFE alone establishes an economic steady state.

## KFE-D3 — later production closure

Corrected multi-province production replacement, steady state, GE/annual/dynamics/IRF and Results remain downstream gates with separate evidence and authority.

Capital/labor K1/C1/K1B/K2 routes remain deferred, not abandoned, behind the current household/KFE integration route.