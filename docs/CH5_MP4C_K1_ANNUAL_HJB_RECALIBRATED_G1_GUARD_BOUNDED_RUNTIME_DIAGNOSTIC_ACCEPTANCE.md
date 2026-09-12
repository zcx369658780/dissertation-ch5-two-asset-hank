# Chapter 5 MP4C K1 annual HJB recalibrated G1-guard bounded runtime diagnostic acceptance

Date: 2026-09-12.

Reviewer verdict:

`ANNUAL_RECALIBRATED_K1A_G1_DIAGNOSTIC_GUARD_SHORT_HORIZON_ROUTE_ACCEPTED__G1_FULLY_SATURATED__WAGE_GUARD_HIGHLY_SATURATED__NOT_READY_FOR_LONGER_G1_OR_G2__OWNER_NUMERAIRE_AND_GUARD_CALIBRATION_DECISION_REQUIRED`

Accepted candidate: `a7eccde5e0ca694f95d3b3c082bfa82e0ce8cbb1`.

## Accepted scope

The candidate is accepted as a bounded short-horizon diagnostic only. It changes no production `src/` scientific equations and preserves the annual recalibration contract, K1 bilateral-capital accounting, same-`S` quantity/payoff mapping, C1 accounting, source-faithful labor, lagged payoff provenance, and K1B/K2 prohibition.

Both U and G1 completed 5/5 turns with zero NaN/Inf, zero scientific retry, zero same-turn feedback, and no capital/C1 hard failure. The external evidence manifest passed `1041/1041`; the receipt-only inherited `.025` reconstruction issue was independently adjudicated without rerunning science, and the annual `.10` identity was independently recomputed to machine precision.

## Accepted scientific findings

1. The annual recalibration is operationally coherent for the bounded route: `rho=.05/year`, `rb=.02/year`, gap `.07/year`, `delta=.10/year`, `Q_z=1/3/year`, `chi0=.1`, `chi1=2 years`.
2. Relative to the prior `.025` route, turn-1 raw firm `ra0` falls by exactly about `.075` province-by-province, as expected from the depreciation change.
3. Annual unguarded U remains executable but strongly nonconverged: treatment HJB convergence is `11/124`.
4. G1 modestly improves aggregate convergence to `18/124` and reduces the worst HJB statistic in turns 3-5, but does not uniformly reduce transfer/cost/drift stress.
5. The G1 return guard is fully upper-saturated: `124/124` treatment province-turns consume `r_a=.20`; therefore the HJB interface loses all cross-province return-level ranking even though the pre-guard converted `rah` retains 31 distinct province values per turn.
6. The existing wage guard is also highly active: G1 treatment saturation is `112/124` (`90.3%`).
7. Because both return and wage interfaces are heavily guard-dependent, the current G1 path is only diagnostic scaffolding. It is not yet an informative longer-horizon provisional steady-state experiment.
8. The accepted result does not justify automatic G2 progression. G2 would be a new scientific/diagnostic decision because the current evidence also shows unresolved wage/asset-numeraire compression and mixed control/drift response.

## Reviewer route decision

Do **not** issue a longer G1 run. Full return-guard saturation means a longer G1 trajectory would mostly study a constant `r_a=.20` household interface rather than the intended provincial payoff heterogeneity.

Do **not** automatically advance to G2. Before widening the return guard, the Owner must decide whether the annual household wage/asset numeraire and temporary guard calibration should be revised jointly. The return and wage guard saturation should be treated as evidence that the current numerical interface is over-compressed, not as evidence that the underlying annual K1 capital network has failed.

The next gate is therefore an Owner scientific decision on annual household numeraire / wage scaling and the next preregistered diagnostic-guard design. A subsequent bounded runtime task may then either: (a) revise the wage/household-flow interface and keep G1; or (b) authorize G2 together with an explicit wage-guard policy. No Builder task is active until that decision is frozen.

KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-`b` leakage and MATLAB-style pinning remain independent blockers. K1B and K2 remain unauthorized. Results eligibility remains `FALSE`.
