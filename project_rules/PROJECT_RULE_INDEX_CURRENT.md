# Chapter 5 当前规则入口
更新：2026-09-15；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_20260915_LOCAL_BASIN_ACCEPTED.md`
6. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
7. `docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_ACCEPTANCE.md`
9. `docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md`
10. `docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_ACCEPTANCE.md`
11. `docs/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACCEPTANCE.md`
12. `docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_ACCEPTANCE.md`
13. `docs/CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT_ACCEPTANCE.md`
14. `docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`

当前状态：`LOCAL_BASIN_REEXECUTION_ACCEPTED__NEXT_REVIEWER_ROUTE_PENDING`。
当前 active Builder task：无。
最新 accepted Builder candidate：`c994cee14b5958e47078bd7281acffcbe56797e5`。
Results eligibility=`FALSE`。

Accepted practical household grid：`I=20,J=160,a=[0,100],b=[-2,20],h=1`，仅用于 bounded diagnostics。Finer-J / finer-I routes 均关闭；禁止通过增加 maxit、damping/relaxation/line-search 或 tolerance/floor/selector/solver 修改制造 convergence。

Accepted first-turn provincial HJB：25/31 converged、六省 legal nonconverged。Accepted temporal mechanism、value-argmax localization、coordinate-resolved selector/floor footprint 均显示异质性；successful controls 也有 substantial upper-b activity，因此 common failure-specific boundary pathology 不成立。

Accepted 31省 input/outcome envelope audit 显示 failures/successes 在 consumed `ra` 与 household composite `w` 上高度重叠：无 single-variable separating threshold、2D boxes/hulls overlap、fixed k=3 graph interleaved，guards 无判别变异。Simple safe-price envelope / universal guard route CLOSED。

Latest accepted local-basin topology：
- 山西→河北 `F→C→C→C→C`
- 重庆→河北 `F→C→C→C→C`
- 江西→安徽 `F→F→C→C→C`
- 贵州→四川 `F→C→F→C→C`

Panel=`LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`。这是 numerical HJB basin evidence only，不是 economic multiple equilibrium、mapping/calibration error 或 counterfactual authority。不得自动 clipping、recalibration、guard/mapping、grid/boundary/HJB change。

Corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning KFE blocker继续独立未解决；standalone contaminated-row KFE 不替代 corrected multi-province KFE authority。

当前无 successor exact task。Reviewer 下一会话必须 fresh-fetch live main 后再 route decision；在新 freeze/task 正式发布前 science runtime=0。不得默认继续 synthetic interpolation、adaptive bisection 或 recalibration。

Owner 保留 structural equations、accepted guards、major calibration、causal interpretation、Results eligibility 最终 authority。GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
