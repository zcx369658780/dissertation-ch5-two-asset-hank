# CH5 MP4C K1 — household illiquid-grid finer precision escalation

Date: 2026-09-15
Task ID: `CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION`

## Goal

Continue the accepted representative-state precision ladder beyond J160 using the repaired grid-generic receipt route, without changing economics, domains or household science.

## Mandatory authority

Read live:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_FREEZE_CURRENT.md`
7. accepted repair/re-execution report/evidence
8. accepted MATLAB-faithful HJB/KFE authority and source provenance.

## Frozen representative state

Exactly:

- `rb=.02`
- `ra=.0675`
- `w=15.5`
- `a=[0,100]`
- `b=[-2,20]`
- `I=20`
- `Nz=2`
- `h=1`

No warm starts.

Reuse accepted `I=20,J=160` result as the reference. Do not rerun J160 science.

## Exact new science points

Run exactly:

1. `I=20,J=320`
2. `I=20,J=640`
3. `I=20,J=1280`

No other J or I values.

For each point:

- fresh source initialization;
- exactly one HJB;
- if and only if HJB is legal/converged, exactly one KFE;
- persist scientific arrays/raw density/grid support immediately after KFE numeric return and before receipt validation.

## Record

For each point record:

- `I,J,da,db`;
- HJB class, iterations, final `max|ΔV|`, max A2max and legality;
- KFE total mass, residual, raw density minimum and negative count;
- `Ct,Lt,At,Bt`;
- modal a/b;
- amin/amax/bmin/bmax masses;
- full a/b marginals;
- top bins;
- deterministic upper-quantile locations if supported by the raw marginal and implemented without science alteration.

Do not clip or smooth signed density.

## Precision comparisons

Using accepted J160 as reference and new points, calculate:

- J160->J320
- J320->J640
- J640->J1280

Compare at least:

- `ΔCt,ΔLt,ΔAt,ΔBt`;
- modal a/b movement;
- endpoint-mass movement;
- full a marginal distance;
- full b marginal distance;
- upper-quantile movement if available.

Use the previously frozen deterministic marginal-distance methodology. No post-result threshold fitting.

## Decision

If the J640->J1280 refinement is descriptively small relative to the preceding finer refinements and the full distribution sequence shows a clear stabilization trend, terminal classification may be:

`ILLIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED_BY_J1280`

Then report the smallest defensible tested J for the next bounded confirmation. Do not run the next task.

If the final refinement remains clearly material, modal/aggregate movement persists, or marginal-shape changes fail to stabilize, terminal classification must be:

`ILLIQUID_GRID_PRECISION_NOT_STABILIZED_BY_J1280__DOMAIN_OR_SCALE_REVIEW_REQUIRED`

Stop. Do not run J>1280.

If a finer-J HJB/KFE becomes invalid, preserve the exact failure and stop without tuning.

## Runtime budget

- HJB new calls: exactly 3 unless shared preflight blocker;
- KFE new calls: <=3;
- scientific retries: 0;
- engineering retry: <=1, only before the first new HJB and only for non-scientific path/import/serialization/output-shape defects;
- global multi-province outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results: all 0.

## Forbidden

Do not change:

- asset bounds;
- `I=20`;
- economic parameters;
- HJB/KFE equations/numerics;
- solver/tolerance/maxit;
- FOC/selector/boundary;
- derivative floor;
- `h=1` bridge;
- wage/return mapping;
- `wjt` guard;
- `ra` mapping.

Do not run:

- J>1280;
- liquid-I precision ladder;
- multi-state/finer 3x3 confirmation;
- global model.

## Required outputs

Create:

- `docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_REPORT.md`
- compact evidence under `docs/evidence/ch5_mp4c_k1_household_illiquid_grid_finer_precision_escalation/`

At minimum:

- `source_identity.json`
- `input_invariance_receipt.json`
- `precision_points.csv`
- `point_receipts.json`
- `marginals.json`
- `precision_comparison.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

Task-owned runner/finalizer/tests and truthful CURRENT closeout docs are allowed. Accepted household scientific source is not.

## Final questions

1. Does `At` stabilize beyond J160?
2. Does modal `a` stabilize or continue moving toward the upper domain?
3. Does the full a marginal stabilize?
4. Is `amax=100` still nonbinding in distributional terms at finer J?
5. Does fixed-I liquid evidence remain nonbinding at bmax=20?
6. Is the old-domain to expanded-domain jump now separable into dominant domain response plus a converged discretization component?
7. What is the smallest defensible tested J for a next bounded cross-state/liquid-I confirmation, if any?
8. Exactly one next Reviewer gate: bounded liquid-I/cross-state confirmation or domain/scale review.

Results eligibility=`FALSE`.

## Git workflow

Fresh-fetch live main and record actual baseline. Use a fresh isolated worktree and branch. No reset/clean/stash/force push. Explicit staging only; no `git add .` or `git add -A`. One coherent Builder commit, non-force push, one remote readback. Do not merge main and do not publish a successor task.

Stop for independent ChatGPT Reviewer acceptance.
