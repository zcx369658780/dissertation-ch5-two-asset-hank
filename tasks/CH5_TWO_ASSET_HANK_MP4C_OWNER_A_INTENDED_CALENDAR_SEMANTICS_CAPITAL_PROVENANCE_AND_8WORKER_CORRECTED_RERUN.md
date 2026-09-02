# CH5_TWO_ASSET_HANK_MP4C_OWNER_A_INTENDED_CALENDAR_SEMANTICS_CAPITAL_PROVENANCE_AND_8WORKER_CORRECTED_RERUN

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / data-provenance auditor / controlled batch executor

Owner: final scientific authority

## 1. Supersession and Owner decision

This task supersedes the unresolved execution route in:

`tasks/CH5_TWO_ASSET_HANK_MP4C_ROLLING_PLM_WINDOW_AND_CALENDAR_LEVEL_ROW_BINDING_CORRECTION_AND_OWNER_RERUN_PREPARATION.md`

Predecessor authority:

`5ccdd555f2e1cb8e4b12c9da1f004261084be381`

That predecessor correctly stopped fail-closed with:

`MP4C_ROLLING_WINDOW_CALENDAR_ROW_OWNER_DESIGNATION_CONTRADICTED_BY_PROTECTED_SOURCE__STOP`

because the protected legacy MATLAB source uses `ii=1..15` both as the annual steady-state counter and as the row index into 24-row level arrays.

The Owner has now made the required scientific decision and explicitly chooses **Option A**:

`OWNER_SELECTS_INTENDED_ROLLING_WINDOW_END_YEAR_CALENDAR_SEMANTICS__LEGACY_MATLAB_DATA_YEAR_EQUALS_II_IS_A_CALENDAR_BINDING_DEFECT`

The intended scientific annual contract is therefore frozen as follows:

- processed annual level data span calendar years `2000–2023`;
- annual steady states are reported for `2009–2023`;
- steady-state year `Y` uses the 10-year rolling PLM window `[Y-9, Y]` for technology/productivity estimation;
- the R PLM vintage therefore runs from `10` through `24`;
- GDP/CAP/POP and other year-specific level objects must correspond to the **window end year `Y`**, not to legacy `ii` rows `1–15`;
- the protected legacy MATLAB annual loop `data_year=ii` is retained as historical implementation evidence but is **not final paper-science authority for calendar-year annual results**.

This Owner decision is a scientific authority change. Do not reject it merely because legacy MATLAB source differs.

## 2. What remains protected and unchanged

The Owner decision changes only annual calendar/data-binding semantics.

It does **not** authorize changes to:

- household equations;
- HJB/KFE numerical implementation;
- transfer FOC;
- adjustment-cost technology;
- grids;
- calibration;
- one-turn order;
- migration logic;
- firm block;
- wage block;
- monetary/fiscal blocks;
- controller semantics;
- convergence thresholds;
- MP4D frozen shock-response semantics.

The separately accepted corrected-2009 MATLAB–Python same-input parity remains the primary numerical regression anchor.

The accepted MP4D classification remains:

`SEQUENTIAL_STATIONARY_COMPARATIVE_STATICS_RESPONSE_PATH_CONFIRMED`

No numerical shock work is authorized by this task.

## 3. Critical remaining blocker: capital-stock provenance

Do **not** immediately change row indices and launch the batch.

When the prior zero-science candidate used calendar level rows `10–24`, 2022/2023 encountered inadmissible/complex `log_pcap` associated with negative capital in the current processed `总资本存量` representation.

The Owner-provided workbook also contains a distinct sheet/series labeled `R语言计算资本存量`, whose later-year values appear positive. That observation is evidence to audit, not automatic authority to substitute it.

Before any scientific rerun, determine exactly which capital-stock construction is the Owner-intended scientific series for annual steady states under Option A.

## 4. Required live continuity

At start:

1. fresh-fetch `origin/main`;
2. require this task live on `main` as direct child of `5ccdd555f2e1cb8e4b12c9da1f004261084be381`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, all CURRENT rules, prior MP4C/MP4D acceptance reports, the predecessor task, current production adapter/worker/scheduler/tests, and the corrected-2009 parity authority.

## 5. Phase A1 — ZERO-SCIENCE intended-calendar contract freeze

Exact scientific calls allowed in Phase A1:

- MATLAB process/model calls: `0`;
- R estimation reruns: `0`;
- Python stationary: `0`;
- household/HJB/KFE: `0`;
- comparator: `0`;
- shock/IRF: `0`.

Build and persist the exact 15-year intended-calendar contract:

| steady year | PLM window | window entry | R vintage | level row | level calendar year |
|---:|---|---:|---:|---:|---:|
| 2009 | 2000–2009 | 1 | 10 | 10 | 2009 |
| 2010 | 2001–2010 | 2 | 11 | 11 | 2010 |
| ... | ... | ... | ... | ... | ... |
| 2023 | 2014–2023 | 15 | 24 | 24 | 2023 |

Required semantic names in code/manifests:

- `rolling_window_entry_index`
- `regression_vintage_index`
- `calendar_level_row_index`
- `steady_state_calendar_year`

Do not reuse one ambiguous `data_mat_index` to mean multiple concepts.

## 6. Phase A2 — ZERO-SCIENCE capital-stock provenance audit

Read-only inspect all relevant local protected/provenance artifacts and processing code, including at minimum:

- `load_GDPdata.m` and helpers;
- R scripts or other code that generated capital-stock series, if present;
- the processed/fill-NA workbook containing `总资本存量`;
- the workbook sheet/series `R语言计算资本存量`;
- fixed-asset-investment source series used by any perpetual-inventory construction;
- `R语言估计结果_plm估计.xlsx`;
- `数据估计结果_1000_100_0.mat`;
- any intermediate MAT/XLSX artifacts that document capital construction;
- dissertation/model documentation explaining capital-stock construction, if locally available.

Answer from evidence:

1. What exact algorithm/source produced `总资本存量`?
2. What exact algorithm/source produced `R语言计算资本存量`?
3. Are they alternative constructions, intermediate/final versions, scaled versions, or one derived from the other?
4. Which one was scientifically intended to initialize `Kt0/Kt/GovInv` for annual HANK steady states?
5. Why do 2022/2023 negative values arise in one representation?
6. Is the positive series reproducible from source inputs and a deterministic documented algorithm?
7. Are units/scaling/province order/year order consistent with GDP/POP and prior corrected-2009 evidence?

Forbidden:

- `abs(CAP)`;
- clipping to epsilon/zero;
- manual replacement;
- undocumented interpolation;
- arbitrary selection of the positive-looking series;
- silently mixing two capital definitions by year/province.

## 7. Capital provenance classification

Choose exactly one strongest classification:

### A1 — intended capital series proven

`MP4C_OWNER_A_INTENDED_CALENDAR_CAPITAL_SERIES_PROVEN__CORRECTED_2009_2023_RERUN_AUTHORIZED`

Use only if one unique, source-backed, scientifically interpretable capital series is proven for all 2009–2023 and all 31 provinces, with finite positive/admissible values and exact units/scaling.

### A2 — deterministic reconstruction proven

`MP4C_OWNER_A_INTENDED_CALENDAR_CAPITAL_RECONSTRUCTION_PROVEN__CORRECTED_2009_2023_RERUN_AUTHORIZED`

Use only if the intended capital stock must be deterministically reconstructed from frozen source data/code and the algorithm is explicitly documented and reproducible without new estimation design.

### BLOCKED

`MP4C_OWNER_A_CAPITAL_PROVENANCE_UNRESOLVED__RERUN_NOT_AUTHORIZED`

Use if the positive-vs-negative capital-series choice remains scientifically ambiguous.

Only A1 or A2 permits Phase A3 and Phase B.

## 8. Phase A3 — corrected input implementation and all-15-year preflight

If A1/A2 is proven, implement the smallest explicit correction.

Preferred architecture:

- preserve rolling PLM technology from the correct cache/window entry `1–15`;
- select year-specific GDP/POP and other level variables from calendar rows `10–24`;
- bind the proven intended capital series for calendar years 2009–2023;
- recompute/validate `log_pcap` from the exact selected CAP/POP if that is the scientifically intended construction; do not import legacy complex log values merely because they exist in the legacy cache;
- preserve source artifact hashes and exact provenance for every field;
- preserve 31-province order;
- expose both rolling-window and calendar-level indices in every runtime manifest.

Do not mutate HJB/KFE/one-turn scientific modules.

Before any model run, materialize all 15 corrected runtime inputs with scientific calls `0` and require for every year:

- correct `[Y-9,Y]` PLM window;
- correct R vintage `10–24`;
- correct calendar level row/year `10–24 / 2009–2023`;
- 31/31 province order exact;
- GDP > 0, POP > 0, intended CAP > 0;
- all required logs finite real;
- technology fields finite/admissible;
- exact source/provenance hashes;
- no worker launch.

For 2009, corrected input must be compared to the separately accepted corrected-2009 same-input authority. A material unexplained contradiction blocks the rerun.

## 9. Prior annual batch classification

The earlier 15-year batch remains immutable historical evidence and is classified:

`LEGACY_CONFLATED_WINDOW_AND_LEVEL_ROW_BATCH__ENGINEERING_CONVERGENCE_ONLY__NOT_FINAL_CALENDAR_YEAR_AUTHORITY`

Do not delete or overwrite it.

The earlier formal annual acceptance remains suspended as final Results authority.

## 10. Phase B — Owner-authorized corrected 8-worker scientific rerun

The Owner explicitly authorizes a corrected full 2009–2023 rerun with:

`Workers = 8`

This task permits Codex to execute the scientific batch **only after Phase A1–A3 pass and A1/A2 classification is established**.

Execution architecture:

- exactly 15 calendar years: 2009–2023;
- year-level parallelism only;
- `Workers=8` exactly for the first attempt;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- max outer turns `250` per year;
- max household calls `7750` per year;
- automatic reruns `0`;
- no default wall-clock kill;
- no MATLAB run;
- no R rerun;
- no shock/IRF run.

If infrastructure/memory failure occurs, STOP and preserve evidence. Do not automatically change worker count or retry. A lower worker count can be separately authorized if needed.

Use a fresh no-overwrite output root, preferred:

`D:\ProjectTemp\ch5-mp4c-owner-a-corrected-calendar-8worker-20260902-001`

Do not reuse any prior batch root.

## 11. Required scientific outputs

Retain the current production output contract:

- 15 annual runtime-input manifests;
- per-year final steady state;
- per-year complete 31×20 terminal field table;
- per-year `Lt_mat`;
- per-year final household restart NPZ;
- per-year Python MATLAB-readable checkpoint MAT;
- checkpoint manifests;
- success/failure markers;
- timing files;
- root `steady_state_panel_2009_2023.csv`;
- corrected `2009_2023_稳态值.xlsx`;
- corrected `2009_2023_稳态Ltmat.xlsx`;
- aggregate/hash/timing manifests.

The corrected batch must record the intended-calendar representation under a new explicit label, e.g.:

`OWNER_A_INTENDED_ROLLING_PLM_END_YEAR_CALENDAR_INPUT`

Do not continue labeling it simply as the legacy MATLAB runtime cache if level-row/capital semantics intentionally depart from the legacy annual loop.

## 12. Existing MATLAB outputs and comparator boundary

Do not rerun MATLAB.

Historical MATLAB annual outputs produced by legacy `data_year=ii` are **not** valid full-calendar 2009–2023 comparator authority after Owner Option A.

They may be used only to document the legacy defect.

For numerical regression:

- retain the separately accepted corrected-2009 MATLAB–Python same-input parity as the primary cross-language anchor;
- use any additional diagnostic-patch artifact only if its exact calendar/input provenance is independently proven compatible with Owner A;
- never claim 2010–2023 MATLAB–Python parity from legacy annual outputs that used rows 1–15.

## 13. Phase C — read-only closeout after corrected rerun

After the 8-worker batch finishes:

1. audit all 15 year statuses;
2. require 15/15 or report exact failures without rerun;
3. verify each corrected runtime-input hash and intended-calendar contract;
4. verify 31/31 household convergence per successful year;
5. verify all 31×20 terminal fields finite;
6. verify checkpoint/output hashes;
7. compare corrected 2009 against the formal corrected-2009 cross-language anchor where exact comparable fields exist;
8. record historical-vs-corrected annual input/output differences as diagnostic, not parity;
9. do not run shock/IRF.

## 14. Required external evidence package

Use a fresh no-overwrite evidence root, preferred:

`D:\ProjectTemp\ch5-mp4c-owner-a-calendar-capital-provenance-20260902-001`

Persist at minimum:

- `owner_a_intended_calendar_contract.csv`;
- `legacy_matlab_calendar_binding_defect_trace.json`;
- `capital_series_provenance_map.json`;
- `capital_series_2000_2023_31province_comparison.csv`;
- `capital_negative_value_diagnosis.json`;
- `selected_intended_capital_contract.json` or deterministic reconstruction contract;
- `all_15_year_corrected_input_preflight.json`;
- `corrected_2009_anchor_check.json`;
- `corrected_vs_legacy_input_diff_2009_2023.json`;
- `zero_science_phase_a_ledger.json`;
- `8worker_execution_ledger.json`;
- `corrected_batch_audit.json`;
- `evidence_manifest.json`.

## 15. Repository mutation boundary

Allowed tracked changes are limited to the smallest necessary:

- corrected annual input/runtime adapter;
- focused input/provenance helper if needed;
- batch/launcher manifest changes needed for the new representation and exact `Workers=8` execution;
- focused tests;
- final repository report.

Forbidden tracked changes:

- protected MATLAB source;
- local data/cache binaries;
- generated annual batch outputs;
- HJB/KFE/household/one-turn/firm/migration/capital/wage/monetary/fiscal/controller scientific algorithms;
- shock implementation.

## 16. Required tests before scientific execution

Zero-science tests must cover at minimum:

- 15 rolling windows `2000–2009` through `2014–2023`;
- R vintages `10–24`;
- calendar level years `2009–2023`;
- exact 31-province order;
- legacy `row=1–15` rejected under Owner-A representation;
- intended capital provenance identity;
- wrong capital source/hash fails closed;
- all 15 intended CAP/GDP/POP finite positive;
- all required logs finite real;
- corrected 2009 anchor consistency;
- scheduler exact years 2009–2023;
- launcher/runner exact `Workers=8` accepted;
- BLAS/OpenMP threads forced to 1;
- no automatic rerun;
- terminal-only logging;
- checkpoint schema retained;
- no protected source mutation.

Run `py_compile` on changed/new Python.

## 17. Terminal classifications

If capital provenance remains unresolved before science:

`MP4C_OWNER_A_CAPITAL_PROVENANCE_UNRESOLVED__RERUN_NOT_AUTHORIZED`

If corrected input preflight passes but scientific execution fails:

`MP4C_OWNER_A_CORRECTED_8WORKER_BATCH_EXECUTION_INCOMPLETE__NO_AUTOMATIC_RERUN`

If all 15 years pass and closeout audit passes:

`MP4C_OWNER_A_INTENDED_CALENDAR_2009_2023_CORRECTED_8WORKER_ANNUAL_STATIONARY_COVERAGE_PASS`

This terminal is Python corrected annual coverage under Owner-A intended calendar semantics. It does not by itself establish full 2010–2023 MATLAB–Python parity.

## 18. Required repository report

On successful or blocked closeout, create exactly one report:

`docs/CH5_TWO_ASSET_HANK_MP4C_OWNER_A_INTENDED_CALENDAR_CAPITAL_PROVENANCE_AND_8WORKER_CORRECTED_RERUN_REPORT.md`

The report must distinguish:

- Owner scientific intent;
- legacy MATLAB calendar-binding defect;
- capital-series provenance decision;
- corrected annual input contract;
- 8-worker execution evidence;
- corrected 2009 regression anchor evidence;
- what remains unproven for cross-language annual parity;
- MP4D numerical shock remains blocked until corrected annual coverage is accepted.

Do not begin MP4D numerical shock implementation inside this task.
