# 第五章动态总目录
这是当前导航；条目按用途区分当前资料与历史快照。网页顾问必须实际读取正文及提交，不能以本目录代替证据。

| 逻辑槽位 | 现存正文 | 使用方式 |
|---|---|---|
| 当前工作方式与角色 | [V1.2现行工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)、[本地启动规则](../AGENTS.md) | 延续 V1.1：新增依赖命令失败即停、UTF-8/LF 记录、最终树回执与 UNKNOWN 遥测；旧Work仅历史 |
| 当前状态、在途与暂停 | [CURRENT](../CURRENT.md)、[迁移交接](CH5_ASTRA_MIGRATION_HANDOFF_20261012.md) | 当前状态入口；本地未同步差异见交接 |
| Codex第二阶段交接（历史） | [执行端交接](CH5_ASTRA_CODEX_EXECUTION_HANDOFF_CURRENT.md)、[新会话启动 Prompt](CH5_ASTRA_CODEX_NEW_SESSION_PROMPT_CURRENT.md) | Owner已报告新会话只读接收；此项为旧迁移交接，不覆盖当前 V0.0.1 版前状态 |
| 记忆、定义、环境 | [网页知识导航与恢复摘要](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md) | 决定、原证据上限及本地工具限制 |
| 路线图与版本登记 | [版本登记](CH5_VERSION_REGISTER_CURRENT.md) | V0.0.2 CLOSED；V0.0.3 已冻结 DOCUMENT_ONLY 且有独立实施许可，尚无执行结果 |
| V0.0.3 冻结计划与授权 | [不可变冻结计划](../versions/0.0.3/plan.md)、[Astra 独立授权](../versions/0.0.3/authorization.md) | 冻结 768a3181fcbc…；源码基线 V0.0.2 8f5457947492…；仅文档，protected/科学0 |
| V0.0.2 冻结与最终结论 | [冻结计划](../versions/0.0.2/plan.md)、[授权](../versions/0.0.2/authorization.md)、[验收](../versions/0.0.2/acceptance.md)、[复盘](../versions/0.0.2/retrospective.md) | freeze SHA 4b11c46823e7… 未追改；candidate 8f5457947492…；真实来源认证未获得 |
| V0.0.1 已冻结计划与结论 | [固定冻结计划](../versions/0.0.1/plan.md)、[实施授权](../versions/0.0.1/authorization.md)、[最终验收](../versions/0.0.1/acceptance.md)、[版本复盘](../versions/0.0.1/retrospective.md) | 冻结提交 6c9a13bd...不变；候选 3260ec39...；仅合成工程 ACCEPT_WITH_OBSERVATIONS |
| 当前/历史计划、结果、验收、复盘 | 版本登记中的具体入口 | 冻结版固定 SHA；代码候选与文档分支可能分离，须按真实提交读取 |
| 历史Sources与本地私有资料 | [知识摘要](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md)、[手工交接](CH5_ASTRA_MIGRATION_HANDOFF_20261012.md) | 私有日志/数据不上传；按需人工提供脱敏片段 |
| 来源/引用资格 | [原知识库正文](knowledge/project-sources/DISSERTATION_KNOWLEDGE_BASE_CURRENT.md) | 历史正文中稳定E0–E3/D0–D4资格保留 |
| 模型研究脉络 | [9月27日改写快照](knowledge/project-sources/CH5_DISSERTATION_CHAPTER5_REWRITE_CURRENT.md)、[科学合同账](../SCIENTIFIC_DECISIONS.md) | 历史状态不能充作当前，后续决定优先 |
| 近期交接证据 | [进度快照](knowledge/published/CH5_WORK_PROGRESS_FLOW_MANUAL_HANDOFF_20261011_140603Z.md)、[验收账快照](knowledge/published/CH5_WORK_ACCEPTANCE_LEDGER_MANUAL_HANDOFF_20261011_140603Z.md)、[劳动决定](knowledge/published/CH5_LABOR_UNIT_HISTORY_AND_EVIDENCE_20261010_145723Z.md) | 脱敏发布副本，旧流程已替代，报告接受不冒称本轮重测 |
| 历史归档覆盖与测试 | [归档安全摘要](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md) | 历史检索结果及Owner补充新会话测试分开 |
| 上传用稳定索引 | [PROJECT_SOURCE_INDEX_CH5](PROJECT_SOURCE_INDEX_CH5.md) | 只在仓库/发布分支/入口改变时通常重传 |

2026-10-13 V0.0.3 经 Codex 执行草稿与 Astra 审议已冻结于 768a3181fcbc9d367ccce08b1d69458353a48229，独立文档许可于 2ec13ea41e7bb86eacb19f4601d243a1298bd4bd 发布；Codex 可以自主实施三文件 DOCUMENT_ONLY 后集中交付。实际 protected/科学0，当前未有新候选或验收。

2026-10-13 Owner 已同意 V0.0.2 复盘后的轻量 V1.2 工作流修订：只增补工程失败依赖检查、编码/换行、最终候选树回执与资源 UNKNOWN 分账；未立 V0.0.3、未修改模型科学合同与冻结原证。现行规则见本表首行。

2026-10-13 V0.0.2 已经由 Astra 最终受限验收：CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS；候选 SHA 8f5457947492eef552f4261f8630c6c886af9fa5，仍不证明真实来源、科学或 Results；后续版本尚未启动。

2026-10-13 工作流 V1.1 已获 Owner 批准，仅更新现行导航/规则，不改冻结版本或开启 V0.0.2；参见上方 V1.1 规则与版本登记。

2026-10-13 V0.0.1 已根据正式冻结提交 6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8 完成工程候选最终验收：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`；候选固定 SHA 3260ec393dd4d53d6aab6c34d7c0442f09aa79f4。仅合成工程闭环通过，不等于真实科学/Results/生产接受；未启动后续版本。详情见版本登记、验收与复盘。

先读工作流、CURRENT、迁移交接与知识摘要，再按具体版本读取冻结计划和真实候选。普通状态使用当前分支路径；正式计划、代码/证据在版本登记保存固定提交。路径带CURRENT不自动证明内容时效，表中的“历史”标记优先。
访问失败/未发布/LOCAL_ONLY要明确缺口，使用Owner提供的对应文件或提交快照，不声称已读。本目录不赋予自动同步或额外权限。
