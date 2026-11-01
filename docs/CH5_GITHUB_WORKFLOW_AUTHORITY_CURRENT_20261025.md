<!-- LOCAL_FIRST_CLASSIFICATION_20261101 -->
> **适用范围：SUPERSEDED_WORKFLOW（日常角色）＋ SCIENTIFIC_CONSTRAINT（保护要求）**
>
> 当前执行入口：[AGENTS](../AGENTS.md) → [唯一短状态](CH5_LOCAL_FIRST_STATUS_CURRENT.md) → [唯一工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)。Owner 决策见 [2026-11-01 决策记录](OWNER_LOCAL_FIRST_CODEX_20261101.md)。
>
> 下方旧 GPT 日常派单、普通工程网页终验、强制三阶段流程及“本文件最高权威”的当前角色声明，已由 2026-11-01 Owner 决定覆盖。普通授权内工程由 Local Codex 自治推进、自作工程验收；Web GPT 按需咨询。
> 原始来源/字节身份、足够实际证据、科学与数值审查、预算、隐私、平台拒绝、STOP/PENDING 和禁止越权的实质要求保留；特定科学合同明确规定的独立门仍有效。
> 旧 GPT 微预算裁量条款不自动转授或恢复试验/重试额度；不得从历史默认次数生成新授权。下方正文逐字节保留为历史与保护依据，不从中复活旧任务。

---

# CH5 GitHub 在线任务与证据审阅工作流（正式权威规则）
STATUS=OWNER_APPROVED_CURRENT
EFFECTIVE=2026-10-25
MODE=MANUAL_PER_TASK_NOT_AUTOMATED
DEFAULT_WORKFLOW=GPT_GITHUB_TASK_SHEET__LOCAL_CODEX__SSH_CANDIDATE_BRANCH__GPT_FIXED_COMMIT_REVIEW__OWNER_DECISION
OFFLINE_ZIP=EXCEPTIONAL_FALLBACK_ONLY
AUTO_ISSUE=DISABLED
AUTO_MERGE=DISABLED
AUTO_CLEANUP=DISABLED
AUTO_NEXT=DISABLED

## 正式流程
GPT顾问在治理分支发布冻结任务单；Owner交本地Codex；Codex核验工作区后仅在任务授权的独立候选分支/目录执行，并通过已授权普通权限SSH推送；Codex回读commit、parent、tree、路径、Blob、大小和必要SHA-256后STOP；GPT/Astra直接从固定commit阅读并独立裁决；Owner决定下一步。每项新任务单独授权。

## 证据要求
复杂程序项目默认以GitHub固定commit中的真实源码与证据文件为审阅载体，不要求常规全量离线ZIP。任务必须提供足够源码上下文、关键输入/输出、diff、来源映射、manifest、必要测试/失败证据、缺口登记和隐私报告。摘要/哈希不能代替必要原件；脱敏副本须记录原件身份和变换。Git Blob与SHA-256分别记录。

## 三阶段审阅与中断恢复
A提交/来源硬门；B关键实现、数值和科学风险；C分层裁决。每阶段记录COMPLETED/BLOCKED/NOT_COMPLETED/NEXT_ACTION。中断后从固定任务、commit和最近检查点恢复，复用已验证对象，不重跑无关历史、不扩大范围、不推断未返回结果。工具故障为REVIEW_TOOL_ERROR；原字节/必要来源缺失为REVIEW_PENDING_IO。证据足以支持CHANGES_REQUIRED时有界早停。

## 写入和安全边界
任务单必须列明唯一TASK_ID、治理HEAD、候选分支、固定parent、来源commit/tree/path/blob、白名单、预算、STOP和验收字段。禁止自动Issue/PR、合并、清理、下一任务。SSH成功不代表Project Sources或本地Codex已同步。遇平台/权限拒绝必须STOP，不换凭据、账号、协议或路径绕过。

## 科研权限
本规则不授权模型运行。保持FORMAL_SOURCE_FREEZE=FALSE、V010=UNCHANGED、V011=NOT_STARTED、Results=FALSE、model_activation=False、REAL_GE=False、FULL_RUNNER_IO_CLOSURE=BLOCKED。不得自动运行HA/HJB/KFE/GE/IRF、调参、稳态或福利计算。

## 旧规则处理
本文件自2026-10-25起为工作流最高权威。旧离线优先、ZIP默认交付、禁止GitHub任务单及旧自动清理规则均被取代，仅作历史记录。科研合同、历史裁决、STOP/PENDING和原始科学证据不得删除或追溯改写。

## 2026-10-27 Owner追加授权：GPT有界低风险微预算裁量（不改变科学硬门）

Owner明确授权 GPT 在 Owner 同意的研究方向内直接签发**逐张冻结任务单**，并在任务内自主批准小规模只读核查、隔离scratch合成no-HA契约试验及其具体有限尝试/重试次数；任务必须显式标记预算、证据、STOP与写入白名单。默认每张任务最多2轮合成检查，每项最多1次工具故障重试；不得将权限泛化为连续自动下单或科研运行许可。HA/HJB/KFE/GE/IRF、真实稳态/校准/调参、经济学机制和公式变更、正式来源冻结、工资统计数据采用或转换、生产部署/模型激活、V010/V011、Results、合并与科研证据清理仍须Owner专项决定。任何实质概念冲突、权限拒绝或越界预算均先STOP并报告Owner。本条由Owner直接批准，不是Codex或模型自行修改权限；本文件其他规则继续有效。具体全文同时记录在 docs/CH5_PROJECT_MEMORY_CURRENT.md。
