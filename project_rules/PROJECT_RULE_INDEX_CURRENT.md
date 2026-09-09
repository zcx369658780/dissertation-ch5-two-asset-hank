# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。每次先读`AGENTS.md`、本索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION.md`。
状态标记：`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER_ACCEPTED__KFE_LEAKAGE_ATTRIBUTION_ACTIVE`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

2018 canonical 数据层继续冻结，workbook SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。最新接受科学候选`9864129dd2e97bae97238ab9cc588aea48682d29`完成5 turns /155 updates，但Reviewer接受为KFE/distribution diagnostic blocker，不是PASS：turn4/5全31省density均`DIAGNOSTIC_ONLY`；machine-scale negative mass不是主因，实质问题是source-free stationarity residual与upper-b outward leakage（全国每轮620 positive upper-b leak cells；其余face leak=0）。

当前task严格zero-science-call，只能用已保存operator/density/drift做KFE mass-balance/row-replacement/escape attribution，并与accepted call725 `rah=.07`机制对照。所有household/HJB/KFE/solve/firm/controller/trajectory/MATLAB/GE/annual/IRF/Results调用必须为0。禁止turn6+、new KFE solve、steady state及production boundary/grid/source/pinning repair。Results eligibility=FALSE。

若当前attribution确认same finite-box upper-b leakage + pinning机制，后续必须先由Reviewer验收，再由Owner决定是否进入boundary/finite-box closure redesign；不得自动继续科学轨迹。正式发布任何后继exact task时，必须同一回复附Codex启动prompt。