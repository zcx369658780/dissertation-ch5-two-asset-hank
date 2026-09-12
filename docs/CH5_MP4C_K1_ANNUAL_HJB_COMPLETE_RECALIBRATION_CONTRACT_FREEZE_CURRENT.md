# Chapter 5 MP4C K1 annual HJB complete recalibration contract freeze

Date: 2026-09-12.
Status: `OWNER_APPROVED_ANNUAL_CONTINUOUS_TIME_RECALIBRATION_CONTRACT__DELTA_POINT10__RAW_RA0_ECONOMIC_SOURCE_RETAINED__TEMPORARY_DIAGNOSTIC_GUARDS_PREREGISTERED`.

## 1. Owner scientific choice

Existing sources do not uniquely identify a common calendar base. The Owner therefore makes a new calibration choice for the rebuilt Chapter-5 multi-province HANK numerical system:

`MODEL_TIME_BASE = ANNUAL_CONTINUOUS_TIME`.

This is a new Owner-frozen recalibration contract, not a claim that the legacy implementation already had coherent annual units.

## 2. Annual common-time contract

The following objects are interpreted per year in the rebuilt K1A route:

- household discount intensity: `rho = 0.05 / year`;
- liquid return: `rb = 0.02 / year`;
- borrowing-return gap: `0.07 / year`;
- firm/HJB depreciation: `delta = 0.10 / year`;
- productivity generator off-diagonal intensity: `1/3 per year`;
- firm `Y/K` and after-tax profit/K retain the corrected-2018 annual flow/stock scale and are not divided by four;
- raw productive-capital payoff source becomes `ra0_annual = rk_annual + after_tax_profit_over_K_annual - 0.10`;
- household illiquid payoff remains `rah_i = sum_j S[j,i] * ra0_annual_j`, with the same destination-by-origin `S` used for capital quantities;
- wage, consumption, transfer and adjustment-cost objects entering the HJB are interpreted as annual flows in the unchanged household-model asset numeraire;
- outer steady-state iterations remain numerical fixed-point iterations and have no calendar-time interpretation.

The dissertation statement that 2.5 percent quarterly depreciation corresponds to approximately 10 percent annually is used only as support for the new annual calibration choice. `0.10` is not claimed to be the exact compounded transform of `0.025`.

PIM depreciation `0.096` remains a separate annual capital-stock-construction parameter and must not replace the firm/HJB depreciation rate.

## 3. Adjustment-cost time calibration

The current economic form of the transfer/adjustment technology remains unchanged. For the first rebuilt annual K1A runtime, the existing coefficient values are retained as provisional annual calibration:

- `chi0 = 0.1`;
- `chi1 = 2 years` in the dimensional interpretation required for the quadratic adjustment-cost term to remain an annual flow when `d` is asset units per year.

This is a provisional Owner calibration, not a final estimated parameter. It must not be tuned after seeing the same run merely to obtain convergence. Any future change to `chi0/chi1` requires a fresh scientific calibration gate.

## 4. Asset and wage numeraire

This freeze changes the common time unit but does not redefine the household asset numeraire. The existing household `a,b,c,w,T,d` model-unit convention is retained provisionally.

Firm-side macro levels may not be injected directly into the household HJB merely because the time unit is annual. Any existing firm-to-household wage aggregation/normalization interface remains explicit and must be audited in runtime evidence. Absolute market-price interpretation remains unresolved.

## 5. Raw, converted and guarded layers

The rebuilt route must keep three conceptually distinct layers wherever a diagnostic guard is used:

1. raw firm object, e.g. annual `ra0_annual`;
2. converted/model-time object under this annual contract; for firm annual return components this is the same annual rate after replacing depreciation with `0.10`;
3. HJB-interface guarded object used only as temporary numerical diagnostic scaffolding.

Raw and converted values must be persisted even when the guarded value is used in the HJB.

## 6. First preregistered diagnostic guards

For the first bounded annualized K1A runtime only, the following guards are frozen before execution:

- household HJB illiquid return input `r_a`: clip converted annual `rah` to `[-0.05, 0.20]`;
- firm wage `wjt`: retain `[0.8, 1.3]` only as a temporary diagnostic guard on the existing guarded route.

These values are deliberately classified as `TEMPORARY_NUMERICAL_DIAGNOSTIC_SCAFFOLDING`, not structural economics or final calibration.

The first relaxation ladder is preregistered as:

- Stage G1: `r_a in [-0.05, 0.20]`;
- Stage G2: `r_a in [-0.10, 0.35]`;
- Stage G3: `r_a in [-0.20, 0.60]`;
- Stage G4: illiquid-return guard OFF.

No later stage is authorized by this freeze alone. Each relaxation stage requires fresh Reviewer authority after evidence from the prior stage. Wage-guard relaxation is not yet numerically frozen and must be separately preregistered before change.

## 7. Accounting and capital-network contract unchanged

The accepted K1 bilateral capital network remains in force:

- fixed `theta_i = inter_prv_ratio_i` in K1A;
- `beta_distance = 2.0` for the pure-geographic scientific path;
- `beta_return = 0`;
- source-faithful labor;
- smoothing OFF;
- C1 `GovInv=max(Ktarget-Kprivate,0)`;
- same `S` for capital quantity and household payoff aggregation.

K1B and K2 remain unauthorized.

## 8. First-runtime scientific boundary

The next runtime is a bounded diagnostic of the annual recalibration plus preregistered G1 guards. It is not a final steady-state experiment.

Any state requiring guards is classified as provisional. The task must record guard saturation/hit counts by province/turn and, where available, grid cell, and must preserve raw/converted/guarded values.

No solver, tolerance, grid, HJB/KFE equation, boundary/KKT law or capital-network equation may be tuned in response to runtime outcomes.

## 9. KFE and Results boundary

Corrected-2018 empirical KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers.

No annual recalibration or diagnostic guard upgrades steady-state, KFE, K1B/K2, annual/IRF/welfare or Results eligibility.

Results eligibility remains `FALSE`.
