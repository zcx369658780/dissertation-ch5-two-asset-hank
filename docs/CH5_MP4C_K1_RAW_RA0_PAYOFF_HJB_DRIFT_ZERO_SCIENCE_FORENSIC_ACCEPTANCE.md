# Chapter 5 MP4C K1 raw `ra0` payoff HJB/drift zero-science forensic acceptance

Date: 2026-09-12.

Reviewer verdict:

`RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC_ACCEPTED__SCALE_EXPOSURE_AND_ACCEPTED_TRANSFER_COST_AMPLIFICATION_LOCALIZED__OWNER_PAYOFF_MAPPING_SCALE_DECISION_REQUIRED`

Accepted candidate:

`cd5abea31cfbfcdb4170970df7e0504b394571d5`

## Scope accepted

This acceptance covers only the zero-science forensic over the already accepted Control/Raw five-turn evidence. The candidate is one commit ahead of baseline `fb5ebaea842f7ce4c3bfa29e6aa328d72fd94eb4` and changes only one forensic analyzer, one focused test, one report and compact forensic evidence. No `src/` scientific implementation or runtime equation is changed. New scientific/model calls are all zero.

## Accepted findings

1. Raw payoff stress is not a simple boundary-only pathology. Most top drift/transfer/cost extreme cells are interior in the accepted `(b,a,z)` grid.
2. The accepted source chain is consistent with raw payoff scale entering household HJB as `r_a`, changing solved value derivatives, then being amplified through the accepted transfer FOC and quadratic adjustment-cost law. The forensic does not infer a new structural law.
3. Raw treatment materially worsens HJB convergence relative to Control: treatment horizon convergence is `12/124` versus `49/124`, with `45` Control-converged -> Raw-nonconverged province-turns and `8` reverse recoveries.
4. Raw payoff exposure and prior raw `ra0`/clipping gap are nearly rank-identical, but payoff level does not by itself rank HJB stress; province-turn correlations between `rah` and HJB statistic are weak. The attribution is therefore scale exposure interacting with state/value-derivative dynamics, not a simple monotone payoff-level threshold.
5. Raw substantially expands upper-`a` outward regimes, but the largest drift/transfer/cost extremes are predominantly interior. Existing upper-`b` outward counts are stronger in Control and remain a separate baseline/source behavior.
6. Control already contains very large finite transfer/cost/drift extremes. Raw is smaller than Control in a material subset of matched province-turn maxima and at the global maxima in turn 4. The correct attribution is mixed baseline numerical behavior plus substantial Raw incremental amplification.
7. Raw lower-`b` exact-sign outward counts are all approximately `-8.881784197e-16`, below the accepted `1e-12` drift tolerance with zero transfer/cost and zero/zero policy labels; they are accepted as floating-point sign noise, not material boundary/KKT failure.
8. Standalone KKT residual remains `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`. No new KKT PASS or FAIL is accepted.
9. All reported correlations are descriptive only, not causal evidence.

## Scientific boundary

This acceptance does not authorize any new payoff mapping, calendar conversion, annualization, normalization, cap, clipping rule, smoothing, boundary-law change, transfer-cost change, HJB/KFE change, solver/tolerance/grid change, K1B, K2, longer Raw trajectory, steady-state claim or Results claim.

The earlier raw `ra0` payoff contract remains the currently frozen intended K1 payoff source object, but its current level as direct HJB `r_a` is not scientifically/numerically accepted for longer runtime because the accepted short-horizon evidence shows severe HJB nonconvergence and transfer/cost sensitivity.

## Next gate

The next gate is an Owner scientific decision on payoff mapping / scale interpretation. Reviewer should not publish a successor Builder task until the Owner freezes whether current-level raw `ra0` should remain the direct household HJB payoff or whether a source-backed period/scale mapping is required.

K1B remains unauthorized. K2 remains unauthorized. Corrected-2018 empirical KFE remains `DIAGNOSTIC_ONLY`. Results eligibility remains `FALSE`.
