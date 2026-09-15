# CH5 MP4C K1 — J160 first-turn local-basin interpolation diagnostic

## Panel terminal class

`LOCAL_BASIN_EVIDENCE_NUMERICALLY_BLOCKED`

Results eligibility=`FALSE`.

## Frozen authority

The four preregistered accepted failure/success pairs passed exact non-`(ra,w)` household-input equality. No endpoint HJB was rerun. All twelve synthetic probes used fresh source-style initialization on `I=20,J=160,Nz=2`, `a=[0,100]`, `b=[-2,20]`, `Delta=1000`, tolerance `1e-7`, maxit `100`, and A2max gate `0.01`.

## Probe outcomes

| pair | t | synthetic ra | synthetic composite w | HJB | iterations | final max abs dV | mixed observer max* | mechanism if nonconverged |
|---|---:|---:|---:|---|---:|---:|---:|---|
| 山西→河北 | 0.25 | 0.086428830600402934 | 18.182765068872058 | HJB_CONVERGED | 34 | 3.973426387915424e-08 | 1.444122138735141 | None |
| 山西→河北 | 0.50 | 0.086421897255665597 | 18.162431075700084 | HJB_CONVERGED | 39 | 5.206770570254093e-10 | 1.445239816033525 | None |
| 山西→河北 | 0.75 | 0.086414963910928247 | 18.142097082528107 | HJB_CONVERGED | 37 | 5.496455734999017e-09 | 1.4463586870987075 | None |
| 重庆→河北 | 0.25 | 0.08604864759581432 | 18.08335240564401 | HJB_CONVERGED | 46 | 2.463109716188683e-10 | 1.4007563571056902 | None |
| 重庆→河北 | 0.50 | 0.086168441919273198 | 18.096155966881383 | HJB_CONVERGED | 57 | 4.538547315746655e-11 | 1.4163183045556078 | None |
| 重庆→河北 | 0.75 | 0.086288236242732047 | 18.108959528118756 | HJB_CONVERGED | 30 | 7.401489643399373e-09 | 1.4318924576916638 | None |
| 江西→安徽 | 0.25 | 0.089079147840043185 | 18.124234435512243 | HJB_NOT_CONVERGED | 100 | 3.334187371994979e-05 | 1.836125668754488 | DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING |
| 江西→安徽 | 0.50 | 0.089038691112697993 | 18.182130020239889 | HJB_CONVERGED | 77 | 7.148407288326553e-08 | 1.8232323604877452 | None |
| 江西→安徽 | 0.75 | 0.088998234385352815 | 18.240025604967535 | HJB_CONVERGED | 71 | 1.389738724100198e-08 | 1.8103670593479084 | None |
| 贵州→四川 | 0.25 | 0.089608234753035143 | 17.533087904411527 | HJB_CONVERGED | 80 | 2.693021361466208e-10 | 1.9869461202237166 | None |
| 贵州→四川 | 0.50 | 0.089426241920948418 | 17.594503654416251 | HJB_NOT_CONVERGED | 100 | 0.00019476215275160413 | 1.9518944809619476 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION |
| 贵州→四川 | 0.75 | 0.089244249088861693 | 17.65591940442097 | HJB_CONVERGED | 56 | 4.3791636983314675e-11 | 1.916941624405155 | None |

## Pair topology

- 山西→河北: `t=0:F → t=0.25:C → t=0.5:C → t=0.75:C → t=1:C`; `PAIR_NUMERICAL_INVALIDITY_BLOCKER`.
- 重庆→河北: `t=0:F → t=0.25:C → t=0.5:C → t=0.75:C → t=1:C`; `PAIR_NUMERICAL_INVALIDITY_BLOCKER`.
- 江西→安徽: `t=0:F → t=0.25:F → t=0.5:C → t=0.75:C → t=1:C`; `PAIR_NUMERICAL_INVALIDITY_BLOCKER`.
- 贵州→四川: `t=0:F → t=0.25:C → t=0.5:F → t=0.75:C → t=1:C`; `PAIR_NUMERICAL_INVALIDITY_BLOCKER`.

## Receipt blocker

`SCIENTIFIC_A2MAX_EXACT_RECEIPT_UNAVAILABLE`. The first implementation incorrectly pooled the post-convergence implicit system matrix with source-generator A2max observations. In all 12 receipts the sole recorded illegal event is at `iterations+1`, so all scientific iteration operators are proven legal; however, their exact maximum A2max was not retained. The mixed values in the table (about 1–2) belong to the post-convergence system matrix and are not scientific generator A2max values.

Because the exact required maximum receipt cannot be reconstructed without another HJB call, all four pair decisions are fail-closed as `PAIR_NUMERICAL_INVALIDITY_BLOCKER`; no rerun or scientific retry was performed.


## Interpretation boundary

These interpolated points are numerical probes only. They are not feasible provincial equilibria, calibrated states, upstream mapping outputs, or counterfactuals. The panel does not identify causality or authorize a threshold, clipping rule, recalibration, mapping/guard/HJB change, or Results use.

HJB started/completed/hard-error=`12/12/0`; KFE=`0`; endpoint HJB reruns=`0`; scientific retries=`0`; engineering retries=`0`.

No outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results route ran.

## Exactly one next gate

`REVIEWER_J160_LOCAL_BASIN_INTERPOLATION_ROUTE_DECISION`
