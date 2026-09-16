# CH5 MP4C 2018 KFE D1-D3 corrected KFE validation design/binding — zero science

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder design/provenance task; zero scientific execution

## Objective

Design and bind the smallest corrected-target source-free KFE validation experiment after the accepted complete Option-A policy map, D2 generator and one direct HJB step. Do not execute any KFE solve, selector map, root, HJB solve, MATLAB call or downstream model block.

The task must determine which already-produced operator/value object is scientifically authorized for the next KFE diagnostic and freeze a pin-free conservation/stationarity/rank/nonnegativity/normalization/uniqueness evidence contract before runtime.

## Required startup authority

Fresh-fetch `origin/main`; record the actual baseline. Read in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_OPTION_A_COMPLETE_POLICY_MAP_D2_DIRECT_STEP_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_Z_SWITCHING_REPAIR_AND_OPTION_A_REEXECUTION_REPORT.md`
7. accepted D1/D2/D3 adoption/static-implementation authority
8. the earlier KFE leakage/pinning forensic authority
9. exact D2/direct-step receipts and artifacts from the accepted candidate.

## Required design questions

Resolve from repository authority, not chat memory:

1. **Operator object.** Decide whether the accepted pre-step `Q0` from the complete Option-A policy map is sufficient for an operator-level KFE diagnostic, or whether a fresh policy map on `V1` is scientifically required before any KFE claim. Distinguish operator validation from HJB fixed-point/steady-state claims.
2. **Orientation and mapping.** Freeze whether stationarity is `Q.T @ g = 0`, exact F-order state mapping, productivity coupling, and density/mass weighting convention.
3. **No implicit source/pin.** The next corrected KFE diagnostic must not reproduce the historical row-replacement/pinning mechanism as a hidden source. Specify a pin-free homogeneous nullspace or equivalent constrained normalization method and how redundancy of any removed/replaced equation would be proven if a numerical constraint is used.
4. **Conservation.** Specify exact prospective arithmetic checks for row sums / `Q@1`, column/source-free residuals after transpose, and any boundary-flux accounting.
5. **Stationary density.** Freeze normalization, negative-mass tolerance (prospective arithmetic only), finite status, total mass, and state-volume weighting.
6. **Uniqueness/rank.** Specify how nullity/rank or irreducibility/communicating-class evidence will establish whether the normalized stationary density is unique. Do not infer uniqueness merely from one solver return.
7. **Solver.** Bind a deterministic bounded numerical method and finite call ceiling. No outcome-dependent retries or source terms.
8. **Interpretation.** State exactly what a PASS would and would not mean given that `Q0` is generated from the Option-A `V0` policy map and only one direct HJB step has been performed.

## Required classification

Return exactly one of:

- `READY_FOR_BOUNDED_CORRECTED_Q0_KFE_OPERATOR_VALIDATION`
- `BLOCKED__V1_POLICY_REMAP_REQUIRED_BEFORE_KFE`
- `BLOCKED__OWNER_SCIENTIFIC_DECISION_REQUIRED`
- `BLOCKED__KFE_CONTRACT_OR_AUTHORITY_CONFLICT`

Do not choose a route because it is numerically easier.

## Zero-call ledger

All must remain exactly zero:
- real/synthetic selector evaluations
- scalar roots
- policy maps
- D2 assemblies
- HJB solves/iterations
- KFE solves/nullspace numerical solves that execute the scientific experiment
- MATLAB
- outer/firm/wage-return
- GE/annual/shock/IRF/Results

Static source inspection, artifact metadata/hash reads, matrix-structure metadata already persisted in evidence, algebraic derivation and documentation checks are allowed. Do not numerically solve the stationary system in this design task.

## Required report

Create:
`docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_REPORT.md`

Include verdict, fresh main SHA, exact authority/artifacts read, operator choice analysis, orientation/mapping, pin-free normalization contract, conservation checks, stationary-density checks, uniqueness/rank contract, finite runtime ceiling, fail-closed rules, interpretation boundary and complete zero-call ledger.

## Git

No reset/clean/stash/force-push. Stage only the report. Commit and non-force push the task branch; verify remote readback and clean worktree. Do not merge main and do not publish a successor task.
