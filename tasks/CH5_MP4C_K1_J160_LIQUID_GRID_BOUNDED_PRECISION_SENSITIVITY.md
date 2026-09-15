# Exact task — CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY

## Objective

At the accepted practical household grid `J=160`, test whether the remaining liquid-asset discretization at `I=20` is sufficiently stable for bounded diagnostics by refining only I.

## Authority

Read first:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`
7. accepted Stage-A / J160 / J320 / J640 evidence and MATLAB-faithful HJB/KFE authority.

## Frozen specification

- `rb=.02`
- `ra=.0675`
- household composite `w=15.5`
- `a=[0,100]`
- `b=[-2,20]`
- `J=160`
- `Nz=2`
- `h=1`
- accepted HJB/KFE equations, source initialization, FOCs, selectors, boundaries, derivative floors, solver, tolerance `1e-7`, maxit `100`, mappings, guards, and economic parameters unchanged.

## Reuse-only reference

Accepted center:

- `I=20,J=160`
- HJB converged in 16 iterations
- `At≈89.29782531`
- `Bt≈5.81025383`
- modal `a≈94.33962264`
- modal `b≈2.63157895`
- `bmax mass≈0.0009774012`

Do not rerun the reference.

## Exact fresh points

Run exactly:

1. `I=40,J=160`
2. `I=80,J=160`

No other I/J points are authorized.

Liquid spacing:

- I20: `db=22/19≈1.1578947368421053`
- I40: `db=22/39≈0.5641025641025641`
- I80: `db=22/79≈0.27848101265822783`

## Runtime

For each fresh point:

- fresh source initialization;
- exactly one HJB;
- if and only if HJB is legal and converged, exactly one KFE;
- scientific retries=0.

Maximum new calls:

- HJB=2
- KFE<=2
- reference rerun=0
- J320/J640/J1280=0
- global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0.

## Receipts

For each point record:

- I/J/db/da
- HJB classification, iterations, final `max|dV|`, max A2max, first illegal iteration if any, finite/shape checks
- KFE status, total mass, residual, raw density minimum, negative count
- `Ct,Lt,At,Bt`, `Bt_pos/Bt_neg` if available
- modal a/b
- amin/amax/bmin/bmax masses
- full a- and b-marginals
- top bins and deterministic quantiles if available.

## Precision comparison

Compare:

- I20→I40
- I40→I80

Use the already accepted deterministic same-support CDF-distance methodology. Because asset supports and J stay fixed, these are genuine liquid-grid precision comparisons.

At minimum compare:

- Delta Ct/Lt/At/Bt
- modal a movement
- modal b movement
- endpoint-mass changes
- full a-marginal distance
- full b-marginal distance.

Do not invent post-result pass thresholds.

## Decision

If both fresh points are legal/converged, KFE-valid/nonpathological, `bmax=20` remains nonbinding, and I40→I80 is descriptively small relative to I20→I40 for `Bt`, modal b and the full b-marginal, terminal may be:

`J160_LIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED`

Report the smallest defensible tested I for subsequent bounded diagnostics.

If I40→I80 remains clearly material, terminal must be:

`J160_LIQUID_GRID_PRECISION_NOT_STABILIZED`

and STOP. Do not run I160 in this task.

If either point shows HJB nonconvergence/chatter, invalid operator, or serious KFE pathology, report truthfully and STOP. Do not auto-run mechanism diagnostics or tune numerics.

## Prohibited

Do not:

- change `J=160` or asset bounds;
- run I160 or other I;
- increase maxit;
- add damping/relaxation/line search;
- alter tolerance, floors, FOCs, selectors, boundaries, solver, wage/return mappings, guards, or economic parameters;
- use warm starts;
- run J320/J640/J1280;
- run cross-state grids, global model, firm, MATLAB, K1B/K2, GE, downstream, shock, IRF, or Results.

## Required outputs

Report:

`docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_REPORT.md`

Evidence directory:

`docs/evidence/ch5_mp4c_k1_j160_liquid_grid_bounded_precision_sensitivity/`

At minimum:

- `source_identity.json`
- `input_invariance_receipt.json`
- `precision_points.csv`
- `point_receipts.json`
- `marginals.json`
- `precision_comparison.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

Exactly one next gate:

`REVIEWER_J160_LIQUID_GRID_ROUTE_DECISION`

Do not publish a successor task. Results eligibility remains `FALSE`.
