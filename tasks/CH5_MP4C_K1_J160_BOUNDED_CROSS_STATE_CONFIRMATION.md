# Exact task — CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION

## Objective

Test whether the provisional practical illiquid-grid density `J=160` is numerically usable across a bounded set of representative household states, after the finer-J route was closed by accepted J640 policy/selector chatter.

## Authority

Read first:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_FREEZE_CURRENT.md`
7. accepted Stage-A / precision / J320-J640 evidence and MATLAB-faithful HJB/KFE authority.

## Frozen specification

- `rb=.02`
- `a=[0,100]`
- `b=[-2,20]`
- `I=20`
- `J=160`
- `Nz=2`
- `h=1`
- accepted HJB/KFE equations, initialization, selectors, FOCs, boundaries, derivative floors, solver, tolerance `1e-7`, maxit `100`, mappings, guards and economic parameters unchanged.

## Exact cross-state set

Reuse accepted center without runtime:

- C: `ra=.0675, w=15.5`

Fresh-run exactly four corners:

- L-L: `ra=.06, w=13`
- L-H: `ra=.06, w=18`
- H-L: `ra=.07, w=13`
- H-H: `ra=.07, w=18`

No other `(ra,w)` points are authorized.

## Runtime

For each of the four new points:

- fresh source initialization;
- exactly one HJB;
- if and only if HJB is legal and converged, exactly one KFE;
- scientific retries=0.

Accepted center J160 and accepted J20 same-state references are reuse-only and must not be rerun.

Maximum new calls:

- HJB=4
- KFE<=4
- global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0.

## Required receipts

For every point, including reused center in the comparison table, report:

- HJB classification, iterations, final `max|dV|`, max A2max, legality/finite/shape checks;
- KFE status/residual/total mass/density minimum/negative count;
- `Ct,Lt,At,Bt` and `Bt_pos/Bt_neg` when available;
- modal `a`, modal `b`;
- amin/amax/bmin/bmax masses;
- full a- and b-marginals;
- top bins and upper-a quantiles when deterministically available.

## Comparison

Use the accepted J20 real-wage 3x3 results for the same five states as comparison references.

For each state compare J20→J160:

- HJB convergence/iterations;
- `Ct,Lt,At,Bt`;
- modal a/b;
- endpoint masses;
- a/b marginal distances using the already accepted deterministic CDF-distance methodology.

Do not invent post-result pass thresholds.

## Decision

If all four new J160 HJBs are legal/converged, KFE-valid/nonpathological, `bmax=20` remains nonbinding, and cross-state distributions remain scientifically interpretable, terminal may be:

`J160_BOUNDED_CROSS_STATE_CONFIRMATION_PASS__PRACTICAL_DIAGNOSTIC_GRID_SUPPORTED`

This means only that J160 is supported as a practical bounded diagnostic grid. It does not mean continuum convergence or production-final precision.

If one or more points reproduce persistent HJB chatter/nonconvergence or serious KFE pathology, terminal must identify the failure truthfully and route back to Reviewer.

## Prohibited

Do not:

- run J320/J640/J1280;
- change I/J/domain;
- increase maxit;
- add damping/relaxation/line search;
- alter tolerance, floors, FOCs, selectors, boundaries, solver, wage/return mappings, guards or economic parameters;
- run global/GE/Results paths.

## Outputs

Report:

`docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_REPORT.md`

Evidence directory:

`docs/evidence/ch5_mp4c_k1_j160_bounded_cross_state_confirmation/`

At minimum:

- `source_identity.json`
- `input_invariance_receipt.json`
- `points.csv`
- `point_receipts.json`
- `marginals.json`
- `j20_j160_comparison.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

Exactly one next gate:

`REVIEWER_J160_CROSS_STATE_ROUTE_DECISION`

Do not publish a successor task. Results eligibility remains `FALSE`.
