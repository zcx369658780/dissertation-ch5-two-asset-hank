# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Accepted route

The frozen source-faithful reference and separately governed corrected successor remain distinct. Owner-adopted corrected semantics now include D1 upper numerical state constraints, D2 consumed-total-drift conservative assembly, D3 regularized-cost-consistent KKT, active lower-a zero-kink multiplier handling, and interior zero-liquid Z switching.

## KFE-D2C-D — completed and accepted

Candidate `9a4eb0e5ec3627743596daa9b991436d2124efa9` completed a fresh Option-A execution:
- 800/800 corrected cells `SELECTED_ADMISSIBLE`;
- 800 selector evaluations;
- 442 roots total, including 206 interior-Z roots;
- 42 selected Z policies;
- one D2 assembly PASS;
- one sparse direct HJB step PASS;
- no retries, V1 selector map, nonlinear continuation, KFE, MATLAB or downstream calls.

The direct step produced V1 SHA-256 `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2` with normwise backward error `1.9727855630325988e-16`.

This closes the single-step corrected-HJB integration gate as bounded diagnostic evidence. It does not establish nonlinear HJB convergence or a corrected fixed point.

## KFE-D2D-A — active: corrected KFE validation design/binding, zero science

Active task:
`tasks/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_ZERO_SCIENCE_20260916.md`

Before any KFE runtime, determine whether the accepted pre-step Q0 is sufficient for an operator-level source-free KFE diagnostic or whether a V1 policy remap is scientifically required. Freeze exact transpose/F-order mapping, pin-free homogeneous stationarity, normalization, conservation, nonnegative-mass, rank/nullity/uniqueness, deterministic solver budget and fail-closed rules.

No scientific/model call is allowed in this design gate.

## KFE-D2D-B — conditional runtime

Only after D2D-A acceptance may Reviewer publish a bounded corrected KFE validation execution task. A future KFE PASS would be operator/stationary-density diagnostic evidence only unless a separately accepted HJB fixed point exists.

## KFE-D3 — later production closure

Corrected multi-province production replacement, steady state, GE/annual/dynamics/IRF and Results remain downstream gates with separate evidence and authority.

Capital/labor K1/C1/K1B/K2 routes remain deferred, not abandoned, behind the current household/KFE integration route.
