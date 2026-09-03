# CH5_TWO_ASSET_HANK_MP4C_2018_FIRST_SINGULARITY_GENERATOR_DIAGNOSTIC

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / diagnostic-instrumentation implementer / single-run scientific diagnostician

Owner: final scientific authority

## 1. Authority basis and accepted route update

Immediate predecessor execution:

`10dade76d0c694c511955226242b8d9f041eccc9`

Accepted predecessor findings:

- MATLAB runtime model-unit scaling is exactly GDP ×1000, CAP ×1000, POP ×100;
- Python Owner-A uses the same scale factors and directions;
- no hidden second scaling exists;
- CAP/POP source-field differences remain provenance differences, not unit-scaling defects;
- the legacy MATLAB annual route contains a calendar-binding defect: rolling PLM entry/vintage and annual level-data row were conflated;
- Owner-A Python corrected route intentionally uses rolling PLM window ending in year Y while binding GDP/CAP/POP levels to calendar year Y;
- 13 Owner-A years (`2009–2017`, `2019–2022`) previously reached `SOURCE_CONVERGED` with internally consistent 31×20 outputs;
- 2018 failed twice under byte-identical corrected input with `MatrixRankWarning: Matrix is exactly singular` followed by `ValueError: faithful contaminated-row solve is non-finite`;
- the 2018 failure is not explained by a missing or inverted 1000/100 runtime multiplier.

The Owner now authorizes resuming 2018 investigation with a narrow objective: capture the **first singular KFE event** with enough state/generator evidence to determine whether the failure comes from a nonconverged HJB post-loop operator, a reducible/conventionally singular Markov generator, or another identifiable local mechanism.

This task does **not** authorize any KFE/HJB scientific correction yet.

## 2. Core objective

Execute exactly one 2018 diagnostic run that:

1. uses the same corrected Owner-A 2018 scientific input contract;
2. preserves the current scientific equations, grid, calibration, controller, and convergence rules;
3. instruments the household/KFE path only enough to capture the first KFE singularity;
4. stops immediately at that first singular event;
5. persists the exact province, outer iteration, household-call index, HJB status, local household inputs, generator structure, contaminated matrix structure, rank/nullity diagnostics, SCC/closed-class diagnostics, and traceback;
6. performs no retry and no repair.

## 3. Required live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `10dade76d0c694c511955226242b8d9f041eccc9`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md` and all CURRENT rules it names;
   - the 2018 observability/single-retry task and report;
   - the 13-pass comparison/2018 forensic task and report;
   - the MATLAB `load_GDPdata` unit-scaling audit task and report;
   - corrected-2009 same-input parity acceptance;
   - `exports/matlab_faithful_two_asset_ha.py`;
   - `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py`;
   - `validators/multi_province/mp4c_python_annual_production.py`;
   - current Owner-A input adapter and stationary runtime.

## 4. Frozen 2018 scientific input contract

Use the same corrected Owner-A 2018 input as the previous failed attempts.

Required known identity:

`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`

Before execution, re-read the preserved original/retry input and prove byte identity.

Required semantic binding:

- `steady_state_calendar_year = 2018`;
- `rolling_window_entry_index = 10`;
- `regression_vintage_index = 19`;
- `calendar_level_row_index = 19`;
- rolling window = `2009–2018`;
- CAP source = `R语言计算资本存量`;
- POP source = `就业人数`;
- GDP source = `GDP`;
- GDP scaling = ×1000;
- CAP scaling = ×1000;
- POP scaling = ×100;
- 31-province order exact;
- `no_2023_scientific_input = true`.

No scientific input mutation is allowed.

## 5. Scientific-code immutability

The diagnostic run must leave unchanged:

- HJB equations;
- transfer FOC;
- adjustment costs;
- illiquid-return taper;
- raw-Vb logic;
- upwind/policy selection;
- generator assembly;
- KFE contaminated-row row choice;
- RHS value `0.007`;
- normalization formula;
- state grid;
- HJB tolerances/iteration ceiling;
- outer fixed-point/controller logic;
- firm/wage/monetary/fiscal logic;
- calibration;
- initial state values.

Instrumentation may only:

- attach diagnostic metadata;
- persist arrays/sparse matrices before the failing solve;
- compute read-only structural diagnostics on the already-built matrix/operator;
- raise/stop after the first singularity is captured.

No regularization, pseudoinverse, row-choice change, fallback stationary solver, damping, perturbation, or retry is permitted.

## 6. Phase A — zero-science instrumentation tests

Before any HANK call, add a bounded diagnostic wrapper/hook with dummy matrices only.

Prove it can persist:

- province label/index;
- outer iteration;
- household call number;
- HJB converged flag;
- HJB iterations;
- HJB convergence statistic;
- household inputs `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap`;
- generator dimensions/nnz/finite status;
- max absolute row-sum residual of the source operator;
- min/max diagonal;
- minimum/maximum off-diagonal entries;
- contaminated row index;
- contaminated matrix dimensions/nnz;
- rank/nullity diagnostics as specified below;
- SCC/closed-class diagnostics as specified below;
- stderr/traceback;
- no-overwrite evidence behavior.

Dummy tests must invoke no scientific solver.

Phase-A scientific calls:

- Python stationary: 0;
- household/HJB/KFE: 0;
- MATLAB: 0;
- R/PLM: 0.

## 7. Required structural diagnostics at the first singular event

The state count is expected to be manageable (`20 × 20 × 2 = 800`). At the first failing KFE event, persist the sparse matrices and calculate read-only diagnostics.

### 7.1 HJB status

Persist:

- `hjb.converged`;
- HJB iteration count;
- HJB convergence statistic;
- whether the event occurred on the normal post-convergence path or the accepted MATLAB post-loop path after HJB nonconvergence.

### 7.2 Generator/operator checks

For the post-HJB source operator `A` and transpose `A'`:

- shape;
- nnz;
- finite-data flag;
- max absolute row-sum residual of `A`;
- max absolute column-sum residual of `A'`;
- diagonal min/max;
- off-diagonal min/max;
- count of materially positive off-diagonal entries where sign contract expects nonnegative transition rates;
- count of isolated/zero-outflow states subject to source conventions;
- connected-component/SCC structure of the directed graph induced by positive transition rates.

Do not reject solely from generic CTMC assumptions if the frozen MATLAB source permits signed/truncated iteration entries; report source-operator and post-convergence operator conventions separately where relevant.

### 7.3 Closed communicating classes

Using a conservative numerical edge threshold documented in the report, compute strongly connected components and identify SCCs with no outgoing transition to another SCC.

Persist:

- SCC count;
- closed SCC count;
- sizes of closed SCCs;
- state indices/ranges for each closed SCC;
- whether more than one closed SCC exists.

### 7.4 Rank/nullity

For the 800×800 transpose and contaminated matrix, use a reproducible diagnostic appropriate for this size.

Preferred:

- dense rank/SVD only if memory/time is reasonable;
- otherwise sparse smallest singular values / rank-revealing method.

Persist:

- method;
- threshold/tolerance;
- estimated rank;
- estimated nullity;
- smallest singular values/eigenvalues used for classification;
- contaminated matrix estimated rank/nullity.

Do not alter the solve based on these diagnostics.

### 7.5 Failing solve evidence

Persist:

- contaminated row index;
- RHS;
- `MatrixRankWarning` text;
- whether `spsolve` returned NaN/Inf;
- count of nonfinite raw-solve entries;
- exact traceback.

## 8. Exact province/iteration/call localization

The run must make it impossible to lose localization again.

Persist before each household call at minimum:

- outer iteration number;
- province index and normalized province name;
- global household-call count about to execute;
- `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap`;
- `Yt`, `Lt`, `Kt`, `Zt`, `GovInv` from the entering outer state.

When first singularity occurs, freeze the exact localization in:

`first_singularity_localization.json`.

## 9. Execution boundary — exactly one 2018 diagnostic run

After Phase-A PASS and input/code identity checks, execute exactly one 2018 diagnostic run.

Use:

- year = 2018 only;
- workers = 1;
- subprocesses = 1;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- same outer/HJB/household ceilings as frozen production;
- automatic reruns = 0;
- no wall-clock kill unless existing infrastructure requires one and task report records it.

The diagnostic must STOP immediately after first singular KFE event is captured.

If unexpectedly the full 2018 run reaches `SOURCE_CONVERGED` without singularity, classify that fact but do not launch a second run.

## 10. Evidence root

Use fresh no-overwrite root, preferred:

`D:\ProjectTemp\ch5-mp4c-2018-first-singularity-generator-diagnostic-20260903-001`

If occupied, use next unused suffix.

Persist at minimum:

- `phase_a_zero_science_test_receipt.json`;
- `scientific_code_identity_manifest.json`;
- `input_2018_identity.json`;
- `household_call_ledger.csv` up to the first failure;
- `first_singularity_localization.json`;
- `first_singularity_hjb_status.json`;
- `first_singularity_operator_summary.json`;
- `first_singularity_operator_A.npz`;
- `first_singularity_operator_transpose.npz`;
- `first_singularity_contaminated_matrix.npz`;
- `first_singularity_rhs.npy`;
- `first_singularity_scc_closed_classes.json`;
- `first_singularity_rank_nullity.json`;
- `first_singularity_stdout.log`;
- `first_singularity_stderr.log`;
- `first_singularity_traceback.txt`;
- `diagnostic_execution_receipt.json`;
- `zero_or_bounded_science_ledger.json`;
- `audit_manifest.json`.

Large arrays/matrices stay outside GitHub.

## 11. Required root-cause classification

Based only on captured evidence, choose the strongest supported classification:

- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_HJB_NONCONVERGED_POSTLOOP_OPERATOR`;
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_MULTIPLE_CLOSED_COMMUNICATING_CLASSES`;
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_OPERATOR_RANK_DEFICIENCY_BEYOND_SINGLE_STATIONARY_NULL_DIRECTION`;
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_GENERATOR_CONSTRUCTION_DEFECT`;
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_OTHER_CAPTURED_NUMERICAL_PATHOLOGY`;
- `2018_KFE_SINGULARITY_ROOT_CAUSE_REMAINS_UNRESOLVED_AFTER_FIRST_EVENT_CAPTURE`.

Do not label a source-faithful MATLAB convention as a defect without direct source/parity evidence.

## 12. Repair boundary

This task does not authorize repair.

Even if the root cause appears obvious:

- no KFE changes;
- no HJB changes;
- no input changes;
- no grid changes;
- no parameter changes;
- no second 2018 run.

After L3 review, a separate live task will authorize the smallest scientifically justified correction and bounded 2018 re-execution.

## 13. Shock/IRF boundary

No shock/IRF execution in this task.

The route after 2018 repair is expected to return to the already accepted MP4D classification:

`SEQUENTIAL_STATIONARY_COMPARATIVE_STATICS_RESPONSE_PATH_CONFIRMED`

but numerical shock/response execution remains blocked until 2018 stationary coverage is accepted.

## 14. Git boundary and report

One bounded final commit/push may include only:

- diagnostic instrumentation/wrapper code;
- focused zero-science tests;
- repository report.

Do not commit generated NPZ/NPY/MAT/log scientific evidence.

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_FIRST_SINGULARITY_GENERATOR_DIAGNOSTIC_REPORT.md`

## 15. Terminal markers

If first singularity is captured and localized with usable generator diagnostics:

`MP4C_2018_FIRST_SINGULARITY_GENERATOR_DIAGNOSTIC_COMPLETE__ROOT_CAUSE_CLASSIFIED_OR_BOUNDED__NO_REPAIR_NO_RETRY`

If diagnostic instrumentation itself fails before useful scientific capture:

`MP4C_2018_FIRST_SINGULARITY_DIAGNOSTIC_INFRASTRUCTURE_BLOCKED__NO_REPAIR_NO_RETRY`

If 2018 unexpectedly converges in the sole diagnostic run:

`MP4C_2018_DIAGNOSTIC_RUN_UNEXPECTEDLY_CONVERGED_WITHOUT_SINGULARITY__NO_SECOND_RUN__L3_REVIEW_REQUIRED`
