# CH5 MP4C K1 — household asset-grid precision receipt repair and re-execution

Date: 2026-09-15
Task ID: `CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION`

## Goal

Repair the grid-size-specific receipt/postprocessing defect exposed by the accepted blocked precision execution, then re-execute the identical frozen precision ladder so the originally requested KFE evidence can be obtained without changing household science.

## Mandatory authority

Read live `AGENTS.md`, project rule index, CURRENT status/handoff, accepted Stage A authority, the original precision freeze/task/report, `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_BLOCKED_EXECUTION_ACCEPTANCE.md`, and `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_FREEZE_CURRENT.md`.

## Phase R0 — engineering repair before science

Repair only task-owned receipt/postprocessing code so it supports the actual authorized grid dimensions instead of requiring an illiquid marginal length of 20.

Requirements:

- preserve the accepted HJB and KFE numerical solvers unchanged;
- derive marginal lengths/support from the actual fixture/result;
- persist raw returned density and complete scientific arrays before grid-size-dependent validation can discard them;
- preserve raw signed density; no clipping, smoothing or science-changing renormalization;
- maintain the previously frozen distribution/aggregate definitions;
- add focused tests for `J=20,40,80,160` receipt extraction and, where applicable, `I=20,40,80` liquid marginals;
- prove accepted `I=J=20` receipt behavior is unchanged up to serialization/metadata ordering.

R0 may use synthetic/test fixtures and no HJB/KFE science calls. If R0 cannot pass, stop before science.

## Frozen representative state

Exactly:

- `rb=.02`
- `ra=.0675`
- `w=15.5`
- `amin=0`, `amax=100`
- `bmin=-2`, `bmax=20`
- diagnostic bridge `h=1`
- all science/numerics unchanged except authorized `I/J` density.

No warm starts.

## Stage P1 — mandatory fresh re-execution

Reuse accepted `I=20,J=20` Stage A evidence as reference; do not rerun it.

After R0 passes, run exactly three fresh science points:

1. `I=20,J=40`
2. `I=20,J=80`
3. `I=20,J=160`

For each point run exactly one HJB and, only if legal/converged, exactly one KFE.

Persist, before postprocessing can fail:

- complete HJB scientific arrays;
- complete raw KFE density;
- grid supports and shapes.

Then produce the full original receipts:

- HJB convergence/iterations/final `max|ΔV|`/max `A2max`/legality;
- KFE mass/residual/signed-density diagnostics;
- `Ct,Lt,At,Bt` and `Bt_pos/Bt_neg` if available;
- modal `a/b`;
- endpoint masses;
- full `a/b` marginals and top bins;
- pairwise changes and deterministic common-support marginal distances.

## P1 decision

Publish raw `J20→J40`, `J40→J80`, `J80→J160` changes.

If the final refinement remains clearly material and does not show stabilization, terminal classification must include `ILLIQUID_GRID_PRECISION_NOT_STABILIZED` and Stage P2 must not run.

If the sequence shows clear descriptive stabilization by `J=160`, with legal/converged HJB, valid KFE and nonpathological `a` distribution, proceed to P2.

Do not invent a post-result numeric pass cutoff.

## Stage P2 — conditional

Only if P1 stabilizes.

Fix `J=160` and reuse the fresh `I=20,J=160` P1 result. Run exactly:

1. `I=40,J=160`
2. `I=80,J=160`

Record the same HJB/KFE and marginal diagnostics and `I20→I40`, `I40→I80` pairwise changes.

If the final I refinement remains clearly material, terminal classification must include `LIQUID_GRID_PRECISION_NOT_STABILIZED`.

If P1 and P2 both descriptively stabilize, terminal classification may be `ASSET_GRID_PRECISION_PROVISIONALLY_STABILIZED_AT_REPRESENTATIVE_STATE`.

## Runtime budget

R0 science calls: 0.

P1 new HJB calls: exactly 3 after R0 pass.
P1 new KFE calls: at most 3, one per legal/converged point.

P2 new HJB calls: 0 if P1 does not stabilize; otherwise exactly 2.
P2 new KFE calls: 0 if P1 does not stabilize; otherwise at most 2.

Scientific retries: 0.
Engineering retries: at most 1 before the first new HJB, limited to path/import/serialization/output-shape defects with unchanged science.

Global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results: all 0.

## Hard stops

Stop on any unauthorized change to asset bounds, economics, HJB/KFE equations or numerical solver, tolerance/maxit, FOC/selector/boundary, derivative floor, wage/return mapping or monetary bridge.

Do not automatically run a finer full 3×3 grid or any point outside the frozen ladder.

## Required outputs

Create:

- `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_REPORT.md`
- compact evidence under `docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution/`

At minimum include:

- `source_identity.json`
- `repair_diff_receipt.json`
- `grid_generic_tests_receipt.json`
- `input_invariance_receipt.json`
- `precision_points.csv`
- `point_receipts.json`
- `marginals.json`
- `precision_comparison.json`
- `stage_trigger_receipt.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

Task-owned runner/finalizer/tests and truthful CURRENT closeout docs are allowed. Accepted scientific source is protected.

## Final questions

1. Did the repair remove only the fixed-grid receipt defect without changing accepted science?
2. Does `At`, modal `a`, `amax` mass and the full `a` marginal stabilize as J rises 20→40→80→160?
3. Is the old-domain→expanded-domain `At` jump primarily a domain effect, a coarse-grid effect, or still unresolved?
4. If P2 runs, do `Bt` and the liquid marginal stabilize as I rises 20→40→80?
5. Does `bmax=20` remain nonbinding at finer precision?
6. What is the minimum numerically defensible grid density for the next bounded cross-state confirmation?
7. Exactly one next Reviewer gate: finer precision escalation, bounded multi-state confirmation, or unresolved recalibration.

Results eligibility=`FALSE`.

## Git workflow

Fresh-fetch live main and record actual baseline. Use a fresh isolated worktree/branch. No reset/clean/stash/force push. Explicit staging only. One coherent Builder commit, non-force push, one remote readback. Do not merge main and do not publish a successor task. Stop for independent ChatGPT Reviewer acceptance.
