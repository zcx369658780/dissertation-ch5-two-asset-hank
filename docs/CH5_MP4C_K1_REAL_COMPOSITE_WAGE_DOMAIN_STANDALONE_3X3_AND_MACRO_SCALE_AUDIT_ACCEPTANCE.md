# CH5 MP4C K1 — real composite-wage standalone 3×3 and macro-scale audit acceptance

Date: 2026-09-13.

Reviewer verdict:

`REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_ACCEPTED__REAL_WAGE_HJB_HEALTHY__B_UPPER_BOUNDARY_CAVEAT__MACRO_DIMENSIONAL_RELATION_UNRESOLVED`

Accepted candidate: `41993260d87387235a2e58cc9a93a8aa06b98515`.

## Acceptance basis

Independent review verified the candidate is exactly one commit ahead of baseline `f1f95f11effa3bfc22e2045da2b04030eb9891a9`. Changed paths are confined to the task-owned report, CURRENT closeout docs, compact evidence, focused test, and task-owned standalone validator/finalizer package. No accepted household scientific source, protected MATLAB source, model calibration, guard, HJB/KFE algorithm, grid, tolerance, derivative floor, or production path was modified.

Accepted execution facts:

- exact grid: `rb=.02`, `ra={.06,.0675,.07}`, household composite `w={13,15.5,18}`;
- nine fresh MATLAB-style initializations; only `inputs.r_a` and `inputs.wages[0]` vary;
- HJB `9/9`, all legal and converged in `13–24` iterations;
- no hard error, invalid transition matrix, or illegal iteration;
- KFE `9/9`, exactly once after each converged HJB;
- scientific retries `0`; engineering retries `0`;
- global outer, firm runtime, MATLAB runtime, K1B/K2, GE, downstream, shock, IRF, Results all `0`.

## Accepted real-wage-domain result

All nine points are `INTERIOR_A_DISTRIBUTION_CANDIDATE` with respect to the illiquid-asset `a` distribution. All three tested `ra` values remain interior across all three real composite-wage points.

Accepted aggregate ranges:

- `Ct=8.27777–11.10279`;
- `Lt=.672871–.708939`;
- `At=7.14335–7.33469`;
- `Bt=1.60951–4.69951`.

This materially differs from the old low-wage map and confirms that the household block's observed stationary geometry is strongly wage-domain dependent. The unobserved interval between `w=1.3` and `w=13` still prevents a continuous-frontier or monotonicity claim.

## Critical boundary caveat

The illiquid-asset classification is not sufficient to call these points globally healthy. At all nine points the liquid-asset marginal mode is at `bmax=5`, with material upper-bound mass. This is direct evidence that the current liquid-asset finite box may bind under the real composite-wage scale.

Therefore this acceptance does **not** freeze a fully admissible household health region and does **not** justify changing `wjt` or returning to full-model execution yet.

Consistent with Owner guidance, future grid review should prioritize economic domain bounds (`bmin/bmax`, `amin/amax`) before increasing precision counts `I/J`; `I/J` remain numerical-resolution parameters and should not be expanded materially without a separate precision sensitivity justification.

## Accepted macro-scale audit

The accepted same-state scale audit supports the following source-consistent magnitudes and transformations:

- raw provincial GDP: about `1,548.4–99,945.2` 亿元;
- GDP model object `Y0_MU = GDP_raw ×1000`;
- raw population multiplied by `100` into `N0_NU`;
- model output/population ratio `Y0_MU/N0_NU ≈ 32.22–151.03`;
- raw firm wage roughly `7.76–36.39`;
- guarded `wjt0=1.3` for all 31 provinces in the accepted initialization receipt;
- household composite wage roughly `13.84–18.52`;
- corrected Track-A capital also uses `×1000`;
- sector GDP shares divide by `100`;
- PIM initialization uses `K0=I0/.1`, recursive depreciation `.096`; firm investment uses a separate `.025` depreciation term;
- legacy export reverses GDP/capital by `÷1000` and population/labor by `÷100`.

No accepted chain proves a common monetary unit linking GDP/per-capita GDP, firm `wjt`, and household composite wage. Therefore the supported conclusion is:

`DIMENSIONAL_RELATION_UNRESOLVED`

It is not scientifically defensible to change `wjt` bounds directly from these magnitudes alone.

## Scientific boundary

This acceptance does not authorize:

- direct `wjt` range changes;
- return-mapping changes;
- normalization rescaling;
- HJB/KFE redesign;
- arbitrary enlargement of `I/J`;
- full multi-province rerun;
- Results use.

The standalone contaminated-row KFE remains distinct from the unresolved corrected-2018 multi-province finite-box upper-`b` leakage and MATLAB-style pinning blocker.

Results eligibility=`FALSE`.

## Exactly one next Owner gate

`OWNER_REVIEW_JOINT_WJT_RA_MACRO_SCALE_RECALIBRATION`

The next Owner review should jointly examine: wage-chain normalization, return mapping, macro scale, and asset-grid domain bounds. Given the observed `bmax` mode at all nine real-wage points, `bmax`/liquid-asset domain adequacy must be part of that review. `I/J` should remain near the original MATLAB level unless a separate numerical-resolution test later demonstrates otherwise.
