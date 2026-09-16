# CH5 MP4C 2018 KFE D1-D3 corrected Q0 KFE operator validation

Date: 2026-09-16
Status: ACTIVE
Role: bounded Builder execution

## Objective

Validate the already accepted corrected `Q0` as a finite-state Markov generator for a source-free, pin-free stationary invariant mass. This is an operator-level KFE diagnostic only. It must not remap `V1`, iterate HJB, or make equilibrium/Results claims.

## Startup authority

Read in order after fresh-fetching `origin/main`:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_OPTION_A_COMPLETE_POLICY_MAP_D2_DIRECT_STEP_ACCEPTANCE_20260916.md`
8. the accepted Q0 D2 artifact/receipt and sealed manifest from candidate `9a4eb0e5ec3627743596daa9b991436d2124efa9`
9. directly relevant corrected generator/grid source.

If live authority materially differs, stop before any KFE/nullspace execution.

## Exact object binding

Use exactly the accepted Q0 artifact:

- path: `reports/ch5_mp4c_2018_kfe_d123_interior_z_switching_option_a_reexecution_20260916/d2_generator.npz`
- SHA-256: `093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`
- shape: `(800,800)`
- state tensor: `(b,a,z)=(20,20,2)`
- F-order; `b` fastest
- asset-cell volume `omega=70/361`

Forward stationarity is `A p = 0` with `A=Q0.T` and probability-mass vector `p`. Density view is `g=p/omega`.

## Frozen structural and conservation audit

Before SVD:

- verify exact artifact path/hash/shape/finiteness;
- verify every off-diagonal `>=0` by exact sign comparison;
- verify accepted diagonal/outgoing-rate construction identity;
- evaluate `Q0 @ ones(800)` exactly once and require `max(abs(.)) <= 5.222144858126786e-14`;
- verify all 800 accepted policy receipts remain present/hash-bound;
- persist an outside-domain flux ledger and require exact zero outward rate and mass flux at lower/upper `b` and lower/upper `a` faces;
- build the exact-positive off-diagonal directed graph and perform exactly one SCC decomposition;
- require exactly one closed communicating class; persist SCC sizes, closed-class count, and transient-state count.

No edge tolerance is allowed.

## Frozen nullspace solve

Exactly once:

```python
A = Q0.T
U, s, Vh = scipy.linalg.svd(
    A.toarray(),
    full_matrices=True,
    lapack_driver="gesvd",
    check_finite=True,
)
v = Vh[-1, :]
```

No other SVD/eigen/nullspace solver is allowed.

For the unnormalized vector, freeze:

- `tau_sum = gamma_800 * max(1, sum(abs(v)))`;
- require `abs(math.fsum(v)) > tau_sum`;
- if `math.fsum(v) < 0`, allow one global sign reversal only;
- normalize exactly once: `p = v / math.fsum(v)`;
- `g = p / omega`.

No row replacement, pin, RHS injection, clipping, absolute-value replacement, optimization, retry, or renormalization loop.

## Rank/nullity and uniqueness

With singular values in descending order:

- `tau_rank = gamma_864 * max(1, sigma_max)`;
- require exactly one singular value `<= tau_rank`;
- require second-smallest singular value `> tau_rank`;
- require numerical rank `799`, nullity `1`;
- persist all singular values or a complete hash plus `sigma_max`, smallest two, `tau_rank`, and gap ratios;
- if graph closed-class count and numerical nullity disagree, stop fail-closed.

The word `unique` is allowed only if both structural and numerical checks pass.

## Stationarity, normalization, and nonnegative mass

Evaluate `r=A@p` exactly once.

Freeze:

- `tau_stationarity = gamma_864 * max(1, ||A||_inf * ||p||_inf)`;
- require finite `r` and `||r||_inf <= tau_stationarity`;
- require normwise backward ratio `<= gamma_864`;
- persist `math.fsum(r)`, `dot(Q0@1,p)`, their discrepancy, and the prospective summation/dot bound; all must pass.

Normalization:

- require `abs(math.fsum(p)-1) <= gamma_800 * max(1,sum(abs(p)))`;
- require `omega*math.fsum(g)` to equal one within the prospectively derived grouped multiplication/summation bound.

Nonnegativity:

- `tau_nonnegative = gamma_864 * max(1, ||p||_inf)`;
- require `min(p) >= -tau_nonnegative`;
- persist exact negative-entry count, minimum component, total negative mass `math.fsum(max(-p_i,0))`;
- require total negative mass `<= 800*tau_nonnegative`;
- do not clip any component.

## Exact runtime ceiling

- Q0 artifact load: `1`
- structural/conservation audit: `1`
- SCC decomposition: `1`
- full dense `gesvd`: `1`
- normalized stationary candidate: `1`
- `Q0 @ 1`: `1`
- `Q0.T @ p`: `1`
- row-replaced/direct KFE solves: `0`
- iterative eigensolver/nullspace solves: `0`
- solver substitutions: `0`
- retries: `0`
- selector/root/policy map/D2/HJB/V1 remap: `0`
- MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results: `0`
- wall time: `<=300s`
- resident memory: `<=2GiB`

Any timeout, warning/nonconvergence, nonfinite output, memory breach, artifact mismatch, conservation failure, multiple closed classes, nullity !=1, negative-mass breach, stationarity breach, or missing evidence is terminal. Do not repair and rerun in this task.

## Evidence and report

Persist under:

`reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916/`

At minimum:

- preflight/binding receipt;
- structural/conservation receipt;
- SCC receipt;
- SVD/rank receipt;
- stationary-mass arrays artifact with hashes;
- stationarity/normalization/nonnegativity receipt;
- execution ledger;
- sealed manifest;
- post-execution code-freeze/readback receipt if any task-local validation code is written.

Write one report:

`docs/CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_REPORT.md`

Report verdict, baseline/branch/candidate, exact changed paths, artifact identity, graph result, singular-value/rank evidence, mass statistics, stationarity residuals, normalization, source-free ledger, call ledger, limitations, remote readback and clean worktree.

## Interpretation boundary

PASS establishes only that the accepted finite corrected `Q0` has a unique, normalized, nonnegative source-free invariant mass under this bounded numerical contract. It does not establish nonlinear HJB convergence, a joint HJB-KFE fixed point, stationary economic equilibrium, GE, production readiness, or Results eligibility.

Commit and non-force push the task branch. Do not merge main. Do not publish a successor task.
