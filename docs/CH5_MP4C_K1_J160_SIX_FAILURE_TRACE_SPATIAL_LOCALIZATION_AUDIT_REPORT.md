# CH5 MP4C K1 — J160 six-failure trace spatial localization audit

## Panel spatial classification

`HETEROGENEOUS_SPATIAL_LOCALIZATION_ACROSS_FAILURES`

Results eligibility=`FALSE`.

## Authority and pre-registration

Trace authority gate: `PASS`.

Actual baseline: `86ae2936f62c3473f48d3671cb08feba19d0fd83`. Accepted source candidate: `ad4cdc8bbdf924c2ed06477abc10d1010038a5f7`.
The accepted 35-entry six-failure manifest, six 100-iteration traces, source/input/instrumentation receipts, panel classifications, diagnostic report, and accepted J640 authority were verified before analysis.

The near-boundary band was frozen before inspecting coordinate values: exact boundary is index `0` or `size-1`; near boundary is index distance exactly one from either edge, excluding exact endpoints; all remaining indices are interior. Asset-side concentration requires share `>=0.80`. The discrete `z` state is reported but is not treated as an asset boundary.

## Province value-argmax spatial footprints

| province | accepted mechanism | spatial label | modal `(b,a,z)` index | modal state | modal share | b lower/upper band | a lower/upper band | joint interior | location changes |
|---|---|---|---|---|---:|---:|---:|---:|---:|
| 天津 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION | MIXED_SPATIAL_FOOTPRINT | (2,159,0) | (0.315789473684,100,0.8) | 4.00% | 6.00%/63.00% | 1.00%/23.00% | 10.00% | 90 |
| 山西 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION | MIXED_SPATIAL_FOOTPRINT | (19,32,1) | (20,20.1257861635,1.3) | 7.00% | 3.00%/52.00% | 4.00%/2.00% | 43.00% | 70 |
| 江西 | DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING | LIQUID_UPPER_BOUNDARY_CONCENTRATED | (19,41,1) | (20,25.786163522,1.3) | 13.00% | 3.00%/89.00% | 2.00%/2.00% | 7.00% | 74 |
| 重庆 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION | MIXED_SPATIAL_FOOTPRINT | (19,33,1) | (20,20.7547169811,1.3) | 7.00% | 3.00%/68.00% | 3.00%/2.00% | 27.00% | 64 |
| 贵州 | REPEATING_OR_LOW_PERIOD_CYCLE | MIXED_SPATIAL_FOOTPRINT | (19,26,0) | (20,16.3522012579,0.8) | 5.00% | 4.00%/56.00% | 2.00%/2.00% | 39.00% | 70 |
| 甘肃 | POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION | LIQUID_UPPER_BOUNDARY_CONCENTRATED | (19,31,1) | (20,19.4968553459,1.3) | 12.00% | 3.00%/89.00% | 2.00%/2.00% | 7.00% | 64 |

These labels describe only the sealed **value-update argmax spatial footprint**; they are not generalized to all unstable cells.

## Selector and derivative-floor localization

- 天津: selector `COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE` (first change 2, active iterations 99); floor `FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE` (first hit 58, active iterations 43).
- 山西: selector `COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE` (first change 2, active iterations 99); floor `FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE` (first hit 7, active iterations 92).
- 江西: selector `COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE` (first change 2, active iterations 99); floor `FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE` (first hit 7, active iterations 87).
- 重庆: selector `COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE` (first change 2, active iterations 89); floor `FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE` (first hit 13, active iterations 88).
- 贵州: selector `COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE` (first change 2, active iterations 99); floor `FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE` (first hit 9, active iterations 91).
- 甘肃: selector `COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE` (first change 2, active iterations 86); floor `FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE` (first hit 11, active iterations 90).

Counts and hashes were not converted into coordinates. Consequently, 江西 floor activity cannot be tied to a particular boundary, and 贵州's joint-selector recurrence remains hash-level only: iteration 96→98, period 2, with no coordinate-resolved selector recurrence and no exact value recurrence.

## Cross-province comparison

Four-chatter comparison: `HETEROGENEOUS_VALUE_ARGMAX_SPATIAL_SIGNATURE__SELECTOR_AND_FLOOR_COORDINATES_UNAVAILABLE`. Maximum pairwise total-variation distance is `0.38` under the pre-registered `0.20` materiality threshold. This comparison is limited to value argmax coordinates.

江西 and 贵州 are compared descriptively with the chatter provinces. Their mechanism labels do not supply missing floor/selector coordinates and are not treated as causal location evidence.

Accepted J640 comparison: `J640_SPATIAL_COMPARISON_LIMITED_BY_ACCEPTED_EVIDENCE`. J640 sealed value-argmax label: `LIQUID_UPPER_BOUNDARY_CONCENTRATED` (b-upper band `89.00%`, joint asset interior `8.00%`). The accepted CSV supports this value-argmax spatial summary, but not selector-changed-cell or derivative-floor-hit coordinates; no J640 replay was run.

## Panel conclusion

`HETEROGENEOUS_SPATIAL_LOCALIZATION_ACROSS_FAILURES`

This conclusion does not authorize boundary repair, grid expansion, HJB modification, or calibration modification. Scientific/model runtime remained exactly zero and Results eligibility remains `FALSE`.

## Exactly one next gate

`REVIEWER_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_ROUTE_DECISION`
