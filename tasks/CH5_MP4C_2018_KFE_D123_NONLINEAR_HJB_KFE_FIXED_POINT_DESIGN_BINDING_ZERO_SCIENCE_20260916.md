# Task — CH5 MP4C 2018 KFE D1-D3 nonlinear HJB-KFE fixed-point design/binding (zero science)

Date: 2026-09-16

## Objective

Design and bind the **smallest scientifically valid corrected-target route** from the accepted one-step objects `(V1,Q1,p1)` toward nonlinear HJB convergence and a joint HJB-KFE fixed point.

This is a zero-science design/provenance task. Do not execute another selector map, HJB solve, D2 assembly, KFE/nullspace solve, MATLAB call or downstream model block.

## Required startup authority

Read, in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_V1_POLICY_REMAP_AND_Q1_RECURRENT_TOPOLOGY_DIAGNOSTIC_REPORT.md`
8. accepted Option-A direct-step report/acceptance and the frozen corrected selector/D2 authority.

## Questions that must be answered

1. Define the exact iteration state. Decide whether the nonlinear loop state is only `V_n`, or `(V_n, policy_n, Q_n)`, or additionally includes the invariant mass `p_n`.
2. Freeze the exact update sequence for one nonlinear iteration, including derivative construction, selector map, D2 assembly, HJB linear solve and any KFE validation step.
3. Determine whether KFE must be solved **every iteration**, only after HJB convergence, or at specific diagnostic checkpoints. Justify from model equations and accepted corrected authority; do not choose for convenience.
4. Define a scientifically meaningful HJB convergence metric and threshold. Distinguish value-function change, Bellman residual, policy stability and operator stability. Do not silently inherit the historical MATLAB stopping statistic unless authority supports it.
5. Define what constitutes a joint HJB-KFE fixed point and which objects must be mutually consistent at termination.
6. Determine whether current `Delta=1000` remains the frozen pseudo-time/implicit-step parameter for continuation, and whether any damping, line search, adaptive Delta or relaxation is already authorized. If not authorized, state so explicitly.
7. Freeze maximum iteration count and hard call budgets prospectively. The budget must be finite and justified from one iteration's known ceilings.
8. Freeze fail-closed rules for: first selector failure, D2 failure, linear-solve residual failure, topology nonuniqueness, KFE nonnegativity failure, cycling/oscillation, convergence-threshold ambiguity, NaN/Inf, timeout and memory breach.
9. Define durable evidence per iteration: hashes for V, policy-map receipts, Q, optional p, convergence metrics and topology summary.
10. State whether the accepted V1/Q1/p1 can serve as iteration-1 starting objects without recomputation, and exactly which objects must be freshly recomputed at iteration 2.
11. Separate three claims: nonlinear HJB convergence; operator-level KFE validity; full stationary household fixed point. State what evidence is needed for each.
12. Recommend exactly one smallest successor runtime task if the route is fully determined. Do not publish it.

## Hard zero-call ledger

All of the following must remain exactly zero:

- selector evaluations
- scalar roots
- policy maps
- D2 assemblies
- HJB/direct solves
- KFE/nullspace/SVD/eigen solves
- `Q.T @ p`
- MATLAB
- outer / firm / wage-return / GE
- annual / shock / IRF / Results

Allowed: repository/source inspection, JSON/text parsing, exact arithmetic, symbolic reasoning, hash/provenance checks and budget arithmetic.

## Forbidden design shortcuts

Do not introduce or authorize without existing authority:

- damping or policy/value averaging
- adaptive `Delta`
- continuation in calibration parameters
- derivative flooring/clipping
- artificial diffusion
- row replacement/pins/sources in KFE
- topology repair
- convergence tolerance chosen after looking at future outcomes
- changing seed/grid/calibration/Z/lower-a/D1-D3 laws

If any such device appears necessary, classify as Owner-decision-required rather than silently adopting it.

## Required classification

Return exactly one:

- `READY_FOR_BOUNDED_NONLINEAR_HJB_CONTINUATION`
- `READY_FOR_BOUNDED_JOINT_HJB_KFE_FIXED_POINT_ITERATION`
- `BLOCKED__OWNER_DECISION_REQUIRED_FOR_ITERATION_OR_CONVERGENCE_LAW`
- `BLOCKED__OTHER_AUTHORITY_CONFLICT`

## Deliverable

Create only:

`docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_REPORT.md`

Commit on a task branch and ordinary non-force push. Do not merge main and do not publish a successor task.
