# MP4C call-725 same-input multi-iteration trajectory diagnosis
Date: 2026-09-07
Task: CH5_MP4C_CALL725_MULTI_ITERATION_TRAJECTORY
Repository: zcx369658780/dissertation-ch5-two-asset-hank
Issuer: Reviewer, under Owner standing authorization.
Accepted predecessor: 25e5db97a0239d956d572359db5835cec945962f.
Record fresh origin/main at start; this task must still be active in the current index.

## Goal and complete work unit
Determine whether the accepted common first iteration remains comparable over independent MATLAB/Python HJB trajectories, where the first material difference arises, and whether it persists under a common-state single-step replay. Implement diagnostic capture, run relevant checks, execute the bounded experiment, compare and publish one report. Routine instrumentation repairs do not require another task.

FIRST_ITERATION_PARITY_PASS is accepted for the predecessor's 53 required checks. It does not establish multi-iteration convergence or 2018 stationary validity. Do not repeat the completed closure experiment merely to recertify it.

## Workspace and reading
Use D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001, verify remote and fetch; branch from fresh main:
codex/ch5-call725-multi-iteration-trajectory-20260907.
Preserve the first-iteration and docs-sync branches. Preserve the original D:\ResearchCode\dissertation-ch5-two-asset-hank checkout and its 70 untracked files. No reset/clean/stash/force-push. Existing Codex conversation may continue with explicit cwd; Zotero is not this repository. Platform/global restrictions still apply.

Read AGENTS, rule index, current status, relevant local-file and MATLAB/Python rules; then:
- docs/CH5_MP4C_CALL725_FIRST_ITERATION_CLOSURE_REPORT.md
- reports/call725_first_iteration_closure_20260907/{stage_map,input_source_identity,comparison_summary}.json
- tasks/CH5_MP4C_CALL725_FIRST_ITERATION_CLOSURE.md for exact frozen input/evaluator identities, not its expired budget.
- the prior post-call stagewise report and HJB100/HJB500 termination report linked in current status, only where needed for source loop/stop semantics.

## Frozen scientific contract
Inherit the predecessor's exact authoritative initialization MAT, scalar binding, grids, parameters, source expressions, branch/boundary rules, sparse operators, direct solver and F-order mapping. Direct-load the actual MAT V0 and l0; never regenerate native initialization or substitute rounded values.
Initialization MAT SHA256: 1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81.
Scalar binding SHA256: A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6.
Protected MATLAB HJB SHA256: 049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE.
Python export Git blob: 9e7dc9556a2b76811e78f89999abecc045886106.
Use accepted identity JSON to locate inputs and wrappers; hash consumed identities once and reuse valid unchanged mappings. Do not re-audit the whole historical chain.

Only external diagnostic wrappers are changed. Derive each iteration from the corresponding accepted source; preserve all loop-carried state and source update/stop order, not just V if other state is carried. Persist the state schema and source attribution. Source expressions must not be silently rewritten to match the other language.
The production maxit=100 remains unchanged. This task explicitly authorizes an external diagnostic continuation of each same trajectory up to 500 updates if still unconverged at 100; mark the 100-step production ceiling and later diagnostic continuation separately. Stop each side at its original source convergence condition, nonfinite/fatal solver failure, or 500 updates. No forced convergence and no new stopping tolerance.

## Execution and comparison
1. Implement source-faithful loop capture using the accepted one-step evaluators as the starting point. Check the small wrapper diff and relevant serialization/index/state-carry behavior before the scientific run. Synthetic tests need not call models.
2. Run each language independently from identical frozen initial state. Save durable per-iteration trace: iteration, stop statistic/flag, finite checks, stage extrema, and sufficient compressed dense/sparse stage operands to locate the first difference without rerunning a trajectory. Persist each completed step before optional diagnostics. Keep full loop-state checkpoints needed for common-state replay. Use sparse storage, not dense expansion.
3. Fresh first steps must satisfy the predecessor contract and match the accepted persisted first-step evidence within the same frozen bounds. A valid scientific discrepancy must be reported; do not spend an external-failure retry to search for PASS.
4. Compare iterations present in both trajectories, in the predecessor's stage order: input state, equivalent derivatives, consumed policy labels/branch views, controls/drifts/utility, coefficients/operators, M/RHS, updated V and statistic. Distinguish first incoming-state discrepancy from first newly generated stage discrepancy. Label-derived Python branch views are not independently captured masks. Preserve raw-vb stage distinction.
5. At the earliest material trajectory discrepancy, conditionally perform ONE matched common-state replay pair: load the exact MATLAB pre-step checkpoint for that iteration into both evaluators, including all equivalent carried state. Both take one step with frozen remaining inputs. This replay does not overwrite or reset either original trajectory. If the state schema cannot be mapped without a scientific assumption, report the missing mapping instead of inventing one.
6. If common-state replay passes, this supports propagation/state-history sensitivity rather than a local one-step formula difference; do not claim it proves all later states equivalent. If it fails, report the earliest stage, operand coordinates and source lines; when M/RHS pass but V differs, distinguish solve sensitivity from formula mismatch. Preserve downstream comparisons when finite.
7. Report 100-step state, first convergence iteration (if any), final statistics and where trajectory comparisons stop because one side already converged. Do not force extra updates on a converged side. A 500-step failure is a legitimate result.

Comparison: continuous abs(x-y) <= 128*eps64*max(1,abs(x),abs(y)); exact shapes/order/categorical labels and mathematical sparse support after dropping only exact stored zeros. No NaN/Inf PASS. Record absolute/scaled errors, mismatch counts and representative coordinates. Calculate residual/backward error from stored M/RHS/V without diagnostic re-solves. No post-hoc tolerance changes, condition-estimation solves, regularization or solver substitution.
Long-trajectory failure of this strict bound is a diagnostic finding, not by itself proof of a formula defect.

## New budget (not inherited)
Per language:
- One independent trajectory invocation, at most 500 value updates/direct solves, stopping earlier as above.
- One conditional common-state replay invocation, exactly one value update/direct solve, only when a valid trajectory discrepancy warrants it.
- At most ONE additional invocation total per language, only after a diagnosed external launch/IO/instrumentation/process failure prevents usable required evidence. It may replace the failed trajectory (<=500 updates) OR replay (one update), not both.
Thus maximum 3 invocations and 1001 direct value-update solves per language including failures/retries; usual case is one trajectory plus, if needed, one replay. Count actual entered iterations/solves and failed invocations, not only successful outputs. Retry is never authorized for numerical mismatch/nonconvergence alone. Do not duplicate already durable usable evidence.
Timeout <=45 minutes per trajectory, <=15 minutes per single-step replay; total task execution <=4 hours. Preserve partial results at budget exhaustion. Ordinary static checks and stored-array comparisons can repeat within this time budget.
New native-init, KFE, post-loop distribution/aggregation, GE, annual, R/PLM, shock, IRF and Results calls: zero. No extra post-loop policy evaluation or solve is implied by this task. Stop wrappers before downstream full-household routines.

## Allowed changes and evidence
- validators/multi_province/call725_multi_iteration_trajectory/
- tests/test_call725_multi_iteration_trajectory.py
- docs/CH5_MP4C_CALL725_MULTI_ITERATION_TRAJECTORY_REPORT.md
- reports/call725_multi_iteration_trajectory_20260907/ (small JSON/CSV/Markdown summaries)
Reuse predecessor comparator helpers by read-only import if useful. Production export/source, protected MATLAB, accepted artifacts, scientific inputs and tolerances remain unchanged.
New external evidence root: D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001 (choose new suffix if occupied). Preserve exact wrapper versions used in each invocation, failures and final evidence. Keep large MAT/NPZ locally; Git receives small summaries and a finite identity manifest.
Allowed repairs include paths/imports, capture timing/fields, equivalent index/serialization handling, state plumbing to the frozen source contract, comparator/report omissions. A genuine policy/operator/solver discrepancy requires a bounded repair recommendation, not a production change in this task.

## Completion and publication
Report diagnostic completion separately from scientific verdict:
- MULTI_ITERATION_PARITY_PASS: all required comparable stages pass and both converge compatibly under the unchanged rule; state whether this occurred by 100 or only in diagnostic continuation.
- TRAJECTORY_DIVERGENCE_WITH_COMMON_STATE_PARITY_PASS.
- COMMON_STATE_STAGE_MISMATCH.
- EVIDENCE_INCOMPLETE when the required experiment cannot be completed.
Also record convergence independently (both/one/neither); nonconvergence cannot be hidden by stage equality. Include earliest divergence, conditional replay result, source-layer diagnosis and concrete next action.
Deliver trace summary, stage comparison, input/source manifest, call ledger, executable wrappers/comparator, focused test result and report. Do not claim annual/Results acceptance.
Stage explicit paths, commit and non-force push the dedicated branch; verify remote SHA once. Builder does not merge main or declare reviewer acceptance. Return outcome, paths, key findings, budget use and branch/commit. Reviewer will accept and issue the next bounded task under standing authorization.
