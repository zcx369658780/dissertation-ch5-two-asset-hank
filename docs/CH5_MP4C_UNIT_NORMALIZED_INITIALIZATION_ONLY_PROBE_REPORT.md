# Chapter 5 MP4C unit-normalized initialization-only probe report

Date: 2026-09-10

Base `origin/main`: `e8f086e37524d80797307854378d2149f18c7d6f`

Verdict: `UNIT_NORMALIZED_INITIALIZATION_PROBE_PASS__DATA_CONSISTENT_PRICE_RECEIPT_COMPLETE`

## Scope and authority

This was the bounded initialization-only diagnostic authorized by `tasks/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_AND_PRICE_RECEIPT.md`. It used actual 2018 GDP and population, raw-NBS GFCF Track-A PIM capital (`delta_pim=.096`), `alpha=.7380939146868483`, and the frozen common units `MU=10万元`, `NU=100 persons`. The helper evaluated protected source equations statically; it did not call MATLAB or any household, HJB, KFE, firm function, wage function, allocation function, controller, root solver, or outer-loop entry point.

## Source-equation finding

The protected `HANK_firm.m:35` retains the old state `rk=.1` in the zero-change NKPC expression. With `pit=pit_1=.02`, `theta=100`, `epsilon=10`, and `mstar=.9`, the source-faithful initialization is therefore `mt0=.92`. This differs from the accepted redesign prose simplification `mt0=.9`. The probe followed the protected executable equation and recorded the discrepancy; no production source or parameter was changed.

For every province the receipt sets `Yt=Yt_1=Y0`, `Kt=Kt_1=K0`, `Lt=Lt_1=N0`, and `Zt=Zt_1=Zt0`. It evaluates `HANK_firm.m:30,33-35,43-54`, then applies the unchanged return and wage bounds plus both corporate-tax compensation steps at `HANK_firm.m:55-74`.

## National receipt

- Raw firm return classification at `[.02,.09]`: below `0`, inside `1`, above `30`. Qinghai is the sole inside observation (`0.08818883738518214`). Raw return min/median/max is `0.08818883738518214 / 0.2080531919891984 / 0.38321987070028335`; used return min/median/max is `0.08818883738518214 / 0.09 / 0.09`.
- Raw firm wage classification at `[.8,1.3]`: below `0`, inside `0`, above `31`. Raw wage min/median/max is `7.7642626541050035 / 12.423284914909623 / 36.39146820961234`; all used wages equal `1.3`.
- All 31 provinces hit at least one price boundary. Corrected units and data-consistent firm initialization therefore do not remove the broad clipping-boundary start.
- Beijing has the largest absolute raw discrepancy from both legacy `ra=.09` and legacy `wjt=.6`; its raw values are `0.38321987070028335` and `36.39146820961234`.
- K/Y ranges from Beijing `1.7736677057631476` to Qinghai `6.396800411050845`. K/N ranges from Gansu `100.11015777092373 MU/NU` to Tianjin `467.05422070207686 MU/NU`.

## Anhui receipt

Anhui binds `Y0=34,010,900 MU`, `N0=L0=607,600 NU`, and Track-A `K0=70,182,433.35888097 MU`, giving `K/Y=2.06352767374227`, `K/N=115.50762567294431`, and source-faithful `Zt0`. Its raw/used firm return is `0.32587797015041736 / 0.09`; raw/used firm wage is `13.487571992789512 / 1.3`. The fully static source-lagged return composite is `rah0=0.08895777765800762`, and the static distance/migration wage composite is `w0=18.29792118969518`. Both are labeled `INITIAL_COMPOSITE_NO_DAMPING_BASE`.

Across provinces, `rah0` min/median/max is `0.06490365475420734 / 0.08488059053640952 / 0.09`; `w0` min/median/max is `13.837477514705718 / 17.874582154052934 / 18.519697907284154`. These are initialization receipts, not household equilibria or convergence evidence.

## Asset bridge diagnostic

The legacy `At=2` was used only to compute `AtN_baseline=2*N0_NU` and its scale relative to `K0` and the historical `GovInv0=K0` reference. Every row is marked `SOURCE_FAITHFUL_BASELINE_ONLY` and `NO_REPLACEMENT_BRIDGE_SELECTED`. The ratios do not select, calibrate, or justify a production asset bridge.

## Calls, verification, and boundary

Across the complete task session, four deterministic helper processes evaluated 124 firm-equation rows, 124 return-composite rows, and 124 wage-composite rows. The first three evidence roots (`-001` through `-003`) are preserved preliminary packaging/order/readback runs; `-004` is the final evidence root. Five focused-test processes executed 30 test cases in total, two Python compile-check processes ran, and four evidence-finalization processes ran. MATLAB, household/HJB/KFE/control, `Lt_seperate`, root/Newton/Broyden/fsolve/Brent/Anderson, outer turns, steady state, GE, annual, IRF, Results, and parameter tuning were all zero. Focused tests and a post-read protected-source hash check passed; the finite manifest independently reopened every listed artifact.

`Results eligibility=FALSE`. This PASS does not authorize a household solve, a first full outer turn, steady state, damping/hysteresis/GovInv redesign, a production asset-bridge choice, Results, merge to main, or a successor scientific task. The next gate is independent ChatGPT Reviewer ACCEPT/REJECT of the dedicated commit.
