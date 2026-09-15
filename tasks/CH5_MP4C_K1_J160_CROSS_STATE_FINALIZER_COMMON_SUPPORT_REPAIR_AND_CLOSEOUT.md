# Exact task — CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_AND_CLOSEOUT

## Objective

Repair the post-science offline comparison/finalization blocker from the completed J160 bounded cross-state confirmation and close the task **without any new scientific runtime**.

## Authority

Read first:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_J160_CROSS_STATE_POST_SCIENCE_FINALIZATION_BLOCKER_ROUTE_DECISION.md`
6. `docs/CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_FREEZE_CURRENT.md`
7. the original J160 bounded cross-state exact task and freeze
8. accepted J20 and J160 reference evidence.

## Expected existing raw execution

Raw evidence root:

`D:\ProjectTemp\ch5-mp4c-k1-j160-cross-state-evidence-20260915-001`

Previous Builder worktree context:

`D:\ProjectTemp\ch5-mp4c-k1-j160-bounded-cross-state-confirmation-20260915-001`

Do not assume these are trustworthy merely because the paths exist. Verify integrity and content first.

## Phase R0 — raw evidence integrity gate

Before changing finalization code, verify and record:

- raw evidence directory exists;
- raw manifest/seal, if present, validates fully;
- exactly four authorized fresh J160 states exist:
  - `ra=.06,w=13`
  - `ra=.06,w=18`
  - `ra=.07,w=13`
  - `ra=.07,w=18`
- each has exactly one HJB and exactly one completed KFE;
- all four HJBs are legal/converged;
- scientific retries=0;
- center `ra=.0675,w=15.5` is reuse-only;
- all J20 references are reuse-only;
- common frozen inputs are exactly `rb=.02,a=[0,100],b=[-2,20],I=20,J=160,Nz=2,h=1` for new J160 points;
- forbidden runtime is zero.

If any required raw science object is missing or inconsistent, STOP with:

`J160_CROSS_STATE_RAW_EVIDENCE_INTEGRITY_BLOCKER`

Do not rerun HJB/KFE.

## Phase R1 — common-support finalizer repair

Repair only task-owned offline comparison/finalization code.

The original failure:

`ValueError: CDF comparison requires a common support`

arose because J20 references use `a=[0,10],b=[-2,5]` while J160 uses `a=[0,100],b=[-2,20]`.

### Required deterministic metric

Preserve the accepted same-support CDF metric exactly.

For different supports, compare over the union interval:

`[min(x_old.min,x_new.min), max(x_old.max,x_new.max)]`.

For each raw signed marginal:

- CDF=0 below its minimum support;
- within support use the existing cumulative-node-mass and piecewise-linear interpolation convention;
- CDF=raw total marginal mass above its maximum support;
- no clipping;
- no science-changing renormalization;
- no smoothing;
- no outcome-fitted rebinning.

Distance:

`integral |F_old-F_new| dx / union_support_width`.

For J20→J160 this must be named and described as:

`DOMAIN_PLUS_GRID_CDF_DISTANCE`

because the economic domain and grid both changed.

Do not call it pure precision distance.

### Regression tests

Focused tests must include at least:

- same-support regression reproduces prior accepted metric;
- different a-support fixture `[0,10]` vs `[0,100]` returns finite deterministic distance;
- different b-support fixture `[-2,5]` vs `[-2,20]` returns finite deterministic distance;
- exterior extension is exactly 0 below min and raw total mass above max;
- raw signed mass is neither clipped nor normalized;
- zero-width/invalid support fails closed.

No science calls are permitted in tests.

## Phase R2 — offline finalization only

After R0 and R1 pass, run the finalizer using the already-completed raw science and accepted reuse-only references.

Generate the originally required five-state J20→J160 comparisons for:

- `(.06,13)`
- `(.06,18)`
- `(.0675,15.5)`
- `(.07,13)`
- `(.07,18)`

Report for each state:

- HJB status/iterations;
- KFE status;
- `Ct,Lt,At,Bt`;
- modal a/b;
- endpoint masses;
- `DOMAIN_PLUS_GRID_CDF_DISTANCE` for a and b;
- clear note that these distances combine domain expansion and discretization change.

## Scientific decision closeout

The final report may classify:

`J160_BOUNDED_CROSS_STATE_CONFIRMATION_PASS__PRACTICAL_DIAGNOSTIC_GRID_SUPPORTED`

only if the verified raw evidence shows:

- all four fresh J160 HJBs legal/converged;
- all four KFE completions valid/nonpathological;
- a distributions scientifically interpretable;
- `amax=100` nonbinding at all new points;
- `bmax=20` nonbinding in the bounded diagnostic sense;
- cross-state aggregates/distributions coherent enough for bounded diagnostic use.

This PASS means only practical diagnostic-grid support. It does **not** establish continuum convergence, production-final precision, GE validity, or Results eligibility.

If the verified evidence does not support that closeout, classify truthfully and route to Reviewer.

## Zero-science-runtime budget

- HJB=0
- KFE=0
- scientific retries=0
- J20/J160/J320/J640/J1280 science=0
- global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0

Engineering iterations are allowed only in task-owned offline finalizer/tests and must not invoke scientific solvers.

## Required outputs

Formal report:

`docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_REPORT.md`

Compact evidence:

`docs/evidence/ch5_mp4c_k1_j160_bounded_cross_state_confirmation/`

At minimum:

- `source_identity.json`
- `raw_evidence_integrity_receipt.json`
- `input_invariance_receipt.json`
- `points.csv`
- `point_receipts.json`
- `marginals.json`
- `j20_j160_comparison.json`
- `finalizer_repair_receipt.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

Focused tests and task-owned finalizer code are allowed.

## Git workflow

Fresh-fetch live `main` and record actual baseline.

Use a fresh isolated worktree and fresh branch.

Do not use reset/clean/stash/force push. Do not use `git add .` or `git add -A`.

Explicit-stage only authorized paths.

Create one coherent Builder commit, non-force push, and perform exactly one remote readback.

Do not merge main. Do not publish a successor task.

## Final response

Start with terminal classification, then report:

- actual baseline;
- branch/worktree/candidate SHA;
- raw evidence integrity result;
- zero-science call ledger;
- finalizer repair summary and regression tests;
- four fresh corner results;
- reused center result;
- five-state J20→J160 comparison;
- a-domain conclusion;
- b-domain conclusion;
- cross-state coherence conclusion;
- whether J160 practical diagnostic grid is supported;
- KFE caveat;
- Results eligibility=`FALSE`;
- exactly one next gate: `REVIEWER_J160_CROSS_STATE_ROUTE_DECISION`.

STOP after publishing the candidate.
