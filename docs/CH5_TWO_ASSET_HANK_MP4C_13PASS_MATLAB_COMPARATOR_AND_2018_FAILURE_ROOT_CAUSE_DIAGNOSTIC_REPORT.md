# MP4C 13-pass MATLAB comparison and 2018 failure diagnosis

## Terminal

`MP4C_13PASS_PYTHON_INTEGRITY_CONFIRMED__MATLAB_REFERENCE_MOSTLY_LEGACY_DIAGNOSTIC__2018_DIAGNOSIS_COMPLETE_OR_PENDING`

The 13 successful Owner-A corrected Python years are internally consistent. No
new Python, MATLAB, household, HJB/KFE, PLM, shock, IRF, R5, or Results run was
performed. The 2018 first-attempt failure remains immutable and was not retried.

## Python evidence

All 13 PASS years (2009--2017 and 2019--2022) have `SOURCE_CONVERGED`, exact
Owner-A representation and runtime-input hashes, expected semantic indices,
2023 exclusion, the frozen four-variable one-thread environment, 31 finite
terminal rows by 20 fields, valid 31x31 destination-row/origin-column `Lt_mat`,
and matching checkpoint/output hashes. This proves artifact integrity, not
complete 14-year annual coverage.

## MATLAB comparison boundary

The protected diagnostic tree has `Multi_Province_12sts_2009.mat` through
`_2023.mat` plus `12年稳态值.xlsx` and `12年稳态Ltmat.xlsx`. Their filename is
not evidence of corrected calendar binding: they belong to the historical
`data_year=ii` annual route and are classified
`LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY`. No existing artifact was proven to
share each Owner-A corrected GDP/CAP/POP calendar-row contract, so no strict
multi-year parity result is issued. The separately accepted corrected-2009
same-input result remains an anchor under its own frozen input contract, not a
claim that the new Owner-A levels are identical.

## 2018 root cause

2018 exited `1`, which the scheduler maps to `SHARED_FAIL`; only exit `2` is
classified as solver `FAIL`. `subprocess.run(..., text=True)` does not persist
stdout, stderr, or traceback. The worker catches only
`SteadyStateConvergenceError`; another exception exits before terminal and
`FAILURE.json` serialization. The strongest supported classification is:

`2018_SHARED_FAIL_RUNNER_EXCEPTION_CAPTURE_DEFECT`

This establishes an engineering observability defect. It does not establish a
scientific solver failure or identify the lost triggering exception.

## Integrated blockers and next gate

Before any retry, a new live task must authorize: (1) a minimal non-scientific
stderr/stdout/traceback and failure-stage persistence repair; (2) a bounded
2018 retry policy; and (3) any separately required corrected-calendar MATLAB
artifact mapping for strict multi-year parity. No retry is authorized here.

External no-overwrite evidence:
`D:\ProjectTemp\ch5-mp4c-13pass-matlab-comparator-2018-diagnostic-20260903-001`.
