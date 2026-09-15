# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ASSET_GRID_PRECISION_REEXECUTION_CANDIDATE_AWAITING_REVIEW`。

本轮 fresh baseline：`03f30ada29ef7cea8dd0ab8f27b090df607c0909`。Active task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION.md`。Results eligibility=`FALSE`。

R0 已 PASS：task-owned receipt extraction 支持实际 `I/J`，KFE 返回后先持久化完整 scientific arrays、raw density、grid supports 与 shape，再做 receipt validation/extraction。Accepted HJB/KFE solver、equations、parameters、bounds、mapping、guards、oracle 与 MATLAB source 均未改变。Focused tests=`17 passed`；R0 HJB/KFE=`0/0`。

Frozen P1 `I=20,J={40,80,160}` 已 fresh 执行 exactly once。HJB 3/3 legal/converged，KFE 3/3 numeric-returned/persisted/valid；scientific retries=0。`J80→J160` 仍有 `ΔAt=+0.69078957`、modal `a:92.4051→94.3396`、a-marginal CDF distance=`0.01462234`，没有 stabilization trend。

Terminal classification：`ILLIQUID_GRID_PRECISION_NOT_STABILIZED`。P2 trigger=false，P2 HJB/KFE=`0/0`。`At`、modal `a` 与完整 a marginal 未稳定；minimum defensible cross-state grid 未建立。

旧域到扩域的巨大 At jump 主要是 domain response：相近 spacing 下 J160 `At=89.2978`，远高于旧域约 `7.14–7.33`；但扩域内 finer-J component 尚未稳定。固定 I20 的 finer-J 点上，modal b 始终为 `2.6316`，bmax mass 最大 `0.0009774`，仅支持 tested P1 points 上 nonbinding，不支持 I-grid precision 结论。

唯一 next Reviewer gate：`FINER_PRECISION_ESCALATION`。不得自动运行 J320/J640、P2、full cross-state grid、recalibration、GE 或 Results。

Compact evidence：`docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution/`。Report：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_REPORT.md`。
