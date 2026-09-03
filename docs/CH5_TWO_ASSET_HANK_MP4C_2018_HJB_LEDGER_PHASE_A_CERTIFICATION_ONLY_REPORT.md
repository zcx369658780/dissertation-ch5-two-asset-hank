# MP4C 2018 HJB-ledger Phase-A certification-only report

## Terminal

`MP4C_2018_HJB_LEDGER_PHASE_A_CERTIFIED__ZERO_SCIENCE__READY_FOR_ONE_DURABLE_2018_CHILD_TASK`

This task certified diagnostic instrumentation only.  It did not read a frozen
2018 input, launch a child, or run stationary, household, production HJB,
production KFE, MATLAB, R/PLM, shock, or IRF work.

## Authority and scope

- Fresh fetch found live task
  `fbf04efc4cec291b4e44f6d0d6be7fa88e2d4be2` as a direct child of
  `fcc0c808f6d35784908c7066d9acfe69de01ad80`.
- Local state fast-forwarded cleanly to the task authority and was `0/0` before
  certification.
- The existing exact-field correction was already correct.  No source code was
  changed in this task.

## Zero-science validation

```text
python -m py_compile validators/multi_province/mp4c_2018_first_singularity_diagnostic.py tests/test_mp4c_2018_first_singularity_diagnostic.py
PASS

python -m pytest -q tests/test_mp4c_2018_first_singularity_diagnostic.py
2 passed, 1 expected dummy MatrixRankWarning
```

The warning belongs to the intentionally singular dummy sparse fixture.  It is
not a production KFE call and does not consume scientific budget.

The Phase-A dummy fixture proved:

- exact callable identities remain
  `exports.matlab_faithful_two_asset_ha.solve_matlab_faithful_hjb` and
  `exports.matlab_faithful_two_asset_ha.solve_matlab_faithful_stationary_kfe`;
- injected adapter order is exactly `hjb -> kfe -> aggregate -> hjb -> kfe ->
  aggregate`;
- `DurableCsvLedger` writes one CSV header and two rows, each append occurring
  before its injected dummy KFE entry after flush and fsync;
- Python `csv.DictReader` parsed exact fields `province` and
  `province_index_0based` once each, avoiding the prior substring defect;
- rows are respectively `DUMMY_A / True / HJB_CONVERGED` and `DUMMY_B / False /
  MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE`;
- dummy raw singularity artifacts existed before any postmortem artifact, and
  the separate read-only postmortem unit test passed;
- the ledger lifecycle closed cleanly, with no `UnboundLocalError`, duplicate
  header, or file lifecycle error.

## Scientific-call ledger

All counts are zero: stationary, household, HJB, KFE, MATLAB, and R/PLM.
Frozen-2018-input reads, scientific children, and source edits are also zero.

## External evidence

Fresh no-overwrite evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-hjb-ledger-phase-a-certification-20260903-001`

It contains the compiler and pytest stdout/stderr, dummy Phase-A receipt,
parsed CSV/callable evidence, zero-science ledger, certification receipt, raw
dummy capture files, and SHA-256 audit manifest.

## Boundary

This certification does not itself authorize 2018 execution.  It supplies the
published prerequisite marker only; a later live task must explicitly allocate
the one durable 2018 scientific child.
