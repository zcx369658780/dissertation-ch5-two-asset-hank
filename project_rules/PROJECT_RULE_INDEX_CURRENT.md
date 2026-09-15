# Chapter 5 当前规则入口
更新：2026-09-15；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_ACCEPTANCE.md`
9. `docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`
10. `docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`
11. active exact task：`tasks/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY.md`

当前状态：`J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY.md`。
最新 accepted cross-state candidate：`0430057603da6fb83ae4731ce4139def149c090c`。
Results eligibility=`FALSE`。

Accepted J640 mechanism：`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`。Finer-J escalation route 已关闭，不得增加 maxit、damping/relaxation/line search 或继续 J1280/J2560 制造 convergence。

Accepted J160 cross-state authority：`I=20,J=160,a=[0,100],b=[-2,20]` 在五个 bounded real-wage/return states 上科学可解释；四个 fresh corner HJB/KFE 4/4通过，fresh amax mass全部0、modal a/b内部、最大 bmax mass约0.01630。因此 J160 支持 practical bounded diagnostic grid，但不代表 continuum convergence 或 production-final precision。

J20→J160 marginal metric 因 domain 与 discretization 同时变化，固定标记为 `DOMAIN_PLUS_GRID_CDF_DISTANCE`，不得用作 pure grid precision claim。

当前 exact task 只验证 liquid-grid precision：固定 center economics、`J=160` 与 domain，复用 accepted `I20/J160`，fresh exactly 运行 `I40/J160`、`I80/J160`。每点 HJB exactly once；legal/converged 时 KFE exactly once；scientific retries=0。若 I40→I80仍明显 material，STOP，不得同任务追加 I160。

禁止 J change、domain/parameter change、recalibration、HJB/KFE modification、global model 或 Results runtime。

Owner 已授权 ChatGPT Reviewer 对类似 bounded numerical diagnostics 直接做预注册决策；结构方程、accepted equations/guards、主要经济校准、因果解释、Results eligibility 的变更仍由 Owner 决定。

Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker 继续分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
