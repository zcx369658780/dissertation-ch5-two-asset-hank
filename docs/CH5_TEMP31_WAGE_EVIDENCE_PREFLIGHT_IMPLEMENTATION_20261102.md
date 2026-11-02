# TEMP31 工资凭据接口与外部源身份预检 · 2026-11-02

STATUS=SOURCE_BYTE_PREFLIGHT_AND_PENDING_WAGE_INTERFACE_IMPLEMENTED__79_FOCUSED_CHECKS_PASS
OWNER_EXACT_STATEMENT=我同意，请继续
GOVERNANCE_AUTHORIZATION_PARENT=e620589bdef11cccdd305f5d78b7f98e7a2e35c2
LOCAL_CODE_CANDIDATE=dc87980d5377309f9b18c1928173488ba1050415
LOCAL_CODE_PARENT=5f7a4cf21b9f0de1c829a3a56fc4a40644b3e161
LOCAL_CODE_TREE=6b4a8360b59c375cafb069a22f1f96b6b11f45d8
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED
PENDING_INTERFACE_PRODUCER_INVOCATION_VERIFIED=FALSE
SCIENTIFIC_CONSUMER_READY=FALSE

后续状态：文末独立单次源工资函数观测提案已获Owner明确批准并执行，见[CH5_TEMP31_SOURCE_WAGE_OBSERVATION_20261102.md](CH5_TEMP31_SOURCE_WAGE_OBSERVATION_20261102.md)。外部实际进入/返回各1、字节交接通过；本接口未自动接纳该外部见证，科学消费者继续关闭。下文提案“未授权/未执行”为原阶段记录，不覆盖后续执行事实。

本轮新增标准库工程模块及测试，实现两项不同的工作：对显式授权根下的限定源文件做真实字节预检；对调用方提供的工资输入/输出字节建立尚未见证执行的凭据接口。没有运行工资生产者、初始化或HA，没有修改原科学模块及其消费者校验器。源码、测试和完整日志仅本地，公开交付本说明与进度。

## 新增代码身份

| 路径 | Git Blob | bytes / SHA-256 |
|---|---|---|
| src/ch5_two_asset_hank/multi_province/temp31_wage_evidence_preflight.py | 55ee7527bf1101133f6b3e9464cdbab65123001f | 12332 / 05236c4ea91384d0f6db969b38ae9adb53c82e00887cab1701fcddbf130043d6 |
| tests/test_temp31_wage_evidence_preflight.py | ed157db01e759ac5b4b2c81365e4b5c04b8c9354 | 12780 / edcdf9359d2d5d98982c34b7867e3e8871aa72ff7b9f50868c8d402458c4697c |

上述candidate是独立工作区的本地提交，不提供不存在的GitHub源码链接。既有569个选定代码路径的Blob保持；本次仅加两文件，既有初始化和模拟接口均未改。

## 源文件预检：实际完成的部分

verify_source_bundle只读取九个固定角色对应的代码路径：工资生产者、净工资合同、新初始化、净工资HJB/policy/economics、指定KFE、数组汇总export及原网格构造参考入口。调用方不能在SourcePin中指定任意路径；角色、完整性、唯一性、预期大小、Git Blob和SHA-256均受检查。源字节最多1MiB/文件，预期来源必须由当前授权清单提供，不能用该API自行授予来源采纳。

预检检查文件和全部祖先的链接/重解析标志，在有界读取前后核对元数据及打开文件状态，发生来源/权限/路径变化即拒绝，不跟随别的来源、换路径或重试。它不导入代码、不执行旧bootstrap、不修改ORACLE_SHA，不读取真实数据、矩阵、R12或历史LOCAL_ONLY原件。标准API的前后检查不是原子OS隔离证明，不改变六路径WASM STOP或保护基线。

现场已从此前批准的固定来源身份清单提取九项pins，实际读回当前工作区九个文件，9/9大小、Git Blob和SHA-256匹配。SourceBundleReceipt只能由该读取工厂生成，不能通过公开构造器把自报标签伪装成读取回执；其scope为SOURCE_BYTES_VERIFIED_ONLY，model_activation=FALSE。回执包含源根及文件集合的身份哈希，不包含原源字节。这是限定九文件字节核对，不证明完整动态依赖、运行时已加载函数的身份、旧bootstrap兼容、科学来源冻结或原件恢复。

## 工资凭据接口：仍保持待见证

WageInvocationContext固定上下文、省序、生成/进入期次、生成快照身份及源根/源集合身份；生成t必须交接进入t+1，布尔期次、重复省名、错源根等被拒。接口封存六类输入：生成快照、目的地企业工资、目的地税、phi、sigma及偏好字节，并封存净工资输出字节的SHA-256和大小。当前载荷完全不透明，不解析或重算工资、价格、人口或数组；生成快照的哈希必须与其实际传入字节相等。

capture_pending_wage_envelope与check_pending_payloads可拒绝输入角色缺失/重复、可变或空字节、上下文/省序/期次变化、源或快照变化及输入/输出字节被替换。PendingWageEnvelope还拒绝非法构造上下文、不完整或错误类型的身份列表，避免异常对象进入相等比较。数值输出不能被自动序列化或重新定价；实际输出编码/形状/数值有效性仍须后续获准调用验证。

这些操作只证明输入输出身份的一致性，不证明工资函数实际执行，也不证明传入字节确为该函数实际参数。pending回执的producer_invocation_verified、consumer_ready、model_activation始终FALSE，scope为PENDING_INVOCATION_NOT_EXECUTION_VERIFIED；即使payload完全匹配，科学消费者仍以PRODUCER_INVOCATION_NOT_VERIFIED拒绝。没有将其转为R5合成见证、改旧SOURCE_COMMIT，或接入现有Temp31NetWageInputs校验器。

现场额外做了“真实九源字节回执+纯模拟载荷”的工程交接检查：只用明确ENGINEERING_MOCK字节封存输入输出，科学消费者保持拒绝。该步骤没有真实工资、企业或31省输入，也没有实际生产者调用。

## 实际测试和限制

测试先行记录新模块缺失导致的red：setup1错误、tests_run0；实现后30项新检查+45项先前限定检查共75项通过。审查新增四项：源回执构造器限制、打开文件元数据变化、非法上下文对象、缺失/可变/错误的pending身份列表；后两项先真实失败，再补构造验证修复。最终34项新检查+34项既有模拟接口检查+11项既有静态合同检查=79/79通过，错误/失败/跳过0。

检查覆盖固定路径/角色、缺件、同大小篡改、Blob/SHA/大小错误、重解析/符号链接标志、读中变化、源根/集合交接、六输入/输出封存、防替换、省序/期次、31虚拟标签及消费者关闭。链接/重解析/读中变化用例为注入元数据的工程策略测试，没有创建真实链接，不冒称重新通过平台保护门。所有测试文件均是新建的隔离假源夹具；没有改坏真实源文件来做故障注入。

执行器只定点加载新的标准库模块及既有模拟模块，阻断NumPy/SciPy/原模型/exports/validators导入并监视原科学src函数进入；79项及现场九源预检的实际科学导入/函数调用均0。没有运行全科学pytest套件，没有把限定测试称为真实生产集成、独立科学评议或稳态验收。数值初始化账本仍3/10已用、余7；本轮不消耗或重置该预算。

## 下一科学门：固定合成输入的一次实际源工资函数调用（提案，未授权未执行）

接口和字节预检已经完成；再前进需要观察源composite_household_wages的实际进入、参数和返回。当前工程许可不包括这次科学函数调用，剩余7个worker仍只适用于原8格初始化。以下是单独供Owner决定的新预算，不自动执行：

- 最多3个新worker，每个墙钟≤30秒，含导入和输入准备；累计composite_household_wages进入最多1次。仅在尚无任何生产者进入时，工程问题可在余量内修复；一旦进入生产者，无论成功、异常或超时均不再重跑。来源/保护/域失败及执行状态不明都停止，不能改输入、公式、容差或pin。
- 固定使用已核实wage.py文件及当前工程接口，按精确文件加载，不导入旧年度loader或完整科学package __init__；记录实际函数源身份、调用入口和返回。环境预案为Python3.11.9/NumPy2.4.6；不安装升级依赖、不需要SciPy，不修改全局配置。
- 合成省序A/B，目的地tau=[.05,.05]，phi为2×2全1、sigma为2×2全0，phi_l=5、alphal=1；两地企业工资均用既有R1/R3合成见证的表达式19/(.95*2^(5/6))，只在获准worker内求值。生成1/进入2只是反事实观察标签，不是真实企业更新或生产期次。函数不消费ra/rb或HA网格，本提案不创建、更改任何HA节点/价格边界。
- 仅报告两元素输出及相对既有数值19的差，不新增科学接受容差；记录输入/输出和函数执行见证。初始化/root/HA/HJB/KFE/GE/IRF/policy/MATLAB及真实数据调用全部0。观察成功仍不放行科学消费者，不等于真实31省生产、来源采纳、严格驻定或Results。

封存的提案输入1230 bytes，SHA-256=98471bf5b9f3594b8051c5e25247aa95ab1e583a8fa769c58b127ee6dcded79f；表达式尚未求值。完整提案、pins和输入文件LOCAL_ONLY保留，没有创建或启动新科学worker，没有新科学授权claim。

ENGINEERING_VERDICT=PASS_BOUNDED_SOURCE_PREFLIGHT_AND_PENDING_EVIDENCE_INTERFACE
ACTUAL_DECLARED_SOURCE_READBACK=9_OF_9_PASS__NOT_FULL_REPOSITORY_CERTIFICATION
PRODUCER_EXECUTION_OBSERVATION=PROPOSED_ONLY_NOT_AUTHORIZED_NOT_RUN
EXISTING_SCIENTIFIC_SOURCE_EDITS=0
HA_GRID_OR_PRICE_CHANGES=0
SCIENTIFIC_CALLS_THIS_TASK=0
FORMAL_SOURCE_FREEZE=FALSE
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE

旧dirty工作树/HEAD/index、旧证据/耗额、V010、WASM/R12 STOP、R13未授权、保护重绑定未授权及16项义务保持；无分支删除、main合并、原件移动或配置修改。

## 后续工程：保存的执行记录已类型化（2026-11-02）

见[保存见证接口实施记录](CH5_TEMP31_SAVED_WAGE_WITNESS_IMPLEMENTATION_20261102.md)。本标准库模块新增保存记录的类型和核对工厂，旧pending/科学消费者行为不变；新版本地candidate547a17b1b0e28d67a4944dd819412d64038955de，103项限定检查通过，现场10份封存记录对接通过，科学导入/调用0。本篇前述79项与旧代码身份为当时交付记录，不覆盖后续版本；单次源工资观测已完成并关闭，不因本轮类型核对而再次运行。
