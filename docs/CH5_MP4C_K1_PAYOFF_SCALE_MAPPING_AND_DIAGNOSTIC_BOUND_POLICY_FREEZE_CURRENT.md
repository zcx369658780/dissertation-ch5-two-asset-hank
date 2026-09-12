# Chapter 5 MP4C K1 payoff-scale mapping and diagnostic-bound policy freeze

Date: 2026-09-12.
Status: `OWNER_APPROVED_RAW_RA0_ECONOMIC_SOURCE_RETAINED__HJB_SCALE_MAPPING_AUDIT_REQUIRED__TEMPORARY_DIAGNOSTIC_BOUNDS_ALLOWED_ONLY_BY_EXACT_TASK`.

## 1. Owner scientific decision

The Owner retains raw firm `ra0` as the economically relevant source object for the K1 household illiquid payoff channel, but withdraws the earlier working assumption that the raw numerical level may automatically be passed one-for-one into the household HJB as `r_a`.

The next scientific question is therefore not whether to restore the historical `[.02,.09]` clip as a structural law. It is whether the firm-side raw return object and the continuous-time household HJB use the same model-time scale, period convention and numeraire. A source-backed payoff-scale mapping must be audited and frozen before additional long-horizon Raw runtime or K1B.

This decision is motivated by accepted evidence: raw payoff is source-consistent and preserves cross-province information, but direct level transmission materially worsened HJB convergence and amplified the accepted value-derivative -> transfer FOC -> quadratic adjustment-cost chain.

## 2. Legacy versus rebuilt numerical system

The old multi-province MATLAB/source-faithful numerical system remains historical provenance and parity evidence, not final scientific authority. Accepted Chapter-5 work has already identified structural defects in the old private-capital allocation and household-return aggregation, as well as severe clipping information loss and unresolved empirical KFE finite-box/pinning behavior.

The replacement system is being rebuilt gate by gate. The bilateral capital-network accounting and bounded dynamic transmission are accepted, but the final household payoff scaling, full numerical stability, empirical KFE closure, K1B/K2 and steady-state/Results gates are not yet accepted.

Accordingly, the project must not describe the old system as globally invalid in every component, nor the new system as already complete. The correct status is: substantial old multi-province numerical contracts have been superseded or demoted to reference status, while the replacement numerical system is still under scientific construction and validation.

## 3. Final-versus-debugging distinction

The Owner explicitly authorizes temporary hard upper/lower bounds on return-like and wage-like objects (including `ra`/`rah` and `wjt`/wage where the active route actually uses those objects) as **diagnostic numerical scaffolding** in future exact runtime tasks when needed to establish a feasible steady-state route.

This authorization does not create any bound values by itself and does not authorize a runtime change in the current zero-science audit.

Any future diagnostic-bound task must:

1. state the exact bounded object and exact lower/upper values before scientific execution;
2. distinguish diagnostic continuation guards from structural economic restrictions;
3. record hit/saturation counts by province/turn and, where available, grid cell;
4. preserve an unbounded/raw receipt for comparison whenever the task design permits it;
5. never tune bounds after seeing the same run merely to obtain PASS;
6. use a preregistered relaxation ladder if progressive relaxation is tested;
7. treat a bound-dependent steady state as provisional rather than final;
8. progressively widen and, where scientifically feasible, remove diagnostic bounds before final economic/Results acceptance.

The historical `[.02,.09]` `ra` clip therefore remains `EMPIRICAL_NUMERICAL_SAFEGUARD`, not a final structural payoff law. Likewise, any future wage/`wjt` guard remains diagnostic unless separately justified by economic/source authority.

## 4. Immediate next gate

The immediate next gate is zero-science only: audit the period/time-unit/numeraire authority linking firm `ra0`, depreciation, discounting, productivity-state transition rates, liquid return, wages and the household HJB.

The audit must determine whether a source-backed identity mapping, calendar/model-time rescaling, or another explicitly documented mapping exists. It must not choose an arbitrary shrinkage coefficient, cap, normalization or smoothing rule.

## 5. Runtime boundary

Until the scale audit is independently reviewed:

- no 25-turn Raw trajectory;
- no new Raw payoff runtime;
- no K1B runtime;
- no K2;
- no solver/tolerance/grid tuning;
- no new return/wage bounds are activated;
- no Results eligibility upgrade.

KFE remains `DIAGNOSTIC_ONLY`; the corrected-2018 finite-box upper-`b` leakage and MATLAB-style pinning remain independent blockers.

Results eligibility remains `FALSE`.
