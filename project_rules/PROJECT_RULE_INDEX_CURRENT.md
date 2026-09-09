# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION.md`。
状态标记：`CORRECTED_2018_TWO_TURN_ACCEPTED__TURN2_PROPAGATION_PASS__TURN3_DIRECT_RATE_TRANSMISSION_ACTIVE`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

2018数据层已关闭并绑定canonical workbook SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。

最新接受科学证据：fresh corrected-2018 turn1与前序完全一致，turn2也完整31省返回。安徽turn2 household `rah=.0829892058879816`由native资本分配规则使用turn1 entering `ra`向量生成，其中安徽source old ra仍为`.09`；turn1 firm used `ra=.02`只成为turn2 entering firm state，并按源码时序要到下一次资本分配后才能进入turn3 household composite return。两轮安徽raw firm return都低于`.02`下限，全国firm rate两轮均31/0/0 lower/interior/upper；turn2 max nk_gap=.45946738761290562，adaptation仍未开启。

当前task只允许fresh三轮轨迹，turn1/turn2必须先复现接受证据；turn3是首个direct corrected-rate household propagation gate。禁止turn4、steady-state/GE/annual/MATLAB/IRF/Results、科学重试、参数/solver/boundary调整。Results eligibility=FALSE。
