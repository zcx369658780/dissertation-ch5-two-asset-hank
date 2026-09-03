# CH5_TWO_ASSET_HANK_MP4C_2018_PHASE_A_FIXTURE_REPAIR_AND_FIRST_SINGULARITY_CAPTURE_EXECUTION

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / diagnostic-fixture repairer / single-run scientific diagnostician

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`0060d3311ea8a6f201c431a4ea70d39315f7c90e`

with terminal:

`MP4C_2018_DIAGNOSTIC_WIRING_REPAIR_PHASE_A_BLOCKED__NO_2018_EXECUTION`

Accepted predecessor facts:

- callable binding was corrected to the production MATLAB-faithful HJB/KFE export;
- Phase A stopped before any HJB/KFE science because the dummy adapter fixture lacked `grid.z`;
- scientific calls were exactly zero;
- no 2018 input was consumed and no 2018 execution occurred;
- no solver/model/input/grid/calibration/controller mutation occurred.

This is a bounded diagnostic-fixture defect. Under the standing simple-debugging delegation, L3 authorizes one Phase-A fixture repair and, only if Phase A passes, one 2018 first-singularity capture execution.

## 2. Purpose

1. Repair only the zero-science dummy fixture so it satisfies the adapter's required grid interface, including `grid.z` and any other purely structural attributes that the production adapter legitimately reads.
2. Prove the wiring/instrumentation path with zero scientific calls.
3. If and only if Phase A passes, execute exactly one 2018 diagnostic run to capture the first genuine KFE singularity event.
4. Do not repair HJB/KFE science in this task.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this task live on `origin/main` as direct child of `0060d3311ea8a6f201c431a4ea70d39315f7c90e`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, all CURRENT rules, and the two predecessor 2018 diagnostic reports/tasks.

## 4. Phase A — fixture repair only — ZERO SCIENCE

The predecessor failure was:

- correct production HJB/KFE symbols;
- dummy adapter fixture missing `grid.z`;
- failure before dummy HJB invocation.

Repair only the dummy fixture/test harness. Prefer constructing the actual production `MatlabFaithfulHJBGrid` with tiny dummy arrays rather than inventing a partial ad-hoc grid object, provided no scientific solver is invoked.

The fixture must expose every structural attribute legitimately read by the adapter, including at minimum:

- `b`;
- `a`;
- `z`;
- switch/generator support needed only for interface validation.

Do not change production solver code merely to make the dummy test pass.

Phase-A tests must prove:

- exact HJB callable identity resolves to `exports.matlab_faithful_two_asset_ha.solve_matlab_faithful_hjb`;
- exact KFE callable identity resolves to `exports.matlab_faithful_two_asset_ha.solve_matlab_faithful_stationary_kfe`;
- post-loop adapter accepts injected wrapped callables;
- positional/keyword arguments are preserved;
- dummy HJB return can flow to dummy KFE without any real HJB/KFE solver call;
- instrumentation can capture a dummy sparse matrix and persist expected receipts;
- py_compile passes;
- scientific call counters remain zero.

Required marker:

`MP4C_2018_PHASE_A_DIAGNOSTIC_FIXTURE_REPAIR_PASS__ONE_FIRST_SINGULARITY_CAPTURE_EXECUTION_AUTHORIZED`

If Phase A fails for any reason: STOP. No 2018 execution.

## 5. Frozen 2018 scientific input

Use exact preserved Owner-A 2018 input SHA-256:

`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`

Required binding:

- steady-state year 2018;
- rolling entry 10;
- PLM vintage 19;
- calendar row 19;
- rolling window 2009–2018;
- GDP source `GDP` ×1000;
- CAP source `R语言计算资本存量` ×1000;
- POP source `就业人数` ×100;
- exact 31-province order;
- no 2023 scientific input.

Byte mismatch: STOP.

## 6. No scientific mutation

Do not change:

- HJB equations or parameters;
- KFE equations;
- grid;
- HJB/KFE tolerances;
- transfer FOC;
- adjustment cost;
- raw-Vb logic;
- illiquid return taper;
- generator assembly;
- contaminated-row index/RHS/normalization;
- migration/firm/wage/monetary/fiscal blocks;
- outer controllers;
- calibration;
- annual input.

Forbidden: pseudoinverse, epsilon regularization, alternate solver, fallback density, changed contaminated row, second retry.

## 7. One diagnostic execution

Only after Phase-A PASS, execute exactly once:

- year = 2018;
- workers = 1;
- subprocesses = 1;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- automatic reruns = 0.

Fresh no-overwrite root preferred:

`D:\ProjectTemp\ch5-mp4c-2018-first-singularity-capture-after-fixture-repair-20260903-001`

## 8. Required pre-call/HJB ledger

Before each household call persist:

- outer iteration;
- province index/name;
- global household-call number;
- `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap`;
- `Yt`, `Lt`, `Kt`, `Zt`, `GovInv`.

After each HJB return persist:

- context;
- `hjb.converged`;
- HJB iterations;
- convergence statistic;
- KFE-entry classification:
  - `HJB_CONVERGED`, or
  - `MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE`.

## 9. First genuine KFE singularity capture

At the first `MatrixRankWarning` or non-finite contaminated-row solve, persist before STOP:

- province / outer iteration / household call;
- exact household inputs and entering macro state;
- exact HJB status;
- post-HJB operator A;
- A transpose;
- contaminated matrix;
- RHS;
- raw solve vector if produced;
- matrix shape/nnz/finite flags;
- maximum row-sum residual;
- diagonal/off-diagonal extrema;
- zero-outflow / isolated states;
- SCC count;
- closed SCC count and members;
- rank/nullity diagnostics for A' and contaminated matrix;
- smallest singular/eigenvalue diagnostics with method/tolerance;
- warning records;
- stdout/stderr/traceback.

Then STOP immediately. No repair in this task.

## 10. Root-cause classification

Choose the strongest evidence-supported classification:

- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_HJB_NONCONVERGED_POSTLOOP_OPERATOR`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_MULTIPLE_CLOSED_COMMUNICATING_CLASSES`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_OPERATOR_RANK_DEFICIENCY_BEYOND_SINGLE_STATIONARY_NULL_DIRECTION`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_GENERATOR_CONSTRUCTION_DEFECT`
- `2018_KFE_SINGULARITY_ASSOCIATED_WITH_OTHER_CAPTURED_NUMERICAL_PATHOLOGY`
- `2018_KFE_SINGULARITY_ROOT_CAUSE_REMAINS_UNRESOLVED_AFTER_FIRST_EVENT_CAPTURE`

Do not call a MATLAB-faithful convention a defect without source/parity evidence.

## 11. If singularity does not recur

If 2018 unexpectedly finishes without singularity, preserve the result and STOP. Do not rerun.

Terminal:

`2018_FIRST_SINGULARITY_NOT_REPRODUCED_AFTER_PHASE_A_FIXTURE_REPAIR__NO_SECOND_RUN`

Do not accept 14-year coverage automatically.

## 12. Required evidence

Persist at minimum:

- `phase_a_fixture_repair_test_receipt.json`;
- `scientific_code_identity_manifest.json`;
- `input_2018_identity.json`;
- `household_call_ledger.csv`;
- `hjb_return_ledger.csv`;
- first-singularity localization/HJB/operator/SCC/rank artifacts;
- captured sparse matrices/arrays;
- stdout/stderr/traceback;
- diagnostic execution receipt;
- bounded-science ledger;
- audit manifest.

## 13. Report

Required repository report:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_PHASE_A_FIXTURE_REPAIR_AND_FIRST_SINGULARITY_CAPTURE_EXECUTION_REPORT.md`

Expected successful diagnostic terminal:

`MP4C_2018_FIRST_SINGULARITY_CAPTURE_COMPLETE_AFTER_PHASE_A_FIXTURE_REPAIR__ROOT_CAUSE_CLASSIFIED_OR_BOUNDED__NO_REPAIR_NO_RETRY`
