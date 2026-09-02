# CH5_TWO_ASSET_HANK_MP4C_LATEST_R_PLM_2023_CAPITAL_LINEAGE_RECOVERY_AND_CORRECTED_8WORKER_RERUN

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / R-forensic verifier / data-binding implementer / controlled batch executor

Owner: final scientific authority

## 1. Authority basis and new Owner evidence

Immediate predecessor execution:

`ad9a5b291f8e69dd59c1a023c2e34719c571ee1b`

with accepted partial finding:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2022_REPRODUCIBILITY_VERIFIED__2023_EXTENSION_PENDING`

and terminal:

`MP4C_STORED_R_CHNCAPITALSTOCK_REPRODUCIBILITY_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`.

The predecessor proved that R 4.6.1 + `CHNCapitalStock 0.1.1` + `CompK_ZJ(prv, bt=2000)` reproduces the stored `R语言计算资本存量` rows 2000–2022 for all 31 provinces up to ordinary Excel floating serialization differences.

The Owner has now recovered the **latest available PLM estimation program from the old PC** and copied it to the current machine at:

`D:\Rprogramme\main.r`

The R source text still contains **historical old-PC path literals**, e.g. an `E:/DBackup/.../MatlabProgramme/...` working directory. Those path strings are provenance evidence only and MUST NOT be executed literally on the current PC.

The current-PC data root must be resolved and verified from actual local files. The expected active root is:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

but Codex must verify exact workbook existence and hashes rather than assume the path.

## 2. Key static facts already visible in the recovered latest R program

The latest recovered `D:\Rprogramme\main.r` must be hashed and read completely. At minimum verify these source facts directly:

1. capital scaffold declares `data_list <- data.frame("省份"=2000:2023)`;
2. capital construction still calls `CompK_ZJ(prv=..., bt=2000)`;
3. that block still selects `temp_result$yr <= 2022`, so the capital-construction preamble by itself does **not** explain the stored 2023 row;
4. later model-calibration/PLM code reads capital from sheet `R语言计算资本存量`;
5. aggregate route is now explicitly `for (ind in 4:4)`;
6. GDP and capital use `GDP_multiplier = 1000` and population uses `POP_multiplier = 100`;
7. aggregate capital is read as `R语言计算资本存量` and multiplied by the same `GDP_multiplier`;
8. rolling PLM uses `itime in 10:24` and for each `itime` reads exactly rows `(itime-9):itime`, i.e. 10-year windows ending at vintages 10–24.

These facts establish the intended PLM/calibration semantics, but they do not by themselves prove how the stored 2023 capital row was generated.

## 3. Frozen intended annual semantics

Retain the Owner-A scientific decision:

- level-data calendar: 2000–2023;
- annual steady states: 2009–2023;
- steady-state year `Y` uses rolling PLM window `[Y-9, Y]`;
- rolling-window entry: `Y-2008` => 1–15;
- R/PLM vintage: `Y-1999` => 10–24;
- calendar level row: `Y-1999` => 10–24;
- GDP, POP and intended CAP correspond to the window-end calendar year `Y`.

The historical MATLAB annual `data_year=ii` implementation remains:

`LEGACY_MATLAB_CALENDAR_BINDING_DEFECT__NOT_FINAL_PAPER_SCIENCE_AUTHORITY`.

The corrected-2009 same-input MATLAB–Python parity remains the numerical regression anchor.

The MP4D source-semantics classification remains accepted:

`SEQUENTIAL_STATIONARY_COMPARATIVE_STATICS_RESPONSE_PATH_CONFIRMED`.

No numerical shock work is authorized here.

## 4. Required live continuity

At start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as a direct child of `ad9a5b291f8e69dd59c1a023c2e34719c571ee1b`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read completely `AGENTS.md`, rule index, all CURRENT rules, predecessor capital-reproduction report, Owner-A annual-data reports, corrected-2009 parity authority, MP4D acceptance, current annual Python adapter/worker/scheduler/tests;
6. hash and read current `D:\Rprogramme\main.r` completely.

## 5. Path rebinding rule — CRITICAL

Do **not** modify `D:\Rprogramme\main.r` in place.

Do **not** execute its old-PC `setwd(...)` path literally.

For any bounded R verification:

1. create a copied verifier script in a fresh external evidence root;
2. preserve the original source SHA and line mapping;
3. change only filesystem path bindings, output destinations, and guards needed to prevent mutation of source workbooks;
4. point read-only input to the verified current-PC workbook root;
5. write every generated verification output to the evidence root only;
6. persist an exact diff between original `main.r` and the verifier copy, proving no regression formula, window, multiplier, package call or economic transformation was changed.

Expected current source artifacts to resolve/read-only include:

- `D:\Rprogramme\main.r`;
- `2000年后各省数据.xlsx`;
- `2000年后各省数据_填充NA.xlsx`;
- `R语言估计结果_plm估计.xlsx`;
- `数据估计结果_1000_100_0.mat`.

## 6. Phase A — latest-R forensic audit — NO HANK SCIENCE

Until all gates below pass:

- MATLAB HANK calls: 0;
- Python stationary calls: 0;
- Python household/HJB/KFE calls: 0;
- comparator calls: 0;
- shock/IRF/R5/Results: 0.

R execution is authorized only for the bounded verification procedures below.

### 6.1 Compare latest recovered `main.r` with prior recovered R evidence

Search prior evidence roots/backups for the previously audited `main.r` copy/hash if available.

Produce a source-diff classification showing exactly what changed in the latest recovered program.

At minimum record whether changes affect:

- capital construction;
- 2023 handling;
- package call;
- aggregate `ind` loop;
- GDP/CAP/POP multipliers;
- rolling-window loop;
- regression formula;
- output sheet names.

If the latest file still does not generate 2023 capital, state that explicitly; do not infer that it does.

### 6.2 Structural consistency of capital-writing preamble

The source declares a 24-row `2000:2023` data frame but selects `CompK_ZJ` values only through 2022 under the currently available package data.

Using a verification-only copied script or minimal isolated R expression, determine the exact behavior of this preamble under current R/package semantics.

Do not allow it to write to the real workbook.

Classify whether the preamble:

- errors because a 23-value vector cannot populate 24 rows;
- recycles/truncates under some historical semantics;
- was likely intended to be run selectively rather than as the full current script;
- or has another source-backed behavior.

This is provenance evidence only.

## 7. Phase B — bounded latest-PLM reproduction audit

The Owner has recovered the latest PLM program specifically so its calibration output can be verified.

Create a verification-only copy of the PLM section with only path/output rebinding.

The verifier MUST:

- read the verified current `2000年后各省数据_填充NA.xlsx` read-only;
- use its existing stored `R语言计算资本存量` sheet exactly as present;
- run only the aggregate `ind=4` grouped/rolling PLM code encoded by the recovered latest program;
- preserve `GDP_multiplier=1000`, `POP_multiplier=100`, `CAP * 1000` exactly;
- preserve rolling `itime=10:24`, 10-year rows `(itime-9):itime`, `time=0:9`, formula `log(pgdp) ~ 1 + time + log(pcap)`, `model="within"`, coefficient and fixed-effect extraction exactly;
- write a new regression workbook only to the evidence root;
- never delete/overwrite the real `R语言估计结果_plm估计.xlsx`.

Compare the reproduced aggregate-industry-4 sheets against the existing stored `R语言估计结果_plm估计.xlsx` for all vintages 10–24.

Report exact sheet-by-sheet/cell-level comparison for:

- `总面板回归系数_<itime>_行业4`;
- `总面板回归截距_<itime>_行业4`;
- aggregate grouped-regression sheet if present and comparable.

If latest PLM outputs do not reproduce the stored regression workbook up to ordinary R/Excel floating serialization differences, STOP before corrected HANK with:

`MP4C_LATEST_R_PLM_2009_2023_REPRODUCTION_MISMATCH__HANK_RERUN_NOT_AUTHORIZED`.

If they do reproduce, freeze:

`MP4C_LATEST_R_PLM_2009_2023_REPRODUCIBILITY_VERIFIED`.

This PLM marker alone does not authorize HANK while 2023 capital lineage remains unresolved.

## 8. Phase C — 2023 capital lineage recovery

Existing accepted evidence:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2022_REPRODUCIBILITY_VERIFIED__2023_EXTENSION_PENDING`.

Do not repeat the 713-cell proof unless needed for regression checking.

### 8.1 Search latest-old-PC lineage

Search read-only current recovered/backup roots for any artifact tied to 2023 capital generation, including:

- later R scripts;
- copied/modified `CHNCapitalStock` source;
- saved `asset` objects;
- `.RData` / `.rds`;
- CSV/XLSX staging files;
- investment-price or deflator extensions;
- notes/comments with 2023 capital construction;
- workbook backups/versioned copies.

Hash every candidate.

### 8.2 Reverse-engineer the stored 2023 row only as a forensic diagnostic

From exact recovered `CompK_ZJ` source semantics, derive for every province the implied 2023 real investment/price-index object required to map verified 2022 `K` into the stored 2023 `K` under the frozen recurrence and `delta=0.096`.

Then compare those implied objects against every locally available 2023 source series in the raw/filled workbooks or recovered files.

This step is diagnostic only. A numerical fit must NOT itself authorize an interpolation/smoothing/fill rule.

Explicitly test common possibilities only to classify history, not to invent science, including where mathematically relevant:

- exact direct 2023 source value;
- carry-forward of a 2022 price/deflator;
- linear extrapolation from previous price/deflator observations;
- growth-rate continuation;
- interpolation/smoothing/fill if and only if a local script/note or exact value identity supports it.

Do not accept any candidate merely because it produces positive capital or a close fit.

### 8.3 Source-faithful extension gate

A 2023 capital lineage may be accepted only if one of the following is proven:

A. a later exact historical source/program/data artifact directly reproduces the stored 31-province 2023 row; or

B. the exact `CompK_ZJ` algorithm plus provenance-qualified 2023 inputs with the same definition/unit/price-base semantics reproduces the stored 2023 row, after the standalone implementation is back-validated on 2000–2022 for all 31 provinces.

If neither A nor B is proven, STOP with:

`MP4C_STORED_R_CHNCAPITALSTOCK_2023_LINEAGE_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`.

If A/B reproduces the stored row up to roundoff, classify:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2023_31PROV_REPRODUCIBILITY_VERIFIED__HANK_USE_AUTHORIZED`.

If A/B proves a unique deterministic corrected 2023 row that materially differs from the stored row, classify:

`MP4C_STORED_R_CHNCAPITALSTOCK_2023_DEFECT_IDENTIFIED__SOURCE_FAITHFUL_RECONSTRUCTION_PROVEN__OWNER_A_HANK_USE_AUTHORIZED`.

Do not overwrite the original workbook in either case.

## 9. Model-unit/scaling contract after capital + PLM PASS only

The latest recovered R program itself provides direct source evidence that:

- GDP source units are treated as `亿元` and multiplied by `1000`;
- capital source units are treated consistently with GDP and multiplied by the same `GDP_multiplier=1000`;
- employment/population source units are treated as `万人` and multiplied by `POP_multiplier=100`.

Verify these exact mappings against the current workbook layout and the corrected-2009 same-input parity anchor.

If direct code + 2009 anchor agree, freeze the model input scaling contract.

If they contradict materially, STOP before HANK with:

`MP4C_LATEST_R_MODEL_UNIT_SCALING_CONTRADICTION__HANK_RERUN_NOT_AUTHORIZED`.

## 10. Corrected annual-input construction and 15-year preflight

Only after:

- `MP4C_LATEST_R_PLM_2009_2023_REPRODUCIBILITY_VERIFIED`; and
- verified/source-faithful 2000–2023 capital lineage; and
- unit/scaling PASS,

construct representation:

`OWNER_A_LATEST_R_VERIFIED_CHNCAPITALSTOCK_ROLLING_PLM_END_YEAR_CALENDAR_INPUT`.

For year `Y`:

- technology objects: verified stored/reproduced PLM vintage `Y-1999` / rolling entry `Y-2008`;
- GDP: calendar row `Y-1999`;
- POP: calendar row `Y-1999`;
- CAP: verified 2000–2023 CHNCapitalStock series, year `Y`;
- recompute `log_pgdp` and `log_pcap` from corrected real positive levels;
- preserve province order and all source identities.

Materialize all 15 years with zero Python HANK calls.

Require:

- 2009–2023 exact calendar labels;
- rolling entry 1–15;
- R vintage 10–24;
- level row 10–24;
- 31 provinces exact;
- GDP/POP/CAP finite positive;
- logs real finite;
- technology objects finite/admissible;
- source hashes/scaling exact;
- 2009 corrected input compatible with the formally accepted corrected-2009 same-input anchor.

If all pass:

`MP4C_LATEST_R_VERIFIED_CORRECTED_INPUTS_2009_2023_PREFLIGHT_PASS__8WORKER_BATCH_AUTHORIZED`.

## 11. Exactly 8-worker corrected HANK execution

Upon the full preflight PASS above, Codex is authorized to execute the corrected batch directly.

Use exactly:

- years 2009–2023;
- `Workers=8`;
- year-level parallelism only;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- max outer turns `250`;
- max household calls `7750`;
- automatic reruns `0`;
- no default wall-clock kill.

No MATLAB rerun.
No further R PLM rerun beyond the bounded verification in Section 7.
No shock/IRF/R5/Results.

Use fresh no-overwrite root, preferred:

`D:\ProjectTemp\ch5-mp4c-latest-r-verified-corrected-8worker-20260902-001`.

If any infrastructure/memory/scientific year failure occurs:

- preserve evidence;
- do not rerun automatically;
- do not change workers;
- STOP.

## 12. Closeout

For full annual PASS require:

- 15/15 `SOURCE_CONVERGED`;
- 31/31 household convergence every year;
- complete finite 31×20 terminal outputs;
- Lt matrices and restart checkpoints present and hash-bound;
- corrected input identities and semantic indices exact;
- root aggregate artifacts/hash manifest valid;
- corrected 2009 comparison against accepted same-input anchor passes.

Do not claim blanket 2010–2023 MATLAB–Python parity because legacy MATLAB annual outputs use the rejected `data_year=ii` calendar binding.

Historical 9-hour batch remains:

`LEGACY_CONFLATED_WINDOW_AND_LEVEL_ROW_BATCH__ENGINEERING_CONVERGENCE_ONLY__NOT_FINAL_CALENDAR_YEAR_AUTHORITY`.

## 13. Evidence package

Use fresh evidence root, preferred:

`D:\ProjectTemp\ch5-mp4c-latest-r-plm-2023-capital-forensics-20260902-001`.

Persist at minimum:

- `latest_main_r_identity.json`;
- `latest_vs_prior_main_r_diff.md` if prior copy available;
- `old_pc_path_rebinding_manifest.json`;
- `plm_verifier_source_diff.md`;
- `latest_r_plm_reproduction.xlsx`;
- `latest_r_plm_vs_stored_summary.json`;
- `latest_r_plm_vs_stored_cell_diff.csv`;
- `capital_2023_lineage_search_manifest.json`;
- `capital_2023_implied_input_forensics.csv`;
- `capital_2023_candidate_method_comparison.json`;
- `capital_2023_verification_or_blocker.json`;
- `model_unit_scaling_audit.json` if eligible;
- `corrected_2009_2023_input_preflight.json` if eligible;
- `zero_python_hank_science_ledger.json`;
- `corrected_8worker_build_receipt.json` if batch authorized;
- `batch_execution_receipt.json` if batch executes;
- `closeout_audit.json` if batch completes;
- `manifest.json`.

## 14. Git/report boundary

Do not commit raw/filled workbooks, R package binaries, generated PLM workbook, MAT/NPZ/XLSX/CSV batch outputs or local data.

After final closeout, one bounded commit/push may include only authorized code/tests/contracts and report.

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_LATEST_R_PLM_2023_CAPITAL_LINEAGE_AND_CORRECTED_8WORKER_RERUN_REPORT.md`.

## 15. Terminal classifications

Latest PLM mismatch:

`MP4C_LATEST_R_PLM_2009_2023_REPRODUCTION_MISMATCH__HANK_RERUN_NOT_AUTHORIZED`

Latest PLM verified but 2023 capital still unresolved:

`MP4C_LATEST_R_PLM_VERIFIED__STORED_2023_CAPITAL_LINEAGE_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`

Preflight PASS / batch authorized:

`MP4C_LATEST_R_VERIFIED_CORRECTED_INPUTS_2009_2023_PREFLIGHT_PASS__8WORKER_BATCH_AUTHORIZED`

8-worker execution incomplete:

`MP4C_LATEST_R_VERIFIED_CORRECTED_8WORKER_BATCH_INCOMPLETE__NO_AUTOMATIC_RERUN`

Full success:

`MP4C_LATEST_R_VERIFIED_CHNCAPITALSTOCK_2009_2023_CORRECTED_8WORKER_ANNUAL_STATIONARY_COVERAGE_PASS`

No numerical shock/IRF implementation is authorized in this task.
