# CH5_TWO_ASSET_HANK_MP4C_2018_DURABLE_CAPTURE_PROCESS_AND_POSTMORTEM_ANALYSIS

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / diagnostic-execution engineer / postmortem analyst

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`7f89498a0398dc9a0c14b38f3851c72ed93b612f`

with terminal:

`MP4C_2018_FIRST_SINGULARITY_CAPTURE_INFRASTRUCTURE_INTERRUPTED__NO_RETRY`

Accepted predecessor facts:

- Phase-A fixture/wiring validation passed with zero scientific calls;
- production MATLAB-faithful HJB/KFE callable identities are correctly bound;
- the authorized 2018 diagnostic subprocess used the exact frozen Owner-A 2018 input;
- six pre-call ledger records were persisted before the execution environment terminated the process after about 30 seconds;
- no HJB-return/KFE-singularity/operator evidence was durably completed;
- the interruption produced no scientific conclusion;
- no second run, scientific mutation, parameter/grid/input change, fallback, or repair occurred.

This is an execution-orchestration blocker, not a scientific blocker. L3 authorizes one durable diagnostic execution under the standing bounded debugging delegation.

## 2. Purpose

Make the already-validated 2018 first-singularity diagnostic durable against short command/tool execution windows, without altering any scientific model behavior.

The task has exactly three stages:

1. harden only the diagnostic execution/capture path so the child scientific process can run to the first singularity without being killed by a ~30-second orchestration timeout;
2. execute exactly one 2018 diagnostic child using the frozen scientific input and unchanged scientific model code;
3. after the child has terminated, perform read-only postmortem SCC/rank/nullity analysis on captured matrices.

No solver repair is authorized.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this task live on `origin/main` as direct child of `7f89498a0398dc9a0c14b38f3851c72ed93b612f`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, all CURRENT rules, and the three preceding 2018 diagnostic reports/tasks.

## 4. Reuse accepted Phase-A result

Do not relitigate the already-passed fixture/wiring result unless code changes invalidate it.

Accepted marker from predecessor:

`MP4C_2018_PHASE_A_DIAGNOSTIC_FIXTURE_REPAIR_PASS__ONE_FIRST_SINGULARITY_CAPTURE_EXECUTION_AUTHORIZED`

If diagnostic code is changed only in orchestration/capture persistence and the HJB/KFE callable bindings remain untouched, run only focused zero-science regression tests necessary to prove the new persistence behavior.

Scientific calls in these tests remain zero.

## 5. Frozen 2018 scientific contract

Use exact Owner-A 2018 input SHA-256:

`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`

Binding:

- steady-state year 2018;
- rolling entry 10;
- PLM vintage 19;
- calendar row 19;
- rolling window 2009–2018;
- GDP source `GDP` ×1000;
- CAP source `R语言计算资本存量` ×1000;
- POP source `就业人数` ×100;
- exact 31-province axis;
- no 2023 scientific input.

Any byte/input difference: STOP.

## 6. Scientific immutability

Do not change:

- HJB equations/parameters;
- KFE equations;
- HJB/KFE tolerances or iteration limits;
- grids;
- policy/upwind selection;
- transfer FOC;
- adjustment cost;
- raw-Vb logic;
- illiquid-return taper;
- generator assembly;
- contaminated-row index, RHS, or normalization;
- household aggregation;
- migration/firm/wage/monetary/fiscal blocks;
- outer controllers;
- annual input values or provenance.

Forbidden: pseudoinverse, regularization, alternate KFE solver, fallback density, changed row/RHS, second scientific run.

## 7. Capture-first instrumentation rule

The scientific child must minimize work done after the first singularity is detected.

At first genuine KFE singularity / non-finite contaminated-row solve:

1. persist context/HJB status immediately;
2. persist raw sparse matrices/arrays immediately:
   - operator A;
   - A transpose;
   - contaminated matrix;
   - RHS;
   - raw solve vector if available;
3. persist warning/traceback receipt immediately;
4. flush/fsync where applicable;
5. terminate the scientific child fail-closed.

Do **not** perform dense SVD, SCC analysis, or expensive postmortem computation inside the scientific child before the raw evidence is durable.

All SCC/rank/nullity analysis occurs only after the child has terminated, as a read-only postmortem stage.

## 8. Durable execution requirement

The prior failure was caused by the orchestration environment ending a process after ~30 seconds. Do not repeat that launch method.

Use one of the following, preferring the simplest supported local mechanism:

### Option A — explicit long-lived command/session

Run the child in a persistent terminal/session with an explicit execution timeout comfortably above expected diagnostic duration (minimum 30 minutes, preferably 60 minutes), and wait for natural child termination.

### Option B — detached local child with durable PID/receipt

If the invoking tool cannot hold a >30-second command:

- launch exactly one local child process detached from the short tool call;
- redirect stdout/stderr directly to files in the fresh evidence root;
- persist PID, command, environment, input SHA, launch timestamp;
- poll only process status / terminal sentinel at reasonable intervals;
- do not launch another scientific child while that PID is alive;
- after the child terminates, verify exit status/sentinel and continue postmortem analysis.

The detached execution is still exactly one scientific run, not a retry.

Do not use shell/job semantics that silently kill the child when the parent tool call returns.

## 9. Exactly one scientific diagnostic execution

After all preflight gates pass:

- year = 2018 only;
- scientific child process count = 1;
- worker count = 1;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- automatic reruns = 0;
- no wall-clock scientific kill shorter than 30 minutes.

Preferred fresh root:

`D:\ProjectTemp\ch5-mp4c-2018-durable-first-singularity-capture-20260903-001`

No overwrite/reuse of prior roots.

## 10. Required live ledgers

Before each household call, append and flush:

- outer iteration;
- province index/name;
- global household-call number;
- `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap`;
- `Yt`, `Lt`, `Kt`, `Zt`, `GovInv`.

After each HJB return, append and flush:

- same context;
- `hjb.converged`;
- HJB iterations;
- convergence statistic;
- KFE-entry class:
  - `HJB_CONVERGED`, or
  - `MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE`.

These ledgers must be durable independently of final process completion.

## 11. Postmortem analysis after child termination

If first singularity raw evidence exists, compute read-only:

### Operator structure

- shape;
- nnz;
- finite-data flag;
- max absolute row sum of A;
- diagonal min/max;
- off-diagonal min/max;
- positive/negative off-diagonal counts;
- zero-outflow and isolated state indices.

### Graph/SCC

Using a documented threshold:

- SCC count;
- closed SCC count;
- sizes and state members of every closed SCC;
- whether multiple closed communicating classes exist.

### Rank/nullity

For A' and contaminated matrix:

- reproducible rank method;
- tolerance;
- rank;
- nullity;
- smallest singular/eigenvalue diagnostics.

Dense 800×800 SVD is permitted in postmortem if practical. It must not delay raw scientific evidence persistence.

## 12. Root-cause classification

Choose strongest evidence-supported class:

- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_HJB_NONCONVERGED_POSTLOOP_OPERATOR`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_MULTIPLE_CLOSED_COMMUNICATING_CLASSES`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_OPERATOR_RANK_DEFICIENCY_BEYOND_SINGLE_STATIONARY_NULL_DIRECTION`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_GENERATOR_CONSTRUCTION_DEFECT`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_OTHER_CAPTURED_NUMERICAL_PATHOLOGY`
- `2018_KFE_SINGULARITY_ROOT_CAUSE_REMAINS_UNRESOLVED_AFTER_FIRST_EVENT_CAPTURE`

Do not label a MATLAB-faithful convention a defect without source/parity proof.

## 13. If singularity does not recur

If 2018 completes without singularity:

- preserve the result;
- do not rerun;
- do not automatically accept 14-year coverage.

Terminal:

`2018_FIRST_SINGULARITY_NOT_REPRODUCED_IN_DURABLE_CAPTURE_RUN__NO_SECOND_RUN`

## 14. Required evidence

Persist at minimum:

- `durable_execution_preflight.json`;
- `scientific_code_identity_manifest.json`;
- `input_2018_identity.json`;
- `diagnostic_child_launch_receipt.json`;
- `household_call_ledger.csv`;
- `hjb_return_ledger.csv`;
- raw first-singularity matrices/arrays if captured;
- `first_singularity_localization.json`;
- `first_singularity_hjb_status.json`;
- `first_singularity_warning_and_traceback.txt`;
- `postmortem_operator_summary.json`;
- `postmortem_scc_closed_classes.json`;
- `postmortem_rank_nullity.json`;
- stdout/stderr;
- child exit/sentinel receipt;
- bounded-science ledger;
- audit manifest.

## 15. Stop / retry rule

This task authorizes exactly one new scientific 2018 diagnostic child.

If it is interrupted again for infrastructure reasons:

- do not launch a second child;
- preserve evidence;
- classify infrastructure failure;
- STOP.

If singularity is captured:

- no scientific repair in this task;
- STOP after postmortem analysis/report.

## 16. Report

Required repository report:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_DURABLE_CAPTURE_PROCESS_AND_POSTMORTEM_ANALYSIS_REPORT.md`

Expected successful diagnostic terminal:

`MP4C_2018_DURABLE_FIRST_SINGULARITY_CAPTURE_COMPLETE__POSTMORTEM_CLASSIFIED_OR_BOUNDED__NO_REPAIR_NO_RETRY`
