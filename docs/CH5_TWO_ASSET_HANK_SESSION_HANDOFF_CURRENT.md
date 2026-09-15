# Chapter 5 当前交接 — first-turn six-failure HJB mechanism panel active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_TASK_ACTIVE`。

最新 accepted provincial candidate：`1e9c8c6416cbd732a44d739e19b40e838993e3d4`。
Acceptance：`docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md`。
Freeze：`docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. Finer-J route is closed by accepted J640 policy/selector chatter; finer-I route is closed by accepted I40 operator illegality. Do not increase maxit or add damping/relaxation/line search.

Accepted first-turn provincial viability used the exact sealed 31-province household input vector without rerunning firm, wage, or return mappings. Result: 25/31 HJBs converged. 天津、山西、江西、重庆、贵州、甘肃 were legal but nonconverged at maxit100. There were no illegal operators or hard errors, and all 31 A2max maxima were below 0.01. KFE was not run.

All 31 real provincial first-turn states are outside the earlier standalone rectangle while 25 still converge, so being outside that rectangle is not sufficient to explain failure. Recalibration is therefore not authorized yet.

Current exact task replays only those six failed provinces with identical accepted inputs and fresh initialization, exactly one HJB each, observation-only instrumentation, maxit100/tolerance unchanged. KFE=0, scientific retries=0, no successful-province reruns. It must classify each province and the six-province panel as slow convergence, policy/selector chatter, floor-amplified behavior, low-period recurrence, heterogeneous, or unresolved.

Use accepted first-turn receipts only for offline nearest-successful-neighbor comparisons. The corrected-2018 multi-province KFE finite-box/pinning blocker remains separate.

Owner has authorized ChatGPT Reviewer to make bounded local numerical/debug route decisions; structural model changes, major calibration changes, accepted-equation/guard changes, causal interpretation, and Results eligibility remain Owner authority.
