# CH5_TWO_ASSET_HANK_MP4C_OWNER_A_2009_2022_CORRECTED_ANNUAL_STATIONARY_8WORKER_EXECUTION_AND_ACCEPTANCE

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / corrected-input implementer / controlled batch executor

Owner: final scientific authority

## 1. Authority basis and Owner scope decision

Immediate predecessor execution:

`89d68ce5a21e298dcdc8dd0d4003d552da85a9a9`

The predecessor established:

- latest recovered `D:\Rprogramme\main.r` SHA-256 `18ab62c26ad6bcb201f2bdc38611b920bcef99b6b4c0d6f0f681b3dec4dd72c0`;
- latest R source confirms aggregate `ind=4`, `GDP_multiplier=1000`, `POP_multiplier=100`, aggregate CAP read from `R语言计算资本存量` and multiplied by `1000`, and rolling PLM `itime=10:24` with 10-row windows;
- `R语言计算资本存量` rows 2000–2022 for all 31 provinces are independently reproduced by R 4.6.1 + `CHNCapitalStock 0.1.1` + `CompK_ZJ(prv,bt=2000)` up to ordinary Excel floating serialization error;
- 2023 capital lineage remains unresolved;
- current local PLM dependencies are incomplete, so no PLM reproducibility run was performed;
- no HANK/MATLAB/Python stationary/comparator/shock execution occurred.

The Owner now explicitly narrows the scientific production scope:

`OWNER_SELECTS_2009_2022_AS_CURRENT_ACCEPTED_ANNUAL_STEADY_STATE_SAMPLE__2023_DEFERRED_TO_FUTURE_DATA_EXTENSION`

This task therefore authorizes corrected annual steady-state production for **2009–2022 only**, exactly 14 years.

2023 is explicitly out of scope and must not block this task.

## 2. Scientific intent of this gate

The purpose is to establish the strongest currently supportable Python annual stationary authority for 2009–2022 under the intended calendar semantics and already accepted MATLAB-faithful numerical implementation.

This task does **not** claim that every 2010–2022 annual output has already been independently compared value-for-value against a scientifically compatible MATLAB output. The target acceptance is instead:

- intended annual calendar/data binding is explicit and audited;
- capital series 2000–2022 is independently source-reproduced;
- stored R/PLM outputs are used as frozen empirical calibration artifacts for vintages 10–23;
- corrected-2009 same-input MATLAB–Python parity remains the numerical cross-language anchor;
- all 14 Python annual steady states satisfy the accepted scientific solver/convergence/checkpoint contracts;
- the complete 14-year production route is reproducible and internally consistent.

Do not use the phrase “absolute correctness” as a mathematical guarantee. Use evidence-bounded acceptance language.

## 3. Frozen scientific sample and calendar contract

Exactly:

- annual steady-state years: `2009–2022` inclusive;
- year count: `14`;
- underlying level-data years required by this task: through `2022` only;
- rolling PLM windows:
  - 2009 -> 2000–2009;
  - 2010 -> 2001–2010;
  - ...;
  - 2022 -> 2013–2022;
- rolling-window/cache entry index: `Y-2008` => `1–14`;
- R/PLM vintage key: `Y-1999` => `10–23`;
- calendar level row index: `Y-1999` => `10–23`;
- level calendar year: `Y`.

The historical MATLAB annual implementation `data_year=ii` remains classified:

`LEGACY_MATLAB_CALENDAR_BINDING_DEFECT__NOT_FINAL_PAPER_SCIENCE_AUTHORITY`.

The prior 15-year Python batch remains:

`LEGACY_CONFLATED_WINDOW_AND_LEVEL_ROW_BATCH__ENGINEERING_CONVERGENCE_ONLY__NOT_FINAL_CALENDAR_YEAR_AUTHORITY`.

## 4. Empirical input authority for 2009–2022

### 4.1 Capital

Accepted partial marker from predecessor:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2022_REPRODUCIBILITY_VERIFIED__2023_EXTENSION_PENDING`.

For this 2009–2022 task, promote only the verified 2000–2022 segment to the bounded authority:

`OWNER_A_CHNCAPITALSTOCK_2000_2022_VERIFIED_SEGMENT__AUTHORIZED_FOR_2009_2022_STEADY_STATE_INPUT`

Use exact sheet:

`R语言计算资本存量`

from the provenance-qualified `2000年后各省数据_填充NA.xlsx`.

Do not use any stored or inferred 2023 capital.

Do not use `总资本存量` as corrected Owner-A CAP authority.

### 4.2 GDP / population

Use calendar-year GDP and employment/population level data corresponding to steady-state year `Y`, restricted to 2009–2022.

Use the latest R source scaling semantics:

- GDP: workbook level × `1000`;
- CAP: verified `R语言计算资本存量` level × `1000`;
- POP/employment: workbook level × `100`.

Prove actual workbook sheets, axes, values and hashes before science.

### 4.3 PLM / technology objects

The latest R program confirms the intended aggregate rolling semantics but the local environment did not reproduce PLM due missing dependencies.

For this bounded 2009–2022 stationary gate, the Owner authorizes the existing provenance-qualified stored R regression workbook / processed runtime technology outputs for vintages `10–23` as **frozen empirical calibration artifacts**, without claiming independent PLM estimator reproducibility.

Use marker:

`OWNER_ACCEPTS_STORED_R_PLM_VINTAGES_10_23_AS_FROZEN_EMPIRICAL_CALIBRATION_ARTIFACTS__ESTIMATOR_REPRODUCIBILITY_DEFERRED`

This is allowed because the immediate scientific target is Python HANK stationary-route validation, not re-estimation of the empirical PLM model.

Do not silently extend this acceptance to vintage 24 / 2023.

Do not rerun or substitute PLM in this task.

## 5. Required live continuity

At start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as direct child of `89d68ce5a21e298dcdc8dd0d4003d552da85a9a9`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md` and all CURRENT rules;
   - latest predecessor report `docs/CH5_TWO_ASSET_HANK_MP4C_LATEST_R_PLM_2023_CAPITAL_LINEAGE_AND_CORRECTED_8WORKER_RERUN_REPORT.md`;
   - CHNCapitalStock reproduction report;
   - corrected-2009 same-input MATLAB–Python parity acceptance/report;
   - prior MP4C annual batch report;
   - MP4D L3 acceptance;
   - current `annual.py`;
   - current runtime-cache adapter;
   - current empirical annual builder;
   - current production worker;
   - current full annual scheduler and PowerShell launcher;
   - relevant focused tests.

## 6. Phase A — zero-HANK corrected-input implementation and audit

Before any HANK worker launch:

- MATLAB HANK calls: `0`;
- Python stationary calls: `0`;
- household/HJB/KFE calls: `0`;
- comparator calls: `0`;
- shock/IRF/R5/Results calls: `0`;
- R PLM calls: `0`.

### 6.1 Build an explicit Owner-A 2009–2022 input representation

Use an explicit representation label, e.g.:

`OWNER_A_2009_2022_VERIFIED_CHNCAPITALSTOCK_ROLLING_PLM_END_YEAR_CALENDAR_INPUT`

For each year `Y=2009..2022`:

- rolling technology entry = `Y-2008` (`1..14`);
- PLM vintage = `Y-1999` (`10..23`);
- GDP calendar row = `Y-1999` (`10..23`);
- POP calendar row = `Y-1999` (`10..23`);
- CAP = verified `R语言计算资本存量` for year `Y`;
- GDP model units = source GDP × `1000`;
- CAP model units = verified capital × `1000`;
- POP/employment model units = source employment/population × `100`;
- recompute `log_pgdp` from selected corrected GDP/POP;
- recompute `log_pcap` from selected corrected CAP/POP;
- recompute source-semantic inter-province capital ratio from corrected intended capital/per-capita-capital representation;
- preserve technology `IND_alpha`, `IND_Zt` from the matching rolling-entry frozen empirical artifact;
- bind every field to source path/hash/sheet/year/province/scaling/index.

Do not reuse legacy invalid `log_pcap` if it came from another capital definition.

### 6.2 Explicit semantic index separation

Code/manifests must expose separate names:

- `steady_state_calendar_year`;
- `rolling_window_entry_index`;
- `regression_vintage_index`;
- `calendar_level_row_index`.

Do not use one ambiguous `data_mat_index` for multiple meanings in the corrected production representation.

### 6.3 Allowed implementation scope

Allowed minimal engineering changes:

- add a narrow Owner-A 2009–2022 empirical/runtime input adapter;
- minimally extend current runtime/cache adapter if necessary without altering historical behavior;
- minimally extend production manifests to support the new representation;
- minimally extend scheduler/launcher to support an explicit end year `2022` or explicit year list while keeping previous 2009–2023 default behavior backward-compatible;
- focused tests.

Preferred scheduler behavior:

- support exact explicit years `2009–2022`;
- do not hard-code 14 years in a way that breaks prior 15-year diagnostics;
- root output names for this task must clearly say `2009_2022`.

Forbidden mutations:

- HJB/KFE implementation;
- household equations;
- one-turn ordering;
- migration;
- firm/wage/monetary/fiscal blocks;
- controllers;
- calibration parameters;
- grids;
- numerical tolerances;
- convergence criteria;
- MP4D shock semantics.

## 7. Mandatory 14-year zero-HANK preflight

Materialize all corrected annual inputs for 2009–2022 before worker launch.

For every year require:

- exact year set only `2009..2022`;
- rolling window `[Y-9,Y]`;
- rolling entry `1..14`;
- PLM vintage `10..23`;
- calendar level row `10..23`;
- exact 31-province order;
- source workbook/cache identities exact;
- verified CAP segment identity exact;
- GDP finite and strictly positive;
- POP/employment finite and strictly positive;
- CAP finite and strictly positive;
- `log_pgdp` finite real;
- `log_pcap` finite real;
- technology parameters finite/admissible;
- exact scaling `GDP×1000`, `CAP×1000`, `POP×100`;
- no 2023 data read required for any scientific input;
- HANK scientific calls `0`.

### 7.1 Static PLM artifact consistency audit

Without rerunning R, verify for vintages `10..23`:

- required aggregate coefficient/intercept sheets exist in the stored R regression workbook;
- values required by the runtime/cache technology construction are finite;
- province ordering maps exactly;
- runtime/cache entry `1..14` technology objects can be traced to corresponding stored vintage `10..23` or to an already source-frozen transformation from those artifacts;
- no vintage 24 / 2023 object is consumed by 2009–2022 inputs.

If a required 2009–2022 PLM artifact is missing or mapping is internally contradictory, STOP before HANK.

Do **not** stop merely because independent PLM estimator reproduction has been deferred.

### 7.2 Corrected-2009 numerical anchor

The corrected 2009 input must be compared against the formally accepted corrected-2009 same-input contract.

Require no unexplained material contradiction in relevant:

- GDP/POP/CAP levels/scaling;
- technology objects;
- province order;
- other frozen annual empirical inputs.

A material contradiction stops before the 14-year batch.

## 8. Phase-A terminal

If all 14 corrected inputs and the corrected-2009 anchor pass:

`MP4C_OWNER_A_2009_2022_CORRECTED_INPUT_PREFLIGHT_PASS__8WORKER_BATCH_AUTHORIZED__SCIENTIFIC_CALLS_0`

If blocked:

`MP4C_OWNER_A_2009_2022_CORRECTED_INPUT_PREFLIGHT_BLOCKED__NO_SCIENCE`

Do not involve 2023 in the blocker classification.

## 9. Phase B — exactly 8-worker 2009–2022 annual stationary execution

Upon Phase-A PASS, Codex is authorized to execute the scientific batch directly.

Use exactly:

- years: `2009–2022` inclusive;
- year count: `14`;
- `Workers=8` exactly;
- year-level subprocess parallelism only;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- max outer turns `250`;
- max household calls `7750`;
- automatic reruns `0`;
- no default wall-clock kill.

Do not run:

- MATLAB;
- R PLM;
- 2023 annual steady state;
- comparator until the Python batch is complete;
- shocks/AR(1)/IRF/R5/Results.

Use a fresh no-overwrite output root, preferred:

`D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001`

Never reuse prior 15-year batch roots.

If any infrastructure/memory/scientific-year failure occurs:

- preserve all evidence;
- no automatic rerun;
- no worker-count change;
- STOP.

## 10. Required annual outputs

For each of 14 years require:

- corrected runtime input artifact + SHA;
- final steady state;
- final 31×20 terminal table;
- `Lt_mat`;
- final household restart NPZ;
- MATLAB-readable Python checkpoint MAT;
- checkpoint manifest;
- year timing;
- `SUCCESS.json` / failure marker;
- runtime input identity and corrected semantic indices.

## 11. Required root outputs

Use 2009–2022-specific names:

- `steady_state_panel_2009_2022.csv`;
- `2009_2022_稳态值.xlsx`;
- `2009_2022_稳态Ltmat.xlsx`;
- `batch_summary.json`;
- `batch_summary.csv`;
- `batch_timing.json`;
- `artifact_hash_manifest.json`;
- persistence/representation contract copy.

Do not generate blank 2023 columns/sheets in 2009–2022 root outputs.

## 12. Phase C — read-only scientific closeout

After execution, do not rerun any worker.

Require for full PASS:

- exactly 14/14 expected years present;
- all 14 statuses `SOURCE_CONVERGED`;
- each year 31/31 household calls/outputs satisfy accepted convergence contract;
- final 31×20 fields finite;
- no unexpected 2023 scientific output;
- corrected runtime input SHA/representation exact;
- semantic index identities exact for every year;
- checkpoint hashes and schemas valid;
- root output hashes valid;
- `Lt_mat` shape/order valid;
- no automatic rerun occurred.

### 12.1 Cross-language evidence boundary

Re-run no MATLAB.

Use corrected-2009 same-input parity as the mandatory cross-language numerical anchor.

For 2010–2022, compare only against any already existing MATLAB artifact that can be proven to share the same intended-calendar/data semantics. If no compatible artifact exists, do not claim annual MATLAB–Python value parity for that year.

Do not use legacy `data_year=ii` annual outputs as corrected calendar-year oracles.

## 13. Acceptance classification

If full Phase C passes, terminal:

`MP4C_OWNER_A_2009_2022_CORRECTED_8WORKER_ANNUAL_STATIONARY_COVERAGE_PASS`

Acceptance level to recommend:

`OWNER_A_2009_2022_CORRECTED_ANNUAL_STATIONARY_PYTHON_AUTHORITY_ACCEPTED__2009_CROSS_LANGUAGE_PARITY_RETAINED__PLM_ESTIMATOR_REPRODUCIBILITY_AND_2023_DATA_EXTENSION_DEFERRED__SHOCK_NUMERICS_NOT_YET_ACCEPTED`

This acceptance means the 2009–2022 Python annual stationary production route is accepted under the frozen intended scientific inputs and numerical solver contracts.

It does not mean:

- PLM estimator environment has been independently reproduced;
- 2010–2022 MATLAB parity is proven where no compatible reference exists;
- 2023 is accepted;
- MP4D numerical shock/IRF is accepted.

## 14. 2023 deferral contract

2023 is explicitly deferred under:

`CH5_2023_EMPIRICAL_DATA_EXTENSION_DEFERRED__DO_NOT_BLOCK_2009_2022_STEADY_STATE_AUTHORITY`

Future 2023 work must be a separate bounded task that:

- supplies provenance-qualified 2023 GDP/POP/CAP/deflator/PLM inputs as needed;
- verifies vintage 24;
- adds/runs 2023 without modifying accepted 2009–2022 science;
- preferentially reuses accepted 2009–2022 code/checkpoints rather than rerunning 14 accepted years unless a scientific reason exists.

## 15. Evidence package

Use a fresh no-overwrite evidence root, preferred:

`D:\ProjectTemp\ch5-mp4c-owner-a-2009-2022-corrected-8worker-evidence-20260902-001`

Persist at minimum:

- `owner_a_2009_2022_scope_contract.json`;
- `verified_capital_2000_2022_contract.json`;
- `stored_plm_vintages_10_23_static_audit.json`;
- `corrected_2009_anchor_input_check.json`;
- `corrected_2009_2022_input_preflight.json`;
- `corrected_runtime_input_hashes_2009_2022.json`;
- `zero_science_preflight_ledger.json`;
- `corrected_8worker_build_receipt.json`;
- `batch_execution_receipt.json`;
- `batch_closeout_audit.json`;
- `matlab_compatible_reference_map_2009_2022.json`;
- `manifest.json`.

## 16. Tests

At minimum add/run zero-science focused tests for:

- exact year set `2009..2022`;
- 14-year scheduler behavior;
- no 2023 leakage;
- window entries `1..14`;
- PLM vintages `10..23`;
- calendar rows `10..23`;
- exact province order;
- verified capital source mapping;
- scaling 1000/1000/100;
- recomputed finite logs;
- corrected 2009 anchor input check;
- backward compatibility of existing 2009–2023 diagnostic/default runner where touched;
- `Workers=8` accepted;
- BLAS/thread env pinned to 1;
- no protected source/workbook mutation.

Run `py_compile` on changed/new Python files.

## 17. Git boundary and report

Do not commit/push generated runtime data, MAT/NPZ/XLSX/CSV production outputs, local source workbooks, or R libraries.

After closeout, one bounded commit/push may contain only authorized code/tests/contracts and the report:

`docs/CH5_TWO_ASSET_HANK_MP4C_OWNER_A_2009_2022_CORRECTED_8WORKER_ANNUAL_STATIONARY_REPORT.md`

If execution fails, commit/push the failure report and bounded code/tests only if the task requires preserving the exact failure state; never auto-rerun.

## 18. Stop conditions

Stop immediately if:

- live authority continuity fails;
- a required 2009–2022 empirical artifact is missing/contradictory;
- corrected 2009 input contradicts the accepted anchor materially;
- source/province/scaling identity cannot be proven;
- any unexpected science mutation would be required;
- any annual scientific year fails under the frozen solver contract;
- infrastructure/memory failure occurs.

Do not turn any of these into calibration/grid/tolerance changes.

No numerical shock/IRF implementation is authorized in this task.
