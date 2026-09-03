# CH5_TWO_ASSET_HANK_MP4C_2018_PRODUCTION_PATH_FAITHFUL_DURABLE_REEXECUTION_AND_TERMINAL_CAPTURE

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / final 2018 production-path-faithful diagnostician

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`c225f3ce3eff4a95236f7b7f9f0f6c814119c222`

with terminal:

`MP4C_2018_DIAGNOSTIC_PRODUCTION_PATH_PARITY_CERTIFIED__PHI_ATTAX_AND_BATCH_SEMANTICS_MATCH_PRODUCTION__ZERO_SCIENCE__READY_FOR_ONE_FINAL_DURABLE_2018_REEXECUTION_TASK`

Accepted predecessor facts:

- the 2018 diagnostic wrapper was audited field-by-field against `validators/multi_province/mp4c_python_annual_production.py`;
- grid, `EconomicParams`, HJB numerics, Owner-A state construction, initial phi allocation, migration wedge, household inputs, post-loop HJB/KFE path, batch fields, one-turn ordering, controller parameters and convergence bounds were classified exact or state-neutral observability differences;
- two material mismatches were repaired in the diagnostic only: per-batch in-place `phi[:]` recomputation from entering `Yt/Lt`, and production-literal `AtTax` from `a_ss`, `rah`, faithful illiquid return, KFE density, and cell weight;
- zero-science focused validation passed `6 passed, 1 warning`, where the warning is the intentional dummy `MatrixRankWarning`;
- no frozen 2018 input, scientific child, stationary/HJB/KFE model execution, MATLAB, R/PLM, shock, or IRF was run in the predecessor;
- the prior 2,015-call no-singularity run is reclassified as non-production-path evidence because it predated the phi/AtTax repair.

This task allocates exactly one final durable 2018 production-path-faithful scientific child.

## 2. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `c225f3ce3eff4a95236f7b7f9f0f6c814119c222`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, all CURRENT rules, the predecessor parity task/report, the current diagnostic, focused tests, annual production worker, faithful HJB/KFE export, post-loop household adapter, Owner-A input adapter, one-turn/stationary/controller code.

## 3. Frozen production-path parity identity

The current diagnostic at predecessor execution has Git blob SHA:

`96f93a42c3ffdd85991c3331df5d934a6890918a`

Path:

`validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`

Before any edit or scientific launch:

- verify the current file content starts from this certified blob/content;
- verify production worker remains unchanged from the predecessor state;
- record Git blob and SHA-256 identities for diagnostic, production worker, faithful HJB/KFE export, household adapter, one-turn, stationary runtime, steady-state controller, Owner-A adapter.

Any unexpected scientific-code drift: STOP before child launch.

## 4. One allowed observability-only addition before execution

The current diagnostic proves singularity capture but discards the returned `ManualSteadyStateResult` on normal completion. For this final run, a normal completion must be auditable without a second scientific run.

Therefore the only pre-execution implementation change allowed is a **diagnostic-only terminal-result persistence addition** that:

- binds the return value of `run_online_stationary(...)` on normal return;
- does not change its arguments, timing, callbacks, model inputs, controller, or call order;
- persists a no-overwrite `normal_completion_summary.json` only after normal return;
- records at minimum:
  - `converged`;
  - `termination_reason`;
  - `iteration_count`;
  - `household_call_count`;
  - final household-converged count;
  - final ra upper/lower counts;
  - final wage upper/lower counts;
  - max final `nk_ratio_gap`;
  - max final `yt_gap`;
  - exact province order;
  - final 31-province state in source-named scalar fields sufficient to reconstruct the existing production `final_31x20` comparison object;
  - if practical, reuse the existing production serializer rather than inventing different field semantics;
  - final summary SHA-256.

This addition is observability only. It must not change any scientific state or result.

Allowed tracked edits before launch are limited to:

- `validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`;
- `tests/test_mp4c_2018_first_singularity_diagnostic.py`.

Production/model files are immutable.

## 5. Mandatory zero-science observability preflight

Before reading the frozen 2018 input, run focused zero-science validation for the new normal-completion persistence path.

Use dummy/synthetic `ManualSteadyStateResult` / `IterationRecord`-compatible objects only; do not call stationary, household, production HJB, production KFE, MATLAB or R/PLM.

The test must prove:

1. normal-result serialization does not invoke model code;
2. result fields are copied without numerical transformation except JSON-safe scalar conversion;
3. `iteration_count` and `household_call_count` are preserved exactly;
4. final diagnostics are persisted exactly;
5. final province order/state length is 31-compatible in the serializer contract;
6. persistence is no-overwrite + flush/fsync;
7. existing phi parity, AtTax parity, batch parity, durable ledgers, raw-capture-before-postmortem, and separate postmortem tests remain passing;
8. scientific call counts remain exactly zero.

At minimum:

`python -m py_compile validators/multi_province/mp4c_2018_first_singularity_diagnostic.py tests/test_mp4c_2018_first_singularity_diagnostic.py`

`python -m pytest -q tests/test_mp4c_2018_first_singularity_diagnostic.py`

If any zero-science preflight fails: STOP. Do not read 2018 input and do not create a scientific PID.

Required preflight marker:

`MP4C_2018_FINAL_TERMINAL_CAPTURE_OBSERVABILITY_CERTIFIED__ZERO_SCIENCE__ONE_CHILD_EXECUTION_AUTHORIZED`

## 6. Frozen 2018 scientific input

Only after the zero-science preflight passes, use the exact preserved Owner-A 2018 input SHA-256:

`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`

Required binding:

- steady-state calendar year = 2018;
- rolling entry = 10;
- regression vintage = 19;
- calendar row = 19;
- rolling window = 2009–2018;
- GDP = `GDP` ×1000;
- CAP = `R语言计算资本存量` ×1000;
- POP = `就业人数` ×100;
- exact 31-province order;
- no 2023 scientific input.

Byte or semantic mismatch: STOP before scientific PID.

## 7. Scientific immutability

Do not change:

- HJB equations or parameters;
- KFE equations or solver;
- grid/state support;
- HJB/KFE tolerances or iteration limits;
- transfer FOC;
- adjustment cost;
- raw-Vb logic;
- illiquid-return taper;
- generator assembly;
- contaminated-row index or RHS `0.007`;
- density normalization;
- household aggregation;
- phi formula/timing/orientation certified in predecessor;
- AtTax formula certified in predecessor;
- migration, capital allocation, firm, wage, monetary or fiscal logic;
- steady-state controller/adaptation/convergence criteria;
- annual input/calendar semantics.

Forbidden:

- pseudoinverse;
- regularization;
- alternate solver;
- matrix perturbation;
- fallback density;
- changed contaminated row;
- parameter/grid/controller edits;
- second scientific child.

## 8. Exactly one durable scientific child

Launch exactly one production-path-faithful 2018 diagnostic child:

- year = 2018;
- scientific-child count = 1;
- worker count = 1;
- subprocess count = 1;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- automatic reruns = 0.

Use a durable local process/session proven not to terminate when a short outer tool call returns.

Persist before/at launch:

- PID;
- exact command;
- Python executable/version;
- cwd;
- thread environment;
- input path/SHA;
- all code identities;
- launch timestamp;
- stdout/stderr paths.

Preferred fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-production-path-faithful-final-durable-reexecution-20260903-001`

If a pre-PID infrastructure action occupies `-001`, preserve it and use the next suffix. Once a scientific PID exists, no second child may be launched under this task.

## 9. Live diagnostic ledgers

Preserve the certified recorder behavior.

Before every household call append + flush + fsync:

- outer iteration;
- province index/name;
- global household-call number;
- `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap`;
- `Yt`, `Lt`, `Kt`, `Zt`, `GovInv`.

After every HJB return append + flush + fsync:

- same context;
- HJB converged flag;
- HJB iterations;
- HJB convergence statistic;
- KFE path classification.

## 10. If the genuine production-path KFE singularity is reproduced

At the first genuine `MatrixRankWarning` or non-finite contaminated-row solve:

1. persist raw evidence first, before heavy analysis:
   - exact context/localization;
   - household inputs and entering macro state;
   - HJB status;
   - operator A;
   - A transpose;
   - contaminated matrix;
   - RHS;
   - raw solve vector if available;
   - warnings;
   - traceback/capture stack;
   - terminal sentinel;
2. flush/fsync;
3. terminate the scientific child fail-closed;
4. after child termination, run only the existing read-only postmortem.

Postmortem must report at minimum:

- operator shape/nnz/finite flags;
- max absolute row-sum residual;
- diagonal/off-diagonal extrema and sign counts;
- zero-outflow and isolated states;
- SCC count;
- closed SCC count/sizes/exact members;
- rank/nullity of A transpose and contaminated matrix;
- tolerance/method;
- smallest singular/eigenvalue diagnostics;
- HJB convergence state at the failing call.

Do not repair anything in this task.

Successful singularity terminal:

`MP4C_2018_PRODUCTION_PATH_FAITHFUL_FIRST_SINGULARITY_CAPTURED__POSTMORTEM_CLASSIFIED_OR_BOUNDED__NO_REPAIR_NO_RETRY`

## 11. If the production-path run completes normally

A normal return from `run_online_stationary` is evidence that the accepted controller returned a converged `ManualSteadyStateResult`; max-iteration failure must not be reclassified as normal completion.

Require:

- child exit 0;
- `normal_completion_summary.json` exists and hashes correctly;
- `converged == true`;
- termination reason equals the accepted converged terminal;
- `household_call_count == 31 * iteration_count`;
- final household-converged count = 31;
- final ra upper count = 0;
- final ra lower count = 0;
- max final KN-ratio gap < `1e-9`;
- max final Y gap < `1e-9`;
- all persisted final state scalars finite;
- no singular raw-evidence artifacts exist;
- no postmortem was run;
- no second scientific run occurred.

Do **not** automatically accept 2009–2022 annual coverage in this task. Preserve the converged final object for L3 review against prior annual evidence.

Successful normal terminal:

`MP4C_2018_PRODUCTION_PATH_FAITHFUL_DURABLE_REEXECUTION_SOURCE_CONVERGED__NO_SINGULARITY__OWNER_ACCEPTANCE_REVIEW_REQUIRED__NO_SECOND_RUN`

## 12. Other failures

If instrumentation/infrastructure fails after scientific PID creation:

`MP4C_2018_PRODUCTION_PATH_FAITHFUL_DURABLE_REEXECUTION_INFRASTRUCTURE_OR_INSTRUMENTATION_FAILED__NO_SECOND_CHILD`

If the stationary controller reaches max iterations or another scientific exception occurs without the target KFE singularity, preserve exact evidence and STOP. Do not retry and do not reinterpret it as singularity or convergence.

## 13. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_PRODUCTION_PATH_FAITHFUL_DURABLE_REEXECUTION_AND_TERMINAL_CAPTURE_REPORT.md`

Report must include:

- authority and direct-parent verification;
- exact changed paths and statement that the change is observability-only;
- zero-science preflight result;
- frozen input identity;
- scientific code identities;
- one-child/PID/thread proof;
- household/HJB ledger counts;
- exact terminal classification;
- if singular: raw/postmortem scientific evidence;
- if normal: full terminal convergence summary and final state evidence;
- explicit no-retry/no-repair/no-shock boundary.

No shock/IRF/Results execution is authorized by this task.