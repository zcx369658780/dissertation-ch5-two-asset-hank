# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_TWO_TURN_PROPAGATION.md`。
状态标记：`CORRECTED_2018_SINGLE_TURN_ACCEPTED__FULL_ORDERED_TURN_PASS__TURN2_PROPAGATION_ACTIVE`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

2018数据层已关闭并绑定canonical workbook SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。最新接受科学证据：corrected-2018 turn 1完整31省通过，31/31 household/HJB/KFE/firm返回；安徽当期firm `ra0=-0.02496997113112164`、used `ra=0.02`，但household进入turn 1仍使用carried `rah=0.09`。全国firm rate全部在下限，adaptation未开启。

该证据只覆盖turn 1，不能宣称旧turn23/call725后期高收益或不收敛已解决。当前task只允许fresh两轮轨迹，中心对象是native state transition后turn 2 household `rah`、firm return、wage、HJB/KFE、gap/controller。禁止手工设置rah、turn 3、steady-state/GE/annual/IRF、科学重试或参数/solver/boundary调整。Results eligibility=FALSE。
