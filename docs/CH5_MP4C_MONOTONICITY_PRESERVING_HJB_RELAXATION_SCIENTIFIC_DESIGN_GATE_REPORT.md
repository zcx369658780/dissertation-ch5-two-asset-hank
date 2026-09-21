# Chapter 5 MP4C monotonicity-preserving HJB relaxation scientific design gate

Date: 2026-09-21

Terminal:

`PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_DESIGN_GATE__GENERIC_LAW_PROPOSAL_COMPLETE__OWNER_ADOPTION_REQUIRED__NO_IMPLEMENTATION`

Classification:

`ADOPTION_READY_GENERIC_RELAXATION_LAW__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK__OWNER_ADOPTION_REQUIRED`

Results eligibility remains `FALSE`.

## Conclusion

A prospective global convex-relaxation safeguard is scientifically and numerically coherent as an invariant-domain line search. The proposed law uses deterministic halving, leaves already legal full updates unchanged, changes no cell or derivative independently, preserves the original HJB fixed points under a positive-alpha/no-represented-stagnation rule, and stops fail closed if a finite search cannot produce a represented state with all raw liquid slopes strictly positive.

This report proposes the law only. The current Owner-adopted full-update rule still forbids relaxation, so Owner adoption and a later implementation/reexecution task are required.

## Authority and inputs

The gate ran from live-main baseline `ac3a4e5e7f76d85f033511e1d0b093cc46b3a1fe`.

The accepted run004 manifest was rebound exactly at:

`1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80`.

Only persisted 黑龙江 checkpoint0/1/2 values and their saved direct-update candidates were loaded. All three direct-update candidates exactly match their persisted successor state identities. Production derivative, selector and root helpers were not imported or called.

## Full-edge alpha feasibility

For every raw b-grid edge, independent arithmetic gives

`s_e(alpha)=s_e(V_n)+alpha*(s_e(Vhat)-s_e(V_n))`.

There are `19*20*2=760` distinct b edges per update and 2,280 inequalities across the three updates.

| Update | Full candidate positive edges | Minimum full slope | Unrestricted critical alpha | Admissible interval in `0<alpha<=1` |
| --- | ---: | ---: | ---: | --- |
| 0→1 | 760/760 | `0.0042677403061128745` | `2.4931512205949184` | `(0,1]` |
| 1→2 | 760/760 | `0.004513872937454847` | `3.6193576019021174` | `(0,1]` |
| 2→3 | 758/760 | `-0.0002428532863339202` | `0.9869478908098366` | `(0,0.9869478908098366)` |

The safeguard is therefore inactive for 0→1 and 1→2. At 2→3, equality at the critical alpha is excluded because it gives a zero slope.

### Binding edges at 2→3

The binding edge is F0062→F0063, indices `(2,3,0)`→`(3,3,0)`:

- old slope: `0.018363586699392222`;
- full candidate slope: `-0.0002428532863339202`;
- slope change: `-0.018606439985726142`;
- critical alpha: `0.9869478908098366`.

One other edge constrains alpha below one, F0082→F0083, indices `(2,4,0)`→`(3,4,0)`:

- old slope: `0.018007130756515985`;
- full candidate slope: `-0.00020081807822456922`;
- critical alpha: `0.9889708566271117`.

The F0062→F0063 edge is strictly tighter.

## Persisted arithmetic replay

Design 0 accepts alpha `1` for every update. It passes the first two updates and produces two negative edges at 2→3.

Design 1 tests `1, 1/2, 1/4, ...` and accepts the first represented candidate with 760 finite slopes strictly greater than zero and a represented state different from the old state:

| Update | Accepted alpha | Halvings | Minimum represented slope | Value-change infinity norm |
| --- | ---: | ---: | ---: | ---: |
| 0→1 | `1` | 0 | `0.0042677403061128745` | `0.6230457816987043` |
| 1→2 | `1` | 0 | `0.004513872937454847` | `0.27122303476390464` |
| 2→3 | `0.5` | 1 | `0.005032838660371801` | `0.017682618173863407` |

The 2→3 relaxed-state SHA-256 is:

`987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF`.

The frozen checkpoint2 linear-system residual is `0.013624345900843285` for the half step. This is diagnostic only: the relaxed state is a convex combination after the accepted solve and is not expected to solve the frozen linear system. No second solve was performed.

## Design comparison

### Design 0 — alpha=1

This is the current authority. It preserves the direct-solve candidate exactly but exits the positive liquid-slope domain at 2→3.

### Design 1 — deterministic halving

This is the proposed generic law. Halving is a conventional deterministic contraction factor, not a uniquely implied economic constant. Its scientific role is limited to a finite invariant-domain line search. It is prospective, global across the value array, does not clip derivatives, and has simple fail-closed accounting.

The proposed ceiling is 52 halvings, tied to binary64 significand resolution as a finite representation/operation bound. It is not a positive derivative floor. A candidate must also differ bitwise from the old state. Exhaustion or represented stagnation stops with:

`FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED`.

### Design 2 — maximal admissible alpha

The real-arithmetic supremum at 2→3 is `0.9869478908098366`, and the endpoint is illegal. A single binary64 predecessor, `0.9869478908098365`, still produces one exactly zero represented slope after the prescribed convex combination. Four predecessor steps are needed in this particular replay; the first passing alpha is `0.9869478908098361`, with minimum slope `1.2053849981644563e-15`.

Thus a simple “one predecessor” rule is not representation safe. A more elaborate certified rounding rule could be designed, but it would accept a nearly zero liquid shadow and add machinery without evidence of better nonlinear convergence. Design 2 remains a diagnostic comparator rather than the proposed law.

### Design 3 — projection or clipping

Projection changes selected values or derivatives locally and therefore changes the iterate beyond a global convex combination. It is not proposed.

### Design 4 — adaptive Delta or a new solve

This changes the numerical map and consumes another linear solve. It was not executed and is not proposed.

## Fixed points and convergence

Let the original update be `T(V)=Vhat` and the relaxed update be

`F(V)=V+alpha(V,T(V))*(T(V)-V)`.

If `T(V)=V`, then `F(V)=V`. Conversely, for every accepted update with `alpha>0`, `F(V)=V` implies `T(V)-V=0`. The represented rule additionally rejects a bitwise unchanged nonfixed candidate. The accepted relaxed map therefore retains the original fixed points under these conditions.

This equivalence does not prove convergence. State-dependent relaxation changes the trajectory and can slow convergence or fail to find a legal step. The proposed law makes no global convergence claim and stops fail closed when its finite search is exhausted.

Strict positivity is a legitimate domain invariant because the consumption FOC requires `q_b=c^(-gamma)>0`, and more liquid wealth cannot reduce attainable value under the repository budget and utility structure. Intermediate implicit iterates do not automatically inherit that property. Applying the safeguard only when the full candidate leaves the domain is therefore an invariant-domain line search, while the unchanged fixed-point equations remain the scientific target.

## Interaction with the adopted convergence law

- `D_n` uses the accepted relaxed `V_n`.
- A future `B_n` is valid only after a fresh complete policy/Q map at that relaxed value.
- Exact and approximate cycle identities use accepted relaxed checkpoints and their fresh policy/Q identities.
- One full solve plus arithmetic relaxation is one HJB update, not a retry.
- Every accepted relaxed update consumes one of the existing 100-update ceiling.
- The inclusive thresholds `B_n<=1e-8` and `D_n<=1e-7` remain unchanged.
- Failure to find a legal represented state within 52 halvings stops fail closed.

## Proposal-only law

After the single full implicit solve passes the existing backward-error gate:

1. reconstruct all 760 raw b slopes from the represented full candidate;
2. accept alpha `1` if all are finite and strictly positive;
3. otherwise test alpha `2^-k`, in order for `k=1,...,52`, using exactly `(1-alpha)*V_old+alpha*Vhat`;
4. accept the first candidate with 760 finite slopes `>0` whose represented state differs from `V_old`;
5. persist the full-candidate hash, every attempted alpha and slope census, the accepted-state hash and value-change norm;
6. if none passes, emit the fail-closed terminal above.

This proposal does not alter D1/D2/D3 economics, the selector, roots, Q assembly, convergence thresholds or the direct-solve accuracy gate.

## Verification and zero-science ledger

Focused tests: `5 passed`.

- persisted NPZ loads: 6;
- persisted JSON loads: 1;
- independent raw b-edge reconstructions: 20;
- edge inequalities evaluated: 2,280;
- convex-relaxation candidates evaluated: 17;
- independent persisted CSR matvecs: 3;
- production derivative/selector/root helper calls: 0/0/0;
- HJB/direct-update executions: 0;
- new linear solves: 0;
- D2/Q rebuilds: 0;
- KFE/SVD: 0;
- aggregate/integration: 0;
- turn2 replay/rerun: 0;
- turn3: 0;
- MATLAB: 0;
- retry/tuning: 0;
- scientific model calls: 0.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_scientific_design_gate_20260921_run001/`

- manifest SHA-256: `F54EDEAA8FC351981CD2CBD44F17FA58950155F12953B7983E174D5EAC0D2803`;
- entries: 15;
- bytes: 25,760;
- independent readback: `PASS`;
- bad paths: none.

No production source or CURRENT file was modified, and no successor was published.
