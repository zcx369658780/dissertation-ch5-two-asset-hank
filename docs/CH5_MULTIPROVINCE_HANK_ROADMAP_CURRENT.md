# 第五章Python多省份HANK主路线图：HA黑箱与外层闭环

最新O3进度：[原外层组件单次有限验证方案](CH5_O3_OUTER_COMPONENT_SINGLE_PROBE_PLAN_20261106.md)与执行器准备完成，21项标准库/mock保护检查及16文件身份核对通过。拟定两省合成输入、1个worker/30秒、7次原组件入口及至多1次只读Windows版本查询，零重试；尚未获新运行批准，真实worker/原组件/HA调用均0。预给定一轮23项是既有工程证据，O2原工厂、完整生产链与科学接受仍未建立。下一步仅等待Owner对该具体新方案的有限许可。


DATE=2026-11-05
DECISION_ID=CH5_MULTIPROVINCE_OUTER_CLOSURE_OWNER_ROUTE_20261105
STATUS=OWNER_APPROVED_MAINLINE__COMPONENT_PROBE_PREPARED_NOT_AUTHORIZED
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
| 1 外层生产链接线 | 固定来源中的外层入口、价格/净工资、省份状态 → HA黑箱 → 劳动与资本配置、企业、汇总及价格更新 | 完整调用与数据流图；逐项标记已接通、缺接线、待Owner经济口径；明确省份方向、维度、单位、工资税单次应用及外层残差入口 | 静态定位、O1/O2接口、A1与财政及预给定阶段一轮拼装已完成；真实O3调度/运行未执行 |
| 2 数据与校准口径 | 对齐31省居民地/工作地、人口/就业/有效劳动、工资、税收及资产口径 | 参数分为文献给定、数据构造、待校准三类，逐项对应观测矩；复用既有来源资格与缺口记录，不以合成值冒充观测 | 可与阶段1并行准备方案；真实数据读取、正式采用和校准另按具体授权 |
| 3 最小外层闭环 | 保持HA原样，贯通价格 → 各省HA → 配置与企业 → 价格更新 | 有界多省一轮接线验证；随后按依赖推进31省一轮与外层稳态；每轮可追溯经济汇总、市场清算残差和退出原因 | 未来有具体代码/输入/次数/时限/退出保护的前瞻有限授权后执行；不复用旧7/7 |
| 4 31省基准经济 | 以确定的数据口径和参数构建政策比较基准 | 校准目标表、观测矩拟合、省际基准汇总与外层均衡记录；接受口径由Owner确定，不预填通过 | 校准及真实均衡运行须具体科学决定；当前NOT_RUN |
| 5 政策实验与写作 | 围绕第五章既定政策问题分析省际及家庭异质性 | 基准/反事实、针对本章扩展机制的分解、稳健性、图表及正文；方法与数据部分可先写，结果文字等待真实证据 | 基准成立后按预先确定的对照、指标和有限运行方案执行；不做HA算法消融 |

当前已记录完整31省生产接线尚未认证，真实31省校准和REAL_GE未建立。下一目标针对外层链条缺口，不重复已完成的资产盘点或S01—S03/参考测试。本路线是Owner批准的任务顺序，不是上述阶段已完成的声明。

## 阶段1进度与下一具体目标

外层调用链及已接通/缺接线/待Owner经济口径矩阵已完成：[缺口定位与最小闭环方案](CH5_OUTER_PRODUCTION_CHAIN_GAPS_AND_MINIMAL_CLOSURE_PLAN_20261105.md)。静态源码定位不等于生产接线、数值运行或均衡接受；本次未导入/执行科学代码。

NEXT_ENGINEERING_TARGET=O3_COMPONENT_PROBE_OWNER_DECISION_PENDING
NEXT_TASK_TITLE=审阅已锁定两省单次外层组件方案并等待Owner新有限许可
NEXT_TASK_STATUS=PROBE_PREPARATION21_CHECKS_PASS__16_PINS_MATCH__REAL_CALLS0

[预给定一轮拼装记录](CH5_O3_SUPPLIED_ONE_TURN_ASSEMBLY_20261105.md)已交付，O2只作现有字段视图/AST兼容，新净工资原pending消费门保持关闭；不是完整生产执行或科学接受。具体实调用方案已在2026-11-06准备完成，等待Owner新独立有限许可；不自动执行或重开额度。

[A1尺度接口记录](CH5_O3_A1_SCALE_INTERFACE_IMPLEMENTATION_20261105.md)已完成历史角色恢复和预给定H/p/E、原劳动矩阵按列乘p的工程片；真实p面板尚未采纳，不填默认值，不将历史O/I/S记录改写为完整数据。

[财政金额组合记录](CH5_O3_PROVINCIAL_FISCAL_COMPOSITION_20261105.md)已交付，连接已采纳账项与原企业其它金额项；旧生产链不改，真实来源/单位、财政/GE接受和运行门保持。

[Tt/AtTax决策稿](CH5_O3_TT_ATTAX_UNIT_CONTRACT_PROPOSAL_20261105.md)已核对论文转移总额、当前家户输入及O2未放大输出，分列家户量与省级金额；Owner已采纳财政边界各乘H一次，独立模块13项限定检查通过，见[实施记录](CH5_O3_HOUSEHOLD_FISCAL_IMPLEMENTATION_20261105.md)；不将内部合同当作真实货币/人口/年频单位认证。

已形成[财政工资税金额合同决策稿](CH5_O3_FISCAL_PAYROLL_CONTRACT_PROPOSAL_20261105.md)：建议tau乘同轮企业输出gross工资与已聚合A1劳动；迭代工资版本、原裁切补偿及省级财政单位门分别记录。Owner随后已采纳工资税子合同，独立子账14项限定检查通过，见[实施记录](CH5_O3_PAYROLL_TAX_IMPLEMENTATION_20261105.md)。其余G04单位/E3与完整O3保持未完成，不建立财政平衡目标或运行许可。

已有批次/工资结构优先复用，不重建同用途stub框架。O1结构适配结果见[接口工程记录](CH5_OUTER_PRODUCTION_WAGE_INTERFACE_ADAPTATION_20261105.md)；Owner已明确允许纯接口适配；O1结构兼容已实施并验证，原pending科学消费门仍关闭。具体任务、完成标准与依赖见[任务清单](../tasks/todo.md)。

真实组合沿既定A1（企业劳动E=pH、家庭聚合H不变）及目的地税/单次扣税推进，不重新选择归一化；工资税金额子合同已采纳；Tt/AtTax的内部H聚合已采纳，实际物理单位/来源资格、收入兼容与基准拟合/均衡目标仍待具体证据/采纳。O1仅完成后轮工资结构兼容，真实生产来源资格仍未建立。不得绕过已有门或以此重开HA内部研究。O1/O2结构工程、O3两份子账及预给定省级财政金额组合已完成，完整O3一轮未接通，不启动科学后继任务；普通工程不恢复旧网页GPT派单制度。

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

O2结果：[多来源批次适配](CH5_OUTER_MULTI_ORIGIN_BATCH_ADAPTER_20261105.md)。O3以[既有决定恢复记录](CH5_O3_LABOR_WAGE_TAX_DECISIONS_RECOVERED_20261105.md)纠正此前遗漏：A1已选、A2未选；工资税子合同已由Owner采纳并完成独立工程，Tt/AtTax内部H聚合也已采纳并独立实现；预给定财政金额组合也已完成18项限定检查；A1规模接口及预给定劳动适配也已完成15项限定检查；预给定一轮拼装也已完成23项限定检查；下一步准备有限实调用验证方案，O2原工厂整合、真实调度及真实p/单位/来源/收入兼容继续保留，不回到HA内部算法研究。
