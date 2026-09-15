# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACTIVE`。

最新 accepted provincial mechanism candidate：`ad4cdc8bbdf924c2ed06477abc10d1010038a5f7`。
Reviewer acceptance：`docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT.md`。
Results eligibility=`FALSE`。

Accepted practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. Finer-J and finer-I escalation routes remain closed; no maxit/tolerance/damping/relaxation/line-search changes are authorized.

Accepted first-turn provincial HJB viability remains 25/31 converged and 6 legal nonconverged. The six exact identical-input replays reproduced all six failures and established a heterogeneous numerical panel: 天津、山西、重庆、甘肃 are policy/selector chatter with value oscillation; 江西 is derivative-floor amplification after earlier switching; 贵州 has exact joint-selector period-2 recurrence without exact value recurrence. No reproducibility blocker occurred.

This evidence does not support a single universal HJB fix or immediate common recalibration. All six begin selector switching at iteration 2, but floor timing, oscillation strength, and recurrence evidence differ.

The active task is trace-only/offline. It must use the already sealed six-province iteration traces to localize the instability in `(b,a,z)` state space and determine whether switching/value argmax/floor/cycle signatures are boundary-concentrated, interior, mixed, heterogeneous, or unresolved. HJB=0, KFE=0, all model/science runtime=0.

No new `(ra,w)` experiment, calibration change, wage/return remapping, grid change, or HJB/KFE algorithm change is authorized.

The corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning KFE blocker remains separate and unresolved.
