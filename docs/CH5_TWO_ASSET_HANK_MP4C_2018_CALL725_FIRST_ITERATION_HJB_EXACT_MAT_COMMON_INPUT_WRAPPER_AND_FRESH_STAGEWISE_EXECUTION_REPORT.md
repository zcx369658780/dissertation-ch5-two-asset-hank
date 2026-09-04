# MP4C 2018 call-725 exact-MAT common-input first-iteration forensic

## Terminal

`MP4C_2018_CALL725_EXACT_MAT_COMMON_INPUT_FIRST_ITERATION_FORENSIC_BLOCKED__NO_KFE_NO_GE_NO_PRODUCTION_CHANGE`

Classification:

`CALL725_EXACT_MAT_COMMON_INPUT_STAGEWISE_FORENSIC_BLOCKED__NO_PRODUCTION_CHANGE`

## What passed before the scientific budget

- Fresh live continuity passed: `HEAD = origin/main = 51a95bb3d180906fd2b2a0ad1bdc682fe2034cad`, direct parent `0a4e102e80af3681c766e54c21029661922e9304`, ahead/behind `0/0`, clean worktree.
- Bound Git blobs and all four protected MATLAB hashes matched the live task.
- The initialization and MATLAB replay manifests rehashed to `817845439CDC77E2C3873AA3D9675E16704E0AB48263F02CFBD653626245D07C` and `87500FF3121ECBBEE1E18A0A574371E06AC2B03B6B24B13465FCFBBF1E02457B`.
- The authoritative HJB100 MAT artifact `hjb100_initialization.mat` (`1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`) was directly loaded and certified for exact `b`, `ah`, `z`, `v0`, and `l0` float64 values. Canonical binary copies and MATLAB/Python ingestion receipts were persisted.
- The prior JSON-grid path was retained only as a rejected diagnostic: its `b` and `ah` differ from the authoritative MAT values by up to `8.881784197001252e-16`, so it did not feed the strict pair.

## Blocking event

The external MATLAB capture-only wrapper was frozen and syntax-checked, then invoked exactly once for Phase A. It failed while reading its scalar JSON manifest, before derivative construction, policy evaluation, operator assembly, sparse solve, or HJB iteration:

`Unrecognized field name "parameters"` at wrapper line 5 (`p=m.parameters; g=m.grid; n=m.numerics;`).

The supplied historical active-input contract has a different JSON schema. No `matlab_stagewise.mat` was created. Per the live task's no-retry boundary, the wrapper was not repaired or invoked again; Python strict-common Phase B and the conditional native probe were not started.

## Ledger and boundary

- MATLAB wrapper invocations: `1`; completed HJB iterations: `0`.
- Python strict-common iteration 1, Python native probe, KFE, household, GE/stationary/annual, R/PLM, shock/IRF/Results: `0`.
- No production, test, validator, protected MATLAB source, parameter, tolerance, `maxit`, or solver change occurred.

External no-overwrite evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-call725-first-iteration-exact-mat-common-input-20260904-001`

Its audit manifest SHA-256 is:

`1A2A72FA19C7E745F9C5C303FDA10A508A5C342887143BAE385F7F4FD6472E29`

The next action requires a new live GitHub task explicitly authorizing a corrected wrapper scalar-manifest binding and a fresh first-iteration budget. This task does not authorize either action.
