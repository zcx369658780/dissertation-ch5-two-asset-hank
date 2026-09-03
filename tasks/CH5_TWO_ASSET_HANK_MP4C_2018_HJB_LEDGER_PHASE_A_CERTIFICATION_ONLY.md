# CH5_TWO_ASSET_HANK_MP4C_2018_HJB_LEDGER_PHASE_A_CERTIFICATION_ONLY

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / zero-science diagnostic-certification executor

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`fcc0c808f6d35784908c7066d9acfe69de01ad80`

with terminal:

`MP4C_2018_HJB_LEDGER_CLOSURE_REPAIR_PHASE_A_FAILED__NO_2018_INPUT_NO_SCIENTIFIC_CHILD`

Accepted predecessor facts:

- the diagnostic HJB-return ledger implementation was moved from fragile nested-writer state to a dedicated `DurableCsvLedger` helper;
- the intended Phase-A test exercises two dummy HJB returns and verifies durable HJB-ledger writes before dummy KFE entry;
- `py_compile` passed;
- the only failing assertion was a zero-science fixture bug: `header.count('province')` counted both exact field `province` and field `province_index_0based`;
- the exact-field assertion correction was already edited after the failure, but per fail-closed rules was not re-executed;
- no frozen 2018 input was read;
- stationary / household / HJB / KFE / MATLAB / R-PLM scientific calls were all zero;
- no scientific-child budget was consumed.

Because several recent 2018 attempts were blocked by instrumentation/test-harness defects, this task intentionally separates **diagnostic certification** from **scientific execution**.

## 2. Purpose

Certify the corrected HJB-ledger / capture instrumentation under zero science only.

This task does **not** authorize reading the frozen 2018 input and does **not** authorize any 2018 scientific child.

A later task will allocate the scientific-child budget only after this certification passes.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `fcc0c808f6d35784908c7066d9acfe69de01ad80`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md` and all CURRENT rules;
   - predecessor task/report;
   - `validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`;
   - `tests/test_mp4c_2018_first_singularity_diagnostic.py`;
   - faithful HJB/KFE export and post-loop adapter only as needed for callable identity verification.

## 4. Allowed scope

Prefer **no source edit** if the exact-field correction is already present and correct.

If a new zero-science test-only defect is found, only the smallest diagnostic/test-harness correction is allowed.

Do not modify:

- production HJB/KFE;
- household equations;
- generator assembly;
- stationary runtime;
- Owner-A input adapter;
- grid/calibration/controller semantics;
- annual scientific inputs.

## 5. Mandatory zero-science certification

Run only focused zero-science validation.

At minimum:

```text
python -m py_compile validators/multi_province/mp4c_2018_first_singularity_diagnostic.py tests/test_mp4c_2018_first_singularity_diagnostic.py
python -m pytest -q tests/test_mp4c_2018_first_singularity_diagnostic.py
```

The test must prove all of the following:

1. exact HJB callable identity is `exports.matlab_faithful_two_asset_ha.solve_matlab_faithful_hjb`;
2. exact KFE callable identity is `exports.matlab_faithful_two_asset_ha.solve_matlab_faithful_stationary_kfe`;
3. adapter injected-callable sequence is exactly:
   `hjb -> kfe -> aggregate -> hjb -> kfe -> aggregate`;
4. `hjb_return_ledger.csv` has exactly one header row;
5. exact header fields contain `province` exactly once and `province_index_0based` exactly once, checked by CSV field parsing, not substring counting;
6. exactly two dummy HJB-return rows are present;
7. first row is `DUMMY_A`, `hjb_converged=True`, `kfe_path=HJB_CONVERGED`;
8. second row is `DUMMY_B`, `hjb_converged=False`, `kfe_path=MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE`;
9. each ledger append is flushed/fsynced before the corresponding dummy KFE call;
10. `DurableCsvLedger.close()` is safe and idempotent enough for the tested lifecycle;
11. raw first-singularity dummy capture persists before postmortem;
12. postmortem remains a separate read-only phase;
13. no `UnboundLocalError`, header-count bug, file-lifecycle error, or duplicate-header behavior occurs;
14. scientific call counters remain exactly zero.

## 6. Hard no-science boundary

Forbidden in this task:

- reading the preserved 2018 canonical input file;
- stationary execution;
- household execution;
- production HJB execution;
- production KFE execution;
- MATLAB execution;
- R/PLM execution;
- any 2018 child process;
- shock/IRF execution.

Scientific call counts must remain zero.

## 7. Evidence

Use a fresh no-overwrite root, preferred:

`D:\ProjectTemp\ch5-mp4c-2018-hjb-ledger-phase-a-certification-20260903-001`

Persist at minimum:

- `phase_a_certification_receipt.json`;
- focused pytest stdout/stderr;
- parsed HJB-ledger header/row evidence;
- callable identity evidence;
- zero-science ledger;
- audit manifest.

## 8. Terminal

On full PASS:

`MP4C_2018_HJB_LEDGER_PHASE_A_CERTIFIED__ZERO_SCIENCE__READY_FOR_ONE_DURABLE_2018_CHILD_TASK`

On any failure:

`MP4C_2018_HJB_LEDGER_PHASE_A_CERTIFICATION_FAILED__ZERO_SCIENCE__NO_2018_EXECUTION`

Stop on failure. Do not self-authorize another attempt.

## 9. Required report

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_HJB_LEDGER_PHASE_A_CERTIFICATION_ONLY_REPORT.md`
