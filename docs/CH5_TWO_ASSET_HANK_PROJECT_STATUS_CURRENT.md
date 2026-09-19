# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`V2_CELL100_FROZEN_LOCAL_KKT_INCOMPATIBILITY_CONFIRMED__OWNER_SCIENTIFIC_DECISION_REQUIRED__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。
当前 active Builder task：无。

## Latest accepted repair/reexecution

Reviewer accepted Builder candidate `19e12ff6c87b2c08490883851e7c50ef958b9c3d`.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_V2_LOWER_B_ACTIVE_NEGATIVE_BACKWARD_A_SELECTOR_REPAIR_AND_CHECKPOINT2_REEXECUTION_ACCEPTANCE_20260919.md`.

The accepted selector repair closes the predecessor implementation omission:
- active lower-b negative-transfer screening now uses the lower-face domain `q_b >= p_b`;
- both authority-backed negative-transfer `a` derivative directions are represented;
- upper-b logic remains distinct;
- focused tests passed `53/53`;
- source-faithful/production code remains unchanged.

## Accepted checkpoint-2 finding

The single fresh repaired V2 remap again stops first at flat F index 100, `(i_b,i_a,i_z)=(0,5,0)`, physical `(-2.0,2.6315789473684212,0.8)`.

Cells 0-99 are selected-policy identical to the predecessor attempt with maximum numeric change 0.

Cell100 now contains the complete eight-case frozen census and zero admissible comparisons. The newly restored active lower-b / negative / backward-`a` case converges at `q_b=0.012457851515416401`, but gives `g_a=0.00670682022114244` and fails the frozen backward-direction condition. The negative/forward-`a` case converges at `q_b=0.012447419227151839`, but gives `g_a=-0.0005429159000894801` and fails the forward-direction condition. The remaining cases are rejected by the already frozen primal/KKT/sign/no-root rules.

Accepted local classification:

`ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`.

This does not establish global nonlinear HJB nonexistence. It establishes that the currently frozen corrected local branch/KKT law cannot produce an admissible policy at this accepted V2 cell.

## Frozen runtime facts

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Checkpoint 1 remains the last complete same-value checkpoint:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`;
- V1->V2 direct residual `1.9012569296705806e-14`;
- backward error `2.5514110567283015e-16`.

No P2/u2/Q2, B2/D2/stability/cycle, topology or terminal KFE object exists.

Owner nonlinear law remains frozen unless Owner changes it: Bellman `<=1e-8` and value change `<=1e-7` at the same checkpoint; fixed `Delta=1000`; backward error `<=1e-12`; frozen cycle rules; no damping/relaxation/adaptive Delta/continuation/clipping/artificial diffusion/solver substitution/scientific retry/post-hoc tolerance tuning.

## Current Owner gate

The implementation omission is closed. Any next attempt to pass cell100 would require a substantive scientific/numerical choice outside current frozen authority, for example changing a boundary/KKT law, finite-domain/discretization contract, or trajectory/initialization construction.

Reviewer must not choose among those alternatives silently.

Until Owner chooses a new scientific route, no new selector/root/policy-map/D2/HJB/KFE/MATLAB/downstream scientific task is active.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain unauthorized.
