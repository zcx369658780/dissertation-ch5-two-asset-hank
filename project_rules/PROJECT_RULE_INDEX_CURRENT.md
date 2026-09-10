# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`RAW_NBS_2018_REBUILD_ACCEPTED_PARTIAL__SAME_YEAR_GDP_POP_AND_LAGGED_FLOW_CAPITAL_REBUILT__SOURCE_ROUTE_DIFFERENCE_REMAINS`。
当前 active Builder task：`tasks/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md`。
该任务是Owner与Reviewer已经达成共识后的zero-science设计/静态source-mapping任务：统一单位合同、恢复/冻结alpha `[0.2,0.8]`边界逻辑、设计2018数据一致初始化、为`w/rah`提出under-relaxation合同，并把原有单循环“接近稳态后在线校准”形式规范成stabilization / near-steady calibration / final confirmation三个阶段。不得运行HANK/HJB/KFE/firm/outer-loop/steady-state模型，也不得实现production source修改。
最新接受候选：`3bd6343011f17d1b2273386732f06e6da6bf84e9`。
Reviewer acceptance：`docs/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

Owner已明确：正确2018 GDP/POP必须使用；PIM只要明确折旧即可，现有`delta=.096`可继续作为Chapter 5估计假设；资本是model-derived calibration object而非官方资本存量。alpha模型可行域按Owner原设计为`[0.2,0.8]`，原思路允许越界后使用边界值；当前重新估计raw alpha=`0.7380939146868483`在范围内，不需要clip。

Owner同意：统一宏观/household/firm之间的量纲；修改遗留的极端统一初值，优先由2018 `Y/K/L/Z/alpha`与现有firm方程反推价格初值；允许对`w/rah`采用under-relaxation；保留原来`HANK_mp_1eq.m`/`HANK_mp_1turn.m`中“接近稳态后开始校准”的高效率单循环思想，不采用完整nested steady-state/calibration双循环；可在此基础上设计staged gate与hysteresis，具体damping系数和阈值需后续bounded validation后再冻结。

最新raw-NBS rebuild仍为PARTIAL calibration evidence：2018原始投资/折旧缺失，lagged-flow公式可由2017流量生成K2018；raw GFCF路线与当前canonical investment route不是同一来源/概念，不能自动替换production capital authority。Track B observed-depreciation仅为诊断。

此前MATLAB mixed-year数据审计、raw-NBS重估和five-turn KFE attribution均继续作为有效历史证据。Owner当前优先修复/规范数据、初始化和外层稳态迭代逻辑，不自动进入KFE boundary redesign或新稳态运行。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新的科学执行必须先发布exact task。以后每次发布exact task，同一回复自动附Codex启动prompt。