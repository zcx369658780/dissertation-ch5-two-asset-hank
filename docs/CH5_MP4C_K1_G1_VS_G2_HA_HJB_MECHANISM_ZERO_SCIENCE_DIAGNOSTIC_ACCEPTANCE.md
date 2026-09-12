# Chapter 5 MP4C K1 G1-vs-G2 HA/HJB mechanism zero-science diagnostic acceptance

Date: 2026-09-12.

Reviewer verdict:

`G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC_ACCEPTED__MIXED_RETURN_REGIMES_AND_PATH_HISTORY_CONFIRMED__DIRECT_CAUSAL_ATTRIBUTION_NOT_IDENTIFIABLE__INSTRUMENTED_BOUNDED_DIAGNOSTIC_REQUIRED`

Accepted candidate:

`f7c52f061b9eb3666d26985602ad6527774b5bb2`

## Accepted scope

This acceptance covers only the zero-science analysis of already persisted G1/G2 evidence. The candidate adds a report, compact evidence, one static analyzer and focused tests; it makes no production-science, equation, parameter, guard, grid, tolerance or solver change and makes zero new model/scientific calls.

## Accepted findings

1. G2 deterioration is not confined to newly-unsaturated return observations. Newly-unsaturated observations are all nonconverged, but the largest HJB statistic and global transfer/cost/drift extrema occur in the still-upper-saturated partition.
2. G2 stress is predominantly interior among extreme cells, while some worst-statistic cases remain boundary-linked. Material outward face hits decline in total from G1 to G2, so a boundary-only explanation is rejected.
3. G1 already contains large finite HA/HJB extrema, and several G1 worst cells improve markedly under G2. The mechanism is therefore mixed, not uniformly monotone in the wider return guard.
4. Large G1->G2 policy-label changes are observed, but the accepted evidence does not persist directional/value derivatives, pre-selector candidates, per-iteration HJB traces or a standalone KKT residual.
5. Because paths share the same turn-1 state but diverge thereafter, turn 2 can support an immediate common-entering-state comparison, whereas turns 3-5 embody endogenous path history and must not be treated as same-state causal comparisons.
6. Persisted evidence is insufficient to identify whether return exposure, wage-guard interaction, value-derivative amplification, selector changes or path history is the first destabilizing channel.

## Scientific boundary

This acceptance does not authorize longer G2, G3/G4, wage-guard relaxation, parameter tuning, `chi0/chi1` changes, derivative-floor changes, solver/tolerance/grid changes, K1B, K2, steady-state acceptance or Results.

Standalone KKT residual remains `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`. KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers.

## Next gate

The next gate is a fresh bounded diagnostic runtime with additional observation-only instrumentation. It must repeat the same annual G1/G2 short-horizon scientific design with no science change and persist the missing HJB intermediate objects needed to separate the immediate turn-2 common-state response from later path-history propagation.

Results eligibility remains `FALSE`.
