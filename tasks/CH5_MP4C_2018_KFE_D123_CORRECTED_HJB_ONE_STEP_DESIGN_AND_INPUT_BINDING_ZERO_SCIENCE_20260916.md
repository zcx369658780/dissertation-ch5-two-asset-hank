# CH5 MP4C 2018 KFE D1-D3 corrected HJB one-step design and input binding — zero science

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder design/provenance task; zero scientific execution

## Objective

Prepare the exact execution contract for the smallest corrected-target HJB experiment after the accepted failed-cell attribution. Do not run a selector, root, HJB, KFE, MATLAB, or any model block. The task must determine whether repository authority uniquely supports a scientifically defensible corrected-HJB starting value/seed and one-step contract.

The intended successor, only if this design gate passes, is one corrected-target policy map plus at most one direct linear HJB solve, with no nonlinear iteration and no KFE solve.

## Required startup authority

Fresh-fetch `origin/main` and read in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_TEN_CELL_REEXECUTION_FAIL_CLOSED_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_2018_KFE_D123_SELECTOR_ACTIVE_EQUALITY_CANONICALIZATION_AND_TEN_CELL_REEXECUTION_REPORT.md`
9. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`
10. direct current source/provenance needed to bind a corrected-HJB one-step experiment.

## Required scientific design questions

Resolve each item from repository authority, not chat memory:

1. **Starting value/seed object.** Identify the exact candidate value-function object(s), provenance, shape/order, hash/byte identity where available, and whether each is source-faithful, corrected-target, or merely a numerical initialization. Determine whether one seed is uniquely justified for the next corrected-target experiment.
2. **Grid/domain.** Freeze the exact asset/productivity grid for the proposed one-step experiment. Do not silently remap the historical call725 panel to the later practical `I=20,J=160` grid or vice versa. Explain why the chosen grid is the correct object for this gate.
3. **Prices and calibration.** Bind all household price/return/wage/transfer/cost parameters consumed by one corrected policy map. No recalculation is allowed in this task. Missing bindings must be explicit.
4. **Derivative construction.** Specify how backward/forward derivatives are formed from the starting value object at interior and lower/upper faces under the corrected D1-D3 target. Distinguish raw one-sided differences from state-constraint shadow values and from the historical post-boundary derivative arrays.
5. **Policy-map contract.** Specify exactly how the already accepted corrected selector is called across the grid, what constitutes a cell-level failure, and whether every grid cell must produce one admissible policy before a direct HJB solve is allowed.
6. **Generator and HJB equation.** State the corrected D2 generator construction and the exact one-step linear HJB equation to be solved if the policy map is complete. Bind discount/time-step/pseudo-time parameters from authority; do not invent them.
7. **One-step output.** Define what derivative/value objects are produced after the single direct solve and which diagnostics will be compared at the historically failed Cells 4/8/10 or their exact corresponding coordinates if and only if the chosen grid is the same object.
8. **Budget.** Propose exact finite ceilings for corrected real-cell selector evaluations, scalar roots, sparse/direct HJB solves, and all downstream calls. No retries for adverse scientific outcomes.
9. **Stop conditions.** Fail closed before scientific execution if the seed, grid, prices, derivative law, HJB equation, or mapping from historical evidence to the proposed corrected object is not uniquely supported by existing authority or would require a new substantive economic law/calibration choice.

## Required classification

Return exactly one of:

- `READY_FOR_SINGLE_CORRECTED_HJB_POLICY_MAP_AND_DIRECT_STEP`
- `BLOCKED__NO_UNIQUE_AUTHORITY_BACKED_CORRECTED_HJB_SEED_OR_INPUT_CONTRACT`
- `BLOCKED__NEW_OWNER_SCIENTIFIC_DECISION_REQUIRED`
- `BLOCKED__OTHER_AUTHORITY_CONFLICT`

Do not choose a seed merely because it makes the selector pass.

## Zero-call ledger

All must remain exactly zero:
- real selector/evaluator calls
- synthetic selector calls if they execute scientific policy logic
- scalar roots
- HJB policy maps/iterations/direct solves
- KFE solves
- MATLAB
- outer loop / firm / wage-return recalculation
- GE / annual / shock / IRF / Results

Static source inspection, persisted-array metadata/hash reads, algebraic derivation, and documentation checks are allowed.

## Required report

Create:
`docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_REPORT.md`

It must contain:
- verdict/classification;
- fresh-start main SHA, branch, candidate SHA placeholder convention;
- exact files/authority read;
- seed/value-object option table with provenance and classification;
- exact chosen input contract if unique, or exact unresolved Owner decision if blocked;
- grid/domain, prices/calibration, derivative construction, selector map, D2 generator and one-step HJB equation;
- proposed finite call budget and fail-closed rules;
- exact successor experiment definition if `READY...`;
- complete zero-call ledger;
- limitations and interpretation boundary.

## Git

Use an isolated worktree if useful. No reset/clean/stash/force-push. Stage only the report. Commit and non-force push the task branch, verify remote readback and clean worktree. Do not merge main and do not publish a successor task.
