# V010 SOURCE_ONLY transitive import：Astra上传原件独立验收

**日期：2026-10-16（北京时间）**
**正式限域裁决：`SOURCE_ONLY_PARTIAL_IMPORT_CLOSURE_WITH_OPEN_GATES__INDEPENDENT_DOCUMENTARY_LIMITED_ACCEPT`**。
**远端身份：`FROZEN_GIT_TREE_BLOB_SIZE_70_OF_70_VERIFIED`；抽样原始文件SHA256 `6_OF_6_VERIFIED`；运行时进口/Windows/HA `NOT_RUN`。**
**交付状态：`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`；Codex已交付且STOP，`ACTIVE_TASK=NONE`。**
**下一停点：`WAIT_OWNER_V010_IMPORT_GUARD_AND_DEPENDENCY_RESOLUTION_DECISION / STOP`。本裁决不发行新执行任务，不授予Python/HA预算。

## 1. 审阅对象、上传文件确切字节与冻结Authority

Astra实际读取本次Owner上传的两份脱敏原件：
- `review_source_only_import_closure_manifest_20261016.json`：**102135字节**，SHA256 `7DFA4A17F0AC9832FCD3093881D4FE55024EE0D21C5352EDEA90D675DBD9764C`；可正常JSON解析，版本`v010.source_only_import_graph.v1`。
- `review_source_only_import_closure_result_20261016.md`：**15502字节**，SHA256 `F9CF010A221550161A939D0CB2778FD19B5DAA19E7C2D82D64BB9CF02DC11E0B`；与JSON核心数值及分类一致。

两份均UTF-8、仅LF、无BOM、末尾LF；常见token/PEM/用户私有绝对Windows路径/邮箱正则扫描无明显命中，不证明绝对无秘密。**它们是当前会话直接上传的文件，绝未作为Codex新的GitHub review候选自动发布**。

冻结任务：`V010_SOURCE_ONLY_IMPORT_DEPENDENCY_CLOSURE_AND_READONLY_ASSEMBLY_PLAN`，发行commit `a2c9bf4b57aa9ce8f0c9ae5a1d920e141ee57ebd`，tree `364bb9184c554caa5ecf3b273ef5bd8b6d7271e9`，blob `7affb983e000c487dc306852383d747420400a63`。原模型commit `94de4501dec051b969bee9d852eba2d4591f30ef`，tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，唯一parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，GitHub实核。上一B–E工程 [独立主审](runner_io_windows_be_github_primary_review_20261016.md) blob `67c15e010c4a90b9773899cd699222d756fe5772` 的 PARTIAL 资格不改变。

## 2. 70份冻结模型源真实性：独立GitHub原树全覆盖

Astra从固定model Git Commit读取下列三个**非递归Git tree**，避免使用已截断的全仓recursive返回：
- `src/ch5_two_asset_hank/`：18个.py，tree `50aff40936c1c7232853eb0b3c32901f101bcae0`；
- `corrected_diagnostic/`：30个.py，tree `e83a5ab436d050bcc8ac60114f3451c6154e1645`；
- `multi_province/`：22个.py，tree `ecaee158decfc6dfe51c4e69789ec16d4d424bec`。

**Manifest全部70个module的`path/source_blob/byte_size`与GitHub 70/70个树条目逐项一致、模式均100644且唯一**；并非只抽样查看Git Blob。70个.py大小合计1102813B，冻结`pyproject.toml`另285B、Git Blob`5c778f7ccbbabfaf1046d4696cf843dc0adbb34c`，总数恰好等于报告71个对象/1103098B。三份原始非空`__init__.py`均在相应固定tree内。对三个init、`multi_province/annual.py`、`multi_province/provenance.py`、`corrected_diagnostic/nonlinear_continuation.py`，另从固定GitHub源实际读取原内容、独立重算**6/6 SHA256与字节数**，均与Manifest相符。其他64份的Git SHA1/byte_size独立核实，但本次没有声称重算其全部raw SHA256；这些raw SHA256保留为Codex原件声明。

## 3. 1056图记录的完整结构复核、42可达与不确定性

独立解析JSON验证70个node ID恰为0..69，module/path/blob各唯一；1056条edge均为六字段tuple，所有source、target、line、type、role有合法域；node.imports与edges反向索引完全一致；35个external记录的edge_ids也与1056条edge目标一一吻合，**结构错误0**。
- type：`IMPORT_TIME=1017`、`FUNCTION_LOCAL=38`、`DYNAMIC_UNKNOWN=1`；其它类型在这版词法检查中观察到0，**不是语义证明绝对不存在**。
- role：`PACKAGE_PARENT_INIT=356`、`FROM_BASE_MODULE=464`、`IMPORT_MODULE=227`、`FROM_CHILD_CANDIDATE_ATTRIBUTE_BINDING_UNVERIFIED=7`、`DYNAMIC_TEXT_MARKER=1`、`AFTER_ENGINEERING_GATES_FROM_ENTRY=1`。
- 从真实runner入口node=-1，仅沿`IMPORT_TIME`到包内node遍历，得到**42个唯一词法可达候选**，与全部`entry_reachable`标记及`predicted_first_encounter_order`准确一致；九份`monitored_nine`均在其中，额外33份候选不在Stage A九源白名单，另外28个全量索引node未在该入口可达集合内。这个42并非运行证实“必定导入”。
- 1056为**边记录数**，存在**7份逐字段完全重复记录**（涉及重复父包预置边）；若按六字段tuple去重为1049条。需以后文件清楚同时记`edge_records=1056`、`unique_edge_tuples=1049`，而不是误称1056条互异模块间语义依赖。这个非致命注记不改变42个候选节点集。
- 入口候选42个node的词法风险标签：`UNRESOLVED=20`、`IMPORT_TIME_SIDE_EFFECT_RISK=14`、`PURE_DEFINITION=8`。`PURE_DEFINITION`只是当前词法没有发现额外风险，不能代替执行安全认证。

JSON另列**35个外部静态名称**和**5项UNKNOWN分组**：本入口外函数helper `compile/exec`动态目标，`exports`与validators的仓库外scope命名空间，两个comprehension/continuation词法误报的人工处置，以及别名绑定、默认参数、dataclass/装饰器、stdlib shadowing、NumPy/SciPy/native依赖及动态加载的语义欠证。pyproject仅声明Python≥3.11、numpy≥2.0、scipy≥1.14、setuptools≥68，不证明当前Windows运行库或ABI符合。故`FULL_IMPORT_CLOSURE_READY`及`LOADER_IMPORT_AUTHENTICATED`**均不成立**。

## 4. 静态装配蓝图与具体工程阻断

Codex蓝图正确拒绝制造空init、剥离原包eager imports或在只读Stage A clone里偷偷补签出。未来只有Owner另行授权，才能在**全新独立只读源根**按固定Git Blob与SHA256物化经审阅的闭包，且与原模型Git identity root区分；当前runner`VerifiedFinder.root=gate.root`、`GitGate`固定4身份+第5inventory真实Git子进程绑定，必须先做**工程设计变更独立评审**，不能指向缺少.git的纯源码根、也不能放宽源身份守门。所有包init、transitive库初始化、`__file__`/loader/sys.modules及科学调用拒绝都仍需后续真正ENGINEERING_ONLY检查。第三方native初始化不是Python`sys.setprofile`能单独证明拦截的OS副作用。

## 5. 本地资源、GitHub失败及资格边界

两份报告一致称：本轮**Python、AST、compile、模型import、runner、HA/HJB/KFE/GE/IRF/pytest/真实数据均0**；模型Git原始源码71对象/1103098B，runner源额外58055B，文本保守预留196608B，上界1357761B小于原5MiB；文件保守78≤90，SOURCE_ONLY身份Git命令9条，静态PowerShell提取4阶段，wall1169.666秒低于7200秒。本会话独立核了报告字段及远端对象，但未访问Codex Windows本机进程账、受保护原树/index、完整artifact最终大小；这些属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`。私有`DELIVERY_RECEIPT.json`据Owner提供SHA256 `38903B28D1809CF9DCAEB736F525C8ACB420C3E5BF048035DE1AEFF8DEE13350`，本会话未直接核hash。

发布失败：报告记录用`--depth=1 --filter=blob:none`定向准备task基线后，在第10条`git write-tree`报exit128：禁止lazy fetch且所需promisor blob缺失。前9条发布Git报告exit0；没有候选commit、review branch、push（0次）。GitHub目标`review/v010-source-only-import-closure-20261016`现场查询404，发行task tree远端真实存在。这是**本地部分Git对象获取策略与write-tree闭包不相容**，不是冻结GitHub模型或任务对象损坏，也不能在本次STOP任务内自动补fetch/重试。**源图文档限域验收与GitHub发布资格分开**：`SOURCE_ONLY_PARTIAL_IMPORT_CLOSURE_WITH_OPEN_GATES`的自报分类恰当，`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`保留。

## 6. 独立结论、后继门及历史保护

**本次认可`INDEPENDENT_DOCUMENTARY_LIMITED_ACCEPT`**，仅覆盖70源Git Blob/大小、静态图结构/42词法候选、正当地保留动态/库不确定性及可审阅的隔离装配蓝图。不认定全导入语义闭包、动态加载安全、真正Windows loader通过或全部OS/Job timeout故障都经实测。任何新Python/工程runner、模型clone/fetch/checkout、Git补推和HA科学调用均须**Owner另行批准新的独立权限和预算**；本轮STOP旧额度不结转。

建议下一步先Owner单独决定`IMPORT_GUARD_DESIGN_AND_DEPENDENCY_GATE`：静态review42入口的20未解析风险、第三方runtime/ABI与源根-身份根双绑定设计，明确真正只读源装配的信任锚及完整性合同，再分阶段申请工程执行；不重复对70源从头做词法盘点。原V010冻结科学plan blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、原两次单点Python1/1及首次存储超额、上一Windows B–E工程3/4 Python和1/2 runner剩余额度、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、real C8 A–D REQUEST_ONLY、8dirty/index/外common-dir/旧失败原证、V011 NOT_STARTED全部保留。
