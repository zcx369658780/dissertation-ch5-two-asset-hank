# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Accepted corrected household route

The corrected route has accepted V0/Q0, V0->V1, V1/Q1, Q1 single closed class and pin-free/source-free unique Q1 invariant mass. The nonlinear design uses same-value `(P_n,u_n,Q_n)`, fixed `Delta=1000`, terminal-only KFE timing and the Owner-adopted Bellman/value convergence law.

Checkpoint 1 is not converged:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`.

The accepted V1->V2 direct solve is numerically valid, but V2 cannot currently produce a complete corrected policy map.

## V2 selector implementation omission — closed

The active lower-b negative-transfer pre-screen omission was attributed, repaired and reexecuted.

The repaired selector restores all eight frozen authority-backed cases at cell100. The map still returns `NO_ADMISSIBLE_POLICY`. Therefore the implementation omission is closed.

Accepted local classification:

`ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`.

## Current stage — interior-a switching adjudication

Owner has authorized a zero-science scientific-design gate:

`tasks/CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_20260919.md`.

Motivation: cell100 is interior in illiquid `a`, and the two active lower-b negative-transfer roots produce opposite-sign `a` drifts relative to their chosen one-sided derivatives:
- backward-`a` -> `g_a>0`;
- forward-`a` -> `g_a<0`.

The gate asks whether a mathematically correct upwind/viscosity treatment should contain a zero-`a)-drift switching branch `g_a=0`, analogous in numerical role to the already adopted liquid-`Z` branch, or whether the current failure is better attributed to boundary/domain/discretization/trajectory construction.

This gate performs no scientific runtime and does not adopt a law.

## Decision branches after adjudication

If an interior-`a` switching law is scientifically supported:
1. Owner explicitly adopts or rejects the prospective contract.
2. Only after adoption may Reviewer publish a minimal implementation/single-cell or bounded-map task.
3. Nonlinear continuation remains separately bounded under the existing convergence law unless Owner changes it.

If it is not supported:
- the frozen local incompatibility stands;
- Owner must choose another scientific route before further HJB runtime.

## Downstream closure

No P2/u2/Q2, B2/D2/stability/cycle or terminal KFE object exists.

Corrected production replacement, market clearing, GE/annual/dynamics/IRF and Results remain downstream and closed.

Capital/labor K1/C1/K1B/K2 routes remain deferred, not abandoned, and do not bypass the household fixed-point gate.
