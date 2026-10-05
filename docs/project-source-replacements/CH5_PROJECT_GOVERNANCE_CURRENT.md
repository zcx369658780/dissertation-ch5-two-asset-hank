# 第五章项目治理与执行规则

更新：2026-10-05（Asia/Shanghai）。供Owner替换ChatGPT项目中同名源文档；本地synced sources未修改。本文件是现行规则快照，不创建任务、调用预算或科学接受。实时权威是唯一工作树中的AGENTS/CURRENT/SCIENTIFIC_DECISIONS/TASK_CURRENT/REVIEW_GATE。

Work目标：01a10914-5f50-7f32-aea2-2635038edd2c/local；唯一Builder：01a0fed3-173a-7d20-8a3a-ffc7a299b726/local。旧Work01a10681-0e7f-7c33-8d0e-e637ba7522b3不再唤醒，不创建、更换执行会话或迁移Dot。
唯一实际工作树D:\ProjectTemp\c5k1bturn56；branch=codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922；基线HEAD=a1db8c114dec0ab69d69a5576e153a7f868cba0e。Zotero-Analytical-Workflow/projectId=local-0758adfaed355d5be608096cdf92a3a2仅界面归属，不授权其仓库访问。

## 阶段目标委托—Codex连续执行—Work集中验收

1. Work依据现行路线和实际状态，把若干相邻实现步骤合并成可独立验收的阶段目标，不按文档数量评估完成率。
2. 阶段委托完整写清目标、可观察完成标准、上下文与基线、读写模块/路径、约束、自主范围、决定停点、总预算、持续无进展处理、证据位置及本地提交权限。明确执行授权后才标记ISSUED；空缺不可凭Builder推断授权。
3. 新签普通工程阶段内，Builder可自主调查、调整步骤、修改范围内源码和测试、验证、诊断、修复与必要重测，不逐步骤申请。普通工程失败保留原始记录，在阶段预算内闭环；不自动撤销整个阶段授权。
4. 不得删除有效测试、降低标准、隐藏失败、用无效结果，或改变未授权的方程、KKT、边界、校准、时序、收益律、求解语义、网格、容差及科学口径。
5. 阶段总预算由委托给出数值：工作时间/资源上限及必要的测试或修复上限；受保护操作另列精确额度。触及总预算，连续规定数量的诊断修复仍无可观察进展，或需要实质扩大范围时停下，报告已尝试方法、失败证据和需决定事项。普通工程不机械按每个读/写/步骤拆分审批；一次性及保护预算仍逐笔记账。
6. 少数决定停点：实质科学/风险/保护选择、未授权资产或敏感传输、发布、预算突破、无法安全保留既有内容、持续无进展、以及Owner明确暂停。历史首失败即停任务及旧独立门不受第3条覆盖。
7. Work正常执行期间不逐步骤验收、不高频询问、不并行修改Builder同批文件；仅完成、实质决定、边界问题或持续无进展时介入。heartbeat只监督有意义变化，不充当逐步骤授权器。
8. Builder完成后集中提交最终改动、完成标准逐项对照、全部相关测试及原始证据位置、失败与修复记录、未完成项和风险；自检不能替代独立接受。
9. Work独立核验，汇总一批实质修复要求；Builder在明确剩余/补充修复预算内完成，Work复核修复及必要回归。新发现实质缺陷可继续受界处理，不为了凑一次验收隐藏问题。既有HIGH独立科学审查及Owner权威保持。
10. GitHub仅作备份。只更新必要现行指导和当前任务，不另建治理体系或治理任务链。本地提交必须在阶段委托明确允许路径/方式；流程放权不授权push、merge、release、发布或解冻保护事项。
11. 约30次真实人工对话或上下文不可靠时保存当前阶段状态、证据身份、剩余预算与下一门后手动交接；工具调用/heartbeat不计人工对话。接续当前阶段，不重新规划全项目；本次不自行创建或更换会话。

## 当前状态与安全

- 现有automation work保持PAUSED、5分钟、上述交接Work；流程采纳及文档备份不等于恢复。当前没有ISSUED实现阶段。当前聊天与目标Work可能不同，不能据此改target或唤醒旧Work。
- Owner decision packet单文件读取仍PROPOSED_NOT_AUTHORIZED/未读；本快照不开放其读取、沿引用、科学输入或旧证据预算。
- 科学权威属Owner；Work是项目负责人及独立验收人，Builder连续完成受界工程实现。既有HIGH独立科学门保留。
- 写入前核Git身份、状态和允许范围，保存dirty/untracked；只暂存本任务范围，不用宽泛add、cleanup、reset、stash、强推。
- GitHub仅备份，不是任务队列、验收门或实时本地状态权威。备份不证明来源、平台保护、科学有效性或Results。
- 只在阶段明确授权时创建工程测试/证据；真实科学产物读取须精确文件、用途和额度。Windows路径替换、文件身份和保护合同保持fail closed，不从静态或tempdir PASS批准runner。
- 本地备份目录沿用C:\Users\zcxve\Documents\Chapter5LocalBackups；本次不另行备份历史证据或重要资产。
- 科学/论文 claim保持E3或等价人工原页核验要求。价格方法归属已采用不等于直接价格验证；turn5–8受界接受不等于fixed point、稳态或GE。

完整Objective A、16 UNRESOLVED、window UNACCEPTED、CALL_LEDGER_UNRESOLVED、C9 PAUSED、model_activation=False、Results FALSE保持。五False：source_authenticated、original_live_identity_restored、scientific_validity_established、model_activation、execution_admitted均为False。
正式模型/consumer、科学实验与定义变更、C8重跑/C9/C10、真实carrier认证、科学JSON-NPZ解析解压、保护变化、发布、敏感外传、重要资产删除均未授权。禁止deep-learning-hank、另一当地Zotero仓、Project sources写入、跨树索引及dirty/node_modules清理。
全部历史STOP/CLOSED及耗尽预算原样保留，不重读已闭证据，不重试、换审者/模型或改名重派；新流程不恢复旧额度。JSON31行仅partial，ZIP拒绝实际原因UNKNOWN，独立回执UNKNOWN/NOT_VERIFIED；launcher NOT_ACCEPTED/全部NOT_RUN。
