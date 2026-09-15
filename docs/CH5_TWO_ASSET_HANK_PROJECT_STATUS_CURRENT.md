# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_TASK_ACTIVE`。

最新 accepted provincial candidate：`1e9c8c6416cbd732a44d739e19b40e838993e3d4`。
Reviewer acceptance：`docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md`。
Current freeze：`docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Accepted practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. Finer-J and finer-I escalation routes remain closed; no maxit/tolerance/damping/relaxation/line-search changes are authorized.

First-turn provincial HJB viability has now been tested on the exact accepted 31-province household input vector. Input authority PASS. HJB converged for 25/31 provinces; 天津、山西、江西、重庆、贵州、甘肃 were legal but nonconverged at frozen maxit=100. There were 0 illegal operators and 0 hard errors; all 31 maximum A2max values remained below 0.01. KFE=0 and no upstream mappings were recomputed.

All 31 real first-turn provincial states lie outside the previously tested standalone J160 rectangle while 25 converge, so support location alone cannot explain the six failures. No recalibration is authorized yet.

The active task performs instrumentation-only identical-input HJB replays for exactly the six failed provinces, one call each, to classify whether failures are slow/near-monotone, policy/selector chatter with value oscillation, floor-amplified, low-period, heterogeneous, or unresolved. KFE=0, scientific retries=0, no successful-province reruns.

The corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning KFE blocker remains separate and unresolved.
