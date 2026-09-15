# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_TASK_ACTIVE`。

最新 accepted liquid-grid candidate：`47fd56418500e42c24c50bcbf86d889c96db0ec5`。
Reviewer acceptance：`docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_ACCEPTANCE.md`。
Current freeze：`docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY.md`。
Results eligibility=`FALSE`。

Accepted practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20]` with diagnostic bridge `h=1`. J160 cross-state confirmation passed, but this is only practical bounded diagnostic authority, not continuum convergence or production-final precision.

Liquid-grid refinement route is now closed. Fresh `I=40,J=160` failed to converge by maxit=100 and first violated `A2max<=0.01` at iteration 94, with max A2max about 0.5876. KFE was correctly not run and I80 was not started. Reviewer therefore does not authorize I80/I160, longer maxit, damping, relaxation, line search, tolerance changes, or scientific-source changes to manufacture liquid-grid precision.

Together with accepted J640 policy/selector chatter on finer J, this establishes a practical numerical boundary: simply refining either asset dimension can move the source-faithful MATLAB HJB outside its stable regime. `I20/J160` is retained for bounded diagnostics because it passed the accepted five-state cross-state household check.

The route now returns to the multi-province model through an HJB-only first-turn viability test. The active task must recover the exact accepted province-level first-turn household input vector from prior repository evidence and, if unambiguous, run exactly one fresh HJB per province on the accepted practical grid. Expected HJB count is 31; KFE=0; no outer turn, firm/wage recalculation, MATLAB, GE, downstream or Results runtime.

The unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker remains separate and is not reopened by this HJB-only task.
