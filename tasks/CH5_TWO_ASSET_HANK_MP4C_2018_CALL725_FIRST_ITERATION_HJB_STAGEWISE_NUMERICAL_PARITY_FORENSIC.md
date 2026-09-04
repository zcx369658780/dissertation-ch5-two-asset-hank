# CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_FIRST_ITERATION_HJB_STAGEWISE_NUMERICAL_PARITY_FORENSIC

Date: 2026-09-04

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / isolated first-iteration HJB forensic executor

Owner: final scientific authority

## 1. Immediate authority and purpose

Immediate live parent at publication:

`36b8efd69178441d8986cbb1fbd7148b73e568cb`

The parent accepted:

`CALL725_INITIALIZATION_ARRAYS_NUMERICALLY_PARITY_ACCEPTED__DIVERGENCE_BEGINS_INSIDE_HJB_ITERATION_OR_LINEAR_SOLVE`.

The pre-HJB initialization gate is therefore closed: Python and MATLAB call-725 initial `V0` and baseline labor arrays are machine-equivalent under the already frozen `128*eps64*max(1,abs(x),abs(y))` rule, and the regenerated Python arrays are digest-bound to the original call-725 evidence.

The unresolved scientific question is now the first HJB iteration itself:

> Starting from one exact common initialization, at what earliest stage do the protected MATLAB-faithful HJB and the accepted Python faithful HJB cease to be numerically/source equivalent: derivatives/boundaries, local policy selection, drift/rate assembly, sparse operator construction, linear-system construction, or the sparse linear solve?

This task authorizes only a bounded isolated first-iteration diagnostic. It does not authorize full HJB convergence, KFE, production changes, 2018 GE, annual reruns, shock/IRF, or Results work.

## 2. Live continuity

At execution start:

1. `git fetch origin`;
2. require this exact task on live `origin/main` as direct child of `36b8efd69178441d8986cbb1fbd7148b73e568cb`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, all CURRENT rules, this task, the initialization-array forensic report, the MATLAB call-725 replay report, the Python call-725 replay report, and the accepted HJB propagation-aware parity report.

## 3. Frozen source identities

Require:

- `exports/matlab_faithful_two_asset_ha.py` Git blob `9e7dc9556a2b76811e78f89999abecc045886106`;
- `validators/multi_province/mp4b_python_empirical.py` Git blob `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`;
- `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py` Git blob `0033baee136c0328e80ffb8b794a88d4405c976c`.

Protected MATLAB source SHA-256:

- `HANK_2ASSETS_HJB.m` `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- `HANK3_FOC.m` `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`;
- `HANK3_cost.m` `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`;
- `lab_solve2.m` `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.

No repository or protected scientific source may be modified.

## 4. Frozen call-725 state and numerics

Use only:

- province `安徽`;
- zero-based province index `11`;
- outer iteration `24`;
- global household call `725`;
- `rah=0.09`;
- `rb=0.02`;
- `rb_gap=0.07`;
- `tau=0.05`;
- `w=16.82014806560587`;
- `Tt=0.1`;
- grid `(20,20,2)` in `(b,a,z)` / MATLAB `(I,J,Nz)` order;
- `b=linspace(-2,5,20)`;
- `a=linspace(0,10,20)`;
- `z=[0.8,1.3]`;
- source switch matrix `[[-1/3,1/3],[1/3,-1/3]]`;
- `rho=.05`, `gamma=2`, `phi=5`, `chi0=.1`, `chi1=2`, `a_bar=1e-6`;
- `Delta=1000`, `crit=1e-7`, drift tolerance `1e-12`.

Do not change any numerical or economic parameter.

## 5. Evidence identities and the exact common initialization

Initialization-parity evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-initialization-array-numerical-parity-20260904-001`

Require final supplemental audit manifest SHA-256:

`817845439CDC77E2C3873AA3D9675E16704E0AB48263F02CFBD653626245D07C`.

MATLAB replay evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-matlab-termination-replay-after-path-recertification-20260904-001`

Require audit manifest:

`87500FF3121ECBBEE1E18A0A574371E06AC2B03B6B24B13465FCFBBF1E02457B`.

For the strict same-input pair, use the already persisted MATLAB HJB100 initialization arrays as the common authority:

- `v0` / initial value;
- `l0` / baseline labor;
- exact `b`, `ah`, `z` arrays.

Both MATLAB and Python first-iteration evaluators must consume the exact same float64 values after only explicit shape/orientation conversion. Do not regenerate MATLAB initialization and do not call `_source_initial_arrays(...)` in the strict pair.

Before scientific execution, persist canonical hashes of the common arrays and prove both evaluators ingest the same numeric arrays. If exact common-input plumbing cannot be established, STOP before scientific calls.

## 6. Evaluator architecture freeze before scientific calls

Prefer the already accepted source-extracted MATLAB HJB evaluator architecture from:

`D:\ProjectTemp\ch5-hjb-propagation-aware-final-20260830-001`

Accepted evaluator identity from prior authority:

`F6D33348329D242AC3C7D867D455DDD0B87184C00A5AD66332A1B62F359599FE`.

Create fresh external validation-only one-iteration wrappers if needed, but freeze them before any scientific output. Any adaptation may change only:

- input plumbing from the exact common arrays;
- 800-state grid size;
- deterministic persistence/serialization;
- explicit stopping after iteration 1.

It may not change HJB formulas, branch logic, boundary formulas, local-policy logic, source sparse assembly, linear-system construction, linear solver, or arithmetic ordering intentionally.

For Python, use the exact accepted faithful source logic in `solve_matlab_faithful_hjb`; an external one-iteration diagnostic copy/extractor is allowed only if source mapping proves scientific expressions are identical.

Required pre-call marker:

`MP4C_2018_CALL725_FIRST_ITERATION_EVALUATORS_AND_COMMON_INPUT_FROZEN__STRICT_STAGEWISE_BUDGET_OPEN`.

## 7. Exact first-iteration pipeline to expose

The Python faithful source currently defines the iteration pipeline as:

1. `old = V0`;
2. raw `vb_f`, `vb_b`, `va_f`, `va_b` from `old`;
3. liquid-boundary marginal-value replacement using baseline labor/resources;
4. per-cell local policy selection;
5. policy outputs: consumption, labor, transfer, adjustment cost, effective illiquid return, `mu_a`, `mu_b`, utility;
6. categorical liquid and transfer labels;
7. iteration rates `bb`, `bf`, `ab`, `af`;
8. sparse `BB`, `AAH`, `Bswitch`, full `A`;
9. linear matrix `M=(1/Delta+rho)I-A`;
10. `rhs = utility(:F) + old(:F)/Delta`;
11. one direct sparse solve for `V1`;
12. first-iteration statistic `max(abs(V1-V0))`.

The MATLAB source-extracted evaluator must expose the corresponding protected-source objects and exact source mapping.

Do not execute iteration 2. Do not execute post-loop KFE.

## 8. Phase A — strict common-input MATLAB first iteration

Run exactly one MATLAB source-extracted first-iteration evaluation from the persisted MATLAB `v0/l0` common arrays.

Persist all stage objects listed in Section 7, including raw derivative arrays, boundary-adjusted derivatives, categorical labels, continuous policy arrays, rate arrays, sparse component matrices, full `A`, `M`, RHS, `V1`, statistic, warnings, and linear-solve residual/backward-error diagnostics.

MATLAB first-iteration scientific call budget: `1`.

If post-call instrumentation fails, persist evidence and STOP. No retry.

## 9. Phase B — strict common-input Python first iteration

Only after Phase A is durably persisted.

Run exactly one Python faithful first-iteration evaluation using the exact same persisted MATLAB `v0/l0` common arrays and the same frozen state/grid/parameters.

Persist the same stage objects.

Python strict-common first-iteration scientific call budget: `1`.

If post-call instrumentation fails, persist evidence and STOP. No retry.

## 10. Stagewise comparator and earliest divergence rule

Compare in source order. The comparator must stop the causal classification at the earliest material mismatch, while still reporting already-persisted downstream objects diagnostically.

Frozen rules:

- categorical labels / branch masks: exact equality required;
- shapes/order: exact equality required;
- continuous same-input arrays/scalars: `128*eps64*max(1,abs(x),abs(y))`;
- sparse mathematical support: ignore only exact stored `0.0/-0.0`; do not epsilon-prune;
- sparse nonzero values: same machine rule;
- no post-observation tolerance broadening.

Required comparison order:

1. raw forward/backward derivatives;
2. boundary derivative replacements;
3. liquid/transfer categorical labels;
4. consumption/labor/transfer/cost/effective-return;
5. `mu_a`, `mu_b`, utility;
6. `bb/bf/ab/af`;
7. `BB`;
8. `AAH`;
9. `Bswitch`;
10. full `A`;
11. `M`;
12. RHS;
13. `V1` and statistic.

For each stage report max absolute difference, max normalized difference, mismatch count under the frozen rule, first/worst state or sparse entry, and PASS/MATERIAL.

## 11. Linear-solve classification rule

If `M` and RHS pass the direct same-input contract but `V1` is materially different, do not call that a formula mismatch. Compute for each solver output:

- `||M*V1-rhs||_inf`;
- accepted backward-error scale/certificate;
- difference between MATLAB/Python `V1`;
- condition/conditioning diagnostics only if they can be computed read-only without changing the solver.

Classify such a case as a direct-solve propagation / conditioning issue, not an HJB equation mismatch.

Do not regularize, change solver, use pseudoinverse, reorder intentionally, or retry.

## 12. Phase C — bounded native-initialization amplification probe

Run this phase only if the strict common-input pair reaches `M/RHS/V1` consistently and no earlier material source-formula mismatch has been found.

Reuse the already persisted digest-bound regenerated Python initialization arrays from the initialization-parity evidence root. Do not call `_source_initial_arrays(...)` again.

Run exactly one additional Python first iteration from those native Python arrays using the same frozen HJB pipeline.

Compare:

`Python native-init first iteration`

versus

`Python common-MATLAB-init first iteration`.

Purpose: quantify whether the machine-equivalent pre-HJB perturbation can be materially amplified by the first near-singular HJB solve.

This is diagnostic only. Do not infer long-run convergence causality from one step unless the evidence directly supports it.

Python native-probe budget: `1` maximum.

## 13. Strict scientific budget

Maximum new scientific evaluations:

- MATLAB source-extracted HJB first iteration: `1`;
- Python faithful strict-common HJB first iteration: `1`;
- Python native-initialization first-iteration probe: `1`, conditional on Section 12;
- retries: `0`.

Forbidden counts must remain zero:

- full HJB100/HJB500 rerun;
- iteration 2+;
- KFE;
- household steady-state composition;
- GE/stationary/annual 2018;
- R/PLM;
- shock/IRF/Results.

## 14. Required scientific classifications

Choose the strongest supported classification:

1. `CALL725_STRICT_COMMON_INPUT_FIRST_ITERATION_PARITY_PASS__NATIVE_MACHINE_PERTURBATION_AMPLIFICATION_DIAGNOSTIC_RECORDED__MULTI_ITERATION_PROPAGATION_FORENSIC_REQUIRED`

2. `CALL725_FIRST_ITERATION_PRE_SOLVE_SOURCE_PARITY_BREAK_CONFIRMED__EARLIEST_STAGE_IDENTIFIED__NO_PRODUCTION_CHANGE`

3. `CALL725_FIRST_ITERATION_LINEAR_SYSTEM_PARITY_PASS__DIRECT_SOLVE_PROPAGATION_DIVERGENCE_CONFIRMED__NO_SOLVER_CHANGE_AUTHORIZED`

4. `CALL725_FIRST_ITERATION_PARITY_FORENSIC_BLOCKED__COMMON_INPUT_OR_EVALUATOR_CONTRACT_NOT_CERTIFIED__NO_PRODUCTION_CHANGE`

Do not authorize `maxit=500`, solver replacement, production repair, or 2018 GE from this task.

## 15. Evidence root

Use fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-first-iteration-hjb-stagewise-parity-20260904-001`

Persist at minimum:

- authority/source identities;
- common-input array identity and exact hashes;
- MATLAB/Python evaluator source maps and hashes;
- zero-call preflight/freeze receipt;
- MATLAB first-iteration full stage artifacts;
- Python strict-common first-iteration full stage artifacts;
- stagewise comparison CSV/JSON;
- sparse-support/value comparisons;
- linear-system and backward-error comparison;
- conditional native-initialization amplification probe artifacts;
- scientific-call ledger;
- stdout/stderr/warnings;
- classification;
- `audit_manifest.json`.

Hash and read back every evidence artifact.

## 16. Report and publication

Write only:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_FIRST_ITERATION_HJB_STAGEWISE_NUMERICAL_PARITY_FORENSIC_REPORT.md`

If completed consistently, only report-only commit + non-force push is authorized.

Suggested commit:

`Diagnose MP4C call-725 first HJB iteration parity`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean.

PASS/completed terminal:

`MP4C_2018_CALL725_FIRST_ITERATION_HJB_STAGEWISE_FORENSIC_COMPLETE__EARLIEST_DIVERGENCE_CLASSIFIED__NO_KFE_NO_GE_NO_PRODUCTION_CHANGE`

Blocked terminal:

`MP4C_2018_CALL725_FIRST_ITERATION_HJB_STAGEWISE_FORENSIC_BLOCKED__NO_KFE_NO_GE_NO_PRODUCTION_CHANGE`

Stop after publication. Return to ChatGPT L3 / Owner for the next gate.