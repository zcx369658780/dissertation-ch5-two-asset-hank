# CH5 MP4C K1 — J160 liquid-grid bounded precision sensitivity freeze

Date: 2026-09-15

Status: `ACTIVE_FREEZE`

## Purpose

After J160 passed bounded cross-state confirmation as a practical household diagnostic grid, isolate the remaining local precision question in the liquid-asset dimension. This task must not reopen finer-J escalation or alter any economic calibration.

## Frozen representative state

- `rb=.02`
- `ra=.0675`
- household composite `w=15.5`
- `a=[0,100]`
- `b=[-2,20]`
- `J=160`
- `Nz=2`
- diagnostic household bridge `h=1`
- accepted HJB/KFE equations, initialization, FOCs, selectors, boundaries, derivative floors, solver, tolerance `1e-7`, maxit `100`, mappings, guards, and economic parameters unchanged.

## Accepted reference

Reuse accepted center `I=20,J=160` evidence without science runtime:

- HJB converged in 16 iterations
- `At≈89.29782531`
- `Bt≈5.81025383`
- modal `a≈94.33962264`
- modal `b≈2.63157895`
- `bmax mass≈0.0009774012`

## Exact liquid-grid ladder

Fresh-run only:

1. `I=40,J=160`
2. `I=80,J=160`

No other I/J points are authorized.

Corresponding liquid spacing:

- I20: `db=22/19≈1.1578947368421053`
- I40: `db=22/39≈0.5641025641025641`
- I80: `db=22/79≈0.27848101265822783`

## Runtime

Each new point uses fresh source initialization and exactly one HJB. Only a legal/converged HJB authorizes exactly one KFE. Scientific retries=0.

Maximum new calls:

- HJB=2
- KFE<=2
- accepted I20/J160 reference rerun=0
- J320/J640/J1280=0
- global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0.

## Required comparisons

Compare:

- `I20→I40`
- `I40→I80`

At minimum record and compare:

- HJB convergence/iterations/final statistic/A2max
- KFE validity/residual/raw density minimum/negative count
- `Ct,Lt,At,Bt`
- `Bt_pos/Bt_neg` if available
- modal `a`, modal `b`
- amin/amax/bmin/bmax masses
- full a- and b-marginals
- deterministic same-support marginal distances using the already accepted CDF methodology.

Because support remains identical across I20/I40/I80, these are true grid-precision comparisons rather than domain-plus-grid comparisons.

## Decision policy

No post-result fitted threshold is allowed.

If both fresh points are legal/converged, KFE-valid/nonpathological, bmax remains nonbinding, and the `I40→I80` change in `Bt`, modal-b and full b-marginal is descriptively small relative to `I20→I40`, terminal may be:

`J160_LIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED`

and the Builder must report the smallest defensible tested I for subsequent bounded diagnostics.

If `I40→I80` remains clearly material, terminal must be:

`J160_LIQUID_GRID_PRECISION_NOT_STABILIZED`

and STOP. Do not add I160 in the same task.

If HJB nonconvergence/chatter or serious KFE pathology appears at either point, report truthfully and STOP; no automatic mechanism replay or tuning is allowed.

## Prohibited

Do not alter domain, J, maxit, tolerance, HJB/KFE science, FOCs, selectors, boundaries, derivative floors, solver, wage/return mappings, guards, or economic parameters. Do not use warm starts. Do not run finer-J points, cross-state grids, global model, GE, or Results paths.

## Interpretation boundary

Even a PASS only supports a practical bounded liquid-grid density under the accepted MATLAB-faithful algorithm. It does not establish continuum convergence or production-final precision. Results eligibility remains `FALSE`.
