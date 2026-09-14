# CH5 MP4C K1 — household asset-grid precision sensitivity freeze

Date: 2026-09-14

Status: `PRECISION_SENSITIVITY_FREEZE_ACTIVE`

## Accepted baseline

Accepted Stage A candidate: `32763fac5a7c4a04dc8278a9069443f35c7c7e3c`.

Accepted diagnostic convention remains:

- household monetary bridge: `h=1` diagnostic only;
- `amin=0`, `amax=100`;
- `bmin=-2`, `bmax=20`;
- economic rates, wages, returns, taxes, guards and household equations unchanged;
- `rb=.02`;
- real household composite-wage domain remains `w∈{13,15.5,18}`;
- return domain remains `ra∈{.06,.0675,.07}`.

Stage A cleared the liquid upper-bound pile-up at `bmax=20`, but `a` levels remain strongly grid-sensitive with `J=20` and `da≈5.26316`.

## Scientific purpose

Separate numerical discretization sensitivity from economic-domain effects before any production or full 3×3 use of the expanded asset domains.

The primary object is the illiquid dimension because `At` and modal `a` changed materially when `amax` expanded from 10 to 100 while `J` stayed 20.

The liquid dimension is secondary: `bmax=20` is retained because its endpoint pile-up cleared, but `I=20` precision must still be checked after illiquid precision is understood.

## Frozen representative state

Use exactly one representative central household input for the first sensitivity ladder:

- `rb=.02`
- `ra=.0675`
- `w=15.5`
- `a=[0,100]`
- `b=[-2,20]`

No warm starts.

## Stage P1 — illiquid-grid precision ladder

Hold `I=20` fixed and run fresh standalone HJB/KFE at:

- `J=20` — accepted Stage A reference only; reuse accepted evidence, do not rerun unless implementation receipt requires a no-science parser check;
- `J=40`;
- `J=80`;
- `J=160`.

Corresponding `da` values are:

- `100/19≈5.2631578947`;
- `100/39≈2.5641025641`;
- `100/79≈1.2658227848`;
- `100/159≈0.6289308176`.

`J=160` is deliberately close to the old-grid spacing scale without requiring exact `J=191` in the first ladder.

For each new point record HJB legality/convergence, KFE validity, `Ct,Lt,At,Bt`, modal `a/b`, endpoint masses, complete marginals, KFE residual and signed-density receipts.

## P1 stabilization rule

Do not fit a post-result tolerance. Publish raw pairwise changes:

- `J20→J40`
- `J40→J80`
- `J80→J160`

for `At`, `Bt`, `Ct`, `Lt`, modal `a`, `amax` mass, and selected marginal-distance metrics.

If the `J80→J160` change remains visibly material relative to the preceding refinement sequence, classify `ILLIQUID_GRID_PRECISION_NOT_STABILIZED` and stop before a full 3×3 grid. Recommend one bounded later precision escalation only; do not run it in the same task.

If `J80→J160` evidence is substantially more stable and the distribution remains interior/nonpathological, classify `ILLIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED` and proceed to Stage P2.

This is a descriptive stabilization rule, not a new production tolerance.

## Stage P2 — liquid-grid precision check

Only if P1 is provisionally stabilized.

Freeze the selected P1 reference at `J=160` and the same representative state. Run:

- `I=20` — accepted/new P1 state as reference, no duplicate science call if exact result already available;
- `I=40`;
- `I=80`.

`b=[-2,20]` remains unchanged.

Record the same household and marginal diagnostics and pairwise changes.

If `I=40→I=80` remains materially unstable, return `LIQUID_GRID_PRECISION_NOT_STABILIZED` and stop.

If it is descriptively stable and `b` remains interior, return `ASSET_GRID_PRECISION_PROVISIONALLY_STABILIZED_AT_REPRESENTATIVE_STATE`.

## No automatic full 3×3 in this task

Even if P1/P2 stabilize, do not run all nine `(ra,w)` points at the finer grid in this task. The next Reviewer gate will decide the smallest justified cross-grid confirmation set.

## Hard prohibitions

Do not change:

- `amax=100`, `bmax=20`;
- `amin`, `bmin`;
- `ra`, `rb`, wage;
- HJB/KFE equations;
- solver/tolerance/maxit;
- FOC/selector/boundary/derivative floor;
- `wjt` guard or `ra` mapping;
- monetary bridge `h=1`;
- any macro calibration.

No global model, firm, MATLAB, K1B/K2, GE, downstream, shock, IRF or Results runtime.

Results eligibility=`FALSE`.
