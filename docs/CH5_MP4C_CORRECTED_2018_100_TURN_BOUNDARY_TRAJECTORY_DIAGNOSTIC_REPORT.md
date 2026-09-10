# Chapter 5 corrected-2018 source-faithful 100-turn boundary trajectory diagnostic

## Verdict

`CORRECTED_2018_100TURN_DIAGNOSTIC_FAIL__BOUNDARY_HITS_PERSIST_OR_OSCILLATE`

Exactly one trajectory was launched. It completed 100 outer turns and
3100 province updates, stopping because
`AUTHORIZED_100_TURN_CEILING`. No second trajectory or scientific retry was used.

## Direct answers

1. Firm-rate hits do not decline: all 31 provinces are on the lower bound in every turn, including turns 50 and 100. Classification: `BOUNDARY_HITS_PERSIST_HIGH`.
2. Wage hits fall only from 27 at turn 1 to 21 by turn 8, then stay at 21 through turns 50 and 100 (14 lower, 7 upper, 10 interior). Classification: `BOUNDARY_HITS_PERSIST_HIGH`; unresolved absolute wage normalization remains a blocker.
3. Every province is a 100-turn firm-rate lower-bound offender. Eleven wage offenders remain on the same bound for all 100 turns (upper: 四川、山东、广东、江苏、河南、浙江; lower: 宁夏、海南、甘肃、西藏、青海); another nine remain lower-bound offenders for turns 5–100, and 湖北 remains upper-bound for turns 6–100.
4. The controller does not materially move the system into the admissible price region. It opens in 49 turns, generating 1,519 Zt adjustments and 1,519 GovInv decreases (zero increases); 47/49 active turns have zero next-turn change in total boundary hits and only two have a one-hit wage reduction. Firm-rate hits never change.
5. The KN/Y/GDP path is `OSCILLATORY`, not convergent: late max KN gap alternates near 0.0514 and 0.1191, while max Y/Y0 gap remains near 0.0782. Small adjacent-turn Y changes do not imply return to the GDP target.
6. The corrected-data path reproduces the Anhui turn2→turn3 asset collapse: A+B 11.978258156033768 → 1.8919618910437164, ratio 0.1579496673387929.
7. The collapse coincides with entering household rah falling 0.0829892058879816 → 0.0184420457528848. Used firm ra stays at 0.02; raw wage moves 2.137336530692252 → 2.205170377619017. GovInv and Zt are unchanged through turn 3, so their first turn-4 controller adjustment follows rather than precedes the collapse.
8. Economic acceptance remains blocked: all 3,100 KFE densities are `DIAGNOSTIC_ONLY`; upper-b leakage is 620 cells per turn from turn 3 through turn 100, and turn-100 max source-free normwise residual ratio is 6.280821269179423e-05. All 31 turn-100 HJB-loop operators are `DIAGNOSTIC_ONLY`, totaling 589 negative offdiagonals (minimum -2.3166728047240652).

## Selected Anhui trace

| turn | raw ra | used ra | raw wage | used wage | entering rah | A+B | GovInv | Zt | KN gap | GDP gap | KFE | HJB operator |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | -0.024969971131121638 | 0.02 | 2.5721358283733027 | 1.3 | 0.089999999999999997 | 11.972375335433068 | 1357314108201.3684 | 0.00069346444958586786 | 98575.170524477158 | 0.58293108760932122 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |
| 2 | -0.024968505109415375 | 0.02 | 2.1373365306922518 | 1.3 | 0.082989205887981601 | 11.978258156033768 | 1357314108201.3684 | 0.00069346444958586786 | 0.34756612158493083 | 0.66121362424745667 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |
| 3 | -0.024968792977977675 | 0.02 | 2.2051703776190168 | 1.3 | 0.0184420457528848 | 1.8919618910437164 | 1357314108201.3684 | 0.00069346444958586786 | 0.16103719246632298 | 0.64602949365242157 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |
| 5 | -0.024980666186283199 | 0.02 | 1.0474070450803297 | 1.0474070450803297 | 0.0184420457528848 | 1.8926686768743746 | 1221582697381.2317 | 0.00042162572596183342 | 0.078644241095566558 | 0.07813474874750892 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |
| 10 | -0.024973361571986711 | 0.02 | 1.1912454427721118 | 1.1912454427721118 | 0.0184420457528848 | 1.8773574584300687 | 890533786390.91797 | 0.00053372622091209286 | 0.12082678883258835 | 0.078101162717580941 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |
| 25 | -0.02494430928972963 | 0.02 | 1.1931567335911546 | 1.1931567335911546 | 0.0184420457528848 | 1.8772913658676487 | 425939549376.03833 | 0.00094370515585945228 | 0.051195335842845857 | 0.078202375403595425 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |
| 50 | -0.024780909579088125 | 0.02 | 1.1911318041853434 | 1.1911318041853434 | 0.0184420457528848 | 1.8773668463045072 | 108268118549.28049 | 0.0027200298318496054 | 0.11913087887412266 | 0.078174704439285758 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |
| 75 | -0.024224249800689834 | 0.02 | 1.1933252021792422 | 1.1933252021792422 | 0.0184420457528848 | 1.8772985043012749 | 30578114537.543247 | 0.0072268044295912817 | 0.051195715008434672 | 0.078202252487491797 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |
| 100 | -0.021948121327818301 | 0.02 | 1.1917273574152731 | 1.1917273574152731 | 0.0184420457528848 | 1.8773950742094523 | 7772546443.7711411 | 0.020829656789424007 | 0.11913286643236376 | 0.07817435060961786 | DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |

## HJB-loop operator correction

The first derived ledger had inspected the KFE-input post-convergence operator. A zero-solve readback of the separately saved HJB-loop `operator` corrected that label. Turn 1/100 national negative offdiagonals are 651/589; diagnostic-only provinces are 31/31. The post-convergence operator has zero negative offdiagonals in both turns. This correction changes no scientific state, solve, boundary verdict, or call count.

## Evidence and reproducibility

- Start authority: fresh live `origin/main=3e1ac9ba70c91d2aa145852e185779ba6e0721ac`.
- Canonical workbook SHA-256: `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`.
- Evidence root: `D:\ProjectTemp\ch5-corrected-2018-100turn-boundary-trajectory-20260910-002`.
- External final manifest SHA-256: `0B5633270720E9E843C609AC9B09A356FEFD958CFB1F04DF7077FA06F844E438`; readback: 19,216/19,216.
- Focused/static tests: 20/20 before science and 20/20 after science; `git diff --check` passed.
- One engineering retry occurred before any scientific state advanced: the inherited predecessor SHA constants were stale against fresh live main. The occupied `...-001` root was preserved, had no `science_started.json`, and was not reused. Scientific retries remain zero.
- Source final predicate was never satisfied; the run stopped only at the authorized 100-turn ceiling.

## Calls and protected boundary

Scientific processes/trajectories: 1/1.
HJB/KFE direct solves: 36017/3100.
Labor roots/Brent calls: 2480000/2480000.
Scientific retries: 0. MATLAB/GE/annual/IRF/Results calls:
0/0/0/0/0.

This diagnostic does not establish production steady state, KFE/HJB admissibility,
GE/annual validity, or Results readiness. Turn 101+ authorized: **NO**. Results eligibility: **FALSE**.
