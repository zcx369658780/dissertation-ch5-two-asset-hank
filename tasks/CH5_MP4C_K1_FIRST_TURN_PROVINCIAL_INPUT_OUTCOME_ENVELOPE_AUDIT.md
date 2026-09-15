# Task — CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT

Status: ACTIVE

## Objective

Perform the frozen zero-science-runtime offline audit of the exact accepted 31-province first-turn household input/outcome envelope. Determine whether the six legal HJB failures admit a simple descriptive separation in accepted input/guard/mapping space or remain interleaved with successful provinces.

## Required authority reads

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT_FREEZE_CURRENT.md`
7. accepted 31-province first-turn viability evidence
8. accepted six-failure mechanism/spatial/matched-control evidence

## Authority gate

Fresh-fetch `origin/main`, record actual baseline, use fresh isolated worktree/branch. Verify accepted first-turn manifest and all source evidence needed for the 31-province table. If the accepted exact input/outcome vector cannot be reconstructed solely from repository evidence, STOP as `FIRST_TURN_INPUT_OUTCOME_ENVELOPE_AUTHORITY_BLOCKER`.

## Runtime budget

All scientific/model runtime is exactly zero:

- HJB=0
- KFE=0
- firm=0
- wage mapping=0
- return mapping=0
- outer=0
- MATLAB=0
- K1B/K2=0
- GE/downstream/shock/IRF/Results=0
- scientific retries=0

Task-owned offline parsing/tests/finalization only.

## Required 31-province table

For every province, extract from accepted sealed evidence when available:

- index/name
- HJB success/failure class
- iterations/final statistic/max A2max
- consumed `ra/rah`
- household composite `w`
- `rb`, borrowing gap, tax, transfer
- return guard state
- wage guard state
- raw pre-guard return, if sealed
- raw provincial `wjt`, if sealed
- exact provenance pointer/hash

Never substitute raw `wjt` for composite household `w`.

## Frozen descriptive analyses

Implement exactly the freeze-defined analyses: ranges/quantiles/ranks, guard contingency, standardized `(ra,w)` nearest successful neighbors, deterministic bounding-box/convex-hull checks if well-defined, one-dimensional threshold existence checks, fixed `k=3` standardized `(ra,w)` neighbor-graph connectivity, and analogous raw-upstream checks only where sealed values exist.

No ML classifier, no fitted production threshold, no post-result metric invention.

## Required report

`docs/CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT_REPORT.md`

Evidence directory:

`docs/evidence/ch5_mp4c_k1_first_turn_provincial_input_outcome_envelope_audit/`

At least:

- `source_authority.json`
- `province_input_outcome_table.json`
- `range_rank_summary.json`
- `guard_contingency.json`
- `nearest_success_standardized.json`
- `envelope_overlap.json`
- `neighbor_graph_summary.json`
- `upstream_raw_mapping_summary.json`
- `runtime_ledger.json`
- `sealed_manifest_sha256.json`

## Terminal class

Exactly one:

- `SIMPLE_INPUT_ENVELOPE_SEPARATION_SUPPORTED`
- `FAILURE_SUCCESS_INPUT_ENVELOPES_OVERLAP_SUBSTANTIALLY`
- `UPSTREAM_GUARD_OR_MAPPING_STATE_ASSOCIATION_SUPPORTED`
- `INPUT_OUTCOME_ENVELOPE_EVIDENCE_INSUFFICIENT`

## Interpretation boundary

This audit cannot authorize recalibration, mapping changes, guard changes, HJB/KFE changes, grid/domain changes, or Results use. It only informs the next Reviewer route.

## Git workflow

Fresh-fetch main, fresh isolated worktree and branch. No reset/clean/stash/force push. No `git add .`/`git add -A`; explicit staging only. One coherent Builder commit, non-force push, exactly one remote readback. Do not merge main and do not publish successor task.

## Final response

Start with terminal class, then report actual baseline, branch/worktree/candidate SHA, changed paths, authority gate, zero-runtime ledger, 31-province table summary, failure-vs-success input overlap, guard-state evidence, nearest-success analysis, threshold-existence results, k=3 graph result, upstream raw mapping availability/findings, interpretation, Results eligibility=FALSE, and exactly one next gate:

`REVIEWER_FIRST_TURN_INPUT_OUTCOME_ENVELOPE_ROUTE_DECISION`

Then STOP.
