# CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_PYTHON_MATLAB_HJB_INITIALIZATION_SOURCE_PARITY_FORENSIC

Date: 2026-09-04

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / read-only source-forensic executor

Owner: final scientific authority

## 1. Immediate authority and purpose

Immediate live parent at publication:

`3716ddd0ca0c39ce45ecfab96f4b0119046ce5dd`

The parent MATLAB call-725 replay established:

- MATLAB HJB100: nonconverged at 100, statistic `1.179090496462085`;
- Python frozen HJB100: nonconverged at 100, statistic `0.3038218386543494`;
- MATLAB HJB500: converged at 275;
- Python frozen HJB500: converged at 196;
- both unchanged legacy KFE solves are admissible after each language's converged HJB;
- all five isolated household aggregates materially differ.

This disproves the assumption that the two call-725 executions were already a strict same-initialization numerical parity pair.

Before any production `maxit` change or further HJB/KFE execution, this task must determine whether the cross-language divergence is already explained by a **source-initialization contract mismatch** between protected MATLAB `HANK_2ASSETS_HJB.m` and the Python annual empirical helper `_source_initial_arrays(...)`.

This is a read-only/source-local forensic task. It does not authorize a production repair or any HJB/KFE/GE rerun.

## 2. Live continuity

At execution start:

1. `git fetch origin`;
2. require this exact task on live `origin/main` as direct child of `3716ddd0ca0c39ce45ecfab96f4b0119046ce5dd`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read `AGENTS.md`, all CURRENT project rules, this task, the parent MATLAB replay report, the Python call-725 replay report, accepted HJB propagation-aware parity report, accepted KFE/aggregate parity reports, and relevant source-map/validator files.

## 3. Hard boundary

Task type:

`READ_ONLY_HJB_INITIALIZATION_SOURCE_CONTRACT_FORENSIC__NO_HJB_NO_KFE_NO_MODEL_RERUN`.

Forbidden:

- MATLAB HJB solve;
- Python HJB solve;
- MATLAB or Python KFE solve;
- protected household scientific call;
- GE/stationary/annual rerun;
- R/PLM;
- shock/IRF/Results;
- modifying repository source/test/validator files;
- modifying protected MATLAB source;
- changing `maxit`, `crit`, `Delta`, grid, calibration, prices, taxes, transfer, borrowing spread, HJB/KFE equations, or solver semantics;
- inferring a production repair before direct source evidence.

Allowed:

- read-only protected-source inspection;
- read-only GitHub source inspection;
- hashing;
- exact algebra/source-expression comparison;
- reuse of already persisted initialization arrays or manifests;
- non-model local arithmetic on already persisted scalars/arrays if required to verify an expression identity;
- no-overwrite external evidence generation.

Scientific model-call ledger must remain all zero.

## 4. Protected MATLAB authority

Logical root:

`C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Physical root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Reuse the already certified finite-root/Junction authority. Fresh hash checks are allowed.

Required protected SHA-256:

- `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`;
- `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`;
- `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.

Stop if the protected HJB/labor source identity does not match.

## 5. Python sources to audit exactly

Read and hash:

- `validators/multi_province/mp4b_python_empirical.py` — current Git blob `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c` at task-authoring parent;
- `exports/matlab_faithful_two_asset_ha.py` — current Git blob `9e7dc9556a2b76811e78f89999abecc045886106`;
- `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py` — current Git blob `0033baee136c0328e80ffb8b794a88d4405c976c`.

The audit must trace the actual annual execution chain proving whether each household in `run_python_once(...)`, including call 725, receives initial arrays from `_source_initial_arrays(...)` before entering the accepted faithful HJB solver.

## 6. Mandatory source-expression audit

Do not assume the defect. Establish it or reject it from direct source evidence.

### 6.1 Freeze the MATLAB source initialization formulas

From protected `HANK_2ASSETS_HJB.m`, identify exact line ranges and expressions for:

- effective/tapered illiquid return as a function of `a`, `amax`, and `rah`;
- liquid rate including the borrowing spread for `b<0`;
- the nonlabor-income / `temp` object passed into `lab_solve2` or equivalent initialization labor equation;
- initialization wage object;
- initial labor root equation and arguments;
- initial consumption/resource object;
- initial value `V0` / `v0` object;
- baseline labor array passed into the HJB iteration, if separately stored.

Persist exact source excerpts or line-numbered hashes within copyright-safe project evidence; do not edit the source.

### 6.2 Freeze the Python initialization formulas

From `_source_initial_arrays(...)` and its paired preflight, record exact expressions for:

- `effective`;
- `rb`;
- `temp`;
- `wage`;
- labor-root call;
- `c` / `c0`;
- initial value;
- baseline labor.

The current source visibly contains the expressions:

`temp = effective*effective + rb*b + Tt`

and

`c = wage*l + rb*b + Tt`

but this task must classify them only after comparing to protected MATLAB source semantics.

### 6.3 Freeze the meaning of `effective`

From `matlab_faithful_illiquid_return(...)`, determine whether `effective` is:

- an illiquid return **rate**, or
- already an illiquid asset-income flow.

Cross-check against the accepted faithful drift formula, where the same object enters `mu_a`.

Record dimensional/economic role using source semantics only; do not replace source authority with intuition.

## 7. Exact formula-parity matrix

Create a row-by-row matrix for MATLAB versus Python initialization objects:

- tapered return object;
- illiquid income contribution;
- liquid income contribution;
- transfer contribution;
- labor `temp` argument;
- wage argument;
- labor-root equation;
- initial consumption/resource expression;
- initial utility/value expression;
- array ordering and shape.

For each row classify exactly one:

- `SOURCE_IDENTICAL`;
- `REPRESENTATION_ONLY`;
- `PYTHON_SOURCE_INITIALIZATION_MISMATCH`;
- `MATLAB_SOURCE_EXTRACTED_EVALUATOR_MISMATCH`;
- `INSUFFICIENT_EVIDENCE`.

No tolerance can turn an expression mismatch into parity.

## 8. Reuse persisted call-725 initialization evidence only

Evidence roots:

Python:

`D:\ProjectTemp\ch5-mp4c-2018-call725-hjb-replay-and-bounded-continuation-20260904-001`

manifest SHA:

`B15FE27D8531D5A1CE65E5D881327F820D82501FABD10B789F9F8B0544C7A0CF`

MATLAB:

`D:\ProjectTemp\ch5-mp4c-2018-call725-matlab-termination-replay-after-path-recertification-20260904-001`

manifest SHA:

`87500FF3121ECBBEE1E18A0A574371E06AC2B03B6B24B13465FCFBBF1E02457B`

Inspect whether either root already contains:

- original `V0` / initial-value array;
- baseline-labor array;
- source-initialization intermediate arrays;
- hashes/digests of those objects.

If both sides have directly comparable persisted objects, compare them without rerun and report:

- shape/order identity;
- max absolute difference;
- first differing `(b,a,z)` state;
- whether the difference is exactly predicted by the source-expression mismatch.

If one side did not persist a needed object, state:

`CROSS_LANGUAGE_INITIAL_ARRAY_DIRECT_COMPARISON_UNAVAILABLE__NO_REGENERATION`

Do not regenerate a missing scientific initialization by invoking HJB/household routines in this task.

## 9. Accepted-HJB-parity scope audit

Explain why the earlier accepted 50-state MATLAB/Python HJB parity can coexist with the present 800-state divergence.

Determine from the accepted parity artifacts whether that test:

- supplied a pre-frozen identical initialization to both languages;
- tested the empirical annual `_source_initial_arrays(...)` constructor itself;
- or only tested the HJB fixed-point solver conditional on an already accepted initialization.

Also trace the 2009 Beijing same-input contract:

`D:\ProjectTemp\ch5-mp4b-beijing-household-20260831-001\beijing_same_input_contract.json`

SHA:

`FE833FAEB48521CD0C7594627AF6FB5012F9497A455E9B2C5E7490E0C40E6F22`

and `validators/multi_province/mp4b_beijing_household_source_map.json`.

Determine whether the earlier Beijing preflight independently validated the MATLAB source initialization formula or merely compared Python-generated arrays to a contract that already contained the same mapping. Do not overstate prior acceptance.

## 10. Causal relevance to call 725

If a direct initialization expression mismatch is established, trace its reachability:

`run_python_once -> solve_batch -> _source_initial_arrays -> solve_matlab_source_postloop_household -> solve_matlab_faithful_hjb`.

Confirm whether call 725 necessarily used the same constructor and therefore inherited the mismatch.

Do not claim that the initialization mismatch fully explains every later HJB/aggregate difference unless the available evidence proves that. Allowed statement:

`INITIALIZATION_MISMATCH_IS_A_DIRECT_UPSTREAM_MATERIAL_PARITY_BREAK_AND_MUST_BE_REPAIRED_BEFORE_TERMINATION_POLICY_COMPARISON`.

## 11. Required classification

Choose strongest supported:

1. `PYTHON_EMPIRICAL_HJB_INITIALIZATION_MISMATCH_CONFIRMED__CALL725_WAS_NOT_STRICT_SAME_INITIALIZATION__TERMINATION_POLICY_COMPARISON_INVALID_UNTIL_REPAIR`

2. `MATLAB_SOURCE_EXTRACTED_INITIALIZATION_MISMATCH_CONFIRMED__MATLAB_CALL725_REPLAY_NOT_SOURCE_IDENTICAL__REPLAY_MUST_BE_REPAIRED_BEFORE_POLICY_REVIEW`

3. `INITIALIZATION_FORMULAS_SOURCE_IDENTICAL__CROSS_LANGUAGE_DIVERGENCE_LIES_DOWNSTREAM__FURTHER_HJB_FORENSIC_REQUIRED`

4. `HJB_INITIALIZATION_SOURCE_PARITY_FORENSIC_INCONCLUSIVE__NO_PRODUCTION_CHANGE`.

If classification 1 is supported, report the exact minimal source-level correction candidate, but **do not modify it**. Explicitly distinguish:

- source-backed correction candidate;
- production authorization (not granted).

## 12. Scientific-call ledger

Final counts must be:

- MATLAB HJB = 0;
- Python HJB = 0;
- MATLAB KFE = 0;
- Python KFE = 0;
- protected household calls = 0;
- GE/stationary/annual model calls = 0;
- R/PLM = 0;
- shock/IRF/Results = 0.

Read-only source inspection and evidence-file hashing are not scientific calls.

## 13. Evidence root

Use fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-hjb-initialization-source-parity-forensic-20260904-001`

Persist at minimum:

- `authority_and_source_identity.json`;
- `matlab_initialization_source_map.json`;
- `python_initialization_source_map.json`;
- `illiquid_return_semantic_contract.json`;
- `initialization_formula_parity_matrix.csv`;
- `annual_python_reachability_trace.json`;
- `accepted_hjb_parity_scope_audit.json`;
- `beijing_same_input_contract_scope_audit.json`;
- persisted-initial-array availability/comparison evidence;
- `classification.json`;
- `zero_science_ledger.json`;
- stdout/stderr;
- `audit_manifest.json`.

Hash and read back all evidence.

## 14. Report and publication

Write only:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_PYTHON_MATLAB_HJB_INITIALIZATION_SOURCE_PARITY_FORENSIC_REPORT.md`

If completed consistently, only report-only commit + non-force push is authorized.

Suggested commit:

`Diagnose MP4C call-725 HJB initialization parity`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean.

PASS terminal:

`MP4C_2018_CALL725_HJB_INITIALIZATION_SOURCE_PARITY_FORENSIC_COMPLETE__UPSTREAM_PARITY_BREAK_CLASSIFIED__NO_MODEL_RERUN_NO_PRODUCTION_CHANGE`

Blocked terminal:

`MP4C_2018_CALL725_HJB_INITIALIZATION_SOURCE_PARITY_FORENSIC_BLOCKED__NO_MODEL_RERUN_NO_PRODUCTION_CHANGE`.

Do not launch a repair, HJB rerun, 2018 GE, shock, or IRF inside this task. Return to ChatGPT L3 / Owner.