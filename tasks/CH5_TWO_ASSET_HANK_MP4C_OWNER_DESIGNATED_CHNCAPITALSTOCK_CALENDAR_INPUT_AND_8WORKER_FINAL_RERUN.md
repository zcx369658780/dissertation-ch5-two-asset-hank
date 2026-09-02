# CH5_TWO_ASSET_HANK_MP4C_OWNER_DESIGNATED_CHNCAPITALSTOCK_CALENDAR_INPUT_AND_8WORKER_FINAL_RERUN

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / R-capital forensic verifier / data-binding implementer / controlled batch executor

Owner: final scientific authority

## 1. Revision, supersession, and current scientific decision

This live task now supersedes the latest reproduction-block execution:

`ebe8b17364a1d9b860d154b7f6c21e000adb515e`

with terminal:

`MP4C_STORED_R_CHNCAPITALSTOCK_REPRODUCIBILITY_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`.

That execution correctly stopped because, at that time, the local R runtime/package/source required for independent reconstruction had not been recovered.

The Owner has now supplied additional decisive evidence:

- R `4.6.1` is available at `C:\Program Files\R\R-4.6.1\bin\Rscript.exe`;
- an independent user library contains `CHNCapitalStock 0.1.1` and `openxlsx 4.2.8.1`;
- `D:\Rprogramme\main.r` contains the historical capital-construction code;
- the available `main.r` is a May-2025 backup and a later local revision may have extended the capital construction to 2023.

The stored Zhang-Jun-method candidate remains the **last sheet** of:

`2000年后各省数据_填充NA.xlsx`

under the exact sheet name:

`R语言计算资本存量`.

The corresponding upstream/raw workbook is:

`2000年后各省数据.xlsx`.

The dissertation documents the Zhang-Jun capital-stock methodology and use of the R package `CHNCapitalStock`.

The stored sheet remains an **Owner-designated candidate** and is not yet final HANK input authority.

Required candidate marker:

`OWNER_DESIGNATES_R语言计算资本存量_AS_CANDIDATE_CHNCAPITALSTOCK_SERIES_PENDING_REPRODUCIBILITY_AUDIT`.

Only after the verification gates below pass may Codex promote it to:

`OWNER_A_R语言计算资本存量_VERIFIED_AS_INTENDED_CHNCAPITALSTOCK_HANK_CAPITAL_SERIES`.

### 1.1 Archived R program proves the recovered copy is only a 2000–2022 reconstruction source

The recovered program contains all of the following:

- `data_list <- data.frame("省份"=2000:2023)`;
- for every province, `CompK_ZJ(prv=..., bt=2000)`;
- `selected_rows <- temp_result$yr >= 2000 & temp_result$yr <= 2022`;
- the result is written to sheet `R语言计算资本存量`;
- the later overall and rolling PLM sections read `R语言计算资本存量` as the capital input;
- the rolling estimation loop is `itime in 10:24`.

Current package evidence shows `CompK_ZJ(..., bt=2000)` exposes years only through `2022`. Therefore the recovered May-2025 script/current package route cannot by itself reproduce the stored 2023 row.

This does **not** prove the stored 2023 row is wrong. It proves only that the currently recovered archived route is insufficient to verify it. The Owner explicitly authorizes a bounded source-faithful investigation of the likely later 2023 extension.

## 2. Frozen intended calendar semantics

Freeze exactly:

- processed annual level-data calendar: `2000–2023`, exactly 24 years;
- reported annual steady states: `2009–2023`, exactly 15 years;
- steady-state year `Y` uses the 10-year rolling PLM window `[Y-9,Y]`;
- rolling-window/cache entry: `Y-2008` => `1–15`;
- R regression vintage: `Y-1999` => `10–24`;
- calendar level row: `Y-1999` => `10–24`;
- level calendar year: `Y`;
- rolling technology/productivity objects come from the matching 10-year PLM window;
- annual GDP, POP and intended capital levels correspond to the **window end year `Y`**.

The historical protected MATLAB annual loop that passes `data_year=ii` for `ii=1..15` is classified as:

`LEGACY_MATLAB_CALENDAR_BINDING_DEFECT__NOT_FINAL_PAPER_SCIENCE_AUTHORITY`.

This decision changes annual calendar/data binding only. It does not authorize mutation of HJB/KFE, household equations, one-turn ordering, migration, firm/wage/monetary/fiscal blocks, controllers, calibration, grids, tolerances, convergence thresholds, or accepted MP4D shock-response semantics.

The corrected-2009 same-input MATLAB–Python parity remains the numerical regression anchor.

## 3. Required live continuity

At execution start:

1. fresh-fetch `origin/main`;
2. require this exact revised task content live on `main`;
3. require the revised-task commit to be the direct child of latest blocker execution `ebe8b17364a1d9b860d154b7f6c21e000adb515e`, modulo only L3 task-refinement commits that update this exact task path;
4. require `HEAD == origin/main`, ahead/behind `0/0`;
5. require a clean tracked worktree;
6. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md` and all CURRENT rules it names;
   - corrected-2009 parity acceptance;
   - prior MP4C scope/data/runtime-cache reports and tasks;
   - capital-provenance blocker report at `f4a905...`;
   - reproduction-block report at `ebe8b173...`;
   - MP4D source-semantics execution and L3 acceptance reports;
   - current annual adapter/worker/scheduler/tests;
   - dissertation passages documenting Zhang-Jun / `CHNCapitalStock` capital-stock construction;
   - `D:\Rprogramme\main.r` and any other recovered historical/later copies.

Do not use chat text as a substitute for the live revised task.

## 4. Phase A0 — exact artifact identity and local-R-history forensic search — ZERO HANK SCIENCE

Before reconstructing capital, identify and hash the exact local artifacts actually present.

Read-only inspect at minimum:

- `2000年后各省数据.xlsx`;
- `2000年后各省数据_填充NA.xlsx`;
- `R语言估计结果_plm估计.xlsx`;
- `数据估计结果_1000_100_0.mat`;
- `D:\Rprogramme\main.r`;
- all `.R`, `.r`, `.RData`, `.rds`, package source, package metadata, saved workspaces and generated artifacts under relevant R/Matlab/back-up roots that mention any of:
  - `CompK_ZJ`;
  - `CHNCapitalStock`;
  - `R语言计算资本存量`;
  - `2023`;
  - `asset`;
  - capital-stock / Zhang-Jun construction.

The purpose is to determine whether a **later local revision** exists that extended the package data or the reconstruction through 2023.

Do not delete, overwrite, normalize or edit any recovered source. The refused cleanup of the older R installation is not a blocker and no deletion is required by this task.

Record SHA-256, bytes, modified time, path, and provenance class for every relevant artifact.

### 4.1 Current R environment identity

Record, without further install/update:

- R executable/version;
- package library paths;
- `CHNCapitalStock` version and installed-source identity;
- `openxlsx` version;
- full source text or deparsed body for `CompK_ZJ` and every helper it calls;
- package datasets/objects consumed by `CompK_ZJ`, including their year/province support;
- package DESCRIPTION/NAMESPACE/source hashes where accessible.

The already available local verification environment may be used. No further internet installation/update is authorized.

## 5. Phase A1 — stored `R语言计算资本存量` axis, completeness, and internal-consistency audit

Treat the stored sheet as a candidate object only.

Prove:

- calendar years exactly `2000–2023` in order;
- exactly 24 annual rows;
- exactly 31 provincial columns excluding the year label;
- province labels map exactly to the accepted common 31-province order;
- no missing values;
- no duplicate year/province labels;
- all 24×31 values finite and strictly positive;
- 2022 and 2023 all 31 provinces finite and strictly positive;
- no hidden alternate rows/columns or formula/error cells change the interpreted data;
- units/price-base interpretation is recoverable from source/script/package evidence rather than guessed from magnitude alone.

Persist a 24×31 audit receipt with exact sheet coordinates and value hashes.

## 6. Phase A2 — split reproducibility audit: 2000–2022 first, 2023 separately

This is the decisive revised gate.

### 6.1 Reproduce 2000–2022 exactly with recovered/current package route

Using the exact recovered script semantics:

`CompK_ZJ(prv=<province>, bt=2000)`

and current local package/source identity, independently reconstruct all available years `2000–2022` for all 31 provinces.

Compare the resulting `23 × 31` matrix cell-by-cell against rows `2000–2022` of the stored `R语言计算资本存量` sheet.

Persist:

- exact-match count;
- max absolute difference;
- max relative/normalized difference;
- worst year/province pair;
- count above roundoff;
- whether any difference is only Excel serialization/display precision.

If 2000–2022 does not reproduce under the recovered route, STOP before any 2023 extension attempt with:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2022_REPRODUCTION_MISMATCH__2023_EXTENSION_NOT_AUTHORIZED`.

If it reproduces, classify:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2022_REPRODUCIBILITY_VERIFIED__2023_EXTENSION_PENDING`.

This partial marker does not authorize HANK.

### 6.2 Determine why current `CompK_ZJ` stops at 2022

From exact package source/data, identify whether the 2022 endpoint is caused by:

- package-internal source-data coverage;
- a hard-coded year bound;
- helper-function bound;
- missing 2023 investment/deflator/depreciation data;
- another deterministic reason.

Do not assume the package algorithm itself is incapable of 2023 merely because bundled data stop at 2022.

### 6.3 Search for a later local 2023 extension before writing any new reconstruction

Prefer, in order:

1. a later local `main.r` / R script;
2. a later local modified `CHNCapitalStock` package/source;
3. a later `asset`/input dataset or `.RData/.rds` object that explicitly includes 2023;
4. a saved deterministic 2023 reconstruction artifact whose lineage can be tied to the same algorithm.

If a later exact source exists, use it read-only to reproduce the stored 2023 row and record its identity.

### 6.4 Verification-only source-faithful 2023 extension is conditionally authorized

If no later source is found, the Owner authorizes Codex to create a **new verification-only R script in a fresh external evidence root** that extends the recovered Zhang-Jun / `CompK_ZJ` construction to 2023.

Do **not** edit:

- `D:\Rprogramme\main.r`;
- installed package files;
- raw/filled workbooks;
- protected MATLAB source.

The verification-only extension is permitted only if all of the following are proven:

1. the exact mathematical/algorithmic body of `CompK_ZJ` and helpers is recovered from local package source;
2. every required 2023 input is available locally with source identity and the **same definition/unit/price-base semantics** as the package's 1952–2022 inputs;
3. province/year mapping is exact;
4. no new empirical assumption, interpolation, clipping, ad-hoc deflator, changed depreciation rule, changed initial-capital rule, or altered package default is introduced;
5. a standalone reimplementation of the recovered algorithm reproduces the package's 2000–2022 results for **all 31 provinces** up to ordinary numerical roundoff before it is allowed to compute 2023.

The verification script may then append one 2023 calculation using the exact same recovered recurrence/method and exact provenance-qualified 2023 inputs.

If any required 2023 input is missing or definitionally incompatible, STOP rather than infer it.

### 6.5 Compare independently reconstructed 2023 to stored 2023

Compare all 31 reconstructed 2023 province values against the stored sheet's 2023 row.

Report:

- exact-match count;
- max absolute difference;
- max relative/normalized difference;
- worst province;
- stored value;
- reproduced value;
- whether discrepancy is roundoff/serialization only or material.

Do not choose a loose tolerance to force PASS.

## 7. Capital verification classifications

Choose exactly one strongest supported classification before correcting annual HANK inputs.

### V1 — full stored 2000–2023 series independently verified

Use if 2000–2022 reproduces and 2023 is reproduced from a later exact source or source-faithful extension with matching stored values:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2023_31PROV_REPRODUCIBILITY_VERIFIED__HANK_USE_AUTHORIZED`.

Promote the stored sheet to:

`OWNER_A_R语言计算资本存量_VERIFIED_AS_INTENDED_CHNCAPITALSTOCK_HANK_CAPITAL_SERIES`.

### V2 — stored 2023 has a uniquely proven deterministic defect, corrected 2023 artifact is reproducible

Use only if 2000–2022 is verified, exact-source algorithm/input evidence proves a unique 2023 correction, and a corrected 2023 row is independently reproducible:

`MP4C_STORED_R_CHNCAPITALSTOCK_2023_DEFECT_IDENTIFIED__SOURCE_FAITHFUL_RECONSTRUCTION_PROVEN__OWNER_A_HANK_USE_AUTHORIZED`.

Do not overwrite the workbook. Use a separately generated provenance-bound corrected capital artifact.

### V3 — unresolved

If 2023 package/source/input lineage is not unique or required 2023 source inputs are unavailable/incompatible:

`MP4C_STORED_R_CHNCAPITALSTOCK_REPRODUCIBILITY_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`.

STOP before HANK science.

### V4 — material contradiction

If exact-source/source-faithful reconstruction materially contradicts stored values and no unique corrected artifact can be proven:

`MP4C_STORED_R_CHNCAPITALSTOCK_MATERIAL_ERROR_CONFIRMED__HANK_RERUN_NOT_AUTHORIZED`.

STOP and persist the precise error map.

## 8. Model-unit/scaling gate after V1/V2 only

Only after V1 or V2, prove the exact conversion from the verified capital series to model-internal `Kt0/Kt/GovInv` units.

Use:

- corrected-2009 same-input parity anchor;
- existing model GDP/population multipliers;
- source unit documentation;
- verified capital artifact.

Do not invent scaling from magnitude alone.

If exact scaling cannot be deterministically recovered, STOP with:

`MP4C_CHNCAPITALSTOCK_MODEL_UNIT_SCALING_UNRESOLVED__RERUN_NOT_AUTHORIZED`.

## 9. Corrected Owner-A input construction after V1/V2 + scaling PASS only

Use explicit representation:

`OWNER_A_VERIFIED_CHNCAPITALSTOCK_ROLLING_PLM_END_YEAR_CALENDAR_INPUT`.

For steady-state year `Y`:

- `IND_alpha`, `IND_Zt` and other rolling-estimation technology objects: correct rolling entry `Y-2008`;
- GDP: calendar year `Y`, row `Y-1999`;
- POP: calendar year `Y`, row `Y-1999`;
- CAP: verified V1/V2 capital series for calendar year `Y` and province;
- `log_pgdp`: recompute deterministically from selected GDP/POP;
- `log_pcap`: recompute deterministically from selected verified CAP/POP;
- inter-province asset/capital ratio: recompute from the verified intended capital representation using the frozen source-semantic formula.

Bind every field to artifact SHA, sheet/source, year, province, unit/scaling rule and semantic index.

Do not reuse invalid legacy complex `log_pcap` after replacing CAP.

## 10. Mandatory 15-year ZERO-HANK-science preflight

Before any annual worker launch, materialize corrected inputs for all years `2009–2023`.

For every year prove:

- rolling window `[Y-9,Y]`;
- rolling entry `1–15`;
- R vintage `10–24`;
- calendar level row `10–24`;
- exact calendar year;
- exact 31-province order;
- exact workbook/cache/R capital artifact identities;
- GDP finite and positive;
- POP finite and positive;
- verified CAP finite and positive;
- `log_pgdp` finite real;
- `log_pcap` finite real;
- technology parameters finite/admissible;
- exact model-unit scaling contract;
- HANK worker launches = `0` during preflight.

For 2009, compare corrected relevant inputs explicitly against the formally accepted corrected-2009 same-input parity anchor. Any material unexplained contradiction stops before expensive execution.

## 11. Phase-A/preflight scientific budget

Until Sections 4–10 PASS:

- MATLAB HANK calls: `0`;
- R rolling-PLM regressions: `0`;
- Python stationary: `0`;
- Python household/HJB/KFE: `0`;
- comparator: `0`;
- shock/IRF/R5/Results: `0`.

Allowed R execution before HANK is limited to:

- current package 2000–2022 reproduction;
- read-only source/body inspection;
- the verification-only 2023 extension contract in Section 6.4.

No further package installation/update or internet retrieval is authorized.

## 12. Preflight terminal

If and only if V1 or V2, unit/scaling PASS, corrected-2009 anchor PASS, and all 15 input preflights PASS:

`MP4C_VERIFIED_CHNCAPITALSTOCK_CORRECTED_INPUTS_2009_2023_PREFLIGHT_PASS__8WORKER_BATCH_AUTHORIZED`.

Otherwise STOP under the strongest blocker classification above.

## 13. Phase B — exactly 8-worker corrected annual HANK rerun

Upon full preflight PASS, Codex is authorized to execute the corrected scientific batch directly without waiting for another Owner launch message.

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
Do not rerun R rolling-PLM estimation.
Do not run shocks/AR(1)/IRF/R5/Results.

Use fresh no-overwrite batch root, preferred:

`D:\ProjectTemp\ch5-mp4c-owner-a-verified-chncapitalstock-8worker-20260902-001`.

Never reuse prior batch roots.

If any infrastructure/memory/scientific-year failure occurs:

- preserve evidence;
- no automatic rerun;
- no worker-count change;
- STOP with incomplete/failure terminal.

## 14. Required annual and root outputs

For every successful year require:

- corrected annual input artifact and identity;
- final steady state;
- 31×20 terminal table;
- `Lt_mat`;
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

## 15. Phase C — read-only closeout

After the 8-worker batch completes:

1. audit all 15 years read-only;
2. require 15/15 `SOURCE_CONVERGED` for full PASS;
3. verify 31/31 household convergence per year;
4. verify all 31×20 fields finite;
5. verify corrected input identities and all semantic indices;
6. verify checkpoint and root artifact hashes;
7. compare corrected 2009 against the formally accepted corrected-2009 same-input anchor;
8. compare other years only against scientifically/calendar-compatible reference artifacts;
9. do not treat legacy `data_year=ii` MATLAB outputs as corrected 2010–2023 parity authority;
10. do not rerun MATLAB;
11. do not claim blanket 2010–2023 MATLAB–Python parity without compatible reference evidence.

## 16. Historical status

Preserve the old 9-hour batch as:

`LEGACY_CONFLATED_WINDOW_AND_LEVEL_ROW_BATCH__ENGINEERING_CONVERGENCE_ONLY__NOT_FINAL_CALENDAR_YEAR_AUTHORITY`.

Corrected-2009 same-input parity remains valid unless direct contradictory same-input evidence emerges.

MP4D source-semantics acceptance remains valid; numerical shock implementation remains blocked until this corrected annual gate closes.

## 17. Evidence package

Use fresh no-overwrite evidence root, preferred:

`D:\ProjectTemp\ch5-mp4c-chncapitalstock-2023-extension-repro-audit-20260902-001`.

Persist at minimum:

- `artifact_identity_manifest.json`;
- `local_r_history_search_manifest.json`;
- `archived_main_r_identity.json`;
- `chncapitalstock_package_source_and_version.json`;
- `compk_zj_source_and_dependency_contract.json`;
- `stored_r_capital_axis_completeness_audit.json`;
- `reproduced_2000_2022_chncapitalstock.csv`;
- `stored_vs_reproduced_2000_2022_diff.csv`;
- `stored_vs_reproduced_2000_2022_summary.json`;
- `package_2022_endpoint_diagnosis.json`;
- `later_2023_extension_source_search.json`;
- verification-only copied/reimplemented R script if Section 6.4 is used;
- `reproduced_2023_chncapitalstock.csv` if reproducible;
- `stored_vs_reproduced_2023_diff.csv` if reproducible;
- `capital_verification_classification.json`;
- `model_unit_scaling_audit.json` if V1/V2;
- `rolling_plm_calendar_contract.csv`;
- `corrected_2009_anchor_input_check.json` if V1/V2;
- `corrected_2009_2023_input_preflight.json` if V1/V2;
- `zero_hank_science_ledger.json`;
- `corrected_8worker_build_receipt.json` if batch authorized;
- `batch_execution_receipt.json` if science executes;
- `closeout_audit.json` if science completes;
- `manifest.json`.

## 18. Git boundary and report

Do not commit/push raw/filled workbooks, installed R package binaries, local package libraries, runtime MAT/NPZ/XLSX/CSV outputs, or generated batch data.

After final closeout, one bounded commit/push may include only authorized code/tests/contracts and the required repository report.

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_CHNCAPITALSTOCK_2023_EXTENSION_REPRO_AUDIT_AND_CORRECTED_8WORKER_RERUN_REPORT.md`.

## 19. Terminal classifications

Full capital verification and corrected rerun succeeds:

`MP4C_VERIFIED_CHNCAPITALSTOCK_2009_2023_CORRECTED_8WORKER_ANNUAL_STATIONARY_COVERAGE_PASS`.

2000–2022 reproduction mismatch:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2022_REPRODUCTION_MISMATCH__2023_EXTENSION_NOT_AUTHORIZED`.

2023 reproducibility unresolved:

`MP4C_STORED_R_CHNCAPITALSTOCK_REPRODUCIBILITY_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`.

Stored capital materially wrong and no unique reconstruction:

`MP4C_STORED_R_CHNCAPITALSTOCK_MATERIAL_ERROR_CONFIRMED__HANK_RERUN_NOT_AUTHORIZED`.

Unit/scaling unresolved:

`MP4C_CHNCAPITALSTOCK_MODEL_UNIT_SCALING_UNRESOLVED__RERUN_NOT_AUTHORIZED`.

Corrected 8-worker batch incomplete:

`MP4C_VERIFIED_CHNCAPITALSTOCK_CORRECTED_8WORKER_BATCH_INCOMPLETE__NO_AUTOMATIC_RERUN`.

No numerical shock/IRF implementation is authorized in this task.