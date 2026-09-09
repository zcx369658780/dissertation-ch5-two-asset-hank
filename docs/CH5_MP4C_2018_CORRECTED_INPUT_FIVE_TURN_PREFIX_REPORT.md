# Chapter 5 corrected-2018 five-turn bounded prefix

## Verdict

`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER__KFE_OR_DISTRIBUTION_VALIDITY`

One fresh trajectory completed exactly five turns. Accepted turns 1-3 reproduced exactly before turn 4 was entered. KFE return is not treated as distribution validity.

## Anhui turns 1-5

| turn | rah | raw ra0 | used ra | raw wage | used wage | HJB iter | C | L | A | B | A+B | nk_gap | yt_gap |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.089999999999999997 | -0.024969971131121638 | 0.02 | 2.5721358283733027 | 1.3 | 64 | 11.400731651949162 | 0.64762359811410397 | 7.2740978684863942 | 4.6982774669466725 | 11.972375335433068 | 98575.170524477158 | 0.58293108760932122 |
| 2 | 0.082989205887981601 | -0.024968505109415375 | 0.02 | 2.1373365306922518 | 1.3 | 31 | 10.151127654132669 | 0.66825904339971121 | 7.293035015032082 | 4.6852231410016856 | 11.978258156033768 | 0.34756612158493083 | 0.049454165914679438 |
| 3 | 0.0184420457528848 | -0.024968792977977675 | 0.02 | 2.2051703776190168 | 1.3 | 11 | 11.26469278859272 | 0.69879328575964927 | 0.013287859137578914 | 1.8786740319061375 | 1.8919618910437164 | 0.16103719246632298 | 0.0091403840983508289 |
| 4 | 0.0184420457528848 | -0.024968817436572574 | 0.02 | 2.2110613834748234 | 1.3 | 11 | 11.361297328122625 | 0.69779743808448624 | 0.013372100749846821 | 1.8793796060847558 | 1.8927517068346027 | 0.062400400123944655 | 0.00078375225059112985 |
| 5 | 0.0184420457528848 | -0.024980666186283199 | 0.02 | 1.0474070450803297 | 1.0474070450803297 | 11 | 11.350967796388458 | 0.69790344964960438 | 0.013363133742819647 | 1.8793055431315548 | 1.8926686768743746 | 0.078644241095566558 | 0.4395068038016402 |

## KFE and asset diagnostics

Turn 4 KFE classifications: `{'DIAGNOSTIC_ONLY': 31}`. Turn 5: `{'DIAGNOSTIC_ONLY': 31}`. Full diagnostics include normalized mass, signed density, contaminated-row and source-free residual numerators/scales/ratios, four boundary outward-leak faces, and upper-b face mass. No additional KFE solve was performed.

Anhui turn-3 asset collapse is retained without smoothing. Turn4/5 violent A+B ratio signals under the declared diagnostic rule: `0` nationally.

## National turn 5

- rate lower/interior/upper: 31/0/0
- wage lower/interior/upper: 18/7/6
- rah min/median/max: 0.014542152579213808/0.0184420457528848/0.02
- max nk_gap: 0.080731791038562983
- adaptation gate open: true
- Zt adjustments: 31; GovInv actions: {'LOW_RA_DECREASE_0P9': 31}

## Calls and boundary

Canonical SHA-256: `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`. Scientific process/trajectory: 1/1; completed turns/province updates: 5/155; HJB/KFE direct solves: 3622/155; labor roots/Brent calls: 124000/124000; scientific retries: 0. MATLAB/GE/annual/IRF/Results/turn6+ calls: 0.

This bounded prefix does not prove steady-state convergence, global admissibility, GE or annual validity, or Results readiness. Turn 6+ authorized: **NO**. Steady state authorized: **NO**. Results eligibility: **FALSE**.
