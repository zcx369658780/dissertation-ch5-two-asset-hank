# O2原生工厂整合、B1集成检查与HA黑箱消费边界

DATE=2026-11-06
STATUS=B1_NATIVE_O2_INTEGRATION_ENGINEERING_COMPLETE__B2_NOT_IMPLEMENTED__NO_HA_OR_GATE_RELEASE
OWNER_CONTINUATION=可以请继续
MODEL_SOURCE_HEAD=a05ba804489d7e8c93ea6e0fcaf9ad41fb69370b
GOVERNANCE_PARENT=34da5e0305f02a0c96f3d8a254704d211d82c31f
MODEL_CODE_CANDIDATE=848feafec5e7e01ff96c38251e3f0ef4a44b91f0__LOCAL_ONLY
EXISTING_PRODUCTION_SOURCE_EDITS=0
NEW_TEST_PATHS=1
SCIENTIFIC_SOURCE_FUNCTION_CALLS_FINAL_CHECK=0
B1_ENGINEERING_CANDIDATE=ab156e3b7f54c9abf53ed9261a5c5ddc168598c9
B1_ENGINEERING_TREE=fb701b9636451b6800e959392850a591a32587e8
NEW_RUN_GRANTS=0
SUBAGENTS=0

## 本次结论

已直接完成**真实O2工厂生成的对象接入既有一轮拼装**的B1工程片，6项集成检查通过，只新增一份测试，不另写同用途包装层、不调用HA。随后按B2外部见证/有限许可绑定、B3黑箱执行器的依赖推进；B2/B3未实现，七次原组件调用成功及本次B1均不授予HA工资消费许可。

HA原HJB/KFE/原汇总、算法/网格/参数控制/原post选择/原归一化继续冻结；本方案只讨论输入输出与外部调度，不解释或修复HA数值算法。AtTax沿原外部重构保持；A1、工资税、财政H聚合和原a*r_a初始化决定均不重开。

## 现场与既有证据的准确范围

两树实际Git根、分支、HEAD、remote和既有改动匹配上轮交付；治理树干净，模型树只有既存两处缓存目录未跟踪。方案静态阶段定点读取15份代码/测试，未导入模型或NumPy；随后在普通工程授权内完成下述B1新集成测试。它加载原接口/容器定义和真实NumPy数组依赖，SciPy数值求解依赖隔离为未被调用的测试哨兵；不认证SciPy/HA实际运行兼容。没有启动科学worker或重跑既有测试。代码图谱已存在，但缺新适配器及部分消费门调用边，故关键结论以当前物理文件和AST核对为准；未重新索引其它项目。

必须澄清“O2原工厂未运行”的范围：2026-11-05的O2专项工程测试**已经在预给定数据上执行过prepare_household_batch与assemble_household_batch**，20项O2加15项相关回归通过；这不应被抹去。2026-11-06的七次原组件探针和此前一轮23项检查采用O2字段视图，没有在那条组合链中运行这两个工厂，也没有真实HA返回。因此，B1补齐了**原生对象进入一轮的组合工程见证**；这不是重新证明工厂存在或重复原20项专项测试，也不证明真实HA批次。

## 边界与复用位置

| 边界 | 当前文件/入口 | 已有能力 | 仍缺的接线或资格 |
| --- | --- | --- | --- |
| O2准备 | multi_province/outer_ha_batch_adapter.py:181 prepare_household_batch | 校验进入快照/省序/工资期次；创建原Temp31NetWageInputs | B1已用实际PreparedHouseholdBatch，不再只用SimpleNamespace；仍不证明HA执行 |
| O2组装 | 同文件:198 assemble_household_batch | 同批次、同request/inputs、完整唯一回复，复制五项原值到PreFrozenHouseholdOutputBatch | 真实HA回复及执行见证未建立；现有scope/资格FALSE必须保留 |
| 一轮拼装 | multi_province/outer_one_turn.py:145、218 | 读取现有O2字段，校验A1/资本/企业/工资/财政交接并生成只读候选状态 | B1已完成实际AssembledHouseholdBatch组合；真实HA返回和完整生产运行仍缺 |
| 工资结构 | multi_province/outer_production_wage_bridge.py:89 | ProductionWageRecord保留封存工资数值与上下文 | 它与PendingWageEnvelope都明确是结构/待核记录，不能改ready/verified布尔值放行 |
| 真实消费 | 同文件:125 require_production_wage_consumer_ready → temp31_wage_evidence_preflight.py:281 | 旧门显式报PRODUCER_INVOCATION_NOT_VERIFIED | 保存的生产者观察不会自动改变此门；需单独匹配将来的具体有限许可 |
| 共享输入边界 | multi_province/temp31_ha_taxfree_bootstrap.py require_netwage_inputs | 所有ProductionWageRecord进入数值消费者前经过上述门 | 当前初始化、HJB和policy均会调用；不只初始化检查一次，也不能用首轮19标签绕过 |
| 旧科学worker | validators/multi_province/temp31_first_origin_worker.py:96、261—321 | 保留原初始化→HJB成功→正式post KFE→原汇总的已执行边界 | 其prepare固定来源0、首轮19、旧预算/诊断；不能改名续用为后轮多省工厂 |
| 原汇总输出 | exports/matlab_faithful_two_asset_ha.py:686 | 原返回c_ss/l_ss/a_ss/b_ss等既有字段 | 不直接返回O2所需AtTax，不新增HA内部返回字段 |
| AtTax外部重构 | validators/multi_province/mp4c_python_annual_production.py:175—181 | 旧外层以同次原g/cell_weight、原资产回报与a_ss重构AtTax后组成五项输出 | 该旧runner还用旧含税输入/旧初始化/年度31省调度，不能整体调用；只逐项固定原外部重构的来源和接线 |

表中multi_province相对src/ch5_two_asset_hank；完整15文件物理身份及AST定位在私有回执，本文不是新科学来源采纳或完整依赖闭合认证。图谱未列出所有require_netwage_inputs入边，不能用图谱的单一入边否认当前HJB/policy的实际检查。

## B1：已完成的原生O2对接工程（无HA、无新运行额度）

本片只新增tests/test_outer_native_o2_one_turn.py一份集成测试；生产源码不动，不新建runner或HA回调。复用已有输入容器、O2两个工厂、PreFrozenHouseholdOutputBatch、Supplied*Stage和assemble_precomputed_outer_one_turn，在**同一隔离模块命名空间**内构造对象，避免同文件加载成多个类后伪造类型兼容。

使用已经封存的两省合成夹具和原组件返回，仅读取副本；原探针目录/claim/记录不改、不作为新额度。可直接从保存trace的SOURCE_RETURN读取外层结果，不再调用劳动/资本/企业/工资/货币/财政生产函数。家户五项输出依然明确为原合成预给定量，不把它们标成真实HA返回。

1. **进入轮1的完整原生组合**：使用原数值初猜19记录准备O2请求，给出明确预给定回复，运行O2原生组装，再与同轮保存的原组件返回组成既有一轮候选状态。核对Prepared/Assembled/PreFrozen的实际类型、同一request/input引用、两省顺序、只读状态、A1和财政交接；资格与诊断中的scientific_execution_verified仍FALSE。
2. **轮1→轮2的工资入口**：保持保存的原工资生成上下文、封存工资向量和进入轮2候选快照各自身份，准备原生O2请求即可。不能把生成于轮1、进入轮2的工资改标签塞回轮1；也不能要求生成快照与进入快照SHA相同。此项不再计算第二轮外层结果、不调用HA。
3. **拒绝与无副作用**：保留原pending消费门的拒绝；拒绝错期次/错省序/源码身份混用/缺省回复及末来源失败后部分提交。只补与原生组合有关的缺口，不重做整个O2或一轮专项套件。

测试可加载数据类型及其现有依赖定义，但必须监视并拒绝科学生产入口/初始化/root/HJB/KFE/原汇总进入；不运行旧年度runner或7次原组件探针。依赖加载若出现未列动作，停止并保存失败，不为通过而扩大保护门。此片只新增工程见证，不能使consumer_ready、real_execution_enabled、formal_ha_accepted、scientific_acceptance、model_activation或Results变TRUE。

### B1实际检查结果与限制

最终6项全部通过：真实Prepared/Assembled/PreFrozen类型与同一输入记录；原生批次完整拼装后的候选状态与保存结果JSON字节完全相同、财政值一致/候选只读；轮1工资与不同进入快照准备原生轮2请求；两来源实际require_netwage_inputs仍报PRODUCER_INVOCATION_NOT_VERIFIED；拒绝后轮工资塞回首轮及源码集合错配；拒绝原生轮2批次复用轮1外层阶段结果。

六项在每项开始时确认科学函数监视器仍启用；最终记录FORBIDDEN_SCIENTIFIC_SOURCE_ATTEMPTS=0、EXTERNAL_ACTION_ATTEMPTS=0、SCIPY_SENTINEL_CALLS=0。未重跑原7入口worker、未调用HA或原科学生产函数，旧probe目录所有文件名/哈希在测试前后保持。原15份代码/测试字节保持，旧6缓存不变、新缓存0；唯一定义变更是新增测试，未改生产源码、源码pin或任何已关闭claim。

首次加载原bootstrap的SciPy依赖时，NumPy.testing间接发起Windows版本查询，被新测试的外部命令保护拦截；该轮setup错误、tests_run=0，完整日志保留。随后只把这份**不做数值求解**的测试中未使用的scipy.optimize.brentq导入绑定到一触即停哨兵，不改原模块源码，也不放行任何命令/网络/数值求解。原O2工厂、Temp31NetWageInputs/PreFrozen容器与NumPy数组构造均真实执行；SciPy依赖安装与原求解运行兼容并未由此验证。

第二轮误把PreFrozenHouseholdOutputBatch.__post_init__内部的数据校验生成式当成数值函数拦截；该轮失败，不作为最终验收。修正新测试的限定代码分类，仍禁止one_turn实际生产入口和所有原劳动/资本/企业/工资/货币/财政/HA数值入口；最终6项全程监视通过。三份独立日志与保护回执LOCAL_ONLY，以上工程检查修复未消费或重开任何科学额度。主代理自审不称独立科学审查。

## B2：工资生产见证与有限消费许可的最小外部扩展（拟工程设计，未实现）

2026-11-06的21条trace可证明固定合成输入下原工资函数调用/进入/返回的对应关系；它不是完整生产来源资格或新的HA许可。旧SavedWageWitness核对函数则固定了另一套9源/10角色/单工资调用记录格式，不接受新七入口trace；不能通过改旧schema、补假角色或重封旧pin硬套进去。

建议保留ProductionWageRecord及PendingWageEnvelope的结构语义和既有FALSE字段，在外部增加与该原记录绑定的、**仅对指定worker/来源/期次有效**的见证与许可伴随信息。复用现有记录/claim/源文件身份，不建立通用科研授权框架，不用一个布尔值表示已运行、可消费和科学接受。

最小改动候选限定在outer_production_wage_bridge.py的外部工厂/校验/消费门及一份专用证据核对模块和测试（约3文件）：

- 旧adapt_production_wage_payload默认仍返回原结构记录；无伴随信息时旧消费路径逐项保持拒绝。
- 新的显式绑定工厂须核对生产者实际输入/输出/函数来源、21条trace、原claim/决定/监督结果、工资六类封存输入与原始输出字节；只能登记“该次保存观察一致”，不能声称当前重新现场执行。
- 若将来接入限定消费分支，必须再匹配新的Owner明确许可、当前唯一worker的claim、原记录上下文/省序/期次、精确输入/网格与完整消费者源码manifest；历史观察或宽泛ready参数不能代替。每次原require_netwage_inputs仍经同一外部消费门，数值文件无需绕过或取消检查。许可针对整个被批准worker，不能把policy中的重复类型检查计作新运行或发放新额度。
- 伴随信息须由显式工厂生成并保持原工资数值不变；禁止伪造旧Temp31EffectiveWageRecord、绕过类型校验、把后轮工资重标为首轮19、monkeypatch门或修改policy/HJB内部。若同一原记录无法在原输入重建链中完整保留伴随信息，先停止该工程分支，不暗中更换输入对象/接口语义。

这只是接入设计，尚未实现或授权任何消费分支。Owner此前允许纯接口适配，但没有因此批准新HA运行、科学接受或全局model_activation。设计中的记录/许可核对是主代理受Owner约束的执行证据，不是密码学身份认证或OS隔离。

**源码身份分开记**：七入口探针的14模块身份集合、旧9角色SourceBundleReceipt和未来O2+HA完整运行manifest是三种不同范围。原工资记录/BindingContext现有source_bundle字段须保留它实际绑定的来源范围；完整消费者manifest另列并交叉引用，不为了相等而给旧记录换hash，也不把14模块标签宣称覆盖HA/网格全体源码。具体新方案需在实施/执行前锁定这些范围和关系。

## B3：未来HA黑箱外部执行器（未实现、未授权）

该执行器位于HA外部：接PreparedHouseholdBatch中的原request.inputs，同一对象交给已选a*r_a初始化及原HJB，之后沿原成功条件使用正式post→原KFE→原汇总，再按原外部AtTax重构填OriginHouseholdReply；失败立即终止该批次，不提交部分省份、不补零、不切算子或修输出。

Ct/Lt/At/Bt由同一次原汇总公开字段复制；AtTax沿既有外部重构原式/符号/每H单位，不重乘H或E。须精确绑定同次原g、cell_weight、a_grid和源ra，不能直接把旧单来源worker没有输出的AtTax当成已存在字段；也不启用corrected_household_adapter中额外误差/接受口径替代原式。原网格内容与输入、原收敛标记只核其既有返回，不新增HA内部字段、行和/残差门、条件数或固定行研究。

现有O2的PRECOMPUTED_BATCH_ROUTING_ONLY标签和FALSE诊断仍只能说明路由校验；真实调用见证在外部单独关联到request/返回，不把改标签当运行证明。未来若需真实执行类型，必须显式设计与现有一轮字段接口的关系，不自行把real_execution_enabled或formal_ha_accepted翻转。

本方案未指定新价格/参数/网格、来源数量、执行次数或资源预算，未生成新Owner决定/claim。七入口夹具的新工资、旧S03价格、初始化旧余额都不会自动成为本片的HA输入/预算。B1/B2就绪后，再把确切源码、输入、每入口调用数、时限/资源、零重试和失败条件制成可审阅方案，适用具体有限许可才执行；原19初猜只用于其原首轮语义。

## 交付、未决事项与本轮停点

本轮完成静态接入方案及B1原生组合工程，新增6项集成检查最终全部通过，原科学生产/HA函数调用0，生产源码修改0。下一项为B2外部见证/未来有限许可绑定的具体工程，不重问已采纳的A1/工资税/H聚合，不自动开始B3或新的科学执行。B1测试的SciPy哨兵隔离限制必须随结果保留。

实际p与H口径/来源、家户收入与劳动激励兼容、Lt_prev经济语义、R/P制度及外层控制/停止口径仍按既有记录待闭合；这些不在本轮替Owner决定。严格reference/thresholds仍null，科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。

TEMP31 7/7、Moll 3/3、新七入口观察1/1均关闭/零重试；工资与补录关闭，旧初始化余量仅原8格，不借用。R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权、16项义务、历史dirty树/HEAD/index/porcelain、原件/缓存/LOCAL_ONLY证据保持；不reset/stash/clean、强推、合并main、删分支、移动证据或修改Desktop/CUA/全局配置。模型代码仅本地，GitHub仅同步本份方案与当前治理文档，API写入0。

前置：[七入口单次观察完成记录](CH5_O3_OUTER_COMPONENT_SINGLE_PROBE_RESULT_20261106.md)、[O2原专项工程记录](CH5_OUTER_MULTI_ORIGIN_BATCH_ADAPTER_20261105.md)。当前：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。本文是工程接入顺序及边界建议，不是B2消费放行或B3运行授权；最终提交/回读以私有交付回执为准。
