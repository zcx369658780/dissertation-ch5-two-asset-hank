# Call725 rah=0.07 — one-household native-initialization sensitivity

Date: 2026-09-08. Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Issuer: ChatGPT Reviewer. Publication baseline: 062cd3b715e9aed85e7c068063d6a099b2e30186; fresh-fetch at execution.
Owner explicitly approved the immediately preceding proposal: isolate Anhui call725, change only household rah from 0.09 to 0.07, regenerate the original native initialization at that price, keep the original algorithm and production ramax unchanged, and reuse the saved 0.09 failure baseline. This task records that scientific decision; no further approval is needed for its bounded execution.

## 1. One complete work unit

Implement a standalone diagnostic wrapper, perform relevant synthetic checks, execute ONE Python household at rah=0.07, persist all reached stages, compare descriptively with the saved native-init rah=0.09 baseline, check HJB/KFE/operator evidence, and publish one report. Ordinary import/path/serialization/log/manifest repairs are inside scope; do not split them into additional approval tasks.

This is a diagnostic-price intervention, not a calibration adoption, policy shock, general-equilibrium counterfactual, production replacement or a new safe-rate criterion. Its estimand is the response of the original household solution chain INCLUDING the rate-dependent native initializer. It is NOT a fixed-V0/l0 operator experiment. No new 0.09 solve, MATLAB comparison, 0.065 or other rate point, rate search, extended HJB, provincial/annual replay or D1–D3 repair is authorized.

## 2. Required narrow reading and workspace

Read AGENTS, rule index, current status, this task and relevant local-safety/Python workflow rules. Reuse unchanged historical source certification; do not repeat all historical audits.
Read:
- docs/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY_{REPORT,ACCEPTANCE}.md;
- reports/2018_observable_prefix_replay_20260908/{manifest_readback,prefix_comparison,delivery_checks}.json and the relevant capture-index/manifest entries;
- validators/multi_province/mp4b_python_empirical.py, specifically _source_initial_arrays and _source_labor_root;
- validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py;
- the original annual worker's single-household argument mapping, the frozen export, and the prior observer's relevant persistence/delegation code only.

Existing work directory: D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001.
New branch: codex/ch5-call725-rah-0p07-native-init-20260908, from valid live main.
New evidence root: D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-001; choose an unused suffix if occupied.
Preserve the original D:\ResearchCode\dissertation-ch5-two-asset-hank checkout, its reported 70 untracked files, all prior evidence/branches, and the existing LF runtime worktree. No reset/clean/stash/force-push, global configuration or Zotero/deep-learning-hank changes.

## 3. Frozen baseline and exact one-factor binding

Baseline accepted commit: 9d76747f48858a3e9289de8f284fffbc49aaedce.
Read-only baseline root: D:\ProjectTemp\ch5-2018-observable-prefix-replay-20260908-001.
Authoritative manifest_02.json SHA256: 4C18B9AA14C23356594F1A0ECCBA346B3DB2AE668B7204A73D88A226B98B0146. The published reports/.../manifest.json is that manifest's repository copy; confirm its identity and use capture/index.jsonl to resolve the necessary call_0725 entries.

Use capture/call_0725/entry.json and its referenced NPZ for the full state/grid/EconomicParams; hjb_entry for actual HouseholdInputs/numerics; native_initialization_return for the saved 0.09 V0/l0 COMPARATOR ONLY; hjb_return_before_kfe, kfe_entry, kfe_direct_input, kfe_direct_return and terminal for baseline outcome and diagnostics. Hash the consumed baseline objects against their bound manifest/index identities. A scoped verification of the consumed set is sufficient; do not rehash all 13,800 historical references. Missing critical input or corrupted binding blocks the dependent new solve, not a report of the gap. Do not manufacture missing inputs from rounded chat/report numbers or from a different initialization experiment.

Decode the saved observation schema deterministically, preserving field names, types, grid order, sparse format/support and binary64 values. Do not execute serialized code or silently substitute class defaults. Verify context: calendar2018, outer24, province index0=11/index1=12, name 安徽, original call725.
Create a deep independent state copy and set ONLY state['rah']=float('0.07'). Do not compute it by 0.09-0.02 (that has a different binary64 value); record repr and hex. The complete state diff must contain exactly this one field. Keep carried firm ra, wjt, ramax, ramin, Zt/GovInv and all unrelated state unchanged; carried ra is metadata here, not a second field to update.
Build the household argument objects through the original worker's mapping. In HouseholdInputs the corresponding sole changed field is r_a; all other fields and all grids/EconomicParams/numerics must be exactly equal to the captured baseline. Expected invariant checks include wage=16.82014806560587, rb=.02, rb_gap=.07, tau=.05, Tt=.1, rho=.05, gamma=2, phi=5, chi0=.1, chi1=2, a_bar=1e-6, original fixed-cost fields, 20x20x2 grids, Delta1000, crit1e-7, maxit100 and drift tolerance1e-12. These numbers are assertions, NOT a replacement for the saved full inputs.
Preserve the effective-return taper and every occurrence of rah in the native initializer and HJB. Regenerate V0/l0 ONCE using unchanged _source_initial_arrays at .07. Differences in effective-return arrays, V0/l0 and later endogenous quantities are intended downstream effects, not extra independent interventions. Do not load the saved .09 initialization as .07 input, warm-start, use an annual endpoint, or use the later MATLAB common-initialization MAT (1718984...); do not fix any initializer formula or FOC/cost inconsistency in this task.

Source anchors (verify unchanged relevant dependencies through prior receipts):
- exports/matlab_faithful_two_asset_ha.py blob 9e7dc9556a2b76811e78f89999abecc045886106;
- native initializer module validators/multi_province/mp4b_python_empirical.py blob b1710ae3c5d8d7baf96e85c932d777fa5f3b908c;
- post-loop adapter blob 0033baee136c0328e80ffb8b794a88d4405c976c;
- original worker blob 7473e04418744d745000afb21d84588273cc5bca (read its mapping; DO NOT call run_year);
- protected MATLAB HJB SHA256 049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE remains read-only;
- original 2018 annual input SHA256 F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0 is lineage only, not an instruction to rerun annual entry/data estimation.

## 4. Execution path and persistence

Reuse the prior science interpreter/environment (record actual versions and thread settings). Read-only imports may use the already bound baseline source_runtime LF worktree; explicitly resolve imports there and keep it unmodified. Alternatively create a fresh isolated LF worktree with identical scientific blobs under the new evidence root, using command-local Git settings. Bind the actual loaded source bytes BEFORE any scientific entry; do not change bootstrap expected hashes to bypass CRLF identity failures. No package/solver installation or fallback environment switch to chase a favorable outcome.

Invoke the original native initializer once, then the original solve_matlab_source_postloop_household adapter once with the .07 inputs. Do NOT use solve_household_steady_state, which introduces a different nonconverged-HJB gate. Use default original primitives or observational wrappers delegating to those exact functions once. Preserve original positional/keyword argument objects, operation ordering, parameters, solver defaults and exceptions.

If HJB returns normally with converged=False, the original adapter still attempts its one KFE; preserve that path. If initializer/HJB/KFE raises, persist and terminate without fallback or repeat. If KFE returns, allow the original aggregate routine to complete once; diagnostic validity is judged separately and does not rewrite the execution path. No firm/capital/migration/controller feedback after this standalone household.

Before scientific entry save source/environment/approval/input bindings and the exact one-field diff. Persist .07 native initialization before HJB; persist complete HJB return (including iteration and post-loop operators distinctly) BEFORE KFE. Capture the KFE contaminated matrix/RHS and raw direct-solver return before the source finiteness check, preserving NaN/Inf if produced; then save returned KFE/aggregates if available. Save warnings, traceback, stage reached, counters and completion/exception receipt. Raw science outputs are immutable. Add small per-iteration scalars only via nonmutating observation of the existing invocation; no extra policy evaluation or fixed-point pass.

## 5. Hard new-call budget and retries

One Python science process/worker; OMP_NUM_THREADS, MKL_NUM_THREADS, OPENBLAS_NUM_THREADS and NUMEXPR_NUM_THREADS all1. Count before entry, including failed calls.

| Category | New upper bound |
| --- | ---: |
| Native household initialization | 1 |
| Original labor-root entries | 800 |
| Nested brentq entries | 800, not an additional set of initializers |
| Household post-loop adapter / HJB | 1 each |
| HJB value updates / original direct solves | 100 |
| KFE / original KFE direct solve | 1 each |
| Original aggregate invocation | 1, only if naturally reached |
| Baseline .09 scientific calls | 0 |
| Additional policy/evaluator passes, diagnostic/condition/high-precision solves | 0 |
| Firm, one-turn/controller, GE, annual, other provinces/years, R/PLM, dynamics/IRF/Results, MATLAB startup | 0 |

The upper bounds are not targets. Root residual/bracketing evaluations are reported separately with the original source bounds unchanged. New init-dependent arrays are generated only once. Normal completion, original fatal exception, budget exhaustion or scientific timeout terminates this run.
Scientific wall-time <=15 minutes; complete task <=90 minutes. Preserve partial outputs on timeout. No scientific restart/retry after the first native initializer/root/HJB/KFE entry, including instrumentation/storage failure. One external launch retry is allowed only when receipts prove zero scientific entry and identify a repaired launch/import/environment fault. Inspect the known LF bootstrap issue before launch rather than deliberately consuming a retry. No 500-step continuation or additional rates on either success or failure.
Postprocessing and synthetic tests may be repaired/repeated against saved outputs within scope. A scalar comparison failure or numerical nonconvergence is not an engineering retry reason.

## 6. Predefined comparisons, diagnostics and interpretation

Reuse saved .09 HJB100 false/statistic .3038218386543494 and nonfinite KFE baseline, without any .09 recomputation. Read its exact values from captures; missing valid baseline density/aggregates stay MISSING, never zero. Distinguish this native-init baseline from the separate common-MAT MATLAB143/Python500 experiment.

First certify unchanged input/source/environment binding. The complete intervention-state diff is exactly rah and the mapped r_a; all other input scalars/tensors must be exact. Do not require .07 V0/policies/output to match .09 under a parity threshold: they are different inputs. Report initial-value/labor differences and available final controls descriptively (shapes, extrema, finite counts, norms/label changes) using only saved arrays.

Primary outcome: original HJB converged flag, iteration count and statistic under the unchanged strict statistic<1e-7 rule; then KFE reached/returned/exception/nonfinite stage. KFE return alone does not establish HJB convergence. Retain all source warnings.
Numerical diagnostics from saved objects, without new solves/evaluators:
- consumption/labor/transfer/cost/drift and value finiteness/extrema; inward/outward boundary drifts;
- BOTH HJB iteration operator and post-loop KFE operator: exact negative-offdiagonal counts/minima, row-sum residuals, matrix scale and existing boundary-leak diagnostics, with source ordering stated;
- if KFE returned, source normalization factor/cell weight, normalized total mass, minimum density, exact negative count/weighted negative mass, contaminated-system raw residual and the ORIGINAL unmodified-transpose stationary residual. Report absolute residuals and normwise scale denominators separately. Do not treat the contaminated-row residual as the stationary residual;
- if source aggregation returned, C, effective z-weighted L, A, B, A+B and their finite/normalization status, labelled diagnostic, not accepted steady-state/annual results.
For saved algebraic identities use the frozen abs(x-y)<=128*eps64*max(1,abs(x),abs(y)) convention. Report exact sign violations separately from tolerance-qualified near-zero observations; do not clip density/negative rates, repair diagonals or renormalize beyond the original KFE. Any additional descriptive residual must state its formula; it is not a new production acceptance tolerance. Do not claim full nonlinear fixed-point validity without the additional policy evaluation that this task does NOT authorize.

Report independent fields: diagnostic_completion, input_binding, HJB_status, KFE_status, generator_diagnostics, aggregates_available, local_rate_sensitivity_conclusion. Valid outcome labels include HJB_CONVERGED_AND_KFE_RETURNED (numerical validity separate), HJB_CONVERGED_KFE_FAILED, HJB_NONCONVERGED_KFE_RETURNED, FAILURE_PERSISTS, PRELAUNCH_BLOCKED or PARTIAL_EVIDENCE. Do not bundle these into an unsupported MODEL_PASS.
An improvement supports local price/initialization-chain sensitivity of this implementation at this one input; it does not prove rah is the unique cause, that .07 is a universally safe bound, that source formulas are valid, or that production ramax should change. Lack of improvement does not prove rates are irrelevant. Known generator/P32/common-initialization issues, corrected-2018 coverage and Results remain open.

## 7. Allowed changes, checks and delivery

Allowed repository writes only:
- validators/multi_province/call725_rah_0p07_sensitivity/
- tests/test_mp4c_call725_rah_0p07_sensitivity.py
- reports/call725_rah_0p07_sensitivity_20260908/ (small bindings, comparison tables, receipts and test logs)
- docs/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_REPORT.md

No production/export/helper/old-task edit; no raw private workbook, calibration MAT or large arrays in Git. Keep all raw arrays in the new evidence root. Reuse original observer primitives where suitable, but do not invoke its annual run function or retain its 725-call budgets.
Relevant synthetic tests: observation-schema decoding; exact one-field state and mapped-input diff including float('0.07'); baseline immutability; native initializer delegation with the new price exactly once; .09 baseline read-only/no warm start; original false-HJB-to-KFE behavior; save-before-failure; per-household budgets and failed-entry counters; no import-time science; missing/nonfinite/phase-correct diagnostics. Use fake scientific primitives or AST-selected pure definitions; real root/HJB/KFE calls under tests would consume the sole budget and are not authorized as extra probes. Do not run broad regression campaigns.

Deliver one execution report, compact summary JSON, .09(reused)/.07(new) comparison table, exact source/input/intervention bindings, complete invocation ledger and original failure evidence. Preserve actual failed and final test logs and parse pass counts. One finite manifest binds only consumed baseline material plus new relevant source/input/output/logs; exclude itself and final readback. Separate raw Windows bytes from Git LF identities and verify once after publication preparation. A new revision may correct delivery-only details without overwriting scientific outputs.
Stage explicit allowed paths, commit and non-force push the dedicated branch, verify remote SHA. Do not merge main or launch a successor. Return headline HJB/KFE outcomes, input-binding result, unresolved validity issues, real counts/retry status, report/evidence paths and commit. Results eligibility=FALSE.
