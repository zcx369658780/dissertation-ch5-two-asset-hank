# V010：IMPORT_GUARD 与第三方依赖门的 SOURCE_ONLY 设计任务（Owner 2026-10-16）

**任务唯一ID：`V010_IMPORT_GUARD_AND_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN`。**
**Owner授权范围：**2026-10-16 Owner在上轮依赖图限域独立验收后答复“可以……请继续”，并进一步明确GitHub临时审阅目录**不得进入本地项目工作树目录或Git索引**；由Astra仅签发一轮静态架构/门禁设计。**不包含Python、AST、model import、真实Windows runner、科学HA/HJB/KFE、GE/IRF、模型数学修改、真实数据访问或新运行预算。**
**冻结与STOP：**本任务发行的固定Commit、Tree、文件Blob须由Codex在运行前从GitHub真实回读（以后续`TASK_CURRENT`准确冻结SHA为准）；任务不可改、不可重发。唯一结果`V010_IMPORT_GUARD_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN_RESULT`，终止于`WAIT_ASTRA_V010_IMPORT_GUARD_DESIGN_REVIEW / STOP`。

## 0. 冻结输入与最小设计目标

- 仓库`zcx369658780/dissertation-ch5-two-asset-hank`，仅`migration/astra-workflow-20261012`为动态治理入口。
- **科学代码唯一固定身份：**模型commit`94de4501dec051b969bee9d852eba2d4591f30ef`，tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，sole parent`a1db8c114dec0ab69d69a5576e153a7f868cba0e`。原V010冻结plan commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`不可追改。
- 前一`V010_SOURCE_ONLY_IMPORT_DEPENDENCY_CLOSURE_AND_READONLY_ASSEMBLY_PLAN`已交付并独立限域验收：[Astra主审](source_only_import_closure_uploaded_primary_review_20261016.md)blob`07371fbeb56097c74c02f8f4d1e9e86460f0550e`。Codex原脱敏本地原件位于**前次新scratch**的准确安全文件名`review_source_only_import_closure_result_20261016.md`（15502B、SHA256`F9CF010A221550161A939D0CB2778FD19B5DAA19E7C2D82D64BB9CF02DC11E0B`）与`review_source_only_import_closure_manifest_20261016.json`（102135B、SHA256`7DFA4A17F0AC9832FCD3093881D4FE55024EE0D21C5352EDEA90D675DBD9764C`）。**仅允许精确只读这两份已经脱敏的材料**作为现成图的来源，不得重新打开此前旧失败原始日志或私有`DELIVERY_RECEIPT.json`。若两份脱敏文件不存在/哈希不符，只可用GitHub本轮固定主审已有的有限事实保守设计，明确`GRAPH_INPUT_UNAVAILABLE`，不能重新扫整库救PASS或要求Owner搬运私有文件。
- 原图`70`模型nodes/1056 edge **records**，其中7精确重复六元组、1049 unique edge tuples；42个入口词法候选（九份Stage A白名单内，额外33个需真实原blob）；42内20个`UNRESOLVED`、14个`IMPORT_TIME_SIDE_EFFECT_RISK`、8个`PURE_DEFINITION`（词法标签并非无风险的运行证明）。35个external名字及动态导入/native初始化均UNKNOWN。三个原始真实非空`__init__.py`不得替换/空置。
- 上一Windows B–E工程[独立主审](runner_io_windows_be_github_primary_review_20261016.md)Blob`67c15e010c4a90b9773899cd699222d756fe5772`：5个真实Git child正常退出/审计回执、68合成测试PASS、N13未评估；缺包init导致`LOADER_IMPORT_NOT_EVALUATED`，`FULL_RUNNER_IO_CLOSURE=BLOCKED`。上述旧工程的Python 3/4、runner 1/2余额**不结转**，本任务不能代为启动或认证运行。
- 本轮只需形成可供未来独立审议的**工程守门设计决策草案**，不是补充运行结果、不补原GitHub`write-tree`失败历史候选。

## 1. 强制静态分析与设计输出

**A. 可信输入与真正风险队列。** 先校前轮两脱敏文件的准确SHA256/字节数、JSON schema/70节点/1056记录、模型fixed commit/hash、前审Blob，再用现有42候选风险分类对**20个UNRESOLVED、14个IMPORT_TIME_SIDE_EFFECT_RISK及8个纯定义标签**分别形成`node_id/path/source_git_blob/risk_kind/static_evidence/owner_decision_needed/guard_requirement`，明确default/annotations、dataclass decorator、class body、顶层构造、`sys.modules`变化、`from ... import name`子模块/属性绑定的 UNKNOWN，而非猜运行结果。35个externals单列`STDLIB_BY_NAME_ONLY`、`THIRD_PARTY_NATIVE_ABI_UNKNOWN`、`OUT_OF_SCOPE_REPO_NAMESPACE_UNKNOWN`，不能把numpy/scipy的C扩展副作用判PURE_DEFINITION。
   
**B. 双信任根设计（不修改模型/guard源码）。** 现`GitGate.root`同时承担Git身份和`VerifiedFinder.root`源码读取。给出严格设计分离：只读`git_identity_root`仍指向已认证的独立Stage A Git clone（HEAD/Tree/Parent/common-dir，4真实身份Git commands＋第五固定Commit inventory保持）；未来的`source_assembly_root`必须是**新排他、无symlink/reparse、位于受保护root外**的独立目录，仅在未来另获权限后从固定commit的Git raw blob恢复本次已认证闭包的真实源。两根通过**一次性绑定manifest**精确联结`fixed commit/tree; module path; raw Git SHA1 header blob; file byte length; SHA256; fixed no-pycache; start/end readback`，禁止将纯源码目录当作Git cwd、放宽GitGate、共享Git objects、伪造空init、改变import order或绕过九源`__file__`/loader/sys.modules实际认证要求。设计应给出伪接口、状态转换、失败回执和OS路径攻击（TOCTOU/reparse替换）的fail-closed策略；**不能实际写出可执行新Python runner**。
   
**C. 信赖的第三方运行时、环境和native I/O隔离前提。** 冻结`pyproject.toml`Blob`5c778f7ccbbabfaf1046d4696cf843dc0adbb34c`仅声明Python>=3.11、numpy>=2.0、scipy>=1.14及构建setuptools>=68，不等于Windows版本/位数/ABI已证。提出未来最小必需证据：受控Python/exe/库文件hash、numpy/scipy发行来源/版本/依赖DLL与sys.path、sitecustomize/.pth与hook provenance、第三方初始化读取/写入/网络/动态库的OS级隔离机制。**Python audit hook或sys.setprofile不足以证明native无文件/网络副作用**；若无法安全保证应保持`IMPORT_GUARD_OS_NATIVE_ISOLATION_UNRESOLVED / STOP`。不实际pip/install/import/执行系统健康探针。
   
**D. 最小解决顺序及验收准则。** 将已经核过的70源身份/42图候选、后续必须设计的full import semantic chain、Windows sandbox依赖、identity vs assembly root一致性、真正九源`VerifiedLoader`绑定、N13/真实kill/reap独立OS测试划分为可审计序列，逐门要求明确`PASS/UNKNOWN/FAIL_CLOSED`证明和未来Owner单独的工程进程/elapsed/RSS/artifact预算。设防：若OS侧不能隔离native/第三方副作用或42节点仍有导入执行时未认证对象，不能进入运行阶段；**最小必要性与边界**应优先于再进行70源词法重扫。任何研究方法变更、HA/Solve、真实C8访问仍属另一个Owner科学决策。
   
**E. 提交结构与分类。** 脱敏结果`V010_IMPORT_GUARD_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN_RESULT`，以及机读manifest至少包含`frozen_inputs,risks_for_all_42,root_binding_contract,external_dependency_gate,real_init_contract,unknowns,review_hinges,resource_ledger,delivery_identity`。除非能静态解释全部20/14/8节点及每项风险，不能称`IMPORT_GUARD_DESIGN_COMPLETE`；保守可报告`SOURCE_ONLY_GUARD_DESIGN_PARTIAL_WITH_OPEN_GATES`或`SOURCE_ONLY_GUARD_DESIGN_CANDIDATE_READY_FOR_ASTRA`，后者也不等于Windows runtime安全或科学PASS。未知项要具体到源码和门，禁止凭已有69 synthetic测试泛化安全性。

## 2. 资源、保护与严格STOP

- **本轮新Python/py/AST/pytest/model import/runner/HJB/KFE/HA/selector/scalarRoots/GE/IRF/MATLAB/真实数据进程均0**。PowerShell/Git只做静态读取/文本审阅和安全report整理，不触任何冻结模型数值函数；拒绝二级脚本调用Python。不能重建原/旧WORKTREE。
- 唯一新独立scratch建议`D:\ProjectTemp\ch5_v010_import_guard_design_source_only_20261016_01`（仅非Git项目外临时分析工件）；wall≤2h、SOURCE_ONLY额外原始源码读取≤55份/4MiB（优先前两脱敏manifest；不得全70重扫），只读Git身份/源码调用≤120次，非Git artifact新增≤8MiB（含日志、事务、最终/应急预留）。新`git clone/fetch/pull/checkout/reset/clean`模型次数0；Git对象来源若缺，标`INPUT_UNAVAILABLE`并STOP，不越权补取。
- 原受保护`D:\ProjectTemp\c5k1bturn56`、8个dirty tracked/index/staged/untracked/ignored、外common-dir、所有旧失败原证及原Stage A只读独立clone**不得修改**；原模型科学合同、GovInv/税/迁移/NumPy算法、旧V009、真实C8/2017/2018/B3不访问。
- 原SOURCE_ONLY发布失败`write-tree`第10命令exit128（blob:none/promisor对象缺）、候选commit/push均0属于前一STOP任务历史；本轮**不能复用旧发布对象库或其不完整index**以图节省预算。严格在新任务中获准的独立GitHub临时review方式发布；不能重试旧失败候选/补模型数据。

## 3. Owner批准的临时GitHub审阅交付（不得污染任何本地工作树）

**强制遵守冻结前已生效[临时交换协议](../../docs/CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md)，且本任务额外固定如下条件**：
- `SANITIZED_REVIEW_DELIVERY=GITHUB_TEMP_REVIEW_DIRECTORY_FIRST`。
- 唯一新的远端审阅分支：`review/ch5-temp-v010-import-guard-design-20261016`（发布前核分支不存在）。
- **唯一可发布的临时目录仅在该远端review分支的Git tree中存在**：`_review_tmp/ch5/v010-import-guard-design-20261016/`，严格限两个脱敏UTF-8 LF文件：`result.md`≤32KiB与`manifest.json`≤128KiB。不得发未经脱敏raw源码、私有绝对路径、环境secret、SSH凭据、真实数据或原本地receipt；若manifest过大则安全摘要聚合且标`DETAIL_LOCAL_ONLY`，不得省略必要UNKNOWN和对象哈希。
- **绝对禁止**在本地博士科研项目/模型repo/治理repo或任何原project worktree、其index/staging/dirty目录内创建`_review_tmp`、`git add`、checkout、stage、提交或共享Git对象；无需修改既有工作树的`.gitignore`/`.git/info/exclude`以掩盖。首选经授权GitHub Git Objects API直接远端造blob/tree/单parent commit/ref、**无本地Git worktree**；工具不支持时，仅允许在**项目外新独占无worktree的bare Git发布元数据仓库**（`core.bare=true`、不共享原objects/common-dir、不得`git worktree add`）定向取得**完整**任务发行基线对象。务必前置验证所有parent tree和blob完整性，禁止以前轮`--filter=blob:none`不完整基线`write-tree`而触发无授权lazy fetch。新bare metadata/object+临时索引（仅外部scratch内）上限1GiB；GitHub发布最多一次普通nonforce，失败LOCAL_ONLY STOP不重试。
- review commit的**唯一parent必须是本任务发行commit**，不能是动态HEAD或上一审议commit；发布后要读远端commit/tree/sole parent、仅两份白名单文件Git Blob+UTF-8原字节SHA256及远端branch HEAD。一切临时目录只在**远端review分支tree**中允许，严禁污染本地工作树。
- `ASTRA_AFTER_REVIEW=ARCHIVE_PERMANENT_VERDICT_THEN_DELETE_ONLY_TEMP_FILES_WITH_READBACK`：Astra独立验收后**先**把科学/工程限域结论和必要摘要永久归档治理分支并回读，**再**仅删除本轮远端review分支中上述两份临时文件、核当前分支tree已无路径、记录cleanup commit；不删除冻结task、正式主审、其它分支/历史失败、模型源。Git历史可能仍有旧字节，故上传前真实脱敏优先；此协议不授权强制重写旧commit或删除branch。

**最终停点`WAIT_ASTRA_V010_IMPORT_GUARD_DESIGN_REVIEW / STOP`。** 即使静态设计获Astra限域接受，所有Windows工程import/Job kill/N13/HA科学仍需Owner另行签发独立资源。原V010已冻结科学计划blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、历史两笔单点Python1/1与首次超额、旧Windows工程Python3/4与runner1/2 STOP、A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER UNRESOLVED/`model_activation=False`/`Results FALSE`/real C8 A–D REQUEST_ONLY/原8dirty/index/common-dir与全部失败原件/`V011 NOT_STARTED`全部维持。
