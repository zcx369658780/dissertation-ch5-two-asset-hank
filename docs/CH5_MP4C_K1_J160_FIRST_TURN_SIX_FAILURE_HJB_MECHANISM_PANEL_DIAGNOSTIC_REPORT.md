# CH5 MP4C K1 — J160 first-turn six-failure HJB mechanism panel diagnostic

## Panel terminal classification

`SIX_FAILURES_HETEROGENEOUS_MECHANISMS`

Results eligibility=`FALSE`.

## Authority and instrumentation invariance

The accepted viability and J640 mechanism manifests passed exact byte/canonical-LF verification. The six full household-call inputs were recovered from the accepted sealed input artifact. The accepted J640 observational wrapper was imported unchanged and its accepted OFF/ON parity authority was reused without a new HJB call.

For all six calls, the sealed common inputs were `rb=.02`, `tau=.05`, transfer income `=.1`, borrowing-rate gap `=.07`, return guard `NOT_APPLIED_BOOTSTRAP`, wage guard `UNSATURATED`, D1 OFF, and the accepted adapter parameters. The province-specific consumed `ra/rah` and composite `w` appear below; raw `wjt` was not substituted.

## Province replay and event ordering

| province | ra | composite w | replay | first switch | first non-decrease | first floor | decreases/non-decreases | class |
|---|---:|---:|---|---:|---:|---:|---:|---|
| 天津 | 0.064903654754207341 | 18.198003011640164 | nonconverged@100 | 2 | 7 | 58 | 33/66 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION |
| 山西 | 0.086435763945140257 | 18.203099062044032 | nonconverged@100 | 2 | 6 | 7 | 55/44 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION |
| 江西 | 0.089119604567388377 | 18.066338850784597 | nonconverged@100 | 2 | 8 | 7 | 54/45 | DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING |
| 重庆 | 0.085928853272355457 | 18.070548844406634 | nonconverged@100 | 2 | 7 | 13 | 50/49 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION |
| 贵州 | 0.089790227585121882 | 17.471672154406804 | nonconverged@100 | 2 | 7 | 9 | 55/44 | REPEATING_OR_LOW_PERIOD_CYCLE |
| 甘肃 | 0.089999999999999997 | 17.49933815729084 | nonconverged@100 | 2 | 7 | 11 | 56/43 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION |

All event-order statements are descriptive temporal evidence, not causal identification.

贵州 has exact joint-selector recurrence from iteration 96 to 98 (period 2); no exact value recurrence was observed.

## Nearest accepted successful provinces

- 天津 → 湖南: raw `(ra,w)` Euclidean distance `0.049244519450320184`, success input `(0.0872058027276669,18.15409814981755)`, iterations `75`, final statistic `8.930916006733014e-10`.
- 山西 → 湖南: raw `(ra,w)` Euclidean distance `0.049006962349792876`, success input `(0.0872058027276669,18.15409814981755)`, iterations `75`, final statistic `8.930916006733014e-10`.
- 江西 → 上海: raw `(ra,w)` Euclidean distance `0.034683197460431164`, success input `(0.0786410648427616,18.0332764190634)`, iterations `51`, final statistic `5.020913906861324e-09`.
- 重庆 → 上海: raw `(ra,w)` Euclidean distance `0.03797822469733616`, success input `(0.0786410648427616,18.0332764190634)`, iterations `51`, final statistic `5.020913906861324e-09`.
- 贵州 → 福建: raw `(ra,w)` Euclidean distance `0.1510271666778284`, success input `(0.08227353131506258,17.622512150269692)`, iterations `52`, final statistic `5.116336243560227e-10`.
- 甘肃 → 福建: raw `(ra,w)` Euclidean distance `0.12341608835437021`, success input `(0.08227353131506258,17.622512150269692)`, iterations `52`, final statistic `5.116336243560227e-10`.

This nearest-neighbor comparison uses accepted receipts only and is descriptive; distance is not a causal explanation.

## J640 comparison and boundaries

The accepted J640 reference was policy/selector chatter with first switch at iteration 2, first value-stat non-decrease at 8, first derivative-floor hit at 10, 61 decreases and 38 non-decreases, persistent switching, and no exact low-period value cycle. Similarity or difference in temporal order does not establish a shared or distinct causal mechanism.

Panel conclusion: `SIX_FAILURES_HETEROGENEOUS_MECHANISMS`.

HJB calls: `6/6`; KFE=`0`; successful-province HJB=`0`; scientific retries=`0`.

The corrected multi-province finite-box upper-b leakage / MATLAB-style pinning KFE blocker remains unresolved. No outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results route ran.

## Exactly one next gate

`REVIEWER_SIX_FAILURE_HJB_MECHANISM_ROUTE_DECISION`
