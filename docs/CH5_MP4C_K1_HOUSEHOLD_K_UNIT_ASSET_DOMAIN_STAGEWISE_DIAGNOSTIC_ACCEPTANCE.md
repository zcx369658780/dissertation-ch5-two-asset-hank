# CH5 MP4C K1 — household k-unit asset-domain stagewise diagnostic acceptance

Date: 2026-09-14

Reviewer verdict:

`HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGE_A_ACCEPTED__LIQUID_BOUNDARY_CLEARED__ILLIQUID_LEVEL_PRECISION_SENSITIVITY_REQUIRED`

Accepted candidate: `32763fac5a7c4a04dc8278a9069443f35c7c7e3c`.

## Acceptance basis

Independent review verified that the candidate is exactly one commit ahead of baseline `9f6d99a32e8feb00cbae0a3a4749c331975fa587`, with changes confined to the task-owned report, CURRENT closeout docs, compact evidence, focused test, and task-owned validator/runner package. Accepted household scientific source was not modified.

Frozen Stage A was executed exactly as preregistered: diagnostic bridge `h=1`; `a=[0,100]`, `b=[-2,20]`, `I=J=20`; `rb=.02`, `ra={.06,.0675,.07}`, `w={13,15.5,18}`; nine fresh initializations; no warm start; no scientific retries; global/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results all zero.

All nine HJBs were legal and converged, and all nine authorized KFEs completed without material signed pathology. The maximum observed `A2max` remained below the frozen MATLAB legality threshold. Stage B was correctly not executed because no KFE-valid Stage A point had `modal b=bmax=20`.

## Accepted liquid-asset conclusion

The prior real-wage scan on `b=[-2,5]` had `modal b=5` in all nine points and substantial upper-bound mass. Under Stage A `b=[-2,20]`, all nine points have `modal b=2.6315789473684212`, exact `bmax` modal count is zero, and `bmax` mass is at most about `6.13e-08`.

Therefore the Stage A evidence supports:

`LIQUID_ASSET_UPPER_BOUNDARY_PILEUP_CLEARED_AT_BMAX_20_FOR_THE_TESTED_REAL_WAGE_GRID`

This is domain-diagnostic authority only. It does not establish production precision, full-model KFE validity, or general equilibrium admissibility.

## Accepted illiquid-asset conclusion

All nine `a` marginals are descriptively interior, but the level results are strongly precision/domain sensitive: `At≈84.02–88.86`, modal `a` is mostly `89.47`, `amax`-bin mass remains about `9.3%–17.4%`, and `da≈5.26316` is very coarse.

The move from the old-domain `At≈7.14–7.33` to the expanded-domain `At≈84–89` must not be interpreted as calibration improvement. It is evidence that the current illiquid level is not numerically stabilized with `J=20` over `[0,100]`.

## Reviewer decision on the next bounded numerical step

Under the Owner's standing authorization for small, local numerical calibration/debugging decisions, the next task is authorized without an additional Owner stop: a bounded precision-sensitivity diagnostic that keeps economic domains and all equations/parameters fixed while varying only numerical grid density.

The next task must first isolate illiquid-grid precision at one representative central state before any full 3×3 rerun. It must not change `amax=100`, `bmax=20`, rates, wages, returns, guards, or household equations.

Results eligibility=`FALSE`.

Standalone contaminated-row KFE remains distinct from the unresolved corrected-2018 multi-province finite-box upper-b leakage and MATLAB-style pinning blocker.
