# TEMP31 生产工资凭据与HA资格：静态接口合同 · 2026-11-02

STATUS=STATIC_DESIGN_READY__NO_RUNTIME_IMPLEMENTATION_OR_CONSUMER_RELEASE
AUTHORIZATION_PARENT=e075a52f4653280fc97a656bfdf97cb6621e7aed
SOURCE_HEAD_AT_CHECK=67fd70d636ee650732b6c8a0112651f29c711458
ACTIVE_CODE_CANDIDATE=547a17b1b0e28d67a4944dd819412d64038955de__UNCHANGED_LOCAL_ONLY
MACHINE_READABLE_CONTRACT=CH5_TEMP31_PRODUCTION_CREDENTIAL_HA_CONTRACT_20261102.json

本合同把已有[生产接线规格](CH5_TEMP31_PRODUCTION_BINDING_SPEC_20261101.md)中的两处缺口细化为可实施接口：工资的实际生产来源证据，以及HA原始诊断与严格资格的交接。现有[保存见证](CH5_TEMP31_SAVED_WAGE_WITNESS_IMPLEMENTATION_20261102.md)保持原资格；不运行模型，不修改源程序或已冻结科学规则。

限定核对当前工作区10个相关文件，字节/Blob/SHA-256与当前固定HEAD一致；标准库AST确认14项静态观察。未使用其他仓库图谱代替当前来源，未导入项目/NumPy/SciPy，也未求值网格、工资或残差。静态身份不证明运行时依赖闭合、正式来源/数据采纳或科学正确性。

## 三种工资资格不能相互改标签

| 输入种类 | 能说明什么 | 进入生产消费者前还缺什么 |
|---|---|---|
| numerical_bootstrap19 | 已有首轮数值初猜合同；没有生产者调用 | 首轮适用合同、输入与运行许可；不能冒称实证工资或税收归宿证据 |
| 保存的合成源函数观测 | 旧固定合成输入上发生过一次调用，保存的记录已对齐 | 真实生产输入与来源资格、对应现场执行及兼容消费者桥；不能靠重放/改标签取得 |
| 未来实际生产调用候选 | 在对应许可内，实际函数、参数、返回及期次可被同时记录 | 仍须分别核对输入采纳、来源、执行状态、消费接口及运行许可；不能仅凭成功返回放行 |

后轮工资沿用生成于t、进入t+1的已有时序，目的地行/来源地列和NET_ONCE语义保持。保存六角色输入字节：企业毛工资、目的地税、phi、sigma、偏好、生成快照；生产函数实际frame参数和return必须与封存载荷对应，不能用消费时的新矩阵重新算一个同名工资。

未来实际生产者入口必须先有有限许可与持久claim，绑定同一执行意图、源/输入哈希和计数。结果分为返回、失败、执行状态不明；超时或记录缺失不代表未执行，不能自动再调用。当前已关闭工资许可与初始化3/10原账本不变，本设计没有生成新科学许可或worker。

## 现有消费者的两处兼容限制

temp31_ha_taxfree_bootstrap.py的validate_effective_wage_record后轮分支调用prepare_proposed_consumers；后者只接受SyntheticNetWageCalculation，并调用recompute_synthetic_net_wage重新计算合成公式。新初始化和净工资HJB又都调用require_netwage_inputs。因此“新增生产凭据对象”不能直接喂进现有类型，也不能通过强制转换、替换SOURCE_COMMIT、修改producer_record或给标志赋TRUE绕过。旧分支保持，未来兼容桥需单独实现、审查并受对应科学/运行合同约束；本轮未改它。

原wage.py允许有限且非负的结果；当前Temp31NetWageInputs要求工资严格大于0。这是已存在的边界差异。未来准入接口遇到零工资须报告WAGE_NONPOSITIVE_FOR_CURRENT_CONSUMER，不自动加epsilon、不改税率/价格、不改公式来使其可消费。非正情形的经济角点处理属于另一个科学决定。

## 拟议类型和职责

下列名称均为设计，尚未成为可调用API；字段定义见配套JSON。JSON使用自定义机读设计词汇，**不是JSON Schema，也不是已实现的运行验证器**。

| 类型 | 必须绑定的内容 | 不授予的资格 |
|---|---|---|
| EvidenceIdentity | 原始字节哈希、大小、编码与独立固定来源 | 哈希匹配不证明内容真实或来源获准 |
| WageContext | 上下文、省序、生成/进入期次、生成快照、来源、输入及运行授权、数据scope | 源字节通过不等于输入采纳或运行许可 |
| ProductionWageCandidate | 不可混淆的种类、实际参数/返回、进入claim、事件、源身份 | 候选不等于生产凭据；本轮不可构造真实现场资格 |
| WageAdmissionReport | 分类、缺件与拒绝码 | 下一工程片consumer_ready/real_execution_enabled始终FALSE |
| HAChainContext | 来源地索引、同一工资/输入快照、原网格对象及组件身份 | 类型名或字段相同不证明组件运行兼容 |
| HADiagnosticRecord | 原HJB字段、原/污染算子、raw/normalized密度、权重与统计量身份 | 记录诊断不判科学通过 |
| HAQualificationReport | 诊断身份、确切科学判据引用、逐项未测/未绑定/失败状态 | 缺判据保持UNKNOWN；下一工程片qualification_passed始终FALSE |
| BatchAdmissionReport | 完整且有序的来源地集合、逐户资格与未乘人口的统计量 | 完整模拟批次不能提交企业/GE，formal_ha_accepted始终FALSE |

拟议纯接口为inspect_wage_candidate、record_ha_diagnostics、inspect_ha_qualification、inspect_complete_batch。下一工程实现只接不透明数据/身份，不接solver或producer callback，不通过导入触发执行。默认关闭，拒绝环境变量、任意布尔值或调用方同时自报内容和哈希来授予科学资格。

## HA诊断保留原义

当前HJB提供operator和post_convergence_operator两个对象，convergence_statistic是max(abs(value-old))，不是HJB方程残差。保留原converged、iterations及该统计量；如另需HJB方程残差，必须有单独定义、原对象身份及相应运行许可，不能给原字段改名充数。

KFE应接同次HJB实际返回的post_convergence_operator.full。当前KFE内部会转CSR，并返回original_operator、transpose、污染行系统、raw_solve_vector、normalization_factor及normalized density。未来记录同时保存传入算子和返回算子的结构/数值身份及源内CSR表示转换；包装层不能另建算子、排序/裁剪/改写原对象来救对接。表示未能对应时标为OPERATOR_LINEAGE_UNVERIFIED，不把“数值看起来相同”当完整证据。

原raw_residual_inf计算的是污染矩阵乘raw向量再减rhs的无穷范数，必须原样保留。它不等于原未污染算子对归一化密度的驻定残差。拟议另记：

- original_stationarity_residual_inf：同一原后置算子A_post、F-order归一化密度g上的`||A_post.T @ g||∞`，不得省略被污染行。
- 密度诊断：有限性、最小值、`sum(g)*db*da`质量及`sum(max(-g,0))*db*da`负质量；保留raw向量、归一化因子和原密度，不剪负值或重归一化补救。
- 单位与权重：沿原代码db*da，对离散z求和，不擅加dz。原汇总l_ss已经包含z权重；保持家户统计量，人口缩放在其受权边界仅执行一次，生产资本接口仍At-only，Bt单列。

上述是拟议诊断字段的明确定义，**本轮没有计算它们，也没有采纳新的数值阈值**。严格资格必须引用已获准且适用于本次来源/范数/权重的确切科学合同；本轮没有绑定该引用，机读合同reference/thresholds均null。下一工程片只记录NOT_MEASURED、CRITERIA_UNBOUND、SOURCE_FAILED或BLOCKED，不从None、缺失字段、HJB收敛或小污染系统残差推定通过。

## 网格和原始证据

HA grid仍是不可变黑箱。未来只记录原对象以及b/a/z/switch_matrix的数值、shape、dtype、轴、strides与flags，并作前后身份比较；不得为了满足Temp31NetWageHJBGrid类型名而重建/转换网格、改节点或改只读标志。现有两个grid类的字段相似，仅支持接口设计，不构成运行时互换认证。本轮未生成任何节点数组或运行时网格哈希。

科学数组、CSR、原始参数/日志和完整现场见证继续LOCAL_ONLY。公开记录字段定义、聚合计数、源身份与哈希；来源资格不明的原件不因“接口需要”自动公开或加载。

## 拒绝路径与下一可实施分片

配套JSON列出14个拟议拒绝码，覆盖工资scope/来源/执行状态/参数返回/正值/旧合成重算/期次，网格、HJB、算子、污染残差、科学判据、完整批次及默认关闭。这些是新接口的设计码，不冒称现有代码已实现。

下一工程片可以直接在现有授权内实施：新增标准库惰性记录/准入类型，保持旧API与SOURCE_COMMIT不变，使用纯工程夹具先覆盖上述拒绝路径；所有生产/科学接受标志固定FALSE，不接真实数组运算、工资生产者或求解器。普通工程不再等待Owner重复许可。

真实消费者兼容修改、冻结生产网格初始化/HA运行、严格驻定接受、实证输入采纳、31省GE/动态/IRF/福利及Results仍须各自对应合同和Owner边界。本设计不要求Owner现在批准一个尚未实施的生产放行；相关操作保持关闭，先完成可独立推进的工程。

ENGINEERING_VERDICT=PASS_REVIEWABLE_STATIC_INTERFACE_DESIGN_ONLY
SOURCE_FILES_VERIFIED=10
STATIC_OBSERVATIONS_CONFIRMED=14
SCIENTIFIC_IMPORTS_AND_CALLS=0
SCIENTIFIC_THRESHOLDS_ADDED=0
CODE_CHANGES=0
SCIENTIFIC_CONSUMER_RELEASE=FALSE
STRICT_KFE_STATIONARITY=FALSE
FORMAL_SOURCE_FREEZE=FALSE
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE

旧dirty工作树/HEAD/index、V010、WASM/R12 STOP、R13未授权、保护重绑定未授权、16项义务、旧预算和历史证据保持。本轮无分支删除、main合并、原件移动或全局配置修改；自审是工程审查，不是独立科学评议。
