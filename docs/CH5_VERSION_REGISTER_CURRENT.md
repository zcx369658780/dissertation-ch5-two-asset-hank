# 第五章路线图与版本登记

## 2026-10-13 现行：第三阶段 V0.0.1 版前协商（未冻结）

Owner 已明确手动启动第三阶段并暂定首版为 V0.0.1。Astra 已发布 [V0.0.1 候选计划](../versions/0.0.1/plan.md)，状态为 `DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`。当前仅请求 Codex 只读提交执行方案草稿，Astra 审议后才能正式冻结计划、登记冻结 SHA 及决定 `ASTRA_APPROVED_EXECUTION`。草案发布不是旧预算重置、科学运行许可或工程执行开始。现阶段无冻结版本，无开发 ISSUED；冻结版 plan/候选/acceptance/retrospective 仍待产生。科学保护、数据门与关闭旧任务不变。

## 2026-10-12 第二阶段迁移记录（历史截点）
迁移后首版：**尚未制定，等待第三阶段**。Owner手动启动；本轮没有新版本号、批准、执行或通过记录。

## 路线图入口
历史[两资产路线图](CH5_TWO_ASSET_HANK_ROADMAP_CURRENT.md)及[Python重建路线图](DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md)保留现有内容和证据级别，不能由旧“下一步”直接启动。未来路线更新不能改原冻结版本。
当前优先未闭问题：真实solver来源绑定、聚合/frozen实际调用、frozen→batch构造、callback装配、量纲/人口分母/时点及科学运行与环境/保护。它们是问题清单，不是第三阶段执行计划。

## 后续登记约定
Owner确立版本后，在此登记：版本标识及阶段、正式计划路径和冻结依据（批准来源及固定提交）、代码基线与候选SHA、实际执行报告、独立验收、复盘位置和终态。
可采用`versions/<Owner确立的版本标识>/plan.md`、`execution.md`、`acceptance.md`、`retrospective.md`；这些是命名约定，目前全部待创建，不是现存链接。草稿仅版前协商。冻结计划不可事后改目标；修复批次针对原目标内缺陷，新增需求入未来版。

## 历史登记与固定证据
- 历史K1B等冻结版本：原件/原状态不重写。已有[科学合同账固定快照](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/a1db8c114dec0ab69d69a5576e153a7f868cba0e/SCIENTIFIC_DECISIONS.md)与[双边资本网络冻结稿固定快照](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/a1db8c114dec0ab69d69a5576e153a7f868cba0e/docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md)。
- 上述SHA是本地提交已存在于远端备份分支的文件快照，不是各合同首次冻结提交或全部验收基线的追认。逐版本原冻结/代码/验收commit尚未从完整历史逐一核出，记UNKNOWN，不补造。
- 最新接受为scripts/tools metadata门ACCEPT/CLOSED；末binding SOURCE_ONLY门NOT_ACCEPTED/CLOSED，见[近期账快照](knowledge/published/CH5_WORK_ACCEPTANCE_LEDGER_MANUAL_HANDOFF_20261011_140603Z.md)。这些旧stage不是迁移后新版本。
- 各历史执行/复盘资料未全量覆盖，若需要立版必须按具体问题核原件。备份≠验收，自测≠最终验收，验收≠发布。

## 第二阶段执行端交接（不登记为新版本）

[Codex实时交接](CH5_ASTRA_CODEX_EXECUTION_HANDOFF_CURRENT.md)及[Owner手工启动Prompt](CH5_ASTRA_CODEX_NEW_SESSION_PROMPT_CURRENT.md)补充本地封存状态。发布基线3ec76075c90f823ed83ca6e0a8c385a61f79ef85；本次文档提交以发布回执及分支fresh-fetch为准。本地代码HEAD不移动；迁移后首版NOT_STARTED，等待Owner第三阶段。交接文件准备完成不等于新会话已实际接收。
