# CH5 MP4C K1 — J160 local-basin A2max receipt repair and controlled reexecution

## Panel terminal class

`LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`

Results eligibility=`FALSE`.

## Receipt repair and invariance

Scientific A2max now contains only source-generator observations from actual HJB iterations. Sequence length is checked against the returned scientific iteration count. The post-convergence implicit system matrix is separately retained as `NOT_SCIENTIFIC_A2MAX / EXCLUDED_FROM_LEGALITY`. Accepted observer invariance and focused deterministic tests passed; no parity HJB call was added.

## Exact probe receipts

| pair | t | HJB | iterations | final max abs dV | max scientific A2max | argmax iter | first illegal | legal | reproducible |
|---|---:|---|---:|---:|---:|---:|---:|---|---|
| 山西→河北 | 0.25 | HJB_CONVERGED | 34 | 3.973426387915424e-08 | 0.002492695895366548 | 7 | None | True | True |
| 山西→河北 | 0.50 | HJB_CONVERGED | 39 | 5.206770570254093e-10 | 0.0024922138437061814 | 14 | None | True | True |
| 山西→河北 | 0.75 | HJB_CONVERGED | 37 | 5.496455734999017e-09 | 0.0024917316834282555 | 14 | None | True | True |
| 重庆→河北 | 0.25 | HJB_CONVERGED | 46 | 2.463109716188683e-10 | 0.0024704178143001854 | 9 | None | True | True |
| 重庆→河北 | 0.50 | HJB_CONVERGED | 57 | 4.538547315746655e-11 | 0.0024773518890932045 | 7 | None | True | True |
| 重庆→河北 | 0.75 | HJB_CONVERGED | 30 | 7.401489643399373e-09 | 0.0024842957556300838 | 13 | None | True | True |
| 江西→安徽 | 0.25 | HJB_NOT_CONVERGED | 100 | 3.334187371994979e-05 | 0.0026476377728827383 | 4 | None | True | True |
| 江西→安徽 | 0.50 | HJB_CONVERGED | 77 | 7.148407288326553e-08 | 0.002645482769450147 | 4 | None | True | True |
| 江西→安徽 | 0.75 | HJB_CONVERGED | 71 | 1.389738724100198e-08 | 0.0026433269692822114 | 14 | None | True | True |
| 贵州→四川 | 0.25 | HJB_CONVERGED | 80 | 2.693021361466208e-10 | 0.002676515867511886 | 8 | None | True | True |
| 贵州→四川 | 0.50 | HJB_NOT_CONVERGED | 100 | 0.00019476215275160413 | 0.0026659397516066163 | 13 | None | True | True |
| 贵州→四川 | 0.75 | HJB_CONVERGED | 56 | 4.3791636983314675e-11 | 0.0026553816079026293 | 10 | None | True | True |

## Formal pair topology

- 山西→河北: `t=0:F → t=0.25:C → t=0.5:C → t=0.75:C → t=1:C`; `ALL_INTERIOR_PROBES_CONVERGE`.
- 重庆→河北: `t=0:F → t=0.25:C → t=0.5:C → t=0.75:C → t=1:C`; `ALL_INTERIOR_PROBES_CONVERGE`.
- 江西→安徽: `t=0:F → t=0.25:F → t=0.5:C → t=0.75:C → t=1:C`; `SINGLE_TRANSITION_FAILURE_TO_SUCCESS`.
- 贵州→四川: `t=0:F → t=0.25:C → t=0.5:F → t=0.75:C → t=1:C`; `NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN`.

## Nonconverged mechanism summaries

- pair03_江西_to_安徽_t25: `DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING`.
- pair04_贵州_to_四川_t50: `POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`.

## Interpretation boundary

The confirmed nonmonotone local numerical basin is not an economic multiple equilibrium, provincial-equilibrium multiplicity, calibration error, or mapping error. These synthetic points remain numerical HJB diagnostics only and do not authorize recalibration, clipping, guard/mapping/HJB/selector/floor/grid changes, or Results use.

HJB started/completed/hard-error=`12/12/0`; KFE=`0`; endpoint HJB=`0`; scientific retries=`0`; engineering retries=`1`.

No outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results route ran.

## Exactly one next gate

`REVIEWER_J160_LOCAL_BASIN_REEXECUTION_ROUTE_DECISION`
