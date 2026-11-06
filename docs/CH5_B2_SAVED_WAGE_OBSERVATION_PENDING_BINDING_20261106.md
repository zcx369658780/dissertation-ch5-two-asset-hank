# B2保存工资观察与待许可消费目标绑定工程

DATE=2026-11-06
OWNER_CONTINUATION=可以请继续
STATUS=B2_SAVED_OBSERVATION_AND_PENDING_TARGET_BINDING_ENGINEERING_COMPLETE
EXECUTABLE_CONSUMER_PERMISSION=NOT_IMPLEMENTED_NOT_GRANTED
MODEL_ENGINEERING_CANDIDATE=61f04f1f4dae47a2a063f64c29a2309f95424468
MODEL_ENGINEERING_TREE=14be1576feca592560ac8127925fc8d117b731e1
MODEL_PARENT=a3753370eb749244bd0a093325adba37ad1764ca
GOVERNANCE_PARENT=6d018072ea410ef428c6e8dd601e6cac429fa335
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED
NEW_SCIENTIFIC_GRANTS=0
SCIENTIFIC_KERNEL_CALLS=0
SUBAGENTS=0

## 完成的工程行为

复用原ProductionWageRecord、PendingWageEnvelope、WageInvocationContext、BindingContext和工资六类输入字节pin，新增保存观察核对与待许可目标绑定。没有重新计算工资，没有调用原七入口探针、初始化、root、HJB、KFE、原汇总或模型；所有HA公式/网格/控制及原a*r_a初始化、净工资和AtTax重构保持。

保存观察一致、目标声明匹配、实际可消费三者仍分开。新接口只实现前两项；可执行消费许可和唯一worker准入分支尚未实现或批准。原require_production_wage_consumer_ready函数的完整AST与改动前相同，仍走原PRODUCER_INVOCATION_NOT_VERIFIED拒绝路径；新的待许可目标入口始终报SCOPED_CONSUMER_PERMISSION_NOT_GRANTED。record/envelope/binding的consumer_ready、producer_invocation_verified、permission_granted、scientific_acceptance和model_activation等原有/新增资格均按各类型保持FALSE。

## 保存观察核对

新增outer_saved_wage_observation.py仅用标准库与既有元数据类型，接收调用方明确提供的封存bytes及独立可信清单，不读文件、不导入模型/NumPy/SciPy、不运行shell或回调。专用reader只针对已关闭CH5_O3_OUTER_COMPONENT_SINGLE_PROBE_20261106，不建立通用科研授权框架，也不修改旧9源/10角色工资核对器。

| 输入范围 | 本轮实际核对 | 限定含义 |
| --- | --- | --- |
| 9份保存载荷 | 原contract、fixture、Owner决定、attempt claim、worker entry、进程输出、trace、worker result、final receipt的大小/SHA与角色唯一完整性 | 9份载荷不是旧9个源码角色；调用方pins本身不是Owner身份认证 |
| 原有限许可 | 固定grant/contract/fixture/worker身份、1worker/30秒/7入口/ver≤1/HA0/零重试及不借旧额度；决定与claim哈希相连 | 只核对该次历史许可，不生成下一次许可 |
| 监督与返回 | exit0、stdout/stderr空、唯一worker entry、CLOSED_CAPTURED_NO_RETRY、实际计数及资格FALSE | 保存记录一致，不声称当前重新执行 |
| 21条trace | 7组attempt→entry→return，精确顺序/标签/计数、trace哈希、工资参数与同轮企业gross输出 | SOURCE_ENTRY没有保存frame filename；源码归属依赖固定原worker中的guard及其锁定源码，不补造帧元数据 |
| 工资血缘 | 原生成快照、gross工资、目的地税、phi/sigma、偏好六类字节及原返回工资、候选w一致 | 不重算工资、不再次扣税、不采纳真实收入/单位 |
| 来源范围 | 保存14模块集合与其原source_bundle身份保持，生成轮1→进入轮2上下文逐项一致 | 不是旧9角色SourceBundleReceipt，也不是完整HA消费者源码闭合认证 |

返回SavedOuterWageObservation只称recorded_invocation_consistent=TRUE；live_execution_verified、consumer_ready、scientific_acceptance、model_activation均FALSE。收据摘要和元数据在复用时重新核对，异常标签先检查类型，拒绝其自定义比较回调。它是数据一致性收据，不是密码学凭证、实时生产认证或OS保护证明。

## 原记录附加与待许可目标

bind_saved_production_wage_observation创建同一原类型的新记录，保留原envelope对象、输出bytes及工资数值；原记录不改。saved_observation与工资上下文、六输入pin和原输出必须完全对应，重复附加或替换数值拒绝。原共享Temp31NetWageInputs和O2工厂仍使用同一record引用，不需要修改初始化/HJB/policy数值文件或新增内部字段。

prepare_pending_wage_consumer_binding进一步绑定现有进入轮BindingContext、明确origin_index、封存进入快照和单列consumer_manifest。检查省序/期次/来源身份、快照SHA、原rah/rb/Tt/rb_gap/w数据以及工资原值；工资生成快照与进入快照各保留自己的身份，不强迫两者相同，也不把后轮工资重标为首轮19。

consumer_manifest必须显式标DECLARED_CONSUMER_SOURCE_MANIFEST_NOT_VERIFIED，拒绝重复/乱序、绝对/越界路径标签、错误大小/摘要；本接口不读取这些源码文件、不认证内容或完整依赖闭合。生产者14模块来源字段不替换为消费者manifest哈希。网格字段也只是目标元数据，不等于实际网格已读取/核对。未来运行前仍须锁完整消费者源码/网格与真实输入。

PendingWageConsumerBinding只能由工厂生成、不可变且permission_granted=FALSE。直接构造、伪造ready/Owner布尔值、修改绑定摘要或错误目标均拒绝；不存在接受某段Owner JSON后自行开启HA的分支。该声明不能用来创建新claim、借用旧额度或绕过原消费门。

## 限定检查与证据资格

最终25项通过：17项标准库保存证据/拒绝检查，2项同原输入对象与原生O2绑定检查，6项B1相关回归；不是把重复执行的早期检查累加成25。首轮16项通过，补原生传递与类型保护后形成最终17+2+6。日志分别保留，既有全部科研测试未重跑，旧探针未重跑。

覆盖真实保存记录正例，以及缺/重角色、大小/摘要漂移、重复JSON/非有限值、Owner/claim/监督/计数不符、trace顺序/标签/长度错误、工资参数或候选w变化、异常标签比较、记录/摘要/资格篡改、错省/错轮/错来源/错进入快照、声明源码标签错误、重复绑定和未授权门拒绝。两项原生检查确认同一个附加见证record经原输入容器重建及O2请求准备完整保留，并实际调用原共享资格检查仍拒绝；不是只检查新数据类。

17项标准库模式无数值模块导入；原生2项及B1的6项沿用B1真实O2/NumPy数组与未用SciPy求解依赖的一触即停哨兵隔离。最终各模式原科学函数进入0、外部命令/网络动作0、SciPy哨兵调用0；不认证真实SciPy/HA运行兼容、不验证HA收敛或实际单位。原闭合probe目录的文件名/字节/SHA完全保持，旧6缓存不变/新增0；无新科学worker、无新运行grant或科学接受。工程自审不称独立科学评议。

## 文件身份与旧锁定范围

只修改原外部工资桥，并新增专用核对模块和测试，共3路径。以下为本次本地代码候选的Git Blob与物理字节身份；不是给旧探针改pin，也不是科学来源冻结。

| 路径 | Git Blob | 物理字节 | 物理SHA256 |
| --- | --- | ---: | --- |
| src/ch5_two_asset_hank/multi_province/outer_saved_wage_observation.py | 3c0f0f55f411d014f3a2bdb453ee6f608b49ae63 | 15023 | 361e58720792df5008fd19120003c4fc9f5e5da8cdd2c9f98cfc27ced7e70c5b |
| src/ch5_two_asset_hank/multi_province/outer_production_wage_bridge.py | 10b435de0dfc48f86fbaa24627c47196c36ad5cf | 12751 | 2ddd07f34618d131cdc23a7c052cddc1f4dff552835d4df19c333fb3b7e28e18 |
| tests/test_outer_saved_wage_observation.py | febad4777f2e306c5a6284d7c006cf160d3ce148 | 20537 | f4b46c3045d89ed004145ac0b5bf788af1cfda821ab454cdfa4c44778a7bac6d |

旧7入口contract/worker/fixture/证据均原字节保留，其14源码中的外部工资桥历史SHA仍为3038df68e147d9826649cdf16b4f0ea5cba2de5251b6054ed68e245fcbdc06ad。本轮纯元数据接口改变了当前工作树的该文件，因此**当前物理文件不再全匹配旧探针清单**，这不是旧观察失效或可续跑的理由。旧来源可由其原Git提交/私有原件追溯，已关闭1/1不能再执行；不更新旧清单、不重封旧claim、不拿旧probe检查当前新增依赖。未来执行器须锁本轮新增模块在内的新完整消费者manifest。

原temp31_wage_evidence_preflight、共享输入模块和全部HA/网格/数值文件未改；新记录只提供旁挂外部元数据，不改原回报、工资、劳动、税或归一化算法。当前代码/测试与载荷仅本地，GitHub只同步脱敏工程报告与当前入口，API写入0。

## 下一项：B3外部执行器及有限准入准备，不运行

下一工程目标是把已有原生O2请求、保存见证及待许可目标，接到HA黑箱外部的具体执行器准备：锁完整源码/网格/输入、原AtTax外部重构交接、每入口计数/时限/资源和失败退出；可执行的消费许可/唯一worker准入仍需结合该具体方案实现并保持未授权默认拒绝。不能仅凭本轮数据绑定发起HA或新增价格点。

方案具体、可审阅后，适用Owner有限许可才执行；本轮未指定新科学输入、发放额度、生成运行claim或批准B3。TEMP31 7/7、Moll 3/3、七入口观察1/1及工资/补录关闭/零重试，旧初始化余额仅原8格，均不跨借。严格reference/thresholds仍null，scientific_acceptance、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。

A1/工资税/财政H聚合已定不重问；实际p与来源单位、收入/劳动激励兼容、Lt_prev、R/P及外层均衡控制口径仍按旧记录，不自行作科学决定。R12/R13/WASM、保护重绑定未授权、16项义务及历史dirty树/原件/缓存/LOCAL_ONLY保护保持，不reset/stash/clean、强推、合并main、删分支、移动证据或修改Desktop/CUA/全局配置。

前置：[B1原生集成与接入方案](CH5_O2_NATIVE_FACTORY_AND_HA_CONSUMER_BOUNDARY_PLAN_20261106.md)。当前：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。最终模型文档HEAD、治理提交及逐文件回读按私有交付回执记录。
