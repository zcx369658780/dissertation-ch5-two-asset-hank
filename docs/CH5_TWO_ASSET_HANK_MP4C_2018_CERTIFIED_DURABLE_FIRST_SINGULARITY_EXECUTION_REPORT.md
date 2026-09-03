# MP4C 2018 certified durable first-singularity execution report

## Terminal

`2018_FIRST_SINGULARITY_NOT_REPRODUCED_IN_CERTIFIED_DURABLE_EXECUTION__NO_SECOND_RUN`

The one authorized durable 2018 child terminated normally with
`COMPLETED_WITHOUT_FIRST_SINGULARITY`.  The certified diagnostic did not observe
a `MatrixRankWarning` or a non-finite contaminated-row solve.  No retry, repair,
alternative solver, regularization, pseudoinverse, or second child was used.

## Authority and frozen scope

- Live task authority: `c1b1ce367cbc37458dee505511705c045b9ad2ad`, a direct
  child of `ebf8f8d91aebdd940ee285670b30677d5bae487e`.
- Pre-launch repository state was clean and synchronized at that authority.
- The certified recorder remained identical to predecessor Git blob
  `fbce4c6d7fc1c38cea5b57566da96d6326f93ef4`; its run SHA-256 was
  `B8326F611D37869F0EF3183CADBA4EFA652920191951FABF8E913CD5D84192CF`.
- No diagnostic, test, HJB, KFE, adapter, stationary-runtime, input-adapter,
  calibration, grid, controller, or frozen-input source was modified.

## Frozen 2018 input

The child consumed the designated preserved input
`calendar_2018_matlab_runtime_cache_input.json` with SHA-256
`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`.

- Calendar binding: 2018, rolling entry 10, PLM vintage 19, calendar row 19,
  and window 2009–2018.
- Province axis: exact 31-province order.
- Source-to-model factors: `GDP` ×1000, `R语言计算资本存量` ×1000, and
  `就业人数` ×100.
- The input explicitly records `no_2023_scientific_input: true`.

## One-child execution evidence

- One detached local child, PID `8420`, launched with Python 3.11.
- Worker count, scientific-child count, and subprocess count were each one.
- `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, and
  `NUMEXPR_NUM_THREADS` were each pinned to `1`.
- Automatic reruns: zero.  The bounded-science ledger records
  `diagnostic_run_count: 1` and `reruns: 0`.
- The child started 2,015 household calls.  Both durable CSV ledgers contain
  one header and 2,015 data rows.
- Captured stdout and stderr are empty; no unhandled-exception traceback was
  produced.

## Singularity and postmortem disposition

No first singularity was captured.  Accordingly, none of the five required raw
artifacts exists: operator A, A transpose, contaminated matrix, RHS, and raw
solve vector.  The read-only postmortem was therefore not invoked.  This is
required by the task; postmortem without all five raw artifacts is forbidden.

The normal completion does not authorize acceptance of 2009–2022 coverage,
MATLAB/Python parity claims, Results claims, a repair, or any rerun.

## Evidence

Fresh no-overwrite evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-certified-durable-first-singularity-execution-20260903-001`

It contains the preflight and launch identities, frozen-input identity,
scientific-code manifest, both durable ledgers, terminal sentinel, execution and
bounded-science receipts, child-exit receipt, empty stdout/stderr, and the
SHA-256 audit manifest.

## Next boundary

This task is complete and fail-closed.  Any interpretation, new diagnostic
route, repair, or additional scientific execution requires a new live task with
explicit authority.
