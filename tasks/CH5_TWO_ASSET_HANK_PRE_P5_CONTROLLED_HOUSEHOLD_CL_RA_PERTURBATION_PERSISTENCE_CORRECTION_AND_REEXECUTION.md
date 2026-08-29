# CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_PERSISTENCE_CORRECTION_AND_REEXECUTION

## Task

Correct only the external MATLAB result-persistence/container defect from the predecessor controlled household experiment, then execute a fresh bounded four-run household-block robustness experiment and persist the requested aggregate evidence.

This task explicitly authorizes one replacement MATLAB baseline run because the predecessor baseline HJB call returned successfully but **no scientific output was persisted** due solely to an external summary-container assignment defect. The predecessor run is not reusable evidence and is not classified as a scientific numerical failure.

This task does **not** authorize P5 acceptance, P1-P4 reruns, outer-equilibrium execution, source modification, tolerance tuning, AR(1), transition, IRF, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted predecessor state

Predecessor blocked execution report commit:

`240fe1432722eac6996a1093c5783c102ef91aba`

Predecessor task authority commit:

`8aa45b948a0077cd620746ba4688bd93acd46a77`

Accepted P1-P4 numerical evidence commit:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

P1-P4 remain accepted and must not be rerun.

## Scientific interpretation

This remains the Owner-requested **partial-equilibrium HA household-block comparative static**.

For each implementation, all household inputs outside the endogenous household solution are fixed. Only the illiquid return changes:

`r_a / rah: 0.040 -> 0.041`.

Endogenous household outputs are allowed to respond, including policies, stationary distribution, `C_hh`, `L_hh`, `A_hh`, and `B_hh`.

Do not call any outer MATLAB equilibrium/turn/shock/multi-province update. In particular, do not call:

- `HANK_mp_1turn`
- `HANK_mp_1eq`
- `mpHANK_equilibrium_2000`
- `multi_prov_HANK_12sts`
- any shock routine

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_EXECUTION.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_EXECUTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HOUSEHOLD_CALL_SNAPSHOT_AUTHORITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- accepted Python R4 HJB/KFE/steady-state source.

Verify live Python `src/tests` remain unchanged from:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

If drift exists, stop:

`BLOCKED_CONTROLLED_CL_RA_PERSISTENCE_CORRECTION_PYTHON_SOURCE_DRIFT`

## MATLAB authority and snapshot

Use the already Owner-approved frozen snapshot only:

- candidate: `C2016-P10`
- year: `2016`
- province: `P10 江苏省`
- cache:
  `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\Multi_Province_12sts_2016.mat`
- cache SHA-256:
  `FC58289EC695A6B7583405CC7F6A7FC3C88B0512F0C93CEAB76F3442CA9F771A`
- observed native saved `rah`:
  `0.040026998056627239`

Accepted original MATLAB execution source:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

Also require:

- `HANK3_cost.m` SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m` SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

The diagnostic-patch HJB must not be executed.

## Predecessor defect diagnosis to preserve

The predecessor scientific MATLAB harness failed only after the baseline HJB returned, at:

```matlab
rows(1) = summarize_output(out0, 0.040);
```

because an empty-field/preallocated struct container could not accept the populated summary struct.

Classification:

`MATLAB_EXTERNAL_RESULT_CONTAINER_PREALLOCATION_DEFECT`

This is output plumbing only. Do not alter any scientific input, formula, solver call, model source, grid, parameter, or tolerance to fix it.

## Corrected MATLAB harness authority

Create a new isolated external artifact root. Copy the predecessor frozen input/snapshot manifests read-only and verify their hashes where available.

Create a corrected MATLAB scientific harness from the predecessor harness with changes restricted to **result persistence and summary-container plumbing only**.

Required robustness of the corrected harness:

1. construct `R0` and `R1` from the same `st.results{10}` and verify pre-override identity;
2. prove all fields except `rah` are identical after override;
3. execute the accepted original HJB directly;
4. **immediately persist the raw returned output object after each HJB call before any summary/container assignment**;
5. only after raw persistence, compute a summary object and write JSON/table evidence.

Recommended persistence order:

```matlab
out0 = HANK_2ASSETS_HJB(..., R0, 0);
save(fullfile(root,'matlab_out_0040.mat'),'out0','-v7');

out1 = HANK_2ASSETS_HJB(..., R1, 0);
save(fullfile(root,'matlab_out_0041.mat'),'out1','-v7');
```

Then summarize using either independently named structs (`summary0`, `summary1`) or a preallocation proven to have exactly matching fields. Do not rely on empty-field struct assignment.

### Mandatory non-scientific plumbing preflight

Before any HJB call, execute exactly one pure-plumbing preflight that does **not** invoke a model or numerical solver. It must test the exact corrected output-container/serialization path using synthetic structs with the same summary field names/types expected from `summarize_output`.

The preflight must prove:

- assignment/collection of both synthetic summary rows succeeds;
- JSON serialization succeeds;
- raw `.mat` save/load succeeds;
- field names/order/types are stable enough for postprocessing.

If preflight fails, correct plumbing before scientific execution, refreeze, and repeat preflight only as needed until a final harness is frozen. Once the first scientific HJB call starts, no harness edit or rerun is allowed under this task.

### Diff gate

Produce the complete predecessor-harness -> corrected-harness diff and prove all modifications are confined to:

- struct preallocation/assignment;
- raw output save/load;
- summary serialization;
- artifact path plumbing.

Any scientific semantic change blocks execution.

Record corrected harness SHA-256 and bytes and freeze it before scientific execution.

## Explicit replacement-run authorization

Because the predecessor baseline returned but its output was not persisted, this new task authorizes a **fresh replacement baseline** at `rah=0.040` exactly once.

This replacement is permitted only after:

- all source/cache/input identity gates pass;
- the corrected harness passes the mandatory non-scientific plumbing preflight;
- the corrected harness is frozen;
- no scientific input differs from the predecessor authorized baseline.

The predecessor consumed baseline is not counted as evidence and must not be mixed numerically with the replacement run.

## MATLAB scientific execution budget

After all gates pass, execute exactly:

1. MATLAB baseline `rah=0.040` — one replacement invocation;
2. MATLAB perturbation `rah=0.041` — one invocation.

For both calls use exactly:

- `st.param`
- `st.grids{10}`
- `st.num`
- `st.CHI`
- identical copies of `st.results{10}` except `rah`
- `show_result=0`

Persist raw returned outputs immediately.

At the first scientific execution failure:

- stop MATLAB execution;
- do not edit the frozen harness;
- do not rerun;
- report the exact blocker.

## MATLAB required outputs

From each persisted returned object report:

- `C_hh = out.Ct` and independently verify `sum(out.C,'all')`
- `L_hh = out.Lt` and independently verify `sum(out.l,'all')`
- `A_hh = out.At`
- `B_hh = out.Bt`
- `sum(out.g,'all')`
- `out.convergent` if present
- any HJB/KFE/normalization diagnostic exposed by the accepted original source/output

Require internal aggregate identities (`Ct == sum(C)`, `Lt == sum(l)`) to machine-scale floating consistency. If they fail materially, classify scientific failure and stop before interpretation.

## Python controlled runs

Only if both MATLAB outputs are successfully persisted and summarized, execute the Python pair.

Use accepted R4 configuration. Construct through an external harness only; do not modify production source.

Execute exactly once each:

1. Python baseline `r_a=0.040`;
2. Python perturbation `r_a=0.041`.

Change no other input, initialization, grid, productivity support/law, buffer protocol, HJB numerics, KKT/generator/KFE tolerance, or aggregation convention.

Compute:

`C_hh = sum(g*c)`

`L_hh = sum(g*l)`

using the solved primary stationary probability mass and primary policy arrays.

Also report:

- `A_hh`, `B_hh`
- primary and buffer HJB iterations/residuals
- KKT residuals
- generator validity
- truncation/common-core diagnostics
- connectivity/recurrent-class/left-nullity diagnostics
- KFE residual/normalization/minimum/negative mass
- mass-density consistency

At any scientific failure, stop and do not rerun or tune.

## Requested result tables

Report exactly this compact level table:

| implementation | r_a | C_hh | L_hh |
|---|---:|---:|---:|
| MATLAB | 0.040 | ... | ... |
| Python | 0.040 | ... | ... |
| MATLAB | 0.041 | ... | ... |
| Python | 0.041 | ... | ... |

Also report within-language response table:

| implementation | Delta C_hh | %Delta C_hh | Delta L_hh | %Delta L_hh |
|---|---:|---:|---:|---:|
| MATLAB | ... | ... | ... | ... |
| Python | ... | ... | ... | ... |

Definitions:

`Delta C_hh = C_hh(0.041)-C_hh(0.040)`

`Delta L_hh = L_hh(0.041)-L_hh(0.040)`

`%Delta X = 100 * Delta X / X(0.040)`.

Report cross-language level differences and differences in the comparative-static responses, but do not invent an exact-native-level parity tolerance because the native MATLAB snapshot and Python R4 fixture are not the same calibration/object.

## Supplementary interpretation

Return exactly one:

- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_SUPPORTS_OWNER_ACCEPTANCE`
- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_NEEDS_OWNER_DISCUSSION`
- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_FAIL_CLOSED`
- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_BLOCKED_SOURCE_OR_ENVIRONMENT`

Use `SUPPORTS_OWNER_ACCEPTANCE` only if:

- both MATLAB runs complete and persist valid outputs;
- both Python runs complete;
- each model's internal validity/aggregation checks pass;
- no unexplained response-sign contradiction or obviously material qualitative comparative-static inconsistency remains after accounting for the known different native calibrations/representations.

Do not convert this supplementary classification into P5 acceptance.

## Output

Write exactly one report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_PERSISTENCE_CORRECTION_AND_REEXECUTION_REPORT.md`

The report must contain:

- live/source/cache identities;
- predecessor blocker and why replacement baseline is authorized;
- complete harness diff;
- plumbing-preflight evidence;
- corrected harness identity;
- proof only `rah/r_a` differs within each pair;
- exact execution counts;
- raw output artifact hashes;
- all aggregate levels and deltas;
- validity diagnostics;
- requested compact tables;
- supplementary classification;
- forbidden-operation check;
- recommended next gate.

## Commit/push authorization

Only the report may be added to the repository.

If and only if it is the sole repository change:

- stage only the report;
- create one commit;
- fresh-fetch remote main;
- fast-forward push only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Complete controlled household C L r_a robustness after persistence fix`

## Forbidden operations

Do not:

- rerun P1-P4;
- execute outer MATLAB equilibrium/turn/shock/multi-province routines;
- execute diagnostic-patch HJB;
- modify MATLAB/Python production source/tests;
- modify/regenerate the selected cache;
- change any scientific input except `rah/r_a` within each baseline/perturbation pair;
- change grids, equations, FOCs, productivity law, boundary/KKT/generator/KFE logic, initialization, or tolerances;
- tune after seeing output;
- edit/rerun the corrected harness after scientific execution begins;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, dynamics, or Results;
- merge, rebase, reset, or force-push.

## Recommended next gate

If the supplementary experiment completes and supports acceptance, the only next scientific gate is:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

If the experiment reveals an unexplained scientific discrepancy, P5 remains blocked for targeted diagnosis.