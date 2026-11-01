# TEMP31 惰性接口骨架与模拟接线检查 · 2026-11-01

STATUS=IMPLEMENTED_STUB_ONLY__45_FOCUSED_ENGINEERING_AND_STATIC_CHECKS_PASS
AUTHORITY=OWNER_CONTINUATION_AFTER_EXPLICIT_INERT_INTERFACE_AND_MOCK_WIRING_PROPOSAL
GOVERNANCE_AUTHORIZATION_PARENT=a3f764c29d235c6abf67f58f18473f9010230f5b
LOCAL_CODE_CANDIDATE=df05d020b67030a8878bd43d755afe432cc17ae1
LOCAL_CODE_PARENT=a6083dac37f3e543e21401c1b4e7d3295255ffd7
LOCAL_CODE_TREE=ca17f4db0443e941ae9c2cc9f0649bd5795773ef
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED
REAL_HA_AND_PRODUCTION_ACTIVATION=FALSE

本轮落实上一阶段生产接线规格中的惰性工程分片，新增一个仅用标准库的接口模块及行为测试。它只校验显式模拟回复和身份声明，不实现净工资经济公式、不调用生产者/初始化/HA，不认证真实来源或数值结果。现有科学源码、生产入口、package __init__、网格、参数和输入均未修改；没有把它接入旧年度入口。

## 两份新增代码身份

| 路径 | Git Blob | bytes / SHA-256 |
|---|---|---|
| src/ch5_two_asset_hank/multi_province/temp31_binding_skeleton.py | f6971d120f9a8b78b975d3b1370ce315b2c42fa0 | 8549 / 2e91f6a34a027f788d6d13524fabc5db71bdeac44b11de3df7afbe01d09fd523 |
| tests/test_temp31_binding_skeleton.py | cbce4c0e38f9c4c0e8a84b501f7b5837d9cf520b | 12207 / 7e7b324c6d8ed6801b7e4d14ab14bf4e698d3f3f735f8b86091c4c3a5bdd51db |

代码仅在独立源码工作区的上述本地提交；治理同步公开这份说明和进度，不上传源码/测试原文或完整测试日志，不能用GitHub链接冒称本地candidate已公开。

## 接口的实际行为

- BindingContext携带上下文、省序、进入期次、快照/来源集合/网格的SHA-256格式身份声明；网格元数据限定既有(b,a,z)=(20,20,2)及轴顺序。它不读取、生成或修改实际HA节点，不计算真实网格/源文件哈希；真实身份核验仍在未来外部绑定层。
- StubWageEvidence仅支持LATER_NET_STUB和NUMERICAL_INITIAL_GUESS_STUB。后轮必须生成于前一轮；初猜标签只能进入第一轮且没有前轮生成记录。初猜标签不计算19或验证价格，只练习已有角色的交接。工资载荷是字符串token，不是工资数值；NET_ONCE为声明校验，不能代替真实工资公式或生产调用见证。
- StubOriginCall绑定省份标签、索引、同一上下文和该省工资token，没有tau/migration_costs参数。错上下文、省序、期次、来源/快照身份或工资token不能混用。
- StubBackend只能保存预先给定的StubOriginResult元组；不接受求解器函数、插件、任意callback或实际HJB结果对象。build_stub_batch默认DISABLED，只能以显式STUB_ONLY模式校验该类模拟数据。require_real_execution即使收到enabled=True也始终拒绝，没有环境开关、默认真实求解器或隐藏的HA调用路径。
- StubBatch只在省份完整、无重复、顺序一致、每行身份匹配、模拟网格身份前后一致、单位声明为未预乘人口且模拟资格声明完整时构造成功。缺行、错序或任何行不合格都不返回部分批次；它不写状态、不进行人口缩放或经济聚合。
- 模拟资格必须同时声明HJB、原算子驻定和密度检查通过，且basis为ORIGINAL_POST_OPERATOR_STUB_CHECK；HJB-only和CONTAMINATED_RAW_SYSTEM_ONLY标签被拒。这里不计算残差、密度或阈值。即使模拟检查全通过，输出scope仍固定STUB_ONLY_NOT_SCIENTIFIC_ACCEPTANCE，real_execution_enabled及formal_ha_accepted始终FALSE，不能直接提升为科学证书。

## 测试先行、实际结果与边界

先写行为测试，记录新模块尚不存在导致的预期red：setUpClass报1个缺文件错误，实际tests_run=0，不冒称已运行一个失败行为用例。实现后首轮31项新测试和既有11项AST/符号合同检查共42项通过。

随后补充31个虚拟来源地完整批次，以及非字符串mode/税状态的错误对象检查。新增两个对象检查先真实失败：宽松相等比较可能执行外部对象的__eq__并接受错误类型。修复仅为先检查普通字符串类型再比较；最终34项新行为测试+11项既有静态合同检查，共45/45通过，错误/失败/跳过均0。未在最终通过后重复相同测试。

覆盖默认禁用、显式stub依赖、拒绝任意求解器callback、运行模式不可升级、上下文/省序/快照/源身份、生成期次、初猜角色、净工资声明、无二次扣税入口、不完整/重复/错序批次、返回身份、网格元数据/指纹、HJB-only/污染系统标签/密度失败、预乘人口单位声明、数值或可变工资载荷，以及31个虚拟省份的完整拼装。31标签检查只使用不透明字符串，不生成经济价格、HA网格或科学数组，不是真实31省运行。

测试通过定点文件加载该新标准库模块，避免原package __init__导入科学依赖。执行器阻断NumPy/SciPy/原模型包/exports/validators导入，并拒绝既有src科学文件的函数进入；实际被拒导入尝试0、已加载科学模块0、既有科学函数调用0。全科学pytest套件未运行，因为其中导入/执行科学路径不在本轮stub-only授权内；普通完整模型包导入、真实接口/数值集成和运行环境闭合仍未认证。本轮工程自审不是独立科学评议。

原选定代码树所有既有路径Blob保持，源码提交仅新增上述两文件；旧初始化候选/11项合同保持。现有初始化调试账本仍3/10已用、7剩余，本轮工程测试不导入/执行初始化或求根，不消耗该数值预算。原始red/green/审查回归记录、测试执行器和版本回执仅LOCAL_ONLY。

## 当前门与下一工程对象

真实生产工资调用凭据、与现有消费者校验的兼容桥、原HA公开组件包装、真实严格驻定资格及外层生产入口仍未实现或启用；本模块的字符串token和模拟通过标志不能替代它们。下一工程对象是实际生产凭据适配层的来源/上下文接口与外部身份预检，仍保持科学调用默认关闭；真实生产者/冻结网格初始化/HA及严格驻定运行须匹配对应来源、科学决定和预算。

EXISTING_SCIENTIFIC_SOURCE_EDITS=0
HA_GRID_OR_PRICE_PARAMETER_CHANGES=0
SCIENTIFIC_INITIALIZER_ROOT_HA_HJB_KFE_GE_IRF_POLICY_MATLAB_CALLS_THIS_TASK=0
ENGINEERING_VERDICT=PASS_BOUNDED_INERT_INTERFACE_AND_OPAQUE_STUB_ROUTING_ONLY
REAL_PRODUCTION_BINDING=NOT_IMPLEMENTED_NOT_ACTIVATED
FORMAL_SOURCE_FREEZE=FALSE
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE

V010、历史证据、旧dirty工作树/HEAD/index、WASM/R12 STOP、R13未授权、保护重绑定未授权、16项义务和旧耗额保持。没有分支删除、main合并、原件移动或全局配置修改。
