# Chapter 5 MP4C initial private-K observation and residual-GovInv probe

Date: 2026-09-11

Builder verdict:

`INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_PASS__ONE_PASS_PRIVATE_K_OBSERVED_AND_RESIDUAL_INITIALIZATION_ACCOUNTING_VALIDATED`

## Scope and authority

Live `origin/main` at task start was `67172ba4cc761cdbbe2716dccc85b78c88b408e3`. The probe used the accepted corrected-2018 Track-A contract: actual 2018 GDP/population, raw-NBS GFCF Track-A PIM capital, `delta_pim=.096`, `alpha=.7380939146868483`, MU=`10万元`, NU=`100 persons`, same-year `Zt0`, accepted fixed initial household prices/states, and firm depreciation `.025` kept separate.

The 31/31 pre-science validator and 26 focused tests passed before `science_started.json` was created. Exactly one scientific process then performed one household-initialization observation per province and one full-batch At-only capital allocation. It did not update or call migration, normalized migration, firm, wage, GovInv controller, outer turn, or steady state.

## One-pass household observation

Numerically usable `At`, `Bt`, `Lt`, and `Ct` were obtained for 31/31 provinces. HJB converged for 20 provinces. Eleven finite, structurally usable nonconverged returns were preserved as `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`: 安徽、江西、河南、湖北、湖南、广东、广西、重庆、四川、贵州、甘肃. Each used the 100-iteration ceiling; statistics are in the province ledger.

All 31 KFE returns were `DIAGNOSTIC_ONLY`. The source-free normwise residual ratio had min/median/max `4.381760389060762e-15 / 0.11827278550097817 / 0.1460882751544755`; upper-b maximum outward-leak rate had min/median/max `0.007759133731191779 / 4.15295658116238 / 4.684902940472038`. Thus all private-K observations remain diagnostic-only even where HJB converged. Numerical availability is not household scientific acceptance.

## Private K and G0/G1 accounting

With the frozen diagnostic bridge `beta_a=1`, private-K/Track-A-target min/median/mean/max was:

`0.0009496604680542149 / 0.003209990990658578 / 0.005053897862873359 / 0.03486516202709419`.

The minimum was 山东 and the maximum 西藏. National private K was `6,633,077.122860028 MU` against national target `2,481,992,906.900551 MU`.

Under G0 (`GovInv0=Ktarget`), total-K/target min/median/mean/max was:

`1.0009496604680541 / 1.0032099909906587 / 1.0050538978628734 / 1.034865162027094`.

National G0 accounting capital was `2,488,625,984.0234103 MU`; the mechanical overshoot was exactly the initial private-K total.

Under G1 (`GovInv0=max(Ktarget-private K,0)`), private K was below target in all 31 provinces. No residual was clipped to zero. Consequently province G1 total-K/target min/median/mean/max was exactly `1/1/1/1`, national G1 accounting capital equaled the target, and the maximum accounting identity error was `0`.

This is an initialization accounting result only. It does not show that the historical return-bound controller is solved or should be changed.

## Bridge sensitivity

The existing allocation is homogeneous in the bridge scalar:

`Kt_supply_initial(beta_a) = beta_a * Kt_supply_initial(beta_a=1)`.

This was verified from the linear At-times-N contribution and exclusion/average formula without a second allocation or beta cell. Province `beta_a_star=Ktarget/K_private(beta=1)` min/median/mean/max was:

`28.681926079187193 / 311.5273540985344 / 380.5993931756444 / 1053.007926136935`.

The first residual-zero threshold is 西藏 and the largest is 山东. At beta=1 all provinces are well below their threshold; as an unidentified beta approaches a province threshold, G1 residual GovInv approaches zero, and above it private-capital overshoot remains. These thresholds diagnose sensitivity but do not identify beta.

## Anhui trace

Accepted initial values were `Y0=34,010,900`, `N0=607,600`, `Ktarget=70,182,433.35888097`, `alpha=.7380939146868483`, and `Zt0=1.681124916844091`. Fixed inputs included `rah=.08895777765800762`, `rb=.02`, `w=18.29792118969518`, `wjt=1.3`, `ra=.09`, `tau=.05`, and `Tt=.1`.

Anhui HJB returned `converged=false`, 100 iterations, statistic `0.18862667495966345`, and was continued as diagnostic-only; KFE was also diagnostic-only. Aggregates were `At=8.633994914935972`, `Bt=-1.7331237220247262`, `Lt=.6370528935500427`, and `Ct=11.708814550329276`.

Its initial private K was `218,901.27196706057 MU`, or `.0031190322348571085` of target. G0 used GovInv `70,182,433.35888097` and total K `70,401,334.63084802` (ratio `1.003119032234857`). G1 used residual GovInv `69,963,532.08691391` and total K exactly `70,182,433.35888097` (ratio `1`). Anhui `beta_a_star=320.6122683902986`.

## Required interpretations

1. One-pass private K is numerically available for 31/31 provinces.
2. All 31 observations are scientific `DIAGNOSTIC_ONLY`: 11 retain HJB nonconvergence, all 31 retain KFE source-free stationarity/boundary blockers, and beta=1 remains an unidentified diagnostic bridge.
3. Initial private K is small relative to target under beta=1, with median ratio about `.00321` and maximum about `.03487`.
4. G1 removes the mechanical `Ktarget+private K` initialization overshoot for every province where private K is below target; that is all 31 here.
5. No province has private K at or above target under beta=1.
6. G1 is bridge-sensitive according to the reported beta-star distribution; beta-star is geometry, not calibration.
7. The evidence is sufficient to propose a separately reviewed **diagnostic successor initialization route** using G1 while keeping beta=1 explicitly diagnostic-only. It is not sufficient for production, trajectory, or Results authority.
8. This initialization probe gives no reason to redesign `HANK_mp_1eq.m` controller now. Initialization and controller behavior remain separate scientific questions.

## Calls and boundaries

The single process completed 31/31 household observations, 31 HJB returns (`1,596` direct solves), 31 KFE returns (`31` direct solves), 31 aggregates, `24,800` labor-root/Brent calls, and exactly one At-only allocation in `221.21899999999732` seconds. Scientific retries, engineering retries, second household passes, beta cells, migration, normalized migration, firm, wage, controller, outer-turn, steady-state, MATLAB, GE, annual, IRF, and Results calls were all zero.

Post-science finalization corrected one documentary column label without rerunning science: `At_times_N_beta1_preallocation` now stores raw `At*N`, while the allocation's ratio-weighted contribution is retained separately as `inter_province_productive_contribution_beta1`. The executed and final harness hashes are both recorded.

Production GovInv remains unchanged. `Results eligibility=FALSE`.
