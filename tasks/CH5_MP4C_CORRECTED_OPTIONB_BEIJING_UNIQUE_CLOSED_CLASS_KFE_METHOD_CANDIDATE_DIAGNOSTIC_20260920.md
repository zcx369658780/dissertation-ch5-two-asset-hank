# Task — Beijing unique-closed-class KFE method-candidate diagnostic

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_20260920`

Status: `ACTIVE`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NONNEGATIVITY_FAILURE_ACCEPTANCE_20260920.md`
6. `docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_ACCEPTANCE_20260920.md`
7. run003 HJB/topology/SVD/stationary-mass evidence
8. accepted support-forensic evidence.

This task is a bounded numerical-method **diagnostic only**.

It does not adopt a new KFE method and does not reopen the multi-province run.

## Motivation fixed by accepted evidence

For the exact Beijing checkpoint-12 generator Q:

- corrected HJB is accepted;
- exact-positive topology has exactly one closed communicating class of 400 states and 400 transient states;
- full-space GESVD rank/nullity is 799/1;
- every full-space stationary-candidate floor breach occurs only on transient states;
- all 400 closed-class entries of the persisted full-space candidate are strictly positive;
- the current full-space KFE nevertheless remains FAIL under its frozen entrywise nonnegativity gate.

The purpose of this task is to test, not adopt, a support-aware KFE candidate implied by the unique closed-class structure.

## Exact input authority

Use only the accepted run003 Beijing checkpoint-12 objects.

Evidence root:

`reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_k1a_c1_one_turn_integration_20260920_run003/`

Require:

- run003 sealed manifest SHA-256:
  `18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B`
- Q12 artifact SHA-256:
  `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`
- topology closed-class count = 1
- closed members exactly F-order flat indices `200..399` and `600..799`
- closed size = 400
- transient size = 400
- full-space accepted rank/nullity evidence = `799/1`.

Also bind the accepted support-forensic manifest:

`E8E346EAFD41A41362B55D479CA1014A124C28724CB7625BABE262F01B691242`.

Do not modify any predecessor artifact.

## Candidate method under diagnostic

Let C be the persisted unique closed-class index set, in the exact order stored by the accepted topology receipt.

Construct only:

`Q_CC = Q[C,C]`.

Do not recompute topology or alter C.

The diagnostic candidate is:

1. verify Q_CC is finite and 400x400;
2. verify closed-class structural consistency directly from Q:
   - no positive outgoing rate from C to transient states;
   - Q_CC row sums satisfy the same arithmetic-conservation scale expected from the accepted Q;
3. set `A_C = Q_CC.T`;
4. execute exactly one full dense
   `scipy.linalg.svd(A_C, full_matrices=True, lapack_driver="gesvd", check_finite=True)`;
5. use only the smallest right-singular vector;
6. apply exactly one global sign orientation;
7. apply exactly one total-mass normalization on the 400 closed states;
8. construct an 800-state diagnostic candidate p_full by:
   - p_full[C] = normalized closed-class vector;
   - p_full[transient] = exact 0 by support construction;
9. execute exactly one full-space `Q.T @ p_full` stationarity check.

This is a newly constructed diagnostic candidate. Do not modify or project the persisted run003 p.

## Restricted singular-spectrum diagnostic

Persist all 400 singular values.

Report rank/nullity under both preregistered threshold views:

### Local-dimension threshold
Use the same gamma-based rank-threshold formula, with matrix dimension 400.

### Inherited full-space threshold
Also evaluate the same 400 singular values against the already frozen full-space-style threshold convention inherited from the 800-state KFE evidence.

The task must report both.

For method-candidate support, both threshold views must agree on:

`rank/nullity = 399/1`.

If they disagree, classify the candidate as unsupported and stop.

Do not tune either threshold after seeing the spectrum.

## Candidate acceptance diagnostics

For the 400-state normalized closed-class vector persist:

- all entries finite;
- signed `math.fsum=1` within arithmetic bound;
- minimum entry;
- negative-entry count;
- total negative mass;
- maximum entry;
- L1 mass;
- p SHA-256.

Because the accepted closed class is irreducible and the candidate is a stationary probability candidate, the strongest diagnostic target is:

- minimum entry strictly greater than 0.

No clipping, absolute-value repair, truncation or second normalization is allowed.

For embedded p_full persist:

- exactly 400 transient entries equal bitwise 0;
- exactly 400 closed entries equal the closed-class candidate;
- `math.fsum(p_full)=1` within arithmetic bound;
- minimum entry;
- negative-entry count;
- p_full SHA-256.

## Full-Q validation

Using the original accepted Q12, execute exactly one:

`Q.T @ p_full`.

Persist:

- residual infinity norm;
- residual L1 norm;
- signed residual sum;
- normwise backward ratio using the existing KFE scaling convention;
- source-free identity diagnostics;
- residual SHA-256.

Use the existing accepted stationarity arithmetic bound convention.

No second full-Q multiplication is allowed.

## Deterministic comparison to run003 full-space candidate

For comparison only, load the already persisted run003 p.

Without altering either vector, report:

- full-space candidate transient signed mass and L1 mass;
- closed-class candidate versus run003 p on C:
  - max absolute difference;
  - L1 difference;
  - cosine similarity or normalized dot product;
- mass difference explained by run003 transient leakage.

Do not renormalize the run003 vector for this comparison.

## Scientific budget

Maximum scientific calls for this task:

- Q12 artifact loads: 1
- topology/SCC recomputations: 0
- HJB/policy/D2 calls: 0
- restricted dense GESVD calls: 1
- normalized stationary candidates: 1
- full-space `Q.T@p` calls: 1
- full-space 800x800 GESVD calls: 0
- alternate SVD/eigen/nullspace solvers: 0
- retries: 0
- clipping/projection of run003 p: 0
- aggregates/K1A/C1/firm/outer calls: 0
- MATLAB/GE/annual/shock/IRF/welfare/Results: 0.

Engineering tests before the single scientific execution may be retried and must use synthetic matrices only.

## Terminal classifications

A successful diagnostic must use exactly one of:

### Supported
`PASS__UNIQUE_CLOSED_CLASS_RESTRICTED_KFE_CANDIDATE_DIAGNOSTIC__OWNER_METHOD_ADOPTION_DECISION_REQUIRED`

only if:

- Q_CC structural checks pass;
- both threshold views give rank/nullity 399/1;
- the closed-class normalized candidate is strictly positive entrywise;
- embedded transient mass is exactly zero;
- full original Q stationarity passes the frozen arithmetic bound;
- normalization/source-free checks pass;
- no retry or forbidden method is used.

### Unsupported
`FAIL__UNIQUE_CLOSED_CLASS_RESTRICTED_KFE_CANDIDATE_DIAGNOSTIC__METHOD_NOT_SUPPORTED`

on the first failed diagnostic gate.

Neither classification changes the accepted KFE method.

## Deliverables

Allowed implementation:

`validators/multi_province/beijing_unique_closed_class_kfe_candidate/run.py`

Allowed focused test:

`tests/test_mp4c_beijing_unique_closed_class_kfe_candidate.py`

Write:

`docs/CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_REPORT.md`

Create fresh evidence root:

`reports/ch5_mp4c_corrected_optionb_beijing_unique_closed_class_kfe_candidate_20260920_run001/`

Persist:

- authority binding
- closed/transient index receipt
- Q_CC structural receipt
- restricted GESVD rank/nullity receipt
- closed-class stationary candidate arrays and receipt
- embedded full-space candidate arrays and receipt
- one full-Q stationarity receipt
- comparison-to-run003 receipt
- exact scientific ledger
- terminal receipt
- sealed manifest and independent readback.

## Git workflow

- isolated task branch
- explicit staging only
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish a successor.

If the diagnostic is Supported, STOP for explicit Owner/Reviewer method-adoption decision. Do not rerun the 31-province model.
