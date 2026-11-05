# 第五章Python多省份HANK主路线图：HA黑箱与外层闭环

DATE=2026-11-05
DECISION_ID=CH5_MULTIPROVINCE_OUTER_CLOSURE_OWNER_ROUTE_20261105
STATUS=OWNER_APPROVED_MAINLINE__DOCUMENTATION_MILESTONE_ONLY
ACTIVE_RESEARCH_MAINLINE=PYTHON_MULTI_PROVINCE_HANK_OUTER_CLOSURE
FORMER_TEMP31_DIAGNOSTIC_ROUTE=HISTORICAL_CLOSED__NOT_ACTIVE_MAINLINE
NEW_SCIENTIFIC_RUN_GRANT=NONE

## Owner决定及覆盖关系

Owner原文：

> 不过我还是先提醒你：整个Moll程序，包括HJB+KFE构成的HA模块都应该视为黑箱。
> 之前的项目在工作流迁移为当前纯本地工作流之前，就在这一块浪费了半个月的时间。
> 请你评估一下如果跳过这一块后续怎么安排任务目标（这块算法可以直接引用Kaplan et.al 2018，我们不需要进行解释）

Owner批准原文：

> 可以，我认为你这个顺序可以，请修正目前线路为主要线路（取代原先temp31线路），保存github路线图文档后我们再继续

据此，当前主线改为：**HA黑箱下的多省份外层闭环 → 31省数据与校准口径 → 基准经济 → 政策实验与第五章写作**。下表阶段1与阶段2可并行准备，其余按依赖推进。

本路线取代此前围绕TEMP31单省点位、HA内部诊断及Moll参考精度的任务推进路线。既有“下一步讨论正式g加权平衡、边界集中或固定点尺度”的安排退出当前任务队列；相关记录作为历史证据保留，不据此自动追加诊断、试价格或算法研究。

“取代TEMP31线路”是任务目标和优先级变更。固定来源56447829ce0e6c3c85552c53c351b26a2452a4bd及现有Python实现继续作为已选开发基础；不改源目录、分支名称、科学模块、既有a*r_a初始化或净工资接口，不重新选源，不移走历史资产。

Local-first职责保持：Codex负责具体授权内工程，Owner保留经济学制度、科学口径、预算、科学接受及受保护/不可逆决定。较早文档的科研保护条款继续有效；与本次“下一目标”冲突的旧安排以本路线为准。

## HA作为完整黑箱的工作边界

- 整个HJB＋KFE及其原汇总视为固定HA模块。冻结原公式、政策/迎风/边界、算子、求解器、停止控制、固定行、归一化及网格；保持既定调用和原返回语义。
- 外层工作只关心输入接口、已有公开输出、省份索引、单位和原调用成功/失败状态；不新增HA内部观测字段、钩子或额外求解。返回失败仍按原保护退出，不修改算法或伪造成功。
- 当前不再安排内部算法解释、行和/固定点追查、条件数或扰动研究、Moll精度比较，也不为这些诊断追加单省价格点。既有观察不删除、不改写为通过。
- 第五章数值方法按Owner指定引用Kaplan、Moll和Violante（2018）；简述所采用方法、HA输入输出和本章扩展，不承担重新解释或证明HJB/KFE算法的任务。此引用不是当前Python实现逐字节等同原作者程序的认证，也不是本文方法创新声明。
- 旧严格HA诊断状态仍按原证据保留，不将补齐HA内部解释或另设内部诊断阈值作为外层静态接线和方案工作的前置任务。本次也不以路线变更授予真实模型运行或正式结果资格。

## 分阶段目标与交付

| 阶段 | 目标与限定范围 | 交付及完成标志 | 运行安排 |
| --- | --- | --- | --- |
| 1 外层生产链接线 | 固定来源中的外层入口、价格/净工资、省份状态 → HA黑箱 → 劳动与资本配置、企业、汇总及价格更新 | 完整调用与数据流图；逐项标记已接通、缺接线、待Owner经济口径；明确省份方向、维度、单位、工资税单次应用及外层残差入口 | 首先只读静态定位和实施计划；本轮未执行 |
| 2 数据与校准口径 | 对齐31省居民地/工作地、人口/就业/有效劳动、工资、税收及资产口径 | 参数分为文献给定、数据构造、待校准三类，逐项对应观测矩；复用既有来源资格与缺口记录，不以合成值冒充观测 | 可与阶段1并行准备方案；真实数据读取、正式采用和校准另按具体授权 |
| 3 最小外层闭环 | 保持HA原样，贯通价格 → 各省HA → 配置与企业 → 价格更新 | 有界多省一轮接线验证；随后按依赖推进31省一轮与外层稳态；每轮可追溯经济汇总、市场清算残差和退出原因 | 未来有具体代码/输入/次数/时限/退出保护的前瞻有限授权后执行；不复用旧7/7 |
| 4 31省基准经济 | 以确定的数据口径和参数构建政策比较基准 | 校准目标表、观测矩拟合、省际基准汇总与外层均衡记录；接受口径由Owner确定，不预填通过 | 校准及真实均衡运行须具体科学决定；当前NOT_RUN |
| 5 政策实验与写作 | 围绕第五章既定政策问题分析省际及家庭异质性 | 基准/反事实、针对本章扩展机制的分解、稳健性、图表及正文；方法与数据部分可先写，结果文字等待真实证据 | 基准成立后按预先确定的对照、指标和有限运行方案执行；不做HA算法消融 |

当前已记录完整31省生产接线尚未认证，真实31省校准和REAL_GE未建立。下一目标针对外层链条缺口，不重复已完成的资产盘点或S01—S03/参考测试。本路线是Owner批准的任务顺序，不是上述阶段已完成的声明。

## 下一具体目标及本次停点

NEXT_ENGINEERING_TARGET=OUTER_PRODUCTION_CHAIN_GAPS_AND_MINIMAL_CLOSURE_PLAN
NEXT_TASK_TITLE=HA黑箱约束下，第五章多省份外层生产链的缺口定位与最小闭环方案
NEXT_TASK_STATUS=PLANNED_NOT_EXECUTED_THIS_MILESTONE

下一目标限定在选定来源的外层入口、工资税、劳动映射、企业、汇总和均衡更新。交付一份有精确代码路径的“已接通／缺接线／待Owner经济口径”矩阵、最短实施顺序及所需检查。遇到经济制度或公式口径待决，列清具体问题交Owner；不回退HA内部研究，也不自行替换科学规则。

本次授权范围仅为主路线修正、本地当前入口对齐及GitHub治理分支文档同步。文档回读完成后结束本轮；不同时启动阶段1实现、模型运行、数据加载或后继任务。后续普通工程继续遵循Local-first，不恢复旧网页GPT派单制度。

## 历史预算、接受状态及保护保持

TEMP31既有诊断CURRENT=CLOSED_COMPLETED_NO_RETRY，累计7/7、零重试；Moll参考3/3关闭、零自动重试。旧初始化3/10、余7仅原8格范围，工资/补录各1/1关闭。没有第8次TEMP31决定、S04或新Moll运行；换路线不创建新预算或跨预算借用。

criteria_reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。未来外层均衡及论文结果的接受口径需按具体科学目标确定，不在本路线中虚设数值阈值，也不把HA引用自动变成当前结果通过。

R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权及16项义务保持。保留历史dirty树、原件、索引、工作树、失败/STOP证据和LOCAL_ONLY载荷；不reset/stash/clean、强推、main合并、删分支、移动证据/缓存或修改Desktop/CUA/全局配置。

## 文档与同步入口

- 当前状态：[CH5_LOCAL_FIRST_STATUS_CURRENT.md](CH5_LOCAL_FIRST_STATUS_CURRENT.md)。
- 工作流：[CH5_ASTRA_WORKFLOW_CURRENT.md](CH5_ASTRA_WORKFLOW_CURRENT.md)。
- Owner决定：[OWNER_LOCAL_FIRST_CODEX_20261101.md](OWNER_LOCAL_FIRST_CODEX_20261101.md)末尾本次记录。
- 旧会话交接：[CH5_SESSION_HANDOFF_20261105_MOLL_KFE_CURRENT.md](CH5_SESSION_HANDOFF_20261105_MOLL_KFE_CURRENT.md)，仅保留来源、预算及证据用途；旧下一步已被本路线覆盖。

PUBLICATION_SCOPE=GOVERNANCE_BRANCH_DOCUMENTS_ONLY
MODEL_BRANCH_AND_CODE=LOCAL_ONLY_NOT_PUSHED
REMOTE_BRANCH=governance/ch5-codex-local-first-20261101

仅同步脱敏治理文档，不推模型分支/科学代码或原载荷，不合并main。已有SSH路径和身份保持；推送失败不自动重试或切换身份/协议。同步完成以实际远端提交及文件Blob/字节数/SHA256回读为准，本地私有回执保存最终身份。旧PENDING_SYNC段落保留为历史，不代表本次交付结果。
