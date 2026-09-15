# CH5 MP4C K1 — J160 coordinate-resolved selector/floor matched-control diagnostic

## Terminal panel class

`HETEROGENEOUS_COORDINATE_RESOLVED_FAILURE_FOOTPRINTS`

Results eligibility=`FALSE`.

## Authority and invariance

Actual baseline: `543e7fc434ea75d1e18453922809bba05a0cec18`. Authority gate and instrumentation invariance both passed before science. The accepted Oracle was called directly; coordinate copies did not feed scientific control flow. No parity HJB was added.

Spatial bins were frozen before science: exact endpoint, one-index near band, interior, one-index near-upper band, exact upper endpoint. The matched-control thresholds were also frozen before science: concentration 0.50, failure-control margin 0.10, and total-variation overlap/heterogeneity boundary 0.20.

## Seven-province outcomes and footprints

| province | role | replay | reproducibility | selector events | selector upper-b | floor hits | floor upper-b | argmax upper-b | argmax/selector coincide | argmax/floor coincide |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 天津 | failure | HJB_NOT_CONVERGED@100 | PASS | 92230 | 6.57% | 105548 | 9.58% | 63.00% | 46.00% | 24.00% |
| 江西 | failure | HJB_NOT_CONVERGED@100 | PASS | 26789 | 9.92% | 29030 | 11.09% | 89.00% | 33.00% | 7.00% |
| 贵州 | failure | HJB_NOT_CONVERGED@100 | PASS | 17995 | 8.20% | 20728 | 20.42% | 56.00% | 34.00% | 9.00% |
| 甘肃 | failure | HJB_NOT_CONVERGED@100 | PASS | 13562 | 8.24% | 2500 | 54.56% | 89.00% | 24.00% | 11.00% |
| 湖南 | control | HJB_CONVERGED@75 | PASS | 13456 | 7.91% | 1174 | 65.76% | 88.00% | 22.67% | 6.67% |
| 上海 | control | HJB_CONVERGED@51 | PASS | 12182 | 8.29% | 836 | 48.80% | 90.20% | 15.69% | 5.88% |
| 福建 | control | HJB_CONVERGED@52 | PASS | 12483 | 7.76% | 1626 | 44.16% | 84.62% | 30.77% | 5.77% |

## Type-resolved selector and floor footprints

| province | liquid selector events / upper-b | transfer selector events / upper-b | forward floor hits / upper-b | backward floor hits / upper-b | selector double-interior | floor double-interior |
|---|---:|---:|---:|---:|---:|---:|
| 天津 | 35873 / 8.28% | 56357 / 5.49% | 52774 / 6.78% | 52774 / 12.37% | 81.95% | 81.77% |
| 江西 | 8147 / 12.30% | 18642 / 8.88% | 14515 / 7.58% | 14515 / 14.60% | 83.19% | 85.17% |
| 贵州 | 4818 / 9.36% | 13177 / 7.78% | 10364 / 16.20% | 10364 / 24.63% | 82.40% | 78.25% |
| 甘肃 | 3229 / 9.01% | 10333 / 7.99% | 1250 / 38.72% | 1250 / 70.40% | 81.53% | 45.44% |
| 湖南 | 3240 / 7.72% | 10216 / 7.98% | 587 / 57.07% | 587 / 74.45% | 81.93% | 34.24% |
| 上海 | 3196 / 7.35% | 8986 / 8.62% | 418 / 30.62% | 418 / 66.99% | 82.48% | 51.20% |
| 福建 | 3020 / 7.95% | 9463 / 7.70% | 813 / 29.15% | 813 / 59.16% | 82.77% | 55.84% |

All coincidence measures are exact-cell, same-iteration descriptive shares; they are not causal effects.

## Matched controls

- 天津 vs 湖南: selector upper-b 6.57% vs 7.91%, TV `0.0253746`; floor upper-b 9.58% vs 65.76%, TV `0.564372`.
- 江西 vs 上海: selector upper-b 9.92% vs 8.29%, TV `0.0302216`; floor upper-b 11.09% vs 48.80%, TV `0.377153`.
- 贵州 vs 福建: selector upper-b 8.20% vs 7.76%, TV `0.0130756`; floor upper-b 20.42% vs 44.16%, TV `0.237406`.
- 甘肃 vs 福建: selector upper-b 8.24% vs 7.76%, TV `0.0159211`; floor upper-b 54.56% vs 44.16%, TV `0.104026`.

## Required interpretation

贵州 recurrence localization: `COORDINATE_RESOLVED_STABLE_CHANGED_CELL_SET`; exact value period-2 recurrence=`FALSE`. No value two-cycle is claimed.

天津's mixed value argmax does not imply a mixed selector/floor footprint: selector and floor events are 81.95% and 81.77% double-interior, while their upper-b shares are only 6.57% and 9.58%.

江西 floor hits are primarily double-interior (85.17%), not liquid-upper concentrated (11.09%), despite its accepted upper-b value-argmax label.

甘肃's upper-b argmax concentration is not mirrored by its selector footprint (8.24%); its floor upper-b share is 54.56%, compared with 44.16% for 福建.

Successful controls have selector upper-b shares comparable to failures and substantial floor upper-b activity. Upper-b activity is therefore not a failure-specific pathology in this panel.

Failure-specific upper-b selector+floor condition across all matched pairs=`FALSE`. Failure selector maximum pairwise TV=`0.0511591` and floor maximum pairwise TV=`0.452391`.

A common coordinate-resolved failure mechanism is not supported: `TRUE` for preregistered failure heterogeneity.

The panel result is descriptive numerical evidence only. It does not authorize a boundary/domain, selector, floor, HJB, mapping, or calibration change.

## Runtime ledger

HJB `7/7`; failed provinces `4/4`; successful controls `3/3`; KFE=`0`; scientific retries=`0`; engineering retry=`1/1` before science. Outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results are all zero.

## Exactly one next gate

`REVIEWER_COORDINATE_RESOLVED_SELECTOR_FLOOR_ROUTE_DECISION`
