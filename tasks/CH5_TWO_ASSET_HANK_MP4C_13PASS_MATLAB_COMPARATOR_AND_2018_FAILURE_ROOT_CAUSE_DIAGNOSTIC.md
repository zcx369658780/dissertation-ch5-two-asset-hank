# CH5_TWO_ASSET_HANK_MP4C_13PASS_MATLAB_COMPARATOR_AND_2018_FAILURE_ROOT_CAUSE_DIAGNOSTIC

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / read-only comparator / failure diagnostician

Owner: final scientific authority

## 1. Authority basis and current state

Immediate predecessor execution:

`390d0eab9feb1f7301c2dfc00acce165ab0060b3`

with terminal:

`MP4C_OWNER_A_2009_2022_CORRECTED_8WORKER_ANNUAL_STATIONARY_COVERAGE_FAILED_STOP_NO_RERUN`

The predecessor established:

- the corrected Owner-A 2009–2022 input preflight passed;
- exact annual scope was 2009–2022, excluding 2023;
- rolling entries were 1–14;
- PLM vintages and calendar rows were 10–23;
- corrected capital came from the independently reproduced 2000–2022 `R语言计算资本存量` segment;
- scaling was GDP ×1000, CAP ×1000, POP ×100;
- 76 focused zero-science tests passed;
- exactly one 14-year, 8-worker scientific batch was launched;
- 13 years returned `PASS`: 2009–2017 and 2019–2022;
- 2018 returned `SHARED_FAIL` / exit `1`;
- no automatic rerun, worker-count change, tolerance/grid/calibration change, MATLAB, PLM, comparator, shock, IRF, R5 or Results action occurred;
- the partial 13/14 batch is not accepted as complete annual coverage.

The Owner now directs the next gate to **first audit the 13 successful annual outputs against all available MATLAB steady-state evidence, then diagnose the 2018 failure, and only after both are understood decide the minimal correction/retry route**.

## 2. Core scientific objective

This is a **comparison-and-diagnostic gate**, not a scientific rerun gate.

The task must answer two questions before any new annual HANK execution is authorized:

1. For the 13 completed Owner-A corrected Python years, how do the provincial steady-state outputs compare with existing MATLAB steady-state artifacts?
2. What exactly caused the 2018 `SHARED_FAIL`, and is it an engineering/orchestration defect, an input/serialization defect, or a scientific/model failure?

Do not hide additional discrepancies behind the 2018 failure. Build one complete issue matrix before proposing a retry.

## 3. Required live continuity

At start:

1. fresh-fetch `origin/main`;
2. require this task live on `main` as direct child of `390d0eab9feb1f7301c2dfc00acce165ab0060b3`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md` and all CURRENT rules it names;
   - predecessor 2009–2022 task and execution report;
   - corrected-2009 same-input MATLAB–Python parity acceptance and comparator evidence;
   - prior MP4C runtime-cache/full-batch reports;
   - prior MATLAB output provenance reports;
   - current Owner-A input adapter, annual production worker, scheduler, launcher and focused tests.

## 4. Frozen scientific boundaries

No new scientific model execution is authorized in this task.

Exact execution budget:

- Python stationary runs: `0`;
- household/HJB/KFE runs: `0`;
- MATLAB model runs: `0`;
- R PLM runs: `0`;
- shock/IRF/R5/Results runs: `0`;
- 2018 retry: `0`.

Allowed:

- read existing Python batch artifacts;
- read existing MATLAB steady-state artifacts;
- run comparator-only Python utilities that perform no HANK/household/HJB/KFE solve;
- parse logs/manifests/checkpoints;
- perform numerical field-by-field comparisons;
- write external evidence and one bounded repository report;
- add narrowly scoped comparator/parser tests if necessary.

## 5. Preserve all existing artifacts

Do not overwrite or delete:

`D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001`

or any earlier batch/evidence root.

The 13 successful years are immutable evidence from the unique first Owner-A 8-worker attempt.

The 2018 partial directory is immutable failure evidence.

## 6. Phase A — audit the 13 Python PASS years first

Exact PASS-year set:

`2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2019, 2020, 2021, 2022`

For each year, read-only verify at minimum:

- `SUCCESS.json` exists and says `SOURCE_CONVERGED`;
- corrected runtime-input SHA matches the input actually consumed;
- representation is the Owner-A corrected representation;
- semantic indices are exact:
  - rolling entry `Y-2008`;
  - PLM vintage `Y-1999`;
  - calendar level row `Y-1999`;
- no 2023 input was consumed;
- worker/thread environment is the frozen BLAS=1 contract;
- 31-province order exact;
- final 31×20 table complete and finite;
- household/checkpoint restart artifact exists and hashes match;
- `Lt_mat` exists, shape/orientation finite and correct;
- year timing and terminal manifests are internally consistent.

Produce one `python_13pass_integrity_audit.json` before any MATLAB comparison.

If any PASS-year artifact is internally inconsistent, classify it as an additional blocker and do not silently exclude it.

## 7. Phase B — locate and classify every existing MATLAB steady-state artifact

Read-only search both protected trees:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23`

and any already-proven MATLAB output roots referenced in repository reports.

Locate and hash where present:

- `Multi_Province_12sts_<year>.mat`;
- historical steady-state workbooks such as `12年稳态值.xlsx`, `12年稳态Ltmat.xlsx`, or current equivalents;
- diagnostic-patch full-state outputs;
- corrected-2009 same-input MATLAB reference artifacts;
- any year-specific `.mat` / workbook / exported table containing provincial steady-state fields.

For every artifact freeze:

- path;
- SHA-256;
- modified time;
- calendar labels;
- fields available;
- province order;
- whether it originates from legacy `data_year=ii` semantics or an independently corrected same-input route;
- whether it is scientifically eligible for strict parity, diagnostic-only comparison, or unusable.

Required classification per artifact/year:

`SAME_INPUT_PARITY_ELIGIBLE`

or

`LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY`

or

`FIELD_SCOPE_LIMITED_DIAGNOSTIC_ONLY`

or

`PROVENANCE_UNRESOLVED_NOT_COMPARABLE`.

Do not relabel a legacy artifact as corrected merely because its filename contains the target year.

## 8. Phase C — two-layer MATLAB/Python comparison

### 8.1 Strict same-input parity layer

For every `SAME_INPUT_PARITY_ELIGIBLE` year/field:

compare Python vs MATLAB exactly using the already accepted comparator conventions.

At minimum report, where fields exist:

- max absolute difference;
- max relative/normalized difference;
- worst province;
- Python value;
- MATLAB value;
- exact/near-exact match count;
- tolerance verdict under the already accepted parity contract.

Corrected-2009 same-input parity MUST be re-read and used as the anchor, not rerun.

Do not loosen tolerances.

### 8.2 Legacy diagnostic layer

For MATLAB artifacts classified `LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY`, comparison is allowed **only as a diagnostic**, never as parity authority.

For overlapping fields, compare:

- province order;
- sign;
- scale;
- ranking/cross-sectional shape where useful;
- raw field differences;
- year-label/input-semantic mismatch.

Clearly label every table/plot/output:

`NOT_SAME_INPUT__NOT_PARITY_EVIDENCE`.

The Owner specifically wants to know whether provincial steady-state values are numerically similar to MATLAB, so report the diagnostic differences transparently, but do not convert them into a scientific equivalence claim.

### 8.3 Required comparison field priorities

Priority 1, if available:

- `Yt0`, `Yt`;
- `Kt0`, `Kt`;
- `Lt0`, `Lt`;
- `Ct`, `At`, `Bt`;
- `ra/rah/rb/w/wjt/tau/Tt/pit`;
- province-level `Lt_mat` elements/aggregates.

Priority 2:

any compatible subset of the Python 31×20 terminal fields.

Never invent MATLAB fields that an artifact does not contain.

## 9. Required 13-year comparison outputs

Create one 13-year matrix containing at minimum:

- year;
- Python status;
- MATLAB artifact identity;
- MATLAB semantic classification;
- fields compared;
- strict-parity eligible yes/no;
- max normalized difference for eligible fields;
- diagnostic max relative difference for legacy-only fields;
- worst field;
- worst province;
- verdict.

Required year-level verdicts:

`STRICT_PARITY_PASS`

or

`STRICT_PARITY_FAIL`

or

`LEGACY_DIAGNOSTIC_SIMILAR`

or

`LEGACY_DIAGNOSTIC_MATERIAL_DIFFERENCE`

or

`NO_COMPATIBLE_MATLAB_REFERENCE`.

Do not collapse these categories.

## 10. Phase D — 2018 failure reconstruction with no rerun

Diagnose 2018 entirely from preserved artifacts and source inspection first.

Read at minimum:

- 2018 corrected runtime input;
- 2018 run manifest;
- root `batch_summary.json/csv` if present;
- launcher/runner stdout/stderr capture if present;
- worker process exit behavior;
- scheduler source;
- annual production worker source;
- any partial files under `year_2018`;
- OS/process/event evidence only if already locally available and non-invasive.

The predecessor says no `FAILURE.json` was written and exact exception was not materialized. Determine why exit `1` became `SHARED_FAIL` without exception persistence.

Required root-cause classification hierarchy:

`2018_SHARED_FAIL_RUNNER_EXCEPTION_CAPTURE_DEFECT`

`2018_SHARED_FAIL_PROCESS_OR_INFRASTRUCTURE_FAILURE`

`2018_SHARED_FAIL_INPUT_SERIALIZATION_OR_IDENTITY_FAILURE`

`2018_SHARED_FAIL_WORKER_PRE_SCIENCE_ENGINEERING_FAILURE`

`2018_SHARED_FAIL_SCIENTIFIC_SOLVER_FAILURE_EVIDENCE_FOUND`

`2018_SHARED_FAIL_ROOT_CAUSE_UNRESOLVED`.

Do not classify as scientific solver failure merely because the subprocess exited 1.

## 11. Reconstruct the missing exception path

Without rerunning 2018, statically trace all exit paths in:

- `mp4c_run_full_annual_batch.py`;
- `mp4c_python_annual_production.py`;
- Owner-A adapter and wrappers.

Prove:

- which exceptions return code 1 vs 2;
- which paths write `FAILURE.json`;
- which paths can terminate before failure serialization;
- whether stdout/stderr were discarded by `subprocess.run`;
- whether the runner's `SHARED_FAIL` classification itself obscures the actual underlying exception.

If an engineering observability defect exists, design the minimum non-scientific patch required to preserve future stderr/traceback/failure classification.

Do NOT apply a patch that changes scientific model behavior.

## 12. Cross-year anomaly scan

Because the Owner wants to address all problems together, inspect the 13 successful years for signs that may predict the 2018 failure or reveal hidden issues:

- outer-turn counts;
- household-call counts;
- convergence margins;
- ra/rah/rb/wage/fiscal/controller boundary hits;
- unusually large/small aggregates;
- runtime outlier status;
- checkpoint size anomalies;
- field extrema;
- province-specific anomalies;
- 2017–2019 discontinuities in corrected empirical inputs and final outputs.

This is read-only diagnostics. Do not alter thresholds or calibration.

Required output:

`cross_year_2009_2022_anomaly_matrix.csv`.

## 13. Integrated issue matrix

Before recommending any retry, build one issue matrix with columns:

- issue_id;
- category;
- year(s);
- evidence;
- scientific vs engineering;
- severity;
- whether it blocks acceptance;
- minimal next action;
- requires Owner scientific decision yes/no.

The matrix must include:

- every MATLAB/Python mismatch that is scientifically meaningful;
- every legacy-only mismatch that is diagnostic but non-authoritative;
- every PASS-year integrity anomaly;
- the 2018 failure root cause or unresolved class;
- observability/logging defects;
- any data/input discontinuity around 2018.

## 14. No retry in this task

Even if the 2018 root cause appears trivial, this task does NOT authorize a second scientific execution.

The purpose is to understand the full issue set first, as requested by Owner.

Do not rerun:

- 2018;
- any other year;
- MATLAB;
- R PLM;
- shock/IRF.

A new live task will authorize the minimal repair and exactly bounded retry after L3 review.

## 15. External evidence package

Use a fresh no-overwrite root, preferred:

`D:\ProjectTemp\ch5-mp4c-13pass-matlab-comparator-2018-diagnostic-20260903-001`

Persist at minimum:

- `python_13pass_integrity_audit.json`;
- `matlab_steady_state_artifact_provenance_map.json`;
- `same_input_parity_comparison_eligible_fields.csv`;
- `legacy_matlab_diagnostic_comparison.csv`;
- `year_level_matlab_python_comparison_matrix.csv`;
- `cross_year_2009_2022_anomaly_matrix.csv`;
- `failure_2018_artifact_inventory.json`;
- `failure_2018_exit_path_trace.json`;
- `failure_2018_root_cause_classification.json`;
- `integrated_issue_matrix.csv`;
- `zero_science_execution_ledger.json`;
- `audit_manifest.json`.

## 16. Repository output and Git boundary

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_13PASS_MATLAB_COMPARATOR_AND_2018_FAILURE_ROOT_CAUSE_DIAGNOSTIC_REPORT.md`

Allowed repository changes:

- the report;
- narrowly scoped comparator/parser/observability tests or utilities only if necessary.

Do not commit generated batch outputs, MATLAB `.mat`, NPZ, XLSX, CSV evidence, local source workbooks or large artifacts.

## 17. Terminal classifications

If all 13 PASS years are internally sound, comparison evidence is complete, and 2018 root cause is identified:

`MP4C_13PASS_MATLAB_COMPARISON_COMPLETE__2018_ROOT_CAUSE_IDENTIFIED__NO_RERUN`

If 13 PASS years reveal a new material scientific blocker:

`MP4C_13PASS_AUDIT_REVEALS_MATERIAL_SCIENTIFIC_BLOCKER__2018_RETRY_NOT_YET_AUTHORIZED`

If MATLAB comparison is limited by incompatible legacy inputs but Python PASS years are internally sound:

`MP4C_13PASS_PYTHON_INTEGRITY_CONFIRMED__MATLAB_REFERENCE_MOSTLY_LEGACY_DIAGNOSTIC__2018_DIAGNOSIS_COMPLETE_OR_PENDING`

If 2018 root cause remains unresolved:

`MP4C_13PASS_COMPARISON_COMPLETE__2018_ROOT_CAUSE_UNRESOLVED__NO_RERUN`

No annual coverage acceptance and no numerical shock/IRF implementation are authorized in this task.
