# Reviewer Acceptance — C1 price/numeraire raw-ra forensic and normalization specification

Date: 2026-09-11

Reviewer verdict:

`C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_ACCEPTED__RAW_RA_PRESSURE_PRIMARILY_YK_MPK_GEOMETRY__RETURN_BOUNDS_NOT_ECONOMICALLY_IDENTIFIED__PRICE_NORMALIZATION_OWNER_DECISION_REQUIRED`

Accepted candidate:

`8c0606ebc67e8f51a0a27ff06505ce67bd69ba7d`

Base reviewed:

`82d81017375e05d08176fda93d36233befa94dab`

## Acceptance basis

The candidate is accepted as zero-science forensic/specification evidence. It changes no active model runtime, performs no scientific/model calls, and decomposes all 775 accepted C1 province-turn observations with maximum raw-`ra0` reconstruction error `2.220446049250313e-16`.

At turn 25, 30/31 provinces have raw `ra0>.09`; this remains 30/31 when the profit term is removed and also remains 30/31 under the static `mt=mstar=.9` counterfactual. Profit is floored at zero in 28/31 provinces and depreciation contributes a fixed `-.025`, so neither is the source of the upper pressure. The dominant accounting term is the MPK-like component `rk=mt*alpha*Y/K`; the accepted corrected-2018 `Y/K` geometry relative to the historical `.09` clip is the primary source, with `mt` only modestly amplifying it.

The return interval `[.02,.09]` is accepted as `EMPIRICAL_NUMERICAL_SAFEGUARD`, not an economically identified admissible return interval. The wage interval `[.8,1.3]` is accepted as `SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`. No replacement return bound, period convention, or price unit is identified by this task, so widening/removing the clips remains `INSUFFICIENT_EVIDENCE`.

The candidate correctly distinguishes the firm raw wage from the household composite wage. Their numeric levels are not directly comparable absent an explicit common currency/period/labor-unit/aggregator mapping. This forensic does not establish that the wage-numeraire issue causes the current raw-`ra0` pressure; wage enters the return path only indirectly through later household and firm states.

Normalized labor remains accepted but intentionally inactive. The current evidence is sufficient to diagnose return pressure before stacking a labor normalization change, but not sufficient to select a new return/wage normalization contract.

KFE remains an independent scientific blocker: accepted C1 evidence still has 775/775 KFE returns classified `DIAGNOSTIC_ONLY`. This acceptance does not repair or reinterpret KFE.

## Governance boundary

This acceptance does **not** authorize:

- widening or deleting `ramin/ramax`;
- selecting a new `ra` target or admissible interval;
- rescaling firm or household wages;
- activating normalized labor in a scientific trajectory;
- changing HJB/KFE, grids, solver, alpha, depreciation, or C1 capital accounting;
- running an outer trajectory, production steady state, GE, annual model, IRF, or Results.

The next scientific gate requires an Owner decision on a pre-registered, unit-consistent price/return normalization object. Until that is frozen, no successor scientific task should be published automatically.

`Results eligibility=FALSE`.
