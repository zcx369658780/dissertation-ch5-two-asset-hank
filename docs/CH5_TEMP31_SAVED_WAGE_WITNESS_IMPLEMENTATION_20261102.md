# TEMP31 保存工资见证的类型化接口 · 2026-11-02

STATUS=IMPLEMENTED__PINNED_SAVED_RECORDS_RECONCILED__NO_SCIENTIFIC_CONSUMER_RELEASE
AUTHORIZATION_PARENT=6a12a47bb26c45b41176f5fa749b4b3cbb58db78
LOCAL_CODE_CANDIDATE=547a17b1b0e28d67a4944dd819412d64038955de
LOCAL_CODE_PARENT=d042472e4748ff877e5c83709301ab49a0c67245
LOCAL_CODE_TREE=32bc54478f468049b8f3b822de672fd4356216f3
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

Owner明确同意继续，并将同类调试的派单权限委托给Codex，见[委托规则](CH5_TEMP31_DELEGATED_DEBUG_AUTHORITY_CURRENT.md)。本轮是已保存见证的纯工程对接，不需要启动科学worker，不重用前次1/1已关闭的工资观测额度或初始化剩余7次。

## 已实现的行为

既有标准库模块temp31_wage_evidence_preflight.py增加不可变SavedWitnessArtifact/SavedWitnessPin及只能经核对工厂生成的SavedWageWitness。reconcile_saved_wage_witness接收当前九源字节回执、明确上下文、十类保存记录及其预期哈希/大小；不读文件、不导入科学模块、不重新计算工资，不提供求解器callback或生产激活入口。

十类记录为原授权、固定合成输入、持久进入claim、父进程回执、实际调用参数、函数进入记录、函数返回记录、原身份交接回执、运行结果和事件账本。先检查角色完整/唯一及所有字节哈希，再严格解析JSON，拒绝重复key、NaN/Infinity、指数溢出、非对象记录或畸形JSON。类型敏感地核对次数，布尔TRUE不能冒充进入1次；事件顺序、超时/退出、授权/输入/源身份、实际参数/返回与pending全部一致才返回记录回执。

输入六角色载荷由已保存实际参数重新编码，返回载荷由已保存返回值重新编码；不求值企业工资表达式、不改价、不再次调用源函数。上下文、省序和生成1/进入2标签与原保存记录一致；标签仍为隔离合成标签，不代表真实年度外层迭代。

该工厂仅支持此次成功合成观测的保存记录格式；不是任意科研运行的统一接受器。expected_pins必须来自另行固定的受权历史清单，不能用调用方同时提供的内容和自算哈希证明来源或执行真实性。Python不可变类型和工厂限制属于工程接口约束，不是抵御同进程任意篡改或原子OS隔离的安全证明。

## 现场对接与检查

前次证据清单SHA-256=c6b41cdad2124c86f98fdb608643179cafcd186fc4827b139e7469b70deb222f，固定后本轮未改。按其预期值读取十份文件，先核大小/SHA-256；SourcePin文件也按同清单核验，再只读重核九个指定源文件。记录的授权、进入/返回、六输入及输出身份全部对接成功。原始输入/输出、账本、执行器和完整回执继续LOCAL_ONLY，仅公开计数、代码身份和哈希。

测试先行：新增接口缺失时，1项测试出现预期AttributeError（错误1）；实施后20项新+79项既有共99项通过；工程自审补充4项授权数字类型、快照回放、指数溢出/空账本行及缺字段拒绝检查，最终24项新+79项既有=103/103通过，失败/错误/跳过0。既有检查为34预检/pending、34stub和11静态合同；不是全科学pytest。

受界执行器只定点加载标准库工程模块并监视导入/原科学src函数；测试与现场保存记录对接的NumPy/SciPy/原模型/exports/validators导入及科学调用均0。没有新依赖、HA节点生成、工资重算、初始化/root/求解或实证数据访问。工程自审覆盖正确性、结构、输入/身份边界及读取限额；未声称独立科学评议。

## 版本和资格

| 路径 | Git Blob | bytes / SHA-256 |
|---|---|---|
| src/ch5_two_asset_hank/multi_province/temp31_wage_evidence_preflight.py | 3e238838692a8e335e7e290d8cbb0348e390423c | 23915 / 5278075702c0bf93f750ab858d438e5f0e5c6bd5d31eea4380f6ce36cd629fa6 |
| tests/test_temp31_saved_wage_witness.py | 0002f08424b1e51948ced6cdd171e9265c8f1e4e | 16342 / 6894b572f97e320ffeea749fc848a357af804ba2556f05cc145f1059b50d297b |

相对初始物化源，原565路径Blob全部保持，现有572个选定代码路径：新增初始化、两个工程模块和四份测试。该片只扩展工程模块并新增测试，不改科学源码、参数、输入、价格、容差或HA grid。源码candidate仅本地，不提供不存在的远端源码链接。

RECEIPT_SCOPE=SAVED_SYNTHETIC_WAGE_OBSERVATION_RECONCILED_ONLY
RECORDED_INVOCATION_CONSISTENT=TRUE
LIVE_EXECUTION_VERIFIED=FALSE
PENDING_PRODUCER_INVOCATION_VERIFIED=FALSE
CONSUMER_READY=FALSE
SCIENTIFIC_CONSUMER_GATE=PRODUCER_INVOCATION_NOT_VERIFIED
MODEL_ACTIVATION=FALSE
FORMAL_SOURCE_FREEZE=FALSE
Results=FALSE
REAL_GE=FALSE

已存在的外部单次源函数观测仍是其原资格；本轮回执证明保存记录一致，没有新观察、正式生产凭据、科学数据采纳或接受权。真实生产凭据/HA组件、严格驻定、GE/动态/IRF/福利和Results仍未完成。下一工程片为生产工资凭据与正式HA资格交接接口的静态设计，不自动改消费者或启动科学运行。旧dirty树/HEAD/index、历史原件/缓存/证据、V010、WASM/R12 STOP、R13未授权、保护重绑定未授权和16项义务保持，无分支清理或main合并。
