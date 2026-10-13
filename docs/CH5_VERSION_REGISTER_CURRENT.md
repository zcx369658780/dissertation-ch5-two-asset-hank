# 第五章路线图与版本登记

## 2026-10-13 现行：V0.0.1 已冻结，实施授权已发布

- **版本 `0.0.1`：`FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_IMPLEMENTATION`。** Owner 启动第三阶段；Codex 已提交 `V0.0.1_EXECUTION_PROPOSAL_DRAFT`，Astra 审议后批准其纯合成工程方案。
- **不可修改的正式冻结计划**：[V0.0.1 plan](../versions/0.0.1/plan.md)；冻结提交 `6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8`，plan blob `065cfaf699db99f36d0fb05f037986ba22479298`。
- **独立实施许可**：[authorization](../versions/0.0.1/authorization.md)；发布提交 `837b99dff12f1b263fd7f4b80c43e19cf4efaa48`，其中含 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.1__SYNTHETIC_HOUSEHOLD_BRIDGE_ONLY`。
- 代码基线截点 `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，本地既有 dirty/untracked/ignored 不包含在该 SHA，Codex 启动前须 fresh-readback 与保护。
- 本版本仅准新的显式合成模块/测试、受控 isolated candidate_view、专属本地 EVIDENCE、脱敏执行报告；focused 工程预算 <=4小时、<=8个测试进程/每个<=120秒、目标<=2GiB、证据<=10MiB；真实科学/模型与受保护数据运行预算 0。
- Codex 在冻结边界内自主实施、调试和聚焦验证，集中发布一次候选供 Astra 最终独立验收。当前**仅为授权就绪**，尚无实际实施或通过证据；`execution.md`、`acceptance.md`、`retrospective.md` 仍待产生。
- 不更改旧 C9 PAUSED、CALL_LEDGER_UNRESOLVED、A16 FAIL_CLOSED、Results FALSE、劳动单位 UNKNOWN、既有经济法则、已关闭预算。**本登记不覆盖 plan 冻结原件。**

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
