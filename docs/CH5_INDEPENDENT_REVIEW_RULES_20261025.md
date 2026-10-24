# CH5 独立审阅规则（Owner批准，2026-10-25）

STATUS=OWNER_APPROVED_INDEPENDENT_REVIEW_RULES
SCOPE=OFFLINE_ZIP_REVIEW
DOES_NOT_AUTHORIZE=HA_HJB_KFE_GE_IRF_OR_FORMAL_V010_MODIFICATION

本文只规定证据处理与裁决，不改变正式V010、科研预算、HA黑箱、来源冻结门或Owner决策权。离线工作流继续优先；GitHub写入仅限Owner明确批准的阶段性治理备份。

## Rule 1 — 固定证据，复用已核验原件
- 固定原始ZIP实际字节身份、字节数和SHA-256；文件名或回执声明不能替代原字节。
- 使用成熟标准库批量核验外层/内层成员、长度、CRC32、SHA-256、manifest、路径安全、重复/大小写冲突和有限隐私模式。
- 已完整核验的原件直接复用，不反复下载、解压或重算；缓存键绑定来源仓库、commit、path/blob或原件身份。
- 不递归扫描无关GitHub Tree；不临时编写ZIP、DEFLATE、SHA或Base64解析器。
- 原字节或工具不可用时记录 `REVIEW_PENDING_IO` 或 `REVIEW_TOOL_ERROR`，不得拼造结果。

## Rule 2 — 聚焦本轮变化和关键证据
- 所有归档成员均做机器完整性核验；语义审阅按风险聚焦，优先候选diff、来源身份、真实接口、工资税与劳动单位、数学推导、测试覆盖和异常情况。
- 已接受且身份未变的组件可引用固定身份和原结论，但仍检查本轮接口影响；身份或关键接口变化不得直接继承旧结论。
- 区分全量机器检查与聚焦语义审阅，不把抽样阅读说成逐项完整审阅。
- Codex自报PASS、测试数量、退出码和自检日志不等于Astra独立验收。

## Rule 3 — 有界执行，尽早作出有证据的裁决
- 一旦有足够证据确认候选缺陷，可提前终止与退修结论无关的检查。
- 退修须列明缺陷位置、证据、修复方向及全部 `NOT_COMPLETED` 项。
- 工具故障不算候选实现失败；不得因无关检查、历史报告缺失或API错误无限扩展工作。
- 不反复调用不支持的API；每次汇报区分已完成、阻塞、未完成和下一步，不静默耗尽会话。

## Rule 4 — 分层裁决
每轮分别记录：`artifact_integrity`、`source_identity`、`numeric_review`、`implementation_review`、`scientific_review`、`privacy_review`、`actual_terminal`、`delivery`、`cleanup`、`not_completed`。
只有本轮合同全部必需检查完成，才可给出完整PASS。归档完整不代表来源身份成立；来源身份成立不代表代码正确；代码和合成数学通过不代表经济学机制已采纳；历史收敛不代表修改后候选收敛；单项PASS不能替代正式来源冻结。

## 科研权限边界
Owner拥有最终经济学方法、科研预算及重大决策权；Codex只执行获批离线合同。除非Owner通过新决策和证据明确更新，保持 `V010=UNCHANGED`、`V011=NOT_STARTED`、`Results=FALSE`、`model_activation=False`、`REAL_GE=False`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`。本规则不授权HA/HJB/KFE/外层固定点/GE/福利/IRF。三个历史PENDING Review及既有STOP/关闭预算原样保留。
