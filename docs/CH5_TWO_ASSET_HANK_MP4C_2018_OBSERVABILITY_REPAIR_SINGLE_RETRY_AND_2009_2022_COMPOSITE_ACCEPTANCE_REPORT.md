# MP4C 2018 observable single retry

## Terminal

`MP4C_2018_OWNER_A_CORRECTED_SINGLE_RETRY_PROCESS_EXCEPTION_FAIL__ROOT_CAUSE_CAPTURED__NO_SECOND_RETRY`

The single authorized 2018 retry used an input byte-identical to the original
failed input (`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`),
one subprocess, one worker, and all four thread variables pinned to `1`. It
exited `1`; no second retry was performed.

## Captured root cause

The observable harness persisted stdout, stderr, command, environment,
timestamps, exit code and input identities. Stderr records a `MatrixRankWarning`
for an exactly singular contaminated-row matrix, followed by:

`ValueError: faithful contaminated-row solve is non-finite`

The traceback is in the KFE path invoked through the unchanged production
worker. This is a captured process exception, not a normal solver
nonconvergence (`exit 2` with `FAILURE.json`). No scientific-model change was
made in this task.

## Consequence

The 13 immutable PASS years remain internally sound, but 14-year composite
coverage is not accepted because the sole authorized 2018 retry failed. No
MATLAB, R/PLM, 2023, shock/IRF, R5 or Results work occurred.

Evidence root:
`D:\\ProjectTemp\\ch5-mp4c-owner-a-2018-observable-single-retry-20260903-002`.
The unused pre-launch `-001` root is preserved separately.

## Next gate

A new live task and scientific review are required before any correction to the
KFE contaminated-row path or any further 2018 execution.
