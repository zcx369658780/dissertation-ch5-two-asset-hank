# CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_EXECUTION

## Task

Execute the Owner-approved controlled two-asset HA household-block robustness experiment before P5.

The Owner has selected the MATLAB frozen household-call snapshot:

- candidate: `C2016-P10`
- year/data index: `2016 / 8`
- province: `P10 江苏省`
- canonical cache:
  `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\Multi_Province_12sts_2016.mat`
- cache SHA-256:
  `FC58289EC695A6B7583405CC7F6A7FC3C88B0512F0C93CEAB76F3442CA9F771A`
- observed native saved `results_in.rah`:
  `0.040026998056627239`

The Owner explicitly approves using this diagnostic-patch canonical cache **only as a frozen input snapshot** for the accepted original MATLAB HJB source. The cache is not treated as accepted-source output provenance.

The accepted original MATLAB HJB remains execution authority:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

The diagnostic-patch HJB that may have produced the cache has a different source identity and must not be executed or substituted.

## Scientific meaning

This is a **partial-equilibrium household-block comparative-static experiment**, not a re-equilibrated multi-province general-equilibrium steady state.

For each implementation, all exogenous/frozen household inputs and numerical settings must remain identical between baseline and perturbation except the illiquid return:

`r_a / rah: 0.040 -> 0.041`.

The household solver is allowed to endogenously change its own outputs in response to that one input change, including policies, stationary distribution, `C_hh`, `L_hh`, `A_hh`, and `B_hh`.

Do not interpret “all other variables fixed” as freezing endogenous household outputs or the stationary distribution. It means all **inputs outside the household solution** are fixed.

No outer-equilibrium object may be updated: wages, taxes, transfers, province data, migration costs, grids, productivity law, other rates, and all non-`rah` fields of the frozen MATLAB direct-call tuple remain unchanged.

Do not call `HANK_mp_1turn`, `HANK_mp_1eq`, `mpHANK_equilibrium_2000`, `multi_prov_HANK_12sts`, any shock routine, or any outer equilibrium/iteration code.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted predecessor evidence

Snapshot-authority report commit:

`079ec59cda8d46d2904af21b04dc8dc4afb301a3`

Accepted P1-P4 numerical evidence commit:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

P1-P4 must not be rerun.

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HOUSEHOLD_CALL_SNAPSHOT_AUTHORITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_AGGREGATE_CL_AND_RA_PERTURBATION_ROBUSTNESS_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- accepted Python source needed for R4 HJB/KFE/aggregation.

Verify Python `src/tests` remain unchanged from `7a2388a2ba89073e307f05a909570e8c40a4be13`. If not, stop:

`BLOCKED_CONTROLLED_CL_RA_PERTURBATION_PYTHON_SOURCE_DRIFT`

## MATLAB identity and snapshot gates

Before execution, verify read-only:

- accepted original `HANK_2ASSETS_HJB.m` SHA-256 exactly:
  `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m` SHA-256 exactly:
  `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m` SHA-256 exactly:
  `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- selected cache SHA-256 exactly:
  `FC58289EC695A6B7583405CC7F6A7FC3C88B0512F0C93CEAB76F3442CA9F771A`

Load only the selected cache and select `st.results{10}` / `st.grids{10}`.

Verify:

- `st.results{10}.convergent == 1`;
- observed saved `st.results{10}.rah == 0.040026998056627239` up to exact loaded double identity;
- all direct-call fields required by the accepted HJB are present;
- no upstream data lookup is needed.

## MATLAB frozen tuple and only permitted difference

Construct two independent in-memory copies from the exact same tuple:

```matlab
R0 = st.results{10};
R1 = st.results{10};
```

Before overriding `rah`, prove `isequaln(R0,R1)` and freeze/hash an external snapshot manifest containing:

- `st.param`
- `st.grids{10}`
- `st.num`
- `st.CHI`
- `R0` before override
- source/cache identities

Then set only:

```matlab
R0.rah = 0.040;
R1.rah = 0.041;
```

Prove all fields other than `rah` remain exactly equal after override. A recursive field comparison or equivalent serialized comparison excluding `rah` must report zero differences.

Execute only:

```matlab
out0 = HANK_2ASSETS_HJB(st.param, st.grids{10}, st.num, st.CHI, R0, 0);
out1 = HANK_2ASSETS_HJB(st.param, st.grids{10}, st.num, st.CHI, R1, 0);
```

No outer caller may run.

## Python controlled pair

Use the accepted R4 native household steady-state configuration exactly:

- `a=[0,0.5,1]`
- `b=[0,2.5,5]`
- primary `z=0.5:0.0625:2.0`
- buffer `z=0.5:0.0625:2.25`
- `rho=0.05`
- `gamma_c=1.0`
- `phi=1.0`
- `chi_0=0.05`
- `chi_1=1.0`
- `a_bar=0.5`
- `mu_z=0.2`
- `sigma_z=0.1`
- `r_b=0.03`
- `tau=0`
- wage `1.0`
- migration cost `0.0`
- labor weight `1.0`
- identical initialization, HJB numerics, KKT/generator/KFE tolerances, truncation/buffer protocol, and cell weights.

Baseline:

`r_a=0.040`

Perturbation:

`r_a=0.041`

Construct both through an external harness using accepted production APIs. Do not modify repo source.

Before execution, serialize/hash the two Python input manifests and prove the only economic input difference is `r_a`.

## Execution budget

Authorize exactly four one-shot scientific household runs:

1. MATLAB selected snapshot, `rah=0.040` — once;
2. MATLAB same snapshot, `rah=0.041` — once;
3. Python accepted R4 household configuration, `r_a=0.040` — once;
4. Python same configuration, `r_a=0.041` — once.

No rerun after a scientific run begins.

If an implementation fails on its baseline run, do not execute its perturbation run.

If a pure pre-scientific harness/plumbing defect is found before any scientific run for that implementation, it may be corrected only if model inputs/equations/grids/tolerances are unchanged. Freeze the corrected harness before execution.

## Aggregate definitions

### MATLAB

Use the accepted original HJB outputs:

- `C_hh = out.Ct = sum(out.C,'all')`
- `L_hh = out.Lt = sum(out.l,'all')`
- `A_hh = out.At`
- `B_hh = out.Bt`
- probability normalization `sum(out.g,'all')`

The report must verify equality of scalar aggregate fields to the explicit sums for `C_hh` and `L_hh`.

### Python

Use primary HJB policy and accepted KFE probability mass `g`:

- `C_hh = sum(g * c)`
- scalar embedded `L_hh = sum(g * l)`
- `A_hh`, `B_hh` from accepted KFE aggregation.

Do not use unweighted arithmetic means.

## Required validity diagnostics

For MATLAB report all diagnostics available from the direct accepted HJB output/source without altering it, including at minimum:

- convergence flag;
- probability normalization;
- finiteness/non-negativity of the stationary distribution if exposed;
- any HJB/generator/KFE diagnostics exposed by the accepted source.

If the accepted original source does not expose a diagnostic that the diagnostic-patch source had added, state `NOT_EXPOSED_BY_ACCEPTED_ORIGINAL_SOURCE`; do not instrument production code.

For Python report:

- primary and buffer HJB residual/convergence;
- KKT residual;
- generator row-sum/off-diagonal validity;
- truncation/common-core compatibility;
- endogenous `a` connectivity and recurrent-class/left-nullity checks;
- KFE stationarity residual;
- normalization;
- minimum/negative mass;
- mass-density consistency;
- `A_hh`, `B_hh`.

## Required comparison output

Report exactly this compact table prominently:

| implementation | r_a | C_hh | L_hh |
|---|---:|---:|---:|
| MATLAB | 0.040 | ... | ... |
| Python | 0.040 | ... | ... |
| MATLAB | 0.041 | ... | ... |
| Python | 0.041 | ... | ... |

Also report, for each implementation:

- `Delta C_hh = C_hh(0.041)-C_hh(0.040)`
- `%Delta C_hh = Delta C_hh/C_hh(0.040)*100`
- `Delta L_hh = L_hh(0.041)-L_hh(0.040)`
- `%Delta L_hh = Delta L_hh/L_hh(0.040)*100`
- baseline and perturbed `A_hh`, `B_hh`.

Also report cross-language differences in the **responses**:

- `Delta C_hh_MATLAB - Delta C_hh_Python`
- `Delta L_hh_MATLAB - Delta L_hh_Python`
- response-sign agreement/disagreement.

Do not invent an exact native-level equality tolerance. The MATLAB selected province-year snapshot and Python R4 fixture are not the same native calibration. P1-P4 remain the formal shared-input parity evidence.

## Interpretation

Return exactly one supplementary classification:

- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_SUPPORTS_OWNER_ACCEPTANCE`
- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_NEEDS_OWNER_DISCUSSION`
- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_BLOCKED_SOURCE_OR_ENVIRONMENT`

Use `SUPPORTS_OWNER_ACCEPTANCE` only if:

- all four one-shot runs complete;
- both baseline/perturbed solutions are valid within each implementation's accepted numerical contracts;
- aggregate formulas are correctly applied;
- only `r_a/rah` differs within each pair;
- there is no unexplained response-sign reversal or obviously material qualitative comparative-static inconsistency after accounting for the different native calibration.

Do not issue P5 acceptance in this task.

## Output

Write exactly one report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_EXECUTION_REPORT.md`

The report must contain:

- live/source/cache identities;
- Owner-selected candidate and provenance approval;
- exact input-freeze proof;
- four execution counts;
- aggregate formulas;
- compact four-row `C_hh/L_hh` table;
- delta/percentage table;
- `A_hh/B_hh` table;
- validity diagnostics;
- cross-language response comparison;
- comparability limitations;
- supplementary classification;
- forbidden-operation check;
- recommended next gate.

## Commit/push authorization

Only the report may be added to the repository.

If and only if the report is the sole repository change, commit once and fast-forward push after fresh remote verification.

Suggested commit subject:

`Record controlled household C L r_a robustness`

## Forbidden operations

Do not:

- modify MATLAB or Python production source/tests;
- modify/regenerate the selected cache;
- run any outer MATLAB equilibrium/turn/shock function;
- change any parameter/input other than `r_a/rah` within each implementation pair;
- change grids, productivity process, initialization, equations, FOCs, boundary/KKT contracts, generator/KFE logic, or tolerances;
- rerun P1-P4;
- rerun any consumed scientific household run;
- tune after observing outputs;
- claim exact native-level MATLAB/Python equality from this supplementary experiment;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, or Results work;
- merge, rebase, reset, or force-push.

## Recommended next gate

If the supplementary experiment supports acceptance and independent review agrees:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

Otherwise P5 remains pending for a targeted diagnostic.