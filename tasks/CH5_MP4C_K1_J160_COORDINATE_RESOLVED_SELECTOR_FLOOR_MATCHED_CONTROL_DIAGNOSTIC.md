# Task — CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC

Status: ACTIVE

## Objective

Obtain coordinate-resolved selector-switch and derivative-floor footprints for a preregistered seven-province matched panel, using observational instrumentation only, to determine whether accepted first-turn HJB failures show spatial patterns that are distinct from nearby accepted successful controls.

## Required authority reads

Before execution read and follow:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_FREEZE_CURRENT.md`
7. accepted first-turn provincial viability evidence
8. accepted six-failure mechanism evidence and spatial-localization evidence
9. accepted MATLAB-faithful HJB authority

## Phase 0 — authority and identity gate

Fresh-fetch `origin/main`; record actual baseline. Use a fresh isolated worktree and fresh branch.

Verify exact authority for the seven province household-call inputs from accepted sealed first-turn evidence. Verify protected HJB/KFE Python identities, Oracle and MATLAB source identities, grid/domain, tolerance, maxit, Delta and A2max gate.

If any exact input or source authority is missing/ambiguous, STOP before science as:

`COORDINATE_RESOLVED_MATCHED_PANEL_AUTHORITY_BLOCKER`

## Phase 1 — instrumentation implementation and invariance

Implement task-owned observation only. At each iteration persist:

- liquid-selector changed-cell coordinates;
- transfer/illiquid-selector changed-cell coordinates;
- derivative-floor-hit coordinates, separated by floor type if applicable;
- counts and hashes;
- value-update argmax coordinates already available under accepted observer semantics.

Every coordinate record must include indices and state values `(b,a,z)`.

Focused tests must prove instrumentation does not alter scientific outputs or control flow. Reuse accepted observer parity methodology where possible. No new scientific HJB call is permitted for parity testing; use deterministic fixtures or already accepted outputs.

If instrumentation invariance cannot be established, STOP before science.

## Exact seven-province replay panel

Run exactly one fresh HJB for each:

Failures:

1. 天津 — exact accepted first-turn input.
2. 江西 — exact accepted first-turn input.
3. 贵州 — exact accepted first-turn input.
4. 甘肃 — exact accepted first-turn input.

Successful controls:

5. 湖南 — exact accepted first-turn input.
6. 上海 — exact accepted first-turn input.
7. 福建 — exact accepted first-turn input.

No other provinces/states.

Common frozen science:

- `I=20,J=160,Nz=2`
- `a=[0,100]`, `b=[-2,20]`
- `h=1`
- tolerance `1e-7`
- maxit `100`
- `Delta=1000`
- A2max gate `0.01`
- fresh source-style initialization
- exact accepted household inputs

KFE=0.

## Reproducibility requirement

The four failure representatives must reproduce their accepted terminal class at the scientific-output level (legal/nonconverged at 100), and the three successful controls must reproduce accepted convergence, subject to ordinary floating-point identity expectations already used in prior diagnostics.

If a panel member fails reproducibility, report it truthfully; do not retry.

## Spatial summaries

For each province, summarize coordinate-resolved activity using the frozen bins in the freeze document:

- exact lower endpoint;
- near-lower one-index band;
- interior;
- near-upper one-index band;
- exact upper endpoint.

Report separately for:

1. liquid-selector changed cells;
2. transfer/illiquid-selector changed cells;
3. derivative-floor hits by type;
4. value-update argmax locations.

Also report joint `(b,a)` categories: liquid-boundary, illiquid-boundary, dual-boundary, double-interior.

Do not invent outcome-dependent thresholds.

## Required matched comparisons

At minimum compare:

- 天津 vs 湖南;
- 江西 vs 上海;
- 贵州 vs 福建;
- 甘肃 vs 福建.

Answer descriptively:

- Are failure selector-switch footprints more upper-b concentrated than controls?
- Are floor hits failure-specific or equally common in controls?
- Does 江西's floor-amplified classification correspond to a coordinate-resolved boundary concentration?
- Can 贵州's period-2 selector recurrence be localized to a stable cell set or spatial region?
- Do value-update argmax locations coincide with selector/floor footprints, or are they spatially distinct?
- Do the four failure representatives share one spatial mechanism after coordinate resolution?

No causal claim is authorized from descriptive contrast alone.

## Pre-registered terminal panel classes

Choose exactly one:

- `FAILURE_SPECIFIC_LIQUID_UPPER_BOUNDARY_SELECTOR_FLOOR_CONCENTRATION`
- `FAILURE_SPECIFIC_OTHER_BOUNDARY_OR_INTERIOR_CONCENTRATION`
- `FAILURE_CONTROL_FOOTPRINTS_OVERLAP_SUBSTANTIALLY`
- `HETEROGENEOUS_COORDINATE_RESOLVED_FAILURE_FOOTPRINTS`
- `COORDINATE_RESOLVED_MECHANISM_UNRESOLVED`
- `MATCHED_PANEL_REPRODUCIBILITY_BLOCKER`

Do not create a new class after seeing results unless the evidence genuinely cannot be represented; if so explain and use unresolved rather than inventing a favorable PASS class.

## Runtime budget

- HJB exactly 7 after clean preflight.
- KFE=0.
- Scientific retries=0.
- Engineering retry <=1, only before first HJB, path/import/serialization/instrumentation plumbing only.
- successful province calls exactly 3; failed province calls exactly 4.
- outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results all 0.

## Hard stops

No tuning or model changes. No maxit extension, no damping/relaxation/line search, no tolerance/Delta/floor/selector/FOC/boundary/solver/grid/domain/input change, no KFE, no outer execution, no recalibration, no new synthetic points.

## Required outputs

Report:

`docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_REPORT.md`

Evidence directory:

`docs/evidence/ch5_mp4c_k1_j160_coordinate_resolved_selector_floor_matched_control/`

At least:

- `source_identity.json`
- `input_authority_receipt.json`
- `instrumentation_invariance_receipt.json`
- `province_outcomes.json`
- `selector_coordinate_footprints.json`
- `floor_coordinate_footprints.json`
- `value_argmax_crosswalk.json`
- `matched_control_comparison.json`
- `panel_decision.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

## Git workflow

Fresh-fetch `origin/main`; record actual baseline. Fresh isolated worktree and branch. No reset/clean/stash/force push. No `git add .` or `git add -A`; explicit staging only. One coherent Builder commit, non-force push, exactly one remote readback. Do not merge main and do not publish a successor task.

## Final response

Start with terminal panel class, then report actual baseline, branch, worktree, candidate SHA, changed paths, authority gate, instrumentation invariance, seven replay outcomes, per-province selector/floor/value-argmax spatial summaries, matched-control comparisons, 贵州 recurrence localization, panel interpretation, call ledger, KFE=0, scientific retries=0, Results eligibility=FALSE, and exactly one next gate:

`REVIEWER_COORDINATE_RESOLVED_SELECTOR_FLOOR_ROUTE_DECISION`

Then STOP for independent ChatGPT Reviewer acceptance.
