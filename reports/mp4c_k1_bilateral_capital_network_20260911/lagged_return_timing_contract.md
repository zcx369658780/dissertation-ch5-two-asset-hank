# K1 lagged-return timing contract

Canonical label: `ALLOCATION_ITERATION_N_PLUS_1_USES_RETURN_SCORE_FROM_COMPLETED_ITERATION_N`.

1. Household iteration `n` receives a portfolio payoff inherited from a previously completed firm state.
2. Allocation iteration `n+1` may use a return-attractiveness score produced from completed iteration `n`.
3. Same-turn `firm -> return -> share -> capital -> firm` feedback is prohibited. The K1 module imports no firm, household, HJB, KFE, controller, one-turn, or trajectory implementation.
4. The module rejects provenance labelled `SAME_TURN` or `CURRENT_FIRM` and requires an explicit `LAGGED` or `COMPLETED_ITERATION` label.
5. This ordering is a numerical steady-state iteration contract, not a calendar-time instantaneous-adjustment claim.
