# 第五章动态总目录

**现行最新（2026-10-14）：V0.0.6已完成受限合成工程独立验收并正式关闭，分类为 `CLOSED__ACCEPT__SOURCE_ONLY_IMPLEMENTATION_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`。冻结commit `4857d9222580b491676cdf75951527eb06d16b49`，代码candidate `198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`（尚未合main）；真实原C8数据、劳动/资本单位、observed consumer、A16/C9/GE/Results仍未认证或开放。V0.0.7 NOT_STARTED；下一步等Owner明确科研立版。当前状态见 [CURRENT](../CURRENT.md)、[版本登记](CH5_VERSION_REGISTER_CURRENT.md)、[V0.0.6验收](../versions/0.0.6/acceptance.md)及[复盘](../versions/0.0.6/retrospective.md)。历史“V0.0.6 DRAFT/冻结待Codex”段落仅为历史时点。**

这是当前导航；条目按用途区分当前资料与历史快照。网页顾问必须实际读取正文及提交，不能以本目录代替证据。

| 逻辑槽位 | 现存正文 | 使用方式 |
|---|---|---|
| 当前工作方式与角色 | [V1.2现行工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)、[本地启动规则](../AGENTS.md) | 延续 V1.1：新增依赖命令失败即停、UTF-8/LF 记录、最终树回执与 UNKNOWN 遥测；旧Work仅历史 |
| 当前状态、在途与暂停 | [CURRENT](../CURRENT.md)、[迁移交接](CH5_ASTRA_MIGRATION_HANDOFF_20261012.md) | 当前状态入口；本地未同步差异见交接 |
| Codex第二阶段交接（历史） | [执行端交接](CH5_ASTRA_CODEX_EXECUTION_HANDOFF_CURRENT.md)、[新会话启动 Prompt](CH5_ASTRA_CODEX_NEW_SESSION_PROMPT_CURRENT.md) | Owner已报告新会话只读接收；此项为旧迁移交接，不覆盖当前 V0.0.1 版前状态 |
| 记忆、定义、环境 | [网页知识导航与恢复摘要](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md) | 决定、原证据上限及本地工具限制 |
| 路线图与版本登记 | [版本登记](CH5_VERSION_REGISTER_CURRENT.md) | V0.0.6 已正式CLOSED（受限合成工程接受）；V0.0.7 未启动，真实科研运行未放行 |
| V0.0.6 M1冻结与受限最终验收 | [冻结计划](../versions/0.0.6/plan.md)、[独立验收](../versions/0.0.6/acceptance.md)、[复盘](../versions/0.0.6/retrospective.md) | 五字段/三轴/双消费者合成工程CLOSED；原始C8真实输入及Results仍UNKNOWN/BLOCKED |
| 本次长会话决策与进度交接 | [2026-10-14晚会话交接文档](CH5_CONVERSATION_HANDOFF_20261014_EVENING.md) | V0.0.5证据/Owner决策/低频GitHub工作流、V0.0.6已启动但仅DRAFT，供新Astra恢复权威 |
| 2026-10-14 论文成果优先战略 | [Owner新战略路线](CH5_PUBLICATION_FIRST_STRATEGIC_ROADMAP_20261014.md)、[历史技术路线](DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md) | 不为一般备份追加物理隔离；第一篇以真实科学闭环为先，A16/Results门不虚构通过 |
| V0.0.5 最终验收、复盘与备份资格 | [最终验收](../versions/0.0.5/acceptance.md)、[复盘](../versions/0.0.5/retrospective.md)、[B3有限验收](../versions/0.0.5/b3_acceptance.md) | V0.0.5有限行政CLOSED；普通字节备份有限PASS、G0 UNPROVEN、物理清理0；V0.0.6未启动 |
| V0.0.5 全量备份技术审议（历史） | [Astra 审议](../versions/0.0.5/full_backup_review.md)、[Owner范围决定](../versions/0.0.5/owner_full_backup_cleanup_decision.md)、[旧预检DRAFT](../versions/0.0.5/full_project_backup_preflight.md) | linked-worktree+外置Git管理目录均须保全；待Owner批准元数据B0，复制/删除仍禁止 |
| V0.0.5 空备份目录附属门验收 | [有限验收](../versions/0.0.5/backup_directory_acceptance.md)、[冻结计划](../versions/0.0.5/backup_directory_gate.md)、[独立授权](../versions/0.0.5/backup_directory_authorization.md) | Codex回报仅空目录已创建；本子门CLOSED/有限接受；无备份复制；主可信根仍 DRAFT |
| V0.0.4 阻塞验收与复盘 | [最终验收](../versions/0.0.4/acceptance.md)、[复盘](../versions/0.0.4/retrospective.md)、[冻结计划](../versions/0.0.4/plan.md)、[授权](../versions/0.0.4/authorization.md) | 安全停止、0实验/0候选，真实保护读取仍禁止 |
| V0.0.3 冻结与验收结果 | [冻结计划](../versions/0.0.3/plan.md)、[独立授权](../versions/0.0.3/authorization.md)、[最终验收](../versions/0.0.3/acceptance.md)、[复盘](../versions/0.0.3/retrospective.md) | freeze 768a3181fcbc…不变，candidate cf74384f1514…，真实读取仍 REQUEST_ONLY |
| V0.0.2 冻结与最终结论 | [冻结计划](../versions/0.0.2/plan.md)、[授权](../versions/0.0.2/authorization.md)、[验收](../versions/0.0.2/acceptance.md)、[复盘](../versions/0.0.2/retrospective.md) | freeze SHA 4b11c46823e7… 未追改；candidate 8f5457947492…；真实来源认证未获得 |
| V0.0.1 已冻结计划与结论 | [固定冻结计划](../versions/0.0.1/plan.md)、[实施授权](../versions/0.0.1/authorization.md)、[最终验收](../versions/0.0.1/acceptance.md)、[版本复盘](../versions/0.0.1/retrospective.md) | 冻结提交 6c9a13bd...不变；候选 3260ec39...；仅合成工程 ACCEPT_WITH_OBSERVATIONS |
| 当前/历史计划、结果、验收、复盘 | 版本登记中的具体入口 | 冻结版固定 SHA；代码候选与文档分支可能分离，须按真实提交读取 |
| 历史Sources与本地私有资料 | [知识摘要](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md)、[手工交接](CH5_ASTRA_MIGRATION_HANDOFF_20261012.md) | 私有日志/数据不上传；按需人工提供脱敏片段 |
| 来源/引用资格 | [原知识库正文](knowledge/project-sources/DISSERTATION_KNOWLEDGE_BASE_CURRENT.md) | 历史正文中稳定E0–E3/D0–D4资格保留 |
| 模型研究脉络 | [9月27日改写快照](knowledge/project-sources/CH5_DISSERTATION_CHAPTER5_REWRITE_CURRENT.md)、[科学合同账](../SCIENTIFIC_DECISIONS.md) | 历史状态不能充作当前，后续决定优先 |
| 近期交接证据 | [进度快照](knowledge/published/CH5_WORK_PROGRESS_FLOW_MANUAL_HANDOFF_20261011_140603Z.md)、[验收账快照](knowledge/published/CH5_WORK_ACCEPTANCE_LEDGER_MANUAL_HANDOFF_20261011_140603Z.md)、[劳动决定](knowledge/published/CH5_LABOR_UNIT_HISTORY_AND_EVIDENCE_20261010_145723Z.md) | 脱敏发布副本，旧流程已替代，报告接受不冒称本轮重测 |
| 历史归档覆盖与测试 | [归档安全摘要](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md) | 历史检索结果及Owner补充新会话测试分开 |
| 上传用稳定索引 | [PROJECT_SOURCE_INDEX_CH5](PROJECT_SOURCE_INDEX_CH5.md) | 只在仓库/发布分支/入口改变时通常重传 |

2026-10-13 Owner 已启动 V0.0.5 版前规划，仅调查可信独立根的获取和隔离证明；旧 G0 实验额度没有恢复，无创建/测试/真实读取许可。

2026-10-13 Owner 已启动 V0.0.4 版前规划。V1.2 已覆盖 fail-fast，当前不升级工作流文档；新版本仅 DRAFT 和 Codex 只读方案，没有北京历史文件读取许可、科学测试或实现授权。

2026-10-13 V0.0.3 已经 Astra 有限验收关闭：`CLOSED__ACCEPT__DOCUMENTARY_SOURCE_CONTRACT_ONLY__WITH_OBSERVATIONS`；GitHub 候选 `cf74384f151427f0b7071ac0461cede6ad6cdf11`、三文档及14/14固定来源匹配，真实北京读取申请仍仅 REQUEST_ONLY。Codex 本地资源/错误回执证据等级单列，V0.0.4 尚未启动。

2026-10-13 Owner 已同意 V0.0.2 复盘后的轻量 V1.2 工作流修订：只增补工程失败依赖检查、编码/换行、最终候选树回执与资源 UNKNOWN 分账；未立 V0.0.3、未修改模型科学合同与冻结原证。现行规则见本表首行。

2026-10-13 V0.0.2 已经由 Astra 最终受限验收：CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS；候选 SHA 8f5457947492eef552f4261f8630c6c886af9fa5，仍不证明真实来源、科学或 Results；后续版本尚未启动。

2026-10-13 工作流 V1.1 已获 Owner 批准，仅更新现行导航/规则，不改冻结版本或开启 V0.0.2；参见上方 V1.1 规则与版本登记。

2026-10-13 V0.0.1 已根据正式冻结提交 6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8 完成工程候选最终验收：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`；候选固定 SHA 3260ec393dd4d53d6aab6c34d7c0442f09aa79f4。仅合成工程闭环通过，不等于真实科学/Results/生产接受；未启动后续版本。详情见版本登记、验收与复盘。

先读工作流、CURRENT、迁移交接与知识摘要，再按具体版本读取冻结计划和真实候选。普通状态使用当前分支路径；正式计划、代码/证据在版本登记保存固定提交。路径带CURRENT不自动证明内容时效，表中的“历史”标记优先。
访问失败/未发布/LOCAL_ONLY要明确缺口，使用Owner提供的对应文件或提交快照，不声称已读。本目录不赋予自动同步或额外权限。
