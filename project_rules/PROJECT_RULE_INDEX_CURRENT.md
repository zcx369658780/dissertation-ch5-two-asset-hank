# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`K1A_BOUNDED_INTEGRATION_PARTIAL_ACCEPTED__VALIDATOR_REPAIRED__SYMMETRIC_AB_RERUN_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN.md`。
最新 accepted bounded-integration candidate：`f57fec4d66bb82d48dc02bed775761ec194e0084`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

Owner 已冻结 K1A runtime comparison：equal-share `beta_distance=0` 对 pure-geographic `beta_distance=2`，两者 `beta_return=0`；K1B `beta_return=.5` 仅预注册。K1A household payoff 继续使用 current source-used/clipped `ra` 作为 `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`。theta 固定、source-faithful labor、smoothing OFF、C1 `GovInv=max(Ktarget-Kprivate,0)` 均保持。

前一 bounded task 的实现与 Path B 25-turn evidence 已接受，但 Path A 在完成 turn 1 后被 task-wrapper 中遗留的 legacy `rah` validator assertion 阻断。由于 scientific state 已推进，Builder 正确地没有重跑。该 assertion 已作为 zero-science provenance defect 修正为对 prior completed K1A same-`S` allocation 的验证；没有改变经济方程、参数、容差或 solver。

当前 symmetric rerun task 只允许在 repaired validator 下，从 identical accepted initialization 重新运行两条 preregistered K1A paths，每条最多25 turns。不得改变 beta、payoff bridge、labor、C1、bounds、solver/tolerance/grid；不得进入 K1B/K2、standalone KFE、annual/GE/IRF/Results。

已接受的 partial evidence 还显示：806 个完成 province-turn 的 K1 quantity/rah same-`S` 与资本守恒均通过；Path B 25 turns 后仍未满足冻结 outer predicate；raw `ra0` pressure 仍严重，Path B `755/775` 高于 `.09`。corrected-2018 empirical finite-box upper-b leakage + MATLAB-style pinning 仍是独立 KFE blocker。

GitHub live main 是 repository-state authority；聊天不能替代 exact task。正式发布 task 时同一回复附 Codex startup prompt。
