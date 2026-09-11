# Chapter 5 MP4C K1 payoff-return contract freeze

Date: 2026-09-12.
Status: `OWNER_APPROVED_RAW_RA0_PAYOFF_CONTRACT__MODEL_TIME_NET_PRODUCTIVE_CAPITAL_RETURN__NO_CALENDAR_ANNUALIZATION__RUNTIME_SAFETY_GATE_REQUIRED`.

This document records the Owner-approved payoff-return contract after the accepted zero-science payoff-return re-audit. It supplements the K1 capital-network and scoring/data freezes and supersedes the transitional K1A payoff bridge as the intended final K1 household illiquid payoff object, subject to a separate bounded runtime-safety gate before any production/runtime switch.

## 1. Final payoff source object

The Owner freezes the source-level K1 household illiquid payoff object as the raw pre-clip firm return:

`ra0_j = rk_j + after_tax_profit_over_K_j - delta`

with the accepted source identity:

`rk_j = mt_j * alpha_j / (K_j / Y_j)`.

For the bilateral portfolio layer, the intended household payoff is therefore:

`rah_i = sum_j S[j,i] * ra0_j`

where `S` is the same destination-by-origin portfolio-share matrix used to allocate household illiquid wealth into destination private productive capital.

The standardized K1B return-attractiveness score remains a different object. It is not a payoff level and must never replace `ra0` in `rah`.

## 2. Economic interpretation

`ra0` is frozen as a **per-model-time endogenous net productive-capital return rate** paid to the household illiquid provincial portfolio fund.

It is not currently interpreted as an observed financial-market return, bond yield, stock return, or directly observed asset-price return.

It is an internally model-consistent productive-capital payoff object constructed from the destination firm block.

## 3. Period convention

The source does not establish a defensible calendar mapping such as annual, quarterly, or monthly.

Therefore the frozen interpretation is:

`MODEL_TIME_RETURN_RATE__CALENDAR_PERIOD_UNRESOLVED`.

No annualization, de-annualization, compounding conversion, or calendar-period scaling is authorized.

Future empirical/calendar interpretation may be added only through a separate source/calibration decision. Numerical values such as `0.26` must not be described as “26 percent annual return” under the current contract.

## 4. Numeraire convention

Within the model, `ra0` is treated as a dimensionless rate-like payoff object formed from output/capital and profit/capital terms plus depreciation.

The project does not claim that it has been externally calibrated to a market-asset-price numeraire. The accepted convention is therefore:

`INTERNAL_MODEL_PRODUCTIVE_CAPITAL_RETURN_NUMERAIRE__EXTERNAL_MARKET_MAPPING_UNRESOLVED`.

This unresolved external mapping does not block use of `ra0` as the internal household illiquid payoff object, but it blocks stronger empirical claims about observed market returns.

## 5. Historical clipped return

The source-used `ra = clip(ra0, .02, .09)` remains documented as a historical runtime object.

Its bounds remain classified as:

`EMPIRICAL_NUMERICAL_SAFEGUARD`.

They are not structural economic payoff bounds and are not the final K1 household payoff contract.

The accepted re-audit showed severe information loss under clipping: equal-share and geographic-beta-2 paths had `754/775` and `755/775` upper clips, respectively, with 30 provinces upper-clipped in all 25 turns and only one or two used-return values per turn.

Accordingly, the clipped return may remain available for provenance comparison and diagnostics, but it must not be presented as the final economically meaningful K1 payoff law.

## 6. Runtime authority boundary

This freeze does **not** by itself authorize switching the active runtime from clipped `ra` to raw `ra0`.

A separate bounded runtime-safety diagnostic must first test the raw-payoff substitution under tightly controlled scope.

The safety task must isolate the payoff substitution and must not simultaneously activate K1B return-attractiveness feedback, K2 endogenous theta, normalized labor, smoothing, new calibration, new bounds, solver changes, tolerance changes, grid changes, or KFE redesign.

If the raw-payoff route generates numerical or economic failures, the failure must be preserved and diagnosed. Parameters, caps, solver settings, tolerances, grids or coefficients must not be tuned merely to recover PASS.

## 7. K1B relationship

The K1B foreign-destination attractiveness signal remains:

`return_score_j^(n) = (ra0_j^(n) - mean_j(ra0^(n))) / sd_j(ra0^(n))`

using completed-iteration raw `ra0` only at the next allocation iteration.

The preregistered `beta_return=.5` remains frozen but runtime-unauthorized until the raw-payoff runtime-safety gate is reviewed.

Thus K1B will, if later authorized, use raw `ra0` in two distinct ways:

- payoff level: `S' * ra0`;
- attractiveness signal: lagged cross-sectional z-score of raw `ra0`.

These must remain separate in code, evidence and interpretation.

## 8. KFE and Results boundary

The corrected-2018 finite-box upper-b leakage and MATLAB-style pinning remain an independent KFE blocker.

This payoff freeze does not upgrade KFE, steady state, annual, IRF, welfare or Results eligibility.

Results eligibility remains `FALSE`.

## 9. Next authorized scientific gate

The next exact Builder task is a bounded raw-`ra0` payoff runtime-safety diagnostic.

Its purpose is not to prove final steady-state validity. It is to determine whether replacing the transitional clipped payoff bridge with the frozen raw payoff object can be executed without immediate HJB/KKT/control/drift pathologies and without violating the accepted K1 capital-network, C1 and source-faithful-labor contracts.
