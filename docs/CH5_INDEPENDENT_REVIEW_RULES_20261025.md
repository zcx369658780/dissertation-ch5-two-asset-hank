# CH5 独立审阅规则 V2（Owner批准，2026-10-25）

STATUS=OWNER_APPROVED_INDEPENDENT_REVIEW_RULES_V2
SCOPE=OFFLINE_ZIP_REVIEW
DOES_NOT_AUTHORIZE=HA_HJB_KFE_GE_IRF_OR_FORMAL_V010_MODIFICATION
DEFAULT_WORKFLOW=OFFLINE_MD__LOCAL_CODEX__OWNER_UPLOAD_ZIP__ASTRA_REVIEW
GITHUB_WRITES=EXPLICIT_OWNER_APPROVED_MILESTONE_BACKUP_ONLY

本文是现行独立审阅规则的增补和精简，不重建工作流，不改写历史STOP/PENDING，不改变正式V010、科研预算、HA黑箱、来源冻结门或Owner决策权。Owner拥有最终经济学方法、科研预算及重大决策权；Codex只执行获批离线合同。

## 两阶段、六项硬门

### 阶段A：交付与来源快速门

1. **原件身份与全量机器完整性。** 固定本轮实际原始ZIP字节数及SHA-256。使用成熟标准库一次性检查外层/内层全部成员的长度、CRC32、SHA-256、manifest一致性、路径安全、重复成员、大小写冲突及有限隐私模式。全量机器检查不等于全量语义阅读。
2. **关键来源身份。** 固定候选基线commit/tree，并核对本轮关键源码的repository/commit/path/blob、候选来源关系和唯一性依据。只读取本轮必要的关键对象；不得为复核一条候选而重新扫描/导出整个历史仓库。历史报告可作为有来源的历史证据，但不能表述成Astra本轮重新核验了报告涵盖的全部文件。
3. **取证与工具停止门。** 原字节或必要工具不可用，记录 `REVIEW_PENDING_IO`；审阅器/工具自身错误记录 `REVIEW_TOOL_ERROR`。不得拼造原件或结果、绕过平台控制，亦不得把纯工具故障判作候选实现失败。同一对象读取失败最多进行一次有界恢复；仍失败即停止该对象的重试。

### 阶段B：候选与科学风险审阅

4. **针对性实现审阅。** 以完整候选diff为入口，检查受影响源码上下文、真实调用接口/是否接线、工资税与劳动单位、关键数学推导、测试输入与预期、异常和边界行为。已接受且身份未变的组件可引用既有结论，但仍检查本轮接口影响；身份或关键接口变化时不得直接继承旧结论。
5. **最小充分的独立复核。** 每项关键主张须映射到能区分正确与错误实现的证据。独立复算关键公式、方向/边界和有代表性的数值；检查测试是否覆盖关键错误模式。测试数量、重复输出、Codex自报PASS、退出码和自检日志均不等于独立验收，也不自动构成相互独立的证据。语义审阅须如实标记范围，不把抽样阅读说成逐项完整审阅。
6. **分层科学与交付裁决。** 分别记录下列状态，不允许单项PASS替代完整接受。只有当前合同全部必需检查完成才可给出完整PASS；已有充分证据支持退修时可提前裁决，无需完成与退修结论无关的检查。

## 必须分别记录的裁决字段

- `artifact_integrity`
- `source_identity`
- `numeric_review`
- `implementation_review`
- `scientific_review`
- `privacy_review`
- `actual_terminal`
- `delivery`
- `cleanup`
- `not_completed`

归档完整不代表来源身份成立；来源身份成立不代表代码正确；代码和合成数学通过不代表经济学机制已采纳；历史收敛不代表修改后的候选收敛；任何单项PASS均不能替代正式来源冻结。科学E3、真实数据、单位、财政、HA/GE/IRF等未闭合项必须明确保留，不得因工程或合成PASS升级。

## 有界执行与早停

- 不对无关GitHub Tree进行recursive全树扫描；不反复下载、解压、重算或重建已完整核验的原件。缓存必须绑定固定来源身份。
- 禁止在验收现场临时编写ZIP、DEFLATE、SHA-256或Base64解析器。
- 一旦存在足以支持 `CHANGES_REQUIRED` 的明确缺陷，立即列出位置、证据、修复方向及所有 `NOT_COMPLETED`，停止与退修结论无关的检查。
- 工具故障不算候选失败；不因无关检查、历史报告缺失或不支持的API而无限扩展工作，不重复调用已明确不支持的接口。
- 每次状态汇报均区分 `COMPLETED`、`BLOCKED`、`NOT_COMPLETED`、`NEXT_ACTION`；不得静默耗尽会话预算。
- 普通工程审阅5–10分钟仅为软目标，不是硬性FAIL阈值。复杂科学审阅按风险定界；到达软目标仍未完成时，先报告已完成、阻塞对象、剩余证据和下一步，再决定一次有界继续或暂停。无法计时写UNKNOWN。

## 科研权限与历史保护

保持 `V010=UNCHANGED`、`V011=NOT_STARTED`、`Results=FALSE`、`model_activation=False`、`REAL_GE=False`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`，除非Owner通过新的明确决策和合格证据更新。本文不授权HA/HJB/KFE/外层固定点/GE/福利/IRF，不冻结正式来源，不改变经济学制度。三个历史PENDING Review及所有既有STOP/关闭预算原样保留。

## 与交付、归档及同步的关系

继续执行离线优先流程：离线MD任务单 → 本地Codex → Owner手动上传完整脱敏ZIP → Astra独立验收。GitHub仅用于Owner明确批准的阶段性治理备份/Code Review；不自动创建Issue、Review分支、上传或清理。终审归档、清理及同步状态分别报告；PENDING时不提前清理。GitHub、Project Sources、本地Codex三个平面只有各自有真实回执后才能称同步。

## 2026-10-25 Owner批准：中断恢复与有界分段验收协议（V2补充，不替代六项硬门）

本补充针对长会话验收中断与范围漂移，优先于任何要求一次性完成超长审阅、重复读取原件或扩展无关历史对象的旧执行措辞；不追溯改变既有任务合同、已归档裁决、STOP/PENDING、预算或科学权限。

### A. 分段、检查点与回复预算
1. 将一次离线ZIP验收固定为最多三个审阅阶段：A交付/来源硬门；B关键实现、数值和科学风险；C分层裁决与归档建议。每阶段形成可独立理解的短检查点，明确 COMPLETED、BLOCKED、NOT_COMPLETED、NEXT_ACTION。不得把检查点误写成最终PASS。
2. 发生回复截断、会话中断、工具输出截断或状态不确定时，停止继续扩展；恢复时先重读本任务的固定合同、最近检查点和已核验对象清单，复用已完成证据，不从头重跑，也不依据未见到的工具结果推断成功。
3. 工具调用按必要性最小化。单次输出只保留与裁决有关的摘要、关键行/字段和身份值；大段源码、全文件、历史记录不得直接倾倒到会话。需要深入时只读相关文件/行段。
4. 不因对话可能中断而把一个任务拆成未经Owner批准的新任务；同一任务内只可继续已冻结范围。若证据不足或会话预算将尽，提交中间检查点并暂停。

### B. 来源身份与范围纪律
1. 先固定任务包自身声明的 repository、commit、tree、path、blob 和输入ZIP身份。只核对本轮 critical_evidence 清单中的必要对象；不因某个GitHub读取接口返回内容不合适，就换用未经证明等价的端点或扩大到其他历史commit。
2. GitHub Contents API 返回的 blob SHA 与文件内容可用于身份核对，但必须在相同 repository/commit/path 下比较；不可将不同commit的Blob差异直接称为候选缺陷。若接口/路径/编码返回不支持或原字节无法取得，记录 REVIEW_PENDING_IO 或 REVIEW_TOOL_ERROR，并在一次有界恢复后停止该对象。
3. 固定commit的tree/parent和候选来源账本与ZIP manifest分别核对。任何不一致先区分：真正来源冲突、查询ref/路径错误、工具返回形态问题、证据缺失。未完成归因前不得将其归为实现失败。
4. 已完整核验的归档只检查一次并缓存结论；不反复解压、复算或重复打印同一清单。历史回执只作历史证据，不冒称本轮重验。

### C. 语义审阅与早停
1. 语义审阅以任务唯一问题和风险清单为边界；先看交付摘要、关键字段账本和对应源码片段，再按需追查原件。不得把“30项账本/98条片段”等数量当作自动PASS，也不得为穷尽无关细节扩大范围。
2. 一旦已出现足以支持 CHANGES_REQUIRED 的明确候选缺陷，可提前停止，并列出定位、证据、建议修复方向及 NOT_COMPLETED。若只是工具或取证故障，则记 REVIEW_PENDING_IO/REVIEW_TOOL_ERROR，不转嫁给候选实现。
3. 如证据支持有限结论，只能使用 PASS_BOUNDED 并明确边界；完整PASS必须完成本任务所有必需硬门。artifact_integrity、source_identity、numeric_review、implementation_review、scientific_review、privacy_review、actual_terminal、delivery、cleanup、not_completed 必须分别记录。

### D. 本轮落地与权限
本次协议修订仅为治理文档更新，不启动新的科研/实现任务，不执行源码、测试、预检、模型、HA/HJB/KFE/GE/IRF，不改变正式V010，不冻结来源，不清理旧PENDING对象。Project Sources更新包是手动上传覆盖层；GitHub治理文档、Project Sources和本地Codex仍是三个独立平面，未获各自回执不得声称同步。
