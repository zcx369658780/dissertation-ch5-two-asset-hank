# Chapter 5 MP4C K1 scoring / data contract freeze

Date: 2026-09-11.
Status: `OWNER_APPROVED_K1_SCORING_DATA_CONTRACT_FREEZE__K1A_BETA_DISTANCE_2__K1B_BETA_RETURN_POINT5_PREREGISTERED__SOURCE_USED_RA_PAYOFF_BRIDGE`.

This document records the Owner-approved scientific choices for K1A/K1B scoring and the transitional K1A payoff bridge. It supplements, and does not replace, `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`.

## 1. Stage order

The scientific sequence is frozen as:

`K1A repaired equal-share baseline -> K1A pure-geographic space-only comparison -> K1B lagged-return endogenous foreign shares -> K2 endogenous home-vs-foreign margin`.

K1A and K1B keep `theta_i=inter_prv_ratio_i` fixed. K2 must not start until K1A/K1B have passed their required accounting, C1-joint, raw-return and bounded numerical evidence gates.

The first K1 scientific integration continues to use source-faithful labor. Accepted normalized bilateral labor is stacked only after the capital channel can be attributed independently.

## 2. K1A distance/friction contract

First scientific distance concept: pure geographical distance only.

Authoritative mapped source for the first K1A scientific version is the protected MATLAB workbook `中国各省省会地理距离矩阵.xlsx`, accepted through the zero-science mapping report/acceptance. Province labels/order are explicitly reconciled to the active 31-province contract.

Dimensionless normalization is frozen as one national common scale:

`distance_score[j,i] = D[j,i] / D_max`

where `D_max` is the maximum valid off-diagonal geographical distance in the frozen 31-province matrix. The diagonal remains exactly zero. Do not normalize separately by origin column or destination row.

Economic distance, market size, trade linkage, industrial similarity and financial-center terms are deferred. In particular `abs(log(pgdp_i)-log(pgdp_j))` is not part of the first K1A run.

## 3. K1A benchmarks

The repaired equal-foreign-share baseline is:

`beta_distance=0`, `beta_return=0`.

After the accepted static diagnostic over `[0,.5,1,2,4]`, the Owner freezes the first scientific pure-geographic benchmark as:

`beta_distance = 2.0`

with:

`beta_return = 0`.

The first bounded K1A scientific comparison is therefore:

`equal-share beta_distance=0` versus `pure-geographic beta_distance=2`.

This coefficient is preregistered before any K1A runtime trajectory. It must not be changed because one runtime path converges better or looks more attractive.

The accepted zero-science evidence at beta 2 shows mean normalized foreign-share entropy `0.984043`, mean largest foreign share `0.056802`, and mean effective foreign destinations `28.4187`, preserving broad diversification while introducing a material geography tilt.

## 4. K1B lagged-return attractiveness contract

K1B attractiveness uses the raw, unclipped destination firm return from the completed previous outer iteration, `ra0`, not the historical clipped `[0.02,0.09]` return.

For completed iteration `n`, define the cross-sectional standardized score:

`return_score_j^(n) = (ra0_j^(n) - mean_j(ra0^(n))) / sd_j(ra0^(n))`.

The next capital allocation uses this score only at iteration `n+1`. Same-turn firm-return feedback remains prohibited.

If the cross-sectional standard deviation is zero or non-finite, future runtime integration must fail explicitly rather than silently substitute another normalization.

After the accepted zero-science algebraic interpretation, the Owner preregisters the first K1B scientific benchmark as:

`beta_return = 0.5`.

At this value, a destination one standard deviation higher in the return score has an attractiveness odds multiplier `exp(.5)=1.648721`; a two-standard-deviation gap gives `exp(1)=2.718282`.

K1B remains unauthorized to run until K1A bounded evidence is reviewed. The preregistered coefficient cannot be changed ex post based on K1A/K1B convergence or fit.

## 5. Attractiveness versus payoff return

Attractiveness and household payoff remain separate objects.

The standardized lagged raw-`ra0` score is authorized only for K1B foreign-destination attractiveness. It is not a household payoff return and must never be passed to `rah` aggregation as if it were a return level.

For the first K1A runtime integration only, the Owner freezes a transitional payoff bridge:

`portfolio_return_by_destination = current source-used/clipped ra`

Classification:

`K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`.

This choice preserves attribution by changing the private-capital quantity/network logic without simultaneously changing the household return-level law. It does **not** validate `[0.02,0.09]` as an economically identified return interval.

After K1A, the project must re-audit raw `ra0`, clipping pressure and the `rk=mt*alpha*Y/K` decomposition under repaired K1 private capital before freezing a final household payoff-return concept.

## 6. Portfolio smoothing

No portfolio smoothing / partial adjustment is used in the first K1A or first K1B scientific version. The capital share rule remains the direct frozen softmax mapping from the completed-iteration signals.

Smoothing may be reconsidered only through a new Owner decision if later authorized evidence establishes a substantive need. It must not be introduced as an ad-hoc convergence fix.

## 7. Accepted zero-science evidence

The accepted K1A distance/static diagnostic establishes:

- workbook SHA-256 `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566`;
- `geom!B2:AF32` with 31/31 label-backed mapping;
- no missing/negative values and exact symmetry;
- `D_max=3639.514265`;
- normalized off-diagonal range `[0.030224736871583606,1]`;
- authoritative 2018 theta receipt SHA-256 `5DAD517983CBC436A5FB3E5AD85F1257D957D844994180D15929044A049C7212`;
- exact equal-share limit at beta 0;
- K1 conservation identities within `1e-12`;
- all 31 origins weakly decreasing in entropy as beta distance increases;
- no scientific/model/runtime call.

Reviewer acceptance:

`docs/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_ACCEPTANCE.md`.

## 8. Required K1A runtime evidence

The first bounded K1A integration must compare only the preregistered pair `beta_distance=0` and `beta_distance=2`, with `beta_return=0`, source-faithful labor, no smoothing, fixed theta, and source-used/clipped `ra` as the transitional household payoff bridge.

It must re-check, for both paths as applicable:

1. portfolio/share and national private-capital conservation;
2. restored home retained private capital;
3. C1 residual public assets using `GovInv=max(Ktarget-Kprivate,0)`;
4. private-only overshoot where `Kprivate>=Ktarget` without negative GovInv;
5. raw `ra0` decomposition and clipping counts/pressure;
6. bounded outer-path diagnostics and attribution between equal-share and geography-only capital allocation;
7. unchanged source-faithful labor route;
8. current empirical KFE caveat, without claiming the finite-box leakage/pinning blocker is solved.

No parameter, tolerance, solver, grid or payoff-law tuning is allowed after seeing runtime outcomes.

## 9. Still pending Owner decisions

The following remain unresolved after this freeze:

- final household payoff-return concept beyond the K1A source-faithful bridge;
- any future economic-distance or destination-market-size extension;
- any future smoothing/partial-adjustment reconsideration;
- K2 functional form for endogenous `theta_i`;
- any change to historical return safeguards after K1A raw-return re-audit.

K1B `beta_return=.5` is preregistered, not yet runtime-authorized. Results eligibility remains `FALSE`.
