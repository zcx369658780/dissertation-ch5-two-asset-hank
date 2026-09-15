# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_CROSS_STATE_POST_SCIENCE_FINALIZER_REPAIR_TASK_ACTIVE`。

最新 accepted mechanism candidate：`b1c4897c72e3c11c1774ec59145865ae3f5fa6ca`。
Reviewer route decision：`docs/CH5_MP4C_K1_J160_CROSS_STATE_POST_SCIENCE_FINALIZATION_BLOCKER_ROUTE_DECISION.md`。
Current freeze：`docs/CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_AND_CLOSEOUT.md`。
Results eligibility=`FALSE`。

J640 mechanism diagnostic 已接受：identical frozen input 下 nonconvergence 精确复现，class=`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`。因此 finer-J escalation route 已关闭；J160 仅作为 provisional practical diagnostic grid 候选，不声称 continuum-converged 或 production-final。

上一 J160 bounded cross-state execution 已报告四个 fresh corner science 全部完成：HJB 4/4 legal/converged，KFE 4/4 completed，scientific retries=0；center J160 与 J20 references 均 reuse-only。四个 fresh 点均报告 amax mass=0、modal a interior、modal b interior，bmax mass 最大约0.0163，且没有 J640 式 HJB nonconvergence。

但 Builder 在首次离线 finalizer 中遇到 `ValueError: CDF comparison requires a common support`，因为 J20 references 使用 `a=[0,10], b=[-2,5]`，J160 使用 `a=[0,100], b=[-2,20]`。原任务只允许首个 HJB 前 engineering retry，因此 Builder 正确停止；没有 candidate commit。

Reviewer 将该事件定性为 post-science finalization/comparison blocker，而非 HJB/KFE scientific failure。当前任务禁止任何新 HJB/KFE runtime，只允许验证现有 raw evidence 后修复 task-owned offline finalizer：same-support CDF metric 必须保持不变；different-support 比较采用 union support + exterior CDF extension，并标记为 `DOMAIN_PLUS_GRID_CDF_DISTANCE`，不得解释为纯 precision distance。

Raw evidence expected at：`D:\ProjectTemp\ch5-mp4c-k1-j160-cross-state-evidence-20260915-001`。若 raw evidence integrity gate 不通过，必须 STOP，不得重跑 science。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。
