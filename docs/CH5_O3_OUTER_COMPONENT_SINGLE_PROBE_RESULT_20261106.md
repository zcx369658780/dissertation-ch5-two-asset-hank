# O3原外层组件单次有限验证完成记录

DATE=2026-11-06
GRANT=CH5_O3_OUTER_COMPONENT_SINGLE_PROBE_20261106
CURRENT=CLOSED_CAPTURED_NO_RETRY__1_OF1_USED__NO_SUCCESSOR
OWNER_APPROVAL=TRUE_HISTORICAL_FOR_THIS_GRANT_ONLY
VERDICT=FIXED_SYNTHETIC_OUTER_COMPONENT_CAPTURE_AND_HANDOFF_VERIFIED
SCIENTIFIC_ACCEPTANCE=FALSE
HA_HJB_KFE_CALLS=0
AUTO_NEXT=FALSE

## Owner决定与实际执行

Owner对治理提交06cb34cc、代码候选848feaf对应的[具体方案](CH5_O3_OUTER_COMPONENT_SINGLE_PROBE_PLAN_20261106.md)回答：

> 授权该一次性方案

被确认的问题是：固定两省合成输入，新增独立1次验证进程、最长30秒；劳动1、资本1、企业2、工资1、货币1、财政诊断1，共7次原入口；依赖如需，至多1次只读Windows版本查询；HA/HJB/KFE、初始化、O2原工厂及GE均0，失败零重试，不借用旧额度。完整Owner问题、回答与字节锁定的原始决定在LOCAL_ONLY回执保存。

先复核两树真实Git根/分支/HEAD/remote及既有改动、16文件物理pin和6缓存基线；注册独立OWNER_DECISION后，由父进程独占登记ATTEMPT_CLAIM，再启动唯一worker。原contract仍保持PROPOSED_NOT_AUTHORIZED的方案原文，由本次Owner决定覆盖执行权限，未改写原方案、执行器、夹具或任一原组件。

实际一次成功返回，父监督状态CLOSED_CAPTURED_NO_RETRY，worker exit0，stdout/stderr为空；监督实测约1.062000秒，小于30秒。唯一额度1/1已用，自动重试0，未启动第二次。批准允许的只读ver查询实际0。该时限是父进程监督实测，不是模型均衡收敛速度或HA效率测量。

| 原入口 | 调用尝试 | 原源码进入 | 成功返回 |
| --- | ---: | ---: | ---: |
| temp31_worksite_tax.reconstruct_temp31_worksite_labor | 1 | 1 | 1 |
| capital_allocation.allocate_productive_capital | 1 | 1 | 1 |
| firm.evaluate_firm | 2 | 2 | 2 |
| wage.composite_household_wages | 1 | 1 | 1 |
| monetary.taylor_assignment | 1 | 1 | 1 |
| fiscal_diagnostics.national_fiscal_diagnostics | 1 | 1 | 1 |
| 合计 | 7 | 7 | 7 |

这7次只计方案列明的原公开入口，包含其内部原私有辅助函数和数据类工作的调用过程。21条保存trace依次构成7组CALL_ATTEMPT→SOURCE_ENTRY→SOURCE_RETURN，顺序、来源标签、每入口计数和trace SHA256均完成离线复核。HA/HJB/KFE/原HA汇总、初始化、root、MATLAB、O2原工厂、旧runner、外层控制迭代、31省、GE、IRF、政策执行均0。

## 已获得的有限证据

本次已不只是预给定所有外层阶段结果：六类原外层组件确实在固定两省输入上产生了返回，结果进入既有外部A1/财政账及一轮候选状态拼装；原一轮生产代码本身未改。可确认的是这组固定输入下的调用可达性、返回捕获及以下外部交接：

- 原劳动核输入仍是H规模，保存的原劳动矩阵按来源列乘p一次后，与两个原企业实际收到的目的地劳动精确相等；未归一化劳动、未以E替换家庭H。
- 原资本入口收到预给定家户At、H、旧ra及跨省比例，返回资本进入企业；Bt不进入其接口。家户输出仍是合成预给定量。
- 两个企业实际Lt_prev仍按预先声明取当轮家户Lt，不改用进入状态的Lt_prev；此观察不裁决其经济时序是否合适。
- 原企业输出的当轮gross工资进入原净工资入口和外部工资税账；工资税按目的地tau×gross工资总额计算，A1劳动已经聚合，不再乘H/p或在HA再扣税。
- 家户Tt、AtTax原值和符号保留，省级财政边界分别乘同源H一次，连同保存的原Corptax/GovInv/ra组成金额；原企业旧Govinc独立保留，没有用它代替新合同账。
- 由保存返回与输入作标准库算术核对，原财政诊断GovSurplus与候选状态拼装的值精确一致；这是同一已定账项交接检查，没有新增数值容差或财政平衡接受标准。
- 候选状态的净工资、利率、前轮Yt/pit等交接与保存的阶段返回/原输入匹配。候选convergent=true来自合成家户声明，**不是观测到的HA收敛**。

完整参数、原返回、逐省候选量、财政金额及证据清单仍LOCAL_ONLY；GitHub只发布本份脱敏结论与治理入口。有限组件可计算不说明这组夹具经济合理、真实数据单位合格、财政已经平衡或多省稳态成立；本轮不对这些问题另设标准或修算法。

## 身份、保护与限定验收

GOVERNANCE_PLAN_COMMIT=06cb34cc4cc0f3b767b91f7dab77186fce89caa2
MODEL_CODE_CANDIDATE=848feafec5e7e01ff96c38251e3f0ef4a44b91f0
MODEL_CODE_TREE=b620da06301dc17a1c66b3051fe1ef44c0ec04b5
MODEL_PRE_RUN_DOCUMENT_HEAD=4abc459da884eac2559f14feb01ff247fa4eb816
CONTRACT_SHA256=9a5666380e50d3074059276592464236e0f9b1014592b0f0fa15b4724d7e48f4
WORKER_SHA256=e516e05284bef83b899ee3a40763ca765b7d82e25b77a6ed67b8496d8c5048cc
FIXTURE_SHA256=7fa51c0ba111fb57ac5fd204e7877dfd66a63856f3aedd02cad92dea87c1be3a
OWNER_DECISION_SHA256=08c3c8600c2ff1031cb420eb43d243620913aeb94493431cf9b2915ba26795a6
SOURCE_CALL_TRACE_SHA256=66a0236665ed4cb95d497785e38ad311bde24c28e88362ef631d94de281124e0
WORKER_RESULT_SHA256=5183a8553e86d6112835d8b6279541d0fc12dd184f186a99086c750e729b04d7
FINAL_PROBE_RECEIPT_SHA256=2e74b5b705dad4e7fd229206e09f7a1de5f0ba3fe427c33df7dc263c65308151

运行前已完成的21项标准库/mock保护检查没有重复整套运行；本轮使用已批准原执行器实调用一次，再仅读取保存JSON/trace作离线复核，没有新增科学生产进程或导入NumPy/原模型来重算。16文件身份和6份旧缓存运行前后完全保持，新缓存0，科学源码与执行器修改0，默认0子代理。

MODEL_CODE_PUSHED=FALSE
O2_NATIVE_FACTORY=NOT_RUN_SUPPLIED_FIELD_VIEW_ONLY
NEW_NET_WAGE_HA_CONSUMPTION=NOT_RUN_NOT_RELEASED
REAL_31_PROVINCE_DATA_OR_CALIBRATION=NOT_RUN
HA_AND_FORMAL_SOURCE_ACCEPTANCE=FALSE
REVIEW=MAIN_AGENT_SELF_REVIEW_AND_SAVED_EVIDENCE_CHECK__NOT_INDEPENDENT_SCIENTIFIC_REVIEW

保护仍限已审阅的Python审计/profile与父超时，不声称OS级隔离、内存硬限制、系统依赖全覆盖或GLOBAL_STOP认证。不借运行成功关闭16项科学/保护义务。TEMP31 7/7、Moll 3/3、工资/补录旧额度保持关闭；旧初始化余额仅原8格。严格reference/thresholds仍null；scientific_acceptance、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE全部FALSE。

R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权、历史dirty树及HEAD/index/porcelain基线、原件/缓存/LOCAL_ONLY保持；未reset/stash/clean、强推、合并main、删分支、移动证据或改Desktop/CUA/全局配置。模型代码/分支仍仅本地，API写入0，治理文档按原SSH分支同步，最终逐文件远端回读以私有交付回执为准。

## 当前停点与后续依赖

本grant已经1/1关闭，owner_approved只记录本次历史许可，不能授权第二轮、HA消费或更大规模运行。本轮结束于证据保存和治理同步，不自动启动后继科研。

下一项工程可针对O2原工厂整合和HA黑箱消费边界准备具体接入方案，复用已有接口与这次有限组件见证；原净工资消费门、真实家户返回资格、实际p与单位/来源、家户收入/劳动激励兼容和外层均衡控制口径仍须分别闭合。任何后继科学调用须对应新的具体范围、输入、预算和适用Owner决定。不得把本次运行成功当作HA/31省/基准经济或正式Results的许可。

当前入口：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。[原准备方案](CH5_O3_OUTER_COMPONENT_SINGLE_PROBE_PLAN_20261106.md)保留其当时未授权状态，不据历史待批文字重复申请本次已经完成的额度。
