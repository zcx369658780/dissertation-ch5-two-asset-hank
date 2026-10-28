# TEMP31 HA × 工资首轮来源、重复税楔、真实消费者接口：静态+无HA合成调试R1

TASK_ID=CH5_TEMP31_HA_WAGE_FIRST_ROUND_PROVENANCE_AND_CONSUMER_STATIC_DEBUG_R1_20261028
STATUS=OWNER_AUTHORIZED_ISSUED_AWAITING_TRANSFER
OWNER_AUTHORIZATION=2026-10-28_22H35_APPROVED_ENTER_HA_AND_WAGE_DEBUGGING
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=0167450609c863ef26a9c48ede74d8ab83a3996e
TASK_PUBLICATION_COMMIT=EXACT_40_HEX_GPT_PROVIDES_AFTER_CONTRACT_PUBLICATION
EXPECTED_REMOTE_HEAD=TASK_PUBLICATION_COMMIT__STRICT_EQUALS__NOT_SOURCE_PARENT
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_HA_WAGE_FIRST_ROUND_PROVENANCE_AND_CONSUMER_STATIC_DEBUG_R1_20261028/CONTRACT.md
CANDIDATE_BRANCH=codex/ch5-temp31-ha-wage-first-round-debug-20261028-r1
FIXED_PARENT=92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27
SOURCE_COMMIT=92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27
SOURCE_ROOT_TREE=adb98b1ad14920902b62ad16bc8ed8e2df4605dc
SOURCE_RELATION=R4_FINAL_ISOLATED_CANDIDATE_ACCEPTED_BOUNDED__NOT_MERGED__NOT_PRODUCTION
NEW_GIT_REPOS=0
SRC_FETCH_FOR_AUXILIARY=0
SCIENCE_BUDGET=0
HA_HJB_KFE_GE_IRF_RUNS=0
MODEL_CALLS=0
REAL_GE=FALSE
REAL_PRODUCTION=0
SYNTHETIC_TEST_INVOCATIONS_MAX=2
TEST_TOOL_ERROR_RETRY_MAX=1_WITHIN_TWO_TOTAL_INVOCATIONS
AUTO_ISSUE=FALSE
AUTO_MERGE=FALSE
AUTO_PR=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 实际研究目标与禁止偷换

Owner已批准工作地工资税 tau_j，单一劳动收入只征一次。R4已独立审阅PASS_BOUNDED（review commit 0167450609c863ef26a9c48ede74d8ab83a3996e，固定候选 92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27），完成两个隔离双边劳动算法及NET_COMPOSITE→单类别HA的**纯数据**接口；没有接入真实HA，未认证首轮工资或财政/有效劳动。R5进入HA—工资**调试前置**而非已授权真实HA数值运行：本次仅做固定源码消费链追踪、显式首轮来源契约和2次以内无HA定向合成验证；不得运行/修改HA/HJB/KFE、31省稳态、校准、真实宏观数据或正式生产；若真实HA的测试成为必要，STOP并列明Owner需另批的网格、调用次数、时间、代码身份和安全预算，绝不能静默升级权限。

验收问题：在外层iteration=1初始工资以及iteration>=2由工资模块生成的工资之间，分别能否证明工资gross/net？真实HA的初始化、HJB边界和policy劳动/消费是否对传入w重新扣tau？在不改HA的条件下，应如何通过同一个候选适配界面保证后续已净工资只进HA一次，且对初轮默认值fail closed，不把tau_j错误替换成原籍tau_i或把税率全域置零？

## 1. 固定Git源身份及更新代码前置

1. 只复用R3/R4上轮明确认证且安全的**同一个独立Git库**。禁止新仓库、替换Git对象存储、清理工作区、复用旧shallow.lock库、跟随任何P3/WASM/reparse目标；检查本地当前refs、候选源分支、独立object store、Git状态及未跟踪文件保护。若身份、锁、路径或未跟踪文件的安全无法证明立即STOP。不修改受保护科研树/旧分支/老证据、index外文件、Git baseline或D盘历史目录。
2. GPT将在本合同发布后于Owner交付指令提供完整40位 TASK_PUBLICATION_COMMIT。通过普通SSH限定一次治理HEAD观察（瞬时工具错误可同通道最多一次技术重试，且显式记录），**严格要求远端治理HEAD==TASK_PUBLICATION_COMMIT**。任务发布commit应仅有一个直接parent==0167450609c863ef26a9c48ede74d8ab83a3996e；发布diff仅新增R5合同。不能错误要求治理HEAD等于FIXED_PARENT，也不能用祖先关系代替严格相等。如本地未缓存治理发布commit对象，允许只读远端Git元数据/已核验的GPT GitHub固定对象证据，记录LOCAL_OBJECT_ABSENT；禁止为此无界fetch。
3. **先同步核对最新固定代码**：R5源码基准不是治理HEAD，而是R4已验收的固定候选 92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27，root tree=adb98b1ad14920902b62ad16bc8ed8e2df4605dc；R4远端候选分支必须精确指向该commit，其直接parent=e99c622b41b255e5312589c61c57689a42a0b3e3。检查R4本地候选HEAD与源码Git Blob/bytes/SHA；复用已认证的R4证据，不重复无意义重算。不存在该固定commit、变更被漂移、源码缺失或来源身份不可认证则STOP，不新建库/不自选其他父。新R5候选从FIXED_PARENT=92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27创建，**保留R4和R3全部分支与证据**；R5合同仅存在于治理发布commit，不要求其在R5候选父里出现。
4. 本任务只读引用下述已经由GPT在冻结来源提交直接核验的历史文件；若Codex隔离库缺少某些HA/anchor对象，按MISSING_LOCAL_OBJECT登记，**不进行新的SSH fetch/raw下载/HTTP切换/借本项目ZIP补源**；基于GPT提供的固定Blob/行号只能得出SOURCE_STATIC_OBSERVATION而非LOCAL_BYTES_VERIFIED。涉及导入缺失模块或实际执行其函数，必须阻断对应部分，不能假装真实HA消费者已经运行。

关键历史源码（以下原源码Git Blob已在R4 A审阅中以固定身份认证，未修改）：
- src/ch5_two_asset_hank/multi_province/wage.py: 48001b2e4ca64d81dda6174255f6ccf130e07004，55–75行：tau[destination]、sigma[destination,origin]的税后综合工资。
- src/ch5_two_asset_hank/multi_province/steady_state.py: 5c5b56e6a2eb82fab4e80eb7b8e5bbbf97f08c22，147–169行：_post_turn_states覆盖state['w']。
- src/ch5_two_asset_hank/multi_province/stationary_runtime.py: 8717cfa759948bd1ad3c8cd788f8f4736f250598，50–56行：先用entering states调HA，再用one_turn合成新工资。
- validators/multi_province/mp4c_python_annual_empirical.py: d2e74cb8b491489053dcde525cd4d83cb4bd0b3a，46–71、139–159、237–245行：accepted_source_scalars默认 composite_wage=20、wage_tax=.05、wjt=.6，入口state['w']来源及HA传入state['tau']。
- validators/multi_province/mp4c_python_annual_production.py: 7473e04418744d745000afb21d84588273cc5bca，145–174行：owner_a/runtime_cache入口分支及正式solve_batch调用。
- validators/multi_province/mp4c_owner_a_2009_2022.py: f89927c7a6234cf1c5106318b2b4249183b90cce，215–222行：Owner-A首轮state['w']=accepted_scalars['composite_wage']。
- validators/multi_province/mp4c_matlab_runtime_cache.py: a02e86af75f272dcbf7c57b1f7d9f68e30afc4bd，98–108行：另一入口首轮同一默认标量。
- validators/multi_province/mp4b_python_empirical.py: b1710ae3c5d8d7baf96e85c932d777fa5f3b908c，171–184、337–350行：HA初始化计算 wage=(1-state['tau'])*state['w']*z，并向HouseholdInputs再传state['tau']。
- src/ch5_two_asset_hank/contracts.py: c746b616bec38531a7d96da81a54e2899d8aba53，79–104行：HouseholdInputs内有效工资定义。
- src/ch5_two_asset_hank/matlab_faithful_hjb.py: e06f9871b361c8e1c8df7aab5c43c2dbd3b09b50，89–103行：HJB边界resources又用(1-inputs.tau)*w*z*l。
- src/ch5_two_asset_hank/matlab_faithful_policy.py: 2021db630f3057026ffc37d375a43aaddbccec48，119–155行：policy净工资w*(1-tau-sigma)*z及消费。
- R4新隔离模块 src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py: 90667ddc00c72b9290e91481af4835c808ecfccb：适配纯数据Temp31NetWageViews与NET_COMPOSITE标记；净工资源语义仍须证明。

## 2. 科学审阅与调试工作范围

A. **首轮工资可证事实**：对正式annual production的owner_a及runtime_cache两分支、annual_empirical路径分别列出从scalars到state['w']与wjt、tau的真实数据来源、量纲/时点和是否已通过wage.py，标初始默认w=20为INITIAL_DEFAULT_UNPROVEN，不能因为数字正或名字叫composite而认定净工资。标第2轮及以后从已计算的综合工资回写为CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA，但仅限此固定代码来源和更新顺序；检查tau_j是省j的目的地税，不是HA入口的原籍tau_i。说明首轮进入HA在one_turn更新工资之前，不能借第1轮末的净工资证明第1轮输入有效。
B. **三个HA消费者逐点审查**：静态跟踪 _source_initial_arrays 初始labor/value、HJB边界resources、policy劳动最优和consumption，分别注明真实输入 w、tau、sigma、z、Tt、rb及净工资的公式；判别 R4 net语义进入这些路径时可能的二次扣税。多点消费公式不等于独立重复收取多笔税，而是同一已净工资在不同HA计算路径被**错误再次乘税楔**；禁止声称财政实际扣税次数已经实证验证。
C. **首轮策略需Owner裁决**：做明确的两种**候选**比较：(i) fail-closed使INITIAL_DEFAULT_UNPROVEN不可声明NET，不进行HA消费；(ii) 将第一轮工资以固定来源的实际目的地工资、phi、sigma、tau_j计算**预备净综合工资**作为初始化的未来方案，但不能擅自宣布其科学采纳，需核对初始wjt=.6、企业工资clip wjtmin=.8、phi更新顺序、源工资来源和有效劳动/工资单位。禁止自行把首轮净工资从20推定出来、把tau_i作为替代、对所有轮次tau全局置零、按人工常数静默重算首轮。
D. **独立纯数据调试器**：可新增一个具名TEMP31非生产模块和必要的定向测试/启动脚本，用原R4纯净工资适配对象验证：
   - 不可信INITIAL_DEFAULT_UNPROVEN的工资来源必须fail-closed（例如默认w=20, tau=.05，不得调用R4已净适配生成“已证净工资”），并保留诊断字段而非替换源。
   - 已用目的地税率/迁移成本、来自所核实的wage.py公式的合成net composite，可传到一个拟议init/HJB共同的净工资视图，额外tau_HA=sigma_HA=0且w_effective相等；不得仅以任意标签字符串当真实性证明，可在小型合成输入对照独立复算或校验输入来源身份。
   - 采用z取不同正值的标量消费资源恒等式检验初始化、HJB边界和policy拟议的**同一个**net*w*z*l，只能算纯代数，绝不调用HJB计算；验证错误注入二次税楔会失败，且保留真实tau_j在独立税数据。
   - 工资来源在首轮与后续轮次交替时的状态不能误标；旧函数及R4全部行为不变。
若实现需要缺失的HA源码或完整运行时，不擅自取回；可以输出静态gap及最小bridge方案，不给虚假运行PASS。
E. 形成 **production integration proposal ONLY**：列精确将来接入的mp4c production/annual_empirical、Owner-A及runtime_cache入口、R4 net adapter、_source_initial_arrays、HouseholdInputs构造的可选最小边界（不执行此接线）；同步标出财政tau_j*w_j*L_j与z/N口径仍未裁决、R4劳动函数未接线，不自动扩大成真实生产调试或模型参数调整。

## 3. 实施白名单与有限预算

候选只能新增：
- src/ch5_two_asset_hank/multi_province/temp31_ha_wage_debug.py（纯Python/纯代数工资来源守卫与HA拟议消费端合同）
- validators/multi_province/temp31_ha_wage_debug_isolated.py（无HA的显式定向测试入口）
- tests/test_temp31_ha_wage_debug_isolated.py（最多小型2/3省合成断言）
- tasks/CH5_TEMP31_HA_WAGE_FIRST_ROUND_PROVENANCE_AND_CONSUMER_STATIC_DEBUG_R1_20261028/（result、source/provenance、消费者矩阵、测试、差异、gap、manifest、隐私与readback seal证据）

除这些新增路径、经确认的本独立候选Git元数据外，所有文件只读：不修改R4的三个代码文件、旧HAL/HJB/KFE、production worker、annual empirical、历史项目规则、V010/V011、ORACLE_SHA、旧任务证据与P3科研资产。若非改旧文件不能继续，则STOP列出接口和Owner科学授权，不能顺手更改。最多2次显式无HA合成测试命令调用，总预算内瞬时工具错误最多一次，不做多轮实验。严禁真的调用HA/HJB/KFE/GE/IRF或真实31省校准，不读三份primary Excel原件或D盘历史目录。禁止pip install、全仓库扫描或无界fetch。

SCIENCE_BUDGET=0
TEST_BUDGET=2_NO_HA_SYNTHETIC_COMMAND_INVOCATIONS
HA_HJB_KFE_GE_IRF_RUNS=0
MODEL_CALLS=0
NO_PRODUCTION_WIRING=TRUE
NO_FORMAL_DATA_ADOPTION=TRUE
SOURCE_FETCH_BUDGET=0_FOR_MISSING_AUXILIARY_OBJECTS
NEW_GIT_REPOS=0
DELETE_OR_CLEAN=0

## 4. 交付、独立审阅与STOP

Codex只在本次新增候选分支下提交最小代码与证据；源commit固定为R4最终隔离候选，后续未合并。交付至少：
- result.md (COMPLETED/BLOCKED/NOT_COMPLETED/NEXT_ACTION)
- source_identity.json (治理任务发布与父身份、R4来源parent/tree/Blob/bytes/SHA、缺失辅助对象标记)
- ha_wage_entry_round_provenance.md (初轮/后轮、Owner-A/runtime_cache/empirical精确来源、wjt clip与phi顺序缺口)
- ha_wage_consumer_matrix.md (初始化、HJB边界与policy不同消费点的公式、税楔、数据语义、源码行号、未运行说明)
- bridge_design_and_decision_cards.md (fail-closed机制、预备净工资候选、Owner尚待科学裁决)
- synthetic_test_evidence.md (2命令内预期/结果、真实stdout/stderr与预算)
- gap_register.md, privacy_report.md
- manifest.json (每载荷path/bytes/SHA-256/Git Blob，manifest自校验，不循环自哈希)
- DELIVERY_FINAL_RECEIPT.json (候选commit/唯一parent/root tree、实际远端GitHub逐项readback/budgets/STOP)
- 最小合成fixtures/证据（如需），不上传任何本地private path、Git凭据、真实工资微观记录或WASM信息。

通过已授权普通SSH在独立候选分支**小批次顺序推送**，先payload后seal，逐阶段精确核对远端commit/parent/tree/path/Blob/bytes/SHA256；若GitHub/SSH权限拒绝或访问保护树立即STOP，不改账号/协议/认证渠道，不自动创建另一个库或重新签发任务。交付完立即STOP。GPT之后仅对固定candidate进行独立A提交/来源→B数值/科学消费语义→C分层裁决，Owner决定下一步。GitHub已验收R4文件及旧STOP历史不删除、不合并、不改写。

## 5. 当前状态

PREVIOUS_TASK=CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R4_20261028
PREVIOUS_VERDICT=PASS_BOUNDED_R4_ISOLATED_WORKSITE_TAU_J_AND_SINGLE_NET_WAGE_DATA_CONTRACT__REAL_HA_FISCAL_EMPIRICAL_BLOCKED
R4_REVIEW_COMMIT=0167450609c863ef26a9c48ede74d8ab83a3996e
ACTIVE_TASK=ISSUED_AWAITING_OWNER_TRANSFER
PROTECTION_BASELINE=BLOCKED
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
