# CH5 MP4C K1 raw `ra0` payoff HJB/drift zero-science forensic report

Date: 2026-09-12

## Classification

`RAW_PAYOFF_SCALE_EXPOSURE_PROPAGATES_THROUGH_ACCEPTED_VALUE_DERIVATIVE_TRANSFER_COST_LAW__UPPER_A_BOUNDARY_REGIME_EXPANDS__MIXED_BASELINE_EXTREMES__OWNER_DECISION_REQUIRED`

The accepted four-turn Raw treatment is not a simple boundary-only failure. Its largest liquid drift, illiquid drift and transfer/adjustment-cost cells are overwhelmingly interior. The direct raw-payoff level increase enters the accepted HJB as `r_a`, changes the solved value derivatives, and is then strongly amplified by the accepted raw-`V_b` transfer FOC and quadratic adjustment-cost law. A separate secondary response is a large expansion of positive outward total `mu_a` at the upper-`a` face.

Control already contains very large finite transfer/cost/drift outliers, and Raw is smaller than Control in a material subset of matched province-turn maxima and in all global maxima at turn 4. The correct attribution is therefore mixed baseline numerical behavior plus substantial Raw incremental amplification, not “all large values are caused by Raw.”

The only recommended next gate is:

`A_OWNER_SCIENTIFIC_DECISION_ON_PAYOFF_MAPPING_SCALE_INTERPRETATION`

No additional runtime or instrumentation is needed to establish this localization. The unresolved decision is whether the frozen model-time raw payoff scale and its interaction with the accepted value-derivative/transfer-cost law are scientifically intended. This report does not select a new mapping, cap, normalization, boundary law or solver rule.

Results eligibility=`FALSE`.

## Authority, evidence and zero-call boundary

- live-main baseline: `fb5ebaea842f7ce4c3bfa29e6aa328d72fd94eb4`;
- accepted safety candidate: `678860073d3d5b653b8863b71f494f569960ced7`;
- accepted input evidence: `D:\ProjectTemp\ch5-k1-raw-ra0-bootstrap-safety-evidence-20260912-001`;
- accepted input manifest: `69E85A9CAF6A23F5B7402821112F1A0465E2617F8A44ACEE167BC61D25B1E644`, `1041/1041` readback PASS;
- final forensic evidence: `D:\ProjectTemp\ch5-k1-raw-ra0-hjb-drift-forensic-evidence-20260912-002`;
- final forensic manifest: `77E8F72BCCF9E9258CD7C4F520D8793C407D999DC3E6C3E8051D19C13949C463`, `11/11` readback PASS;
- compact evidence: `docs/evidence/ch5_mp4c_k1_raw_ra0_hjb_drift_forensic/`.

The earlier `...forensic-evidence-20260912-001` directory is a preserved, superseded zero-science engineering draft. It was not overwritten; it is not the final evidence root and is not tracked.

New scientific/model calls were exactly zero: trajectory `0`, HJB `0`, KFE `0`, firm runtime `0`, household runtime `0`, MATLAB `0`, K1B `0`, K2 `0`, GE `0`, annual `0`, IRF `0`, Results `0`. The forensic only verified hashes and parsed persisted JSON/CSV/NPZ arrays.

## Matching and grid-coordinate provenance

The analysis matched `124` province-turn observations in each path over turns 2-5 and matched all HJB cells by `(province, turn, i_b, i_a, i_z)`. Turn-1 numeric arrays and policy-label arrays were rechecked as exactly identical.

Each HJB NPZ persists arrays of shape `(20,20,2)` in `(b,a,z)` order plus `liquid_label` and `transfer_label`, but it does not persist coordinate axes as separate arrays. Coordinates reported here are therefore classified:

`PERSISTED_ARRAY_INDEX_PLUS_ACCEPTED_SOURCE_FIXED_GRID`

The binding comes from `validators/multi_province/g1_residual_govinv_25turn_isolated/run.py:315-318`: `b=linspace(-2,5,20)`, `a=linspace(0,10,20)`, `z=[0.8,1.3]`, and HJB `max_iterations=100`, drift tolerance `1e-12`. This is not described as an NPZ-contained coordinate object.

The file `province_turn_array_stats.csv` contains, for every matched province, turn and variable, Control/Raw min, median, p95, p99, max and absolute max plus Raw-Control differences and ratios. `extreme_cells.csv` contains matched coordinates, values, labels and HJB context for the top cells.

## HJB convergence localization

| Turn | Control converged | Raw converged | Control hit 100 | Raw hit 100 | Control-converged to Raw-nonconverged | Raw recovery |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 13/31 | 4/31 | 18 | 27 | 11 | 2 |
| 3 | 13/31 | 4/31 | 18 | 27 | 13 | 4 |
| 4 | 12/31 | 4/31 | 19 | 27 | 10 | 2 |
| 5 | 11/31 | 0/31 | 21 | 31 | 11 | 0 |

Across the treatment horizon, Raw creates `45` matched Control-converged/Raw-nonconverged observations and recovers `8` Control-nonconverged observations. Only `4` observations converge in both paths. Thus the aggregate `49/124` versus `12/124` comparison hides substantial state-path switching rather than a strict nested loss of convergence.

The provinces switching from Control converged to Raw nonconverged in all four turns are `辽宁、吉林、黑龙江、广西、云南`. Frequencies are four turns for those five; three turns for `海南、青海、西藏、新疆`; and one or two turns for the remaining affected provinces. The complete turn-specific lists are in `province_turn_hjb_exposure.csv`.

The largest Raw HJB statistics occur at:

| Turn | Province | Raw statistic | Matched Control | Raw entering `rah` |
|---:|---|---:|---:|---:|
| 2 | 山东 | 403.6870 | 0.1842 | 0.3533 |
| 5 | 广西 | 297.0192 | 7.16e-09 | 0.3991 |
| 2 | 宁夏 | 292.4053 | 0.2119 | 0.4130 |
| 4 | 河南 | 152.6812 | 0.3770 | 0.3397 |
| 5 | 贵州 | 142.2752 | 0.00248 | 0.5992 |
| 2 | 浙江 | 128.8730 | 0.5400 | 0.5854 |
| 3 | 黑龙江 | 98.8560 | 2.12e-08 | 0.3333 |

Control's own worst observation is 河南 turn 5 with statistic `17.9950`; its next largest are 湖南 turn 5 `5.6028`, 浙江 turn 5 `4.2700`, and 北京 turn 5 `3.3340`. The worst Raw HJB observations are not simply the highest-`rah` provinces.

## Payoff exposure

Raw median entering `rah` remains about `5.306/5.627/5.609/5.591` times Control over turns 2-5. At the matched province-turn level, Raw entering `rah` is almost rank-identical to the same-index prior raw firm `ra0` and raw-minus-used gap: Pearson `0.9982`, Spearman `0.9946`. This confirms the intended scale exposure and clipping-gap provenance.

The highest exposures are 北京 and 上海. 北京 reaches `rah=1.02825` with same-index prior `ra0=1.11390`; 上海 reaches `rah=0.95736` with prior `ra0=1.02545`. Their HJB outcomes vary sharply: 北京 turn 4 has statistic only `2.41e-4`, while 上海 turn 4 has `49.1861`. Conversely, the global worst statistic, 山东 turn 2, has `rah=0.35334`, below the cross-province Raw median.

Consistently, Raw `rah` has weak province-turn association with the HJB statistic (Pearson `-0.1309`, Spearman `-0.1080`) and with hitting the iteration ceiling (`-0.0850`, `-0.1227`). It also has weak association with Raw drift/transfer absolute maxima (absolute coefficients generally below `0.17`). Payoff scale cleanly separates the two paths but does not by itself rank which province-turn becomes the most numerically stressed.

All correlations in this report are `DESCRIPTIVE_ONLY_NOT_CAUSAL`.

## Drift, control and adjustment-cost forensic

The full required distributions are in `array_distribution_by_turn.csv` and `province_turn_array_stats.csv`. The main pooled treatment-turn findings are:

- effective illiquid return has Control median approximately `0.08998` in every turn and Raw medians `0.4767/0.5053/0.5042/0.5026`; Raw absolute maxima are `0.8951/1.0142/1.0283/1.0281`, roughly `9.95-11.43` times Control;
- Raw transfer medians are `-1.109/-0.833/-0.683/-0.851`, while Control medians are zero. Raw transfer p99 is `417.7/505.6/168.7/844.0` versus Control `68.2/96.2/51.6/420.4`;
- Raw adjustment-cost medians are `4.85/5.84/8.37/6.11` versus Control `0.112/0.121/0.136/0.134`. Raw p99 is `4.59e5/9.92e5/8.39e4/1.02e6`;
- Raw `mu_b` medians change sign and become `-2.61/-5.40/-13.51/-8.11`, whereas Control medians remain positive near `1.80-2.14`;
- Raw labor p95 is `1.275/1.215/0.953/1.047` versus Control `0.781/0.780/0.786/0.791`; Raw labor absolute maxima are `1.31-3.10` times Control;
- consumption median changes are moderate and non-monotone. Both paths have p95/p99/max exactly `1000` in every treatment turn, matching the accepted `V_b` derivative-floor consumption branch rather than a Raw-only phenomenon.

Global absolute maxima expose the mixed attribution:

| Turn | Quantity | Control abs max | Raw abs max | Raw/Control |
|---:|---|---:|---:|---:|
| 2 | transfer / `mu_a` | 5.95e4 / 5.95e4 | 1.93e6 / 1.93e6 | 32.39 / 32.39 |
| 2 | cost / `mu_b` | 3.74e8 / 3.74e8 | 4.15e11 / 4.15e11 | 1111 / 1111 |
| 3 | transfer / `mu_a` | 8.28e5 / 8.28e5 | 2.74e6 / 2.74e6 | 3.30 / 3.30 |
| 3 | cost / `mu_b` | 1.00e11 / 1.00e11 | 1.29e12 / 1.29e12 | 12.91 / 12.91 |
| 4 | transfer / `mu_a` | 4.84e5 / 4.84e5 | 2.50e5 / 2.50e5 | 0.517 / 0.517 |
| 4 | cost / `mu_b` | 2.78e10 / 2.78e10 | 1.08e10 / 1.08e10 | 0.389 / 0.389 |
| 5 | transfer / `mu_a` | 9.29e4 / 9.29e4 | 2.24e6 / 2.24e6 | 24.12 / 24.12 |
| 5 | cost / `mu_b` | 1.17e9 / 1.17e9 | 6.36e11 / 6.36e11 | 542.99 / 542.94 |

At the matched province-turn level, Raw absolute maxima are smaller than Control in `35/124` transfer, `35/124` `mu_a`, `36/124` adjustment-cost and `36/124` `mu_b` observations. Raw is smaller for labor in `25/124`, but never for effective illiquid return. This rules out a uniform monotone Raw amplification claim.

Nevertheless the stress variables move together strongly. Raw `mu_b` abs max versus adjustment-cost abs max has Pearson `0.999999999998` and Spearman `0.9979`; `mu_a` versus transfer has Pearson `0.999999999955` and Spearman `0.9991`. HJB statistic versus each drift/transfer/cost maximum has weak outlier-dominated Pearson values near zero but strong rank association, Spearman approximately `0.763-0.768`. This is descriptive evidence that convergence stress ranks with the derivative/transfer/cost amplification even though a few enormous cells dominate levels.

## Extreme-cell localization

Of the top ten cells per turn/path for each of `mu_b`, `mu_a` and transfer, `114/120` Raw-ranked entries and `111/120` Control-ranked entries are interior. The same cell commonly supplies all three extrema because adjustment cost is quadratic in transfer and is subtracted from `mu_b`.

Representative Raw maxima are:

| Turn | Province | `(b,a,z)` | Labels `(liquid,transfer)` | transfer | cost | `mu_a` | `mu_b` |
|---:|---|---|---|---:|---:|---:|---:|
| 2 | 辽宁 | `(2.421,8.947,1.3)` | `(B,B)` | `1.927e6` | `4.151e11` | `1.927e6` | `-4.151e11` |
| 3 | 安徽 | `(-0.895,5.789,1.3)` | `(B,B)` | `-2.736e6` | `1.293e12` | `-2.736e6` | `-1.293e12` |
| 4 | 江苏 | `(0.579,5.789,0.8)` | `(B,B)` | `-2.503e5` | `1.082e10` | `-2.503e5` | `-1.082e10` |
| 5 | 上海 | `(2.053,7.895,0.8)` | `(B,B)` | `-2.240e6` | `6.356e11` | `-2.240e6` | `-6.356e11` |

All four cells are interior. At 辽宁 turn 2 the matched Control values are transfer `-0.872`, cost `0.172`, `mu_a=-0.0967`, `mu_b=6.415`; the Raw branch switches both labels from `(F,F)` to `(B,B)`. At 安徽 turn 3, Control is already nontrivial (`d=77.0`, cost `1031.9`, `mu_b=-2106.4`) but Raw expands it by many orders. At 上海 turn 5, Control is already extreme (`d=3891`, cost `1.918e6`, `mu_b=-1.922e6`) before Raw reaches `-6.356e11`. Turn 4 is the global counterexample: Control's 福建 upper-`b` cell is more extreme than Raw's global maximum.

## Boundary regimes

Each single face contains `1240` cells per path and turn.

| Turn | upper-`a` Control | upper-`a` Raw | Raw-only upper-`a` | upper-`b` Control | upper-`b` Raw | lower-`b` Raw exact-sign |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 211 | 513 | 419 | 649 | 398 | 0 |
| 3 | 249 | 517 | 411 | 664 | 386 | 6 |
| 4 | 251 | 387 | 271 | 692 | 344 | 9 |
| 5 | 258 | 496 | 380 | 646 | 417 | 7 |

Lower-`a` outward counts are zero in both paths. Upper-`a` positive total-`mu_a` events expand from roughly `17-21%` of Control face cells to `31-42%` in Raw, with `271-419` Raw-only cells per turn. Raw HJB statistic has Spearman `0.567` with its upper-`a` count and `0.519` with Raw-only upper-`a` count, though Pearson is only `0.127/0.064`; this supports a rank-level boundary interaction, not a linear or causal estimate.

Upper-`b` outward total-`mu_b` events are a strong Control baseline: `646-692` per turn. Raw has fewer total upper-`b` events (`344-417`), although the cell identities change substantially: Raw-only `145-180`, Control-only `402-493`. Control upper-`b` outward cells uniformly carry `(liquid F, transfer B)` labels; almost all Raw cells do as well. Raw therefore does not create a larger aggregate upper-`b` outward regime.

The previously reported Raw lower-`b` counts `0/6/9/7` are all exactly `mu_b=-8.881784197001252e-16`, below the accepted `1e-12` drift tolerance. They occur only in 海南 and 青海 at `z=0.8`, with liquid/transfer labels `(0,0)`, transfer `0`, and adjustment cost `0`. They are classified:

`EXACT_SIGN_ONLY_BELOW_ACCEPTED_DRIFT_TOLERANCE__NOT_MATERIAL_KKT_EVIDENCE`

They are not a new economically material policy branch and do not establish a KKT failure.

## Exact source-law trace

1. Actual runtime binding: `validators/multi_province/g1_residual_govinv_25turn_isolated/run.py:164-193` passes `state["rah"]` as the first `HouseholdInputs` argument (`r_a`), calls `solve_matlab_faithful_hjb`, and persists `hjb_return.npz` before KFE. The static API crosswalk states the same mapping at `src/ch5_two_asset_hank/multi_province/household_adapter.py:45,200-219`.
2. Effective return: `exports/matlab_faithful_two_asset_ha.py:111-124` applies `r_a*(1-0.1*(a/a_max)^9)`. Lines `371-378` put this tapered return into the illiquid shadow construction.
3. Consumption/labor: lines `126-146` derive them from `V_b`; lines `274-304` floor `V_b` at `1e-6` for these branches. Raw `r_a` therefore affects them indirectly through the HJB value function and derivatives, not as a direct addend.
4. Transfer: lines `93-109` compute the faithful transfer candidate from raw `V_a/V_b` and bare `a`, without the consumption derivative floor. Lines `306-369` combine candidates and select `B/F/0` branches. This raw-derivative ratio is the immediate source-law channel capable of producing the persisted million-scale transfers.
5. Adjustment cost and drifts: lines `80-83` define `chi_0*abs(d)+0.5*chi_1*d^2/max(a,a_bar)`. Lines `148-167` then define `mu_a=r_a_effective*a+d` and `mu_b=r_b*b+labor_income-d-cost-consumption`. The persisted near-identity between cost and huge negative `mu_b`, and between transfer and `mu_a`, follows these exact equations.
6. Boundary selectors: lines `312-320` constrain transfer candidates at lower/upper `a`; lines `348-355` suppress backward transfer at lower `b` and force the backward branch at upper `b`. Lines `371-376` add effective return at the upper-`a` shadow branch, and lines `401-415` form direction/rate labels.
7. Operator law: lines `424-463` omit outward neighbor entries but retain their rates in the diagonal. HJB iteration and convergence occur at lines `510-562`; the post-convergence operator at line `561` separately upwinds saved total drifts. These are accepted faithful laws, not new correctness claims.

The accepted source thus supports a direct `r_a -> tapered return -> mu_a` channel, an indirect `r_a -> solved V -> raw V_a/V_b -> d -> quadratic cost -> mu_b` amplification chain, and explicit boundary-selector interactions. It does not support the shortcut claim that `rah` directly enters consumption or that every outward sign is a KKT violation.

## KKT and final boundary

The accepted HJB return object contains no standalone KKT residual. This forensic did not synthesize one. KKT status is:

`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`

Policy labels, boundary indices, raw drift signs and source-law invariants are descriptive evidence only. No payoff remapping, clipping, normalization, cap, smoothing, HJB/KFE equation, boundary law, grid, tolerance or solver change is authorized. No 25-turn Raw trajectory, K1B, K2 or Results work follows automatically.
