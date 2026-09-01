# CH5_TWO_ASSET_HANK_MP4C_ANNUAL_DRIVER_GENERALIZATION_AND_CHUNK01_2010_2011_EXECUTION

Date: 2026-09-01

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor: Codex bounded Builder / annual-input preparer / sequential annual stationary executor

Owner: final scientific authority

## 1. Authority basis

Accepted predecessor execution:

`MP4C_MATLAB_ACTIVE_DATA_SOURCE_CONFIRMATION_AND_PYTHON_LOCAL_COPY_STAGING_PASS`

Execution commit:

`dde810ea4c62a1b59cbe335ba16a89701a4d2a02`

Accepted annual scope:

- calendar years `2009–2023` inclusive;
- corrected-2009 is already formally accepted and MUST NOT be rerun;
- future Python annual execution set is `2010–2023`;
- scheduling unit is two calendar years;
- scientific execution concurrency is exactly `1`.

This task authorizes only **Chunk 01: 2010 and 2011**, executed sequentially after a bounded zero-model annual-driver generalization and preflight.

The accepted corrected-2009 scientific implementation remains the anchor. This task does not authorize MATLAB reruns, cross-language comparator claims for 2010/2011, shocks, AR(1), dynamics, R5, or Results.

## 2. Required live continuity

Required execution-start predecessor:

`dde810ea4c62a1b59cbe335ba16a89701a4d2a02`

At execution start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as the direct child of the required predecessor;
3. require clean tracked worktree, `HEAD == origin/main`, ahead/behind `0/0`;
4. read completely:
   - `AGENTS.md`;
   - all CURRENT project rules named by the rule index;
   - formal corrected-2009 L3 parity acceptance report;
   - MP4C multiyear scope-freeze report;
   - MP4C local-data staging report;
   - current `src/ch5_two_asset_hank/multi_province/annual.py`;
   - current `validators/multi_province/mp4b_python_empirical.py`;
   - current repaired `one_turn.py`, `firm.py`, stationary runtime and household adapter used by the accepted 2009 route.

Any authority, identity, local-data, or source-readability failure => stop before scientific execution.

## 3. Frozen scientific identities

Before mutation or science require at minimum:

- repaired `one_turn.py` Git blob `e5d6835cdc9e6d182e1c84e11f4d51938be592e1`;
- frozen `firm.py` Git blob `1f7d37247e2d712fc0477a9f562dce81d1b367ce`;
- accepted 2009 scientific driver Git blob `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`;
- accepted standalone household oracle SHA-256 `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`;
- formal 2009 acceptance marker `MP4B_CORRECTED_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_FORMALLY_ACCEPTED`.

No equation, parameter, grid, household algorithm, migration/capital formula, firm formula, wage rule, controller rule, threshold, tolerance, update order, or source semantics may change.

## 4. Verified local primary-source inputs

Use only the ignored local byte-identical snapshot:

`data_local/matlab_primary_source_snapshot`

Required filenames and SHA-256:

- `2000年后各省数据_填充NA.xlsx`
  - `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929`
- `R语言估计结果_plm估计.xlsx`
  - `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68`
- `中国各省省会地理距离矩阵.xlsx`
  - `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566`

Require exact hashes before any annual canonical generation.

Do not use the unfilled workbook.
Do not use `数据估计结果_1000_100_0.mat` as primary scientific input.

## 5. Zero-model annual-driver generalization

The current accepted 2009 driver is intentionally calendar-2009-specific and must remain unchanged.

Create a new validation/scientific execution entry dedicated to MP4C, preferred path:

`validators/multi_province/mp4c_python_annual_empirical.py`

It must preserve the accepted 2009 scientific execution semantics and differ only where necessary to support explicit annual binding.

### 5.1 Required annual input behavior

Use existing production annual API:

- `DecoupledAnnualIndex.for_calendar_year(year)`;
- `PrimaryAnnualSourceFiles`;
- `AnnualSourceScalars`;
- `load_primary_annual_input(...)`;
- `CanonicalAnnualInput.canonical_bytes()` / `canonical_sha256()`.

Do not recouple calendar year, workbook row, analysis index, `data_MAT` index, regression vintage, or output filename year.

For 2010 and 2011 the frozen identities are:

| Year | Workbook numeric row | Analysis index | data_MAT index | Regression vintage |
|---:|---:|---:|---:|---:|
| 2010 | 11 | 2 | 2 | 11 |
| 2011 | 12 | 3 | 3 | 12 |

The annual source scalars must be sourced from the already accepted corrected-2009 primary canonical contract, not re-estimated or guessed.

The source fixed-`Zt` initialization remains the protected calendar-2020 anchor exactly as defined by the accepted annual API.

### 5.2 Canonical filename hardcoding

Current `write_canonical_artifact(...)` in `annual.py` uses a calendar-2009 filename literal even though the API supports 2009–2023.

This task may either:

A. minimally repair that utility so the filename is derived from `canonical.binding.calendar_year`, with focused zero-science tests; or

B. leave production `annual.py` untouched and have the MP4C validation driver write `canonical.canonical_bytes()` to an explicit year-named external artifact.

Choose the smaller and safer change. Do not change canonical bytes or formulas.

### 5.3 Scientific driver semantics

The new MP4C driver must use the same accepted modules and source order as the accepted corrected-2009 driver:

- same household adapter;
- same HJB/KFE numerics;
- same grid;
- same synchronous/Jacobi 31-province household batch;
- same migration/capital/firm/wage/monetary/fiscal/controller route;
- repaired same-turn `household_lt -> firm_source["Lt_prev"]` mapping through current `one_turn.py`;
- current firm labor remains migration destination `Lt_supply`;
- same `AtTax` mapping;
- same source controller thresholds and 0.9/1.1 actions;
- same convergence definition.

The driver must take an explicit canonical annual JSON and derive/verify calendar year and canonical SHA from that input; it must not hardcode 2009.

### 5.4 Execution ceiling

MP4C per-year finite ceiling is frozen as:

- outer turns: maximum `250`;
- household calls: maximum `7750`;
- wall-clock: maximum `14400` seconds;
- reruns: `0`.

The 250-turn ceiling is a fail-isolation execution ceiling. It must not change any convergence tolerance or controller rule. A year that reaches the ceiling is classified anomalous rather than silently accepted.

## 6. Pre-science validation

Before any 2010/2011 stationary call:

1. verify all frozen scientific identities;
2. verify all three local input hashes;
3. generate 2010 and 2011 canonical annual artifacts in fresh external no-overwrite roots;
4. validate for each year:
   - exact calendar binding;
   - exact 31-province order;
   - expected regression sheet/vintage;
   - source hashes;
   - finiteness and source formulas;
5. perform a zero-model 2009 compatibility proof for the new generic path:
   - using the verified local copies and accepted 2009 scalars, reconstruct 2009 canonical bytes;
   - require exact SHA-256 equality with accepted canonical `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`;
   - do NOT run 2009 stationary;
6. compare the new MP4C driver against the accepted 2009 driver statically or via no-model entry-state/preflight logic, proving no scientific-semantic change beyond dynamic annual binding and execution ceiling;
7. `py_compile` all changed/new Python files;
8. run focused zero-science/non-empirical tests;
9. require no scientific/model calls before the first annual launch.

Any failed common preflight => stop before all annual science.

## 7. Scientific execution budget — Chunk 01 only

Authorized years:

- 2010: maximum one Python annual stationary execution;
- 2011: maximum one Python annual stationary execution.

Concurrency: exactly `1`.
Reruns: `0` for each year.

MATLAB calls: `0`.
Comparator calls: `0`.
Other calendar years: `0`.

Run 2010 first, then 2011 only after the 2010 process has terminated and the common scientific identities remain unchanged.

### 7.1 Per-year failure isolation

If a year ends because of ordinary model non-convergence / finite execution ceiling after a valid launch, preserve its evidence and classify that year as `ANOMALY`; this alone does not require rerunning it and does not automatically invalidate the other independent year.

If a failure indicates shared infrastructure, corrupted canonical binding, source identity change, driver defect, or scientific-code mutation, stop the chunk before launching any later year.

No repair-and-rerun lane exists after a year's scientific call is consumed.

## 8. Required per-year evidence

For each launched year persist externally:

- canonical annual input JSON and SHA-256;
- calendar/index identity manifest;
- source-file hashes;
- scientific code identity manifest;
- exact launcher command;
- run manifest;
- terminal summary;
- outer-turn count;
- household-call count;
- final household convergence count;
- terminal province order;
- final 31x20 frozen field table or complete final-state object;
- terminal category counts:
  - household converged;
  - ra upper/lower;
  - wage upper/lower;
- national `Ct/At/Bt/Yt`;
- wall-clock duration;
- execution ledger;
- anomaly reason if not accepted.

Intermediate HJB non-convergence flags retain the already accepted source-postloop semantics; do not invent a new rejection rule.

## 9. Chunk classifications

A per-year normal coverage PASS requires:

- process exits normally;
- `SOURCE_CONVERGED`;
- outer turns <= 250;
- household calls <= 7750;
- final 31-province state complete and unique;
- final household convergence `31/31`;
- all frozen final fields finite;
- category fields source-consistent;
- no source/input/scientific identity violation.

Use per-year marker:

`MP4C_YEAR_<YYYY>_PYTHON_ANNUAL_STATIONARY_COVERAGE_PASS`

If both years pass:

`MP4C_CHUNK01_2010_2011_PYTHON_ANNUAL_STATIONARY_COVERAGE_PASS`

If one or both years are scientifically launched but anomalous:

`MP4C_CHUNK01_2010_2011_COMPLETED_WITH_FAIL_ISOLATED_ANOMALY`

If common preflight/shared infrastructure blocks science:

`MP4C_CHUNK01_2010_2011_BLOCKED_BEFORE_COMPLETE_EXECUTION`

Do not call 2010/2011 MATLAB-Python parity; only corrected-2009 has cross-language parity authority.

## 10. External roots

Preferred preparation root:

`D:\ProjectTemp\ch5-mp4c-chunk01-2010-2011-preparation-20260901-001`

Preferred run roots:

- `D:\ProjectTemp\ch5-mp4c-python-annual-2010-20260901-001`
- `D:\ProjectTemp\ch5-mp4c-python-annual-2011-20260901-001`

Use next deterministic suffix if a preferred root exists. Never overwrite.

Persist a chunk-level summary and manifest containing every artifact SHA/size and the complete call ledger.

## 11. Repository mutation scope

Allowed repository changes:

- new MP4C annual execution driver under `validators/multi_province/`;
- minimal focused tests required for the annual-generalization contract;
- `annual.py` only if choosing the bounded dynamic-filename repair in Section 5.2;
- required execution report.

Do not modify:

- household/HJB/KFE scientific implementation;
- `one_turn.py`;
- `firm.py`;
- migration/capital/wage/monetary/fiscal/controller implementation;
- accepted 2009 driver;
- comparator;
- source data;
- canonical 2009 artifact;
- thresholds/tolerances;
- project rules or prior reports.

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_ANNUAL_DRIVER_GENERALIZATION_AND_CHUNK01_2010_2011_EXECUTION_REPORT.md`

Before commit:

- explicit allowed-path staging only;
- no binary/local data staged;
- `git diff --check --cached` PASS.

Closeout:

- exactly one execution commit;
- exactly one non-force push;
- fresh GitHub read-back of every changed repository path;
- `HEAD == origin/main`;
- ahead/behind `0/0`;
- clean tracked worktree;
- report ignored local data path separately.

## 12. Exactly one recommended next gate

If both 2010 and 2011 pass without a shared implementation anomaly, recommend:

`MP4C_CHUNK02_2012_2013_PYTHON_ANNUAL_STATIONARY_EXECUTION`

If an anomaly occurs, recommend one fail-isolated diagnostic gate for the first anomalous year instead of continuing blindly.

Do not start Chunk 02, another year, shocks, AR(1), transition/IRF, R5, or Results from inside this execution.
