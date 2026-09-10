# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`PYTHON_RUNTIME_INPUT_BINDING_REPAIR_ACCEPTED__CORRECTED_2018_TRACK_A_UNIT_CONTRACT_ENFORCED__SCIENTIFIC_RERUN_STILL_NOT_AUTHORIZED`。
当前 active Builder task：无。
最新接受候选：`a7bd3b1a705ff42e2933b22a8c6563ec47248ce4`。
Reviewer acceptance：`docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新实现修复已接受：corrected-2018 active runtime现在单一路径绑定actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`及same-year `Zt0`。legacy/canonical builder仅保留为显式historical replay API，不再是corrected route fallback。31/31 pre-science assertions通过；serialized payload在write/readback及science launch之前再次校验，旧尺度安徽`K/GovInv/Zt`注入会在`science_started.json`写入前fail-closed。

安徽当前accepted corrected initialization receipt：`Y0=34010900 MU`、`N0=L0=607600 NU`、`K0=GovInv0=70182433.35888097 MU`、`alpha=.7380939146868483`、`Zt0=1.681124916844091`。`GovInv0=Ktarget`仍只是`SOURCE_FAITHFUL_INITIALIZATION_RULE__SCIENTIFIC_REDESIGN_PENDING`；`beta_a=1`仍只是`SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`。

上一100-turn候选`242e853708d3d0d4f891c7a043d7d4e3fba05c50`已被Reviewer拒绝为frozen-input contract violation：该trajectory实际使用legacy/canonical old-scale capital/GovInv/Zt，不能作为Track-A/unit-normalized corrected-2018 trajectory证据。它可以保留为历史错误尺度如何压低`ra/rah`的diagnostic evidence，但不得作为后续科学验收基线。

此前firm-price forensic仍有效：wage bound主要受未闭合numeraire影响；firm return主要受`Y/K`经济比率相对历史数值safeguard影响。household绝对货币归一化、asset bridge识别、GovInv初始化科学规则、Lt迁移/生产劳动映射、KFE/HJB独立blockers均尚未解决。

当前禁止自动运行新trajectory、steady state、GE/annual/IRF/Results。下一步先由Owner/Reviewer选择：优先做`Kt/Lt`与原始2018数据的reconciliation和GovInv/Lt initialization设计，或另行发布新的correctly-bound bounded trajectory exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。

GitHub live main是repository-state authority；聊天不能替代exact task。