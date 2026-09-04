# MP4C 2018 call-725 post-call residual repair and first-iteration forensic closure

## Authority and scope

This report closes the predecessor execution task through the successor
zero-science evidence-closure task
`CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_ZERO_SCIENCE_EVIDENCE_CLOSURE_AND_REPORT_PUBLICATION_RECOVERY`.
The successor was read from live `origin/main` at
`9b223e65fff44277b66de7e569fe6c31296bb316`, direct child of
`9463531cbd0091326b7b736a6f0045ad6ef9cc79`; its task blob is
`585d6c983fe62471f0679f19d5eeb39ffc71fb23`.

The closure task performed only static reads, hashes, line diffs,
serialization/readback checks, and comparisons of already-persisted artifacts.
It made no MATLAB/Python scientific call, native-init probe, retry, HJB/direct
solve rerun, derivative regeneration, source repair, tolerance change, KFE,
GE/stationary/annual, R/PLM, shock/IRF, or Results call.

## Zero-science certification recovery

The exact predecessor/repaired wrapper sources were recovered and compared
line by line. The MATLAB diff consists only of the wrapper-name change,
persistence-before-diagnostics, readback assertion, `updated(:)` residual
vectorization, and diagnostic append. The Python diff preserves its direct
solve expression through `reshape(shape, order='F')`; changes only move
persistence ahead of diagnostics, retain RHS, add a core readback assertion,
and use F-order `v1` vectorization for diagnostics. Every changed line is
classified `POST_CALL_INSTRUMENTATION_OR_PERSISTENCE_ONLY` or
`NON_SCIENTIFIC_DEFENSIVE_ASSERTION_ONLY`.

The authoritative HJB100 initialization MAT re-hashed to
`1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`.
Its direct-loaded `b`, `ah`, `z`, `v0`, and `l0` fields match the predecessor's
canonical Fortran-order payload digests. The predecessor scalar binding
re-hashed to
`A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`;
all frozen provenance, scalar, numerical, and switch-matrix values match the
task contract. Static source-region equality through the direct solve also
passed.

## Preserved calls and earliest stage

The durable call ledger is unchanged:

| Call category | Count |
| --- | ---: |
| MATLAB exact-MAT/common-scalar first iteration | 1 |
| Python exact-MAT/common-scalar first iteration | 1 |
| Python native-init probe; retries | 0; 0 |
| KFE; GE/stationary/annual; R/PLM; shock/IRF/Results | 0; 0; 0; 0 |

The persisted MATLAB core artifact
`matlab_core_stagewise.mat` has SHA-256
`B863BBE5A3CF6327954C71520F609B9949FE9DEF64BA5225AA4CE9661392B69E`;
the Python strict-common artifact
`python_strict_stagewise.npz` has SHA-256
`CEAE235AC0DC62C1FCD0D9728F840DEEA1E12038ABFCE73CA0DA6BD449CE915F`.
Their persisted arrays were independently reread under the frozen
`128 * eps64` machine rule. Old/V0 and raw `va_f` / `va_b` are exact. The
earliest material stage is raw liquid derivatives:

| Stage | Material entries | Maximum absolute difference |
| --- | ---: | ---: |
| raw `vb_f` | 40 | 0.01228045195367922 |
| raw `vb_b` | 40 | 0.012844718557132808 |

This earlier source-parity break controls classification. The conditional
native-init probe remains forbidden and was not run; no later-stage result is
used to override or reclassify this earliest divergence.

## Finite evidence closure

The predecessor root was read-only. The first fresh no-overwrite closure root
contains the recursive inventory of all 28 regular predecessor-root files,
including the cache file, and the line-diff, MAT identity, scalar equality, and
persisted-artifact receipts. Its expression receipt was then superseded without
overwriting it by the monotonic fresh root
`D:\ProjectTemp\ch5-mp4c-2018-call725-zero-science-evidence-closure-20260904-002`.
That final root re-hashes every substantive first-root artifact and records the
complete compared wrapper paths, full-file hashes, exact source regions, and
normalized direct-solve comparison method.

The final finite, non-self-referential closure manifest has SHA-256
`BFA87A4B2DCB2D4E8A439994836D9D627368B6244564106FC3EE89D5FF28EC29`.
The detached final readback receipt has SHA-256
`5F2184C992FEA1C676B2064FC84A6FF5765B87B7E7F82003BE2982115F081A2E`.
The final manifest covers all substantive final-root artifacts except itself
and that detached receipt, exactly as required by the successor task.

## Classification and boundary

All ten successor evidence-closure gates passed. The supported classification
is:

`CALL725_FIRST_ITERATION_PRE_SOLVE_SOURCE_PARITY_BREAK_CONFIRMED__EARLIEST_STAGE_IDENTIFIED__NO_PRODUCTION_CHANGE`

This is a first-iteration forensic classification only. It does not authorize a
derivative or production repair, further iterations, KFE, GE, annual work,
R/PLM, shock/IRF, or Results work.

## Terminal

`MP4C_2018_CALL725_ZERO_SCIENCE_EVIDENCE_CLOSURE_COMPLETE__PRE_SOLVE_DERIVATIVE_BREAK_DURABLY_CERTIFIED__NO_RERUN_NO_KFE_NO_GE_NO_PRODUCTION_CHANGE`
