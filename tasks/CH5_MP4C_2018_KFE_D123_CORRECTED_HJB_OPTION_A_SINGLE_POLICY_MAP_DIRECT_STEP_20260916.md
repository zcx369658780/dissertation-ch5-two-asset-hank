# CH5 MP4C 2018 KFE D1-D3 corrected HJB Option A single policy-map + direct-step

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder implementation + one-shot scientific execution

## Objective

Using the Owner-adopted Option A seed and the already accepted corrected D1+D2+D3 contract, execute exactly one complete corrected-target policy map on the exact call-725 grid and, only if all 800 cells are admissible with durable receipts, assemble D2 once and perform at most one direct linear HJB solve. No nonlinear continuation, second policy map, KFE solve, MATLAB call, production replacement, or Results use is authorized.

## Required startup authority

Fresh-fetch `origin/main`; record the actual baseline. Read in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SEED_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_BLOCKED_ACCEPTANCE_20260916.md`
7. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_REPORT.md`
8. `docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_ACCEPTANCE_20260916.md`
9. the accepted corrected-diagnostic implementation/source and exact seed/scalar/grid provenance.

If live authority materially differs, stop before scientific execution.

## Exact Owner-bound seed

Use only:
- `hjb100_initialization.mat:v0`
- file SHA-256 `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`
- field SHA-256 `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665`
- shape `(20,20,2)`, F-order.

No fallback to post-step143, replay output, trajectory state, or another initialization is allowed after observing any outcome.

## Frozen grid and scalar contract

Use the exact accepted call-725 object:
- state order `(b,a,z)`; shape `(20,20,2)`; 800 cells; F-order;
- `b` 20 nodes from `-2` to `5`;
- `a` 20 nodes from `0` to `10`;
- `z=[0.8,1.3]`;
- frozen productivity generator `[[-1/3,1/3],[1/3,-1/3]]` using accepted binary64 values;
- `r_a=.09`, `r_b=.02`, borrowing gap `.07`, `tau=.05`, `w=16.82014806560587`, `T=.1`, `rho=.05`, `gamma_c=2`, `phi=5`, labor weight `1`, `chi_0=.1`, `chi_1=2`, `a_bar=1e-6`, `Delta=1000`;
- effective `R_a(a)=.09*(1-.1*(a/10)^9)`;
- no outer/firm/wage-return recalculation.

Do not remap to the later practical `I=20,J=160` grid.

## Derivative adapter

Construct raw forward/backward finite differences from Option A `V0` exactly as frozen in the design report.

At each lower asset face only the forward one-sided derivative is scientifically valid; at each upper face only the backward one-sided derivative is scientifically valid. If the finite `CellDerivatives` carrier requires both fields, duplicate the valid inward raw derivative into the unused outward slot and persist marker `UNUSED_BOUNDARY_SLOT_DUPLICATES_INWARD_RAW_DERIVATIVE`. This duplicate is representation-only and must never become an additional derivative candidate.

Before any real selector call, add/verify focused static tests proving the selector consumes only the legal inward slot on boundary axes. Do not insert historical post-boundary resource derivatives, derivative floors, state-constraint shadow values, or historical derivative arrays.

## Corrected policy map

Traverse exactly once in F-order, `b` fastest, then `a`, then `z`.

For each of the 800 cells:
- construct one corrected selector cell from the frozen grid/scalars and raw derivatives;
- invoke the accepted corrected selector exactly once;
- persist a durable receipt before continuing, containing cell identity, derivative/adaptor marker, comparison set, root count, selected controls, utility/Hamiltonian, `g_b/g_a`, slacks, multipliers, complementarity, transfer KKT, active-equality receipts, and cumulative budget state;
- require outcome `SELECTED_ADMISSIBLE` and exactly one selected policy after accepted deduplication/comparison.

Any `NO_ADMISSIBLE_POLICY`, `NO_UNIQUE_ADMISSIBLE_POLICY`, invalid domain, exception, budget breach, nonfinite value, receipt failure, or scientific-code mutation is terminal. Stop immediately with no retry. Do not skip the cell and do not continue to D2.

## Code freeze

Implementation, adapter, tests, evidence schema, and all scientific code must be complete before the first real selector call. Persist pre-execution scientific-code hashes. After selector call 1, no scientific-code edit is allowed under this task. If a defect is discovered post-freeze, stop and preserve evidence; do not patch and rerun.

## D2 assembly gate

Only after all 800 durable policy receipts are present and all cells are `SELECTED_ADMISSIBLE`, assemble D2 exactly once using selected total drifts `mu_b=g_b`, `mu_a=g_a`, exact grid, and frozen productivity generator.

Require:
- strict zero-tolerance closed-face feasibility;
- nonnegative offdiagonals;
- diagonal construction error exactly `0`;
- `max(abs(Q @ 1))` <= prospective generator arithmetic bound;
- coordinate-action errors within prospectively derived operation-count + spacing representation bounds fixed before outcomes are inspected.

Any D2 rejection/invariant failure stops before the direct solve. No clipping, projection, diagonal patch, tolerance change, or reassembly is authorized.

## One direct HJB step

If and only if the full map and D2 pass, form exactly:

`M = (rho + 1/Delta) * I_800 - Q0`

`rhs = vec_F(u0) + vec_F(V0)/Delta`

and perform at most one sparse direct solve:

`vec_F(V1) = solve(M, rhs)`.

Persist solver identity, `M/rhs/V1` identities, finite status, `||M*V1-rhs||_inf`, and normwise backward error. No solver substitution after failure, no retry, no damping, no line search, no second solve.

From `V1`, compute and persist raw one-sided derivative diagnostics only; do not call the selector again. Record `V0`, `V1`, raw derivatives/signs and `V1-V0` at exact coordinates `(19,19,0)`, `(19,19,1)`, `(19,18,0)` corresponding to historical Cells 4/8/10. These are diagnostics only.

## Exact scientific-call budget

- corrected policy maps: <=1
- real selector evaluations: <=800, exactly one per visited cell
- scalar root invocations: <=264 total
- D2 generator assemblies: <=1
- sparse direct HJB solves: <=1
- selector evaluations on `V1`: 0
- nonlinear HJB continuation/iterations after the direct step: 0
- adverse-outcome/adverse-numerics retries: 0
- KFE: 0
- MATLAB: 0
- outer loop: 0
- firm block: 0
- wage/return recalculation: 0
- GE/annual/downstream production: 0
- shock/IRF/Results: 0

All failed invocations count. A process interruption or hardware failure does not enlarge the budget.

## Allowed writes

Only:
- isolated corrected-diagnostic adapter/one-step driver changes under `src/ch5_two_asset_hank/corrected_diagnostic/`;
- focused tests under `tests/`;
- bounded evidence under `reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/`;
- one report: `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SINGLE_POLICY_MAP_DIRECT_STEP_REPORT.md`.

Do not edit frozen MATLAB/source-faithful paths, accepted historical evidence, production integration, calibration/grid constants outside the isolated corrected diagnostic, or Results material.

## Required report

Report:
- verdict;
- fresh-start main SHA, branch, frozen implementation SHA if separate, candidate SHA;
- exact changed paths;
- exact seed/file/field/hash readback;
- preflight and boundary-adapter proof;
- policy-map progress and, if terminal early, exact first failing cell and durable comparison receipt;
- total selector/root counts;
- D2 evidence if reached;
- direct-solve evidence if reached;
- Cells 4/8/10 `V0/V1` derivative diagnostics if solve reached;
- pre/post scientific-code hash freeze proof;
- complete call ledger;
- limitations, remote readback and worktree status.

## Verdict classes

Use a narrow evidence-backed verdict. A successful terminal may state `PASS__OPTION_A_COMPLETE_800_CELL_CORRECTED_POLICY_MAP__D2_PASS__ONE_DIRECT_HJB_STEP_COMPLETED`, but must not claim nonlinear HJB convergence, corrected fixed point, KFE validity, production readiness or Results eligibility.

Any map/D2/solve failure must preserve the exact fail-closed mechanism and stop. Do not publish a successor task.

## Git

Use an isolated worktree if useful. No reset/clean/stash/force-push. Stage only allowed paths. Commit and non-force push the task branch, verify remote readback and clean worktree. Do not merge main and do not publish a successor task.
