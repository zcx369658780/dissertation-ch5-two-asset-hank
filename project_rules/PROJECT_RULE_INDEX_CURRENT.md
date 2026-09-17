# Chapter 5 当前规则入口
更新：2026-09-17；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`
6. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`
7. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_REPORT.md`
8. `docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_ACCEPTANCE_20260916.md`
9. `docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_REPORT.md`
10. active task plus exact accepted V1/Q1/p1 artifacts and corrected selector/D2/HJB authority.

Current status: `OWNER_CONVERGENCE_LAW_ADOPTED__BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_ACTIVE__PRODUCTION_UNCHANGED`。
Current active Builder scientific task: `tasks/CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_20260917.md`。
Results eligibility=`FALSE`。

Owner-adopted convergence law:
- stationary Bellman residual `<=1e-8`;
- value change `<=1e-7`;
- both required at one checkpoint;
- policy/operator stability diagnostic only;
- normwise backward error for each direct solve `<=1e-12`;
- exact period `k>=2` recurrence fail-closed before convergence;
- approximate period-2/3 complete-window lag tests at `1e-8` fail-closed after primary convergence fails;
- no more than 100 total HJB updates, with `V0->V1` already consuming update 1;
- fixed `Delta=1000` and no damping, relaxation, adaptive Delta, continuation, clipping, artificial diffusion, solver substitution, scientific retry or post-hoc tolerance tuning.

The active runtime route starts from exact accepted V1/P1/u1/Q1, evaluates V1 first, and continues only as required. Ordinary rounds never execute KFE. Only an HJB convergence candidate may enter the accepted terminal topology plus pin-free/source-free KFE gate on the same Q*.

Owner retains final authority over new economic laws, major calibration, production replacement, causal interpretation and Results eligibility. GitHub live main remains repository-state authority.