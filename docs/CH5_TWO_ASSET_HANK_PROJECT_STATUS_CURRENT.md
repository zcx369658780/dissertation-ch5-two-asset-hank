# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`V2_CELL185_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted implementation/reexecution

Reviewer accepted Builder candidate `fc9ac9464a0bcc0a1e4b6f2dafbd8795cf79bf6b`.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_ACCEPTANCE_20260919.md`.

The Owner-adopted interior-`a` switching law is correctly implemented. Focused tests passed `59/59`.

Cell100 is now closed by a selected admissible switching candidate:
- `q_b=0.012448197327813425`;
- `q_a=0.008962703432234596`;
- `d=-0.236841961910238`;
- canonical `g_b=g_a=0`;
- D3 KKT residual `0`.

## First new failure

The single fresh V2 map proceeds through cell184 and fails first at flat 185, `(5,9,0)`, physical `(-0.1578947368421053,4.7368421052631575,0.8)`.

Cell185 is interior in both asset dimensions.

The accepted liquid-`Z` candidates show an `a` strict crossing only after the liquid shadow is switched:

- backward-`a` liquid-`Z`: `g_a=+0.009287240997760404`;
- forward-`a` liquid-`Z`: `g_a=-0.005170298666228812`.

Current Owner authority explicitly forbids a simultaneously newly-created interior-`a` switch plus liquid-`Z` switch. Therefore the fail-closed result is correct under current law.

No complete P2/u2/Q2 or checkpoint-2 B2/D2 object exists.

## Active zero-science adjudication

`tasks/CH5_MP4C_2018_KFE_D123_V2_CELL185_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_20260919.md`.

The task asks whether a joint `g_b=0, g_a=0` interior-interior switching candidate with endogenous `(q_b,q_a)` is mathematically/scientifically supported.

It may use static authority/evidence and scalar algebra only. It may not execute selector/root/policy-map/D2/HJB/KFE/MATLAB/downstream work and may not adopt or implement a new law.

## Frozen checkpoint facts

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Checkpoint 1 remains the last complete same-value checkpoint:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain unauthorized.
