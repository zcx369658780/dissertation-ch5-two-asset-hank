# Chapter 5 MP4C C1 price/numeraire and raw-ra upper-pressure forensic/spec

Date: 2026-09-11

Builder verdict: `C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_PASS__RETURN_PRESSURE_DECOMPOSED_AND_NEXT_GATE_IDENTIFIED`

## Result

All 775 accepted C1 province-turn rows were statically decomposed with maximum raw-ra reconstruction error `2.220446049250313e-16`. No firm, wage, household, HJB, KFE, migration, controller, outer-turn, MATLAB, root/Brent, GE, annual, IRF or Results runtime was called.

At turn 25, raw ra0 min/median/max is `0.08784757593701044/0.2140623214392065/0.40633797203054156` and lower/interior/upper counts remain `0/1/30`. Y/K is `0.15599747756595098/0.32382875036281344/0.5626487280968079`; recovered mt is `0.9748297435105832/1.0001936748583722/1.038648805373765` around mstar `0.9`. Profit is floored at zero in `28/31` provinces and profit/K min/median/max is `0.0/0.0/0.0008065469707180163`.

## Attribution

The upper pressure is overwhelmingly the MPK-like `rk=mt*alpha*Y/K` term. Among the 30 upper provinces, rk's share of positive pre-depreciation components is `0.9965424662935316/1.0/1.0`, while after-tax profit/K contributes `0.0/0.0/0.0034575337064683027`. Removing profit leaves `30/31` above `.09`; replacing mt by source mstar while retaining the source profit equation also leaves `30/31` above `.09`. Depreciation offsets every row by exactly `-.025`. Cross-sectionally, upper-province Y/K coefficient of variation is `0.31296628873828747` versus mt `0.017122879173393078`. Thus corrected empirical Y/K relative to the historical bound is primary; mt modestly amplifies it, profit is negligible at turn 25, and depreciation reduces rather than causes pressure.

Saved `mt` and `PIt` were not columns in the accepted ledger. `mt` is recoverable from the independently saved `rk`, K, alpha and Y identity; `PIt/K` is then reconstructed from the source profit equation using frozen theta, pit and corptau. A separate NKPC reconstruction of mt is not possible because complete lagged K, prior rk and inflation-lag objects were not saved. This limitation is explicit and does not affect the component identity check.

## Bounds and geometry

The return interval `[.02,.09]` is classified `EMPIRICAL_NUMERICAL_SAFEGUARD`, not an economically identified rate interval. The source says it prevents convergence-time failure and contains commented alternatives. Wage `[.8,1.3]` is `SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`: its clipping behavior is source-defined, but its currency, period and calibration are not. The K/Y values in `ky_return_geometry.csv` are algebraic comparisons only, not targets or recommendations.

Answer on widening/removing return clips: `INSUFFICIENT_EVIDENCE`. Current rows show that the numerical bound is tight relative to corrected Y/K, but do not identify an economically admissible period, return concept or replacement interval.

## Wage/numeraire and sequencing

Firm raw wage has implied macro unit MU/NU per model period, while the legacy wage clip lacks an absolute-unit mapping. Household `w` is a nonlinear, unnormalized 31-destination composite of clipped `wjt`; it is not a directly comparable single-firm wage level. The earlier raw firm wage near 12 and household composite near 18 are therefore compatible with different aggregation scales and unresolved absolute numeraire mapping. Wage does not enter the current ra0 equation directly, so this task does not establish causal contamination of ra0; it can affect future returns indirectly through household labor/assets and firm Y, K and mt.

Normalized labor should remain inactive until the price/return and wage numeraire mapping is identified. Labor enters ra0 indirectly through Y, K/L and the lagged-L term in mt, but turn-25 pressure is already reproduced almost entirely by saved Y/K and rk. Stacking normalized labor first would confound these channels.

## Next gate and blockers

The lowest-risk next scientific experiment is conditional on an Owner-approved, pre-registered price/return normalization object: one initialization-only price receipt on the frozen C1 corrected-2018 inputs, with no outer trajectory and no post-observation tuning. It must compare raw and mapped units without silently changing bounds. This report does not publish or authorize that task.

KFE remains an independent scientific blocker: accepted C1 has 775/775 KFE `DIAGNOSTIC_ONLY`. This forensic does not repair or reinterpret KFE. Results eligibility remains FALSE.

## Required questions answered

1. **Why are 30/31 raw-ra values above `.09` although C1 holds K at target?** Holding K at the corrected empirical target does not force a historical return clip to bind internally. The accepted corrected Y/K, combined with `mt*alpha`, implies an rk level that already leaves 30/31 provinces above `.09` after the fixed depreciation offset.
2. **What mainly causes the upper pressure?** Corrected empirical Y/K relative to the historical bound is primary. Recovered mt modestly amplifies it; profit/K is negligible at turn 25; depreciation subtracts `.025` and therefore cannot cause the pressure.
3. **Are `.02/.09` economically identified?** No. They are classified `EMPIRICAL_NUMERICAL_SAFEGUARD` from their source role and lack of a documented empirical rate/period mapping.
4. **Is widening or removing the clips justified?** `INSUFFICIENT_EVIDENCE`. No economically identified replacement interval or period convention is available.
5. **Can a firm-price/household-wage numeraire mismatch contaminate returns indirectly?** There is evidence of unresolved unit and aggregation comparability, so indirect contamination is possible through future household labor/assets and firm Y, K and mt. It is not demonstrated causally here, and wage does not enter the saved-row ra0 equation directly.
6. **Should normalized labor be activated first?** No. Price/return and wage-numeraire identification should remain the next gate; normalized labor stays inactive to avoid confounding channels.
7. **What is the lowest-risk next scientific experiment?** After Owner approval of one pre-registered unit-consistent normalization object, run one initialization-only price receipt on frozen C1 inputs, with no outer trajectory and no post-observation tuning. This report does not authorize or publish it.
