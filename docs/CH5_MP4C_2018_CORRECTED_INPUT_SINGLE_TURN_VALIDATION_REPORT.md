# Chapter 5 MP4C corrected-2018 single-turn validation report

## Verdict

`CORRECTED_2018_SINGLE_TURN_PASS__FULL_ORDERED_TURN_COMPLETED`

The accepted canonical workbook SHA-256 is `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`. The validator bound all 31 provinces in the frozen source order under `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT` and completed exactly one ordered turn. Downstream steady-state execution is **not authorized**. Results eligibility remains **FALSE**.

## Corrected runtime input

The runtime used 2018 analysis/data_MAT index 10, level row 19, PLM vintage 19, rolling window 2009–2018, and same-year 2018 Zt. Anhui stayed at Python index 11 / MATLAB index 12 / Excel N. Its bound inputs were GDP `34010900.0`, POP `607600.0`, PIM CAP `1357314108201.3684`, alpha `0.772866243094144`, Zt `0.0006934644495858679`, and GovInv `1357314108201.3684`. The grid remained I20 b[-2,5], J20 a[0,10], Nz2 z[0.8,1.3].

The private canonical workbook was read only and was not copied into Git. The distance matrix retained SHA-256 `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566` and the existing destination-by-origin normalization.

## Household and one-turn result

All 31 native initializations returned. Each used 800 labor roots. All 31 HJB calls converged in 64 updates, for 1,984 HJB direct solves total; every HJB result was saved before its KFE call. All 31 KFE direct solves and aggregates returned. The one-turn output contains finite JSON-serializable observables for all provinces.

Anhui's household input was rah `0.09`, rb `0.02`, composite wage `20.0`, and entering Lt_prev `607600.0`. Its HJB converged in `64` updates with statistic `3.5073277615538245e-11`; KFE returned. Household aggregates were C `11.400731651949162`, L `0.647623598114104`, A `7.274097868486394`, B `4.6982774669466725`, A+B `11.972375335433068`.

## Anhui firm forensic

After correcting the time/data input, Anhui first-turn raw return was `-0.02496997113112164`. It did **not** hit the upper bound 0.09; it fell below the lower bound and the used rate was clipped to `0.02`. Raw wage was `2.5721358283733027` and the used wage was clipped to the upper bound `1.3`. The household still entered this first turn with carried rah `0.09`.

Across all provinces, firm rates hit the lower boundary in `31` cases and the upper boundary in `0` cases. Wages hit the lower/upper boundaries in `5` / `22` cases. Maximum nk_gap was `204296.40029802968` at `山东`. Because this exceeded the 0.1 adaptation gate, the existing controller recorded no Zt or GovInv adjustment in this turn. This one-turn PASS does not establish stationary convergence or household/KFE global admissibility.

## Saved old mixed-year comparison

This is `DESCRIPTIVE_INPUT_CORRECTION_EFFECT_ONLY`; the old model was not rerun. For Anhui, saved old versus corrected values were: GDP `34010910.0` to `34010900.0`, POP `438530.0` to `607600.0`, CAP `54313245.2543264` to `1357314108201.3684`, Zt `0.000641551386937363` to `0.0006934644495858679`, firm ra0 `-0.024756723746024084` to `-0.02496997113112164`, and raw wage `0.0014794593428676367` to `2.5721358283733027`. Alpha and carried rah remained `0.772866243094144` and `0.09`.

## Call ledger and checks

One scientific Python process ran for `294.1720000000205` seconds with zero scientific retries. Counts were: one-turn 1/1 attempted/returned; province updates 31/31; household 31/31 returned and 0 failed; HJB 31 calls / 1,984 direct solves; KFE 31 calls / 31 direct solves; firm 31/31; wage batch 1 with 31 outputs; controller 1. MATLAB, second turn, steady-state loop, GE, annual model, IRF, and Results calls were all 0.

Focused static and one-turn component checks passed `15` tests. Full machine-readable evidence and per-province records are in `reports/mp4c_2018_corrected_single_turn_20260909/` and the external evidence root `D:\ProjectTemp\ch5-corrected-2018-single-turn-20260909-001`.
