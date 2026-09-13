# CH5 MP4C K1 — k-unit normalization and asset-domain recalibration freeze

Date: 2026-09-14.
Status: `OWNER_APPROVED_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_FIRST`.

## Owner decisions and hypotheses

1. The current `amax=10` and `bmax=5` are regarded as too small for the intended household asset domain.
2. Owner proposes expressing monetary/asset quantities in `k` units (thousands of currency units) as the preferred normalization target, subject to a source-consistent dimensional audit before implementation.
3. Owner proposes `amax=100` under the k-unit interpretation as the first illiquid-asset upper-domain target. This is a household state-grid upper bound, not a direct cap on provincial aggregate `At`; any aggregate implication must be derived from the stationary distribution.
4. `bmax` also requires expansion, but no numerical replacement is frozen yet. The next task must derive a scientifically defensible candidate from source scaling, accepted household distributions, and the intended k-unit normalization rather than inventing a value.
5. The original MATLAB version is treated as a useful successful reference implementation, but its dimensional consistency is not assumed without verification.

## Verified original-MATLAB scaling facts to preserve in the audit

The designated original MATLAB source uses `param.GDP_multiplier=1000` and `param.POP_multiplier=100`; the source comments call this a comparatively good version. `load_GDPdata.m` multiplies GDP/capital by `GDP_multiplier` and population by `POP_multiplier`, while export routines divide GDP/capital by the GDP multiplier and population/labor by the population multiplier.

These facts do not by themselves prove that all household variables are in thousands of currency units. The next task must trace the complete dimensional chain.

## Scientific boundary

This stage is a design/audit gate before implementation. Do not modify HJB/KFE equations, `wjt` guards, return mapping, calibration, asset grids, or runtime model behavior yet.

The audit must distinguish:

- monetary unit normalization;
- population unit normalization;
- aggregate provincial stocks/flows;
- per-capita quantities;
- household individual asset-grid states `a,b`;
- stationary aggregates `At,Bt`;
- firm wage `wjt`;
- household composite wage `w`;
- consumption, transfers, investment, capital, GDP, productivity and labor variables.

A pure unit conversion is allowed in the design only if every dimensionful equation and parameter is transformed consistently. Parameters whose numerical values change under a monetary-unit rescaling must be identified explicitly; no assumption of invariance is allowed.

## Asset-domain rule

`I` and `J` remain precision controls and are not the first adjustment margin. Domain bounds must be reviewed first. However, increasing `amax` or `bmax` while holding `I/J` fixed changes spacing, so the design must calculate the implied `da/db` and flag when a later independent precision-sensitivity gate is required.

Owner-proposed first target: `amax=100` under k units. `amin=0` remains the economic lower bound unless the source/economic authority proves otherwise. `bmin` and the new `bmax` require explicit design review.

## Recalibration principle

If the final k-unit normalization is accepted, upstream objects must be transformed jointly. Do not separately rescale `w`, `wjt`, `ra`, GDP, investment, capital or transfers to force convergence. Return rates such as `ra/rb` are rates and should remain dimensionless unless a source equation proves otherwise; level variables and dimensionful cost/transfer parameters require explicit transformation analysis.

## Required next gate

`CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT`

The design audit must finish before any implementation/runtime recalibration.

Results eligibility=`FALSE`.
