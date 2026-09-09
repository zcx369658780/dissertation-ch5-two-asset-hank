# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_REVISED_GDP_AND_CANONICAL_DATA_WORKBOOK.md`。
状态标记：`REVISED_2018_GDP_AND_CANONICAL_WORKBOOK_ACTIVE__PIM_AND_POPULATION_CLOSED`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

已接受：2018安徽人口修订历史值`6076`万人；PIM资本链按冻结公式逐年binary64精确复现，`K2018=1357314108.2013683`，资本/PIM blocker关闭。资本是model-derived calibration object，2011投资统计定义断点继续作为限制。

当前只剩修订后2018安徽现价GDP身份未闭合。Owner授权从公开官方来源检索，并要求完成后将长期使用的数据统一保存为一个版本化`.xlsx`。当前task同时负责GDP最终身份闭合和`CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`构建；完整私有/CNKI数据工作簿默认只保存在本地证据根，不提交GitHub。

本任务所有MATLAB、household/HJB/KFE、root/direct/eigen、firm/one-turn/controller、annual/GE/IRF/Results科学调用均为0。不调GovInv/alpha，不扩大bmax，不切换PLM。Results eligibility=FALSE。