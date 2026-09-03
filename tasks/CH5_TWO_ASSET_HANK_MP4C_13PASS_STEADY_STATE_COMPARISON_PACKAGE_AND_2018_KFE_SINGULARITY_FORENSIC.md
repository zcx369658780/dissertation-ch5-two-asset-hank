# CH5_TWO_ASSET_HANK_MP4C_13PASS_STEADY_STATE_COMPARISON_PACKAGE_AND_2018_KFE_SINGULARITY_FORENSIC

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / read-only scientific-output packager / KFE-failure forensic analyst

Owner: final scientific authority

## 1. Authority basis and current scientific decision

Immediate predecessor execution:

`c2c7e70a3f546111d05314f13cd7be16c373c5c7`

with terminal:

`MP4C_2018_OWNER_A_CORRECTED_SINGLE_RETRY_PROCESS_EXCEPTION_FAIL__ROOT_CAUSE_CAPTURED__NO_SECOND_RETRY`

Accepted predecessor findings:

- the single authorized 2018 retry used a byte-identical corrected input with SHA-256 `F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`;
- it used one subprocess / one worker and thread pins `OMP=MKL=OPENBLAS=NUMEXPR=1`;
- stderr captured `MatrixRankWarning: Matrix is exactly singular` followed by `ValueError: faithful contaminated-row solve is non-finite` in the KFE path;
- no second retry was performed;
- the 13 existing PASS years remain immutable and internally sound;
- complete 2009–2022 composite coverage is not accepted because 2018 failed twice;
- no MATLAB/R/PLM/2023/shock/IRF/R5/Results execution occurred.

The Owner now explicitly decides:

`OWNER_DEFERS_ANY_FURTHER_2018_RERUN_OR_KFE_SCIENTIFIC_MUTATION__FIRST_PREPARE_FULL_13PASS_STEADY_STATE_COMPARISON_PACKAGE_AND_2018_FAILURE_FORENSIC`

Therefore this task authorizes **zero new HANK science**. It has two goals only:

1. organize the 13 successful Python annual steady-state outputs into a portable comparison package suitable for independent manual MATLAB/Python comparison by the Owner/L3 reviewer;
2. organize and deepen the read-only forensic evidence around the 2018 contaminated-row KFE singularity, without rerunning or modifying the solver.

## 2. Required live continuity

At start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as direct child of `c2c7e70a3f546111d05314f13cd7be16c373c5c7`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require a clean tracked worktree;
5. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md` and every CURRENT rule it names;
   - Owner-A 2009–2022 execution task/report;
   - 13-pass/MATLAB/2018 diagnostic task/report;
   - 2018 observability-repair/single-retry task/report;
   - corrected-2009 same-input parity acceptance;
   - current Owner-A input adapter;
   - current annual production worker;
   - KFE contaminated-row implementation and all directly called KFE/generator helpers.

## 3. Immutable evidence roots

Treat the following as read-only:

### Original 13-pass / 2018-first-failure batch

`D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001`

Accepted PASS years:

`2009–2017`, `2019–2022`.

### 13-pass / MATLAB / 2018 diagnostic evidence

`D:\ProjectTemp\ch5-mp4c-13pass-matlab-comparator-2018-diagnostic-20260903-001`

### Observable 2018 retry evidence

Preferred successful evidence root from predecessor:

`D:\ProjectTemp\ch5-mp4c-owner-a-2018-observable-single-retry-20260903-002`

Also inspect the predecessor task’s documented evidence root if different and record exact identity.

Do not modify, rename, delete, normalize, regenerate, or overwrite any existing scientific artifact.

## 4. Scientific execution budget

Exact authorized scientific calls:

- Python stationary: `0`;
- household/HJB: `0`;
- KFE: `0`;
- annual one-turn / fixed point: `0`;
- MATLAB model: `0`;
- R/PLM: `0`;
- shock/IRF/R5/Results: `0`;
- 2018 retry: `0`.

Allowed computation is limited to:

- JSON/CSV/XLSX parsing;
- hash computation;
- read-only matrix/table/statistical comparison of already materialized outputs and inputs;
- source-code inspection;
- deterministic packaging/ZIP creation;
- non-model summary statistics on existing artifacts.

## 5. Phase A — build portable Python steady-state package for the 13 PASS years

For exactly these years:

`2009–2017`, `2019–2022`

collect from the immutable original batch root:

- `final_steady_state.json`;
- corrected annual runtime input JSON used by the worker;
- `SUCCESS.json`;
- `run_manifest.json`;
- `checkpoint_manifest.json`;
- year timing where separately materialized;
- optional small text/JSON manifests needed to establish provenance.

Do NOT copy large NPZ/MAT/NPY scientific artifacts into the portable ZIP unless strictly necessary. Their hashes may be recorded instead.

For every copied source file record:

- original absolute path;
- filename;
- year;
- SHA-256;
- byte size;
- artifact type;
- source batch root;
- representation;
- semantic indices;
- status.

### 5.1 Standardized long table

Create:

`python_owner_a_steady_state_2009_2022_13pass_long.csv`

with one row per:

`year × province`

for the 13 PASS years, i.e. exactly `13 × 31 = 403` rows.

Include at minimum:

- `year`;
- `province`;
- all 20 terminal fields from the accepted final table:
  - `Ct`;
  - `At`;
  - `Bt`;
  - `Lt`;
  - `Lt_supply`;
  - `Kt_supply`;
  - `rah`;
  - `Kt`;
  - `Yt`;
  - `mt`;
  - `KNratio`;
  - `w`;
  - `wjt`;
  - `rk`;
  - `ra`;
  - `GovInv`;
  - `rb`;
  - `it`;
  - `Zt`;
  - `Govinc`;
- `runtime_input_sha256`;
- `rolling_window_entry_index`;
- `regression_vintage_index`;
- `calendar_level_row_index`;
- `representation`.

### 5.2 Standardized corrected input-level table

Create:

`python_owner_a_input_levels_2009_2022_13pass_long.csv`

with the same 403 `year × province` rows and, where present in the corrected input, at minimum:

- GDP level used by Python;
- CAP level used by Python;
- POP/employment level used by Python;
- `log_pgdp`;
- `log_pcap`;
- `IND_alpha`;
- `IND_Zt`;
- inter-province capital/asset ratio object used by the Owner-A adapter;
- province index/order;
- semantic indices;
- source workbook/cache SHA identities.

Use the already materialized corrected input JSON. Do not reconstruct scientific input by rerunning R or MATLAB.

### 5.3 Human-readable wide workbook

Create:

`PYTHON_OWNER_A_STEADY_STATE_2009_2022_13PASS.xlsx`

with separate sheets for at least:

- `Yt`;
- `Kt`;
- `Lt`;
- `Ct`;
- `At`;
- `Bt`;
- `ra`;
- `rah`;
- `rb`;
- `w`;
- `wjt`;
- `Zt`;
- `GovInv`;
- `Govinc`.

Recommended layout:

- rows = 31 provinces in accepted common order;
- columns = years `2009–2017`, `2019–2022`;
- explicit gap/absence for 2018, not zero fill;
- no 2023.

Also include a `README` sheet documenting that 2018 is absent because both authorized attempts failed and that 2023 is out of scope.

## 6. Phase B — extract legacy MATLAB steady-state record for diagnostic manual comparison

Locate and hash the existing MATLAB steady-state workbook, expected in the protected/diagnostic MATLAB tree and commonly named:

`12年稳态值.xlsx`

Do not assume the uploaded/chat copy is available to Codex; use the local project copy actually present on disk and record its path/hash.

Read only the existing workbook.

Identify the final complete 31-province block for each relevant sheet and extract at minimum:

- `稳态值_Yt0`;
- `稳态值_Yt`;
- `稳态值_Kt0`;
- `稳态值_Kt`;
- `稳态值_Lt0`;
- `稳态值_Lt`.

For each sheet, prove:

- which rows correspond to the final complete 31-province record;
- province order;
- year columns and year labels;
- any repeated/intermediate write blocks that must not be mistaken for the final record.

Create:

`MATLAB_LEGACY_STEADY_STATE_RECORD_EXTRACT.xlsx`

and CSV extracts:

- `matlab_legacy_Yt_2009_2022.csv`;
- `matlab_legacy_Kt_2009_2022.csv`;
- `matlab_legacy_Lt_2009_2022.csv`;
- `matlab_legacy_Yt0_2009_2022.csv`;
- `matlab_legacy_Kt0_2009_2022.csv`;
- `matlab_legacy_Lt0_2009_2022.csv`.

Important semantic label on every file/sheet:

`LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY__NOT_SAME_INPUT_PARITY_EVIDENCE`

Do not claim that same filename-year means same Owner-A calendar input.

## 7. Phase C — prepare a direct diagnostic MATLAB/Python overlap table

Without claiming strict parity, create:

`matlab_python_legacy_overlap_diagnostic_13pass.csv`

for the 13 PASS Python years and 31 provinces, comparing only directly named overlapping final variables:

- MATLAB `Yt` vs Python `Yt`;
- MATLAB `Kt` vs Python `Kt`;
- MATLAB `Lt` vs Python `Lt`.

For each row include:

- year;
- province;
- variable;
- MATLAB legacy value;
- Python Owner-A value;
- raw difference;
- absolute difference;
- relative difference using a clearly documented denominator;
- ratio `Python / MATLAB` where denominator nonzero;
- semantic label `NOT_SAME_INPUT__DIAGNOSTIC_ONLY`.

Create year-level summary:

`matlab_python_legacy_overlap_diagnostic_summary.csv`

with for each `year × variable`:

- mean absolute difference;
- median absolute difference;
- max absolute difference;
- mean relative difference;
- median relative difference;
- max relative difference;
- Pearson correlation across provinces where finite;
- Spearman rank correlation across provinces where finite;
- worst province;
- MATLAB value;
- Python value.

These statistics are for manual forensic interpretation only. Do not classify them as parity PASS/FAIL.

## 8. Phase D — organize 2018 failure package

Create a dedicated read-only summary package containing:

- original failed 2018 corrected input JSON and SHA;
- observable retry copied input JSON and SHA;
- proof they are byte-identical;
- original run manifest if present;
- retry command/environment receipt;
- retry stdout log;
- retry stderr log;
- retry execution receipt;
- predecessor reports relevant to 2018;
- exact traceback text in a dedicated UTF-8 file;
- exact source path/function/line chain implicated by the traceback.

Create:

`2018_KFE_FAILURE_SUMMARY.md`

that states exactly:

- both 2018 attempts used the same Owner-A scientific input;
- first attempt lost the exception due to observability defect;
- second/observable attempt captured an exactly singular contaminated-row KFE matrix warning and non-finite solve exception;
- this is not ordinary convergence failure;
- no scientific mutation or second retry is authorized here.

## 9. Phase E — read-only KFE singularity forensic analysis

Do not run the model.

Read the exact KFE/generator source implicated by the traceback and document the mathematical meaning of the failing operation.

At minimum determine:

1. which matrix is solved in the faithful contaminated-row stationary KFE route;
2. which row is replaced/contaminated and what normalization constraint is imposed;
3. why this solve is expected to be nonsingular in accepted years;
4. what mathematical conditions can make the contaminated-row system exactly singular (e.g. nullity > 1 / multiple closed communicating classes / reducible generator / disconnected mass blocks), clearly distinguishing general mathematical possibility from proven 2018 evidence;
5. whether the code has any source-faithful fallback or intentionally fail-closed behavior;
6. whether the exception arises before or after the HJB for the failing household/province is reported converged, if recoverable from existing logs only;
7. whether existing stdout/stderr identifies the exact province, outer iteration, household call, or control state at failure.

### 9.1 2018 input-neighbor forensic

Using existing already-materialized inputs only, compare 2018 against 2017 and 2019 for every province and available empirical/model input field:

- GDP;
- CAP;
- POP;
- `log_pgdp`;
- `log_pcap`;
- `IND_alpha`;
- `IND_Zt`;
- inter-province ratio objects;
- any source-calibrated scalar that differs by year.

Create:

`input_2017_2018_2019_neighbor_comparison.csv`

and flag only objective numerical outliers/discontinuities; do not infer causality from a large change alone.

### 9.2 Failing-stage localization

From existing logs and partial artifacts only, identify the strongest supported localization:

- exact province if available;
- exact outer iteration if available;
- exact household call number if available;
- exact KFE helper/function;
- whether HJB convergence for that same call is established;
- whether a generator/matrix artifact was persisted before failure.

If exact province/call cannot be recovered, explicitly mark it `UNKNOWN_FROM_EXISTING_EVIDENCE` rather than guessing.

### 9.3 Root-cause hypothesis matrix

Create:

`2018_kfe_singularity_hypothesis_matrix.csv`

with columns:

- `hypothesis_id`;
- `hypothesis`;
- `mechanism`;
- `evidence_for`;
- `evidence_against`;
- `status` (`SUPPORTED`, `POSSIBLE`, `DISFAVORED`, `UNRESOLVED`);
- `would_require_new_scientific_run_to_test`;
- `minimal_future_test`.

Do not mark a hypothesis `SUPPORTED` unless existing evidence directly supports it.

## 10. Phase F — program-correctness evidence map

Create:

`python_program_correctness_evidence_map.md`

separating clearly:

### Already strong evidence

- household/HJB/KFE MATLAB-faithful parity gates previously accepted;
- corrected-2009 same-input cross-language parity anchor;
- 13 Owner-A years internally converged with complete finite 31×20 results and valid artifacts;
- Owner-A capital 2000–2022 segment independently reproduced from `CHNCapitalStock`;
- calendar/index/scaling contracts are explicit.

### Not yet proven

- strict same-input MATLAB/Python parity for every annual year 2010–2022;
- correctness of 2018 KFE stationary distribution under its current input;
- 2023 data extension;
- numerical shock/IRF results.

### Current 2018 blocker

- exactly singular contaminated-row KFE solve under the frozen 2018 input;
- scientific cause not yet established without further targeted diagnostics.

This document must not overstate “absolute correctness.”

## 11. Portable package

Use a fresh no-overwrite external root, preferred:

`D:\ProjectTemp\ch5-mp4c-manual-steady-state-comparison-package-20260903-001`

Build one portable ZIP:

`CH5_MP4C_MANUAL_COMPARISON_PACKAGE_2009_2022_13PASS_PLUS_2018_FAILURE.zip`

The ZIP should contain only compact review artifacts, not large scientific arrays.

Required contents at minimum:

- `README.md`;
- `python_owner_a_steady_state_2009_2022_13pass_long.csv`;
- `python_owner_a_input_levels_2009_2022_13pass_long.csv`;
- `PYTHON_OWNER_A_STEADY_STATE_2009_2022_13PASS.xlsx`;
- MATLAB extract workbook and six CSVs from Section 6;
- overlap diagnostic CSVs from Section 7;
- all 13 `final_steady_state.json` files organized by year;
- all 13 corrected input JSON files organized by year;
- `2018_KFE_FAILURE_SUMMARY.md`;
- 2018 retry stdout/stderr/receipt and exact traceback extract;
- `input_2017_2018_2019_neighbor_comparison.csv`;
- `2018_kfe_singularity_hypothesis_matrix.csv`;
- `python_program_correctness_evidence_map.md`;
- `package_file_manifest.csv` with SHA-256 and bytes for every ZIP member.

Do not include credentials or unrelated local files.

## 12. Acceptance criteria

PASS only if:

- all 13 Python PASS years are packaged with exact hashes;
- standardized Python long table has exactly 403 rows and all 20 terminal fields finite;
- corrected-input long table has exactly 403 rows and source identities preserved;
- MATLAB workbook extraction is read-only and its final 31-province blocks are explicitly identified;
- overlap diagnostics are clearly labeled non-same-input;
- 2018 failure package contains the captured singular-matrix warning and traceback;
- no new HANK/MATLAB/R/PLM scientific execution occurs;
- portable ZIP and manifest hashes are complete.

Terminal:

`MP4C_13PASS_STEADY_STATE_COMPARISON_PACKAGE_COMPLETE__2018_KFE_SINGULARITY_FORENSIC_COMPLETE__NO_SCIENTIFIC_RERUN`

## 13. Git boundary and report

Do not commit generated ZIP/XLSX/CSV/JSON scientific artifacts or local MATLAB/R/data files.

One bounded final commit/push may include only:

- a small reusable packaging/forensic script if created;
- focused non-scientific tests if created;
- the required repository report.

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_13PASS_STEADY_STATE_COMPARISON_PACKAGE_AND_2018_KFE_SINGULARITY_FORENSIC_REPORT.md`

No 2018 scientific retry, KFE scientific mutation, MATLAB run, PLM run, 2023, shock/IRF/R5/Results is authorized.
