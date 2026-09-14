# CH5 MP4C K1 — household asset-grid precision sensitivity diagnostic

Date: 2026-09-14
Task ID: `CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC`

## Goal

Determine whether the expanded household asset domains accepted for diagnostic use are numerically stable with respect to grid density, without changing economic domains, parameters, equations, guards or the temporary diagnostic monetary bridge.

## Mandatory authority

Read live `AGENTS.md`, project rule index, CURRENT status/handoff, `docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_ACCEPTANCE.md`, `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`, accepted Stage A report/evidence, accepted MATLAB-faithful HJB/KFE authority and designated source/provenance.

## Frozen representative state

Exactly:

- `rb=.02`
- `ra=.0675`
- `w=15.5`
- `amin=0`, `amax=100`
- `bmin=-2`, `bmax=20`
- diagnostic bridge `h=1`
- all science/numerics unchanged except authorized `I/J` grid density.

No warm starts.

## Stage P1 — mandatory illiquid precision ladder

Reuse accepted `I=20,J=20` Stage A evidence as the reference. Do not rerun it unless a task-owned receipt requires a no-science readback check.

Run exactly three new fresh science points:

1. `I=20,J=40`
2. `I=20,J=80`
3. `I=20,J=160`

No other `J` values.

For each point run exactly one HJB and, only if converged/legal, exactly one KFE.

Record:

- HJB converged flag, iterations, final `max|ΔV|`, max `A2max`, legality failure if any;
- KFE mass/residual/signed-density receipts;
- `Ct,Lt,At,Bt`;
- modal `a`, modal `b`;
- `amin/amax/bmin/bmax` mass;
- full `a` and `b` marginals;
- top bins;
- pairwise changes against the immediately coarser grid.

Compute descriptive marginal distances using deterministic metrics such as L1 distance after mapping/coarsening onto a common support where well-defined; preserve exact methodology and do not use the metric as a post-hoc pass threshold.

## P1 decision

Publish raw changes for:

- J20→J40
- J40→J80
- J80→J160

If the final refinement remains clearly material and does not show stabilization, terminal classification must include `ILLIQUID_GRID_PRECISION_NOT_STABILIZED`; Stage P2 must not run.

If the sequence shows clear stabilization by J160 with legal/converged HJB, valid KFE and interior/nonpathological `a`, proceed to P2.

Do not invent a new numerical cutoff after seeing results.

## Stage P2 — conditional liquid precision ladder

Only if P1 is provisionally stabilized.

Use `J=160` and the same exact representative household input/domain.

Reuse the `I=20,J=160` P1 result as reference. Run exactly two new fresh science points:

1. `I=40,J=160`
2. `I=80,J=160`

No other `I` values.

Record the same HJB/KFE and marginal diagnostics and pairwise changes.

If the I40→I80 change remains clearly material, terminal classification must include `LIQUID_GRID_PRECISION_NOT_STABILIZED`.

If P1 and P2 are both descriptively stabilized, terminal classification may be `ASSET_GRID_PRECISION_PROVISIONALLY_STABILIZED_AT_REPRESENTATIVE_STATE`.

## Runtime budget

P1 new HJB calls: exactly 3 unless shared preflight blocker.

P1 new KFE calls: at most 3, exactly one per converged/legal point.

P2 new HJB calls: 0 if P1 does not stabilize; otherwise exactly 2.

P2 new KFE calls: 0 if P1 does not stabilize; otherwise at most 2.

Scientific retries: 0.

Engineering retry: at most 1 and only before the first new HJB, for path/import/serialization/output-shape defects with unchanged science.

Global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results: all 0.

## Hard stops

Stop on any unauthorized change to asset bounds, household economic parameters, HJB/KFE equations, solver/tolerance/maxit, FOC/selector/boundary, derivative floor, wage/return mapping, monetary bridge, or any science point outside the authorized precision ladder.

Do not automatically run a finer full 3×3 grid.

## Required outputs

Create:

- `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC_REPORT.md`
- compact evidence under `docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_sensitivity/`

At minimum compact evidence must include:

- `source_identity.json`
- `input_invariance_receipt.json`
- `precision_points.csv`
- `point_receipts.json`
- `marginals.json`
- `precision_comparison.json`
- `stage_trigger_receipt.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

Allow task-owned runner/finalizer/tests and truthful CURRENT closeout docs only.

## Final questions

1. Does the illiquid level (`At`, modal `a`, marginal shape, endpoint mass) stabilize as J rises from 20 to 160?
2. Is the large old→expanded-domain `At` jump primarily domain response, coarse-grid response, or still unresolved?
3. If P2 runs, does the liquid distribution and `Bt` stabilize as I rises 20→40→80?
4. Does `bmax=20` remain safely nonbinding at finer precision?
5. What is the smallest numerically defensible grid density for the next bounded cross-state confirmation?
6. Exactly one next Reviewer gate: finer precision escalation, bounded multi-state confirmation, or unresolved recalibration.

Results eligibility=`FALSE`.

## Git workflow

Fresh-fetch live main; record actual baseline; use fresh isolated worktree/branch; no reset/clean/stash/force push; explicit staging only; one coherent Builder commit; non-force push; one remote readback; do not merge main; do not publish a successor task.

Stop for independent ChatGPT Reviewer acceptance.
