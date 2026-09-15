# CH5 MP4C K1 J160 liquid-grid bounded precision sensitivity

## Terminal classification

`J160_LIQUID_GRID_PRECISION_UNRESOLVED__I40_HJB_INVALID_OPERATOR`

The frozen I40 HJB did not converge within maxit=100 and first violated the accepted `A2max<=0.01` operator-legality guard at iteration 94. Consequently the I40 KFE was not authorized, I80 was not started, and liquid-grid precision remains unresolved. There was no scientific retry or numerical tuning.

## Authority and frozen inputs

- Actual fresh-fetched baseline: `ec6b7941739ee405c026aa8faf5275ee8bfb0251`.
- Representative state: `rb=.02, ra=.0675, w=15.5, a=[0,100], b=[-2,20], J=160, Nz=2, h=1`.
- Accepted equations, source initialization, FOCs, selectors, boundaries, derivative floor, solver, tolerance `1e-7`, maxit `100`, mappings, guards, and economic parameters were unchanged.
- Input invariance PASS: only `grid.b` differs from accepted I20/J160 and between the fresh fixtures. Both fresh initial-value and baseline-labor arrays were independently constructed, finite, and not warm-started.
- One pre-science path engineering retry was consumed because the initial desktop cwd pointed at the Zotero workflow remote. It was corrected before any HJB call and did not change science.

## Reused I20/J160 reference

The accepted reference was reused without HJB or KFE runtime:

- HJB: converged, 16 iterations, final statistic `2.2613111383407158e-10`.
- `At=89.29782530984971`, `Bt=5.8102538288563`, `Ct=14.258799707659694`, `Lt=0.6280595704784232`.
- modal `a=94.33962264150944`, modal `b=2.6315789473684212`.
- `amax mass=0`, `bmax mass=0.0009774011966318837`.
- KFE residual `8.187894806610529e-16`; total mass `1`; raw density minimum `-1.549036611714108e-18`.

## Fresh I40/J160 result

- `db=22/39=0.5641025641025641`; `da=100/159=0.6289308176100629`.
- Exactly one HJB was run from fresh source initialization.
- Classification: `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`.
- `converged=false`; iterations used `100`; final `max(abs(Vnew-Vold))=1.86941660663958`.
- Maximum `A2max=0.5875978072484334`.
- First illegal iteration: `94`, where `A2max=0.5875978072484334` exceeded the frozen `0.01` guard. Iteration 95 was also illegal (`A2max=0.3297377626101176`).
- Minimum stored off-diagonal across the trajectory: `-138678.75940842906`.
- Scientific arrays remained finite and shape-valid `(40,160,2)`, but this does not override nonconvergence/operator illegality.
- KFE was not run; therefore `Ct/Lt/At/Bt`, modal values, endpoint masses, and marginals are unavailable for I40.

## I80/J160 status

I80 was not run. The I40 terminal numerical failure required STOP, so the authorized second HJB and conditional KFE remained unused. No I160 or other fallback grid was attempted.

## Precision comparisons

- I20→I40: unavailable because I40 has no admissible KFE receipt.
- I40→I80: unavailable because I80 was not run after the I40 terminal failure.
- No post-result numerical threshold was introduced.

Therefore the task cannot evaluate `Bt`, modal-b, full b-marginal, a-marginal spillover, or endpoint-mass refinement. The accepted I20 evidence still shows `bmax=20` nonbinding at the reference, but nonbinding behavior on a finer liquid grid was not established.

## Call ledger and interpretation

- HJB started/completed: `1/1` of budget 2.
- KFE started/completed: `0/0` of budget at most 2.
- I20 reference HJB/KFE: `0/0`.
- I80, I160, J320, J640, J1280 calls: all `0`.
- Scientific retries: `0`.
- Global outer, firm, MATLAB, K1B, K2, GE, downstream, shock, IRF, Results: all `0`.

Engineering verification: focused plus relevant accepted tests `27 passed`; `py_compile` PASS; `git diff --check` PASS; compact sealed manifest PASS with 8 entries totaling 98,128 bytes.

Bt precision, modal-b stability, b-marginal stability, a-marginal spillover, and the finer-grid bmax conclusion are all unresolved. There is no smallest defensible tested I from this task.

KFE caveat: only the accepted I20 standalone contaminated-row KFE is present. It retains raw signed floating-point entries and remains separate from the unresolved corrected-2018 finite-box/pinning issue.

Results eligibility=`FALSE`.

Exactly one next gate: `REVIEWER_J160_LIQUID_GRID_ROUTE_DECISION`.
