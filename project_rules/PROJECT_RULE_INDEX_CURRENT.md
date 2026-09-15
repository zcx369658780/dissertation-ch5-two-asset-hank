# Chapter 5 当前规则入口
更新：2026-09-15；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_FREEZE_CURRENT.md`
9. active exact task：`tasks/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY.md`

当前状态：`J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY.md`。
最新 accepted liquid-grid candidate：`47fd56418500e42c24c50bcbf86d889c96db0ec5`。
Results eligibility=`FALSE`。

Accepted practical household grid：`I=20,J=160,a=[0,100],b=[-2,20],h=1`。它通过了 bounded cross-state validation，但不代表 continuum convergence 或 production-final precision。

Finer-J route 因 accepted J640 `POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION` 关闭。Finer-I route 也因 `I40/J160` 在 maxit100 内不收敛并于 iteration94 首次违反 `A2max<=0.01` 关闭。禁止继续 I80/I160/J1280、增加 maxit、damping/relaxation/line-search 或修改 tolerance/floor/selector 来制造精度收敛。

当前 route 返回 multi-province integration：只验证 accepted first-turn province household inputs 在 practical grid 上的 HJB viability。必须从 repository accepted evidence 恢复 exact first-turn per-province input vector；不得重新运行 firm/wage mapping，也不得把 raw `wjt` 当 household composite `w`。

若 authority gate 通过，expected HJB exactly31，KFE=0，scientific retries=0；无 global outer/firm/wage/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results runtime。失败时只报告 exact province/input，不得在本 task 内 recalibrate。

Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker继续分离。

Owner 已授权 ChatGPT Reviewer 对 bounded numerical diagnostics 作预注册决策；结构方程、accepted equations/guards、主要经济校准、因果解释与 Results eligibility 仍由 Owner 决定。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
