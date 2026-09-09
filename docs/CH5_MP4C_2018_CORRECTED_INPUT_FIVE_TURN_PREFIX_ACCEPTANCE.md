# Chapter 5 corrected-2018 five-turn bounded prefix acceptance

Date: 2026-09-09

Accepted candidate: `9864129dd2e97bae97238ab9cc588aea48682d29`

Reviewer verdict:

`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER_ACCEPTED__KFE_SOURCE_FREE_STATIONARITY_AND_UPPER_B_LEAKAGE_BLOCK_PREFIX_INTERPRETATION`

## Accepted findings

1. Fresh turns 1–3 reproduced accepted predecessor evidence exactly before turns 4–5 were entered.
2. The trajectory completed exactly five turns / 155 province updates with zero scientific retries; all 155 household/HJB/KFE/aggregate/firm calls returned.
3. Turn 4 and turn 5 returned densities are not accepted as source-free stationary distributions. All 31 provinces are classified `DIAGNOSTIC_ONLY` in both turns.
4. Near-machine negative density entries are not the material blocker: weighted negative mass is around machine precision. The material blockers are nonzero source-free stationarity residuals and upper-b outward leakage.
5. Turn 4/5 upper-b leakage is widespread: 620 positive upper-b leak cells nationally in each turn, with maximum leak rate about 2.2393. Lower-b/lower-a/upper-a outward leakage is zero in the saved diagnostics.
6. Turn 3 Anhui asset collapse is preserved. Turn 4–5 assets remain near the post-collapse level, but because density validity is blocked, these aggregates remain diagnostic rather than accepted economic distribution moments.
7. Turn 4 is the first observed turn where native adaptation opens (`national max nk_gap < .1`), and turn 4–5 execute native Zt adjustments and `LOW_RA_DECREASE_0P9` GovInv actions for all 31 provinces. This is observed controller behavior, not evidence that the KFE blocker is resolved.
8. No turn 6+, steady state, GE, annual model, MATLAB, IRF or Results execution occurred. Results eligibility remains FALSE.

## Scientific boundary

Do not continue the trajectory merely because turn 5 executed. The next route is zero-science-call post-processing attribution using the saved five-turn operator/density/drift artifacts. The objective is to determine whether the corrected-2018 turn 4–5 blocker is the same finite-box upper-b leakage / contaminated-row source mechanism previously established in the call725 `rah=.07` diagnostic, and to quantify how broadly it holds across provinces and turns.

No production boundary law, grid, solver, pinning, source, or model equation is changed by this acceptance.
