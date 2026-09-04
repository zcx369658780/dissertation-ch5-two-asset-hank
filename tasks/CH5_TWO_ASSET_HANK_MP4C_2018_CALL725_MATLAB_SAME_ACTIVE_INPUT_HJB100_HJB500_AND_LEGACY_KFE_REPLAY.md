# CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_MATLAB_SAME_ACTIVE_INPUT_HJB100_HJB500_AND_LEGACY_KFE_REPLAY

Date: 2026-09-04

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / isolated MATLAB validation executor

Owner: final scientific authority

## 1. Authority basis and purpose

Immediate predecessor execution:

`d6265e8de33d9fe332f5b1b1430a74ad44294463`

with accepted isolated-call classification:

`CALL725_HJB100_REPLAY_CONFIRMED__HJB_CONVERGES_ONLY_AFTER_100__LEGACY_KFE_ON_CONVERGED_OPERATOR_ADMISSIBLE__PRODUCTION_HJB_TERMINATION_POLICY_OWNER_REVIEW_REQUIRED`

The predecessor proved, in Python, that the exact captured 2018 Anhui call 725:

- exactly reproduces the captured HJB100 endpoint and post-loop operator at `max_iterations=100`;
- remains nonconverged at 100 with statistic `0.3038218386543494`;
- converges at iteration 196 when the sole numerical change is `max_iterations=500`;
- then produces a finite, normalized, backward-error-certified and economically admissible density under the unchanged legacy/source-faithful KFE.

The next scientific question is whether the protected MATLAB source exhibits the same termination behavior on the same **HJB-active household input**.

This task therefore performs a bounded MATLAB isolated validation at `maxit=100` and `maxit=500` using the protected source semantics and compares the 500-ceiling output to the already persisted Python isolated result.

This is not production termination-policy authority, not a 2018 annual/GE rerun, and not Results evidence.

## 2. Interpretation boundary

Primary authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Accepted cross-language household authorities remain:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`;
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`;
- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_ACCEPTED`;
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_KFE_DENSITY_PARITY_ACCEPTED`;
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_PARITY_ACCEPTED`;
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HOUSEHOLD_AGGREGATE_PARITY_ACCEPTED`.

Do not use the legacy annual MATLAB batch as a corrected-2018 same-input oracle because the annual calendar-binding defect remains separately accepted.

The present comparison is an **isolated household same-HJB-active-input validation**, not an annual-model comparison.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `d6265e8de33d9fe332f5b1b1430a74ad44294463`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read:
   - `AGENTS.md`;
   - all CURRENT project rules;
   - predecessor Python call-725 report;
   - accepted HJB propagation-aware parity report;
   - accepted KFE parity closeout report;
   - accepted end-to-end aggregate parity closeout report;
   - `validators/multi_province/mp4b_beijing_household_source_map.json`;
   - `validators/multi_province/matlab/mp4b_beijing_household_wrapper.m`;
   - `validators/multi_province/matlab/mp4b_beijing_household_parity_runner.m`;
   - protected MATLAB `HANK_2ASSETS_HJB.m`, `HANK3_FOC.m`, `HANK3_cost.m`, `lab_solve2.m` as read-only source evidence;
   - accepted source-extracted MATLAB HJB-only evaluator artifacts under the HJB parity root if present.

## 4. Hard boundary

Task type:

`ISOLATED_MATLAB_CALL725_TERMINATION_PARITY__NO_GE__NO_PRODUCTION_CHANGE`

Forbidden:

- 2018 annual steady-state or GE outer loop;
- any province other than isolated Anhui call 725;
- R/PLM execution;
- Python HJB/KFE scientific rerun;
- production/model/test/source modification;
- any edit to protected MATLAB sources;
- changing equations, grid, prices, tax, transfer, borrowing spread, cost parameters, `Delta`, `crit`, or KFE semantics;
- G1/G2 gauge redesigns;
- adaptive row, mass-normalization gauge, pseudoinverse, regularization, fallback, grid expansion, clipping, or alternate solver;
- automatic retries;
- shock/IRF/Results work.

The only authorized MATLAB numerical comparison is:

`num.maxit = 100` versus `num.maxit = 500`.

`num.maxiter` and every other numerical field remain at their source values unless the Phase-0 source audit proves `num.maxiter` is the HJB ceiling instead of `num.maxit`; if that occurs, STOP and report the source mapping rather than silently changing a different field.

## 5. Protected MATLAB source identity and path authority

Logical protected root:

`C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Physical protected root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Require exact `C:\MatlabProgram -> D:\MatlabProgram` Junction evidence using the already accepted finite-root method. Do not use Java canonical-path substitution.

Required SHA-256:

- `HANK_2ASSETS_HJB.m` `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- `HANK3_FOC.m` `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`;
- `HANK3_cost.m` `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`;
- `lab_solve2.m` `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.

Any mismatch: STOP before MATLAB scientific execution.

## 6. Frozen Python predecessor evidence

Predecessor evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-hjb-replay-and-bounded-continuation-20260904-001`

Require audit-manifest SHA-256:

`B15FE27D8531D5A1CE65E5D881327F820D82501FABD10B789F9F8B0544C7A0CF`.

Reuse only; do not rerun Python.

Frozen call-725 HJB-active state:

- province `安徽`;
- zero-based province index `11`;
- outer iteration `24`;
- global household call `725`;
- `rah=0.09`;
- `rb=0.02`;
- `tau=0.05`;
- `w=16.82014806560587`;
- `Tt=0.1`;
- `rb_gap=0.07`.

Frozen Python HJB100:

- converged `false`;
- iterations `100`;
- statistic `0.3038218386543494`.

Frozen Python HJB500:

- converged `true`;
- iterations `196`;
- statistic `2.2986279546444166e-10`.

Frozen Python HJB500 + legacy-KFE isolated aggregates:

- `C_ss=10.434969443057815`;
- `L_ss=0.6241861388467347`;
- `A_ss=9.212879584614942`;
- `B_ss=-1.5496915046150406`;
- `A_ss+B_ss=7.663188079999902`.

Permanent evidence caveat remains:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`.

## 7. Phase 0 — mandatory zero-call MATLAB contract audit

Before any MATLAB household call, inspect the protected source and accepted source maps/evaluators.

Required conclusions to freeze in a new contract artifact:

1. confirm the HJB loop uses `num.maxit` as the finite HJB iteration ceiling and uses `num.crit=1e-7`, `num.Delta=1000`;
2. confirm grid/parameter bindings:
   - `ga=2`, `alphap=1`, `alphal=1`, `rho=0.05`, `frisch_l=0.2`;
   - `I=20`, `bmin=-2`, `bmax=5`, `J=20`, `amin=0`, `amax=10`;
   - `Nz=2`, `z=[0.8,1.3]`, switch matrix `[[-1/3,1/3],[1/3,-1/3]]`;
   - `chi0=0.1`, `chi1=2`, `a_bar=1e-6`;
3. identify every `results.*` field that affects HJB initialization, iteration, post-loop operator, KFE, or aggregates;
4. prove that any required field not present in the durable call-725 localization is either:
   - execution-inactive for the household solution, or
   - reconstructable without rerunning GE from already persisted evidence;
5. if a noncaptured/nonreconstructable field materially affects HJB/KFE/aggregates, STOP before execution with:

`MP4C_2018_CALL725_MATLAB_SAME_ACTIVE_INPUT_BLOCKED__REQUIRED_HOUSEHOLD_INPUT_NOT_CAPTURED__NO_MATLAB_RUN`.

Do not fill an execution-critical missing field by guess.

The audit must also determine whether the existing accepted source-extracted HJB-only evaluator can be safely reused/adapted in the external evidence root. Prefer an HJB-only evaluator for the 100/500 convergence comparison because it avoids coupling the HJB termination question to the KFE.

No protected MATLAB source may be copied and scientifically edited. A validation-only external evaluator may reproduce already accepted source-extracted HJB-only logic if its source mapping is explicit and audited.

Required Phase-0 marker:

`MP4C_2018_CALL725_MATLAB_SAME_ACTIVE_INPUT_CONTRACT_AUDIT_PASS__TWO_CALL_BUDGET_OPEN`.

## 8. Phase A — MATLAB HJB100 same-active-input replay

After Phase 0 PASS, run exactly one MATLAB HJB-only evaluation on the call-725 active input with:

- source initialization;
- source grid/parameters;
- `Delta=1000`;
- `crit=1e-7`;
- `maxit=100`.

Prefer the accepted source-extracted HJB-only evaluator architecture used by the HJB parity project, adapted only in fresh external evidence to the frozen 800-state contract. Do not alter protected source.

Persist, where source-observable:

- converged flag;
- iteration count;
- convergence statistic;
- value/policy finiteness;
- iteration and post-loop operator shape/nnz;
- mathematical sparse support and values;
- warning/error status.

Compare to the frozen Python HJB100 using the accepted propagation-aware parity contract:

- convergence boolean and iteration count exact if both observable;
- converged/nonconverged status is a hard gate;
- same-input primitive/coefficient replay uses `128*eps64*max(1,abs(x),abs(y))`;
- mathematical sparse support ignores only exact stored zeros;
- independent solver-propagated raw differences are diagnostic only if all same-input source replay gates pass.

Expected scientific question, not assumed result:

Does protected MATLAB also fail to satisfy `crit` by HJB iteration 100 on this same active state?

No KFE is run in Phase A.

## 9. Phase B — MATLAB HJB500 same-active-input continuation

Run Phase B only if the Phase-A input contract is valid and the MATLAB HJB100 result is durably persisted.

Run exactly one second MATLAB HJB-only evaluation from the same original source initialization. The sole authorized numerical change is:

`num.maxit: 100 -> 500`.

Do not warm-start from the HJB100 terminal value.

Persist the same HJB diagnostics as Phase A.

If MATLAB reports convergence, compare to the frozen Python HJB500 under the accepted propagation-aware parity contract. Exact iteration count should be compared when the source-extracted evaluator exposes it. If MATLAB iteration count/statistic cannot be observed without modifying protected source, report that limitation explicitly and do not invent it.

If MATLAB remains nonconverged by 500, STOP before KFE and classify accordingly.

## 10. Phase C — one unchanged MATLAB legacy KFE / household output after HJB500 convergence

Only if Phase-B MATLAB HJB converges, run exactly one source-faithful MATLAB legacy KFE on the Phase-B post-loop operator, preferably through the already accepted source-extracted KFE evaluator architecture.

Use exactly:

- 800 states;
- MATLAB one-based contaminated row `floor(0.37*800)=296`;
- unit-row replacement;
- RHS `0.007` at that row;
- full direct solve;
- normalization by `sum(raw_g)*db*dah`;
- `db=7/19`, `dah=10/19`;
- no dz/productivity/trapezoid weight;
- no G1/G2;
- no fallback or retry.

Report:

- solver warnings/errors;
- raw finiteness;
- normalization factor and normalized mass;
- min/max density if density is exposed;
- negative count / weighted negative mass if exposed;
- raw contaminated residual and accepted backward-error certificate if exposed;
- source household aggregates `Ct`, `Lt`, `At`, `Bt`, `At+Bt`.

Compare MATLAB aggregates with the frozen Python HJB500+legacy-KFE aggregates using the already accepted same-input rule and finite-sum aggregate contract. Do not introduce a broader tolerance after observing output.

If only aggregate outputs are source-observable, aggregate parity is still sufficient for this task's termination-policy cross-language classification; do not instrument protected source to expose hidden density internals.

## 11. Strict scientific budget

Maximum MATLAB scientific calls:

- HJB100: `1`;
- HJB500: `1`;
- MATLAB legacy KFE: `1` only after HJB500 convergence.

If the HJB-only evaluator internally performs no KFE, count these separately as above.

If instead the only source-valid route is a whole-household protected call that internally includes KFE, document the exact call decomposition before execution and keep the total protected household call count at maximum `2`; do not additionally run a separate KFE.

In all cases:

- automatic retries `0`;
- Python scientific reruns `0`;
- GE/stationary annual outer-loop calls `0`;
- R/PLM `0`;
- shock/IRF `0`.

## 12. Required classifications

Choose the strongest supported result:

- `MATLAB_CALL725_HJB100_NONCONVERGED_AND_HJB500_CONVERGED__PYTHON_HJB_CEILING_DIAGNOSIS_CROSS_LANGUAGE_SUPPORTED__LEGACY_KFE_AGGREGATES_PARITY_PASS__PRODUCTION_TERMINATION_POLICY_OWNER_REVIEW_REQUIRED`;
- `MATLAB_CALL725_HJB100_NONCONVERGED_AND_HJB500_CONVERGED__LEGACY_KFE_OR_AGGREGATE_PARITY_FAILS__CROSS_LANGUAGE_TERMINATION_POLICY_NOT_YET_ACCEPTED`;
- `MATLAB_CALL725_HJB100_CONVERGED__PYTHON_MATLAB_TERMINATION_DIVERGENCE_REQUIRES_FORENSIC__NO_PRODUCTION_CHANGE`;
- `MATLAB_CALL725_HJB500_NONCONVERGED__HJB_CEILING_DIAGNOSIS_NOT_CROSS_LANGUAGE_CLOSED__NO_PRODUCTION_CHANGE`;
- `MATLAB_CALL725_SAME_ACTIVE_INPUT_EXECUTION_BLOCKED__SOURCE_CONTRACT_OR_OBSERVABILITY_INSUFFICIENT__NO_PRODUCTION_CHANGE`.

Do not classify the task as production acceptance even if the strongest PASS case occurs.

## 13. Evidence root

Preferred fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-matlab-same-active-input-hjb100-hjb500-20260904-001`

Persist at minimum:

- `authority_and_source_identity.json`;
- `junction_and_matlab_environment.json`;
- `call725_matlab_active_input_contract.json`;
- `source_dependency_audit.json`;
- external evaluator/wrapper source and SHA-256;
- zero-call smoke/preflight receipt;
- `matlab_hjb100_result.json` or equivalent MAT+compact JSON;
- `matlab_hjb500_result.json` if Phase B runs;
- `matlab_legacy_kfe_or_household_result.json` if Phase C runs;
- `python_predecessor_reuse_identity.json`;
- `matlab_python_termination_and_aggregate_comparison.json`;
- MATLAB stdout/stderr/warnings;
- scientific-call ledger;
- `classification.json`;
- `audit_manifest.json`.

No helper/evaluator source may be committed to the repository.

## 14. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_MATLAB_SAME_ACTIVE_INPUT_HJB100_HJB500_AND_LEGACY_KFE_REPLAY_REPORT.md`

The report must explicitly state:

- protected MATLAB source identities and exact junction evidence;
- which `results.*` fields are HJB/KFE execution-active;
- whether the contract is full same-input or same-HJB-active-input and why;
- HJB100 result;
- HJB500 result;
- MATLAB/Python convergence comparison;
- MATLAB/Python aggregate comparison if Phase C runs;
- complete call budget and zero retries;
- no production change;
- no 2018 GE/annual rerun;
- no IRF/Results work;
- permanent capture-time hash caveat.

## 15. Publication

If the bounded validation completes consistently, only a report-only commit + push is authorized.

Suggested commit message:

`Compare MP4C 2018 call-725 MATLAB HJB termination behavior`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean.

PASS terminal:

`MP4C_2018_CALL725_MATLAB_SAME_ACTIVE_INPUT_HJB_TERMINATION_REPLAY_COMPLETE__CROSS_LANGUAGE_CEILING_BEHAVIOR_CLASSIFIED__NO_GE_NO_PRODUCTION_CHANGE`

Blocked terminal:

`MP4C_2018_CALL725_MATLAB_SAME_ACTIVE_INPUT_HJB_TERMINATION_REPLAY_BLOCKED__NO_GE_NO_PRODUCTION_CHANGE`

No automatic production maxit change, 2018 GE rerun, shock, or IRF task is authorized inside this task.