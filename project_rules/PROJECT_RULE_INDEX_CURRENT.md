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
8. `docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md`
9. `docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_ACCEPTANCE.md`
10. `docs/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACCEPTANCE.md`
11. `docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_ACCEPTANCE.md`
12. `docs/CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT_ACCEPTANCE.md`
13. `docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_ACCEPTANCE.md`
14. `docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_FREEZE_CURRENT.md`
15. active exact task：`tasks/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION.md`

当前状态：`J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION.md`。
最新 accepted blocked local-basin candidate：`06b427f4f0c705a17c0d064a5f508c7e3e72ccce`。
Results eligibility=`FALSE`。

Accepted practical household grid：`I=20,J=160,a=[0,100],b=[-2,20],h=1`，仅用于 bounded diagnostics。Finer-J/finer-I routes 均关闭。

The first local-basin interpolation execution passed pair authority and used exactly the frozen 12 probes, but formal topology was fail-closed because task-owned A2max aggregation mixed an `iterations+1` post-convergence system matrix with true source-generator observations. Exact scientific maximum A2max was not persisted.

Current task may repair only the task-owned receipt boundary and then rerun the same 12 sealed probes once. It must persist per-scientific-iteration A2max, exact scientific maximum/argmax iteration, and first scientific illegal iteration. Post-convergence matrix diagnostics must be separately named and excluded from scientific legality.

No new pairs/t values, endpoint reruns, adaptive bisection, KFE, outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results runtime, or calibration/HJB changes are authorized. Scientific retries=0.

Owner retains final authority over structural equations, accepted guards, major calibration, causal interpretation and Results eligibility. GitHub live main is sole repository authority.
