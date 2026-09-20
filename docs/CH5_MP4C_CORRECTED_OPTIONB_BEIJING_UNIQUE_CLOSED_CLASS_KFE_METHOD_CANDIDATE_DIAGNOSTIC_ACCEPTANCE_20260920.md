# Chapter 5 Beijing unique-closed-class KFE method-candidate diagnostic acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_PASS__UNIQUE_CLOSED_CLASS_RESTRICTED_KFE_CANDIDATE_DIAGNOSTIC__OWNER_METHOD_ADOPTION_DECISION_REQUIRED`

## Accepted candidate

- live-main baseline: `39ea65985cab75f99c820bf9b9c7004bc8cc76b7`
- Builder candidate: `bb5f2796b0d1b8a8c56dda40afa898cc7f8da315`
- candidate tree reported/read back by Builder: `21b9770f9991326736fc7a4009d494c4b01d537a`
- ancestry independently verified: `1 ahead / 0 behind`, merge-base exactly baseline
- independently verified changed paths: 19
  - validator: 1
  - focused test: 1
  - report: 1
  - evidence: 16
  - CURRENT files: 0
- Builder did not merge main and did not publish a successor.

The candidate has been fast-forwarded into live `main`.

## Diagnostic acceptance

The unique-closed-class restricted KFE method candidate is numerically supported for the accepted Beijing checkpoint-12 Q.

### Closed-class structure

- Q_CC shape: `400 x 400`
- Q_CC nnz: `1537`
- finite: PASS
- minimum off-diagonal: `0.010064816171231113`
- closed-to-transient positive outgoing count/rate: `0 / 0`
- maximum absolute Q_CC row sum: `1.4988010832439613e-15`
- accepted conservation bound: `1.9355021455918682e-14`.

### Restricted GESVD

Exactly one full dense `scipy.linalg.svd` with `lapack_driver="gesvd"`, `full_matrices=True`, `check_finite=True` was used.

- sigma_max: `18.892884771371254`
- second-smallest: `0.08638674902004014`
- smallest: `1.4166892406619692e-18`
- local-dimension threshold: `1.946509294618518e-12` -> rank/nullity `399/1`
- inherited-800 threshold: `3.624534548600321e-12` -> rank/nullity `399/1`.

Both preregistered views agree.

### Closed-class stationary candidate

After exactly one sign orientation and one normalization:

- `math.fsum=1.0`
- minimum: `3.4169927217543985e-07 > 0`
- maximum: `0.15047341337280534`
- negative entries: `0`
- total negative mass: `0`
- L1 mass: `1.0`
- candidate SHA-256:
  `649481483AA0DD54081ACD9C3419B926EF94D0C3CC3637F2412D13F31F0D0C48`.

### Embedded full-space candidate

Constructed by support:

- closed entries = restricted candidate exactly
- transient entries = exact bitwise positive zero, `400/400`
- `math.fsum=1.0`
- minimum: `0`
- negative entries: `0`
- L1 mass: `1.0`
- p_full SHA-256:
  `5D7DA01D02C8EA711CD43AE5CD3FBF14107CE8394B97BE2E7AE1C904EDC658E0`.

### Full original-Q validation

Exactly one original full-Q `Q.T @ p_full` call was executed.

- residual infinity norm: `2.325020736918329e-16`
- residual L1 norm: `1.9932610131266322e-14`
- signed residual sum: `2.910108745234237e-17`
- normwise backward ratio: `7.197295889756597e-17`
- frozen stationarity bound: `6.197427304806514e-13`
- source identity discrepancy: `1.1719884465940349e-17`
- status: PASS.

### Comparison to run003 full-space candidate

- run003 transient signed mass: `-1.0085295212390263e-11`
- run003 transient L1 mass: `1.0090064860097144e-11`
- restricted-vs-run003 closed max abs difference: `1.5158707622475731e-12`
- closed L1 difference: `1.0085356535968933e-11`
- closed cosine similarity: `1.0`
- transient-leakage mass accounting discrepancy: `-1.9278790958386809e-16`.

The persisted run003 vector was not modified or renormalized.

## Scientific ledger

Accepted diagnostic consumption:

- Q12 loads: 1
- restricted dense GESVD: 1
- normalized stationary candidates: 1
- sign orientations: 1
- normalizations: 1
- full-Q `Q.T@p`: 1
- SCC/topology recomputation: 0
- HJB/policy/D2 calls: 0
- full-space 800x800 GESVD: 0
- alternate SVD/eigen/nullspace: 0
- retries: 0
- aggregate/K1A/C1/firm/outer: 0
- remaining provinces: 0
- turn 2: 0
- MATLAB/GE/Results: 0.

## Evidence

Evidence root:

`reports/ch5_mp4c_corrected_optionb_beijing_unique_closed_class_kfe_candidate_20260920_run001/`

Sealed manifest:

`278D5ECF2772FFD434130C8553EEDB2A99EE2B6E989D918D793DBCC0263CDDA0`

with 14 entries and 24,898 bytes. Independent readback PASS.

## Scientific decision boundary

This acceptance establishes **numerical support for the method candidate only**.

It does not adopt the method.

The current accepted KFE authority remains the prior full-state-space contract until the Owner explicitly decides whether to replace it with:

**unique-closed-class support KFE**
1. identify the unique closed communicating class from the already required exact-positive topology;
2. solve `Q_CC.T p_C = 0` on that class using one dense GESVD;
3. require restricted rank/nullity `|C|-1 / 1`;
4. orient and normalize once on C;
5. set transient mass exactly to zero by support construction;
6. validate the embedded candidate against the original full Q with one `Q.T@p_full`;
7. retain the existing stationarity, normalization, source-free, finite and nonnegativity gates.

No clipping, tolerance relaxation, row pinning, source RHS, iterative eigensolver or post-hoc repair is part of this candidate.

Because this is a substantive KFE numerical-method change, no successor Builder task is published until explicit Owner adoption or rejection.

Turn 2, K1B, K2, GE and Results remain closed. Results eligibility remains `FALSE`.
