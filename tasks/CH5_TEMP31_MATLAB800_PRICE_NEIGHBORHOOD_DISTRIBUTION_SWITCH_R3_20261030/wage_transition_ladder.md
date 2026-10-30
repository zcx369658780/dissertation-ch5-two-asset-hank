# Predeclared net-wage ladder19 to20

All pairs fix rah=.05, rb=.02. P2(wt19) and D07(wt20) are immutable historical reference results; E00-E04 are new cold-start measurements. No historical point was rerun. The rule was fixed before execution: abs(delta At)>=1 OR abs(delta b_upper_mass)>=.25. Adjacent absent/nonconvergent points are UNTESTED_INTERVAL; no interpolation, new point or gap bridging.

| Pair | changed axes | status | delta At | delta Bt | delta b upper | TV a | TV b | transition flag | strict warning |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| P2 -> E00 | wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | -0.003982084602 | 0.0004584149268 | 0.0007133622946 | 0.001222852744 | 0.001283612531 | False | True |
| E00 -> E01 | wt | UNTESTED_INTERVAL | - | - | - | - | - | NOT_EVALUATED | True |
| E01 -> E02 | wt | UNTESTED_INTERVAL | - | - | - | - | - | NOT_EVALUATED | True |
| E02 -> E03 | wt | UNTESTED_INTERVAL | - | - | - | - | - | NOT_EVALUATED | True |
| E03 -> E04 | wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | 2.18407263 | 2.887900476 | 0.4393009996 | 0.5507289162 | 0.6423866234 | True | True |
| E04 -> D07 | wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | -0.0001810035925 | 0.0005739458773 | 0.0005536382758 | 0.0003428724694 | 0.0005536382758 | False | True |

The complete signed20-bin changes and raw marginal identities are in discrete_transition_flags.json and per-point results. Marginals already represent probability mass, so the half-L1 calculation applies no additional db*da factor. Tiny signed entries are retained; comparisons require inherited mass/negative-mass diagnostics, and strict original stationarity is displayed independently. These are descriptive distances on conditional source-method outputs, not proof of invariant-distribution TV or economic bifurcation. A flagged pair only locates a change between two measured prices, not an unobserved critical value or unique steady-state branch.
