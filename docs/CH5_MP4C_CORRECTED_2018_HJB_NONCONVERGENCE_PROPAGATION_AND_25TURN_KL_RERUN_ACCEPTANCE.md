# Chapter 5 corrected-2018 HJB nonconvergence propagation and 25-turn K/L rerun acceptance

Date: 2026-09-10

Reviewer verdict:

`HJB_PROPAGATION_REPAIR_AND_25TURN_KL_ACCEPTED__GOVINV_DOMINATES_CAPITAL_OVERSHOOT__LABOR_PROXY_SCALE_MISMATCH_REQUIRES_SEPARATE_REDESIGN`

Accepted candidate:

`0616c72b1f7f82185e6216149d06f035a071511c`

## Acceptance basis

The candidate correctly removes the predecessor harness's premature abort on finite, structurally usable HJB returns with `converged=false`. Such returns are explicitly classified `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`, propagated through KFE/aggregation, and their false convergence flags remain in the household batch. The final source steady-state predicate is not allowed to pass unless all household HJB flags are true. Nonfinite or malformed HJB/KFE objects still fail closed.

The bounded execution obeyed the exact task: one corrected-2018 Track-A trajectory, 25/25 turns, no scientific retry, no second trajectory, no parameter-cell tuning, and no change to HJB/KFE equations, grids, solver family, migration rule, GovInv rule, price bounds, damping, or hysteresis.

## Accepted K finding

Turns 20-25 show that firm total capital is systematically above the Track-A 2018 target. Across all late-window province-turn observations, `firm_K_total/Ktarget` has min/median/max `1.3422659595802506 / 2.359983542526 / 2.866669200187509`.

The overshoot is overwhelmingly GovInv-driven rather than household private capital-driven. Late-window median `private_K/Ktarget` is `0.00291675418808339`, while median `GovInv/Ktarget` is `2.3579476910000015`. The source-faithful initialization `GovInv0=Ktarget` mechanically overshoots once positive private supply is added, and the existing controller amplifies rather than removes the gap over this 25-turn prefix.

This finding is accepted as diagnostic evidence only. It does not by itself authorize a new GovInv economic rule.

## Accepted labor finding

Destination firm labor under the existing `Lt_seperate`-style migration allocation is extremely large relative to the initialization population proxy. Turns 20-25 pooled `firm_Lt_supply/N0` has min/median/max `4.589147349109114 / 14.2307874070677 / 153.05180501585224`; all 31 province late-window means are severely above the proxy.

This does not establish that firm labor itself is wrong, because `N0` is only a population/labor initialization proxy and not observed workplace employment. The result instead proves that the current comparison/normalization contract between household labor, population proxy, migration allocation, and destination firm labor is not yet scientifically closed.

## HJB/KFE boundary

There were 60 finite nonconverged-but-continued HJB province-turn observations across 20 provinces. Anhui recovered to convergence at turn 6 and remained converged through turn 25. Turns 23-25 had 31/31 HJB convergence.

All 775 KFE returns nevertheless remained `DIAGNOSTIC_ONLY`, including turns 23-25. Therefore HJB convergence-path behavior and KFE scientific validity remain distinct gates.

## Scientific disposition

Accepted conclusions:

- the predecessor turn-1 stop was a Python harness-policy error;
- source-style continuation with finite nonconverged HJB objects is implementable;
- `GovInv0=Ktarget` plus positive private supply creates an observed early capital overshoot;
- by turns 20-25 the capital overshoot is dominated by GovInv, not private household capital;
- the existing controller does not correct the overshoot over this bounded prefix;
- destination firm labor is not commensurate with the population proxy under the present normalization/reference contract;
- KFE remains independently diagnostic-only.

Not yet authorized:

- residual GovInv initialization;
- Lt normalization or redesign;
- new wage/return bounds;
- new damping/hysteresis;
- KFE/HJB production repair;
- steady-state production acceptance;
- Results.

`Results eligibility=FALSE`.
