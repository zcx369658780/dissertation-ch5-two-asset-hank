# Chapter 5 corrected Option-B run003 stationary-mass support forensic acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_PASS__RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_A__TRANSIENT_ONLY_BREACHES__CLOSED_CLASS_ENTRYWISE_POSITIVE__KFE_METHOD_DECISION_SUPPORT_AUTHORIZED`

## Accepted candidate

- live-main baseline: `03a6c3d17b9741cf60fb0d3f4bd2b981ac5e2fef`
- Builder candidate: `633e93d3ab114df95ac5d127170ced7da67a2cb1`
- candidate tree reported/read back by Builder: `9565296b9229fda4a000f432a280a92abc4cb9b9`
- ancestry independently verified: `1 ahead / 0 behind`, merge-base exactly the baseline
- independently verified changed paths: 14
  - validator: 1
  - focused test: 1
  - report: 1
  - forensic evidence: 11
  - CURRENT files: 0
- Builder did not merge main and did not publish a successor.

The candidate has been fast-forwarded into live `main`.

## Forensic terminal

`PASS__RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_COMPLETE__NO_KFE_METHOD_CHANGE`

Classification A:

`RUN003_NEGATIVITY_BREACHES_TRANSIENT_ONLY__CLOSED_CLASS_MASS_PASSES_ENTRYWISE_FLOOR__KFE_METHOD_DECISION_REQUIRED`

The existing run003 KFE remains FAIL. No KFE method, tolerance, vector, topology, or stationary-mass acceptance rule was changed.

## Exact accepted support decomposition

Accepted run003 topology remains:

- one unique closed communicating class;
- closed states: exactly 400;
- transient states: exactly 400;
- closed members: F-order flat indices `200..399` and `600..799`.

For the persisted normalized full-space SVD candidate p:

### Closed class

- state count: 400
- positive entries: 400
- negative entries: 0
- entrywise floor breaches: 0
- minimum p: `3.416992721942287e-07`
- signed mass: `1.0000000000100855`
- total negative mass: `0`.

### Transient states

- state count: 400
- positive entries: 122
- negative entries: 278
- entrywise floor breaches: 14
- minimum p: `-2.217909641958515e-12`
- signed mass: `-1.0085295212390263e-11`
- L1 mass: `1.0090064860097144e-11`
- total negative mass: `1.0087680036243705e-11`.

Every one of the 14 entries with `p < -tau_nonnegative` is transient. No closed-class entry violates the frozen entrywise floor.

The global minimum occurs at flat index `419`, F-order `(b,a,z)=(19,0,1)`, physical state `(5,0,1.3)`, and is transient.

## Persisted residual decomposition

No new `Q.T@p` was executed.

Using only the persisted run003 residual:

- closed residual infinity norm: `1.3682631416767066e-16`
- transient residual infinity norm: `1.208264235905564e-16`
- closed residual L1 norm: `1.4464432662687418e-14`
- transient residual L1 norm: `1.1548046149573596e-14`.

## Scientific interpretation boundary

The forensic establishes an important structural diagnosis:

- the accepted exact-positive topology has a unique closed communicating class;
- all frozen entrywise nonnegativity breaches of the full-space SVD vector occur only on transient states;
- the closed-class portion is strictly positive entrywise and carries mass `1 + O(1e-11)`.

This supports testing a closed-class-support stationary-mass construction as a candidate KFE numerical method.

However, the present forensic does **not** adopt that method and does **not** accept the current KFE.

A method change from full-space 800-state SVD to a support-aware construction is substantive scientific/numerical-method authority. It requires a separately bounded diagnostic and then an explicit Owner/Reviewer method decision.

No clipping, projection of the run003 vector, tolerance relaxation, or post-hoc renormalization is accepted.

## Evidence

Forensic evidence root:

`reports/ch5_mp4c_corrected_optionb_run003_stationary_mass_negativity_support_forensic_20260920_run001/`

Sealed manifest:

`E8E346EAFD41A41362B55D479CA1014A124C28724CB7625BABE262F01B691242`

with 9 entries and 17,215 bytes. Independent readback PASS. All prohibited scientific calls are zero.

## Route consequence

The next bounded task is a method-candidate diagnostic only.

It may construct a fresh stationary candidate from the already accepted unique closed communicating class by solving only the closed-class generator block, embed zero mass on transient states by support construction, and test that candidate against the full accepted Q.

That diagnostic does not itself change the accepted KFE method. A later explicit method-decision step is required before any multi-province rerun.

Turn 2, K1B, K2, GE and Results remain closed. Results eligibility remains `FALSE`.
