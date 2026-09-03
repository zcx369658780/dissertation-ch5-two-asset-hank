# CH5_TWO_ASSET_HANK_MP4C_2018_DIAGNOSTIC_PRODUCTION_PATH_PARITY_REPAIR_AND_ZERO_SCIENCE_CERTIFICATION

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / diagnostic-path parity auditor / zero-science certification executor

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`e7f014fd35252f69237c0eb34b84dc9d658ac31b`

with terminal:

`2018_FIRST_SINGULARITY_NOT_REPRODUCED_IN_CERTIFIED_DURABLE_EXECUTION__NO_SECOND_RUN`

Accepted predecessor facts:

- the certified diagnostic recorder completed one durable 2018 child without instrumentation failure;
- the child started and completed 2,015 household/HJB calls;
- no `MatrixRankWarning` or non-finite contaminated-row KFE solve was observed;
- no retry, scientific repair, regularization, pseudoinverse, alternate solver, or second child occurred;
- the result does **not** authorize acceptance of 2018 or 2009–2022 coverage.

Post-execution L3 source review identified a material diagnostic/production-path mismatch that must be resolved before interpreting the non-reproduction result.

## 2. Identified production-path mismatches

The authoritative annual production worker is:

`validators/multi_province/mp4c_python_annual_production.py`

At each household batch, production semantics include:

1. recomputing productivity from the entering snapshot:

`prod_i = Yt_i / Lt_i`;

2. mutating the shared destination-by-origin matrix:

`phi[d,o] = 1 + 0.3 * (prod_d - prod_o) / (prod_d + prod_o)`;

3. using the household KFE density to compute province `AtTax` exactly as:

`AtTax = a_ss * rah - sum(a * effective_illiquid_return(a, rah) * density) * cell_weight`;

4. placing that `AtTax` into the `PreFrozenHouseholdOutputBatch`, from which the one-turn/firm block consumes it.

The current certified 2018 diagnostic instead:

- initializes `phi = ones((31,31))` and does not recompute it from `Yt/Lt` before each batch;
- returns `AtTax = 0.0` for every household output.

Therefore the 2,015-call non-reproduction execution did not follow the authoritative annual production trajectory after the first household batch. It is diagnostic evidence only and must not be interpreted as proof that the original production-path 2018 singularity disappeared.

## 3. Core objective

Repair only the 2018 diagnostic wrapper so that its scientific path is behaviorally identical to the authoritative annual production worker for all state-affecting household-batch semantics, while preserving the already certified capture/ledger instrumentation.

Then certify that parity under **zero science only**.

This task does **not** authorize reading or running the frozen 2018 scientific input and does **not** authorize any 2018 scientific child.

## 4. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `e7f014fd35252f69237c0eb34b84dc9d658ac31b`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md` and all CURRENT rules it names;
   - predecessor certified-execution task/report;
   - predecessor HJB-ledger certification task/report;
   - `validators/multi_province/mp4c_python_annual_production.py`;
   - `validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`;
   - `tests/test_mp4c_2018_first_singularity_diagnostic.py`;
   - `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py`;
   - `src/ch5_two_asset_hank/multi_province/one_turn.py`;
   - `src/ch5_two_asset_hank/multi_province/stationary_runtime.py`;
   - faithful HJB/KFE export only as needed for identity and pure helper checks.

## 5. First deliverable: field-by-field production-path audit

Before editing, produce a source-grounded matrix comparing production worker versus diagnostic for every object that can affect the subsequent outer-turn path.

At minimum compare:

- grid construction;
- `EconomicParams`;
- HJB numerics;
- initial-state construction;
- `phi` initialization;
- per-batch `phi` recomputation timing and formula;
- `sigmau_destination_origin`;
- `_source_initial_arrays`;
- household `rah`, `rb`, `tau`, `w`, `Tt`, `rb_gap` inputs;
- post-loop HJB behavior;
- KFE callable;
- household aggregates `Ct`, `Lt`, `At`, `Bt`;
- `AtTax` formula;
- `PreFrozenHouseholdOutputBatch` contents;
- model parameter dictionary passed to `OnlineStationaryInputs`;
- `reg_threshold`;
- `max_outer_turns`;
- `steady_state=True`;
- province order;
- migration-wedge matrix;
- one-turn call order;
- outer controller path.

Classify each item as:

- `EXACT_MATCH`;
- `DIAGNOSTIC_ONLY_OBSERVABILITY_DIFFERENCE__STATE_NEUTRAL`;
- `PRODUCTION_PATH_MISMATCH__MUST_REPAIR`;
- `UNRESOLVED__STOP`.

Do not assume only `phi` and `AtTax` differ. Audit the full path.

## 6. Allowed diagnostic-only repair

If the audit confirms deterministic mismatches, modify only:

- `validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`;
- its focused zero-science test file(s), preferably `tests/test_mp4c_2018_first_singularity_diagnostic.py`.

Required scientific-path repair includes, at minimum if confirmed by source:

### 6.1 Per-batch phi

Before the province household loop, reproduce the production calculation exactly:

`prod = [Yt_i / Lt_i]`

`phi[:] = 1 + 0.3 * (prod[:,None] - prod[None,:]) / (prod[:,None] + prod[None,:])`

Preserve destination-row × origin-column orientation and mutation timing.

### 6.2 AtTax

After each household result, reproduce the production calculation exactly using:

- the same accepted `matlab_faithful_illiquid_return`;
- the same `grid.a` and `a_max`;
- the province's current `rah`;
- the returned stationary density;
- the returned KFE `cell_weight`;
- the returned aggregate `a_ss`.

Then pass that exact `AtTax` into `PreFrozenHouseholdOutputBatch` rather than zero.

### 6.3 No other scientific changes

Do not alter:

- HJB equations or parameters;
- KFE equations;
- grid/state support;
- transfer FOC;
- adjustment cost;
- raw-Vb behavior;
- illiquid return taper;
- contaminated-row method;
- density normalization;
- migration, firm, wage, monetary, fiscal, controller logic;
- Owner-A annual input semantics;
- production worker itself.

Do not refactor production code merely for convenience in this task.

## 7. Preserve certified instrumentation

The existing durable recorder behavior must remain intact:

- `DurableCsvLedger` semantics;
- pre-call ledger;
- HJB-return ledger;
- flush/fsync ordering;
- raw singularity capture-before-postmortem;
- fail-closed first-singularity stop;
- separate read-only postmortem.

A production-path repair must not regress any previously certified instrumentation property.

## 8. Mandatory ZERO-SCIENCE parity tests

No preserved 2018 input may be read in this task.

No production HJB/KFE/stationary call may execute.

Use synthetic/dummy states, dummy household results, and injected dummy callables only.

At minimum add tests proving:

### 8.1 Phi parity

For a synthetic multi-province snapshot with non-identical `Yt/Lt`, compare diagnostic-generated `phi` against the literal production formula.

Require exact array equality where arithmetic/order is identical, otherwise justify and freeze a machine-precision tolerance.

Test orientation explicitly:

- row = destination;
- column = origin.

Test that `phi` is recomputed on a second synthetic turn with changed `Yt/Lt`, not left at the previous or all-ones value.

### 8.2 AtTax parity

Using a synthetic grid, known `rah`, known `a_ss`, known finite density, and known `cell_weight`, compare diagnostic `AtTax` against the literal production expression.

Require the same faithful illiquid-return helper identity.

Require a nonzero synthetic expected `AtTax` so the prior hardcoded-zero defect cannot accidentally pass.

### 8.3 Batch-output parity

With injected dummy HJB/KFE/aggregate results, verify the diagnostic `PreFrozenHouseholdOutputBatch` fields match production semantics for:

- `ct`;
- `household_lt`;
- `at`;
- `bt`;
- `at_tax`;
- `converged`;
- diagnostics metadata.

### 8.4 Downstream one-turn sensitivity proof

Without running household/HJB/KFE science, construct synthetic `PreFrozenHouseholdOutputBatch` objects and call the already accepted deterministic one-turn arithmetic only if project rules classify this as zero-science arithmetic; otherwise perform pure formula/static verification.

Prove that changing `phi` and/or `AtTax` can change state-affecting downstream objects (migration/wage and/or Govinc), establishing why the previous 2,015-call non-reproduction is not production-path evidence.

This is explanatory evidence only, not a new model result.

### 8.5 Instrumentation regression

Re-run the previously certified dummy ledger/capture tests and require them to remain PASS.

## 9. Hard no-science boundary

Scientific calls must remain zero:

- 2018 frozen-input reads = 0;
- stationary = 0;
- household = 0;
- production HJB = 0;
- production KFE = 0;
- MATLAB = 0;
- R/PLM = 0;
- scientific child = 0;
- shock/IRF = 0.

No full annual model execution.

## 10. Reclassification of predecessor 2,015-call run

The report must explicitly classify the predecessor execution as:

`2018_SINGULARITY_NOT_REPRODUCED_UNDER_DIAGNOSTIC_PATH_WITH_NONPRODUCTION_PHI_AND_ATTAX_SEMANTICS__NOT_PRODUCTION_PATH_EVIDENCE`

unless the field-by-field audit disproves one or both mismatches.

Do not call it a 2018 PASS.

Do not accept 2009–2022 coverage.

## 11. Evidence root

Use fresh no-overwrite root, preferred:

`D:\ProjectTemp\ch5-mp4c-2018-diagnostic-production-path-parity-zero-science-20260903-001`

Persist at minimum:

- `production_vs_diagnostic_path_audit.csv`;
- `production_vs_diagnostic_path_audit.md`;
- `phi_zero_science_parity_receipt.json`;
- `attax_zero_science_parity_receipt.json`;
- `batch_output_zero_science_parity_receipt.json`;
- `instrumentation_regression_receipt.json`;
- compiler/pytest stdout and stderr;
- `zero_science_execution_ledger.json`;
- `audit_manifest.json`.

## 12. Acceptance terminal

On full parity repair + zero-science certification:

`MP4C_2018_DIAGNOSTIC_PRODUCTION_PATH_PARITY_CERTIFIED__PHI_ATTAX_AND_BATCH_SEMANTICS_MATCH_PRODUCTION__ZERO_SCIENCE__READY_FOR_ONE_FINAL_DURABLE_2018_REEXECUTION_TASK`

If any state-affecting production-path mismatch remains unresolved:

`MP4C_2018_DIAGNOSTIC_PRODUCTION_PATH_PARITY_UNRESOLVED__ZERO_SCIENCE__NO_2018_REEXECUTION`

If zero-science tests fail:

`MP4C_2018_DIAGNOSTIC_PRODUCTION_PATH_PARITY_TEST_FAILED__ZERO_SCIENCE__NO_2018_REEXECUTION`

Stop on failure. Do not self-authorize scientific execution.

## 13. Required repository report

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_DIAGNOSTIC_PRODUCTION_PATH_PARITY_REPAIR_AND_ZERO_SCIENCE_CERTIFICATION_REPORT.md`
