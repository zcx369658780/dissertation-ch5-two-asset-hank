# Chapter 5 Beijing unique-closed-class KFE method-candidate diagnostic

## Terminal classification

`PASS__UNIQUE_CLOSED_CLASS_RESTRICTED_KFE_CANDIDATE_DIAGNOSTIC__OWNER_METHOD_ADOPTION_DECISION_REQUIRED`

This is a numerical-method candidate diagnostic only. The accepted KFE method remains unchanged and the 31-province run was not reopened.

## Q_CC structural checks

- Shape: `[400, 400]`; nnz: `1537`; finite: `True`.
- Closed-to-transient positive outgoing count/rate: `0` / `0`.
- Maximum absolute stable Q_CC row sum: `1.4988010832439613e-15` against `1.9355021455918682e-14`.

## Restricted GESVD

- sigma_max: `18.892884771371254`; second-smallest: `0.086386749020040135`; smallest: `1.4166892406619692e-18`.
- Local 400 threshold: `1.946509294618518e-12` -> rank/nullity `399/1`.
- Inherited 800-dimension convention: `3.624534548600321e-12` -> rank/nullity `399/1`.

## Restricted and embedded candidates

- Closed candidate min/max: `3.4169927217543985e-07` / `0.15047341337280534`; negative count `0`; math.fsum `1`.
- Embedded transient positive-zero bit patterns: `400/400`; negative count `0`; math.fsum `1`.

## One full-Q stationarity validation

- Residual infinity/L1: `2.325020736918329e-16` / `1.9932610131266322e-14`.
- Signed residual sum: `2.910108745234237e-17`; normwise backward ratio: `7.1972958897565971e-17`.
- Frozen stationarity bound: `6.1974273048065135e-13`; source identity discrepancy: `1.1719884465940349e-17`.

## Comparison with persisted run003 full-space p

- Run003 transient signed/L1 mass: `-1.0085295212390263e-11` / `1.0090064860097144e-11`.
- Closed max-abs/L1 difference: `1.5158707622475731e-12` / `1.0085356535968933e-11`.
- Closed cosine similarity: `1`.
- Mass-accounting discrepancy after transient leakage identity: `-1.9278790958386809e-16`.

All task-forbidden calls are zero. Exactly one restricted GESVD, one orientation, one normalization, and one original full-Q `Q.T@p_full` were executed. No method adoption occurred.
