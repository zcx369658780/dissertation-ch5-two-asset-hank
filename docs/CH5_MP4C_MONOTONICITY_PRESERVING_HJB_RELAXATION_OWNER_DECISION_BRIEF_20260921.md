# Chapter 5 monotonicity-preserving HJB relaxation — Owner decision brief

Date: 2026-09-21

Status:

`OWNER_DECISION_A_RECORDED__RELAXATION_LAW_ADOPTED`

This is a decision brief, not an adopted numerical law.

## Owner decision recorded — Decision A

Owner decision on 2026-09-21:

`OWNER_ADOPTED__MONOTONICITY_PRESERVING_HJB_RELAXATION__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK`

Owner wording:

`同意采用 monotonicity-preserving deterministic halving relaxation law。`

Formal authority:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_OWNER_ADOPTION_20260921.md`

This adoption authorizes the exact global deterministic halving invariant-domain law. It does not itself authorize fresh HJB or turn-2 execution.


## Why a decision is required

Accepted evidence now establishes:

1. the 黑龙江 checkpoint2->3 full implicit solve is numerically accurate;
2. that exact solve creates the first negative liquid marginal-value finite differences;
3. selector-level extrapolation is scientifically unsupported;
4. a global convex relaxation can preserve strict positive liquid slopes on the persisted trajectory while leaving the original HJB fixed points unchanged in exact arithmetic.

The current Owner convergence authority explicitly forbids damping/relaxation, so implementation requires a new Owner adoption.

## Proposed law

After one full implicit solve passes the existing `1e-12` backward-error gate:

1. test the full candidate `alpha=1`;
2. require all 760 raw b finite differences finite and strictly positive;
3. if the full candidate fails, test:
   `alpha=1/2,1/4,...,2^-52`;
4. each candidate is the global convex combination:
   `(1-alpha)V_old+alpha Vhat`;
5. accept the first represented candidate with all slopes `>0` and a state not bitwise identical to V_old;
6. if none passes, stop fail closed:
   `FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED`.

No derivative floor, clipping, projection, adaptive Delta, second solve or tolerance change is included.

## Decision A — adopt the proposed relaxation law

Decision text:

`OWNER_ADOPTED__MONOTONICITY_PRESERVING_HJB_RELAXATION__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK`

Meaning:

- the existing full implicit solve remains the only linear solve per HJB update;
- the represented nonlinear state may be globally relaxed only when needed to preserve strict positive raw liquid slopes;
- alpha search is exactly `1,1/2,...,2^-52`;
- the first passing candidate is accepted;
- no-pass or represented stagnation fails closed;
- existing B/D thresholds, cycle rules, update ceiling, D1/D2/D3, selector and terminal KFE laws remain unchanged.

A later bounded implementation/replay task would still be required before any fresh HJB continuation.

## Decision B — reject relaxation and preserve current full-update fail closed

Decision text:

`OWNER_DECISION__PRESERVE_FULL_IMPLICIT_NO_RELAXATION_LAW__F0063_REMAINS_NUMERICAL_FAIL_CLOSED`

Meaning:

- no damping/relaxation is introduced;
- 黑龙江 checkpoint3 remains the terminal first failure;
- further progress would require a different numerical redesign.

## Reviewer recommendation

Adopt Decision A.

Reason:

- the safeguard addresses the upstream numerical-domain failure rather than weakening selector science;
- it is global rather than cell-specific;
- it leaves legal full updates unchanged;
- it preserves the original fixed-point equations;
- it uses no derivative floor or local clipping;
- the persisted 2->3 case passes after a single halving with a comfortable positive minimum slope;
- it remains bounded and fail closed.

The recommendation is not itself Owner adoption.

## Important limitation

The design gate does not prove global convergence.

After adoption and implementation, a bounded replay/continuation task must still demonstrate that the relaxed trajectory can proceed under the existing Bellman/value convergence law without generating a new scientific failure.

Results eligibility remains `FALSE`.
