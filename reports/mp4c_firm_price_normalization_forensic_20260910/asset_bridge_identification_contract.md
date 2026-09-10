# Household-to-macro asset bridge identification contract

## Current literal bridge

For household province `i`, the HJB returns mean illiquid grid holdings `At_i`. The current one-turn source then applies:

`tempKt = sum_i(inter_prv_ratio_i * At_i * N_i)`

`Kt_supply_i = [tempKt - inter_prv_ratio_i * At_i * N_i] / 30`

and the firm consumes:

`K_firm_i = Kt_supply_i + GovInv_i`.

This is the exact `At_grid -> At*N -> Kt_supply -> Kt_supply+GovInv -> firm K` path at `HANK_mp_1turn.m:29-36` and `HANK_firm.m:9-15`. Liquid `Bt` is not productive capital in this path.

## Dimensionally explicit successor form

The missing conversion must be visible:

`K_private_MU = At_grid * beta_a * N_NU`,

where `beta_a` has units `MU/(grid-unit*NU)`. The cross-province allocation must apply the same `beta_a` before forming destination `Kt_supply_MU`. Current source algebra implicitly inserts `beta_a=1`, but neither the HJB grid nor initialization parameters define that value economically.

Using legacy `At=2` and accepted 2018 N only as a descriptive baseline, `beta_a=1` gives `At*N/K0` min/median/max `0.004282158069342776 / 0.011388983617207863 / 0.019977992688578954` (Tianjin minimum, Gansu maximum). These ratios are `SOURCE_FAITHFUL_BASELINE_ONLY`; they do not identify or select `beta_a`.

## Legitimate future identification routes

- document a household currency/grid normalization from an independently authoritative household data or calibration contract;
- match aggregate household illiquid wealth to independently measured private productive capital, after separately accounting for public capital and the cross-province ownership/allocation map;
- identify the flow numeraire from independently measured consumption, labor income, transfers, and period frequency, then apply the same stock-flow convention to `a` and `b`;
- construct a full dimensional accounting identity with independently sourced household wealth and productive-capital targets and test it outside convergence behavior.

No route is adopted here. Convergence, price-bound occupancy, target K matching by construction, or GovInv residual truncation may not identify `beta_a`.
