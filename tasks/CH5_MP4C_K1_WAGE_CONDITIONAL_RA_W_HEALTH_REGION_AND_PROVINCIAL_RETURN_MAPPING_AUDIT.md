# CH5 MP4C K1 — wage-conditional `(ra,w)` health-region and provincial return-mapping audit

Date: 2026-09-13
Task ID: `CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT`
Type: docs/evidence integration + source-trace audit; no new scientific runtime.

## Goal

Use the accepted standalone MATLAB-faithful household scans to build a provisional two-dimensional `(ra,w)` health map, prove the wage-variable semantics/scaling, and, only if the wage gate passes, project accepted provincial household-HJB input states onto that map.

Do not modify or rerun HJB/KFE. Do not run the global model.

## Mandatory authority

Read live:

1. `AGENTS.md`;
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`;
5. `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_ACCEPTANCE.md`;
6. `docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_FREEZE_CURRENT.md`;
7. accepted coarse/refinement/narrow standalone scan reports and compact evidence;
8. accepted multi-province HJB mechanism / price-guard / return-interface evidence containing exact provincial HJB inputs;
9. designated MATLAB wage construction source/provenance and accepted Python household input construction.

GitHub live main is repository authority.

## Phase 0 — provenance and evidence inventory

Fresh-fetch live main and record actual baseline.

Identify the exact accepted artifacts used for:

- standalone `(ra,w)` observed labels;
- original MATLAB wage construction (`wjt`, `results.w`, `wage_caculate` or equivalent);
- Python multi-province household wage construction;
- turn-1/turn-2 provincial household HJB entering `ra/rah` and wage values;
- return/wage guard raw and consumed values.

Do not substitute unaccepted traces if an accepted source exists. If multiple accepted sources differ, report the conflict and stop before projection.

## Phase 1 — construct observed 2D household-health map

Build a compact table containing every accepted standalone observed `(ra,w)` point available from the accepted scans.

For each point record:

- `rb`;
- `ra`;
- household wage value used by the standalone oracle;
- HJB legal/converged status;
- distribution label;
- `Ct,Lt,At,Bt` where valid;
- `amin/amax/interior-a` mass;
- modal `a`;
- KFE signed pathology flag;
- source report/evidence identity.

Canonical labels:

- `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`;
- `LOWER_A_BOUNDARY_DOMINATED`;
- `UPPER_A_BOUNDARY_PILEUP`;
- `KFE_NUMERICALLY_PATHOLOGICAL`.

For `(ra,w)=(.06,.8)`, preserve the accepted severe signed KFE pathology explicitly. Do not call it healthy.

No interpolation may create a new health label. Unobserved coordinates remain `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED`.

## Phase 2 — wage semantic/scaling gate

Trace, from source and accepted evidence, the wage chain end-to-end:

`wjt` → any migration/aggregation/weighting transformation → exact wage object passed into household HJB.

For both MATLAB and Python record:

- source variable names;
- dimensions;
- equations/code locations;
- units/normalization if explicit;
- raw versus guarded values;
- whether the current Python HJB consumes `wjt`, a transformed household composite wage, or another object.

Compare that exact consumed object with the standalone scan's `w`.

Return exactly one gate result:

- `WAGE_VARIABLE_IDENTITY_PROVEN_DIRECTLY_COMPARABLE`;
- `WAGE_VARIABLE_MAPPING_PROVEN_REQUIRES_TRANSFORMATION`;
- `WAGE_VARIABLE_NOT_COMPARABLE_OR_SCALING_BLOCKER`.

If transformation is required, it must be source-defined and deterministic. Persist an exact mapping receipt. Never infer/fudge a mapping from the numerical scan outcomes.

### Hard stop at wage gate

If comparability cannot be proven, do **not** project provinces onto the health map. Instead produce the audit report, identify the exact missing mapping evidence, recommend the smallest next task, and stop.

## Phase 3 — provincial projection, only if wage gate passes

Use accepted existing provincial input evidence only. No fresh household/global runtime.

Prioritize exact turn-1 and turn-2 per-province states because accepted mechanism evidence already distinguishes their HJB outcomes.

For each province/turn persist:

- province index/name;
- turn;
- raw entering `ra/rah`;
- consumed `ra/rah`;
- return guard state;
- raw/source wage quantity;
- consumed household-HJB wage quantity;
- wage guard state;
- exact mapping receipt from raw wage object to comparable standalone `w` if transformation is needed;
- accepted HJB converged/failed result for that same input state where available.

Then classify relation to the observed standalone map conservatively:

1. `EXACT_OBSERVED_INTERIOR_MATCH` — only exact accepted observed coordinate with interior label;
2. `EXACT_OBSERVED_UNHEALTHY_MATCH` — only exact accepted observed coordinate with boundary/pathological label;
3. `EXACT_OBSERVED_AMBIGUOUS_MATCH`;
4. `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED` — default for non-exact coordinates.

For unobserved points, compute only descriptive distances to nearby observed points and report nearest wage slice / return frontier ordering. Do not assign interior/boundary status by interpolation.

## Phase 4 — association summary

Without causal overclaim, compare accepted turn-1 versus turn-2 HJB outcomes to the observed map/proximity data.

Report at least:

- counts by turn of converged/failed HJB;
- counts by exact observed-map class;
- counts of unobserved points;
- raw/consumed return guard states;
- raw/consumed wage guard states;
- nearest observed frontier side where definable;
- whether turn-2 failures are descriptively concentrated at higher `ra` or at low/high comparable wage relative to turn-1 states;
- whether any conclusion is blocked because provincial HJB wages live outside the standalone wage scale.

This phase is descriptive association only. Do not claim the standalone map proves the causal source of full-model failure.

## Runtime budget

Scientific runtime:

- HJB calls = 0;
- KFE calls = 0;
- outer turns = 0;
- MATLAB runtime = 0;
- firm = 0;
- K1B/K2 = 0;
- GE/downstream/shock/IRF/Results = 0.

Allowed operations are repository/source reads, accepted-evidence parsing, deterministic offline tabulation, tests for parser/mapping logic, and report generation.

## Required outputs

Create:

- `docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_ra_w_health_region_provincial_mapping/`;
- task-owned offline parser/analyzer/tests if needed;
- truthful CURRENT closeout docs.

Compact evidence must include at minimum:

- `standalone_health_map.csv/json`;
- `wage_semantic_trace.json`;
- `wage_mapping_receipt.json` if applicable;
- `provincial_projection.csv/json` if wage gate passes;
- `association_summary.json`;
- provenance/source identity receipt;
- call ledger proving all scientific runtime counts are zero.

## Questions to answer

1. Is standalone `w` the same object and scale as the current multi-province household-HJB wage input?
2. If not, is there a source-proven deterministic mapping?
3. What exact 2D `(ra,w)` health observations are currently supported?
4. Where do accepted provincial turn-1/turn-2 states sit relative to observed points/frontiers?
5. Does current turn-2 failure correlate descriptively with leaving the observed healthy region or with guard saturation?
6. Is the next problem primarily return mapping, wage mapping/scaling, or insufficient observed health-map coverage?
7. Exactly one next Owner gate.

## Next-gate rule

Choose exactly one:

- `OWNER_REVIEW_PROVINCIAL_RETURN_MAPPING_REDESIGN_WITH_WAGE_CONDITIONAL_HEALTH_CONSTRAINT` if wage semantics are aligned and evidence shows provincial return mapping pushes states toward unhealthy frontier;
- `OWNER_REVIEW_WAGE_MAPPING_OR_NORMALIZATION_CORRECTION` if wage semantics/scaling are inconsistent;
- `OWNER_REVIEW_BOUNDED_PROVINCIAL_INPUT_REPLAY` if mapping is aligned but accepted evidence lacks enough exact provincial states;
- `OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED` if evidence is insufficient/mixed.

Recommend only; do not execute successor work.

## Git workflow

Fresh isolated worktree/branch from fresh-fetched live main. No reset/clean/stash/force push. Explicit stage paths only; no `git add .` / `git add -A`.

One coherent Builder commit, non-force push, one remote readback. Do not merge main. Do not publish successor task.

## Final response

Return terminal classification first, then actual baseline/branch/worktree/candidate SHA; changed paths; wage-semantic gate result; observed 2D health map summary; provincial projection summary if allowed; raw-versus-consumed guard findings; association limits; call ledger proving zero scientific runtime; exactly one next Owner gate; KFE caveat; `Results eligibility=FALSE`.

Stop for independent ChatGPT Reviewer acceptance.
