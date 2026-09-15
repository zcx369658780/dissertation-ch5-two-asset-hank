# Task — CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION

Status: ACTIVE

## Objective
Repair the task-owned A2max receipt boundary and reexecute exactly the same 12 preregistered local-basin probes so formal pair topology can be decided with valid scientific legality receipts.

## Required reads
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_FREEZE_CURRENT.md`
7. accepted blocked report/evidence
8. accepted MATLAB-faithful HJB authority

## Phase 0
Fresh-fetch `origin/main`; record actual baseline; use fresh isolated worktree/branch. Verify source identities, accepted pair authority and exact synthetic inputs from the blocked run. If authority is incomplete, STOP before science.

## Phase 1 — receipt repair
Repair only task-owned observer/aggregator code so scientific A2max includes only source-generator A2max values from actual HJB iterations. Exclude the post-convergence implicit system matrix and any `iterations+1` object. Add focused tests proving no scientific behavior changes.

Required per-probe receipt:
- `scientific_iteration_count`;
- A2max sequence length exactly equal to it;
- exact `max_scientific_A2max`;
- argmax iteration;
- first scientific illegal iteration or null;
- optional post-convergence matrix metric under a separately named non-scientific field.

## Exact reexecution
Reexecute exactly these 12 points, fresh initialization, one HJB each:
- 山西→河北: t=.25,.50,.75
- 重庆→河北: t=.25,.50,.75
- 江西→安徽: t=.25,.50,.75
- 贵州→四川: t=.25,.50,.75

Use the exact same synthetic `(ra,w)` values already sealed by the blocked run. Do not recompute them from rounded chat values. Endpoints are reuse-only.

Frozen science: `I=20,J=160,Nz=2,a=[0,100],b=[-2,20],h=1,Delta=1000,tol=1e-7,maxit=100,A2max_gate=.01`; all equations/FOCs/selectors/boundaries/floors/solver unchanged. KFE=0.

## Reproducibility
Compare each rerun against the blocked raw outcome:
- 山西→河北: C,C,C
- 重庆→河北: C,C,C
- 江西→安徽: F,C,C
- 贵州→四川: C,F,C

Also compare iteration counts and final max|dV|. Any unexpected divergence is reported and not retried.

## Pair topology
Only after all 12 scientific legality receipts are valid, classify each pair exactly one:
- `SINGLE_TRANSITION_FAILURE_TO_SUCCESS`
- `ALL_INTERIOR_PROBES_CONVERGE`
- `ALL_INTERIOR_PROBES_FAIL`
- `NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN`
- `PAIR_NUMERICAL_INVALIDITY_BLOCKER`

Panel exactly one:
- `LOCAL_BASIN_BOUNDARIES_SIMPLE_AND_PAIR_SPECIFIC`
- `LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`
- `LOCAL_BASIN_EVIDENCE_NUMERICALLY_BLOCKED`

No post-result probes or bisection.

## Runtime budget
HJB exactly12; KFE=0; endpoint HJB=0; scientific retries=0; engineering retry <=1 before first HJB only; all outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0.

## Required outputs
Report:
`docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_REPORT.md`

Evidence:
`docs/evidence/ch5_mp4c_k1_j160_local_basin_a2max_receipt_repair_and_reexecution/`

At least:
- `source_identity.json`
- `pair_input_authority.json`
- `receipt_repair_invariance.json`
- `probe_receipts.json`
- `reproducibility_comparison.json`
- `pair_topology.json`
- `panel_decision.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

## Git workflow
Fresh isolated branch/worktree; explicit staging only; no reset/clean/stash/force push; one coherent Builder commit; non-force push; exactly one remote readback; do not merge main; do not publish successor task.

## Final response
Start with panel terminal class, then report actual baseline, branch/worktree/candidate, receipt repair and invariance, 12 scientific A2max maxima and legality, 12 terminal outcomes and reproducibility, four pair sequences/classes, panel interpretation, runtime ledger, KFE=0, Results eligibility=FALSE, and exactly one next gate:

`REVIEWER_J160_LOCAL_BASIN_REEXECUTION_ROUTE_DECISION`

Then STOP.
