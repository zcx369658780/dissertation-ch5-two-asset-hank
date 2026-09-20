# Chapter 5 unique-closed-class support KFE Owner adoption

Date: 2026-09-20

Owner decision:

`OWNER_ADOPTED__UNIQUE_CLOSED_CLASS_SUPPORT_KFE_AS_TERMINAL_KFE_AUTHORITY`

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Results eligibility remains `FALSE`.

## Decision

The Owner explicitly adopts the unique-closed-class support KFE method as the new terminal KFE authority for the corrected two-asset household route.

This replaces the prior full-state-space stationary-mass construction as the accepted terminal KFE method.

The prior full-space 800-state SVD evidence remains historically valid diagnostic evidence, but it is no longer the terminal stationary-mass construction authority for successor corrected-household executions.

## Evidence basis

This adoption is supported by accepted Beijing checkpoint-12 evidence:

- corrected HJB convergence PASS;
- exact-positive topology with exactly one closed communicating class;
- closed-class size `400`, transient size `400`;
- full-space rank/nullity `799/1`;
- all 14 frozen entrywise negativity breaches of the full-space SVD candidate occur only on transient states;
- all 400 closed-class entries of that candidate are strictly positive;
- a bounded candidate diagnostic on `Q_CC` passes:
  - structural closure/conservation;
  - one restricted dense GESVD;
  - rank/nullity `399/1` under both preregistered threshold views;
  - strictly positive normalized closed-class stationary vector;
  - exact-zero transient support embedding;
  - one full original-Q `Q.T@p_full` stationarity validation.

Accepted supporting documents:

- `docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_ACCEPTANCE_20260920.md`
- `docs/CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_ACCEPTANCE_20260920.md`.

## New terminal KFE authority

For every converged corrected-household generator Q:

### 1. Exact-positive topology

Use the already accepted exact-positive directed-graph construction.

Execute exactly one SCC decomposition.

Require exactly one closed communicating class.

Let its persisted state-index set be `C`.

If closed-class count is not exactly one, terminal KFE FAILS immediately.

Do not use a fallback full-state-space stationary solve.

### 2. Closed-class structural block

Construct:

`Q_CC = Q[C,C]`.

Require:

- square finite matrix of dimension `m=|C|`;
- no positive outgoing Q rate from C to transient states;
- offdiagonals nonnegative;
- Q_CC row-conservation error within the accepted Q/D2 arithmetic-conservation bound.

No graph recomputation is required or allowed for this step.

### 3. Restricted source-free solve

Set:

`A_C = Q_CC.T`.

Execute exactly one full dense:

`scipy.linalg.svd(A_C, full_matrices=True, lapack_driver="gesvd", check_finite=True)`.

No alternate SVD driver, eigensolver, sparse nullspace solver, row replacement, pin equation, source RHS or balancing source is allowed.

Use only the smallest right-singular vector.

### 4. Rank/nullity gate

Persist the complete restricted singular spectrum.

Evaluate the spectrum under both preregistered threshold views:

**Local-dimension view**

`tau_rank_local = gamma(m + 64) * max(1, sigma_max)`.

**Inherited full-state compatibility view**

`tau_rank_800 = gamma(800 + 64) * max(1, sigma_max)`.

Require both views to agree on:

- numerical rank `m-1`;
- numerical nullity `1`;
- second-smallest singular value strictly above both thresholds.

Any disagreement or nullity other than one is a terminal KFE FAIL.

### 5. Orientation and normalization on C

For the smallest restricted right-singular vector `v_C`:

- compute its signed and absolute sums;
- require signed sum to be separated from zero using the local-dimension arithmetic scale
  `gamma(m) * max(1, sum(abs(v_C)))`;
- apply at most one global sign reversal;
- apply exactly one total-mass normalization on C.

No clipping, absolute-value transformation, truncation or second normalization is allowed.

The normalized `p_C` must be finite and **strictly positive entrywise**.

Strictly positive closed-class mass is the adopted irreducible-class gate; arithmetic-negative allowance is not used to excuse a negative restricted-support entry.

### 6. Structural embedding

Construct the full-state mass vector from support:

- `p_full[C] = p_C`;
- every transient entry is exact positive zero by construction.

This is not projection or repair of a previously computed full-space vector. It is the definition of the stationary-support embedding under the unique closed-class authority.

Require:

- all transient entries exactly zero;
- full vector finite;
- no negative entry;
- total probability mass normalized under the existing full-state arithmetic normalization bound.

Define density with the accepted state-cell volume exactly as before:

`g_full = p_full / OMEGA`.

Require the existing density-volume normalization gate.

### 7. Full original-Q source-free validation

Using the original full Q, execute exactly one:

`Q.T @ p_full`.

Retain the existing full-state stationarity/source-free arithmetic gates, including:

- residual infinity norm;
- normwise backward ratio;
- residual signed sum;
- `dot(Q@1,p_full)`;
- source-identity discrepancy;
- accepted full-state gamma-based bounds.

No second full-Q stationarity multiplication is allowed.

### 8. Accepted stationary mass

Only if every gate above passes is `p_full/g_full` the accepted terminal stationary mass for household aggregation.

All existing corrected aggregate semantics remain unchanged.

## Removed authority

The prior terminal method:

- one full 800x800 dense SVD of `Q.T`;
- direct normalization of its full-space smallest right-singular vector;
- arithmetic allowance for transient numerical leakage

is no longer the accepted stationary-mass construction route for future corrected-household executions.

It remains historical evidence only.

## Prohibitions unchanged

The new authority does not permit:

- clipping;
- absolute-value repair;
- tolerance relaxation;
- post-hoc support projection of an already-computed full-space vector;
- second normalization;
- row pinning/replacement;
- source RHS or balancing source;
- iterative eigensolver;
- alternate SVD driver;
- scientific retry;
- solver substitution.

## Scope

This adoption changes terminal KFE numerical-method authority only.

It does not change:

- HJB equations;
- D1/D2/D3;
- KKT/boundary/upwind/switching laws;
- grid;
- Delta;
- HJB convergence thresholds;
- corrected aggregate definitions;
- K1A;
- C1;
- raw-ra0 payoff law;
- turn timing.

The next bounded Builder task may implement this authority and rerun the corrected initial-turn route from the accepted turn-1 initialization states.

Turn 2, K1B, K2, GE and Results remain closed.
