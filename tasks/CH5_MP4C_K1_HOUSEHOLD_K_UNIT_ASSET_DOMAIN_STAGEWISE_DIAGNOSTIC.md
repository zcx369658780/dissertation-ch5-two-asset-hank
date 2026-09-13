# CH5 MP4C K1 — household k-unit asset-domain stagewise diagnostic

Date: 2026-09-14
Task ID: `CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC`

## Goal

Implement only the task-owned diagnostic configuration frozen in `docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_BRIDGE_AND_ASSET_DOMAIN_DIAGNOSTIC_FREEZE_CURRENT.md` and determine whether expanding household asset domains resolves the accepted artificial boundary behavior without changing HJB/KFE science.

Results eligibility=`FALSE`.

## Mandatory authority

Read live `AGENTS.md`, rule index, CURRENT status/handoff, the accepted k-unit/domain design audit acceptance, the new household k-unit/domain freeze, accepted real-wage standalone report/evidence, accepted MATLAB-faithful HJB/KFE authority, and source provenance.

## Exact diagnostic convention

For this task only use temporary household bridge `h=1`: existing household monetary numerics are provisionally treated as k-unit numerics with no numerical rescaling.

Do not alter `alphac`, `a_bar`, derivative floor, drift tolerance, rates, wage input, transfer, FOC, selectors, HJB/KFE equations, solver or tolerances.

## Stage A — mandatory

Grid/domain:

- `I=20`, `J=20`, `Nz=2`;
- `amin=0`, `amax=100`;
- `bmin=-2`, `bmax=20`;
- `rb=.02`;
- `ra={.06,.0675,.07}`;
- household composite `w={13,15.5,18}`.

Run exactly 9 Cartesian points with fresh initialization and no warm start.

Each point gets exactly one HJB. Only HJB-converged points get exactly one KFE.

## Stage B — conditional and pre-authorized

After all Stage A points are complete, inspect only the raw liquid-asset marginal modes.

If at least one Stage A converged/KFE-valid point has modal `b` exactly equal to `bmax=20`, activate Stage B.

Stage B changes only `bmax` from `20` to `50`; all other scientific inputs and numerics remain identical. Run exactly 9 fresh points. No warm start from Stage A.

If no Stage A point has modal `b=20`, Stage B calls must be zero.

No domain expansion beyond `bmax=50` is authorized.

## HJB receipts

For each executed point record:

- stage;
- `(rb,ra,w)`;
- fresh-init identity;
- converged flag;
- iteration count;
- final `max(abs(V_new-V_old))`;
- maximum `A2max=max(abs(sum(A,2)))`;
- first illegal iteration;
- nonfinite/hard-error reason;
- expected array shapes and label domains.

HJB class must be exactly one of:

- `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`;
- `HJB_NOT_CONVERGED`;
- `HJB_CONVERGED`.

## KFE receipts

For each HJB-converged point record:

- total mass;
- `Ct,Lt,At,Bt`;
- `Bt_pos,Bt_neg` if available;
- full 20-bin `a` marginal;
- full 20-bin `b` marginal;
- exact `amin,amax,bmin,bmax` masses;
- interior mass for each asset;
- modal `a` and modal `b`;
- top three bins for `a` and for `b`;
- KFE residual;
- density minimum and negative-count;
- finite/shape receipts.

Do not clip signed mass.

## Domain interpretation

For `a`, preserve the accepted descriptive logic and publish raw marginals.

For `b`, classify:

- `B_INTERIOR_DISTRIBUTION_CANDIDATE`;
- `B_LOWER_BOUNDARY_DOMINATED`;
- `B_UPPER_BOUNDARY_PILEUP`;
- `B_TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`;
- `KFE_NUMERICALLY_PATHOLOGICAL`.

No post-result percentage threshold may be fitted. Exact endpoint modal location is authoritative for the boundary labels.

## Comparison

Use the accepted prior same-input real-wage scan (`a=[0,10]`, `b=[-2,5]`) as comparison baseline.

For every common `(ra,w)` report changes in:

- HJB convergence/iterations/A2max;
- `Ct,Lt,At,Bt`;
- modal `a`, `a` endpoint masses;
- modal `b`, `b` endpoint masses;
- KFE residual/signed density.

Do not interpret domain-induced changes as GE/calibration improvements.

## Decision rules

If Stage A has zero exact-`bmax` modal points and all 9 HJBs are legal/converged with no material KFE pathology, recommend exactly one next gate:

`OWNER_REVIEW_ASSET_DOMAIN_STAGE_A_ACCEPTANCE_AND_PRECISION_SENSITIVITY`

If Stage B is activated and has zero exact-`bmax` modal points with legal/converged HJBs and no material KFE pathology, recommend:

`OWNER_REVIEW_ASSET_DOMAIN_STAGE_B_ACCEPTANCE_AND_PRECISION_SENSITIVITY`

If Stage B is activated and any point still has exact `bmax=50` mode, or new serious HJB/KFE pathology appears, recommend:

`OWNER_REVIEW_ASSET_DOMAIN_OR_HOUSEHOLD_SCALE_RECALIBRATION_UNRESOLVED`

Recommend exactly one. Do not execute a successor task.

## Runtime budget

Stage A:

- HJB exactly 9 unless shared preflight corruption;
- KFE <=9, one per converged HJB.

Stage B:

- either HJB=0/KFE=0, or HJB exactly 9 and KFE<=9 according to the frozen trigger.

Scientific retries=0. One engineering retry is allowed only before the first HJB call for path/import/serialization/output-shape defects with identical science.

Global outer turns, firm runtime, MATLAB runtime, K1B/K2, GE, downstream, shock, IRF, Results: all 0.

## Hard stops

Stop on any unauthorized scientific-source change, `wjt` or `ra` mapping change, HJB/KFE/tolerance/grid-count change, `h!=1` monetary rescaling, unregistered parameter point, or expansion beyond `bmax=50`.

## Required outputs

Create:

- `docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_household_k_unit_asset_domain_stagewise/`;
- task-owned runner/finalizer/tests as needed;
- truthful CURRENT closeout docs.

Compact evidence must include at least:

- `input_invariance_receipt.json`;
- `stage_trigger_receipt.json`;
- `call_ledger.json`;
- `points.csv`;
- `point_receipts.json`;
- `marginals.json`;
- `baseline_comparison.json`;
- `source_identity.json`;
- `sealed_manifest_sha256.json`.

## Git workflow

Fresh-fetch live main and record actual baseline. Use a fresh isolated worktree/branch. No reset/clean/stash/force push. No `git add .` or `git add -A`; explicit staging only.

One coherent Builder commit, non-force push, one remote readback. Do not merge main. Do not publish a successor task.

## Final response

Return terminal classification first, then actual baseline/branch/worktree/candidate SHA, changed paths, Stage A results, Stage B trigger and results if any, complete HJB/KFE call ledger, 3×3 matrices for each executed stage, per-point asset-domain receipts, comparison with prior accepted baseline, exactly one recommended next gate, KFE caveat, and `Results eligibility=FALSE`.

Stop for independent ChatGPT Reviewer acceptance.
