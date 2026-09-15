# Exact task — J160 six-failure trace spatial localization audit

Task ID：`CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT`

## Purpose

Use only the accepted/sealed six-province iteration traces and accepted receipts to identify where numerical instability is expressed in `(b,a,z)` state space. This is an offline evidence-analysis task. No new scientific runtime is authorized.

## Required authority

Read and verify:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
- `docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_ACCEPTANCE.md`
- accepted six-failure diagnostic report and sealed evidence
- accepted J640 mechanism authority for descriptive comparison only

Fresh-fetch `origin/main` before work and record actual baseline.

## Hard runtime gate

Scientific/model runtime must remain exactly zero:

- HJB=0
- KFE=0
- outer=0
- firm=0
- wage recalculation=0
- return recalculation=0
- MATLAB=0
- K1B/K2/GE/downstream/shock/IRF/Results=0

Do not rerun or recompute household solutions. Do not alter accepted scientific source.

## Evidence identity gate

Verify the accepted six-failure sealed manifest and trace files. If any required trace/hash/receipt is missing or inconsistent, STOP with:

`TRACE_SPATIAL_LOCALIZATION_AUTHORITY_BLOCKED`

## Required analysis

For each of 天津、山西、江西、重庆、贵州、甘肃, analyze the existing 100-iteration trace and report, where available from sealed evidence:

1. Value-update argmax location over time: `(b index/value, a index/value, z index/value)`.
2. Whether argmax observations are at `bmin`, `bmax`, `amin`, `amax`, near-boundary bands, or interior.
3. Selector-switch spatial footprint: changed-cell counts and state-space concentration by liquid/illiquid boundary versus interior. If raw changed-cell coordinates are not present in the sealed trace, explicitly report `COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE` rather than inventing them.
4. Derivative-floor activation spatial footprint and timing. If only hit counts/timing exist but not coordinates, explicitly distinguish count evidence from coordinate evidence.
5. For 贵州, localize the exact joint-selector period-2 recurrence as far as sealed evidence permits; distinguish hash recurrence from value recurrence and from coordinate-resolved recurrence.
6. For the four chatter provinces, test whether their spatial signatures are materially common or heterogeneous.
7. Compare 江西 and 贵州 against the four chatter provinces without converting descriptive differences into causal claims.
8. Compare with accepted J640 trace only at the level actually supported by accepted evidence.

## Pre-registered spatial labels

Use these labels only when supported by available coordinates:

- `LIQUID_LOWER_BOUNDARY_CONCENTRATED`
- `LIQUID_UPPER_BOUNDARY_CONCENTRATED`
- `ILLIQUID_LOWER_BOUNDARY_CONCENTRATED`
- `ILLIQUID_UPPER_BOUNDARY_CONCENTRATED`
- `MULTI_BOUNDARY_CONCENTRATED`
- `INTERIOR_CONCENTRATED`
- `MIXED_SPATIAL_FOOTPRINT`
- `SPATIAL_LOCALIZATION_UNRESOLVED`

For each province assign exactly one final spatial label, but use `SPATIAL_LOCALIZATION_UNRESOLVED` whenever sealed evidence lacks enough coordinate-level information.

## Panel decision labels

Exactly one:

- `COMMON_BOUNDARY_LOCALIZATION_ACROSS_FAILURES`
- `COMMON_INTERIOR_LOCALIZATION_ACROSS_FAILURES`
- `HETEROGENEOUS_SPATIAL_LOCALIZATION_ACROSS_FAILURES`
- `SPATIAL_LOCALIZATION_EVIDENCE_INSUFFICIENT`

Do not infer a common numerical repair from a common location.

## Required report/evidence

Create:

`docs/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_REPORT.md`

Evidence directory:

`docs/evidence/ch5_mp4c_k1_j160_six_failure_trace_spatial_localization_audit/`

At minimum:

- `source_trace_authority.json`
- `province_spatial_summary.json`
- `cross_province_spatial_comparison.json`
- `panel_spatial_decision.json`
- `runtime_ledger.json`
- `sealed_manifest_sha256.json`

Task-owned validator/tests are allowed, but they must operate only on already accepted evidence and must not invoke scientific/model runtime.

## Forbidden

No maxit/tolerance/Delta/floor/selector/FOC/boundary/solver/grid/domain/input changes. No damping, relaxation, line search, policy freezing, warm start, clipping, recalibration, or new `(ra,w)` experiments.

## Git workflow

Fresh isolated worktree and fresh branch. No reset/clean/stash/force push. Explicit staging only; no `git add .` or `git add -A`. One coherent Builder commit, non-force push, exactly one remote readback. Do not merge main and do not publish a successor task.

## Final response

Report actual baseline, branch/worktree/candidate SHA, changed paths, evidence identity gate, zero-runtime ledger, six province spatial labels, common-vs-heterogeneous comparison, any unavailable coordinate evidence, panel decision, Results eligibility=`FALSE`, and exactly one next gate:

`REVIEWER_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_ROUTE_DECISION`

STOP for Reviewer acceptance.
