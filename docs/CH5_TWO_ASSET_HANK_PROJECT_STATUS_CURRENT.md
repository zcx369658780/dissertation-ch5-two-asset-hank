# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_ACTIVE`。

最新 accepted blocked local-basin candidate：`06b427f4f0c705a17c0d064a5f508c7e3e72ccce`。
Reviewer acceptance：`docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_ACCEPTANCE.md`。
Current freeze：`docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION.md`。
Results eligibility=`FALSE`。

Accepted practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. Finer-J/finer-I routes remain closed; no maxit/tolerance/damping/relaxation/line-search changes are authorized.

The prior local-basin run passed pair input authority and executed exactly 12 fresh HJB probes with endpoint reruns=0, KFE=0 and scientific retries=0. Raw terminal sequence was 山西→河北 C/C/C, 重庆→河北 C/C/C, 江西→安徽 F/C/C, 贵州→四川 C/F/C.

Formal topology is not yet accepted because the task-owned receipt aggregator mixed a post-convergence implicit system matrix into the A2max maximum. The exact maximum scientific source-generator A2max was not persisted. All scientific iteration operators are evidenced as preceding the sole erroneous `iterations+1` observation, but the required exact receipt cannot be reconstructed offline.

The active task repairs only this receipt boundary and reexecutes exactly the same 12 sealed synthetic points once. No new pairs, interpolation fractions, endpoint reruns, adaptive bisection, calibration/mapping change, KFE, outer model or Results runtime is authorized.

The corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning KFE blocker remains separate and unresolved.
