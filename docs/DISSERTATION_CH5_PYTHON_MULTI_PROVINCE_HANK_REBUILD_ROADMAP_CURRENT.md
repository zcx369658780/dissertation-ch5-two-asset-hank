# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Accepted route

The frozen source-faithful reference and separately governed corrected successor remain distinct. Owner-adopted corrected semantics include D1 upper numerical state constraints, D2 consumed-total-drift conservative assembly, D3 regularized-cost-consistent KKT, active lower-a zero-kink multiplier handling, and interior zero-liquid Z switching.

## KFE-D2C/D/E — accepted corrected household checkpoints

The corrected route has:
- accepted V0 800-cell policy map and Q0;
- accepted direct HJB update `V0->V1`;
- accepted V1 remap and Q1;
- Q1 exact-positive single closed class `[5,6,405,406]`;
- accepted pin-free/source-free unique Q1 invariant mass with rank/nullity `799/1`.

These remain household/operator diagnostics until nonlinear HJB convergence is established.

## KFE-D2F-A/B — nonlinear design and Owner convergence law accepted

Accepted nonlinear design freezes state `V_n`, same-value derived `(P_n,u_n,Q_n)`, fixed `Delta=1000`, terminal-only KFE timing and at most 100 total HJB updates.

Owner convergence law:
1. Bellman residual `<=1e-8`;
2. value change `<=1e-7`;
3. both at the same checkpoint;
4. policy/operator stability diagnostic only;
5. direct-solve backward error `<=1e-12`;
6. frozen exact and approximate period-2/3 cycle rules fail closed;
7. no damping, relaxation, adaptive Delta, continuation, clipping, artificial diffusion, solver substitution, scientific retry or post-hoc tolerance tuning.

## KFE-D2F-C — bounded nonlinear continuation fail-closed

Accepted checkpoint 1:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`.

The one authorized `V1->V2` direct solve passed:
- residual `1.9012569296705806e-14`;
- backward error `2.5514110567283015e-16`;
- V2 SHA-256 `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

The original V2 remap first failed at flat 100 with seven persisted cases.

## KFE-D2F-D — selector attribution and repair accepted

Zero-science attribution established that the active lower-b negative-transfer pre-screen incorrectly used an upper-face multiplier domain and omitted the negative/backward-`a` case.

The minimal corrected-selector repair is accepted in Builder candidate `19e12ff6c87b2c08490883851e7c50ef958b9c3d`.

A single fresh repaired V2 remap:
- leaves cells 0-99 selected policies byte/numerically unchanged at the reported comparison level;
- restores the complete eight-case frozen census at cell100;
- still yields zero admissible comparisons and `NO_ADMISSIBLE_POLICY`;
- does not reach P2/u2/Q2 or B2/D2.

The restored negative/backward-`a` case converges in liquid equality but yields positive `g_a` and is backward-direction inconsistent. The negative/forward-`a` case converges but yields negative `g_a` and is forward-direction inconsistent. The remaining regimes fail the already frozen primal/KKT/sign/no-root requirements.

Accepted local classification:

`ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`.

## KFE-D2F-E — Owner scientific decision gate

The implementation omission is closed. The current frozen corrected route cannot construct a complete V2 policy map under its adopted local branch/KKT law.

This does not prove global HJB nonexistence. It means the next step can no longer be an implementation repair under current authority.

Any successor must begin with an Owner scientific decision about which assumption or numerical contract may change, such as the boundary/KKT formulation, finite-domain/discretization choice, or trajectory/initialization construction. No successor scientific task is active until that choice is made.

## KFE-D3 — later production closure

Corrected multi-province production replacement, market clearing, GE/annual/dynamics/IRF and Results remain downstream gates with separate evidence and authority.

Capital/labor K1/C1/K1B/K2 routes remain deferred, not abandoned. They must not be represented as having bypassed the unresolved household fixed-point route.
