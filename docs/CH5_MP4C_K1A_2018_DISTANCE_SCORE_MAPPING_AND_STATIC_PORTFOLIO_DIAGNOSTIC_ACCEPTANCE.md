# Chapter 5 MP4C K1A distance-score mapping and static portfolio diagnostic acceptance

Date: 2026-09-11.

Reviewer verdict:

`CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_ACCEPTED`

Accepted candidate:

`2ad7c74876d91326c127d8c7ef1c400991320968`

## Evidence accepted

The candidate is one commit ahead of task publication baseline `0090f6d60ba7eeede09a88f2bd5c21887b45bb7b` and contains only the authorized report, zero-science script, and static CSV/JSON receipts. No production scientific source was changed.

The protected geographical-distance workbook was identified as:

`中国各省省会地理距离矩阵.xlsx`

SHA-256:

`26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566`

The mapped source range is `geom!B2:AF32`. All 31 province labels map one-to-one to the active province contract. The mapped matrix has 961 finite values, no missing values, no negative values, exact symmetry, and maximum off-diagonal distance `3639.514265` between Heilongjiang and Tibet. The source unit remains unresolved and is therefore not invented.

The frozen common-scale normalization `D/D_max` is accepted. The normalized off-diagonal range is `[0.030224736871583606,1]` and `max|D-D.T|=0`.

The 2018 `theta_i=inter_prv_ratio_i` vector is provenance-bound through the accepted initialization receipt with SHA-256 `5DAD517983CBC436A5FB3E5AD85F1257D957D844994180D15929044A049C7212`; all 31 entries map to the exact active province order and the source-formula replay residual is zero.

The repaired equal-share special case is reproduced exactly. All foreign-share, full-share, origin-capital and national-capital conservation residuals are below the accepted `1e-12` tolerance and no destination-`theta_j` double weighting is present.

## Static distance diagnostics

The pre-registered `beta_distance=[0,.5,1,2,4]` grid was evaluated with `beta_return=0` only as a static mapping diagnostic. Mean normalized entropy declines monotonically from `1.000000` at beta 0 to `0.943791` at beta 4; all 31 origins weakly decrease in entropy with increasing beta. Mean largest foreign share rises from `0.033333` to `0.088301`, while mean effective destinations decline from `30.0000` to `24.8228`.

The evidence therefore supports using geography as a meaningful but still diversified foreign-allocation friction. It does not by itself estimate or calibrate a coefficient.

## K1B algebra accepted

The zero-science algebraic interpretation of `beta_return=[0,.25,.5,1,2]` is accepted. For one and two standard-deviation score gaps the corresponding odds multipliers are respectively:

- beta 0: `1`, `1`;
- beta .25: `1.284025`, `1.648721`;
- beta .5: `1.648721`, `2.718282`;
- beta 1: `2.718282`, `7.389056`;
- beta 2: `7.389056`, `54.598150`.

No new `ra0` was generated and no household payoff-return choice was made by the Builder.

## Verification boundary

Pure capital-network tests: `29/29` passed. Scientific/model/runtime calls: `0` for MATLAB, HJB, KFE, household, firm, outer loop, steady state, trajectory, GE, annual, shock/IRF and Results. Remote manifest readback passed `11/11` with manifest SHA-256 `5B35A568EBBF8D62B003755B23215EF8988911D5DEB22A45284B02FD1DCF9588`.

The early abandoned non-v2 branch is not accepted evidence. The only accepted Builder candidate for this task is `codex/ch5-k1a-distance-mapping-20260911-v2` at `2ad7c74876d91326c127d8c7ef1c400991320968`.

## Owner freeze following acceptance

After reviewing these static diagnostics, the Owner explicitly approved the Reviewer recommendation:

1. K1A pure-geographic scientific benchmark: `beta_distance=2.0`;
2. first bounded K1A comparison: repaired equal-share `beta_distance=0` versus pure-geographic `beta_distance=2`;
3. K1B benchmark is preregistered as `beta_return=0.5`, but K1B is not yet authorized to run;
4. K1B attractiveness remains completed-iteration raw unclipped `ra0` cross-sectional z-score;
5. K1A household payoff bridge remains the current source-used/clipped `ra` only to preserve attribution, classified as `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`;
6. smoothing/partial adjustment remains OFF;
7. source-faithful labor remains frozen for first K1 integration;
8. K1A must re-audit K1 private capital + C1 residual GovInv and raw-ra decomposition;
9. K1B may start only after K1A bounded evidence is reviewed;
10. K2 remains unauthorized.

Results eligibility remains `FALSE`.
