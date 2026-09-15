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
13. `docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_FREEZE_CURRENT.md`
14. active exact task：`tasks/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC.md`

当前状态：`J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC.md`。
最新 accepted input-envelope candidate：`49ea4c12692c669701cdc7bcf8fd02267a068090`。
Results eligibility=`FALSE`。

Accepted practical household grid：`I=20,J=160,a=[0,100],b=[-2,20],h=1`，仅用于 bounded diagnostics。Finer-J/finer-I routes 均关闭；禁止通过增加 maxit、damping/relaxation/line-search 或 tolerance/floor/selector 修改制造 convergence。

Accepted first-turn provincial HJB 为 25/31 converged、6 legal nonconverged。Temporal mechanism、value-argmax spatial pattern、coordinate-resolved selector/floor footprints均异质；successful controls 也存在明显 upper-b activity，因此 common failure-specific boundary pathology 不成立。

Accepted 31省 input/outcome envelope audit 又显示 failures/successes 在 consumed `ra` 和 household composite `w` 上高度重叠：single-ra/single-w threshold 均不存在，2D bounding boxes/convex hulls overlap，固定 k=3 graph interleaved，guard states 无判别变异。简单 safe-price envelope 或单一 guard rule 不被支持。

Active exact task 是 bounded local-basin interpolation diagnostic：仅使用 山西↔河北、重庆↔河北、江西↔安徽、贵州↔四川 四个预注册 matched pairs。必须先证明 pair 内除 `ra`/composite `w` 外全部 consumed household inputs exact equal；endpoints reuse-only。每 pair 只运行 t=.25/.50/.75 三个 synthetic probes，共 HJB exactly12，KFE=0，scientific retries=0；禁止 adaptive bisection、额外 synthetic points 或任何 calibration/mapping/HJB change。

Synthetic probes 只用于 numerical basin topology，不是经济可行省级状态或校准目标。Standalone contaminated-row KFE 与 unresolved corrected-2018 finite-box upper-b leakage / MATLAB-style pinning blocker继续分离。

Owner 已授权 ChatGPT Reviewer 对 bounded numerical diagnostics 作预注册决策；结构方程、accepted equations/guards、主要经济校准、因果解释与 Results eligibility 仍由 Owner 决定。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
