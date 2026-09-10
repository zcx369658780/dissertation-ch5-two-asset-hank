# Chapter 5 MP4C GovInv initialization and labor-normalization redesign specification — Reviewer acceptance

Date: 2026-09-10

Reviewer verdict:

`GOVINV_LABOR_REDESIGN_SPEC_ACCEPTED__CAPITAL_AND_LABOR_CORRECTION_PATHS_SEPARATED__OWNER_IDENTIFICATION_DECISIONS_REQUIRED_BEFORE_IMPLEMENTATION`

Accepted candidate: `afb1cffeba207368b78c8ac4b93958285312eb53`.

## Acceptance basis

The candidate is accepted as zero-science design authority. It correctly preserves the accepted corrected-2018 data/runtime contract and the accepted 25-turn K/L evidence while separating two distinct redesign problems:

1. GovInv initialization: the historical/source-faithful `GovInv0=Ktarget` start is retained only as a numerical baseline; because firm capital is `Kt_supply+GovInv`, the accepted positive private supply implies mechanical overshoot. The residual candidate `max(Ktarget-Kt_supply_initial,0)` is correctly classified as algebraically coherent but not yet scientifically identified because the private-capital observation point and the household-asset-to-MU bridge are unresolved.
2. Labor normalization/reference: the source chain distinguishes household efficiency labor, one population multiplication inside `Lt_seperate`, destination-origin `Lt_mat`, and destination aggregate firm labor. The candidate correctly finds no evidence of a second population multiplication. The very large `firm_Lt_supply/N0` ratios are therefore not interpretable as observed employment excess; they arise from comparing unnormalized destination efficiency-labor levels against a resident-population proxy with no common target normalization.

The candidate also correctly separates GovInv initialization from any future controller redesign. No damping/controller objective is frozen here.

## Labor-reference acceptance

The following classifications are accepted:

- `L0=N`: transparent population-proxy baseline only, not observed workplace employment and not yet commensurate with firm efficiency labor.
- `L1`: a geography/GDP-per-capita source-inspired migration-adjusted reference is mathematically feasible only after an explicit normalized exogenous kernel is chosen; literal `Lt_seperate` cannot be reproduced from geography/GDP per capita alone because it also depends on endogenous `Ct` and `wjt`.
- `L2`: employment-rate-scaled population is not currently authorized because a hash-bound, year-aligned employment/labor-force data authority has not been accepted.
- `L3`: normalized migration shares combined with an independently fixed national labor aggregate are structurally promising, but both the national aggregate and share kernel remain Owner/data choices.

## Accepted sequencing

The lowest-risk dependency order is accepted:

`freeze Y/K/N/alpha -> choose labor reference and national-total contract -> recompute same-year Z and initial price receipt -> if authorized, run one labeled initialization household observation -> identify private K supply -> choose GovInv initialization -> separately decide GovInv controller -> only then run a new bounded trajectory`.

## Remaining Owner decisions

No implementation task is authorized automatically because the remaining choices are substantive scientific/calibration decisions. At minimum the Owner must decide:

- whether to authorize a normalized migration-adjusted labor reference and, if so, its kernel and national labor total;
- whether to introduce external province employment/labor-force data;
- the private-K observation contract and asset-to-MU bridge used by any residual GovInv initialization;
- whether the next capital route should be G1 residual initialization or another externally justified G2/G3 route;
- whether controller redesign should follow only after an initialization-only validation.

## Scientific boundary

No scientific/model call was made in the candidate. No production parameter, equation, bound, controller, grid, HJB/KFE implementation, labor allocation rule, or GovInv rule was changed. `Results eligibility=FALSE`.
