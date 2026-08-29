# CH5_TWO_ASSET_HANK_PRE_P5_PYTHON_BOOLEAN_SERIALIZATION_CORRECTION_AND_CL_RA_COMPLETION

## Task

Complete the Owner-requested pre-P5 controlled household `C_hh/L_hh` and `r_a: 0.040 -> 0.041` robustness experiment by correcting **only** the external Python result-serialization defect, reusing the already persisted MATLAB pair without rerunning MATLAB, and executing one replacement Python pair.

This task explicitly authorizes replacement Python runs because the predecessor Python baseline and perturbation each returned from the scientific `run_one` solve path, but **no Python scientific result was durably persisted** because final JSON serialization failed. Those two consumed runs are not reusable scientific evidence and are not classified as numerical/scientific failures.

This task does **not** authorize P5 acceptance, P1-P4 reruns, MATLAB reruns, production-source/test modification, scientific-input changes, tolerance tuning, outer-equilibrium execution, AR(1), transition, IRF, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Live predecessor evidence

Predecessor completed/blocked report commit:

`b6d3bc4e3f12449c206c19d240a7317a5e841b89`

Predecessor task authority commit:

`4bc7cc00d36aab144a63387b737f1ed40200c034`

Accepted P1-P4 numerical evidence commit:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

P1-P4 remain accepted and must not be rerun.

## Accepted MATLAB evidence — reuse only, no rerun

The predecessor report durably persisted the Owner-approved MATLAB `C2016-P10` pair under the accepted original MATLAB HJB source.

Accept and reuse exactly these raw artifacts, if and only if their identities match:

- MATLAB `rah=0.040` raw object:
  - `matlab_out_0040.mat`
  - bytes `19306`
  - SHA-256 `E723D267ABEFC16A20B4D17D6EC20554561B601FB028405FDA41D30EFAC03D00`
- MATLAB `rah=0.041` raw object:
  - `matlab_out_0041.mat`
  - bytes `19660`
  - SHA-256 `83B877820FEA59A655C98A4669189EEA0D3A17E4CDC1D9B334EBAF6115ED58BC`
- MATLAB summary JSON:
  - bytes `1159`
  - SHA-256 `0083726D2D3911566DE71C6A97C6DF6FD58739019B8530661809EEBA189C1FEF`

Accepted MATLAB numerical values to read back from the persisted artifacts, not from chat:

| `rah` | `C_hh` | `L_hh` | `A_hh` | `B_hh` |
|---:|---:|---:|---:|---:|
| 0.040 | 9.093838085759417 | 0.7208465448372894 | 0.4205741387968296 | 2.162515255782729 |
| 0.041 | 9.088797065167160 | 0.7201767277365387 | 0.5227979944275221 | 2.168714217374641 |

Accepted MATLAB comparative statics:

- `Delta C_hh = -0.00504102059225708`
- `%Delta C_hh = -0.0554333664698860%`
- `Delta L_hh = -0.000669817100750647`
- `%Delta L_hh = -0.0929209005089758%`

MATLAB `convergent=1` for both runs, `Ct == sum(C,'all')`, `Lt == sum(l,'all')`, `sum(g,'all') == 1`, and only machine-scale signed probability roundoff was observed.

**MATLAB must not be executed in this task.** If any required MATLAB artifact identity is missing or differs, stop:

`BLOCKED_PYTHON_SERIALIZATION_COMPLETION_MATLAB_EVIDENCE_IDENTITY_DRIFT`

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_PERSISTENCE_CORRECTION_AND_REEXECUTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- accepted Python R4 HJB/KFE/steady-state source needed by the frozen harness.

Verify live Python `src/tests` remain unchanged from:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

except report/task-only commits.

If scientific source/test drift exists, stop:

`BLOCKED_PYTHON_SERIALIZATION_COMPLETION_SOURCE_DRIFT`

## Predecessor Python scientific harness identity

Locate the predecessor external Python harness from the predecessor artifact root and require:

- `run_python_pair.py`
- bytes `6763`
- SHA-256 `018C1E0A154F32E7D62C9BF7B19F20B3EACE30126D4DF687E40EDC76A2DCBA46`

Require the predecessor serialized input manifest identity:

- bytes `3255`
- SHA-256 `32252AD3899FFE65EC96D31D6A74637A95597502FDCB6BA629C8D0CD2B3F8DA8`

The scientific `run_one` logic, imports used by the scientific solve, R4 fixture reconstruction, HJB/KFE calls, diagnostics, aggregate formulas, scientific inputs, tolerances, grids, initialization, productivity process, buffer protocol, and run ordering are frozen.

## Exact defect to diagnose

The predecessor scientific solves completed in this control flow:

```python
rows = [run_one(0.040)]
rows.append(run_one(0.041))
# only after both returned:
json.dumps(output, indent=2, sort_keys=True, allow_nan=False)
```

Final serialization failed with:

```text
TypeError: Object of type bool is not JSON serializable
```

This task treats the defect as external persistence/serialization plumbing unless preflight proves otherwise.

## Authorized correction scope

Create a new external corrected harness derived from the exact predecessor harness.

The predecessor-to-corrected diff may change **only**:

- recursive conversion/coercion of Python/NumPy boolean scalar values for JSON compatibility;
- if required by the exact observed serializer path, generic NumPy scalar conversion to their native Python scalar via `.item()`;
- JSON serialization/persistence helper code;
- immediate durable persistence of the completed per-rate summary before final combined JSON assembly;
- artifact-root/path plumbing.

The diff must **not** change:

- `run_one` scientific calculations;
- any HJB, policy, generator, connectivity, KFE, aggregation, or diagnostic formula;
- any model input;
- `r_a` values;
- grids or productivity process;
- initialization/buffer protocol;
- numerical tolerances;
- output field definitions or aggregate definitions;
- production source/tests.

If a correction beyond this scope appears necessary, stop:

`BLOCKED_PYTHON_SERIALIZATION_COMPLETION_REQUIRES_SCIENTIFIC_HARNESS_CHANGE`

## Mandatory pure-serialization preflight

Before any replacement scientific run, execute one synthetic serialization preflight only.

It must not call HJB, KFE, generator, policy, fixture solve, or any model routine.

The preflight must construct a synthetic object containing at minimum:

- native Python `bool` values;
- `numpy.bool_` values;
- representative `numpy.float64` and `numpy.int64` scalar diagnostics if those types occur in the real output schema;
- nested dictionaries/lists matching the real output's structural shape;
- all expected output field names.

It must prove:

1. recursive conversion leaves numeric values unchanged apart from scalar type representation;
2. boolean values preserve logical truth values exactly;
3. `json.dumps(..., allow_nan=False)` succeeds;
4. written JSON can be read back;
5. expected field names are unchanged;
6. no scientific function was called.

Record preflight artifact SHA-256/bytes.

Then freeze the corrected harness SHA-256/bytes and prove the complete diff is serialization/persistence-only.

After the first replacement scientific run begins, do not edit the corrected harness.

## Replacement Python pair authority

This task explicitly authorizes exactly two fresh Python scientific executions:

1. replacement baseline `r_a=0.040` — exactly once;
2. replacement perturbation `r_a=0.041` — exactly once.

The two predecessor unpersisted runs are superseded as non-evidence because no durable output exists.

Use the accepted R4 household configuration exactly, including:

- `a=[0,0.5,1]`
- `b=[0,2.5,5]`
- primary `z=0.5:0.0625:2.0`
- upper buffer `z=0.5:0.0625:2.25`
- `rho=0.05`
- `gamma_c=1`
- `phi=1`
- `chi_0=0.05`
- `chi_1=1`
- `a_bar=0.5`
- `mu_z=0.2`
- `sigma_z=0.1`
- `r_b=0.03`
- `tau=0`
- wage `1`
- migration cost `0`
- labor weight `1`
- accepted R4 HJB/KKT/generator/KFE numerics and tolerances.

The only input difference between the pair is:

`r_a: 0.040 -> 0.041`.

Before execution prove the two serialized input manifests differ only in `r_a`.

## Persistence order

For each replacement Python run, persist its completed summary **immediately after `run_one` returns and before starting the next scientific run**, using the corrected preflight-proven serialization path.

Required order:

```text
run_one(0.040)
-> persist baseline summary durably
-> verify file exists/read-back/hash
-> only then run_one(0.041)
-> persist perturbation summary durably
-> verify file exists/read-back/hash
-> only then build/write combined comparison JSON
```

This avoids losing both scientific outputs to one final serialization failure.

If baseline solve returns but baseline persistence fails, stop and do not run 0.041.

If baseline persists and 0.041 solve/persistence fails, retain baseline as partial evidence but do not rerun either rate in the same task.

## Required Python scientific outputs

For each rate report and persist at minimum:

- `C_hh = sum(g*c)`
- `L_hh = sum(g*l)`
- `A_hh`
- `B_hh`
- primary and buffer HJB convergence/residuals;
- KKT residual;
- generator max row sum / minimum off-diagonal;
- common-core truncation policy/value diagnostics used by accepted R4;
- recurrent-class count/size, interior-`a` support, left-nullity/connectivity evidence;
- KFE stationarity residual;
- normalization error;
- minimum mass / negative count;
- mass-density consistency.

Use existing accepted diagnostic definitions only. Do not add or tune scientific thresholds.

## Required final comparison

If both Python replacement summaries are durably persisted, combine them with the reused MATLAB evidence and report:

| implementation | `r_a/rah` | `C_hh` | `L_hh` | `A_hh` | `B_hh` |
|---|---:|---:|---:|---:|---:|
| MATLAB | 0.040 | reused | reused | reused | reused |
| Python | 0.040 | ... | ... | ... | ... |
| MATLAB | 0.041 | reused | reused | reused | reused |
| Python | 0.041 | ... | ... | ... | ... |

For each implementation compute:

- `Delta C_hh`
- `%Delta C_hh`
- `Delta L_hh`
- `%Delta L_hh`
- optionally `Delta A_hh`, `Delta B_hh` as supplementary diagnostics.

Then report cross-language comparative-static comparison:

- sign agreement/disagreement for `Delta C_hh`;
- sign agreement/disagreement for `Delta L_hh`;
- ratio or relative magnitude of percentage responses when finite;
- any material unexplained qualitative discrepancy.

Do **not** require equality of native MATLAB/Python levels because their native grids/productivity/calibration differ. Formal exact/adapter parity remains the accepted P1-P4 evidence.

## Supplementary classification

Return exactly one:

- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_COMPLETE_SUPPORTS_OWNER_ACCEPTANCE`
- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_COMPLETE_NEEDS_OWNER_DISCUSSION`
- `PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_BLOCKED_SOURCE_OR_ENVIRONMENT`

Use `SUPPORTS_OWNER_ACCEPTANCE` only if:

- both replacement Python runs complete and persist;
- all accepted Python scientific validity diagnostics pass;
- MATLAB evidence identities match and is reused without rerun;
- both implementations have valid `C_hh/L_hh` levels and within-language responses;
- no unexplained qualitative/sign inconsistency appears that materially undermines the supplementary robustness interpretation.

Do not convert this supplementary classification into P5 acceptance.

## Output file

Write exactly one repository report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_PYTHON_BOOLEAN_SERIALIZATION_CORRECTION_AND_CL_RA_COMPLETION_REPORT.md`

The report must contain:

- live/source identities;
- MATLAB reused artifact hashes and read-back values;
- predecessor Python harness/input-manifest hashes;
- exact full harness diff;
- synthetic serialization preflight evidence;
- corrected harness identity;
- exact execution counts;
- per-rate Python output artifact hashes;
- Python scientific validity diagnostics;
- four-row MATLAB/Python aggregate table;
- within-language delta/percentage tables;
- cross-language response interpretation;
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

`Complete Python C L r_a robustness after serialization correction`

## Forbidden operations

Do not:

- execute MATLAB;
- rerun P1-P4;
- modify MATLAB/Python production source/tests;
- change Python scientific `run_one` calculations;
- change any input except the already frozen `r_a` pair;
- change grids, productivity, initialization, equations, FOCs, policy logic, boundary/KKT, generator/KFE logic, aggregate formulas, or tolerances;
- tune after observing outputs;
- rerun either replacement Python rate after its one authorized invocation;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, dynamics, or Results work;
- merge, rebase, reset, or force-push.

## Recommended next gate

If the supplementary classification is `...SUPPORTS_OWNER_ACCEPTANCE` and independent review accepts the evidence:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

If it is `...NEEDS_OWNER_DISCUSSION`, P5 remains pending until the discrepancy is resolved or explicitly accepted by the Owner.
