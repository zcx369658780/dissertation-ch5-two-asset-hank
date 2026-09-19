# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`INTERIOR_A_ZERO_DRIFT_SWITCHING_OWNER_ADOPTED__IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Owner adoption

Owner explicitly adopted the interior-`a` zero-drift switching law:

`docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md`.

The adopted law applies at interior illiquid-`a` nodes with a strict backward-positive / forward-negative drift crossing under the same existing liquid branch/active set and transfer regime. It imposes `g_a=0`, sets `d_Z=-r_a a`, uses unchanged D3 KKT for the switching shadow, requires the shadow inside the closed one-sided derivative interval, preserves the liquid-axis law, and enters the existing Hamiltonian comparison only after all frozen legality checks pass.

This is a corrected-diagnostic law only. Source-faithful/production paths remain frozen.

## Active Builder task

`tasks/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_20260919.md`.

The task authorizes:

1. minimal implementation of the adopted interior-`a` switching law in the corrected-diagnostic route;
2. focused tests and exact cell100 regression;
3. exactly one fresh accepted-V2 checkpoint-2 policy-map attempt;
4. if and only if all 800 cells succeed, at most one Q2 assembly and one checkpoint-2 Bellman/value/policy/operator/cycle diagnostic evaluation.

It authorizes zero V2->V3 HJB updates, zero terminal topology/KFE/SVD, zero MATLAB/production/GE/annual/IRF/Results and zero scientific retries.

## Frozen runtime facts

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Checkpoint 1 remains the last complete same-value checkpoint until a new complete V2 map exists:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`;
- V1->V2 direct residual `1.9012569296705806e-14`;
- backward error `2.5514110567283015e-16`.

No P2/u2/Q2 or B2/D2/stability/cycle/topology/KFE object currently exists.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain unauthorized.
