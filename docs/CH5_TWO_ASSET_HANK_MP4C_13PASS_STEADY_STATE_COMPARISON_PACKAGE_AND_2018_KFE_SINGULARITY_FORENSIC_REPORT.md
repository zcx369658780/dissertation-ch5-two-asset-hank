# MP4C 13-pass comparison package and 2018 KFE singularity forensic

## Terminal verdict

`MP4C_13PASS_STEADY_STATE_COMPARISON_PACKAGE_COMPLETE__2018_KFE_SINGULARITY_FORENSIC_COMPLETE__NO_SCIENTIFIC_RERUN`

This task performed zero Python stationary, household/HJB/KFE, annual fixed-point,
MATLAB, R/PLM, comparator, shock/IRF/R5, Results, or 2018-retry calls.

## Authority and continuity

- Fresh-fetched task commit: `77183cccea83e6d6549a8652be75c74917641e85`.
- Direct parent: `c2c7e70a3f546111d05314f13cd7be16c373c5c7`.
- Start and final repository state were clean, `HEAD == origin/main`, with
  ahead/behind `0/0` before this task's bounded report/utilities commit.
- Immutable sources were read-only:
  `D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001`,
  `D:\ProjectTemp\ch5-mp4c-13pass-matlab-comparator-2018-diagnostic-20260903-001`,
  and `D:\ProjectTemp\ch5-mp4c-owner-a-2018-observable-single-retry-20260903-002`.

## Portable package

The fresh no-overwrite root is:

`D:\ProjectTemp\ch5-mp4c-manual-steady-state-comparison-package-20260903-002`

Its ZIP is
`CH5_MP4C_MANUAL_COMPARISON_PACKAGE_2009_2022_13PASS_PLUS_2018_FAILURE.zip`
with SHA-256
`AB0D9CC93C688D1D8EA3C0F6AC7D25B5191B079F06A67A270A70F624E52B354E`
and 668,019 bytes. `package_file_manifest.csv` records every payload member;
the manifest is included as the conventional administrative self-member.

For exactly `2009-2017, 2019-2022`, the package contains the immutable final
state JSON, corrected runtime input JSON, `SUCCESS.json`, run/checkpoint
manifests and timing receipt. It intentionally excludes large NPZ/MAT/NPY
arrays. The standardized steady-state and corrected-input long tables each
have exactly `13 * 31 = 403` rows. All 20 terminal fields in the former are
finite. The Python wide workbook has 14 field sheets plus a README sheet;
2018 is visibly absent rather than zero-filled and 2023 is absent.

`source_artifact_provenance.csv` is a portable 88-record ledger for each
copied source: original absolute path, filename, year, artifact type, source
root, representation, all three semantic indices, status, SHA-256 and bytes.

The protected source workbook was read only at:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\12年稳态值.xlsx`

SHA-256: `FF65B8A0BC27CF9A382C5F00FE1E377575517EE9B5A568976452BFFEAA83CE4B`.
For `稳态值_Yt0`, `稳态值_Yt`, `稳态值_Kt0`, `稳态值_Kt`, `稳态值_Lt0`, and
`稳态值_Lt`, the final complete province block is rows `1273-1303` (not any
of the preceding 41 repeated write blocks). The extracted workbook and six
CSVs state, on every sheet/file:

`LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY__NOT_SAME_INPUT_PARITY_EVIDENCE`

The 1,209-row Yt/Kt/Lt overlap table (13 years x 31 provinces x 3 fields) and
its annual summary use `NOT_SAME_INPUT__DIAGNOSTIC_ONLY`. They are descriptive
manual-comparison material, never a parity PASS/FAIL. The separately accepted
corrected-2009 same-input anchor remains the only cited cross-language anchor;
this task makes no multi-year same-input parity claim.

Both generated workbooks were structurally inspected and all 15 Python and 6
MATLAB-extract sheets rendered successfully. No source workbook was modified.

## 2018 failure package and localization

The original and sole observable retry input SHA-256 is byte-identical:

`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`.

Its frozen binding is year 2018, rolling entry 10, regression vintage 19,
calendar row 19, rolling window 2009-2018. The original batch retained the
input and manifest but no stdout/stderr/traceback; its scheduler mapped a
nonzero code other than 2 to `SHARED_FAIL` without persisting child output.
The retry receipt, stdout, stderr, input, manifests, predecessor reports, and
an exact UTF-8 traceback extract are in the package.

The retry stderr captures `MatrixRankWarning: Matrix is exactly singular` at
`exports/matlab_faithful_two_asset_ha.py:596`, then
`ValueError: faithful contaminated-row solve is non-finite` at line 597.
The preserved chain is the post-loop household adapter line 37, annual worker
lines 174/187, and stationary runtime line 52. The worker catches only
`SteadyStateConvergenceError`; this `ValueError` therefore escaped normal
`FAILURE.json` handling. Existing evidence does not identify province, outer
iteration, household-call number, control state, or a persisted generator:
each is `UNKNOWN_FROM_EXISTING_EVIDENCE`.

## Read-only KFE forensic

The actual annual path uses the export KFE implementation. It transposes the
post-convergence operator, selects zero-based row
`floor(0.37 * state_count) - 1`, zeros that row, sets its diagonal to one, and
solves the contaminated system with RHS `0.007` at that same row. It then
normalizes raw mass by `sum(raw) * db * da`. Nonfinite raw values and invalid
normalization fail closed; there is no fallback, retry, regularization, or
alternate solver path.

For a finite conservative generator with a unique stationary null direction,
replacing one equation with a normalization constraint ordinarily removes the
singularity. Exact singularity can generally be consistent with more than one
null direction, multiple closed communicating classes, reducibility, or
disconnected mass blocks. The retained 2018 evidence does **not** establish
which, if any, of those mechanisms caused the event. The package's hypothesis
matrix distinguishes the directly observed singular system from possible and
unresolved mechanisms, and its 2017/2018/2019 input table records numerical
steps without assigning causality.

## Program-correctness boundary

The package includes a separate evidence map. Strong evidence remains the
previous household/HJB/KFE MATLAB-faithful gates, corrected-2009 same-input
stationary parity, 13 internally converged finite Owner-A annual outputs, the
independently reproduced 2000-2022 CHNCapitalStock segment, and explicit
calendar/index/scaling contracts. It does not prove annual 2010-2022
same-input MATLAB parity, 2018 stationary-distribution correctness, a 2023
extension, or shock/IRF results.

No KFE mutation and no further 2018 execution are authorized by this result.
