# Chapter 5 corrected-2018 two-turn propagation validation

## Verdict

`CORRECTED_2018_TWO_TURN_PASS__TURN2_PROPAGATION_OBSERVED`

The fresh corrected-2018 trajectory completed exactly two turns in the frozen 31-province source order. Fresh turn 1 reproduced every accepted observable and controller field exactly (`mismatch_count=0`), so turn 2 was entered. This is a bounded propagation observation, not steady-state or convergence evidence. Third turn authorized: **NO**. Steady state authorized: **NO**. Results eligibility: **FALSE**.

## Central propagation finding

For Anhui (Python 11 / MATLAB 12 / Excel N), turn-2 household `rah` was `0.082989205887981601`. It was produced by the native pre-firm capital-allocation rule

`(1-ratio_i)*old_ra_i + ratio_i*(sum_j(ratio_j*old_ra_j)-ratio_i*old_ra_i)/(n-1)`.

The source vector was the turn-1 **entering** `ra` vector (SHA-256 `FAF59BC7EC664D07D0385426AB9F11E77C446683503E56901C0DE980ACA73745`), whose Anhui value was `0.09`. Therefore turn-1 firm used `ra=0.02` did not directly become turn-2 household `rah`. It did become turn-2 entering firm state `ra=0.02`; the capital block reads that state when constructing the next post-turn `rah`, which would concern turn 3 and was not executed.

## Anhui turn 1 to turn 2

| observable | turn 1 | turn 2 |
|---|---:|---:|
| household rah | 0.089999999999999997 | 0.082989205887981601 |
| household composite wage | 20 | 17.14928118359844 |
| firm raw ra0 | -0.024969971131121638 | -0.024968505109415375 |
| firm used ra | 0.02 | 0.02 |
| firm raw wage | 2.5721358283733027 | 2.1373365306922518 |
| firm used wage | 1.3 | 1.3 |
| HJB iterations | 64 | 31 |
| HJB statistic | 3.5073277615538245e-11 | 1.3493204331638253e-09 |
| KFE returned | True | True |
| C | 11.400731651949162 | 10.151127654132669 |
| L | 0.64762359811410397 | 0.66825904339971121 |
| A | 7.2740978684863942 | 7.293035015032082 |
| B | 4.6982774669466725 | 4.6852231410016856 |
| nk_gap | 98575.170524477158 | 0.34756612158493083 |
| yt_gap | 0.58293108760932122 | 0.049454165914679438 |

Turn-2 raw `ra0` remained below the 0.02 lower bound and used `ra` remained clipped to 0.02. Raw wage decreased from `2.5721358283733027` to `2.1373365306922518`, but both exceeded 1.3 and were clipped at the upper wage bound. HJB and KFE returned in both turns. The adaptation gate remained closed because the national maximum `nk_gap` was `0.45946738761290562`, above 0.1; no Zt or GovInv action occurred.

## National transition

| diagnostic | turn 1 | turn 2 |
|---|---:|---:|
| firm rate lower/interior/upper | 31/0/0 | 31/0/0 |
| wage lower/interior/upper | 5/4/22 | 5/8/18 |
| raw ra0 min/median/max | -0.0249780865 / -0.024967168 / -0.0248934011 | -0.0249770432 / -0.0249656356 / -0.0248877545 |
| nk_gap min/median/max | 5815.69305 / 62629.152 / 204296.4 | 0.305434685 / 0.348015784 / 0.459467388 |
| yt_gap min/median/max | 0.365657936 / 0.745250684 / 1.98867578 | 0.0306070579 / 0.0493749065 / 0.0570514745 |
| HJB failures / KFE failures | 0 / 0 | 0 / 0 |
| Zt adjustments / GovInv non-NONE | 0 / 0 | 0 / 0 |

Turn 1 had 31 HJB returns at 64 iterations. Turn 2 iterations ranged from 13 to 41; the full distribution is saved in `transition_summary.json`. These two observations do not establish convergence.

## Input and calls

Canonical workbook SHA-256: `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`. The private workbook was read only and was not copied into Git. The corrected 2018 temporal contract, grids, model equations, solvers and tolerances were unchanged.

The single scientific process took `369.797` seconds. It executed 2 turns and 62 province updates: 62 household calls, 62 native initializations, 49600 labor-root attempts and 49600 Brent calls, 62 HJB calls with 2599 direct solves, 62 KFE calls with 62 direct solves, 62 aggregates, 62 firm calls, 2 wage batches, 2 migration calls, 2 capital allocations and 2 controller evaluations. All 62 household/HJB/KFE/firm calls returned; retries were 0. MATLAB, GE, annual model, IRF and Results calls were 0.
