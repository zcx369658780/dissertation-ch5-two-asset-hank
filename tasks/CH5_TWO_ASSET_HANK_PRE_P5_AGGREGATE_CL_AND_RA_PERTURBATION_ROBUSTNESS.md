# CH5_TWO_ASSET_HANK_PRE_P5_AGGREGATE_CL_AND_RA_PERTURBATION_ROBUSTNESS

## Task

Before Owner P5 final acceptance, add one supplementary native-model robustness check requested by the Owner:

1. compute household aggregate consumption and labor, `C_hh` and `L_hh`, for both the accepted Python two-asset HA model and the designated MATLAB two-asset HA model;
2. repeat each model after changing only the illiquid return from `r_a = 0.040` to `r_a = 0.041`, holding every other model input fixed within that implementation;
3. report baseline levels, perturbed levels, absolute changes, and percentage changes side by side.

This is a **pre-P5 supplementary robustness experiment**. It does not replace the already completed P1–P4 shared-input numerical parity evidence, and it must not silently reinterpret native-model differences caused by accepted redesigns as a parity failure.

This task does **not** authorize P5 acceptance, AR(1), transition dynamics, IRFs, calibration extension, or Results claims.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted scientific baseline

Accepted Python scientific source baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Accepted P1–P4 numerical evidence commit:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Accepted P1–P4 status:

`MATLAB_PYTHON_TWO_ASSET_HA_NUMERICAL_PARITY_EVIDENCE_COMPLETE__OWNER_P5_ACCEPTANCE_PENDING`

Do not rerun P1, P2, P3, or P4 in this task.

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- accepted Python source needed to solve HJB/KFE and aggregate policy outcomes;
- current R4 steady-state fixture/configuration code and accepted steady-state report.

Verify live Python `src/tests` remain unchanged from `7a2388a2ba89073e307f05a909570e8c40a4be13` except later task/report-only commits.

If scientific source drift exists, stop:

`BLOCKED_PRE_P5_AGGREGATE_ROBUSTNESS_PYTHON_SOURCE_DRIFT`

## MATLAB source identity

Read-only verify the designated MATLAB source tree:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Require exact identities:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

Do not modify any MATLAB production source or helper.

## Native-model invocation authority

### Python

Use the accepted R4 household steady-state economic configuration as the native Python object, but execute through an external harness rather than modifying repository source.

For the baseline Python run use exactly the accepted R4 parameters and grids, including:

- `rho = 0.05`
- `gamma_c = 1.0`
- `phi = 1.0`
- `chi_0 = 0.05`
- `chi_1 = 1.0`
- `a_bar = 0.5`
- `r_a = 0.040`
- `r_b = 0.03`
- `tau = 0.0`
- wage = `1.0`
- migration cost = `0.0`
- labor weight = `1.0`
- all accepted R4 grids, productivity support, boundary law, HJB numerics, KKT/generator/KFE tolerances, initialization, and buffer protocol unchanged.

For the perturbed Python run change **only**:

`r_a: 0.040 -> 0.041`

Everything else, including initialization rule and all numerical tolerances, must remain identical.

Do not edit `_fixture_objects` or any production file. Construct the perturbed input in the external harness using the accepted public/internal production APIs exactly as they are.

### MATLAB

Identify the exact native driver/call configuration in the designated MATLAB date tree that invokes `HANK_2ASSETS_HJB.m` for the corresponding two-asset household block.

Record:

- exact driver/caller path(s);
- SHA-256 and bytes;
- the complete parameter values passed into the household block;
- grid sizes and ranges;
- productivity-state specification;
- exact output fields or arrays used for stationary distribution, consumption, and labor aggregation.

Do not infer or fabricate missing native inputs.

If there is no unique, auditable native invocation configuration in the designated tree, stop before MATLAB scientific execution with:

`BLOCKED_PRE_P5_AGGREGATE_ROBUSTNESS_MATLAB_NATIVE_INVOCATION_AUTHORITY`

For the MATLAB baseline, run the identified native household configuration unchanged.

For the perturbed MATLAB run change **only the economically corresponding illiquid return parameter** from `0.040` to `0.041` in an external copied input/harness. Do not alter the production source tree.

If the native baseline uses a mapped field name such as `Rah`, explicitly document the mapping to `r_a` and prove no other parameter changes.

## Important comparability note

The production MATLAB and Python household blocks contain previously accepted differences, including productivity representation, boundary/KKT implementation, candidate closure, stationary normalization, and the low-`a` MATLAB FOC legacy limitation.

Therefore this task has two distinct purposes:

1. **within each native implementation**: verify a clean `r_a` perturbation and compute internally valid steady-state aggregates;
2. **across implementations**: report the levels and comparative-static responses side by side.

Do **not** require machine-equality of native full-model `C_hh` or `L_hh` levels unless the two native configurations are proven to be the same economic/numerical object. The formal exact shared-input parity evidence remains P1–P4.

If the two native configurations differ materially in grids/productivity or other accepted redesign dimensions, state this clearly and compare the response to `r_a` as a robustness result, not as a new exact-parity criterion.

## Aggregate definitions

For each completed steady state compute household aggregate consumption and labor from the model's own stationary distribution and policy arrays.

### Python

Using the accepted KFE probability mass `g` and primary accepted HJB policy:

`C_hh = sum_{a,b,z} g(a,b,z) * c(a,b,z)`

For the scalar embedded labor case:

`L_hh = sum_{a,b,z} g(a,b,z) * l(a,b,z)`

If the production labor array has a final labor-choice dimension of length one, sum that single component. Do not average over states independently of `g`.

Also report `sum(g)`, KFE residual, minimum mass, HJB residual, and KKT residual so that `C_hh/L_hh` are tied to a valid solved state.

### MATLAB

Use the MATLAB model's own stationary distribution object and consumption/labor policy arrays.

If MATLAB stores density rather than probability mass, apply exactly the model's native quadrature/measure convention before aggregation. Show the formula and confirm the implied probability/weight normalization.

Report the native aggregate formula explicitly.

Do not substitute Python weights into MATLAB or vice versa.

## Execution budget

After all identity/configuration/preflight checks pass, authorize exactly four native steady-state scientific runs:

1. Python baseline `r_a=0.040` — exactly once;
2. Python perturbed `r_a=0.041` — exactly once;
3. MATLAB baseline native configuration — exactly once;
4. MATLAB perturbed configuration with only `r_a/Rah=0.041` — exactly once.

Order may be Python then MATLAB or MATLAB then Python, but every run is one-shot.

At the first scientific execution failure within an implementation:

- stop further runs for that implementation;
- do not repair, tune, change tolerance, or rerun;
- report the exact blocker.

If a pre-scientific harness/API/container defect is detected before any scientific run for that implementation, it may be corrected only if it is pure plumbing and does not change any model input, equation, grid, or tolerance. Freeze and hash the corrected harness before the scientific run.

## Required outputs

For both implementations and both `r_a` values report at minimum:

- `C_hh`
- `L_hh`
- `A_hh` if available
- `B_hh` if available
- HJB convergence/residual
- KKT/boundary residual if available
- KFE/stationarity residual
- mass/density normalization

Then report the requested compact comparison table:

| implementation | r_a | C_hh | L_hh |
|---|---:|---:|---:|
| MATLAB | 0.040 | ... | ... |
| Python | 0.040 | ... | ... |
| MATLAB | 0.041 | ... | ... |
| Python | 0.041 | ... | ... |

Also report within-language changes:

`Delta C_hh = C_hh(0.041) - C_hh(0.040)`

`Delta L_hh = L_hh(0.041) - L_hh(0.040)`

and percentage changes relative to baseline.

Report cross-language level differences and cross-language differences in the comparative-static changes, but do not invent a pass tolerance for native-model levels if the objects are not exactly identical.

## Interpretation classification

Return exactly one supplementary classification:

- `PRE_P5_NATIVE_AGGREGATE_ROBUSTNESS_SUPPORTS_OWNER_ACCEPTANCE`
- `PRE_P5_NATIVE_AGGREGATE_ROBUSTNESS_NEEDS_OWNER_DISCUSSION`
- `PRE_P5_NATIVE_AGGREGATE_ROBUSTNESS_BLOCKED_SOURCE_OR_ENVIRONMENT`

Use `SUPPORTS_OWNER_ACCEPTANCE` only if:

- both baseline and perturbed runs complete in both implementations;
- each solved state satisfies its own accepted numerical validity checks;
- `C_hh/L_hh` are correctly aggregated from each native stationary distribution;
- no unexplained sign reversal or obviously material comparative-static inconsistency appears between MATLAB and Python after accounting for accepted structural redesigns.

Do not convert this supplementary classification into P5 acceptance.

## Output file

Write exactly one report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_AGGREGATE_CL_AND_RA_PERTURBATION_ROBUSTNESS_REPORT.md`

The report must contain:

- live/source identities;
- exact MATLAB native invocation authority and parameter mapping;
- exact Python native configuration;
- proof that only `r_a` changed between each baseline/perturbed pair;
- all four execution counts;
- validity diagnostics;
- aggregate formulas;
- complete `C_hh/L_hh` results;
- baseline/perturbed comparison table;
- delta and percentage-response table;
- comparability limitations;
- supplementary classification;
- forbidden-operation check;
- recommended next gate.

## Commit/push authorization

Only the report may be added to the repository.

If and only if the report is the sole repository change:

- stage only the report;
- create one commit;
- fresh-fetch remote main;
- fast-forward push only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Record pre-P5 aggregate C L and r_a robustness`

## Forbidden operations

Do not:

- modify MATLAB or Python production source/tests;
- change any parameter other than `r_a` in the perturbed run;
- change grids, productivity process, initialization, equations, FOCs, boundary/KKT contracts, generator/KFE logic, or tolerances;
- rerun P1–P4;
- rerun any of the four one-shot native steady-state runs;
- tune after seeing outputs;
- claim exact native-model parity solely from this robustness experiment;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, or Results work;
- merge, rebase, reset, or force-push.

## Recommended next gate

If the supplementary experiment supports acceptance and independent review agrees:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

If it reveals a material unexplained discrepancy, P5 remains blocked pending a targeted diagnostic task.