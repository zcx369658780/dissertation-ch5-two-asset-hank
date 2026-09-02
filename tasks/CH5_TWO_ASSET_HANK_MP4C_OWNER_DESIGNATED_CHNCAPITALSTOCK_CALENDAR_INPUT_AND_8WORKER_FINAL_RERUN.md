# CH5_TWO_ASSET_HANK_MP4C_OWNER_DESIGNATED_CHNCAPITALSTOCK_CALENDAR_INPUT_AND_8WORKER_FINAL_RERUN

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / data-binding implementer / controlled batch executor

Owner: final scientific authority

## 1. Supersession and resolved Owner designation

This task supersedes the blocked route recorded by execution commit:

`f4a905bf45a51ccc6433cc5954f39ecc59f37823`

with terminal:

`MP4C_OWNER_A_CAPITAL_PROVENANCE_UNRESOLVED__RERUN_NOT_AUTHORIZED`.

The unresolved choice is now scientifically resolved from the Owner's dissertation specification plus the Owner's prior selection of intended calendar semantics.

The dissertation explicitly states that provincial capital stock is estimated using the Zhang-Jun methodology and that provincial total capital stock can be obtained directly using the R package `CHNCapitalStock` developed by Chen Pu et al. It further states that the multi-province model uses provincial GDP, capital stock and population data to construct per-capita output/capital and technology estimates.

Therefore the Owner designates:

`OWNER_DESIGNATES_R语言计算资本存量_AS_INTENDED_2000_2023_31_PROVINCE_HANK_CAPITAL_STOCK_SERIES`

and:

`OWNER_DESIGNATES_CHNCAPITALSTOCK_AS_SCIENTIFIC_CAPITAL_CONSTRUCTION_AUTHORITY`

The workbook sheet named exactly:

`R语言计算资本存量`

is the intended scientific capital-stock series for the corrected annual HANK calibration.

The active legacy MATLAB read of `总资本存量` is retained as historical implementation evidence only. It is not final scientific authority under Owner-A intended calendar semantics.

## 2. Scientific calendar contract

Freeze exactly:

- processed level-data calendar: `2000–2023`, 24 years;
- reported annual steady states: `2009–2023`, 15 years;
- steady-state year `Y` uses rolling PLM window `[Y-9,Y]`;
- rolling-window/cache entry: `Y-2008` => `1–15`;
- R regression vintage: `Y-1999` => `10–24`;
- calendar level row: `Y-1999` => `10–24`;
- level calendar year: `Y`;
- technology/productivity objects come from the matching rolling PLM entry;
- GDP, POP and capital levels correspond to the steady-state calendar year.

The legacy MATLAB `data_year=ii` row `1–15` annual implementation is classified as:

`LEGACY_MATLAB_CALENDAR_BINDING_DEFECT__NOT_FINAL_PAPER_SCIENCE_AUTHORITY`.

## 3. Capital series contract

Use the exact frozen sheet `R语言计算资本存量` from the provenance-qualified processed workbook.

Expected structure to verify before any science:

- years: exactly `2000–2023`;
- rows: 24 annual observations plus header;
- provinces: exactly 31 mainland provinces in the accepted common province order;
- no missing values;
- all capital values finite and strictly positive;
- 2022 and 2023 all 31 provinces finite and strictly positive.

Do not use `总资本存量` for corrected annual HANK Kt0/Kt/GovInv calibration.

Do not mix the two capital series across years or provinces.

Do not use `abs`, clipping, epsilon replacement, manual interpolation, or ad-hoc repair.

### 3.1 Unit and scaling authority

`CHNCapitalStock` documentation defines investment/depreciation inputs in units of 100 million yuan and returns provincial capital stock together with the investment price index. The workbook capital series is to be treated as the frozen `CHNCapitalStock` capital-stock output in its recorded price-base units, economically corresponding to `亿元`-scale provincial capital stock.

Do not invent an additional empirical scaling.

Before scientific execution, prove the exact conversion from workbook capital values to model-internal `Kt0/Kt/GovInv` units using the formally accepted corrected-2009 same-input anchor and the existing model input multipliers/contracts. Prefer the same monetary-unit multiplier used for GDP if and only if the 2009 anchor proves it exactly.

If the exact 2009 scaling cannot be reproduced deterministically, STOP before science with:

`MP4C_CHNCAPITALSTOCK_MODEL_UNIT_SCALING_UNRESOLVED__RERUN_NOT_AUTHORIZED`.

## 4. Required live continuity

At start:

1. fresh-fetch `origin/main`;
2. require this task live on `main` as direct child of `f4a905bf45a51ccc6433cc5954f39ecc59f37823`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read `AGENTS.md`, rule index, all CURRENT rules, corrected-2009 parity acceptance, prior MP4C reports/tasks, MP4D acceptance, current annual adapter/worker/scheduler/tests;
6. read the dissertation passages documenting `CHNCapitalStock` and annual parameter calibration;
7. read-only inspect the processed workbook, `R语言估计结果_plm估计.xlsx`, runtime cache, and existing provenance-qualified data copies.

## 5. Phase A — ZERO-SCIENCE implementation and preflight

Exact scientific execution budget in Phase A:

- MATLAB: `0`;
- R estimation/model rerun: `0`;
- Python stationary: `0`;
- household/HJB/KFE: `0`;
- comparator: `0`;
- shock/IRF: `0`.

### 5.1 Corrected input representation

Create/use an explicit representation label:

`OWNER_A_CHNCAPITALSTOCK_ROLLING_PLM_END_YEAR_CALENDAR_INPUT`

For steady-state year `Y`:

- select `IND_alpha`, `IND_Zt` and other rolling-estimation technology objects from rolling entry `Y-2008`;
- select GDP and population for calendar year `Y` from row `Y-1999`;
- select capital for calendar year `Y` from sheet `R语言计算资本存量`, year `Y`, same province;
- derive `log_pgdp` deterministically from selected GDP/POP;
- derive `log_pcap` deterministically from selected CHNCapitalStock/POP;
- derive inter-province capital ratios from the selected positive capital/per-capita-capital representation according to the already frozen source-semantic formula;
- bind every selected field to source artifact SHA, sheet/field, calendar year, province and conversion/scaling rule.

Do not reuse legacy complex `log_pcap` values after replacing the underlying capital series.

### 5.2 Implementation scope

Allowed minimal changes:

- `validators/multi_province/mp4c_matlab_runtime_cache.py` or a new narrowly scoped Owner-A input adapter;
- annual production/batch manifests only as necessary to expose the new representation and semantic indices;
- focused tests;
- PowerShell launcher only if necessary for the new representation or worker count.

Forbidden scientific mutations:

- HJB/KFE;
- household equations;
- one-turn ordering;
- migration;
- firm/wage/monetary/fiscal blocks;
- controllers;
- calibration parameters;
- grids;
- tolerances;
- convergence thresholds;
- MP4D shock semantics.

### 5.3 Mandatory all-15-year preflight

Materialize corrected inputs for every year 2009–2023 before starting any worker.

For each year prove:

- rolling window `[Y-9,Y]`;
- rolling entry `1–15`;
- R vintage `10–24`;
- calendar level row `10–24`;
- exact calendar year;
- exact 31-province order;
- exact workbook/cache/R-regression identities;
- GDP finite and positive;
- POP finite and positive;
- CHNCapitalStock finite and positive;
- `log_pgdp` finite real;
- `log_pcap` finite real;
- technology parameters finite/admissible;
- exact model-unit scaling contract;
- worker launches = `0` during preflight.

For 2009, require explicit comparison against the formally accepted corrected-2009 same-input parity anchor. The corrected input must reproduce the accepted 2009 relevant input fields within the already accepted representation/tolerance contract. Any material unexplained contradiction stops before batch execution.

Persist a full per-year/per-province audit of the CHNCapitalStock mapping and the prior-vs-corrected capital difference.

## 6. Phase A terminal

If all zero-science checks pass:

`MP4C_OWNER_A_CHNCAPITALSTOCK_CORRECTED_INPUTS_2009_2023_PREFLIGHT_PASS__8WORKER_BATCH_AUTHORIZED__SCIENTIFIC_CALLS_0`

If any identity/scaling/calendar condition fails, stop without science.

## 7. Phase B — exactly 8-worker corrected annual rerun

Upon Phase-A PASS, Codex is authorized to execute the corrected scientific batch directly.

Use exactly:

- years: `2009–2023` inclusive;
- `Workers=8`;
- year-level subprocess parallelism only;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- max outer turns `250`;
- max household calls `7750`;
- automatic reruns `0`;
- no default wall-clock kill.

Do not run MATLAB.
Do not rerun R estimation.
Do not run comparator until the corrected Python batch has completed.
Do not run shocks/AR(1)/IRF/R5/Results.

Use a fresh no-overwrite output root, preferred:

`D:\ProjectTemp\ch5-mp4c-owner-a-chncapitalstock-corrected-8worker-20260902-001`

Never reuse either prior batch root.

If the batch has any infrastructure/memory failure or any scientific year failure:

- preserve all evidence;
- no automatic rerun;
- no worker-count change;
- stop with the appropriate incomplete/failure terminal.

## 8. Required scientific outputs

For every successful year require:

- corrected annual input artifact and identity;
- final steady state;
- 31×20 terminal table;
- Lt_mat;
- final household restart NPZ;
- MATLAB-readable Python checkpoint MAT;
- checkpoint manifest;
- year timing;
- success/failure marker.

Root outputs must include:

- `steady_state_panel_2009_2023.csv`;
- `2009_2023_稳态值.xlsx`;
- `2009_2023_稳态Ltmat.xlsx`;
- batch summary JSON/CSV;
- batch timing;
- artifact hash manifest.

## 9. Phase C — read-only closeout and comparison

After the 8-worker batch completes:

1. audit all 15 years read-only;
2. require 15/15 `SOURCE_CONVERGED` for full PASS;
3. verify 31/31 household convergence per year;
4. verify all 31×20 fields finite;
5. verify checkpoint and root artifact hashes;
6. verify all corrected input identities and semantic indices;
7. compare corrected 2009 against the formally accepted corrected-2009 MATLAB–Python same-input anchor;
8. compare other years only against provenance-qualified MATLAB artifacts whose scientific calendar/data semantics are actually compatible;
9. do not treat legacy `data_year=ii` MATLAB outputs as corrected 2010–2023 parity authority;
10. do not rerun MATLAB.

Do not claim blanket 2010–2023 MATLAB–Python parity unless compatible reference evidence actually exists.

## 10. Historical status

Preserve the old 9-hour batch as:

`LEGACY_CONFLATED_WINDOW_AND_LEVEL_ROW_BATCH__ENGINEERING_CONVERGENCE_ONLY__NOT_FINAL_CALENDAR_YEAR_AUTHORITY`.

The corrected-2009 same-input parity remains valid unless this task produces direct contradictory same-input evidence.

MP4D source-semantics acceptance remains valid, but numerical shock implementation remains blocked until this corrected annual gate closes.

## 11. Evidence package

Use a fresh no-overwrite evidence root, preferred:

`D:\ProjectTemp\ch5-mp4c-owner-a-chncapitalstock-correction-20260902-001`

Persist at minimum:

- `owner_capital_designation_contract.json`;
- `chncapitalstock_axis_and_unit_audit.json`;
- `rolling_plm_calendar_contract.csv`;
- `corrected_2009_anchor_input_check.json`;
- `corrected_2009_2023_input_preflight.json`;
- `capital_series_legacy_vs_chncapitalstock_diff.csv`;
- `zero_science_test_receipt.json`;
- `corrected_8worker_build_receipt.json`;
- `batch_execution_receipt.json` if science executes;
- `closeout_audit.json` if science completes;
- `manifest.json`.

## 12. Git boundary

Do not commit/push large generated data, runtime MAT/NPZ/XLSX/CSV outputs, or local source workbooks.

After final closeout, one bounded commit/push may include only authorized code/tests/contracts and the required repository report.

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_OWNER_A_CHNCAPITALSTOCK_CORRECTED_8WORKER_RERUN_REPORT.md`

## 13. Terminal classifications

Preflight blocked:

`MP4C_OWNER_A_CHNCAPITALSTOCK_CORRECTED_INPUT_PREFLIGHT_BLOCKED__NO_SCIENCE`

Batch incomplete/failure:

`MP4C_OWNER_A_CHNCAPITALSTOCK_CORRECTED_8WORKER_BATCH_INCOMPLETE__NO_AUTOMATIC_RERUN`

Full success:

`MP4C_OWNER_A_CHNCAPITALSTOCK_2009_2023_CORRECTED_8WORKER_ANNUAL_STATIONARY_COVERAGE_PASS`

No numerical shock/IRF implementation is authorized in this task.
