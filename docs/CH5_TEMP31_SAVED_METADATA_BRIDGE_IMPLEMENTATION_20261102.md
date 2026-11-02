# TEMP31 固定保存见证的元数据桥 · 2026-11-02

STATUS=IMPLEMENTED_PINNED_METADATA_BRIDGE__TWO_EXPLICIT_GAPS__ADMISSION_BLOCKED
AUTHORIZATION_PARENT=79b9c7290e49baa966ebb4008fd73cce9585e193
LOCAL_CODE_CANDIDATE=3f32f958be1574e173900479fc164a9aa5f46514
LOCAL_CODE_PARENT=656cf50aa41dd4db0a4f59b8f23a41c514f26dbd
LOCAL_CODE_TREE=c210511bb4e572c1c5996cd40e3fd2a5e99cfe30
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

本轮把[保存见证记录](CH5_TEMP31_SAVED_WAGE_WITNESS_IMPLEMENTATION_20261102.md)的已有元数据对接到[惰性准入模块](CH5_TEMP31_DORMANT_ADMISSION_IMPLEMENTATION_20261102.md)，不重新计算或读取科学载荷。桥接完成的是有据字段的投影及缺口报告，不是生产凭据或科学接受。

## 实际读取与映射

仅两份历史元数据文档：ACTUAL_SAVED_RECONCILIATION.json和OBSERVED_LINEAGE_RECEIPT.json。它们只含源pins、上下文、输入输出哈希/大小、资格标志与计数，不含原参数/返回数值数组。两份文件按各自独立固定历史清单检查原始字节数和SHA-256；两份清单自身也先核固定哈希。另对当前标准库工程模块的SOURCE_ROLE_PATHS做静态AST读取，不导入其科学目标，不读取九个目标源文件。

| 元数据清单 | SHA-256 |
|---|---|
| 保存见证工程交付清单 | ce450fff61243a9d84323d86ccbe10d3c1836dad5c653c5f053c9d943687afe1 |
| 原单次源工资观测清单 | c6b41cdad2124c86f98fdb608643179cafcd186fc4827b139e7469b70deb222f |

原source bundle的canonical元数据表示由root哈希、9份源pins及固定角色路径重新编码，得到1757字节，SHA-256精确匹配历史bundle=1a3d44635e53c623b7748e77553f708ac9b1480efcda67597a7c847043529825。这是清单元数据重建和哈希吻合，不是本轮源码回读、动态来源闭合或来源采纳。1757只表示这一重建元数据的实际编码长度，不拿它代替参数/数组大小。

已映射上下文、省序、生成1/进入2、六类输入的已记载SHA/大小、输出SHA/大小及历史manifest引用。原进入claim和事件账本仅传递历史清单条目身份，文件本身未在本轮读取；引用标记明确为“本轮未回读”。原输入/返回文件、日志、数组、CSR及真实数据均未访问。

## 两项真实缺口与准入结果

| 字段 | 现有记录 | 本轮处理 |
|---|---|---|
| 完整实际调用参数的canonical byte_count | lineage保存了canonical SHA，未给该完整对象大小 | 参数EvidenceIdentity保持None，另保留已记载SHA；不从其他载荷估计大小 |
| 实际返回向量shape | pending保存输出SHA与39字节大小，未独立记录shape | candidate.output_shape保持None；不以A/B两省标签推断实际shape |

非首轮候选现在允许None表示尚未记载的shape，inspect_wage_candidate会据此拒绝；首轮数值初猜仍要求显式shape。六个分角色输入的已记载大小，不等于完整函数参数对象的大小，也不能拿生成快照的392字节直接代替。

实际报告classification=BLOCKED，含WAGE_INPUT_RETURN_LINEAGE_MISMATCH、WAGE_SCOPE_NOT_PRODUCTION、UNVERIFIED_SOURCE_OR_INPUT_SCOPE及REAL_EXECUTION_DISABLED；consumer_ready/real_execution_enabled/scientific_acceptance均FALSE。除上述元数据缺口外，原合成scope、来源/输入采纳、现场资格和真实消费者桥仍未获得生产接受。旧外部一次调用的事实保持其原资格，不能把这次“缺元数据”说成原观测失败，也不能据重建哈希把它升级为真实生产来源。

## 工程实现与检查

新增bridge_saved_wage_metadata及不可变SavedWageMetadataBridge，复用现有惰性上下文、候选和拒绝工厂。解析器只支持该固定历史元数据格式，先核大小/哈希再解析，最大1MiB/文档；拒绝重复key、浮点/非有限JSON值、未知字段、缺角色/重复角色、scope或接受旗标升级、布尔计数冒充整数、清单或上下文/输入/输出身份变化。源清单只处理pins和编码；没有数组、数值载荷、源函数、callback或文件I/O能力。

新接口缺失时1项测试出现预期AttributeError；实现后18新+145旧=163项限定检查全部通过，错误/失败/跳过0。检查覆盖固定哈希、有限字节读取接口、元数据格式、角色和清单重建、上下文/输出/快照漂移、scope/接受旗标、实际缺件、缺失引用及只读报告；工程夹具不是科学观测。现场固定元数据对接也通过，明确得到两个缺口和BLOCKED结果。

受界执行器定点加载标准库工程模块，阻断科学包导入并监视原科学函数进入；测试与现场映射的科学导入/函数调用、新科学worker均0，原始参数/返回数值解码0。这里只验证工程元数据投影，未重算工资、初始化/root/HJB/KFE/HA/GE/IRF/policy/MATLAB，也未重跑全科学测试。自审是工程审查，不是独立科学评议。

| 路径 | Git Blob | bytes / SHA-256 |
|---|---|---|
| src/ch5_two_asset_hank/multi_province/temp31_dormant_admission.py | d2589e07e1fb0cd8deb2d0c3a7d4549180293733 | 33660 / eac5f111fb13c5953ad17a9ecfe69ff863934467dc094f81f8ee5f323d8ac8fa |
| tests/test_temp31_saved_metadata_bridge.py | ced09124ca0d8b94222cfb9c16e19b5a32e8a7f5 | 11152 / 6f6a22326c36d61c3ab2745da0a57e2ed082640dcdfffc0f755352a817aba6a4 |

原565路径Blob全部保持；原574仅扩展惰性工程模块，新增一份测试后575个选定代码路径。代码candidate仅本地，公开同步脱敏文档，不提供不存在的远端源码链接。原科学源码、SOURCE_COMMIT、公式/参数/输入/价格/容差和HA网格不变。

下一工程先形成只追加的元数据补录合同，明确固定记录、可读范围、非数值提取方法和新旧证据的绑定；本轮未读取原参数/返回文件来补录，也不允许通过重跑、补造或改旧文件解决缺口。科学接受与生产运行仍须其各自对应门。

ENGINEERING_VERDICT=PASS_PINNED_METADATA_PROJECTION_WITH_EXPLICIT_GAPS
ADMISSION_CLASSIFICATION=BLOCKED
ARGUMENT_BYTE_COUNT=UNKNOWN
ACTUAL_RETURN_SHAPE=UNKNOWN
SCIENTIFIC_PAYLOAD_VALUES_READ_OR_DECODED=FALSE
SCIENTIFIC_IMPORTS_AND_CALLS=0
CONSUMER_READY=FALSE
REAL_EXECUTION_ENABLED=FALSE
SCIENTIFIC_ACCEPTANCE=FALSE
FORMAL_SOURCE_FREEZE=FALSE
STRICT_KFE_STATIONARITY=FALSE
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE

原工资1/1额度关闭、初始化3/10已用余7保持。旧dirty树/HEAD/index、历史证据、V010、WASM/R12 STOP、R13未授权、保护重绑定未授权和16项义务保持，无分支删除/main合并/原件移动/全局配置修改。脚本、完整回执与日志继续LOCAL_ONLY。
