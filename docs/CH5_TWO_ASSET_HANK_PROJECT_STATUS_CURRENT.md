# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`INTERIOR_A_ZERO_DRIFT_SWITCHING_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。
当前 active Builder task：无。

## Accepted adjudication

Reviewer accepted Builder candidate `d4ed09015f184ab8e4a39e1de019c33b8868cd20` as:

`ADJUDICATED__INTERIOR_A_ZERO_DRIFT_SWITCHING_BRANCH_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_ACCEPTANCE_20260919.md`.

## Accepted scientific finding

The repaired V2 cell100 complete eight-case census remains locally incompatible under the currently frozen one-sided `a` direction law, but the incompatibility has a structured strict crossing:

- backward-`a` candidate -> `g_a=+0.00670682022114244`;
- forward-`a` candidate -> `g_a=-0.0005429159000894801`.

A prospective interior-`a` zero-drift branch is statically supported.

At cell100:

- `d_Z=-r_a a=-0.23684196191023801`;
- D3 gives `q_a/q_b=0.72000010894821909`;
- `q_a in [p_a^F,p_a^B]` maps to
  `q_b in [0.012440285887428097,0.012546045881996438]`;
- the entire interval satisfies lower-b active `q_b>=0.012333311206716577`;
- fixed-`d_Z` liquid equality is strictly increasing and changes sign from
  `-0.0039748658728543454` to `+0.048890867998731984`.

Therefore exactly one compatible local crossing exists statically.

## Authority boundary

The branch is compatible with existing D1/D2/D3, but it is not already authorized by the liquid-`Z` law or lower-`a` zero-kink law. It is a new interior-`a` derivative-selection law and requires explicit Owner adoption.

No implementation, root call, policy map, D2, HJB or KFE runtime is active.

## Frozen runtime facts

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Checkpoint 1 remains the last complete same-value checkpoint:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`;
- V1->V2 direct residual `1.9012569296705806e-14`;
- backward error `2.5514110567283015e-16`.

No P2/u2/Q2 or B2/D2/stability/cycle/topology/KFE object exists.

## Current Owner gate

Owner must explicitly adopt, modify or reject the prospective interior-`a` zero-drift switching contract before further corrected-route runtime.

Until that decision, active Builder task = none.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain unauthorized.
