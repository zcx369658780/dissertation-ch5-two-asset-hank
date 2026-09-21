# Chapter 5 monotonicity-preserving HJB relaxation scientific design gate — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__GENERIC_MONOTONICITY_PRESERVING_RELAXATION_PROPOSAL_COMPLETE__OWNER_ADOPTION_REQUIRED`

Accepted terminal:

`PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_DESIGN_GATE__GENERIC_LAW_PROPOSAL_COMPLETE__OWNER_ADOPTION_REQUIRED__NO_IMPLEMENTATION`

Accepted classification:

`ADOPTION_READY_GENERIC_RELAXATION_LAW__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK__OWNER_ADOPTION_REQUIRED`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `ac3a4e5e7f76d85f033511e1d0b093cc46b3a1fe`
- candidate: `9ad1c844b331ae4b131b57aeb70ade127b82000e`
- candidate tree: `659b8c707d6812dda4e91ece2f4e49aefbb04ac2`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- changed paths: 20
- production `src/ch5_two_asset_hank/**`: 0 changes
- CURRENT: 0 changes
- remote candidate branch SHA/tree: exact.

All changed paths are confined to the design report, fresh evidence, focused tests and design validator.

Focused tests: 5/5 PASS.

## Accepted scientific design result

The design gate supports a prospective **global convex invariant-domain relaxation** of the accepted full implicit HJB candidate:

`V_new(alpha)=(1-alpha)V_old+alpha*Vhat`

with `0<alpha<=1`, where `Vhat` is still obtained from exactly one accepted full implicit direct solve under the existing fixed-`Delta=1000` linearized equation.

The proposed safeguard is global across the entire value array. It does not clip individual values, derivatives, controls or drifts.

Its sole new role is to reject a represented next iterate whose raw liquid finite differences leave the strictly positive marginal-value domain required by the corrected household problem.

## Exact alpha-feasibility evidence

Every liquid b-edge slope is affine in alpha:

`s_e(alpha)=s_e(V_old)+alpha[s_e(Vhat)-s_e(V_old)]`.

There are exactly 760 distinct b edges per update.

Persisted 黑龙江 replay gives:

| Update | full positive edges | critical alpha | admissible alpha |
| --- | ---: | ---: | --- |
| 0->1 | 760/760 | 2.4931512205949184 | (0,1] |
| 1->2 | 760/760 | 3.6193576019021174 | (0,1] |
| 2->3 | 758/760 | 0.9869478908098366 | (0,0.9869478908098366) |

The binding 2->3 edge is F0062->F0063:

- old slope: `0.018363586699392222`
- full slope: `-0.0002428532863339202`
- slope change: `-0.018606439985726142`
- critical alpha: `0.9869478908098366`.

The second constrained edge is F0082->F0083 with critical alpha:

`0.9889708566271117`.

## Deterministic halving replay

The proposed Design 1 tests:

`alpha = 1, 1/2, 1/4, ...`

and accepts the first represented candidate with:

- all 760 raw b slopes finite;
- all 760 raw b slopes strictly greater than zero;
- represented candidate not bitwise identical to V_old.

Persisted replay:

- update 0->1: alpha=1
- update 1->2: alpha=1
- update 2->3: alpha=0.5 after one halving.

At alpha=0.5 for 2->3:

- all 760 raw b slopes are strictly positive;
- minimum raw b slope:
  `0.005032838660371801`
- value-change infinity norm:
  `0.017682618173863407`.

Therefore the rule is inactive on already legal full updates and activates only when the full candidate exits the accepted liquid marginal-value domain.

## Maximal-alpha comparator

The exact real-arithmetic critical alpha is not itself legal because it produces a zero slope.

The first binary64 predecessor also fails after the prescribed represented convex combination.

For this replay, four predecessor steps are required before all represented slopes become strictly positive:

- alpha:
  `0.9869478908098361`
- minimum represented slope:
  `1.2053849981644563e-15`.

Reviewer accepts the Builder's judgment that this maximal-step construction is a less robust default design: it requires representation-sensitive endpoint machinery and leaves a nearly zero liquid marginal value.

It remains a comparator, not the proposed law.

## Fixed-point argument

Let the original nonlinear map be:

`T(V)=Vhat`.

Let the relaxed map be:

`F(V)=V+alpha(V,T(V))[T(V)-V]`.

In exact arithmetic:

- if `T(V)=V`, then `F(V)=V`;
- if `F(V)=V` and `alpha>0`, then `T(V)=V`.

Thus positive-alpha relaxation preserves the original fixed-point set.

This does **not** prove global convergence, contractivity, or improved convergence speed.

The actual trajectory and rate change, and the safeguard may itself fail closed if no represented legal candidate is found.

## Scientific basis for the invariant domain

The corrected household consumption FOC requires:

`q_b=c^{-gamma}>0`.

Under the model budget/utility structure, extra liquid wealth cannot reduce attainable value, so strictly positive liquid marginal value is a scientifically meaningful domain property of the target value function.

The previous accepted forensic proved that the full implicit update can leave that domain even when the linear solve is numerically exact.

A global convex relaxation that keeps the next iterate inside the domain while preserving the fixed point is therefore scientifically distinguishable from:

- derivative flooring;
- clipping;
- local projection;
- one-sided co-state extrapolation;
- selector rescue.

It is best interpreted as an invariant-domain line search on the nonlinear iteration.

## Interaction with the adopted convergence law

If later adopted, the proposal preserves:

- Bellman threshold `B<=1e-8`;
- value-change threshold `D<=1e-7`;
- exact and approximate cycle rules;
- 100-update ceiling;
- fixed full-solve `Delta=1000`;
- direct-solve backward-error threshold `<=1e-12`;
- terminal KFE authority.

The accepted relaxed state becomes the next nonlinear state.

Therefore:

- `D_n` uses the relaxed accepted state;
- `B_n` is computed only after a fresh complete policy/Q map at that state;
- cycle identities use accepted relaxed checkpoints and their fresh policy/Q identities;
- one full direct solve plus the deterministic arithmetic relaxation search counts as one HJB update, not a scientific retry.

No convergence threshold is changed.

## Exact proposal-only rule

The accepted proposal for Owner consideration is:

1. perform the existing full implicit solve exactly once;
2. require the existing solve backward-error gate to pass;
3. reconstruct all 760 raw b slopes of the represented full candidate;
4. if every slope is finite and strictly positive, accept alpha=1 unchanged;
5. otherwise test, in order:
   `alpha=2^-k`, `k=1,...,52`;
6. construct each candidate exactly as:
   `(1-alpha)V_old+alpha Vhat`;
7. accept the first represented candidate whose 760 raw b slopes are finite and strictly positive and whose represented state differs bitwise from V_old;
8. if the finite search finds no such state, fail closed with:
   `FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED`;
9. persist the full-candidate identity, every attempted alpha, slope census, accepted state identity and value-change norm.

No positive slope magnitude floor is introduced. The condition is strict `>0`.

### Reviewer clarification on the 52-halving ceiling

The number 52 is accepted here as a **prospective finite numerical-operation bound**, not as a uniquely implied mathematical constant.

Its use is motivated by binary64 significand-scale resolution, but the scientific content of the law is the deterministic finite halving search plus strict positivity and bitwise no-stagnation checks.

Owner adoption, if granted, should be understood as explicitly adopting this numerical ceiling as part of the bounded algorithm.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_scientific_design_gate_20260921_run001/`

- manifest SHA-256:
  `F54EDEAA8FC351981CD2CBD44F17FA58950155F12953B7983E174D5EAC0D2803`
- entries: 15
- bytes: 25,760
- independent readback: PASS
- bad paths: none.

Zero-science ledger confirms:

- production selector/root/derivative helper: 0
- HJB/direct update execution: 0
- new linear solve: 0
- D2/Q rebuild: 0
- KFE/SVD: 0
- integration/turn2/turn3/MATLAB: 0
- scientific model calls: 0.

## Reviewer decision

The proposal is accepted as **adoption-ready**, not adopted.

The current Owner-adopted no-relaxation convergence law remains authoritative until Owner makes a new explicit scientific decision.

No implementation or HJB rerun is authorized by this acceptance.
