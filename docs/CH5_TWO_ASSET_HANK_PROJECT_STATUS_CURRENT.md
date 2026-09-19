# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoint before the active adjudication

The repaired selector candidate `19e12ff6c87b2c08490883851e7c50ef958b9c3d` is accepted.

The lower-b branch-coverage implementation defect is closed. The repaired V2 map still fails first at flat 100, `(i_b,i_a,i_z)=(0,5,0)`, physical `(-2.0,2.6315789473684212,0.8)`, after representing all eight frozen authority-backed cases.

Accepted local classification:

`ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`.

The two active lower-b negative-transfer roots exhibit the key interior-`a` crossing:
- backward-`a`: `g_a=+0.00670682022114244`;
- forward-`a`: `g_a=-0.0005429159000894801`.

This does not prove global HJB nonexistence.

## Owner-authorized active task

Owner has authorized a zero-science scientific-design adjudication:

`tasks/CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_20260919.md`.

The task asks whether the strict sign crossing at an interior illiquid-`a` node scientifically supports a zero-drift switching branch `g_a=0`, analogous in numerical role but not automatically identical in authority to the accepted interior-liquid `Z` branch.

It must derive the prospective law from the frozen D3 Hamiltonian/KKT equations, test cell100 compatibility using only persisted evidence and scalar algebra, compare against existing authority, and distinguish a missing switching law from finite-domain/boundary/trajectory alternatives.

This task is **zero science**:
- no selector/root/policy-map/D2/HJB/KFE/MATLAB/downstream calls;
- no source or numerical-law modification;
- no law adoption;
- no successor publication by Builder.

## Frozen runtime facts

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Checkpoint 1 remains the last complete same-value checkpoint:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`;
- V1->V2 direct residual `1.9012569296705806e-14`;
- backward error `2.5514110567283015e-16`.

No P2/u2/Q2, B2/D2/stability/cycle, topology or terminal KFE object exists.

Owner nonlinear convergence law remains frozen unless Owner later changes it.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain unauthorized.
