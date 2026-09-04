# CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_EXACT_HJB_REPLAY_AND_BOUNDED_CONTINUATION_DIAGNOSTIC

Date: 2026-09-04

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / isolated household diagnostic executor

Owner: final scientific authority

## 1. Owner decision and authority basis

Immediate predecessor execution:

`5f05c441ca8d313a7af628b0594cdfc3f12968a0`

with accepted finding:

`GAUGE_REDESIGN_CHANGES_ACCEPTED_LEGACY_SUCCESS_DENSITY_MATERIALLY__NOT_A_PURE_GAUGE_REDESIGN__NO_PRODUCTION_REPAIR_AUTHORIZED`

The Owner explicitly approves the next route:

> Run an isolated exact replay of the captured 2018 Anhui call 725 at the source-faithful HJB ceiling `max_iterations=100`; only if that replay reproduces the captured HJB/operator, run one bounded continuation diagnostic with the sole numerical change `max_iterations=500`. If the 500-iteration HJB converges, run exactly one source-faithful legacy KFE on that converged operator. Do not run the 2018 GE outer loop and do not modify production.

This task tests whether the captured 2018 KFE failure is downstream of an HJB iteration-ceiling limitation rather than a KFE-gauge-only problem.

It does **not** assume in advance that more HJB iterations are a production fix.

## 2. Important MATLAB-faithful interpretation boundary

The project authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

However, algorithmic faithfulness does not imply that every state must converge within a finite source ceiling. A faithful reconstruction may faithfully reproduce a source solver reaching `maxit` without meeting `crit`.

Also, do not use the legacy annual MATLAB batch as an exact same-input 2018 oracle without the already accepted calendar-binding review. This task is Python isolated-call evidence only. It does not make a new MATLAB/Python same-input claim.

The report must explicitly preserve this distinction.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `5f05c441ca8d313a7af628b0594cdfc3f12968a0`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read:
   - `AGENTS.md`;
   - all CURRENT project rules;
   - final 2018 production-path-faithful singularity execution report;
   - retrospective evidence-integrity certification report;
   - captured-operator forensic report;
   - nullspace numerical-consistency cross-check report;
   - fresh KFE gauge-redesign comparison report;
   - accepted HJB parity/source-contract reports;
   - `exports/matlab_faithful_two_asset_ha.py`;
   - `validators/multi_province/mp4b_python_empirical.py`;
   - `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py`;
   - the protected MATLAB HJB source/audit report as read-only source evidence if available.

No execution from a dirty tracked worktree.

## 4. Hard boundary

Task type:

`ISOLATED_CALL725_EXACT_HJB_REPLAY_AND_BOUNDED_CONTINUATION__NO_GE__NO_PRODUCTION_CHANGE`

Forbidden:

- 2018 annual steady-state / GE outer-loop execution;
- any province other than the isolated captured Anhui call 725 household state;
- MATLAB execution;
- R/PLM execution;
- shock/IRF/Results work;
- production/model/source/test modification;
- changing HJB equations, grid, parameters, `delta`, convergence tolerance, drift tolerance, prices, tax, transfer, borrowing spread, or initialization formula;
- changing KFE gauge, row, RHS, normalization, solver, or fallback;
- G1/G2 mass-normalization/adaptive-row KFE diagnostics;
- pseudoinverse, regularization, clipping, alternate solver, warm-start substitution, or grid expansion;
- automatic retries.

Only one diagnostic numerical change is Owner-authorized in Phase B:

`HJB max_iterations: 100 -> 500`.

This is a bounded diagnostic ceiling change, not a production calibration or solver-policy change.

## 5. Frozen source and evidence identities

Preserved 2018 execution root:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`

Require retrospective manifest SHA-256:

`D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490`

Require current captured hashes:

- `first_singularity_operator_A.npz`:
  `A17AA9CF512D4D3FDD79235D0D1897CFB20486D2EF5FAA68850910C849AA1B42`;
- `first_singularity_operator_transpose.npz`:
  `7C1ADEDEE5B26BB30B5A8CC1C9D3D0E83DFF18FAE7860C39986E9E6C2D8FDA66`;
- `first_singularity_localization.json`:
  `3628725A54B97344F501C0E44D32338A0B5CF6733D6022B9DD7A4C82C890BD63`;
- `first_singularity_hjb_status.json`:
  `2B2436E575BB057C9C4BD51F1F6CC5979CBBDACB78D9C9A452BFE90B6181CAF5`.

Require captured localization:

- outer iteration `24`;
- global household call `725`;
- province `安徽`;
- province index `11`.

Require captured HJB status:

- `converged=false`;
- `iterations=100`;
- convergence statistic `0.3038218386543494`;
- KFE path `MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE`.

Current repository source identities must be recorded before execution. At minimum require Git blob identities:

- `exports/matlab_faithful_two_asset_ha.py`: `9e7dc9556a2b76811e78f89999abecc045886106`;
- `validators/multi_province/mp4b_python_empirical.py`: `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`;
- `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py`: `0033baee136c0328e80ffb8b794a88d4405c976c`.

Also record the standalone faithful source file SHA-256 already accepted by project authority if available from the current source audit; do not substitute a different implementation.

Permanent evidence caveat remains:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`.

Any identity mismatch: STOP before numerical execution.

## 6. Exact call-725 state reconstruction

Reconstruct the isolated household state only from the cryptographically bound captured localization/HJB evidence plus frozen source constants.

The exact HJB-active state fields are the captured values used by the production path:

- `rah`;
- `rb`;
- `tau`;
- `w`;
- `Tt`;
- `rb_gap`.

The current source `_source_initial_arrays(state, grid, params)` uses these fields to construct the initial value/labor arrays. Do not use a different initialization.

Freeze the exact grid and household parameters used in the captured execution:

- `b = linspace(-2,5,20)`;
- `a = linspace(0,10,20)`;
- `z = [0.8,1.3]`;
- switch matrix `[[-1/3,1/3],[1/3,-1/3]]`;
- `rho=0.05`;
- `gamma_c=2`;
- `phi=5`;
- `chi_0=0.1`;
- `chi_1=2`;
- `a_bar=1e-6`;
- `mu_z=0`;
- `sigma_z=0`.

Freeze source numerics except the Phase-B ceiling:

- `delta=1000`;
- `convergence_tolerance=1e-7`;
- `drift_tolerance=1e-12`.

Set thread environment to one for OMP/MKL/OpenBLAS/NUMEXPR before numerical execution and record versions of Python/NumPy/SciPy.

Persist the reconstructed active state and SHA-256 hashes of generated initial-value and baseline-labor arrays before any HJB call.

No GE state update, migration update, firm block, fiscal block, or controller is allowed.

## 7. Phase A — exact replay at source ceiling 100

Run exactly **one** isolated call to:

`solve_matlab_faithful_hjb(...)`

with:

`MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)`.

No KFE solve is authorized in Phase A.

Required replay checks:

1. `hjb.converged == false`;
2. `hjb.iterations == 100`;
3. convergence statistic equals the captured value `0.3038218386543494` under exact binary64 equality if reproducible; otherwise STOP unless a previously accepted same-Python scalar tolerance explicitly permits the observed difference;
4. canonical CSR of `hjb.post_convergence_operator.full` must equal the captured `first_singularity_operator_A.npz` in:
   - shape;
   - `indptr`;
   - `indices`;
   - binary64 `data` values.

The preferred gate is exact canonical sparse equality because the same Python implementation, same active state, same initialization, and same deterministic single-thread environment are being replayed.

If exact operator equality fails, persist the strongest mismatch evidence and STOP:

`MP4C_2018_CALL725_EXACT_HJB100_REPLAY_MISMATCH__BOUNDED_CONTINUATION_NOT_AUTHORIZED`

Do not proceed to 500 iterations on a non-reproduced baseline.

If Phase A passes, persist marker:

`MP4C_2018_CALL725_EXACT_HJB100_REPLAY_PASS__CAPTURED_POSTLOOP_OPERATOR_REPRODUCED`.

## 8. Phase B — bounded HJB continuation ceiling 500

Only after Phase A PASS, run exactly **one** second isolated HJB call from the **same original initial arrays**, same state, same grid, same parameters and same numerics except:

`max_iterations = 500`.

Do not warm-start from the Phase-A iteration-100 value. Re-run from the same original initialization so iterations 1--100 follow the same deterministic algorithm and only the ceiling differs.

Record:

- converged flag;
- stopping iteration;
- final convergence statistic;
- whether stopping iteration is `>100`;
- final value/policy finiteness;
- post-loop operator shape/nnz/finite status;
- canonical operator hash/in-memory digest;
- max absolute and scale-normalized difference between the 500-run final operator and captured HJB100 operator;
- max absolute differences in value, consumption, labor, transfer, `mu_a`, and `mu_b` between Phase A final arrays and Phase B final arrays.

If the HJB does not converge by 500:

- persist the result;
- do not increase the ceiling again;
- do not run KFE;
- classify:

`CALL725_HJB_REMAINS_NONCONVERGED_AT_500__HJB_CEILING_ONLY_DIAGNOSIS_NOT_CLOSED__NO_PRODUCTION_CHANGE`.

If it converges at an iteration `>100` and `<=500`, proceed to Phase C.

If it reports convergence at or before iteration 100 despite Phase A exact replay failure-to-converge, classify an internal consistency failure and STOP.

## 9. Phase C — exactly one legacy/source-faithful KFE on the converged operator

Only if Phase B HJB converges, run exactly **one** call to:

`solve_matlab_faithful_stationary_kfe(...)`

on:

`hjb500.post_convergence_operator.full`.

Use exact source-faithful KFE semantics:

- shape `(20,20,2)`;
- `db = 7/19`;
- `da = 10/19`;
- legacy contaminated row `floor(0.37*800)-1 = 295`;
- unit-row replacement;
- RHS `0.007` at row 295;
- standard source normalization by `sum(raw)*db*da`;
- no G1/G2;
- no fallback;
- no retry.

Capture any warning. If the solve is nonfinite or throws, persist and STOP without alternative KFE.

For a finite KFE result report:

- raw solve finiteness;
- normalization factor;
- density mass and mass error;
- min/max density;
- negative-entry count;
- most-negative density;
- weighted negative mass;
- raw contaminated-system residual infinity norm;
- accepted backward-error bound using the already frozen project formula:
  `256*eps64*max(1, ||M||_inf*||raw||_inf, ||rhs||_inf)`;
- backward-error PASS/FAIL;
- `||A' g||_inf` and `||A' g||_2` as diagnostics only, not standalone pass gates because the source-faithful operator may have boundary row-sum nonconservation.

For nonnegativity/admissibility, use an already accepted KFE/density tolerance if one exists. If no explicit nonnegativity tolerance exists, compare each negative entry to the already accepted direct density machine rule against zero and report the exact weighted negative mass; do not invent a new looser tolerance.

Then compute isolated household aggregates with the **Phase-B converged policies** and source-faithful aggregation only:

- `C^ss`;
- `L^ss`;
- `A^ss`;
- `B^ss`;
- `A^ss+B^ss`;
- density normalization.

These are isolated household diagnostics only. They are not a 2018 GE steady state or Results evidence.

## 10. Strict numerical budget

Maximum scientific calls in this task:

- HJB100 exact replay: `1`;
- HJB500 bounded continuation: `1` only if Phase A passes;
- legacy KFE on converged HJB500 operator: `1` only if Phase B converges.

Maximum:

- HJB calls = `2`;
- KFE calls = `1`;
- GE/stationary/household batch/MATLAB/R/shock/IRF calls = `0`.

No automatic retry of any consumed call.

## 11. Required interpretation ladder

The report must distinguish:

1. **Replay identity:** did the isolated HJB100 exactly reproduce captured call 725?
2. **HJB ceiling diagnosis:** does the exact same HJB converge when only the ceiling rises from 100 to 500?
3. **Downstream KFE outcome:** if HJB500 converges, does the unchanged legacy/source-faithful KFE produce a finite, normalized, backward-error-certified, economically admissible density?
4. **Production implication:** does the evidence justify only a new Owner review of HJB termination policy, or does the blocker remain deeper?

Allowed strongest classifications include:

- `CALL725_HJB100_REPLAY_CONFIRMED__HJB_CONVERGES_ONLY_AFTER_100__LEGACY_KFE_ON_CONVERGED_OPERATOR_ADMISSIBLE__PRODUCTION_HJB_TERMINATION_POLICY_OWNER_REVIEW_REQUIRED`;
- `CALL725_HJB100_REPLAY_CONFIRMED__HJB_CONVERGES_ONLY_AFTER_100__LEGACY_KFE_STILL_FAILS_OR_IS_NONADMISSIBLE__HJB_CEILING_NOT_SUFFICIENT`;
- `CALL725_HJB100_REPLAY_CONFIRMED__HJB_REMAINS_NONCONVERGED_AT_500__HJB_CEILING_ONLY_DIAGNOSIS_NOT_CLOSED`;
- `CALL725_HJB100_EXACT_REPLAY_MISMATCH__CONTINUATION_BLOCKED`;
- `CALL725_BOUNDED_CONTINUATION_DIAGNOSTIC_INCONCLUSIVE__NO_PRODUCTION_CHANGE`.

Do not classify a successful HJB500/KFE result as production acceptance. A source-semantics or same-input MATLAB review remains a separate Owner/L3 gate before changing production HJB termination behavior.

## 12. Evidence root

Preferred fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-hjb-replay-and-bounded-continuation-20260904-001`

Persist at minimum:

- `authority_and_source_identity.json`;
- `captured_evidence_identity.json`;
- `call725_active_state.json`;
- `initial_array_identity.json`;
- `phase_a_hjb100_result.json`;
- `phase_a_operator_identity_and_exact_comparison.json`;
- `phase_b_hjb500_result.json` if Phase B runs;
- `phase_a_vs_phase_b_policy_operator_comparison.json` if Phase B runs;
- `phase_c_legacy_kfe_result.json` if Phase C runs;
- `phase_c_household_aggregates.json` if finite Phase-C density exists;
- warning/stdout/stderr evidence;
- `scientific_call_budget_ledger.json`;
- `classification.json`;
- `audit_manifest.json`.

No helper source may be committed to GitHub.

## 13. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_EXACT_HJB_REPLAY_AND_BOUNDED_CONTINUATION_DIAGNOSTIC_REPORT.md`

The report must include:

- Owner-authorized scope;
- exact captured/source identities;
- exact active state reconstruction;
- Phase-A replay identity result;
- Phase-B 500-ceiling result if run;
- Phase-C legacy KFE result if run;
- scientific call counts and zero retries;
- explicit statement that no GE/2018 annual/MATLAB/shock/IRF run occurred;
- permanent capture-time hash caveat;
- explicit statement that algorithmic faithfulness does not itself guarantee finite-iteration convergence;
- no production change.

## 14. Publication and terminals

If the bounded diagnostic completes consistently, only a report-only commit + push is authorized.

Suggested commit message:

`Diagnose MP4C 2018 call-725 HJB iteration ceiling`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean.

PASS terminal:

`MP4C_2018_CALL725_EXACT_HJB_REPLAY_AND_BOUNDED_CONTINUATION_COMPLETE__HJB_CEILING_AND_LEGACY_KFE_CLASSIFIED__NO_GE_NO_PRODUCTION_CHANGE`

Blocked terminal:

`MP4C_2018_CALL725_HJB_REPLAY_OR_CONTINUATION_BLOCKED__NO_GE_NO_PRODUCTION_CHANGE`

No automatic production repair, 2018 GE rerun, MATLAB run, or IRF task is authorized inside this task.