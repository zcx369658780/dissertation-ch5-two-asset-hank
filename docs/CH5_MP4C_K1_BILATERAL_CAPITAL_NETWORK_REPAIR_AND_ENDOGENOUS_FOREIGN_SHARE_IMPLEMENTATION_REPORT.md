# Chapter 5 MP4C K1 bilateral capital-network implementation report

Date: 2026-09-11

Builder verdict: `K1_BILATERAL_CAPITAL_NETWORK_PASS__HOME_CAPITAL_RESTORED_PORTFOLIO_WEIGHTS_CONSERVED_AND_ENDOGENOUS_FOREIGN_SHARE_ENGINE_IMPLEMENTED`

## Outcome

A separately named pure K1 module now constructs one conserved `S[destination,origin]` portfolio matrix and uses it for both private-capital quantities and household `rah`. It restores `(1-theta_i)*A_i*N_i` to each origin's domestic destination, implements a stable foreign-only softmax over explicit distance and lagged-return scores, and keeps `theta_i` fixed. The module is not connected to one-turn, C1, firm, wage, steady-state, or trajectory runtime.

The asymmetric equal-foreign-share fixture has origin wealth `[20.0, 60.0, 120.0]`, total `200.0`. Repaired destination private K is `[79.0, 80.0, 40.99999999999999]` and also totals `200.0`; national residual is `0.0`. Share-column, origin-capital, home-retention, foreign-outflow, row-sum, and rah-same-matrix maximum residuals are respectively `0.0`, `0.0`, `0.0`, `0.0`, `0.0`, `0.0`.

Legacy destination private K is `[63.0, 50.0, 17.0]` versus repaired `[79.0, 80.0, 40.99999999999999]`. Their difference `[16.0, 30.0, 23.999999999999993]` exactly equals missing retained home capital. Legacy implied rah weight sums are `[0.93, 0.75, 0.4799999999999999]`, not one; repaired sums are `[1.0, 1.0, 1.0]`. The repaired equal-share case therefore removes destination `theta_j` double weighting.

## Required answers

1. **Retained home private capital restored exactly?** Yes. Every diagonal flow equals `(1-theta_i)*A_i*N_i`; the fixture maximum residual is `0.0`.
2. **National private K equals total household illiquid wealth?** Yes under the current bridge. Both equal `200.0` in the fixture and the national residual is `0.0`.
3. **Do quantity and rah use the same matrix?** Yes. Both are computed from the single returned `portfolio_shares_destination_origin`; the direct rah identity residual is `0.0`.
4. **Does equal-foreign-share repair remove destination theta double weighting?** Yes. Foreign payoff weights are `theta_i/(N-1)` and never multiply `theta_j`; legacy non-unit weight sums are reproduced in the discrepancy receipt.
5. **Is lagged timing encoded without same-turn circular feedback?** Yes. The API requires explicit lagged/completed-iteration provenance, rejects same-turn/current-firm labels, imports no firm runtime, and remains disconnected from active one-turn code.
6. **Can later distance + lagged-return shares be supported without more HJB assets?** Yes. The pure post-household aggregate portfolio map operates on each origin's scalar aggregate illiquid wealth, preserving the existing two-asset household state space.
7. **What Owner decisions remain before science?** Owner must freeze dimensionless distance/friction data mapping, lagged-return-score normalization and source, `beta_distance`, `beta_return`, any adjustment/smoothing rule, and the payoff-return concept (`ra0`, clipped `ra`, normalized or expected return). Price/return units remain unresolved; no values were inferred here.
8. **Is engineering evidence sufficient for a later bounded K1 trajectory task?** Conditionally yes: the isolated algebra/API is ready for a separately authorized integration task after the preceding Owner decisions. This PASS does not itself authorize runtime integration or a trajectory, and C1 GovInv plus KFE would require separate revalidation.

## Verification and boundary

Focused suite: `29/29` passed after one message-order repair; compile and diff checks are recorded separately. The legacy source SHA-256 remains `BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40`. All returned arrays are read-only. Scientific/model/runtime calls and selected scientific coefficients are zero. Results eligibility remains `FALSE`.
