# CH5 MP4C K1 — household k-unit asset-domain stagewise diagnostic report

Date: 2026-09-14

Task ID: `CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC`

## Terminal classification

`ASSET_DOMAIN_STAGE_A_BOUNDARY_CLEARED__PRECISION_SENSITIVITY_REQUIRED`

Stage A completed exactly as frozen. All nine HJBs were legal and converged, all nine authorized KFEs completed without material signed pathology, and no liquid marginal had its mode at exact `bmax=20`. The preregistered Stage B trigger was therefore false and Stage B scientific calls remained zero.

This is standalone household-domain diagnostic evidence only. `Results eligibility=FALSE`.

## Repository and execution identity

- Actual fresh-fetched baseline: `9f6d99a32e8feb00cbae0a3a4749c331975fa587`.
- Branch: `codex/ch5-mp4c-k1-household-k-unit-asset-domain-stagewise-20260914`.
- Fresh isolated worktree: `D:\ProjectTemp\ch5-mp4c-k1-household-k-unit-asset-domain-stagewise-20260914-001`.
- External raw evidence: `D:\ProjectTemp\ch5-mp4c-k1-household-k-unit-asset-domain-stagewise-evidence-20260914-001`.
- Compact evidence: `docs/evidence/ch5_mp4c_k1_household_k_unit_asset_domain_stagewise/`.
- Frozen oracle SHA-256: `F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8`.
- Frozen MATLAB source SHA-256: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.

## Input invariance and diagnostic convention

Temporary household bridge was exactly `h=1`: existing `w/C/Tt/a/b/At/Bt` numerics were used unchanged as diagnostic k-unit numerics. No macro rebase was applied. Relative to the accepted old-domain fixture, only `grid.a` and `grid.b` changed.

Stage A used `I=J=20`, `Nz=2`, `a=[0,100]`, `b=[-2,20]`, `da=100/19=5.2631578947368425`, and `db=22/19=1.1578947368421053`. The exact grid was `rb=.02`, `ra={.06,.0675,.07}`, `w={13,15.5,18}`. Nine distinct initial-value and baseline-labor objects were constructed through `source_initial_arrays`; no point used a warm start.

`alphac`, `a_bar`, derivative floor, drift tolerance, `ra/rb/gap/rho/delta/taxes`, HJB/KFE equations, FOC, selectors, solver, tolerance, iteration ceiling, `wjt` guard and `ra` mapping were unchanged.

## Stage A 3×3 matrix

Every cell is `HJB classification / KFE validity / modal b`:

| `ra \ w` | 13 | 15.5 | 18 |
|---|---|---|---|
| .0600 | CONVERGED / valid / 2.631579 | CONVERGED / valid / 2.631579 | CONVERGED / valid / 2.631579 |
| .0675 | CONVERGED / valid / 2.631579 | CONVERGED / valid / 2.631579 | CONVERGED / valid / 2.631579 |
| .0700 | CONVERGED / valid / 2.631579 | CONVERGED / valid / 2.631579 | CONVERGED / valid / 2.631579 |

HJB iterations were 9–13. Final `max|ΔV|` was `1.46493e-10–6.88552e-08`, below the frozen `1e-7` tolerance. Maximum observed `A2max` was `0.00118779–0.00163471`, below `HOMECRIT=.01`; no point had an illegal iteration or hard error.

## Stage A per-point receipts

Raw marginals, top-three bins, array/label shapes and all iteration legality records are retained in compact evidence. Values below are not rounded in `points.csv` or `point_receipts.json`.

| # | ra | w | iter | final `max|ΔV|` | max A2max | Ct | Lt | At | Bt | modal a | amax mass | modal b | bmax mass | KFE residual | density min / negative count |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | .0600 | 13 | 9 | 3.487e-08 | .001188 | 11.90096 | .640484 | 85.87328 | 4.00611 | 89.47368 | .107456 | 2.631579 | 3.576e-14 | 6.093e-17 | -1.771e-23 / 2 |
| 2 | .0600 | 15.5 | 10 | 1.365e-09 | .001195 | 13.29279 | .634895 | 84.85842 | 4.09743 | 89.47368 | .098477 | 2.631579 | 1.256e-09 | 9.530e-17 | -5.234e-20 / 8 |
| 3 | .0600 | 18 | 10 | 1.745e-09 | .001201 | 14.65679 | .629144 | 84.01876 | 4.24454 | 84.21053 | .093123 | 2.631579 | 6.134e-08 | 1.645e-16 | -0 / 0 |
| 4 | .0675 | 13 | 9 | 3.496e-08 | .001503 | 11.99795 | .626194 | 88.44015 | 4.14334 | 89.47368 | .157254 | 2.631579 | 0 | 6.989e-17 | -2.340e-19 / 25 |
| 5 | .0675 | 15.5 | 10 | 4.304e-09 | .001513 | 13.39060 | .621365 | 87.75417 | 4.15547 | 89.47368 | .143050 | 2.631579 | 6.511e-34 | 7.953e-17 | -3.638e-19 / 198 |
| 6 | .0675 | 18 | 10 | 6.863e-09 | .001520 | 14.74863 | .616373 | 87.12970 | 4.21815 | 89.47368 | .133158 | 2.631579 | 1.319e-13 | 7.219e-17 | -8.341e-21 / 102 |
| 7 | .0700 | 13 | 9 | 3.492e-08 | .001617 | 12.01217 | .621695 | 88.86351 | 4.19923 | 89.47368 | .173673 | 2.631579 | 0 | 4.909e-17 | -1.308e-18 / 215 |
| 8 | .0700 | 15.5 | 9 | 6.886e-08 | .001627 | 13.40479 | .617069 | 88.26838 | 4.18963 | 89.47368 | .155513 | 2.631579 | 3.482e-18 | 6.359e-17 | -4.352e-18 / 183 |
| 9 | .0700 | 18 | 13 | 1.465e-10 | .001635 | 14.76106 | .612296 | 87.70237 | 4.22959 | 89.47368 | .144251 | 2.631579 | -1.111e-30 | 1.085e-16 | -5.258e-19 / 348 |

## Stage B trigger

The only inspected trigger field was each converged/KFE-valid point's raw `kfe.distribution.modal_b`. All nine modes were exactly the interior grid value `2.6315789473684212`; none contained `20`. Therefore:

- `trigger=false`;
- triggering point count=0;
- Stage B initialization constructions=0;
- Stage B HJB=0 and KFE=0;
- no `bmax=50` fixture or scientific point was executed.

No post-result percentage threshold was introduced.

## Asset-domain conclusions

### Illiquid asset a

All nine points satisfy the preregistered `INTERIOR_A_DISTRIBUTION_CANDIDATE` rule: the exact modal bin is strictly interior. Eight modes are at `a=89.473684`, and one is at `a=84.210526`; no mode is at `amax=100`.

This does not establish production adequacy. `At` is `84.01876–88.86351`, while raw `amax`-bin mass is still `0.093123–0.173673`. The distribution is concentrated near the upper portion of an extremely coarse grid. The movement from old `At≈7.14–7.33` to new `At≈84.02–88.86` is a material finite-domain/discretization response, not a GE or calibration improvement. Independent precision sensitivity is mandatory.

### Liquid asset b

All nine points are `B_INTERIOR_DISTRIBUTION_CANDIDATE`. The mode moved from old exact `bmax=5` to interior `b=2.6315789473684212`. New `bmax=20` mass is at most `6.13381e-08` in raw signed evidence, versus old upper-bound mass `0.130896–0.683403`; interior b mass is at least `0.999999823`.

Under the frozen exact-modal trigger, the liquid upper-bound pile-up is cleared in Stage A. This is domain-diagnostic evidence only and does not prove accuracy at `db≈1.158`.

## Accepted old-domain comparison

All comparisons use the same `(rb,ra,w)` points from accepted `a=[0,10]`, `b=[-2,5]` evidence:

| Object | Accepted old range | Stage A range | Pointwise change |
|---|---:|---:|---:|
| HJB iterations | 13–24 | 9–13 | -15 to -4 |
| max A2max | .003837–.005246 | .001188–.001635 | lower at all points |
| Ct | 8.27777–11.10279 | 11.90096–14.76106 | +3.32670 to +3.86119 |
| Lt | .672871–.708939 | .612296–.640484 | -.085867 to -.032715 |
| At | 7.14335–7.33469 | 84.01876–88.86351 | +76.74838 to +81.52882 |
| Bt | 1.60951–4.69951 | 4.00611–4.24454 | -.58385 to +2.39660 |
| modal a | 7.36842 | 84.21053 or 89.47368 | moves with expanded/coarsened a-domain |
| modal b | exact 5 | interior 2.63158 | old endpoint pile-up cleared |
| bmax mass | .130896–.683403 | roundoff to 6.134e-08 | materially lower at all points |

KFE residual remains finite at `4.90873e-17–1.64473e-16`. Raw density minima are `-4.35176e-18–0`; negative-entry counts are 0–348, but all negatives are within the preregistered `100*epsilon` rounding band. No signed mass was clipped.

## Call ledger and scientific boundary

- Stage A: HJB started/completed=`9/9`; KFE started/completed=`9/9`.
- Stage B: HJB=`0`; KFE=`0` because trigger=false.
- Stage A initialization constructions=9; scalar labor roots=7200. Stage B values are zero.
- Scientific retries=0.
- Engineering retries=1, consumed before the first HJB for a focused static-test false positive; science was unchanged.
- Global outer, firm, MATLAB, K1B, K2, GE, downstream, shock, IRF and Results calls/writes all equal 0.

The accepted standalone contaminated-row KFE remains the only KFE authority used here. Corrected-2018 multi-province finite-box upper-b leakage and MATLAB-style pinning remain unresolved and separate. No Results or production claim is authorized.

## Exactly one next gate

`OWNER_REVIEW_ASSET_DOMAIN_STAGE_A_ACCEPTANCE_AND_PRECISION_SENSITIVITY`

STOP for independent ChatGPT Reviewer ACCEPT/REJECT. Do not merge main and do not publish a successor task.
