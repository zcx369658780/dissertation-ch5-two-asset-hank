# Task — CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC

## Goal

Diagnose the accepted J640 HJB nonconvergence mechanism at the identical frozen representative household state without changing scientific equations, numerical algorithm, tolerance, or maxit.

## Required reads

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_FREEZE_CURRENT.md`
7. accepted finer-precision report/evidence and prior accepted HJB mechanism-diagnostic evidence where relevant.

## Phase 0 — governance / preflight

Fresh-fetch `origin/main`; record actual baseline. Use fresh isolated worktree and branch. Verify protected HJB/KFE source, oracle, MATLAB source, accepted J640 inputs, tolerance, and maxit identities. No scientific runtime until preflight is clean.

## Phase 1 — diagnostic instrumentation

Add task-owned instrumentation only. Do not modify the accepted HJB scientific source behavior. The wrapper/instrumentation may record per-iteration values already computed by the accepted algorithm.

Required per-iteration receipt:
- `max(abs(V_new-V_old))`
- argmax coordinate and signed dV
- A2max / legality
- finite/shape checks
- liquid selector-label changes versus previous iteration
- transfer/illiquid selector-label changes versus previous iteration
- deterministic policy-change counts when available without science changes
- derivative-floor hit count and first-hit iteration
- hashes of V and selector-label arrays
- repeated-hash / low-period-cycle detection

Focused tests must prove instrumentation does not alter a controlled accepted small-grid result and preserves maxit/tolerance semantics.

## Phase 2 — exactly one J640 diagnostic replay

Frozen inputs exactly:
- rb=.02
- ra=.0675
- w=15.5
- a=[0,100]
- b=[-2,20]
- h=1
- I=20
- J=640
- Nz=2
- fresh source initialization
- maxit=100
- accepted tolerance unchanged

Run exactly one HJB. No warm start. No retry.

If it reproduces nonconvergence, classify the mechanism using the frozen classes in the freeze doc. If it unexpectedly converges, terminal classification must be a reproducibility blocker and stop. In either case KFE=0 and J1280=0.

## Phase 3 — mechanism analysis

Compare iteration dynamics against prior accepted mechanism evidence only descriptively. Establish ordering of:
- policy/selector switching
- value-stat non-decrease/oscillation
- derivative-floor first hit
- repeated/cycling state evidence

Do not infer causality beyond observed temporal ordering. Do not propose algorithm changes inside the Builder task.

## Runtime budget

- HJB: exactly 1 after clean preflight
- KFE: 0
- J1280: 0
- scientific retries: 0
- engineering retry: at most 1 before HJB and only for path/import/serialization/instrumentation plumbing, with science unchanged
- global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results: 0

## Required outputs

Report:
`docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_REPORT.md`

Evidence directory:
`docs/evidence/ch5_mp4c_k1_j640_hjb_nonconvergence_mechanism_diagnostic/`

At least:
- `source_identity.json`
- `input_invariance_receipt.json`
- `iteration_trace.csv` or JSON
- `mechanism_summary.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

Exactly one terminal next Reviewer gate:
`REVIEWER_J640_HJB_MECHANISM_ROUTE_DECISION`

## Git workflow

Fresh branch/worktree from fresh-fetched main. No reset/clean/stash/force. Explicit staging only. One coherent Builder commit. Non-force push. One remote readback. Do not merge main. Do not publish successor task.
