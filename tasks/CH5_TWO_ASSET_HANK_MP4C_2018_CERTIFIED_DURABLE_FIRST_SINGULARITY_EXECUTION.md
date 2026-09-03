# CH5_TWO_ASSET_HANK_MP4C_2018_CERTIFIED_DURABLE_FIRST_SINGULARITY_EXECUTION

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / execution-only 2018 diagnostician

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`ebf8f8d91aebdd940ee285670b30677d5bae487e`

with terminal:

`MP4C_2018_HJB_LEDGER_PHASE_A_CERTIFIED__ZERO_SCIENCE__READY_FOR_ONE_DURABLE_2018_CHILD_TASK`

Accepted predecessor facts:

- the HJB/KFE diagnostic recorder is now zero-science certified;
- `py_compile` passed;
- focused pytest passed `2 passed` with one intentional dummy `MatrixRankWarning`;
- HJB/KFE callable identities are the production MATLAB-faithful exports;
- injected adapter order is exactly `hjb -> kfe -> aggregate -> hjb -> kfe -> aggregate`;
- `DurableCsvLedger` writes one exact CSV header and two durable rows with flush/fsync before dummy KFE entry;
- exact fields `province` and `province_index_0based` are parsed correctly;
- raw first-singularity persistence precedes separate read-only postmortem;
- no frozen 2018 input was read and all scientific calls were zero.

The certified diagnostic script at the predecessor state has GitHub blob SHA:

`fbce4c6d7fc1c38cea5b57566da96d6326f93ef4`

for:

`validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`.

This task allocates **exactly one** new durable 2018 scientific child. It is execution-only: the certified recorder is frozen for this run.

## 2. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `ebf8f8d91aebdd940ee285670b30677d5bae487e`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, all CURRENT rules, predecessor certification report, current diagnostic script, faithful HJB/KFE export, post-loop adapter, Owner-A input adapter, and stationary runtime.

## 3. Execution-only freeze

Before launching any scientific child:

- verify the diagnostic script content is identical to the certified predecessor blob/content; record its SHA-256 and Git blob identity;
- verify no tracked source/test changes are required;
- do **not** edit the diagnostic script, tests, HJB, KFE, adapter, stationary runtime, Owner-A input adapter, model code, calibration, grids, or controllers in this task.

If the certified diagnostic script differs unexpectedly or cannot be used as-is: STOP. Do not consume the scientific-child budget.

No new Phase-A test is required. The certification at `ebf8f8d...` is the gate.

## 4. Frozen 2018 scientific input

Use the exact preserved corrected Owner-A 2018 input with SHA-256:

`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`

Required binding:

- `steady_state_calendar_year = 2018`;
- `rolling_window_entry_index = 10`;
- `regression_vintage_index = 19`;
- `calendar_level_row_index = 19`;
- rolling window `2009–2018`;
- GDP source `GDP`, source-to-model factor ×1000;
- CAP source `R语言计算资本存量`, source-to-model factor ×1000;
- POP source `就业人数`, source-to-model factor ×100;
- exact 31-province order;
- no 2023 scientific input.

Byte mismatch or semantic mismatch: STOP before child launch.

## 5. Scientific immutability

Do not change:

- HJB equations or parameters;
- KFE equations;
- grid or state support;
- HJB/KFE tolerances or iteration limits;
- transfer FOC;
- adjustment cost;
- raw-Vb logic;
- illiquid-return taper;
- generator assembly;
- contaminated-row index;
- RHS `0.007`;
- density normalization;
- household aggregation;
- migration / firm / wage / monetary / fiscal logic;
- outer fixed-point controller;
- annual input or calendar semantics.

Forbidden:

- pseudoinverse;
- regularization;
- matrix perturbation;
- alternate KFE solver;
- fallback density;
- changed contaminated row;
- second scientific child.

## 6. Exactly one durable scientific child

Launch exactly one scientific child with:

- year = 2018;
- worker count = 1;
- subprocess/scientific-child count = 1;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- automatic reruns = 0.

Use a durable local process/session that survives short outer tool-call windows.

Do not use a launch mechanism known to kill the child after ~30 seconds.

Persist before/at launch:

- PID;
- exact command;
- Python executable;
- cwd;
- environment pins;
- input path/SHA;
- diagnostic script hash/blob identity;
- launch timestamp;
- stdout/stderr redirection paths.

Preferred fresh root:

`D:\ProjectTemp\ch5-mp4c-2018-certified-durable-first-singularity-execution-20260903-001`

Fresh no-overwrite root only. If prelaunch infrastructure occupies `-001` without creating a scientific PID, preserve it and move to the next fresh suffix. Once a scientific PID has been created, no second child may be launched under this task.

## 7. Certified live ledgers

Use the certified recorder unchanged.

Before every household call, append + flush + fsync:

- outer iteration;
- province index/name;
- global household-call number;
- `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap`;
- `Yt`, `Lt`, `Kt`, `Zt`, `GovInv`.

After every HJB return, append + flush + fsync:

- same context;
- `hjb.converged`;
- HJB iterations;
- convergence statistic;
- KFE-entry class:
  - `HJB_CONVERGED`, or
  - `MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE`.

## 8. First genuine KFE singularity capture

At the first genuine `MatrixRankWarning` or non-finite contaminated-row solve, the child must immediately persist raw evidence first:

- localization/context;
- household inputs and entering macro state;
- HJB status;
- exact post-HJB operator A;
- A transpose;
- contaminated matrix;
- RHS;
- raw solve vector if available;
- warning records;
- traceback / capture stack;
- terminal sentinel.

Flush/fsync all raw evidence, then fail-closed stop the scientific child.

Do not perform dense SVD, SCC, rank, or other heavy postmortem inside the scientific child before raw evidence is durable.

## 9. Postmortem after child termination

Only after the scientific child has terminated and raw singularity evidence is complete, run the existing read-only postmortem path. No HJB/KFE/stationary/model call is allowed during postmortem.

At minimum report:

### Operator structure

- shape;
- nnz;
- finite-data flags;
- max absolute row-sum residual;
- diagonal extrema;
- off-diagonal extrema;
- positive/negative off-diagonal counts;
- zero-outflow states;
- isolated states.

### Graph structure

- SCC count;
- closed SCC count;
- sizes and exact state members of closed SCCs;
- whether more than one closed communicating class exists.

### Rank/nullity

For A' and contaminated matrix:

- method;
- tolerance;
- rank;
- nullity;
- smallest singular/eigenvalue diagnostics.

Dense 800×800 SVD is allowed in postmortem if practical.

## 10. Root-cause classification

Choose the strongest evidence-supported classification only:

- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_HJB_NONCONVERGED_POSTLOOP_OPERATOR`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_MULTIPLE_CLOSED_COMMUNICATING_CLASSES`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_OPERATOR_RANK_DEFICIENCY_BEYOND_SINGLE_STATIONARY_NULL_DIRECTION`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_GENERATOR_CONSTRUCTION_DEFECT`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_OTHER_CAPTURED_NUMERICAL_PATHOLOGY`
- `2018_KFE_SINGULARITY_ROOT_CAUSE_REMAINS_UNRESOLVED_AFTER_FIRST_EVENT_CAPTURE`

Do not call a MATLAB-faithful convention a defect without source/parity proof.

Do not repair anything in this task.

## 11. If singularity does not recur

If the one 2018 child completes without the singularity:

- preserve its complete result/evidence;
- do not rerun;
- do not automatically accept 2009–2022 coverage;
- terminal:

`2018_FIRST_SINGULARITY_NOT_REPRODUCED_IN_CERTIFIED_DURABLE_EXECUTION__NO_SECOND_RUN`

## 12. If infrastructure fails

If infrastructure/instrumentation fails after the single scientific PID is created:

- preserve all evidence;
- do not launch another child;
- STOP.

If a prelaunch infrastructure failure occurs before any scientific PID is created, it may be corrected only if no tracked scientific/diagnostic code change is needed and the exact certified recorder remains unchanged; otherwise STOP and return for new authority.

## 13. Evidence and report

Persist an auditable evidence root including launch identity, input identity, scientific code identity, live ledgers, raw capture, child terminal sentinel, stdout/stderr, postmortem outputs if applicable, execution receipt, bounded-science ledger, and audit manifest.

Required repository report:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_CERTIFIED_DURABLE_FIRST_SINGULARITY_EXECUTION_REPORT.md`

Expected successful diagnostic terminal:

`MP4C_2018_CERTIFIED_DURABLE_FIRST_SINGULARITY_CAPTURE_COMPLETE__POSTMORTEM_CLASSIFIED_OR_BOUNDED__NO_REPAIR_NO_RETRY`
