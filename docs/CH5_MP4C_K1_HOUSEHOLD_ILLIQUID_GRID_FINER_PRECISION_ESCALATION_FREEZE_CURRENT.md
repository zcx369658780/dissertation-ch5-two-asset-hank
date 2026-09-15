# CH5 MP4C K1 — household illiquid-grid finer precision escalation freeze

Date: 2026-09-15

Status: `FINER_ILLIQUID_PRECISION_ESCALATION_FROZEN`

## Authority

This freeze follows accepted Reviewer verdict:

`GRID_GENERIC_RECEIPT_REPAIR_ACCEPTED__ILLIQUID_GRID_PRECISION_NOT_STABILIZED__FINER_PRECISION_ESCALATION_REQUIRED`

Accepted report:

`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_REPORT.md`

Acceptance:

`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`

## Frozen representative state

Exactly:

- `rb=.02`
- `ra=.0675`
- household composite `w=15.5`
- `amin=0`
- `amax=100`
- `bmin=-2`
- `bmax=20`
- `I=20`
- `Nz=2`
- diagnostic monetary bridge `h=1`

All household economic parameters, initialization logic, HJB/KFE equations, FOC, selector, boundaries, derivative floor, solver, tolerance, max iterations, wage/return mappings and guards remain frozen.

## Accepted reference

Use accepted fresh `I=20,J=160` evidence from the preceding re-execution as the coarsest reference. Do not rerun J160 science.

Accepted J160 facts include approximately:

- `At=89.29782531`
- `Bt=5.81025383`
- modal `a=94.33962264`
- modal `b=2.63157895`
- `amax` mass `0`
- `bmax` mass `0.00097740`

These are reference facts, not production calibration authority.

## Authorized finer ladder

Run exactly three new fresh standalone points:

1. `I=20,J=320`
2. `I=20,J=640`
3. `I=20,J=1280`

No other J is authorized.

Approximate `da` values:

- J320: `100/319 ≈ 0.3134796238`
- J640: `100/639 ≈ 0.1564945227`
- J1280: `100/1279 ≈ 0.0781860829`

No warm starts.

## Purpose

Determine whether the expanded illiquid asset distribution approaches a stable level/shape as J rises beyond 160, and whether the continuing upward movement of modal `a` represents finite-grid resolution or a deeper domain/scale issue.

This task does not test liquid-grid precision and does not authorize cross-state confirmation.

## Required scientific receipts

For every new point record and persist before postprocessing validation:

- actual grid supports and shapes;
- HJB value, consumption, labor, transfer, multipliers/policies available from accepted oracle;
- raw KFE density;
- HJB convergence iterations/statistic and A2max;
- KFE total mass/residual/raw signed density diagnostics;
- `Ct,Lt,At,Bt`;
- full a/b marginals;
- modal a/b;
- endpoint masses;
- top bins.

No clipping, smoothing, science-changing renormalization, or post-result threshold fitting.

## Comparisons

Compute deterministic pairwise comparisons:

- J160 -> J320
- J320 -> J640
- J640 -> J1280

At minimum compare:

- `Ct,Lt,At,Bt`;
- modal a/b;
- amin/amax/bmin/bmax masses;
- full a marginal distance;
- full b marginal distance;
- location of upper quantiles if deterministically available from raw marginal.

Use the already frozen marginal-distance method from the accepted precision task. Do not change metric definition after seeing results.

## Decision boundary

No new numeric pass threshold may be invented after execution.

If the J640->J1280 refinement is descriptively small relative to the preceding finer refinements and the marginal sequence shows a clear stabilization trend, classify:

`ILLIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED_BY_J1280`

and recommend the smallest defensible J among the tested finer ladder for the next bounded liquid-I or cross-state confirmation.

If the J640->J1280 refinement remains clearly material, modal/aggregate movement persists, or the a-marginal sequence does not show stabilization, classify:

`ILLIQUID_GRID_PRECISION_NOT_STABILIZED_BY_J1280__DOMAIN_OR_SCALE_REVIEW_REQUIRED`

and STOP. Do not run J beyond 1280 in this task.

If HJB/KFE becomes numerically invalid at finer J, report the exact failure without tuning.

## Runtime budget

- new HJB calls: exactly 3 unless a shared preflight blocker occurs;
- new KFE calls: at most 3, exactly one after each legal/converged HJB;
- scientific retries: 0;
- engineering retry: at most 1 and only before the first new HJB for non-scientific path/import/serialization/output-shape defects;
- global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results: all 0.

## Hard stops

No changes to:

- asset bounds;
- I=20;
- economic parameters;
- monetary bridge;
- HJB/KFE science;
- solver/tolerance;
- derivative floor;
- wage/return mapping;
- wjt guard;
- ra mapping;
- J beyond 1280.

No P2 liquid-grid ladder and no multi-state or full 3x3 finer-grid rerun in this task.

Results eligibility=`FALSE`.
