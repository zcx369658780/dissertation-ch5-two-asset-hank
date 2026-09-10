# CH5 MP4C 2018 raw-NBS data rebuild, capital stock and productivity re-estimation

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Rebuild a clean province-year data panel directly from the original National Bureau of Statistics source files used by the Owner, then re-estimate province capital stock and productivity for the 2018 comparison object.

The immediate scientific purpose is to replace the legacy mixed-year MATLAB input object with a transparent same-year data object before any further HANK/outer-loop simulation.

The final deliverable must make it easy for the Reviewer/Owner to compare:

1. the legacy MATLAB 2018-labelled values;
2. the corrected raw-NBS 2018 values;
3. the newly estimated 2018 capital stock and productivity.

This task is a **data reconstruction / econometric-calibration task only**. It does not authorize any HJB/KFE/firm/outer-loop/steady-state/GE/IRF/Results model execution.

## 2. Required authority

Read live GitHub first:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`;
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`;
- `docs/CH5_MP4C_2018_MATLAB_INPUT_DATA_AND_INITIAL_STATE_COMPARISON_AUDIT_REPORT.md`;
- its Reviewer acceptance and 31-province ledger;
- current accepted PIM / rolling-PLM / same-year-Zt reports needed to reproduce the presently frozen calibration definitions.

The previous data audit is accepted evidence. Do not rerun or rewrite it.

## 3. Raw NBS source files

Read the Owner's original source directory read-only:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Primary raw files supplied by the Owner:

- `地区生产总值 亿元.xls`
- `固定资本形成总额 亿元.xls`
- `固定资产折旧 亿元.xls`
- `年末常住人口 万人.xls`

These are source data downloaded from the National Bureau of Statistics website according to the Owner.

Do not modify or overwrite the XLS files.

Hash every source file actually consumed and record workbook/sheet/year/province layout.

If exact filenames differ only by benign Windows naming/encoding display, resolve cautiously and record the actual file read. Do not silently substitute a processed workbook such as `2000年后各省数据_填充NA.xlsx` for the raw NBS sources.

## 4. Data cleaning and same-year reconstruction

Construct a clean 31-province panel from the four raw source files.

Requirements:

1. preserve the accepted 31-province order;
2. identify the actual year columns/rows in every source workbook;
3. normalize province names only through an explicit mapping table;
4. retain the original units in raw columns;
5. create explicit transformed/model-unit columns separately;
6. do not forward/backward fill missing observations silently;
7. flag missing/nonpositive/structurally unavailable values;
8. prefer the common observed-year intersection for estimation;
9. produce a dedicated same-year 2018 slice.

For 2018, GDP, population, investment/capital-formation and depreciation must all come from their actual 2018 observations when present.

If a raw 2018 value conflicts materially with the already accepted corrected/canonical 2018 object, preserve both and report the discrepancy rather than silently forcing a match.

## 5. Capital stock estimation — two separated tracks

Do not silently choose a new production-capital definition. Produce two explicitly separated capital series.

### Track A — primary comparable PIM

Use the currently accepted Chapter-5 PIM contract as the **primary comparison series**, now applied to the cleaned raw-NBS fixed-capital-formation series:

`K0 = I0 / 0.1`

`Kt = (1 - 0.096) * K(t-1) + I(t-1)`

where the exact timing/index convention must be stated and tested.

This track exists to preserve comparability with the current accepted canonical calibration while correcting the underlying year/data route.

### Track B — observed-depreciation accounting diagnostic

Because the Owner supplied `固定资产折旧 亿元.xls`, construct a separate diagnostic capital path, if the source coverage permits, using the accounting accumulation identity based on observed capital formation and observed depreciation.

Do not promote this Track-B object to production authority. State the exact timing used, initial-stock assumption, and any coverage limitation. If the accounting identity cannot be formed cleanly, report the gap rather than inventing data.

For both tracks:

- retain raw and transformed units;
- report 2018 capital by province;
- report capital per capita and K/Y diagnostics;
- quantify Track A vs Track B differences where both exist.

The raw fixed-capital-formation and depreciation flows themselves must also appear in the final 2018 comparison ledger.

## 6. Re-estimate alpha under the existing PLM logic

Re-estimate the capital elasticity using the corrected panel and the same econometric specification family previously accepted for Chapter 5, rather than carrying over the legacy mixed-year object.

Primary 2018-vintage specification:

- rolling 10-year window;
- 2018 vintage window = 2009–2018;
- equation family consistent with the accepted/original route:

`log(Y/L) = intercept + time trend + alpha * log(K/L) + error`

where `L` is the currently used population proxy unless the live accepted contract specifies a different variable.

Use Track-A capital for the primary re-estimation so that alpha and Zt are internally consistent with the primary PIM series.

Record:

- sample size;
- exact years;
- included provinces;
- missing-data exclusions;
- coefficient estimate alpha;
- standard error / t-stat / p-value when available;
- fit diagnostics;
- estimation implementation and package/version.

Do not force alpha into any prior range merely to match the legacy MATLAB value.

Also compare the newly estimated alpha with the previous accepted value:

`0.772866243094144`

but do not treat equality as a target.

## 7. Re-estimate province productivity

Using the corrected same-year 2018 objects and the newly estimated primary alpha, compute province productivity consistently as:

`Z_i,2018 = Y_i,2018 / (K_i,2018 ^ alpha * L_i,2018 ^ (1-alpha))`

with raw/model-unit conventions stated explicitly.

Also compute a diagnostic productivity using Track-B capital where available, but label it separately.

Do not use 2020 levels to generate the 2018 productivity object.

The primary 2018 Zt must be a genuine same-year 2018 object.

## 8. Required MATLAB-vs-corrected comparison table

Produce a 31-province human-readable Markdown table and machine-readable CSV with at least these columns:

- province index
- province name
- legacy MATLAB level year
- corrected year
- legacy MATLAB GDP
- raw-NBS corrected 2018 GDP
- GDP relative difference
- legacy MATLAB population
- raw-NBS corrected 2018 population
- population relative difference
- raw-NBS 2018 fixed capital formation
- raw-NBS 2018 depreciation
- legacy MATLAB capital object
- corrected Track-A 2018 capital
- capital relative difference
- corrected Track-B 2018 capital, if available
- Track-A / Track-B ratio
- legacy alpha
- newly re-estimated alpha
- legacy MATLAB Zt
- corrected same-year Track-A Zt
- Zt relative difference
- Track-B Zt, if available
- K/Y
- K/N
- Y/N
- data-quality / provenance flag

Highlight 安徽 explicitly, but retain all 31 provinces.

The table is the object the Reviewer will display to the Owner after acceptance, so keep it compact enough to read while preserving exact machine values in the CSV.

## 9. Validation and reconciliation

Perform static/data-estimation checks only.

At minimum verify:

- 31/31 province order;
- exact year identity for the 2018 slice;
- no legacy 2009/2020 mixing in the corrected 2018 object;
- source-file hashes;
- unit transformations;
- capital recursion identity for Track A;
- accounting recursion identity for Track B where available;
- alpha estimation sample and equation;
- same-year Zt formula;
- finite/positive requirements for logs and production function inputs;
- reproducibility from committed scripts + derived CSVs.

Compare the rebuilt raw-NBS 2018 GDP/POP and primary capital against the current accepted canonical 2018 values. Classify differences rather than silently overwriting one authority.

## 10. Execution budget and prohibited model work

Allowed:

- Python/R/Stata-style data cleaning and regression/calibration scripts;
- read-only XLS parsing;
- deterministic PIM/accounting accumulation;
- PLM/panel/OLS estimation required by this task;
- derived-table generation and tests.

These are authorized data/calibration computations for this task.

Model/scientific runtime budget remains zero for:

- MATLAB HANK calls = 0;
- Python household/HJB/KFE calls = 0;
- firm/wage/migration/capital-allocation calls = 0;
- outer turn = 0;
- steady state/GE/annual/IRF/Results = 0.

Do not run any model simply to see whether the new data converge.

## 11. Repository outputs

Use a fresh no-overwrite evidence root under `D:\ProjectTemp`.

Commit repository-safe derived results and reproducible scripts to the repository. Do **not** commit the original XLS source files unless a later Owner instruction explicitly requests raw-data publication.

Required outputs:

- `docs/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_REPORT.md`
- `reports/mp4c_2018_raw_nbs_rebuild_20260910/cleaned_province_year_panel.csv`
- `reports/mp4c_2018_raw_nbs_rebuild_20260910/corrected_2018_vs_matlab_ledger.csv`
- `reports/mp4c_2018_raw_nbs_rebuild_20260910/corrected_2018_vs_matlab_ledger.md`
- `reports/mp4c_2018_raw_nbs_rebuild_20260910/alpha_estimation_receipt.json`
- `reports/mp4c_2018_raw_nbs_rebuild_20260910/capital_method_comparison.csv`
- `reports/mp4c_2018_raw_nbs_rebuild_20260910/source_hash_receipt.json`
- `reports/mp4c_2018_raw_nbs_rebuild_20260910/data_quality_flags.csv`
- reproducible builder/validator script(s) under an appropriate `validators/` or `scripts/` path
- focused tests
- manifest/readback receipt

If the full cleaned panel contains years with unreliable coverage, keep the observations and flags explicit; do not fabricate completeness.

## 12. Required report answers

The report must answer first:

1. What years are actually available in each raw NBS source file?
2. Is a fully same-year 2018 31-province dataset available from the four raw sources?
3. What is the corrected 2018 Track-A capital stock for each province?
4. What does the observed-depreciation Track-B diagnostic imply, and how different is it?
5. What is the newly re-estimated 2009–2018 alpha?
6. What is the corrected same-year 2018 Zt for each province?
7. How large are the differences versus the legacy MATLAB mixed-year object?
8. Does 安徽 remain an unusually large discrepancy after rebuilding from the raw NBS files?
9. Are there unit/year/province/coverage problems that still require Owner scientific judgment?
10. Confirm that no HANK/HJB/KFE/firm/outer-loop model was run.

## 13. Verdicts

Allowed primary verdicts:

- `RAW_NBS_2018_REBUILD_PASS__CAPITAL_AND_PRODUCTIVITY_REESTIMATED`
- `RAW_NBS_2018_REBUILD_PARTIAL__SOURCE_COVERAGE_OR_UNIT_AMBIGUITY`
- `RAW_NBS_2018_REBUILD_BLOCKED__RAW_SOURCE_INSUFFICIENT`

A PASS means only that the data/calibration object is reproducibly rebuilt. It does not authorize model convergence claims or Results.

## 14. Git / publication

Use a dedicated branch/worktree where practical.

- preserve unrelated dirty/untracked files;
- no reset/clean/stash;
- explicit path staging only;
- no force push;
- commit and non-force push the report, scripts and repository-safe derived data;
- do not merge main;
- do not publish a successor model task.

Return the candidate commit SHA and branch to ChatGPT Reviewer for acceptance.