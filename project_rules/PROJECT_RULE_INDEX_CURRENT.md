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
9. `docs/CH5_MP4C_K1_J160_CROSS_STATE_POST_SCIENCE_FINALIZATION_BLOCKER_ROUTE_DECISION.md`
10. `docs/CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_FREEZE_CURRENT.md`
11. active exact task：`tasks/CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_AND_CLOSEOUT.md`

当前状态：`J160_CROSS_STATE_POST_SCIENCE_FINALIZER_REPAIR_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_AND_CLOSEOUT.md`。
最新 accepted mechanism candidate：`b1c4897c72e3c11c1774ec59145865ae3f5fa6ca`。
Results eligibility=`FALSE`。

Accepted J640 mechanism：`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`。Finer-J escalation route 已关闭；J160 只作为 provisional practical diagnostic grid 候选，不得宣称 continuum-converged 或 production-final。

上一 J160 cross-state execution 已完成四个 authorized fresh science points，但没有 candidate commit：首次 offline finalizer 因 J20/J160 support 不同而失败。Reported HJB=4/4 legal/converged、KFE=4/4 completed、scientific retries=0；center J160 与 J20 references reuse-only。该 raw science 仅可在 successor task 完成 integrity gate 后用于 closeout。

当前 exact task 是 zero-science finalizer repair：HJB=0、KFE=0。必须验证 raw evidence `D:\ProjectTemp\ch5-mp4c-k1-j160-cross-state-evidence-20260915-001` 后，只修 task-owned offline CDF/finalizer。Same-support metric 语义必须不变；different-support 使用 union interval + exterior CDF extension，J20→J160 距离必须标记 `DOMAIN_PLUS_GRID_CDF_DISTANCE`，不得当作 pure precision metric。

禁止任何 science rerun、J320/J640/J1280、I-grid ladder、domain/parameter change、recalibration、global model 或 Results runtime。若 raw evidence integrity gate 失败，必须 STOP。

Owner 已授权 ChatGPT Reviewer 对类似 bounded numerical/engineering closeout 直接做预注册决策；结构方程、accepted equations/guards、主要经济校准、因果解释、Results eligibility 的变更仍由 Owner 决定。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
