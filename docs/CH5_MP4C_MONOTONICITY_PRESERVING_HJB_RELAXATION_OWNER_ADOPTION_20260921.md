# Chapter 5 monotonicity-preserving HJB relaxation — Owner adoption

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Owner decision:

`OWNER_ADOPTED__MONOTONICITY_PRESERVING_HJB_RELAXATION__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK`

Owner wording:

`同意采用 monotonicity-preserving deterministic halving relaxation law。`

Results eligibility remains `FALSE`.

## Adopted authority

This adoption prospectively extends the corrected-target nonlinear HJB iteration law.

It supersedes only the prior prohibition on **global value-iterate relaxation/damping** to the exact extent defined below.

All other previously adopted convergence, solver, selector, D1/D2/D3 and terminal-KFE laws remain unchanged.

## Exact adopted update law

At each nonconverged corrected HJB checkpoint:

1. construct the fresh same-value policy/operator under the existing authority;
2. form the existing full implicit direct-solve problem with fixed `Delta=1000`;
3. execute exactly one direct linear solve;
4. require the existing solve acceptance gate:
   `normwise_backward_error <= 1e-12`,
   with the existing warning/finite/shape fail-closed rules;
5. denote the represented full solution by `Vhat`;
6. reconstruct all 760 raw liquid b-edge finite differences of `Vhat`;
7. if every edge is finite and strictly positive, accept `alpha=1` and set:
   `V_next=Vhat`;
8. otherwise test, in order:
   `alpha=2^-k`, for `k=1,...,52`;
9. for each alpha construct exactly:
   `V_candidate=(1-alpha)*V_old+alpha*Vhat`;
10. accept the first represented candidate for which:
    - all 760 raw liquid b-edge slopes are finite;
    - every raw liquid b-edge slope is strictly `>0`;
    - `V_candidate` is not bitwise identical to `V_old`;
11. if no candidate passes through `k=52`, stop fail closed:
    `FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED`.

No positive derivative magnitude floor is introduced.

The positivity condition is the exact represented comparison `>0`.

The finite ceiling `52` is explicitly adopted as a prospective bounded numerical-operation parameter. It is not an economic parameter or a uniquely implied mathematical constant.

## Scientific interpretation

The relaxation is a **global invariant-domain line search on the nonlinear value iteration**.

It is not:

- derivative flooring;
- cellwise clipping;
- local value projection;
- control/drift clipping;
- one-sided co-state extrapolation;
- adaptive Delta;
- a second linear solve;
- scientific retry.

The full direct solve remains the unique linear solve for one HJB update.

One full solve plus any arithmetic alpha checks consumes exactly one HJB update.

## Fixed-point target

Let `T(V)=Vhat` be the pre-existing full-update nonlinear map and

`F(V)=V+alpha(V,T(V))*(T(V)-V)`.

For every accepted nonfixed update, alpha is represented positive and the candidate differs from V.

Under that rule:

- `T(V)=V` implies `F(V)=V`;
- `F(V)=V` with alpha>0 implies `T(V)=V`.

Thus the adopted relaxation preserves the original fixed-point set.

This adoption does not assert global convergence or improved convergence rate.

## Preserved nonlinear convergence authority

The following remain unchanged:

- same-value Bellman metric:
  `B_n=||rho V_n-u_n-Q_n V_n||_inf`;
- convergence threshold:
  `B_n<=1e-8`;
- value-change metric computed from the **accepted nonlinear states**:
  `D_n=||V_n-V_(n-1)||_inf`;
- convergence threshold:
  `D_n<=1e-7`;
- primary convergence requires both thresholds at the same checkpoint;
- exact-cycle rule;
- approximate period-2 / period-3 cycle rule;
- total HJB update ceiling of 100;
- terminal-only KFE timing.

After a relaxed state is accepted, any next `B_n` is computed only after a fresh complete policy/Q map at that accepted state.

Cycle identities are formed from accepted relaxed checkpoints and their fresh policy/Q identities.

## Preserved scientific law

Unchanged:

- q_b consumption-shadow domain;
- ordinary upwinding;
- interior-liquid Z authority;
- lower-a zero-kink law;
- interior-a switching;
- joint switching;
- D1 boundary law;
- D2 consumed-drift generator law;
- D3 adjustment technology/KKT;
- grid/calibration;
- direct solver family;
- direct-solve tolerance;
- terminal unique-closed-class KFE authority.

No derivative floor, clipping, artificial diffusion, adaptive Delta, parameter continuation, solver substitution or tolerance tuning is authorized.

## Required audit receipt

Each future update that reaches the relaxation stage must persist:

- V_old identity;
- full direct candidate Vhat identity;
- direct-solve receipt;
- full-candidate raw b-edge sign/minimum census;
- every attempted alpha in order;
- for each attempted alpha:
  - represented candidate identity;
  - finite/positive edge counts;
  - minimum raw b slope;
  - bitwise-stagnation result;
- accepted alpha and halving count;
- accepted V_next identity;
- accepted value-change norm;
- terminal if exhausted.

## Immediate implementation authority

Reviewer may publish one bounded implementation-and-persisted-replay task.

That task may implement only this adopted relaxation law and validate it against already persisted accepted updates.

It must not execute a fresh HJB direct solve, fresh selector map, D2/Q, KFE, integration or turn2 continuation.

Any fresh scientific runtime remains a separate later task after implementation acceptance.
