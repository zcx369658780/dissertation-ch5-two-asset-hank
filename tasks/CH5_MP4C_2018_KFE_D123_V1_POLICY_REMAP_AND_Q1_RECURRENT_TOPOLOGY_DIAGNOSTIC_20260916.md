# CH5 MP4C 2018 KFE D1-D3 V1 policy remap and Q1 recurrent-topology diagnostic

Date: 2026-09-16

## Objective

Determine whether the two exact-zero-asset-drift recurrent sinks found in accepted Q0 persist after exactly one accepted HJB direct step, by constructing one fresh corrected policy map from accepted V1, assembling one conservative Q1 under the unchanged D1+D2+D3 contract, and auditing only its directed recurrent topology.

This task is a bounded post-step policy/topology diagnostic. It is **not** nonlinear HJB continuation, KFE stationary-mass validation, equilibrium computation, production replacement, or Results work.

## Repository and authority

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.

Fresh-fetch `origin/main` and read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_OPTION_A_COMPLETE_POLICY_MAP_D2_DIRECT_STEP_ACCEPTANCE_20260916.md`
8. exact accepted direct-step V1 artifact/receipt and current corrected selector/generator authority.

## Exact V1 input

Bind the accepted direct-step arrays artifact and V1 field from the accepted Option-A run:

- arrays artifact SHA-256: `28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173`;
- V1 SHA-256: `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2`;
- shape `(20,20,2)`;
- F-order, b fastest;
- same grid/scalars/productivity generator as accepted Option-A/Q0 run.

No other seed or value object is permitted.

## Frozen selector/generator law

Use the already accepted corrected-target law unchanged:

- D1 upper/lower numerical state constraints;
- D2 consumed-total-drift conservative generator;
- D3 regularized-cost-consistent KKT;
- active lower-a zero-kink multiplier interval law;
- Owner-adopted interior zero-liquid Z switching law;
- strict zero-tolerance outward-face rejection.

No averaging, interpolation, derivative floor, transfer cap, clipping, tolerance tuning, grid/calibration change, or new candidate branch is allowed.

## Required execution

After preflight and scientific-code freeze:

1. derive raw directional derivatives from accepted V1 using the same accepted finite-difference/F-order/boundary-adapter contract;
2. execute exactly one fresh 800-cell corrected selector map from V1;
3. persist every cell receipt durably before the next cell/Q1 assembly;
4. fail closed immediately on the first `NO_ADMISSIBLE_POLICY` or budget/receipt violation;
5. only if all 800 cells are `SELECTED_ADMISSIBLE`, assemble Q1 exactly once with accepted D2;
6. require the same D2 invariants as Q0: nonnegative offdiagonals, accepted construction identity, row-sum within prospective bound, exact-zero outward-face drift/rate/flux, coordinate-action checks;
7. build the exact-positive offdiagonal graph of Q1 once;
8. run exactly one SCC decomposition and one condensation/reachability analysis;
9. compare Q1 topology to accepted Q0 topology, especially the four prior recurrent coordinates flats `5,405,6,406` and the basin split around `i_b=5/6`.

## Mandatory topology outputs

Persist and report:

- Q1 closed communicating class count;
- every closed class member flat index and `(i_b,i_a,i_z)` / physical `(b,a,z)` coordinate;
- selected policy details for every Q1 recurrent state;
- exact consumed `g_b,g_a` and outgoing Q1 rates for every recurrent state;
- whether prior Q0 recurrent coordinates remain recurrent, become transient, or change policy branch;
- SCC count/sizes, condensation edge count, transient-state count;
- A/B-style basin partition if exactly two corresponding sinks survive;
- otherwise the full new reachability partition without forcing Q0 labels onto unrelated classes;
- separatrix/category changes in the asset grid;
- exact comparison of Q0 vs Q1 closed-class count and membership.

## Runtime ceilings

Hard ceilings for the scientific run:

- V1 artifact loads: `1`
- corrected policy maps: `1`
- real selector evaluations: `800`
- scalar root invocations total: `3144`
- interior-Z roots: `2880`
- Q1 D2 assemblies: `1`, only after 800/800 selector PASS
- structural graph audits: `1`
- SCC decompositions: `1`
- condensation/reachability analyses: `1`
- retries: `0`

Forbidden / ceiling zero:

- HJB direct solves or nonlinear continuation: `0`
- V2 construction: `0`
- KFE/nullspace/SVD/eigen/stationary-mass solve: `0`
- `Q1.T @ p`: `0`
- row replacement / pin / RHS source: `0`
- MATLAB / outer / firm / wage-return / GE / annual / shock / IRF / Results: `0`

## Fail-closed rules

Stop without retry if:

- V1/artifact/grid/scalar identity mismatches;
- any scientific/test code changes after freeze;
- first inadmissible selector cell occurs;
- root/selector budget is exceeded;
- Q1 D2 invariants fail;
- required durable receipts are missing;
- graph/SCC/topology evidence cannot be completed exactly under the bound task.

Do not repair or rerun after the first scientific failure.

## Allowed terminal classifications

Use one of these or a strictly more specific equivalent:

- `PASS__V1_COMPLETE_POLICY_MAP__Q1_SINGLE_CLOSED_CLASS__Q0_TWO_SINKS_DO_NOT_PERSIST`
- `PASS__V1_COMPLETE_POLICY_MAP__Q1_TWO_RECURRENT_CLASSES_PERSIST`
- `PASS__V1_COMPLETE_POLICY_MAP__Q1_RECURRENT_TOPOLOGY_CHANGED_OTHERWISE`
- `FAIL__V1_POLICY_MAP_FIRST_CELL_NOT_ADMISSIBLE__STOPPED_WITHOUT_RETRY`
- `FAIL__Q1_D2_INVARIANT__STOPPED_BEFORE_TOPOLOGY`
- `FAIL__Q1_TOPOLOGY_AUDIT__STOPPED_WITHOUT_RETRY`
- `BLOCKED__INPUT_OR_FREEZE_BINDING_MISMATCH`

A topology PASS does not imply HJB convergence or economic equilibrium.

## Git/output requirements

Work on a fresh task branch. Commit and non-force push. Verify remote readback and clean worktree. Do not merge main and do not publish a successor task. Return the candidate SHA, changed paths, validation evidence, scientific ledger, and full report path.