# Chapter 5 当前交接 — J160 provincial first-turn HJB viability active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_TASK_ACTIVE`。

最新 accepted liquid-grid candidate：`47fd56418500e42c24c50bcbf86d889c96db0ec5`。
Acceptance：`docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_ACCEPTANCE.md`。
Freeze：`docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY.md`。
Results eligibility=`FALSE`。

Practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. J160 cross-state confirmation passed; finer-J route was closed by accepted J640 policy/selector chatter. Finer-I route is now also closed because `I40/J160` failed to converge and became operator-illegal at iteration 94 under the frozen source-faithful HJB.

Do not continue I80/I160, do not increase maxit, and do not introduce damping/relaxation/line-search or tolerance/floor/selector changes. The practical-grid choice is numerical-authority by bounded robustness, not continuum-convergence authority.

Current exact task returns to multi-province integration without KFE. It must first recover the exact accepted first-turn per-province household input vector from prior mechanism/trajectory evidence. Expected 31 provinces. Raw provincial `wjt` must not be substituted for household composite `w`, and no firm/wage/return recalculation is allowed.

If the first-turn vector is unambiguous, run exactly one fresh HJB per province on I20/J160 with source-style initialization, tolerance `1e-7`, maxit `100`, and `A2max<=0.01`. KFE=0, scientific retries=0. Report exact failure provinces and consumed `(ra,w)` inputs if any; do not recalibrate within the task.

No global outer turn, firm runtime, wage recalculation, MATLAB, K1B/K2, GE, downstream, shock, IRF or Results execution is authorized. The corrected-2018 KFE finite-box/pinning blocker remains separate.
