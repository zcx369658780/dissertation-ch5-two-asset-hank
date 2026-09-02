# MP4C Owner-A corrected 2009--2022 annual stationary execution

## Terminal verdict

`MP4C_OWNER_A_2009_2022_CORRECTED_8WORKER_ANNUAL_STATIONARY_COVERAGE_FAILED_STOP_NO_RERUN`

The Owner-A corrected-input preflight passed with zero scientific calls.  The
authorized one-time 14-year, eight-worker Python batch subsequently stopped at
2018 with shared failure exit code `1`; no rerun, worker-count change,
calibration change, grid/tolerance change, MATLAB, PLM, comparator, shock, IRF,
R5, or Results action was performed.

## Verified preflight

- Exact years: 2009--2022, excluding 2023.
- Semantic entries: rolling-window 1--14; PLM vintage and calendar row 10--23.
- Corrected capital: `R语言计算资本存量`, verified 2000--2022 segment.
- Scaling: GDP x1000, CAP x1000, POP x100.
- Focused zero-science suite: 76 passed.
- Corrected-2009 anchor: GDP and technology exact/binary64-compatible; POP and
  CAP differences were explicitly Owner-A source-designated representation
  changes.

## Batch record

The batch root is
`D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001`.
It used exactly eight year-level workers with all four BLAS/thread environment
variables pinned to `1` and automatic reruns `0`.

Thirteen years returned `PASS`: 2009--2017 and 2019--2022.  Year 2018 returned
`SHARED_FAIL` / exit `1`.  Its output directory contains the corrected input and
run manifest but no `FAILURE.json`, final state, checkpoint, or terminal table;
the exact exception was not materialized by the runner.  The partial root output
must not be interpreted as accepted 2009--2022 annual stationary coverage.

External immutable evidence is at
`D:\ProjectTemp\ch5-mp4c-owner-a-2009-2022-corrected-8worker-evidence-20260902-002`,
including the Phase-A receipt and batch failure receipt.  The initial,
pre-serialization zero-science attempt is separately preserved under suffix
`-001`.

## Required next gate

A new live task is required before any 2018 diagnostic, source inspection beyond
the preserved artifacts, retry, modified execution, or acceptance claim.  It
must preserve the current batch root and state explicit retry/diagnostic scope.
