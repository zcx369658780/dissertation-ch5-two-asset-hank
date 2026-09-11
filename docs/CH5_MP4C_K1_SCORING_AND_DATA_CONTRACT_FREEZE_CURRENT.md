# Chapter 5 MP4C K1 scoring / data contract freeze

Date: 2026-09-11.
Status: `OWNER_APPROVED_K1_SCORING_DATA_CONTRACT_PARTIAL_FREEZE__ZERO_SCIENCE_MAPPING_AUTHORIZED__PAYOFF_AND_FINAL_BETAS_STILL_PENDING`.

This document records the Owner-approved scientific choices that must be fixed before the next zero-science K1 mapping task. It supplements, and does not replace, `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`.

## 1. Stage order

The scientific sequence is frozen as:

`K1A repaired equal-share baseline -> K1A pure-geographic space-only comparison -> K1B lagged-return endogenous foreign shares -> K2 endogenous home-vs-foreign margin`.

K1A and K1B keep `theta_i=inter_prv_ratio_i` fixed. K2 must not start until K1A/K1B have passed their required accounting, C1-joint, raw-return and bounded numerical evidence gates.

The first K1 scientific integration continues to use source-faithful labor. Accepted normalized bilateral labor is stacked only after the capital channel can be attributed independently.

## 2. K1A distance/friction contract

First scientific distance concept: pure geographical distance only.

Primary source candidate is the already-audited protected MATLAB workbook `中国各省省会地理距离矩阵.xlsx`, subject to a new zero-science identity/mapping receipt before use. Province labels/order must be explicitly reconciled to the active 31-province contract; no position-only silent mapping is allowed.

First dimensionless normalization is frozen as one national common scale:

`distance_score[j,i] = D[j,i] / D_max`

where `D_max` is the maximum valid off-diagonal geographical distance in the same frozen 31-province matrix. The diagonal remains exactly zero. Do not normalize separately by origin column or destination row.

Economic distance, market size, trade linkage, industrial similarity and financial-center terms are deferred. In particular `abs(log(pgdp_i)-log(pgdp_j))` is not part of the first K1A run.

## 3. Equal-share and space-only benchmarks

The first repaired benchmark is the already-accepted equal-foreign-share special case:

`beta_distance=0`, `beta_return=0`.

The next K1A comparison is pure geography with `beta_return=0` and a positive `beta_distance` selected only after static diagnostics. The zero-science task may evaluate a pre-registered diagnostic grid, but none of those values becomes a scientific benchmark merely because it gives attractive matrices or later convergence.

Diagnostic `beta_distance` grid for the zero-science mapping task:

`[0.0, 0.5, 1.0, 2.0, 4.0]`.

This grid is for shape/concentration interpretation only. The Owner must freeze the benchmark coefficient before a model trajectory.

## 4. K1B lagged-return attractiveness contract

K1B attractiveness uses the raw, unclipped destination firm return from the completed previous outer iteration, `ra0`, not the historical clipped `[0.02,0.09]` return.

For completed iteration `n`, define the cross-sectional standardized score:

`return_score_j^(n) = (ra0_j^(n) - mean_j(ra0^(n))) / sd_j(ra0^(n))`.

The next capital allocation uses this score only at iteration `n+1`. Same-turn firm-return feedback remains prohibited.

If the cross-sectional standard deviation is zero or non-finite, the future runtime integration must fail explicitly rather than silently substitute another normalization. The zero-science task may document this edge case; it must not invent a fallback.

Diagnostic `beta_return` grid for static/synthetic interpretation:

`[0.0, 0.25, 0.5, 1.0, 2.0]`.

As with the distance grid, these values are diagnostic candidates, not identified parameters. No coefficient may be selected from trajectory convergence or ex-post fit.

## 5. Attractiveness versus payoff return

Attractiveness and household payoff remain separate objects.

The standardized lagged raw-`ra0` score is authorized only for K1B foreign-destination attractiveness. It is not a household payoff return and must never be passed to `rah` aggregation as if it were a return level.

The final payoff-return concept remains pending. Current candidates remain raw `ra0`, clipped/used `ra`, or a separately justified expected-return object. This unresolved payoff decision does not block the present zero-science distance/score mapping task, but it blocks any K1 runtime integration that would alter household `rah`.

## 6. Portfolio smoothing

No portfolio smoothing / partial adjustment is used in the first K1A or first K1B scientific version. The capital share rule remains the direct frozen softmax mapping from the completed-iteration signals.

Smoothing may be reconsidered only through a new Owner decision if static concentration diagnostics or later authorized numerical evidence establish a substantive need. It must not be introduced as an ad-hoc convergence fix.

## 7. Required zero-science evidence before trajectory

Before any HJB/KFE/firm/outer-loop trajectory call, produce a reproducible zero-science mapping receipt that:

1. identifies and hashes the actual geographical-distance source used;
2. records source labels and exact mapping to the active province order;
3. checks shape, diagonal, finite values, non-negativity and symmetry (or reports any source asymmetry without silently repairing it);
4. computes the frozen `D/D_max` score matrix;
5. confirms the accepted equal-share limit at `beta_distance=beta_return=0`;
6. reports static pure-geographic foreign-share concentration over the diagnostic `beta_distance` grid;
7. documents the frozen lagged raw-`ra0` z-score formula and the diagnostic `beta_return` grid without generating new model returns;
8. preserves the K1 destination-by-origin orientation and all share/conservation identities using static/unit-wealth diagnostics;
9. makes no scientific model call and makes no runtime integration change.

## 8. Still pending Owner freeze

The following remain unresolved after this partial freeze:

- final scientific `beta_distance` benchmark;
- final scientific `beta_return` benchmark;
- household portfolio payoff-return concept;
- any future economic-distance or destination-market-size extension;
- any future smoothing/partial-adjustment rule;
- K2 functional form for endogenous `theta_i`.

These unresolved objects must not be inferred from convergence or chosen after observing a scientific trajectory.

Results eligibility remains `FALSE`.
