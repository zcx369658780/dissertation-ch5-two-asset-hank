# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。
当前 active Builder task：无。

## Accepted adjudication

Reviewer accepted Builder candidate `3a3df94bd80874d531d58f3710bc82d2069aa619` as:

`ADJUDICATED__SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_V2_CELL185_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_ACCEPTANCE_20260919.md`.

## Accepted cell185 finding

Cell185 is interior in both assets. Its accepted liquid-`Z` candidates create a strict post-liquid illiquid-drift crossing:

- backward-`a`: `g_a=+0.009287240997760404`;
- forward-`a`: `g_a=-0.005170298666228812`.

A simultaneous coupled closure is statically supported.

At cell185:

- `d_ZZ=-0.42626460578345887`;
- D3 ratio `q_a/q_b=0.7200216108914285`;
- exact joint interval
  `q_b in [0.011790364625750628,0.011910163904713082]`;
- this interval lies inside the liquid derivative interval;
- fixed-`d_ZZ` liquid equality changes sign from
  `-0.023007467717380714` to `+0.041147374843733764`;
- the equality is strictly increasing.

Therefore exactly one coupled local solution of `g_b=g_a=0` exists statically.

## Authority boundary

The joint law is compatible with existing D1/D2/D3 and one-axis switching laws, but it is not already authorized by them. It is a new coupled derivative-selection law and requires explicit Owner adoption.

No implementation, policy-map, D2, HJB or KFE runtime is active.

## Frozen runtime facts

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Checkpoint 1 remains the last complete same-value checkpoint:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`.

Cell100 is closed by the adopted one-axis interior-`a` switch. Cell185 remains the first fail-closed V2 object until Owner adopts or rejects the joint law.

No complete P2/u2/Q2 or B2/D2/stability/cycle/topology/KFE object exists.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain unauthorized.
