# Call-725 policy switching, operator growth and terminal-state replay
Date: 2026-09-07
Task: CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY
Repository: zcx369658780/dissertation-ch5-two-asset-hank
Issuer: Reviewer under Owner standing authorization.
Accepted predecessor: dedd0f8e5fa894b83c8b20e522d66893e7b6b377.
Record fresh main before execution; this task must be active in the rule index.

## Goal
Close one diagnostic question: do later identical states still produce equivalent policies/operators/value updates, and which frozen arithmetic or branch decisions generate the observed operator growth and convergence split?
Use the existing 143-step MATLAB and 500-step Python evidence first. Implement minimal diagnostics, run the four selected common-state comparisons below, analyze and publish in one task. No new full trajectory is needed.

Accepted finding: first generated discrepancy is consumption at step2; same MATLAB pre-step2 state gives 38/38 cross-language PASS. This explains the earliest propagation, not all later divergence. First transfer-label/support split is step24. Both fail to converge by100; MATLAB converges143, Python remains unconverged500. Do not call the full trajectory parity PASS.

## Startup and frozen inputs
Use D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001.
Verify remote, fetch, read AGENTS, current rule index/status, relevant MATLAB/Python and local-file rules, predecessor trajectory report and its state_schema, manifest, stage_overview and result JSON.
Create codex/ch5-call725-policy-operator-stability-20260907 from fresh origin/main in the clean existing worktree. Preserve predecessor branches, original main checkout and its70 untracked files. No reset/clean/stash/force-push. The Zotero starting project is not the scientific repository; keep platform/global restrictions.

Read-only evidence root:
D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001.
Use its artifact_inventory.json bound by predecessor manifest (SHA256 6D77926997A566E94FE3F016E2BD632042D22276D20D07997DCAB287749E46FC).
Validate the inventory identity and only consumed files; no redundant full3715-file audit.
The predecessor manifest binds exact scalar input and protected MATLAB/helper sources. Inherit all source expressions, grids, F-order, l0, rates, calibration, boundaries, direct solvers and numerical constants.
Protected HJB SHA256: 049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE.
Python export Git blob: 9e7dc9556a2b76811e78f89999abecc045886106.
Scalar binding SHA256: A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6.
The only changed scientific input in each replay is V0, replaced by the exact selected persisted tensor; all other inputs are identical. Do not regenerate a state or use rounded report values.

## A. Solve-free examination of existing trajectories
- Locate the exact first transfer-label/support difference at step24. Report both coordinates, derivatives, candidates/consumed decisions, signed margins relative to the source branch thresholds and relevant boundary overrides. Separate different-state decisions from same-state implementation differences.
- Trace the entries driving the largest operator norms, including Python step32 and MATLAB step57, using stored sparse entries and dense policy operands. Trace the causal arithmetic back through transfer, cost, derivative denominators/clamps and branch selection. Where intermediate operands were not saved, explicitly label source-formula reconstruction from persisted inputs; never label it an independent runtime capture.
- Compute generator diagnostics from stored A: row sums, off-diagonal sign extrema and counts, boundary leakage where implied by the source, and diagonal dominance margins for stored M. Report actual values and coordinates; do not invent new PASS thresholds. Small linear backward error does not imply a sound generator or nonlinear convergence. Separate legacy source behavior from a Python-only difference.
- Summarize Python final100 updates (401–500): stop-statistic range/trend, label-change counts, operator-norm/clamp extrema, and evidence for repeated switching or transient excursions. Do not assert a limit cycle from visual similarity or one near recurrence.
- Reuse the complete existing trajectory without replaying it. Deterministic array arithmetic, sparse reductions and explicit reconstruction of individual source expressions are allowed; no hidden full HJB evaluator or solve in postprocessing.

## B. Four fixed common-state replay cases
Use both language evaluators on each exact common state:
| Case | Input V0 | Purpose |
| --- | --- | --- |
| M24 | matlab_trajectory/step_0024.mat initial_value (pre-step24) | MATLAB side of first discrete split |
| P24 | python_trajectory/step_0024.npz old (pre-step24) | Python side of first discrete split |
| P32 | python_trajectory/step_0032.npz old (pre-step32) | extreme operator state |
| M143_FINAL | matlab_trajectory/step_0143.mat updated (post-step143) | local update at MATLAB terminal state |

For every case, create a new MAT with v0 and exact b/ah/z/l0, bind the source file/field/hash and verify exact array readback. Both evaluators load this same MAT. P32 is not the output of step32. M143_FINAL is deliberately the output, not the pre-step143 state.
Each side executes one source-faithful iteration and one direct value-update solve, with optional capture of branch candidates/margins added around existing computations. Never chain these cases into a trajectory. Do not force either side to converge.
For M24/P24/P32, compare the originating-language replay to the saved originating step as a replay-fidelity check, then compare the two fresh outputs. For M143_FINAL report each update distance from the exact input, source stop flag and nonlinear fixed-point defect u(V0)+A(V0)*vec_F(V0)-rho*vec_F(V0), computed from this step's arrays. Do not confuse that defect with the linear update residual M*V1-RHS or with an accepted equilibrium.
If a case cannot be replayed due to corrupt/missing authoritative input, report that case incomplete and continue other independent valid cases. No substitute checkpoints without a new decision.

## C. Comparisons and interpretation
Reuse the frozen first-step stage map and sparse comparator from accepted code. Compare all required fields in causal order: exact common input, equivalent derivatives, consumed labels/branch views, controls/drifts, rates/operators, M/RHS, V1/statistic.
Continuous rule: abs(x-y)<=128*eps64*max(1,abs(x),abs(y)).
Shapes/order/categories exact; sparse mathematical support exact after removing only exact stored zeros. NaN/Inf fails. Preserve raw-vb stage semantics; label-derived masks are not independent captures.
Provide earliest failing stage and relevant operands/source locations for each case. M/RHS agreement followed by V1 disagreement points to a solve/sensitivity question; do not automatically label it a formula defect or prove ill-conditioning without evidence.
Report new per-step residual/backward error from stored operands, without extra solves.
If all selected common-state maps pass, classify SELECTED_COMMON_STATES_PARITY_PASS__TRAJECTORY_STABILITY_UNRESOLVED. This strengthens local equivalence at these states only.
If a genuine same-state stage differs, classify COMMON_STATE_IMPLEMENTATION_OR_NUMERICAL_DIFFERENCE_LOCALIZED and identify which interpretation the evidence supports. Otherwise use EVIDENCE_INCOMPLETE.
In every outcome report separately generator properties, terminal-state test, convergence gap still unresolved/resolved only to the extent actually tested, and the smallest useful follow-up.
No modification of formulas, clipping, damping, Delta, maxit, tolerance, source/helper implementations or solvers. A proposed stabilization experiment may be specified as a follow-up recommendation with changed object and scientific tradeoff; do not run it in this task.

## Budget and repairs
New maximum per language: four primary single-step invocations (one per case), plus ONE additional invocation total only for a diagnosed external instrumentation/launch/IO failure preventing usable output. Thus <=5 invocations/updates/direct solves per language, including retries. Usually four each, eight total solves.
No retry for numerical mismatch, nonconvergence or unfavorable generator diagnostics. Count entered evaluators and solves, including failures. Missing outputs already recoverable from valid durable files do not justify rerunning.
Each invocation <=15 minutes; complete task <=3 hours. Save scientific output before optional diagnostics. Repair ordinary paths/imports/index/capture/serialization/comparator/report issues within allowed files and budget; no separate preflight task.
Full trajectories, native initialization, diagnostic condition solves, KFE, distribution/aggregation, GE/annual, R/PLM, shocks/IRF and Results calls: zero. Prior budgets remain consumed; this is a new explicit bounded budget.

## Deliverables and publication
Allowed repository paths:
- validators/multi_province/call725_policy_operator_stability/
- tests/test_call725_policy_operator_stability.py
- docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_REPORT.md
- reports/call725_policy_operator_stability_20260907/ (small summaries only).
Reuse predecessor wrappers/comparator read-only; adapt into new allowed directory as needed. Do not invoke the old launcher's task-bound paths/budget directly or change historical evidence.
New evidence root: D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001; choose fresh suffix if occupied.
Deliver source-expression attribution, branch/generator/operator-growth summary, four-case comparison table, terminal-state diagnostic, finite source/input/output manifest, actual ledger, relevant checks and clear repair/experiment recommendation.
Derive machine-readable verdicts/iteration numbers from comparisons; do not carry forward predecessor hardcoded step2/519 results as generic logic.
Focused tests for changed diagnostics suffice. Preserve exact runtime snapshots and failures. Commit explicit paths and non-force push the dedicated branch; verify remote SHA once. Builder stops without merging main or starting a successor. Reviewer is authorized to accept and issue the next bounded task without routine reconfirmation.
