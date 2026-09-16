# CH5 MP4C 2018 KFE D1-D3 Q0 KFE structural-audit arithmetic reaggregation acceptance

Date: 2026-09-16

Reviewer verdict:

`PASS__FAIL_CLOSED_EVIDENCE_ACCEPTED__EXACT_CONSTRUCTION_IDENTITY_REMAINS_RECEIPT_AUTHORITY__SPARSE_REAGGREGATION_EXACT_ZERO_REQUIREMENT_RECLASSIFIED_AS_OVERSTRICT_SECONDARY_AUDIT`

## Accepted evidence

Builder candidate `d4f643f1d26ad5a28395f60a58c545447abda7ba` is accepted as valid fail-closed evidence. The run loaded the exact accepted Q0 once, performed one structural/conservation audit and one `Q0 @ 1` evaluation, then stopped before SCC/SVD because a secondary sparse-matrix off-diagonal reaggregation produced

`max |diag(Q0) + sum(stored offdiagonals by row)| = 3.552713678800501e-15`

instead of exact zero.

All other reached structural checks passed: exact Q0 identity/hash, finite CSR `(800,800)`, zero negative off-diagonals, minimum positive off-diagonal `0.2642984748447064`, `max(abs(Q0@1))=3.552713678800501e-15 <= 5.222144858126786e-14`, and exact-zero outward-face drift/rate/flux ledgers. SCC, GESVD, stationary candidate and `Q0.T@p` were correctly not run.

## Reviewer interpretation

The accepted D2 generator constructs each asset diagonal from a separately accumulated retained-outgoing array and then adds the accepted productivity generator. Its accepted D2 receipt records the construction identity

`max |diag(Q0) + retained_outgoing_total| = 0.0`

exactly. This remains the authoritative **construction identity**.

Recomputing an outgoing total later from the serialized sparse off-diagonal entries is a distinct floating-point reduction with a different accumulation order. Exact bitwise equality between those two reductions is not a scientifically meaningful invariant. The observed `3.552713678800501e-15` is the same scale as the already accepted `Q0@1` residual and is far below the preregistered conservative row-sum bound `5.222144858126786e-14`.

Therefore the failure does **not** indicate a generator defect, source term, leakage, diagonal omission or violation of the D2 construction law. It identifies an overstrict secondary validator condition.

## Frozen repair to the validator contract

The next fresh validation must preserve both checks, with different semantics:

1. **Construction-provenance identity:** accepted D2 receipt/artifact identity remains mandatory and its recorded `diagonal_construction_error` must remain exactly `0.0`.
2. **Independent sparse reaggregation audit:** recompute `diag(Q0) + sum(stored offdiagonals by row)` from the loaded CSR without modifying Q0, and require its maximum absolute discrepancy to be finite and `<= 5.222144858126786e-14`.

The independent sparse reaggregation discrepancy must be persisted exactly. It may not be silently replaced by zero, and the bound may not be fitted or tuned after observation.

No other KFE design contract changes are authorized. In particular: Q0 identity, orientation, F-order, pin-free homogeneous stationarity, SCC rule, full single GESVD, rank/nullity threshold, normalization, nonnegative-mass rule, source-free residual bounds, runtime ceilings and interpretation boundary all remain unchanged.

## Scientific scope

This acceptance authorizes only a fresh rerun of the bounded Q0 operator-level KFE validation after the validator's secondary diagonal audit is corrected as above. It does not authorize V1 remapping, HJB continuation, KFE production integration, steady state, GE, dynamics, IRFs or Results.

Results eligibility remains `FALSE` and production remains unchanged.
