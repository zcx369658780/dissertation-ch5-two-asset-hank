# CH5_TWO_ASSET_HANK_MP4C_2018_NULLSPACE_NUMERICAL_CONSISTENCY_AND_SVD_DRIVER_CROSSCHECK

Date: 2026-09-04

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / read-only numerical-consistency analyst

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`7bd5a7c7fe4ba486ec21dd1481dee79ecfeb200f`

with terminal:

`MP4C_2018_CAPTURED_OPERATOR_NULLSPACE_AND_CONTAMINATED_ROW_FORENSIC_COMPLETE__PROXIMAL_CAUSE_CLASSIFIED_OR_BOUNDED__CAPTURE_TIME_HASH_GAP_EXPLICIT__NO_REPAIR_NO_RERUN`

The predecessor established a strong proximal gauge-row hypothesis, but its published numerical report contains one material internal-consistency issue that must be resolved before any KFE repair decision.

Published predecessor facts that appear inconsistent for the same captured `A.transpose()` are:

1. the original execution postmortem reported smallest singular value approximately `2.824569525631866e-15` for `A.transpose()`;
2. the later forensic report states dense-SVD smallest singular value `2.1488433480633367e-08`;
3. the same later forensic reports a candidate vector `v` with `||A'v|| = 1.2795425290966635e-12` after `max(abs(v))=1` normalization.

For a correctly paired right singular vector and singular value of the same unscaled matrix, these values cannot be accepted without reconciliation. This task is therefore a zero-model, read-only numerical certification of the nullspace computation itself.

## 2. Hard boundary

Task type:

`READ_ONLY_CAPTURED_MATRIX_NUMERICAL_CONSISTENCY__NO_MODEL_RERUN__NO_REPAIR`

Forbidden:

- any new 2018 scientific execution;
- stationary / household / HJB / KFE model calls;
- MATLAB or R/PLM execution;
- any new scientific PID;
- any density solve or `spsolve`;
- any production/model/diagnostic/test source modification;
- any contaminated-row production change;
- regularization, pseudoinverse, fallback, parameter/grid/controller edits;
- shock/IRF/Results work.

Any helper code must live only in a fresh external analysis root and consume already captured matrices as data.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `7bd5a7c7fe4ba486ec21dd1481dee79ecfeb200f`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read `AGENTS.md`, all CURRENT rules, the final 2018 execution report, retrospective integrity report, and the predecessor forensic report.

## 4. Evidence identity gate

Preserved execution root:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`

Require retrospective manifest SHA-256:

`D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490`

Require current raw hashes:

- A: `A17AA9CF512D4D3FDD79235D0D1897CFB20486D2EF5FAA68850910C849AA1B42`
- A transpose: `7C1ADEDEE5B26BB30B5A8CC1C9D3D0E83DFF18FAE7860C39986E9E6C2D8FDA66`
- contaminated matrix: `B04F5A4B99135272FCFF61BEAE220A2C25F5455E478F7994C1394CD6EC869EF4`

Permanent caveat:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`

Any hash mismatch: STOP.

## 5. Reproduce the conflicting singular-value claims

Using the exact current captured `A.transpose()` bytes, compute the smallest tail of the singular spectrum with clearly recorded library/version/driver details.

At minimum run, where available:

1. `numpy.linalg.svd(A_dense, full_matrices=False)` and retain both `s` and `vh`;
2. `numpy.linalg.svdvals(A_dense)`;
3. `scipy.linalg.svd(A_dense, full_matrices=False, lapack_driver='gesdd')`;
4. `scipy.linalg.svd(A_dense, full_matrices=False, lapack_driver='gesvd')`;
5. `scipy.linalg.svdvals(A_dense)` with its actual driver/version recorded.

Do not silently substitute values from different decompositions.

For each successful method persist at least the smallest 16 singular values.

If a method errors or fails, record once and continue with the remaining methods; do not repeatedly tune or retry iterative solvers.

## 6. Singular-vector pairing check

For every decomposition returning singular vectors:

- take the right singular vector corresponding to that decomposition's smallest reported singular value;
- normalize it by `||v||_2 = 1` and separately by `max(abs(v)) = 1` for reporting;
- verify directly:
  `||A'v||_2`;
- verify the SVD identity:
  `||A'v||_2 / ||v||_2` should agree with that decomposition's paired smallest singular value within a numerically explained tolerance;
- record `v[295]`, `abs(v[295])/max(abs(v))`, and cosine/sign-invariant overlap with vectors from other successful decompositions.

If a reported singular value and its own paired vector residual disagree materially, classify that numerical method/output as unreliable for the bottom singular mode.

## 7. Scaling robustness

Because the matrix contains rates up to about `1.5e8`, repeat the dense SVD diagnostics on deterministic scalar-scaled copies only:

- `A_scaled = A' / max(abs(A'.data))`;
- optionally `A' / ||A'||_2` if practical after the first decomposition.

Map the scaled singular values back to original units.

The objective is to determine whether the `1e-15` versus `1e-8` discrepancy is an ill-conditioning / LAPACK-driver artifact.

Do not alter rows, sparsity, or scientific content.

## 8. Rank-tolerance robustness

For the same singular-value tails, report numerical rank/nullity under explicit tolerances:

- predecessor tolerance `3.821460885301736e-05`;
- NumPy default matrix-rank tolerance;
- scale-aware tolerances based on `eps * max(shape) * sigma_max`;
- relative thresholds `sigma_max * 1e-12`, `1e-14`, and `1e-16` where meaningful.

Do not equate one numerical-rank convention with exact algebraic rank.

## 9. Recheck B and row-replacement theorem with one certified vector

Only after choosing the best-supported numerical null/near-null vector from the cross-driver analysis:

- compute `||Bv||_2`;
- record `v[295]`;
- repeat the rank-only row checks for row 295 and row 620 using the same SVD driver and the same rank tolerance convention.

No density solve and no `spsolve`.

The task is not to discover a new repair. It is only to confirm whether the predecessor qualitative conclusion — row 295 is an ineffective gauge while row 620 removes the dominant numerical null direction — survives a consistent decomposition.

## 10. Source-faithful conservation note

Read the current faithful source only as source evidence. Record that `assemble_source_axis` explicitly truncates outward boundary off-diagonals while retaining their diagonal contribution, and the module authority states that boundary row sums may be nonzero.

Therefore do not classify the predecessor's boundary nonconservation findings as a Python implementation defect in this task.

## 11. Required classification

The report must select the strongest supported result among:

- `NULLSPACE_FORENSIC_NUMERICALLY_CONFIRMED__CROSS_DRIVER_SINGULAR_VECTOR_AND_RESIDUAL_CONSISTENT`;
- `NULLSPACE_FORENSIC_QUALITATIVE_GAUGE_RESULT_CONFIRMED__BOTTOM_SINGULAR_VALUE_DRIVER_DEPENDENT`;
- `PREDECESSOR_NULLSPACE_NUMERICAL_CLAIM_REQUIRES_CORRECTION__GAUGE_CONCLUSION_REMAINS_OR_FAILS_AS_SPECIFIED`;
- `NULLSPACE_NUMERICAL_CONSISTENCY_REMAINS_UNRESOLVED__NO_REPAIR_AUTHORIZED`.

The exact `2.824...e-15` versus `2.148...e-08` discrepancy must be explicitly reconciled or left as unresolved; it may not be ignored.

## 12. Evidence root

Preferred fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-nullspace-numerical-consistency-crosscheck-20260904-001`

Persist at minimum:

- `source_evidence_identity.json`;
- `library_and_lapack_environment.json`;
- `svd_driver_crosscheck.csv`;
- `singular_value_tails.json`;
- `singular_vector_residual_crosscheck.csv`;
- `singular_vector_overlap.csv`;
- `scaling_robustness.json`;
- `rank_tolerance_robustness.csv`;
- `certified_vector_b_and_row_check.json`;
- `classification.json`;
- analysis stdout/stderr;
- `audit_manifest.json` for this new analysis root only.

## 13. Report and publication

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_NULLSPACE_NUMERICAL_CONSISTENCY_AND_SVD_DRIVER_CROSSCHECK_REPORT.md`

If analysis completes consistently, only one report-only commit + push is authorized.

Suggested commit message:

`Cross-check MP4C 2018 nullspace numerics`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean.

PASS terminal:

`MP4C_2018_NULLSPACE_NUMERICAL_CONSISTENCY_CROSSCHECK_COMPLETE__GAUGE_CONCLUSION_CONFIRMED_OR_CORRECTED__NO_REPAIR_NO_RERUN`

Blocked terminal:

`MP4C_2018_NULLSPACE_NUMERICAL_CONSISTENCY_CROSSCHECK_BLOCKED__NO_REPAIR_NO_RERUN`

No repair task is authorized inside this task.