# Chapter 5 当前规则入口
更新：2026-09-17；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`
6. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_REPORT.md`
9. exact accepted V1/Q1/p1 artifacts and corrected selector/D2/HJB authority as needed.

Current status: `Q1_SOURCE_FREE_KFE_ACCEPTED__NONLINEAR_FIXED_POINT_DESIGN_BLOCKED_ON_OWNER_CONVERGENCE_LAW__PRODUCTION_UNCHANGED`。
Current active Builder scientific task: none. Owner decision required.
Results eligibility=`FALSE`。

Accepted nonlinear design freezes `V_n` as the only nonlinear state; same-value `P_n,u_n,Q_n` are derived checkpoint objects. The sequence is derivatives -> complete corrected policy map -> D2 Q_n -> stationary Bellman/stability metrics -> one fixed-Delta implicit HJB update only if convergence has not passed. KFE is terminal-only on final same-value Q*. `Delta=1000` remains fixed.

At most 100 total HJB updates are allowed for the call-725 corrected trajectory; accepted `V0->V1` consumed update 1, leaving at most 99. No damping, relaxation, adaptive Delta, parameter continuation, clipping, artificial diffusion, solver substitution or scientific retry is authorized.

Before any continuation runtime, Owner must freeze Bellman-residual threshold, value-change threshold/conjunction, policy/operator stability role/window, direct-solve backward-error bound, and non-exact cycle/oscillation rule. Historical `max|V_new-V_old|<1e-7` is provenance only.

Owner retains final authority over this convergence law, new economic laws, major calibration, production replacement, causal interpretation and Results eligibility. GitHub live main remains repository-state authority.
