# Call-725 P32 frozen linear systems: crossed solvers and representation sensitivity

Date: 2026-09-07.
Task: CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION.
Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Issuer: Reviewer under Owner standing authorization.
Accepted predecessor: b2d7a814039a585b696d8cc5079b8b9865017501.
Acceptance: docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_ACCEPTANCE.md.
This task must be active on live main before scientific execution. Publication is not execution.

## Goal and non-goals
Complete one numerical-attribution work unit: separate same-stored-system solver differences from sensitivity to the two slightly different stored P32 systems; determine whether a fixed, algebraically equivalent row scaling changes linear accuracy. Prepare, test relevant instrumentation, execute the finite matrix below, analyze existing/new arrays and publish in this task.
P32 policies/operators/M/RHS passed the prior tolerance but were not bitwise equal; V1 did not pass. No formula defect or condition-number claim follows from that alone. Do not optimize toward a PASS.
No HJB evaluator, policy update, new trajectory, initial-value search, KFE, distribution/aggregation, GE/annual, dynamic/IRF or Results run. No production/helper/formula/boundary/parameter/Delta/maxit/tolerance/solver replacement. No transfer clamp, damping, iterative refinement, condition-estimator solve, inverse, eigen/SVD or high-precision solution. High-precision residual arithmetic on saved solutions is allowed and is not a solve.
The signed-generator/boundary-leakage blocker remains open even if all linear comparisons pass.

## Startup, workspace and source identities
Use D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001, or an isolated worktree only if needed to preserve unrelated dirty work. Fetch and record live main, repository/remote/HEAD/status; read AGENTS, rule index, current status, this task, predecessor report/acceptance and relevant local-file/Python/MATLAB rules. Do not repeat completed sync, first-iteration, trajectory or policy/operator tasks.
Create branch codex/ch5-call725-frozen-linear-system-20260907 from current main after checking this task remains active and dependencies unchanged. Preserve historical branches and D:\ResearchCode\dissertation-ch5-two-asset-hank with its unrelated files; no reset/clean/stash/force-push. Do not alter Zotero, global configuration or model/provider settings.
New evidence root: D:\ProjectTemp\ch5-call725-frozen-linear-system-20260907-001; choose a fresh suffix if occupied and pass the actual root consistently to all scripts. Never overwrite accepted evidence.
Protected HJB SHA256 remains 049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE. Frozen export Git blob remains 9e7dc9556a2b76811e78f89999abecc045886106. Neither is executed/imported or edited by this task. Git comparison suffices for unchanged repository source; do not repeat unrelated source-directory archaeology.

## A. Bind the two already saved systems, with zero solves
Read-only predecessor root:
D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001.
Use the P32 common-state REPLAYS, not new model evaluation:
- M-origin: matlab_P32/step_0001.mat, fields matrix, rhs, updated; also A and initial_value for stored diagnostic context.
- P-origin: python_P32/step_0001_M.npz and python_P32/step_0001.npz fields rhs, v1, old; stored step_0001_A.npz for context.
The common input P32.mat SHA256 is 094B4B0815335B4C6257E6EE14C9FC75186CD7792BC3CD6BAC6D996486334FA4. It binds pre-step32 V, not updated step32 V.
Scalar binding SHA256 remains A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6; get its exact path from predecessor identities, never reconstruct scalars from rounded report numbers.

Read predecessor manifest.json and manifest_readback.json, verify their digest relationship and only consumed artifact/runtime-source entries. Persist a compact consumed-input receipt, including predecessor manifest/readback hashes and exact source fields, in the new Git summaries. A manifest's old CURRENT-doc hashes refer to the prior commit; do not compare them to intentionally updated live CURRENT files and invent a blocker. Preserve old receipts unchanged. Missing/corrupt required science inputs stop the affected cases; no regeneration/substitute system.

Export each existing M/RHS pair into a fresh common MAT readable by both languages, preserving dimensions (800,800), binary64 values, mathematical sparse support and F-order RHS/value association. Canonicalization may sort indices and remove only exact stored zeros. Detect duplicate entries; do not silently change an ambiguous representation by summing duplicates. Verify elementwise exact numerical values/support and byte/dtype information on readback, not the 128-eps comparison rule. Record signed-zero/storage-order differences separately from mathematical identity.
Both solvers must load each same file; validate their loaded data/RHS against the saved canonical payload before solving. This establishes genuinely identical linear input, rather than merely identical nonlinear state. Keep original and canonical storage formats recorded. Python solver input should use the predecessor's CSR convention; MATLAB remains sparse. Do not change ordering/pivot options or global solver settings. Record actual versions, warnings and backend information available without extra solves; distinguish observed backend facts from assumptions.
Copy the already saved full P32 stage-comparison rows, replay-fidelity summary and predecessor manifest receipt into compact, provenance-labelled Git-readable summaries where practical. Do not recompute them by calling an evaluator. The prior checks.json test count is a Builder summary, not a parsed test log; retain that distinction.

## B. Fixed execution matrix: eight primary direct solves in total
For each of the two origins (M-origin and P-origin), both MATLAB and Python execute exactly one direct solve for each representation below:
1. ORIGINAL: x = M\rhs in MATLAB; x = scipy.sparse.linalg.spsolve(M,rhs) in Python, preserving the predecessor direct-solver entry points and configuration.
2. ROW_POW2: x solves (D*M)x = D*rhs using the same respective direct solver. This is a diagnostic equivalent-system representation, NOT a production algorithm change.
Thus 2 origins x 2 representations x 2 languages = 8 solves, four per language. One invocation contains one direct solve. Do not chain solutions or run a nonlinear update using them.

Freeze ROW_POW2 before observing any new solve: for row i let s_i=max_j abs(M_ij); if s_i=0 set k_i=0, otherwise use the binary frexp exponent e_i of s_i and set k_i=1-e_i, D_ii=2**k_i. Use ldexp/binary scaling, no fitted scaling choices. Prepare each scaled system once from its canonical origin and give the exact same scaled file to both languages. Store k and scaled payload hashes.
Require finite scaling factors/results, unchanged nonzero support, no overflow/underflow and exact reverse-scaling recovery of M and rhs. If that contract fails, mark that scaled case ineligible and preserve the reason; do not tune exponents or switch methods. A zero matrix row is retained and reported, not repaired. ORIGINAL independent valid cases may proceed.
Every completed or failed entered solve counts. A numerical mismatch, singularity warning, nonfinite output or unfavorable residual is an outcome, never a retry reason.

## C. Solve-free analysis and attribution
Preserve core outputs/loaded-input receipts before optional diagnostics. Validate shapes, finite status and column/F-order association. Compare:
- same origin and representation, MATLAB versus Python;
- M-origin versus P-origin within each solver/representation;
- ORIGINAL fresh originating-language solutions versus their already saved predecessor solutions (replay fidelity);
- ROW_POW2 versus ORIGINAL for each solver/origin, without replacing the original result.
Use the existing frozen continuous rule abs(x-y)<=128*eps64*max(1,abs(x),abs(y)); exact shapes/categories and sparse support after removing only exact zeros. Report maxima, scaled maxima, material-coordinate counts and representative coordinates. Do not loosen thresholds. A failed replay-fidelity comparison must remain visible and limits historical attribution; do not retry it.

On ORIGINAL solutions give both vector decompositions of the observed split, using the fresh solves, and compare the reconstructed split to the prior saved split:
Delta = x_M(M_M,b_M)-x_P(M_P,b_P)
      = [x_M(M_M,b_M)-x_P(M_M,b_M)] + [x_P(M_M,b_M)-x_P(M_P,b_P)]
      = [x_M(M_M,b_M)-x_M(M_P,b_P)] + [x_M(M_P,b_P)-x_P(M_P,b_P)].
The brackets distinguish a fixed-input language/solver effect and a within-solver input perturbation effect. Vector identities may cancel; do not add infinity norms or assign causal percentages as though contributions were orthogonal. This does not by itself identify the original full-trajectory cause or mathematically prove ill-conditioning.

For every saved/fresh x compute residuals against BOTH original stored systems and, where applicable, the actually solved scaled system. Include ordinary binary64, compensated row-sum and an independently implemented 80-decimal-digit residual calculation using exact conversion of the stored binary64 operands (for example Decimal.from_float). This is residual evaluation only, not a high-precision solve. Report precision and product/summation conventions; math.fsum of already rounded products is not an exact dot product.
Report residual infinity norm, normwise backward error and componentwise backward error max_i |r_i|/(sum_j |M_ij|*|x_j|+|rhs_i|), using the same high-precision operand interpretation for the latter diagnostic where feasible. Handle 0/0 as 0 and a positive numerator/zero denominator as an explicit nonfinite diagnostic, not a pass. Compare scaled and original residuals in their own equation units; a smaller scaled absolute norm alone is not evidence of greater accuracy.

From the stored A/M and exact scalar binding, examine representation of sigma=rho+1/Delta at the extreme diagonal rows: report compensated/high-precision M_ii+A_ii, sigma, local binary64 spacing, and relevant row sums. This is a diagnostic question, not a preasserted finding. Row scaling cannot restore information already lost before the saved M was formed. Do not regenerate A or its policies.
No new numerical-admissibility threshold is invented for signed rates, leakage, diagonal margins or condition numbers. Separate observed solve differences, input sensitivity, representation effects, legacy operator defects and unanswered nonlinear stability questions. A selected checkpoint pass does not accept all iterations or the model.

## Budget, repairs and stop conditions
Each language: four primary direct-solver invocations, plus at most ONE additional invocation/solve only for a diagnosed external launch/instrumentation/IO failure that prevented usable durable output. Maximum five per language, ten total; normal total eight. Log attempted/entered/completed separately. Existing outputs mean postprocessing repair rather than rerun. No numerical retries or extra validation solves, including hidden condition estimators or unit-test solves on real matrices. Synthetic tests use arithmetic and mocked solver boundaries; any actual scientific direct solve must be one of the enumerated cases.
Each invocation <=5 minutes, whole task <=2 hours. Record actual resource use; timeout counts consumed attempts. Routine imports/serialization/exact sparse binding/JSON/report issues may be fixed and relevant checks repeated inside allowed files. Preserve failures. A new conversation does not reset budget.
HJB/policy/evaluator calls=0; full trajectories=0; KFE/GE/annual/dynamics/IRF/Results=0. Stop affected execution on damaged authoritative input, out-of-scope scientific change or exhausted budget, while completing unaffected evidence/report work.

## Deliverables and publication
Allowed repository paths only:
- validators/multi_province/call725_frozen_linear_system/
- tests/test_call725_frozen_linear_system.py
- docs/CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION_REPORT.md
- reports/call725_frozen_linear_system_20260907/ (small text/JSON/log summaries only).
Reuse predecessor diagnostics read-only; new scripts must not invoke an old launcher or model evaluator. No MAT/NPZ/private input or secrets in Git.
Deliver exact input/representation receipts, eight-case result table, original replay fidelity, vector attribution, residual and diagonal-representation diagnostics, failures/warnings, actual invocation ledger, focused test log with parsed counts, one finite manifest/readback and a report with the smallest justified next experiment/repair recommendation. Publish compact comparison rows and manifest digest/readback counts to allow remote review; keep large arrays external. Exclude manifest itself and terminal receipts from its entries; one completed readback is sufficient.
Completion marker when all eligible prescribed cases and analyses are reported: FROZEN_LINEAR_SYSTEM_ATTRIBUTION_COMPLETE__TRAJECTORY_AND_GENERATOR_BLOCKERS_OPEN. This is diagnostic completion even when comparisons fail. Use EVIDENCE_INCOMPLETE when missing inputs/execution prevent the question from being answered; explain partial results. Never use FULL_PARITY_PASS or model-convergence/Results acceptance.
Stage explicit allowed paths, make a coherent commit, non-force push the dedicated branch, verify remote SHA once, and return outcome first. Do not merge main or start a successor. Reviewer handles acceptance and the next bounded task; production adoption or a change to the FOC/boundary law remains a separate scientific decision.
