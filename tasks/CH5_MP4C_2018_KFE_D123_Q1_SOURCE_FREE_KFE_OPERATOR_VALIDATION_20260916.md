# CH5 MP4C 2018 KFE D1-D3 Q1 source-free KFE operator validation

Date: 2026-09-16

Status: `ACTIVE`

## Objective

Validate the exact accepted Q1 operator from the accepted V1 policy remap as a finite-state Markov generator with a unique, normalized, nonnegative, source-free invariant mass.

This task is operator-level only. It must not be described as nonlinear HJB convergence, a joint HJB-KFE fixed point, stationary economic equilibrium, production readiness or Results evidence.

## Startup authority

Fresh-fetch `origin/main` and read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_V1_POLICY_REMAP_Q1_TOPOLOGY_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_V1_POLICY_REMAP_AND_Q1_RECURRENT_TOPOLOGY_DIAGNOSTIC_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_REPORT.md`
9. exact Q1 artifact / D2 receipt / sealed manifest authority from the accepted V1-remap run.

## Exact object binding

Use only accepted Q1:

- artifact: `q1_generator.npz`
- SHA-256: `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E`
- state shape: `(20,20,2)`
- flattening: F-order, `b` fastest
- `omega = 70/361`
- forward stationarity: `Q1.T @ p = 0`
- probability mass: `p`
- density view: `g = p/omega`

The accepted Q1 D2 receipt is construction authority and must remain unchanged:

- diagonal construction error exactly `0.0`
- `max_abs(Q1 @ 1)=2.220446049250313e-15`
- prospective row-sum bound `2.976424297233587e-14`
- minimum offdiagonal `0.016508228132885275`
- zero coordinate-action violations
- exact-zero outward drift/rate/flux on all four asset boundaries.

## Frozen source-free contract

Preserve the previously accepted pin-free homogeneous-nullspace design:

1. Load and hash-bind exact Q1 once.
2. Structural audit exact CSR shape/finite data/nonnegative offdiagonals.
3. Bind accepted D2 construction identity exactly; any independent CSR reaggregation discrepancy must be persisted raw and evaluated against a prospectively fixed floating-point bound, never silently zeroed.
4. Evaluate `Q1 @ 1` exactly once and require it within the accepted prospective bound.
5. Reproduce exact-positive-edge SCC topology once. Require exactly one closed communicating class. The accepted expected membership is `[5,6,405,406]`; any mismatch fails closed.
6. Form `A = Q1.T` with no row removal/replacement.
7. Run exactly one full dense `scipy.linalg.svd(..., full_matrices=True, lapack_driver="gesvd", check_finite=True)`.
8. Use only the right singular vector associated with the smallest singular value as the homogeneous null candidate.
9. Allow only one global sign orientation and one scalar total-mass normalization.
10. Evaluate all 800 original equations with exactly one `Q1.T @ p`.
11. Persist `p` and density view `g=p/omega` without clipping, absolute-value repair or second normalization.

## Rank/nullity and uniqueness

Use the previously accepted prospective binary64 threshold form, adapted only to Q1 dimensions/norms:

- `N=800`
- `gamma_m = m*eps/(1-m*eps)`
- `tau_rank = gamma_(N+64) * max(1, sigma_max)`

Require:

- exactly one singular value `<= tau_rank`
- second-smallest singular value `> tau_rank`
- numerical rank `799`
- numerical nullity `1`
- structural SCC result and numerical nullity agree.

Any ambiguity at the frozen threshold is terminal; no threshold tuning or second decomposition is allowed.

## Stationarity / normalization / nonnegativity

After one sign orientation and one normalization, require prospective-bound checks inherited from the accepted Q0 design:

- finite `p` and `g`
- mass normalization within its prospective summation bound
- density normalization `omega*sum(g)=1` within its prospective grouped arithmetic bound
- source-free residual `Q1.T @ p` within `gamma_(N+64) * max(1, ||Q1.T||_inf * ||p||_inf)`
- normwise backward ratio within `gamma_(N+64)`
- global source ledger (`fsum(r)`, `dot(Q1@1,p)`, discrepancy) within prospective bounds
- componentwise `min(p) >= -tau_nonnegative`, where `tau_nonnegative = gamma_(N+64) * max(1, ||p||_inf)`
- total negative mass `<= N*tau_nonnegative`

Persist original signs; do not clip or replace negative values.

## Hard runtime ceilings

- Q1 artifact load: `<=1`
- structural/conservation audit: `<=1`
- `Q1 @ 1`: `<=1`
- SCC decomposition: `<=1`
- full dense `gesvd`: `<=1`
- normalized stationary candidate: `<=1`
- `Q1.T @ p`: `<=1`
- retries: `0`
- solver substitutions: `0`
- row-replaced/direct KFE solve: `0`
- iterative eigensolver/nullspace solve: `0`
- selector/root/policy-map: `0`
- D2 reassembly: `0`
- HJB solve / V2 / nonlinear continuation: `0`
- MATLAB / outer / firm / wage-return / GE / annual / shock / IRF / Results: `0`
- wall time: `<=300s`
- resident memory: `<=2 GiB`

## Fail closed

Stop immediately without retry if any identity, topology, rank/nullity, stationarity, normalization, nonnegativity, source-free, resource or evidence condition fails.

Do not modify Q1, selector, D2 law, grid, calibration, V1, Z law, lower-a law or any production/source-faithful code.

## Required outputs

Create a fresh evidence root distinct from all prior Q0/Q1 evidence. Persist at minimum:

- preflight binding receipt
- pre-execution scientific-code freeze
- structural/conservation receipt
- SCC receipt
- SVD/rank/nullity receipt
- stationary-mass arrays artifact
- stationarity/normalization/nonnegativity receipt
- execution ledger
- terminal receipt
- post-execution freeze check
- sealed manifest

Write final report:

`docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_REPORT.md`

Git workflow: task branch, one bounded implementation/report commit, non-force push, remote SHA readback, clean worktree. Do not merge main and do not publish a successor task.