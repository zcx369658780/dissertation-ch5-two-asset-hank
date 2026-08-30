# CH5_TWO_ASSET_HANK_MP4B_PYTHON_DIRECT_SCRIPT_BOOTSTRAP_REPAIR_AND_PYTHON_ONLY_CALENDAR2009_STATIONARY_COMPARISON

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / Python validation-entry repairer / Python-only stationary executor / preserved-MATLAB comparator

Owner: final scientific authority

## 1. Purpose

Repair only the Python validation-entry direct-script bootstrap defect that blocked the first two-language calendar-2009 stationary comparison **after the corrected MATLAB route had already completed successfully**.

Then:

1. prove the repaired Python entry can be invoked by the exact direct-script command form with **zero scientific/model calls**;
2. re-establish the frozen calendar-2009 presolver identity;
3. verify and preserve the already completed MATLAB calendar-2009 run as immutable comparison evidence;
4. execute **one Python-only** corrected calendar-2009 stationary top-level invocation maximum;
5. compare the maximum available Python result against the preserved MATLAB result and the already frozen MP4B comparison contract;
6. do not rerun MATLAB.

Prior terminal:

`MP4B_FRESH_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_BLOCKED`

Prior report/implementation commit:

`92379b704f74ecb13eaedc0f080a71132882efe8`

Prior first divergence:

`PYTHON_DIRECT_SCRIPT_BOOTSTRAP_BEFORE_MODEL_ENTRY`

Observed exception:

`ModuleNotFoundError: No module named 'exports'`

The prior MATLAB scientific result is valid preserved execution evidence. It MUST NOT be rerun or replaced in this task.

## 2. Controlling authority

Read in full and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
- `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- all Owner MP4 decision/adjudication documents;
- accepted MP4A2 report;
- all prior MP4B task authorities and reports;
- `docs/CH5_TWO_ASSET_HANK_MP4B_FRESH_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_EXECUTION_REPORT.md`;
- `validators/multi_province/mp4b_comparison_contract.json`;
- `validators/multi_province/mp4b_fresh_scientific_preflight.json`.

Preserve all accepted contracts, including:

- `OWNER_SINGLE_ACTIVE_CODEBASE_TWO_ASSET_HANK_ONLY`;
- corrected calendar-2009 identity;
- canonical input SHA `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`;
- `MP4B_LOGICAL_PHYSICAL_PATH_EQUIVALENCE_SMOKE_PASS`;
- `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS` as prior evidence, to be freshly rechecked here;
- accepted standalone HA oracle SHA `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`;
- accepted MP2 and MP3 arithmetic/controller semantics;
- `OWNER_PARITY_MISMATCH_BOUNDED_ROOT_CAUSE_DIAGNOSIS_AUTHORIZED`.

Primary reconstruction authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

## 3. Live continuity

Expected execution-start parent / prior blocked implementation commit:

`92379b704f74ecb13eaedc0f080a71132882efe8`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is live on `main` as a direct child of the prior blocked commit;
3. require a clean worktree;
4. verify all controlling-rule blobs are unchanged;
5. verify protected MATLAB hashes, accepted household oracle, MP2, MP3, MP4A2 annual binding, `stationary_runtime.py`, current Python empirical entry and comparison-contract identities;
6. verify the canonical 2009 artifact still exists locally at the accepted no-overwrite root and has the accepted SHA;
7. verify no historical `chapter5_model` runtime dependency exists.

If continuity or authority identity fails, stop before any scientific execution.

## 4. Preserved MATLAB comparison authority — no rerun

The following already completed corrected calendar-2009 MATLAB run is immutable evidence for this task:

Run root:

`D:\ProjectTemp\ch5-mp4b-fresh-calendar2009-matlab-20260830-001`

Required preserved identities:

- stationary output SHA-256: `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B`;
- profile SHA-256: `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C`;
- terminal JSON SHA-256: `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270`;
- terminal status: `COMPLETED`;
- outer turns: `184`;
- household HJB/KFE calls: `5704 = 184 * 31`;
- final household convergence flags: `31/31` true.

Before repairing or running Python, re-hash these preserved artifacts. If any required identity differs, stop BLOCKED. Do not regenerate them.

The preserved MATLAB result may be read and summarized non-destructively. It may not be modified, moved, renamed, overwritten, or rerun.

## 5. Python direct-script bootstrap root cause and bounded repair

Current validation entry:

`validators/multi_province/mp4b_python_empirical.py`

The file is invoked directly, e.g.:

```text
python validators/multi_province/mp4b_python_empirical.py <canonical-json> <fresh-run-root>
```

In direct-file execution, Python places the script directory rather than repository root on `sys.path`. The entry imports:

- `exports.matlab_faithful_two_asset_ha` from repository root;
- `ch5_two_asset_hank...` from repository `src/` layout.

`pyproject.toml` only gives pytest `pythonpath = ["src"]`; that pytest configuration is not a direct-script bootstrap contract.

### 5.1 Mandatory bootstrap audit

Before coding, audit the entry's repository-local imports and classify every required import root.

At minimum establish:

- repository root is required for `exports/matlab_faithful_two_asset_ha.py`;
- repository `src` root is required for `ch5_two_asset_hank` unless the active environment independently installs the package;
- validator/test roots are not scientific runtime dependencies;
- no legacy one-asset path may be added.

Required marker:

`MP4B_PYTHON_DIRECT_SCRIPT_BOOTSTRAP_SCOPE_COMPLETE`

### 5.2 Authorized repair

Repair only the validation entry/bootstrap layer. A preferred auditable pattern is:

```python
REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
```

and an explicit finite bootstrap of only those repository-local roots before repository-local imports.

The implementation may differ if it is more robust, but it MUST:

- derive paths from `__file__`, not current working directory;
- add only the exact current repository root and current `src` root needed by the accepted code;
- fail closed if expected repository files/roots are missing;
- verify the accepted standalone oracle file identity before scientific execution;
- not read or import historical R5;
- not introduce hidden user/site-package fallbacks as scientific authority;
- not modify accepted oracle or `src/ch5_two_asset_hank` scientific arithmetic;
- not execute a model merely by import.

Do not solve this by requiring an ad hoc shell `PYTHONPATH` that is absent from the stored validation entry. The direct-script entry itself must have an auditable, reproducible bootstrap contract.

## 6. Mandatory zero-model direct-invocation smoke

Static import tests were insufficient previously. This task MUST test the **exact direct-script process boundary** before the scientific call.

Add a validation-only mode such as `--bootstrap-check` (or an equivalently explicit no-model mode) to the Python entry.

The direct-invocation smoke MUST:

- launch the entry in a fresh subprocess using the same Python executable and direct-file invocation style intended for the scientific run;
- derive/import the exact repository root and `src` root;
- verify the resolved `exports.matlab_faithful_two_asset_ha` file is exactly the accepted current-repository oracle;
- verify the resolved `ch5_two_asset_hank` package is under the current repository `src` root;
- verify no `chapter5_model` or historical R5 import/path;
- report `scientific_model_calls = 0`;
- create at most one small timestamped/no-overwrite bootstrap manifest.

It MUST NOT call:

- `solve_household_steady_state`;
- HJB/KFE;
- `run_online_stationary`;
- MP2 one-turn;
- any MATLAB model;
- any scientific solver.

Required marker:

`MP4B_PYTHON_DIRECT_SCRIPT_BOOTSTRAP_SMOKE_PASS`

If this smoke fails, stop BLOCKED and consume zero Python scientific calls.

## 7. Static review and regression gate

Before the direct smoke and scientific run:

- Python compile: PASS;
- focused direct-entry tests must execute the exact subprocess bootstrap mode, not only import the module under pytest;
- existing MP3/online controller exact regression must still PASS on all seven scenarios;
- accepted household/oracle, MP2, MP3 and `stationary_runtime.py` identities must remain unchanged unless this task identifies a **pure bootstrap/interface** defect before science;
- no model execution on import;
- no-overwrite behavior preserved;
- no unsafe absolute developer-specific repository path hard-coded into source;
- `git diff --check` PASS.

Required marker:

`MP4B_PYTHON_BOOTSTRAP_REPAIR_STATIC_AND_DIRECT_SMOKE_REVIEW_PASS`

## 8. Fresh presolver identity revalidation

After bootstrap smoke PASS, re-establish the complete calendar-2009 presolver semantic identity without rerunning MATLAB science.

Use the accepted canonical input and already source-bound prepared-state contract. Re-hash/re-read the preserved MATLAB presolver evidence as needed and generate a fresh Python-side presolver comparison artifact only if required.

Require:

`MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

with semantic mismatch count exactly `0`.

Frozen identity remains:

- calendar year `2009`;
- analysis index `1`;
- workbook numeric row `10`;
- physical Excel row `11`;
- `data_MAT_index=1`;
- output year `2009`;
- regression key `10`;
- fixed-2020 `IND_Zt` as source numerical initialization anchor only;
- canonical SHA `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.

## 9. Scientific execution budget — Python only

### MATLAB

- corrected calendar-2009 stationary scientific invocation: **0**.
- wrong-year route: **0**.
- MATLAB scientific rerun of any kind: **0**.

The preserved MATLAB result is the comparison baseline.

### Python

After Sections 6-8 PASS:

- corrected calendar-2009 Python stationary top-level invocation: **maximum 1**.
- scientific rerun: **0**.

Internal household solves are part of the single top-level Python invocation and remain bounded by source controller semantics: 31 households per outer turn, maximum 500 turns.

If the Python scientific invocation fails or nonconverges after model entry, persist the outcome and stop. Do not repair or rerun in this task.

Forbidden scientific calls remain zero:

- MATLAB stationary rerun;
- legacy wrong-year MATLAB;
- 2010-2023 batch;
- shocks/AR1;
- transition/genuine dynamics/IRF;
- historical one-asset R5;
- Results/manuscript claims.

## 10. Python run-root and evidence contract

Use one fresh timestamped no-overwrite Python run root distinct from the failed intended root and every previous run root.

Persist at minimum:

- bootstrap/source/environment manifest;
- canonical input identity;
- Python terminal summary;
- household-call count;
- outer-turn/iteration count;
- convergence/termination status;
- per-turn household input/output files already defined by the entry where successfully produced;
- controller history/final state as already designed;
- warnings/errors if any;
- output artifact hashes.

Do not commit large scientific outputs to GitHub. Commit text-first report/manifests/hashes only.

## 11. Comparison against preserved MATLAB result

If Python produces scientific output, compare it against the preserved MATLAB run without rerunning MATLAB.

Use the existing pre-science contract:

`validators/multi_province/mp4b_comparison_contract.json`

Its frozen rules remain controlling; no post-hoc tolerance loosening.

### 11.1 Maximum available comparison

Compare all objects available from both preserved routes. At minimum attempt final/provincial comparison for source-relevant objects present in MATLAB `st` and Python final state, including where available:

- convergence/termination;
- iteration/outer-turn count;
- provincial `Ct`, `At`, `Bt`, household `Lt`, `AtTax`, household convergence;
- `Yt`, `Kt`, `Lt`, `wjt`, `rk`, `ra`, `Govinc`;
- composite `w`, `rb`, `rah`;
- province boundary/clipping status;
- national `Ct`, `At`, `Bt`, `Yt` and other source-defined totals/diagnostics;
- cross-province ranking/order where economically meaningful.

The already preserved MATLAB descriptive anchors include:

- `sum Ct = 283.3909431582526`;
- `sum At = 47.95553248807161`;
- `sum Bt = 65.2831672243048`;
- `sum Yt = 350556701.89460325`;
- final wage-bound upper/lower counts `7 / 17`.

These are comparison anchors only, not Results claims.

### 11.2 MATLAB output extraction

Non-scientific read-only extraction of the preserved MATLAB `.mat` result is allowed if needed to expose final comparison fields.

Such extraction MUST:

- load only the preserved output artifact;
- not invoke protected model functions or any solver;
- not modify the preserved artifact;
- write only to a fresh no-overwrite comparison/extraction root;
- record extraction helper/script/hash if a helper is created;
- be classified as evidence extraction, not a MATLAB scientific run.

Do not rerun MATLAB for missing traces. If the preserved run lacks a field/iteration history, report it as unavailable.

## 12. Comparison hierarchy and diagnosis

Use this hierarchy:

1. preserved/fresh input identity;
2. Python bootstrap/process identity;
3. Python household execution/termination;
4. final household/province objects available in both languages;
5. outer/final state objects;
6. national aggregates;
7. categorical convergence, clipping/boundary, and ranking diagnostics.

Because the preserved MATLAB run does not necessarily contain a full per-turn observability trace, do not invent layer-by-layer evidence that is absent.

If a material mismatch is visible but the preserved MATLAB evidence is insufficient to localize its first upstream numerical source, classify the mismatch as **observability-limited** and recommend a separately authorized observability-only diagnostic gate. Do not rerun MATLAB in this task.

Allowed scientific root-cause classes, when evidence supports them:

- `PYTHON_IMPLEMENTATION_ERROR`;
- `MATLAB_SOURCE_OR_LEGACY_NUMERICAL_BEHAVIOR`;
- `DATA_OR_CALIBRATION_PROVENANCE_MISMATCH`;
- `SHARED_SOURCE_NUMERICAL_PROPAGATION_DIFFERENCE`;
- `SCIENTIFIC_SPECIFICATION_OR_PROVENANCE_AMBIGUITY`.

No automatic scientific repair or rerun.

## 13. Terminal semantics

If bootstrap/static/presolver fails before Python science:

`MP4B_PYTHON_BOOTSTRAP_REPAIR_AND_PYTHON_ONLY_CALENDAR2009_COMPARISON_BLOCKED`

If the Python scientific invocation fails/nonconverges and no accepted two-route stationary comparison can be completed:

`MP4B_PYTHON_ONLY_CALENDAR2009_STATIONARY_SCIENTIFIC_FAILURE`

If Python completes and the preserved-MATLAB comparison package is successfully generated, use:

`MP4B_PYTHON_ONLY_CALENDAR2009_STATIONARY_COMPARISON_COMPLETE__L3_ACCEPTANCE_PENDING`

Do **not** claim final stationary parity PASS merely because both languages converge. L3 must independently review the actual numerical/categorical comparison before freezing MP4 stationary acceptance.

## 14. Allowed repository changes

Authorized writes are limited to:

- bounded bootstrap/direct-invocation repair to `validators/multi_province/mp4b_python_empirical.py`;
- focused bootstrap/direct-process tests;
- one small bootstrap/preflight validator/manifest schema if needed;
- read-only preserved-MATLAB output extraction/comparison helper(s) under `validators/multi_province/` only if needed;
- bounded comparison helper/report support;
- CURRENT roadmap status update;
- one new report:

`docs/CH5_TWO_ASSET_HANK_MP4B_PYTHON_BOOTSTRAP_REPAIR_AND_PYTHON_ONLY_CALENDAR2009_STATIONARY_COMPARISON_REPORT.md`

Do not modify:

- protected MATLAB source;
- accepted household/HJB/KFE/oracle arithmetic;
- MP2 arithmetic;
- MP3 controller semantics;
- MP4A2 annual scientific input logic;
- canonical 2009 input;
- primary workbooks/regression/distance/cache;
- historical R5;
- controlling rule files;
- preserved MATLAB scientific run artifacts.

Do not commit raw/private data, scientific MAT outputs, large logs, figures, caches, or secrets.

## 15. Required report

Include at minimum:

1. terminal verdict;
2. live continuity;
3. prior MATLAB scientific run identity and hash verification;
4. direct-script bootstrap root-cause audit;
5. complete repository-local import-root table;
6. exact bootstrap repair diff;
7. static review marker;
8. exact direct-subprocess bootstrap smoke command and manifest/hash;
9. proof of zero scientific calls during bootstrap smoke;
10. fresh presolver equality and mismatch count;
11. Python-only scientific call ledger;
12. Python run root and artifact hashes;
13. Python household-call count;
14. Python outer-turn count and convergence/termination;
15. preserved MATLAB versus Python comparison table;
16. absolute/relative/normalized differences as required by the frozen comparison contract;
17. categorical convergence/boundary/ranking comparison;
18. first supported divergence/root-cause classification, or observability limitation;
19. unavailable preserved-MATLAB fields/traces list;
20. material mismatch/unresolved/environment failure lists;
21. tests/checks;
22. forbidden-operation check;
23. Git closeout;
24. exactly one recommended next gate.

## 16. Next-stage boundary

Even if comparison looks good, this task does not authorize MP5/shocks, 2010-2023 batch, transition/dynamics, or Results.

After `...COMPARISON_COMPLETE__L3_ACCEPTANCE_PENDING`, stop for ChatGPT L3 review.

On BLOCKED or SCIENTIFIC_FAILURE, recommend exactly one bounded successor addressing the localized cause only.

## 17. Closeout

Use explicit-path staging only. One execution commit. One non-force push. GitHub read-back every changed path. Require `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree.
