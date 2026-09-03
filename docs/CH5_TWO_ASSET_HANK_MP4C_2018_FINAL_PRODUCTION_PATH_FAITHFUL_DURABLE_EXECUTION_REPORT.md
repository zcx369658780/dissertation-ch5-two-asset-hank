# MP4C 2018 final production-path-faithful durable execution

## Terminal

`MP4C_2018_FINAL_PRODUCTION_PATH_FAITHFUL_FIRST_SINGULARITY_CAPTURED__POSTMORTEM_CLASSIFIED_OR_BOUNDED__NO_REPAIR_NO_RETRY`

The one authorized 2018 scientific child completed fail-closed after its first
captured KFE singularity.  The required raw artifacts were durable before the
child stopped; read-only postmortem was run only after that termination.  This
is not a 2009–2022 coverage/parity/Results acceptance, and it makes no
root-cause conclusion.

## Authority and frozen identity

- Live authority at launch: `95b122e858b6b3e364fedd8e40eb27f7b2c8c3c5`.
- Required direct parent: `a72de261f53c36f9c21d8193b8e4dd56bf3bfa3a`.
- Launch preflight verified `HEAD == origin/main`, ahead/behind `0/0`, and a
  clean tracked worktree.
- No source or test file was modified.

| Frozen component | Git blob |
| --- | --- |
| diagnostic | `a021b0749f572846a264ad206a2250dae3285e5b` |
| focused tests | `158cab1bdaa1f08678890243ce7b1f61a6363354` |
| annual production worker | `7473e04418744d745000afb21d84588273cc5bca` |
| faithful HA export | `9e7dc9556a2b76811e78f89999abecc045886106` |
| post-loop adapter | `0033baee136c0328e80ffb8b794a88d4405c976c` |
| one-turn | `e5d6835cdc9e6d182e1c84e11f4d51938be592e1` |
| stationary runtime | `8717cfa759948bd1ad3c8cd788f8f4736f250598` |
| steady-state controller | `5c5b56e6a2eb82fab4e80eb7b8e5bbbf97f08c22` |
| Owner-A adapter | `f89927c7a6234cf1c5106318b2b4249183b90cce` |

## Frozen input and one-child proof

- Input SHA-256:
  `F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`.
- Binding: 2018 calendar year; rolling entry 10; PLM vintage 19; calendar row
  19; 2009–2018 window; 31 provinces; GDP ×1000; CAP
  `R语言计算资本存量` ×1000; POP `就业人数` ×100; no 2023 input.
- Scientific PID: `67056`; Python `3.11.9`; launch UTC:
  `2026-09-03T12:08:50.3947587Z`.
- Thread environment: `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`,
  `OPENBLAS_NUM_THREADS=1`, and `NUMEXPR_NUM_THREADS=1`.
- Receipts record one scientific child, one worker, one subprocess, and zero
  automatic reruns.  The PID had exited before postmortem started.

## Durable execution evidence

External no-overwrite evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`

- `household_call_ledger.csv`: 725 data rows, SHA-256
  `78F1BAFC3664D1ED644293FE98FA384468B23291F9CE8E42400EE0F63BB06A9F`.
- `hjb_return_ledger.csv`: 725 data rows, SHA-256
  `7D914989AD3CD047FA45CABA5A9209563465BE1799410BB01699F51CF542DA3F`.
- Terminal sentinel and execution receipt both record
  `FIRST_SINGULARITY_CAPTURED_FAIL_CLOSED`, `first_capture=true`, 725 started
  household calls, and no normal-completion summary.
- First capture localization: outer iteration 24, call 725, province 安徽
  (0-based index 11).  Recorded HJB state: not converged, 100 iterations,
  convergence statistic `0.3038218386543494`, and
  `MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE` KFE path.
- Raw capture includes A, A transpose, contaminated matrix, RHS, raw solve
  vector, context/HJB records, and warning/traceback.  The warning is
  `MatrixRankWarning: Matrix is exactly singular`; the raw vector has 800
  non-finite entries.

## Read-only postmortem

- Operator shape/nnz: 800×800 / 3106; finite stored data: true.
- Maximum absolute row-sum residual: `5.209558481541731`.
- Diagonal range: `[-152123993.47991544, -0.3419303928413932]`; off-diagonal
  range: `[0.002778298838661253, 152113673.94362345]`; positive off-diagonal
  count: 2306.
- Zero-outflow states: none; isolated states: none; SCC count: 139; closed SCC
  count: 3, with sizes 2, 24, and 4.  Exact members are retained in
  `postmortem_scc_closed_classes.json` in the external evidence root.
- A transpose: rank 799, nullity 1; contaminated matrix: rank 799, nullity 1.
  Both use `numpy.linalg.svdvals_dense_float64` with tolerance
  `3.821460885301736e-05`; their smallest reported singular values are
  `2.824569525631866e-15` and `6.140548357084362e-16`, respectively.

## Boundaries

No repair, retry, alternate solver, parameter/controller change, second
scientific child, shock, IRF, or Results claim was made.  The external evidence
is retained outside Git; this commit publishes only this text report.
