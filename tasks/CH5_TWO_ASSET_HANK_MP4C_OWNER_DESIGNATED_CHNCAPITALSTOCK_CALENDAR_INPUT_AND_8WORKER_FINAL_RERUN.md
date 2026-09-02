# CH5_TWO_ASSET_HANK_MP4C_OWNER_DESIGNATED_CHNCAPITALSTOCK_CALENDAR_INPUT_AND_8WORKER_FINAL_RERUN

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / data-provenance verifier / data-binding implementer / controlled batch executor

Owner: final scientific authority

## 1. Revision, supersession, and current scientific decision

This live task supersedes the blocked execution recorded by:

`f4a905bf45a51ccc6433cc5954f39ecc59f37823`

with terminal:

`MP4C_OWNER_A_CAPITAL_PROVENANCE_UNRESOLVED__RERUN_NOT_AUTHORIZED`.

It also revises the immediately preceding version of this same task. The Owner has clarified that MATLAB/R preprocessing had already computed a Zhang-Jun-method provincial capital-stock series and stored it in the **last sheet** of:

`2000年后各省数据_填充NA.xlsx`

under the exact sheet name:

`R语言计算资本存量`

The corresponding upstream/raw workbook is:

`2000年后各省数据.xlsx`

The dissertation documents the Zhang-Jun capital-stock methodology and the use of the R package `CHNCapitalStock` for provincial capital-stock construction.

**Critical revision:** the stored `R语言计算资本存量` sheet is now an **Owner-designated candidate scientific capital series**, but it MUST NOT be treated as final input merely because its values are positive or because its label references R. Before any corrected HANK execution, Codex must independently verify that this stored 2000–2023 × 31-province series is a faithful output of the intended Zhang-Jun / `CHNCapitalStock` construction from the relevant upstream/raw inputs.

Required candidate marker:

`OWNER_DESIGNATES_R语言计算资本存量_AS_CANDIDATE_CHNCAPITALSTOCK_SERIES_PENDING_REPRODUCIBILITY_AUDIT`

Only after the verification gate in Sections 4–7 passes may Codex promote it to:

`OWNER_A_R语言计算资本存量_VERIFIED_AS_INTENDED_CHNCAPITALSTOCK_HANK_CAPITAL_SERIES`

The Owner continues to select intended calendar semantics over the historical MATLAB annual-loop indexing defect.

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

This decision changes annual calendar/data binding only. It does not authorize mutation of HJB/KFE, household equations, one-turn ordering, migration, firm/wage/monetary/fiscal blocks, controllers, calibration, grids, tolerances, convergence thresholds, or the accepted MP4D shock-response semantics.

The corrected-2009 same-input MATLAB–Python parity remains the numerical regression anchor.

## 3. Required live continuity

At execution start:

1. fresh-fetch `origin/main`;
2. require this exact **revised task content** live on `main`;
3. require the revised task commit to be the direct child of the prior task-authority commit `cc5a9c3038b4ddfac32cf76d1a1bc0aca9f47427`;
4. require `HEAD == origin/main`, ahead/behind `0/0`;
5. require a clean tracked worktree;
6. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md` and all CURRENT rules it names;
   - corrected-2009 parity acceptance;
   - prior MP4C scope/data/runtime-cache reports and tasks;
   - the capital-provenance blocker report at `f4a905...`;
   - MP4D source-semantics execution and L3 acceptance reports;
   - current annual adapter/worker/scheduler/tests;
   - dissertation passages documenting the Zhang-Jun / `CHNCapitalStock` capital-stock method.

Do not use chat text as a substitute for the live revised task.

## 4. Phase A0 — exact artifact identity and workbook-structure audit — ZERO HANK SCIENCE

Before reconstructing capital, identify and hash the exact local artifacts actually used.

Read-only inspect at minimum:

- `2000年后各省数据.xlsx`;
- `2000年后各省数据_填充NA.xlsx`;
- `R语言估计结果_plm估计.xlsx`;
- `数据估计结果_1000_100_0.mat`;
- every R script / MATLAB script / helper under the protected project tree that constructs, imports, copies, transforms, or comments on provincial capital stock;
- any locally available `CHNCapitalStock` package source, package metadata, lock/version record, R library installation, saved R workspace, generated CSV/XLSX/MAT artifact, or script invocation relevant to the stored sheet.

Record SHA-256, bytes, modified time where available, workbook sheet order/names, and exact axes.

For both the raw and filled workbooks, enumerate the capital-relevant sheets and source series, including at minimum where present:

- `固定资产投资额`;
- `总资本存量`;
- `R语言计算资本存量`;
- any investment price / deflator / depreciation / base-year / price-base series needed by the Zhang-Jun / `CHNCapitalStock` construction.

Do not mutate any workbook.

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

## 6. Phase A2 — independent reproducibility audit of the Zhang-Jun / CHNCapitalStock output

This is the key new gate requested by the Owner.

### 6.1 Recover the exact intended construction

From dissertation text, local R/package source, scripts, comments, and workbook provenance, determine the exact capital-stock construction used/intended, including as far as recoverable:

- package/function name;
- package version or source identity;
- Zhang-Jun methodological variant implemented;
- required raw input series;
- base year / initial capital rule;
- depreciation assumptions;
- investment-price / deflator treatment;
- nominal-to-real transformation;
- currency unit;
- output price-base;
- province ordering;
- year ordering;
- any NA fill or preprocessing that occurs before capital reconstruction.

Do not silently replace unknown package defaults with generic perpetual-inventory assumptions.

### 6.2 Raw-versus-filled input provenance

Compare `2000年后各省数据.xlsx` with `2000年后各省数据_填充NA.xlsx` for every input that enters the capital reconstruction.

Identify exactly:

- which cells differ;
- which cells were NA/missing originally;
- how those missing values were filled, if the rule is source-recoverable;
- whether the stored `R语言计算资本存量` sheet was generated from raw inputs, filled inputs, or another intermediate representation;
- whether any later manual edit occurred after the R calculation.

If the input lineage cannot be established uniquely, do not claim exact reproducibility.

### 6.3 Bounded independent R reproduction is authorized

The Owner explicitly authorizes a **data-preprocessing verification run only** of the capital-stock construction.

Allowed:

- run local R only to reproduce/verify the `CHNCapitalStock` capital-stock calculation from identified local inputs;
- use an already installed/local package or locally available package source whose identity/version can be recorded;
- execute the minimum deterministic capital reconstruction necessary for the audit;
- write outputs only to a fresh external evidence root.

Forbidden:

- rerun the rolling PLM regressions;
- install/update packages from the internet;
- change package source;
- change package defaults without source evidence;
- run MATLAB HANK;
- run Python stationary/HJB/KFE;
- run shocks/IRFs.

If the exact package/version is unavailable but local source code or a deterministic equivalent script is available, Codex may reproduce the calculation from that exact source and must label it accordingly.

If neither exact package/source nor a uniquely recoverable deterministic reconstruction is available, classify reproducibility as unresolved rather than guessing.

### 6.4 Stored-sheet versus independent-reproduction comparison

Compare the independently reproduced 24×31 capital matrix against the stored `R语言计算资本存量` sheet.

Report at minimum:

- exact-match count;
- maximum absolute difference;
- maximum relative/normalized difference;
- worst year/province/value pair;
- count above numerical roundoff;
- whether discrepancies are explained solely by workbook display/serialization precision;
- whether any discrepancy is economically/materially nontrivial.

If the same package/source and same inputs are reproduced, expect equality up to ordinary floating serialization/roundoff. Do not adopt a loose tolerance merely to force PASS.

Persist both matrices and a cell-level diff table in the external evidence package; do not commit them to GitHub.

## 7. Capital verification classifications

Choose exactly one strongest supported classification **before correcting annual HANK inputs**:

### V1 — verified stored CHNCapitalStock series

Use only if construction lineage and independent reproduction support the stored 24×31 sheet:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2023_31PROV_REPRODUCIBILITY_VERIFIED__HANK_USE_AUTHORIZED`

This promotes:

`R语言计算资本存量`

to the intended capital-stock authority for the corrected annual HANK route.

### V2 — stored sheet contains a correctable deterministic generation/serialization defect

Use only if exact source/package evidence proves a unique deterministic correction and the corrected matrix can be independently reproduced:

`MP4C_STORED_R_CHNCAPITALSTOCK_DEFECT_IDENTIFIED__DETERMINISTIC_RECONSTRUCTION_PROVEN__OWNER_A_HANK_USE_AUTHORIZED`

Do not overwrite the workbook. Use a separately generated, fully provenance-bound corrected capital artifact for Python.

### V3 — unresolved

If package/source/input lineage or numerical reproduction is not unique:

`MP4C_STORED_R_CHNCAPITALSTOCK_REPRODUCIBILITY_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`

STOP before HANK science.

### V4 — stored sheet materially wrong

If independent exact-source reproduction materially contradicts the stored sheet and no uniquely proven corrected artifact exists:

`MP4C_STORED_R_CHNCAPITALSTOCK_MATERIAL_ERROR_CONFIRMED__HANK_RERUN_NOT_AUTHORIZED`

STOP before HANK science and report the precise error map.

## 8. Model-unit/scaling gate after V1/V2 only

Only after V1 or V2, prove the exact conversion from the verified capital series to model-internal `Kt0/Kt/GovInv` units.

Use:

- corrected-2009 same-input parity anchor;
- existing model GDP/population multipliers;
- source unit documentation;
- the verified capital artifact.

Do not invent scaling from magnitude alone.

If exact scaling cannot be deterministically recovered, STOP with:

`MP4C_CHNCAPITALSTOCK_MODEL_UNIT_SCALING_UNRESOLVED__RERUN_NOT_AUTHORIZED`.

## 9. Corrected Owner-A input construction after V1/V2 + scaling PASS only

Use a representation label that explicitly distinguishes intended science from legacy MATLAB annual binding, e.g.:

`OWNER_A_VERIFIED_CHNCAPITALSTOCK_ROLLING_PLM_END_YEAR_CALENDAR_INPUT`

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
- R PLM regressions: `0`;
- Python stationary: `0`;
- Python household/HJB/KFE: `0`;
- comparator: `0`;
- shock/IRF/R5/Results: `0`.

The only newly authorized executable computation before HANK is the bounded R capital-reconstruction verification described in Section 6.3.

## 12. Preflight terminal

If and only if V1 or V2, unit/scaling PASS, corrected 2009 anchor PASS, and all 15 input preflights PASS:

`MP4C_VERIFIED_CHNCAPITALSTOCK_CORRECTED_INPUTS_2009_2023_PREFLIGHT_PASS__8WORKER_BATCH_AUTHORIZED`

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
Do not rerun R PLM estimation.
Do not run shocks/AR(1)/IRF/R5/Results.

Use a fresh no-overwrite batch root, preferred:

`D:\ProjectTemp\ch5-mp4c-owner-a-verified-chncapitalstock-8worker-20260902-001`

Never reuse prior batch roots.

If any infrastructure/memory/scientific year failure occurs:

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

Use a fresh no-overwrite evidence root, preferred:

`D:\ProjectTemp\ch5-mp4c-chncapitalstock-repro-audit-20260902-001`

Persist at minimum:

- `artifact_identity_manifest.json`;
- `raw_vs_filled_capital_input_diff.csv`;
- `chncapitalstock_package_source_and_version.json`;
- `chncapitalstock_method_contract.json`;
- `stored_r_capital_axis_completeness_audit.json`;
- `independent_chncapitalstock_reproduction.csv` if reproducible;
- `stored_vs_reproduced_chncapitalstock_cell_diff.csv` if reproducible;
- `stored_vs_reproduced_chncapitalstock_summary.json`;
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

Do not commit/push raw/filled workbooks, R package binaries, runtime MAT/NPZ/XLSX/CSV outputs, or generated batch data.

After final closeout, one bounded commit/push may include only authorized code/tests/contracts and the required repository report.

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_CHNCAPITALSTOCK_REPRO_AUDIT_AND_CORRECTED_8WORKER_RERUN_REPORT.md`

## 19. Terminal classifications

Capital stored-sheet verified and full rerun succeeds:

`MP4C_VERIFIED_CHNCAPITALSTOCK_2009_2023_CORRECTED_8WORKER_ANNUAL_STATIONARY_COVERAGE_PASS`

Capital reproducibility unresolved:

`MP4C_STORED_R_CHNCAPITALSTOCK_REPRODUCIBILITY_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`

Stored capital materially wrong and no unique reconstruction:

`MP4C_STORED_R_CHNCAPITALSTOCK_MATERIAL_ERROR_CONFIRMED__HANK_RERUN_NOT_AUTHORIZED`

Unit/scaling unresolved:

`MP4C_CHNCAPITALSTOCK_MODEL_UNIT_SCALING_UNRESOLVED__RERUN_NOT_AUTHORIZED`

Corrected 8-worker batch incomplete:

`MP4C_VERIFIED_CHNCAPITALSTOCK_CORRECTED_8WORKER_BATCH_INCOMPLETE__NO_AUTOMATIC_RERUN`

No numerical shock/IRF implementation is authorized in this task.
