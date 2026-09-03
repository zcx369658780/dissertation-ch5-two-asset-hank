# MP4C 2018 nullspace numerical-consistency and SVD-driver cross-check

## Terminal

`MP4C_2018_NULLSPACE_NUMERICAL_CONSISTENCY_CROSSCHECK_COMPLETE__GAUGE_CONCLUSION_CONFIRMED_OR_CORRECTED__NO_REPAIR_NO_RERUN`

## Scope and identity

This is read-only dense linear algebra over already captured matrices.  No 2018
rerun, scientific PID, stationary, household, HJB, KFE, MATLAB, R/PLM, density
solve, `spsolve`, shock, or IRF call occurred.  No model, production worker,
diagnostic, test, controller, HJB, or KFE source was modified.

- Live authority at start: `ddd35b7353714ff1dbecc92b1c814b76222f4cff`, direct
  child of `7bd5a7c7fe4ba486ec21dd1481dee79ecfeb200f`.
- Start state after fast-forward and fetch: `HEAD == origin/main ==
  ddd35b7353714ff1dbecc92b1c814b76222f4cff`, ahead/behind `0/0`, and clean
  tracked worktree.
- Preserved root:
  `D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`.

The identity gate passed for the retrospective manifest
`D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490`, A
`A17AA9CF512D4D3FDD79235D0D1897CFB20486D2EF5FAA68850910C849AA1B42`, A transpose
`7C1ADEDEE5B26BB30B5A8CC1C9D3D0E83DFF18FAE7860C39986E9E6C2D8FDA66`, and B
`B04F5A4B99135272FCFF61BEAE220A2C25F5455E478F7994C1394CD6EC869EF4`.

The permanent limitation remains:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`

The accepted retrospective identity gate certifies current preserved bytes; it
does not turn the historical absence of a capture-time raw-hash manifest into a
capture-time proof.

## Environment and method

The 800 by 800 captured A transpose (3,106 stored entries) was converted to a
float64 dense array without altering its entries, rows, or sparsity.  The
maximum absolute stored rate is `152123993.47991544`.  The process used Python
3.11.9, NumPy 2.4.6, SciPy 1.17.1, with OMP/MKL/OpenBLAS/NUMEXPR thread limits
all set to one.  The recorded LAPACK entry points are `dgesdd` and `dgesvd`.
Full library configuration is retained in the external environment artifact.

On the same unscaled dense A transpose, the following completed once each:

| Method | Driver | Smallest singular value | Largest singular value |
| --- | --- | ---: | ---: |
| `numpy.linalg.svd` | NumPy default | `2.1488433480633367e-08` | `215129122.7381978` |
| `scipy.linalg.svd` | `gesdd` | `2.1488433480633367e-08` | `215129122.7381978` |
| `scipy.linalg.svd` | `gesvd` | `3.674373165385648e-15` | `215129122.7381978` |
| `numpy.linalg.svdvals` | NumPy default | `3.674373165385648e-15` | `215129122.7381978` |
| `scipy.linalg.svdvals` | SciPy default | `3.674373165385648e-15` | `215129122.7381978` |

For every method the first 15 values of the 16-value tail agree to the reported
precision; only the last value is driver/mode dependent.  The complete tails
are persisted in `singular_value_tails.json` and bound by the external audit
manifest.

## Reconciliation of the predecessor discrepancy

The original postmortem value `2.824569525631866e-15` was a values-only dense
SVD tail.  It is not bit-for-bit reproduced in this current NumPy/SciPy stack,
but it agrees in scale and numerical regime with the current values-only/
`gesvd` tail, `3.674373165385648e-15`.  It does not agree with the vector-
returning `gesdd` result, `2.1488433480633367e-08`.

Thus the predecessor forensic's use of `2.1488433480633367e-08` together with
an apparent near-null vector was a material numerical-consistency gap, not
evidence of two different captured matrices.  The current cross-check shows
that the conflict is localized to the extreme bottom singular value of the same
ill-conditioned float64 matrix and is LAPACK-driver/mode dependent.  The ratio
between successful unscaled extrema is `5848190.293534877`; no exact algebraic
rank is inferred from either tail.

## Paired singular-vector check

For each vector-returning decomposition, its own last right singular vector was
separately L2-normalized and multiplied directly by the same A transpose.

| Driver | Reported sigma min | Direct `||A'v||2` | Relative difference | `v[295] / max(abs(v))` |
| --- | ---: | ---: | ---: | ---: |
| NumPy default / `gesdd` | `2.1488433480633367e-08` | `5.943759622974463e-13` | `0.9999723397257956` | `3.529503652146397e-14` |
| `gesvd` | `3.674373165385648e-15` | `1.0119384438046227e-13` | `0.9636897561518567` | `1.5266397729935424e-17` |

None of these direct residuals agrees materially with its decomposition's own
reported bottom singular value.  Per task rule, each vector/SVD pair is
therefore **unreliable for certifying the absolute bottom singular value**.
This does not license a retry or alternate scientific calculation.

The unscaled vectors nevertheless have sign-invariant cosine overlap exactly
`1.0` for every pair (the two `gesdd`/NumPy vectors coincide, and the `gesvd`
vector differs only by sign).  Their faithful-row components are all negligible
at the displayed scale.  This is evidence for a stable numerical near-null
*direction*, not a certification of an exact singular value.

## Scaling robustness

The full vector-returning scaling check was performed on
`A_scaled = A' / 152123993.47991544` in a separate fresh no-overwrite correction
root after preserving an earlier root whose vector-returning scale argument was
not applied.  The earlier unscaled results and its valid values-only scaled
results were retained; no file was overwritten.  The correction root exists
solely to make the required scaled vector calls correctly.

| Scaled decomposition | Scaled sigma min | Mapped original-unit sigma min | Direct original-unit residual |
| --- | ---: | ---: | ---: |
| NumPy default / `gesdd` | `1.4125604376493637e-16` | `2.148843348069583e-08` | `4.3429315078486653e-13` |
| `gesvd` | `3.1594617046666914e-23` | `4.806299317607583e-15` | `1.460501487368569e-13` |

Scaling preserves the driver split and the paired-residual inconsistency; it
does not resolve the bottom-value ambiguity.  This supports a floating-point
conditioning/driver-behavior explanation for the `1e-15` versus `1e-8`
conflict, rather than a changed matrix, changed sparsity, or new scientific
execution.

## Rank tolerance and qualitative gauge check

For all successful unscaled spectra, the predecessor tolerance and NumPy's
default/`eps * max(shape) * sigma_max` tolerance coincide at
`3.821460885301736e-05`; numerical rank is 799 and nullity 1.  At relative
tolerances `sigma_max * 1e-12`, `1e-14`, and `1e-16` — respectively
`0.0002151291227381978`, `2.151291227381978e-06`, and
`2.151291227381978e-08` — all five spectra still give rank 799 and nullity 1.
These are numerical-rank conventions only, not an exact-algebraic-rank claim.

Because no vector/SVD pair certifies the absolute bottom singular value, the
least-mismatched, cross-driver-aligned **near-null witness** (`gesvd`) was used
only for the prescribed B and row-rank checks.  With the same `gesvd` driver
and predecessor tolerance:

| Check | Result |
| --- | --- |
| witness `v[295]` | `-7.416589004572169e-18` after L2 normalization (`1.5266397729935424e-17` after max-abs normalization) |
| `||Bv||2` | `1.0119051627067357e-13` |
| unit-row replacement at 295 | rank 799, nullity 1, smallest singular `3.781768064500847e-15` |
| unit-row replacement at 620 | rank 800, nullity 0, smallest singular `0.0009447159791128249` |

Accordingly, under the explicitly stated numerical convention, **row 295
remains an ineffective gauge and row 620 removes the dominant numerical
near-null direction**.  This is a qualitative conclusion; it is not a KFE
repair instruction and no density was solved.

## Source-faithful conservation note

The current source `assemble_source_axis` was read as evidence only (source
SHA-256 `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`).
It explicitly truncates outward boundary offdiagonals while always retaining
the diagonal contribution `-(backward + forward)`.  Boundary row sums may
therefore be nonzero under this source-faithful contract.  This task does not
classify the predecessor boundary nonconservation as a
`PYTHON_IMPLEMENTATION_DEFECT` and makes no repair.

## Evidence roots and classification

Primary cross-driver evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-nullspace-numerical-consistency-crosscheck-20260904-001`

Its 13 produced files, including all required cross-driver CSV/JSON artifacts,
hash to its audit manifest, SHA-256
`BADBF868D9B6F6ACA081A8D9634D44EAD938554AE5E1BC3D6BBD969578E8D221`.

The preserved scaling correction root is:

`D:\ProjectTemp\ch5-mp4c-2018-nullspace-numerical-consistency-crosscheck-20260904-002`

Its audit-manifest SHA-256 is
`81DFE81FF90D930DAABFFDFB5A998687234E8CDCDAC4C621CB51BC4223969B9E`.
Both manifests record zero scientific calls, zero density solves, and zero
`spsolve` calls.

The strongest supported classification is:

`NULLSPACE_FORENSIC_QUALITATIVE_GAUGE_RESULT_CONFIRMED__BOTTOM_SINGULAR_VALUE_DRIVER_DEPENDENT`

The numerical correction is precise: the earlier absolute-singular-value and
paired-vector wording cannot be treated as an exact nullspace certificate.  The
row-295/row-620 qualitative gauge finding survives the consistent cross-driver
and rank-only checks.  No repair, rerun, coverage/parity acceptance, Results
claim, or new scientific route is authorized by this report.
