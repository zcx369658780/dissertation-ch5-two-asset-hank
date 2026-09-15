# Chapter 5 corrected-2018 KFE closure route freeze

Date: 2026-09-15.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Reviewer authority: L3 independent Reviewer / scientific-route authority.

## Route decision

Reviewer selects **Route B**: stop extending the local `(ra,w)` synthetic-basin map and return to the corrected multi-province integration main line.

The local-basin program has already answered the integration-relevant question at its present scope: the six first-turn HJB failures do not support a common upper-`b`, simple price-envelope, universal guard, or monotone local-basin explanation. The accepted four-pair topology is heterogeneous and includes a nonmonotone/interleaved pair. More interpolation points, adaptive bisection, more matched pairs, or denser basin mapping would primarily refine geometry without currently changing an integration decision. They are therefore not authorized.

## Why KFE is the next integration bottleneck

The corrected-2018 five-turn KFE attribution is already accepted under:

`FIVE_TURN_KFE_ATTRIBUTION_ACCEPTED__SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED__OWNER_BOUNDARY_DECISION_REQUIRED`.

Accepted evidence establishes, across all 62 province-turn objects in turns 4/5, the same finite-box upper-`b` leakage plus MATLAB-style dropped-equation/pinning algebra. The material source-free residual is concentrated in the dropped pin equation; off-pin residuals are machine scale. The implied balancing source is algebraic and is **not** an adopted household entry/exit mechanism.

Therefore the next scientific bottleneck is not another KFE run. It is the unresolved **Owner scientific choice about finite-domain/KFE closure semantics**. Production boundary/grid/source/pinning repair cannot be selected by Reviewer or Builder merely to obtain convergence or mass conservation.

## Immediate successor

Before any new KFE/HJB science, publish and execute one zero-science decision-enabling task:

`tasks/CH5_MP4C_2018_KFE_OWNER_DECISION_RECOVERY_AND_OPTION_MATRIX_ZERO_SCIENCE_20260915.md`.

The task must recover the exact historical/current definitions of deferred D1-D3 proposals from live repository authority/history, trace each proposal to source/equation consequences, and produce an Owner-ready option matrix. It must not adopt an option, invent a missing proposal, modify production science, or run a solver.

If D1-D3 cannot be recovered exactly from repository evidence, the report must say so and stop at the Owner gate rather than reconstructing them from memory.

## Frozen boundaries

- Accepted practical HJB grid remains `I=20,J=160,Nz=2,a=[0,100],b=[-2,20],h=1`, diagnostic only.
- Finer-J and finer-I routes remain closed.
- Accepted HJB equations, selectors, boundary laws, derivative-floor logic, sparse solve, tolerance, maxit, and A2max legality semantics remain unchanged.
- No `ra`/`w` clipping or recalibration change is authorized.
- No upper-`b` expansion, KFE boundary repair, source insertion, pinning transplant/removal, or production KFE change is authorized by this freeze.
- Standalone contaminated-row KFE evidence cannot substitute for corrected multi-province authority.
- Results eligibility remains `FALSE`.

## Runtime ledger

Reviewer route decision and publication use repository reads/writes only.
Scientific/model/solver runtime: `0`.

## Next gate

After the zero-science decision package is accepted, Owner chooses the finite-box/KFE closure semantics. Only then may Reviewer issue a bounded implementation/scientific-validation task consistent with that choice.
