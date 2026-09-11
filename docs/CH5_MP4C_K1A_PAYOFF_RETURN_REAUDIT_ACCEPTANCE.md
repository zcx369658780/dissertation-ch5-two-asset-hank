# Chapter 5 MP4C K1A payoff-return re-audit acceptance

Date: 2026-09-12.

Reviewer verdict:

`K1A_PAYOFF_RETURN_REAUDIT_ACCEPTED__CLIPPED_RA_TRANSITIONAL_ONLY__RAW_RA0_SOURCE_CONSISTENT_CANDIDATE__OWNER_PERIOD_NUMERAIRE_FREEZE_REQUIRED_BEFORE_RUNTIME_CHANGE`

Accepted candidate:

`e6297bb19e10a77593e1c2c7876eb94f02c71533`

## Scope accepted

This acceptance covers the zero-science source/evidence re-audit only. The candidate is one commit ahead of baseline `9cf0a2bb0dc6994a1f9670eb78b30c684aad35fe` and changes only the audit report, six compact evidence receipts, one zero-science audit script and one focused zero-science test file. No production-science source, parameter, bound, grid, tolerance, solver semantic, K1B/K2 runtime or Results artifact is changed.

## Accepted scientific findings

1. The active source identity is `ra0 = rk + after_tax_profit_over_K - delta`, with `rk=mt*alpha/(K/Y)`. Source-used `ra` is `ra0` clipped to `[.02,.09]`.
2. K1A passes entering source-used `ra` into the destination-by-origin capital network and computes household illiquid payoff with the same `S` used for capital quantities: `rah = return_by_destination @ S`.
3. The lagged timing/provenance is consistent: completed-turn firm return is used by the next allocation/household iteration, and the audit verified the persisted same-`S` mapping through the authorized horizon without model feedback.
4. `[.02,.09]` remains `EMPIRICAL_NUMERICAL_SAFEGUARD`, not an economically identified payoff interval.
5. Accepted K1A evidence shows severe clipping information loss: upper clips are `754/775` for equal-share and `755/775` for geographic beta=2, lower clips are zero, 30 provinces are upper-clipped in all 25 turns, and used returns have only one or two unique values per turn.
6. Raw-return reconstruction closes to floating-point precision (`5.551115123125783e-17` maximum residual), with return pressure driven overwhelmingly by `rk`; the fixed depreciation deduction is approximately `.025`.
7. The static no-feedback comparison, holding persisted `S` fixed, gives median `S'ra0-S'ra_used` around `.172` and maxima near `.95`. This is accepted only as arithmetic evidence, not as evidence that a raw-payoff trajectory would converge.
8. Raw `ra0` is therefore a source-consistent payoff candidate that preserves cross-province ranking and dispersion, but calendar period, final economic numeraire/payoff interpretation and runtime safety remain unresolved.

## Scientific boundary

The current clipped/used `ra` remains only a transitional source-faithful bridge. This acceptance does not authorize replacing it with raw `ra0`, annualizing or transforming returns, changing `[.02,.09]`, smoothing/normalizing/risk-adjusting payoff returns, or changing the HJB/firm/capital-network runtime.

The K1B z-scored raw-`ra0` object remains an attractiveness signal only and is not a household payoff return. `beta_return=.5` remains preregistered but runtime-unauthorized. K2 remains unauthorized.

Corrected-2018 empirical finite-box upper-b leakage and MATLAB-style pinning remain an independent KFE blocker. Results eligibility remains `FALSE`.

## Next gate

No successor Builder task is authorized at this point because the next step requires an Owner/Reviewer scientific freeze, not engineering execution.

The next scientific decision must freeze the payoff-return contract, specifically the interpretation of raw `ra0` versus the transitional clipped bridge, including the model-period/numeraire convention and the meaning of the illiquid household payoff. If raw `ra0` is selected, a separate future exact task may then authorize only a bounded runtime-safety diagnostic before any K1B integration.
