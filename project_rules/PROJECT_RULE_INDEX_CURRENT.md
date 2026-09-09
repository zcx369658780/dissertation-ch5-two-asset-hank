# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION_REEXECUTION.md`。
状态标记：`CORRECTED_2018_THREE_TURN_CONTROLLED_FAIL_ACCEPTED__PERSISTENCE_REPAIR_FROZEN__REEXECUTION_ACTIVE`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

2018 canonical 数据层继续绑定 SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。

最新接受候选`8b80b491421603b94a281211d683d94e2a78fdaf`是受控FAIL证据：fresh turn1/turn2完全复现，随后在turn3进入前因`predecessor_reproduction.json`第二次排他写入触发`FileExistsError`；turn3未进入，科学retry=0。该失败是evidence persistence collision，不是模型/household/HJB/KFE/firm failure。候选中的一行 persistence sequencing repair 已静态验证但未科学执行，Reviewer已冻结其工程边界。

当前新task授权一次fresh repaired-runner three-turn reexecution：先核验canonical/repair身份和静态门；最多turn1–3、93 province updates、1 scientific process、0 retries。turn1/turn2必须复现接受证据后才可进入turn3。禁止turn4、steady-state/GE/annual/MATLAB/IRF/Results及任何参数/solver/boundary调整。Results eligibility=FALSE。
