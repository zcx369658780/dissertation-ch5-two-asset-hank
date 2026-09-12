# Chapter 5 MP4C K1 temporary transfer-control admissibility safeguard freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_TEMPORARY_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD__CHI0_CHI1_AND_OTHER_SCIENCE_FROZEN__NUMERIC_BOUND_NOT_YET_FROZEN`.

## 1. Owner scientific decision

The Owner approves introducing a **temporary transfer-control admissibility safeguard** for the rebuilt annual K1A household HA/HJB route.

This safeguard is authorized only as numerical continuation scaffolding for the transfer control `d`. It is not a structural economic restriction, not a final adjustment-cost law, and not evidence that household transfer behavior is economically bounded at the diagnostic values used during continuation.

The accepted instrumented G1/G2 diagnostic established the initiating chain:

`higher frozen HJB return input -> effective illiquid-return contribution -> mu_a / a-drift assembly -> HJB operator/value update -> value-derivative divergence -> transfer-FOC candidate divergence -> extreme raw transfer candidate -> quadratic adjustment-cost amplification`.

The Owner therefore authorizes a bounded continuation safeguard at the **transfer-candidate admissibility layer**, while keeping the underlying transfer FOC and adjustment-cost technology under observation.

## 2. Science frozen for the next gate

The following remain unchanged unless a later Owner decision explicitly reopens them:

- `chi0=.1`;
- `chi1=2 years`;
- annual continuous-time calibration;
- firm/HJB `delta=.10/year`;
- `rho=.05/year`, `rb=.02/year`, borrowing gap `.07/year`;
- productivity transition intensity `1/3/year`;
- G1/G2 return guards and the existing wage guard;
- derivative floors/safeguards;
- HJB/KFE equations;
- transfer FOC formula;
- policy selector and boundary/KKT laws;
- capital network, C1, labor science, grid, tolerance, and solver semantics.

The safeguard policy does **not** authorize changing any of these objects to obtain convergence.

## 3. Safeguard placement

The safeguard must act only after a raw transfer candidate has been computed from the accepted transfer FOC and before that candidate is allowed to enter final candidate selection / drift / cost assembly.

The rebuilt route must persist at least three layers wherever the safeguard is active:

1. raw transfer candidate from the accepted FOC;
2. admissibility status / safeguarded candidate presented to selection;
3. finally selected transfer control used in HJB drift and adjustment-cost construction.

The raw candidate must never be overwritten.

The safeguard may not silently alter the transfer FOC equation itself.

## 4. Temporary numerical classification

Any transfer-control admissibility rule introduced under this freeze is classified:

`TEMPORARY_NUMERICAL_CONTINUATION_SAFEGUARD`

It must not be called:

- structural household behavior;
- an estimated adjustment-frequency restriction;
- a final economic bound;
- a welfare-relevant borrowing/portfolio constraint.

Any steady state that depends on an active transfer-control safeguard remains `PROVISIONAL_STEADY_STATE` only.

## 5. Numeric values are not yet frozen

This Owner decision intentionally does **not** choose a numerical `d` lower/upper bound.

The next gate must be zero-science only and use already accepted G1/G2 instrumented traces to design a first transfer-control safeguard ladder. The design must distinguish normal finite transfer candidates from the heavy-tail / exploding candidate region and must avoid choosing bounds merely to maximize the observed HJB convergence count.

No new runtime is authorized until the numeric safeguard design is independently reviewed and the Owner/Reviewer freezes exact values.

## 6. Design principles for the future safeguard ladder

The zero-science design should, where evidence permits:

- preserve the central mass of ordinary transfer candidates;
- isolate the finite explosive tail that drives quadratic cost blow-ups;
- use symmetric bounds only if the accepted evidence supports approximate symmetry; otherwise report an asymmetric design as a candidate rather than forcing symmetry;
- provide several preregistered continuation stages rather than a single permanent hard cap;
- preserve province/turn/grid-cell hit identities and counts;
- separate raw-candidate hits from finally selected-control hits;
- compare proposed thresholds against asset-grid and annual-flow scales without claiming a structural economic interpretation;
- avoid post-hoc tuning on the same future runtime.

A future ladder must be frozen before scientific execution.

## 7. Price safeguards remain independently monitored

Return and wage safeguards remain unchanged and continue to require MATLAB-style province/turn hit monitoring.

Long-run target remains:

`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`

The transfer-control safeguard adds a separate long-run objective: final accepted economics should also demonstrate that substantive results do not depend on a binding temporary transfer-control continuation cap.

## 8. Current scientific boundary

Until the next zero-science safeguard-design gate is accepted:

- no longer G1/G2 runtime;
- no G3/G4;
- no wage relaxation;
- no transfer-control bound is numerically activated;
- no `chi0/chi1` tuning;
- no derivative-floor change;
- no boundary/selector change;
- no K1B/K2;
- no steady-state acceptance;
- no Results.

KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-`b` leakage and MATLAB-style pinning remain independent blockers. Results eligibility remains `FALSE`.
