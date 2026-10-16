# V010 IMPORT_GUARD SOURCE_ONLY 设计：Astra GitHub 原件独立验收

日期：2026-10-16（北京时间）。
**独立终审：`SOURCE_ONLY_GUARD_DESIGN_PARTIAL_WITH_OPEN_GATES__INDEPENDENT_DOCUMENTARY_LIMITED_ACCEPT`。**
**GitHub交付：`TEMP_REVIEW_CANDIDATE_VERIFIED`。**
**运行/科学：`ENGINEERING_RUNTIME_NOT_RUN__HA_SCIENCE_NOT_RUN__FULL_RUNNER_IO_CLOSURE_BLOCKED`。**
**阶段：Codex已交付并STOP、`ACTIVE_TASK=NONE`；下一步须Owner另选Windows原生隔离方案及host/guest trust broker的可信边界，新Python/runner/HA预算0。**
**远端临时文件：必须先完成本正式审议及治理状态远端回读，方能按Owner既批准协议限定清理；清理结果另立cleanup receipt，不改原候选commit或Git历史。**

## 一、提交/任务身份及字节认证（本轮GitHub实查）

- 唯一发行任务：`V010_IMPORT_GUARD_AND_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN`，发行commit `79f82934184292e7d021cbef8d4322c02c9cc0bc`、tree `80a18652013613f883d4d8b48a87cb2a36c882f7`、task blob `1bdb77a12d4494cae3052ba52392125a94bf0413`；任务已交付STOP，不能二次签发。
- Codex [临时脱敏候选](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/dc10a8f12f5333126b16bc56695abf2e67c5b2c0)：commit `dc10a8f12f5333126b16bc56695abf2e67c5b2c0`、tree `fabb22aae49f961afe336ad209fc56b382338c84`；**唯一Parent**为上述task发行commit。远端`review/ch5-temp-v010-import-guard-design-20261016` 在验收时HEAD为候选commit；与task基线`1 ahead / 0 behind`，恰仅新增两项白名单临时文件、无其他tracked变动。
- `_review_tmp/ch5/v010-import-guard-design-20261016/result.md`：Git Blob `18febce9a110f3d9d15c5ccd2e19ee674f46a017`，GitHub获取UTF-8原文字节**22424B**，独立SHA256 `ED3D8679335F3FE847FC771F4923BE578F2B3A4EF35D11919B075A09FBBB3C0C`。
- `_review_tmp/ch5/v010-import-guard-design-20261016/manifest.json`：Git Blob `d297f07d5bd867eb9b7b544e98fff03025ab47bd`，GitHub获取UTF-8原文字节**100391B**，独立SHA256 `C8F55625AE302F040CE738BBE62A1D8150E6146ED7DED0F7901B0DB06E17B9DA`。
- 两件均在任务30? 不，准确上限**result.md≤32KiB、manifest.json≤128KiB**内，UTF-8无BOM、LF无CR、含末行LF；常见私钥/token/敏感绝对Windows用户路径及邮箱模式扫描0命中，不能证明绝对没有一切秘密。SHA256由已用空字符串/abc标准向量检查的独立计算逻辑重新算得，不只信Codex数字。
- 两份文件完整公开且根本**没有创建到本轮治理分支/main/model分支**；GitHub tree只能核实远端没有其他新增tracked路径，**不能独立证明Codex本机没有临时目录或index写入**。Codex报告使用GitHub Git Objects API直接创建远端对象、0本地worktree/index/git add；本地回执仍为`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`。Owner上传回执哈希`18ACE20340D732A6D9640336A87470797307AE93099CC61101DC03E8AFB497D6`未由Astra读取D盘字节核算；本任务最初的PowerShell tuple/null失败1次和纠正行为亦保留本地报告级。

## 二、42节点风险队列与源身份交叉复核

本轮独立解析`manifest.json`schema `v010.import_guard_dependency_design.v1`，其`risks_for_all_42`恰**42项，42个唯一node_id**，每条均有`path,source_git_blob,raw_sha256,byte_size,prior_risk_label,risk_kind,static_evidence,owner_decision_needed,guard_requirement,remaining_unknown`，并标`STATIC_DISPOSITION_RECORDED__RUNTIME_UNKNOWN`且“before_materialization_or_execution=true”。分类严格为**20 UNRESOLVED、14 IMPORT_TIME_SIDE_EFFECT_RISK、8 PURE_DEFINITION**；不是20个已证明运行安全。前次1056条边记录/7重复/1049去重、70节点/42词法候选/9受监测、35 external基础事实沿用，未伪称另行运行依赖解析器。
- 由冻结模型commit `94de4501dec051b969bee9d852eba2d4591f30ef` 的三个**非递归**源码Git tree独立重建70条目，逐项验证此轮**42/42风险条目的路径、Git Blob、byte_size、mode=100644**全吻合，42份总518251B；另冻结pyproject.toml 285B + 公开runner静态文本58055B，合计576591B，与本轮SOURCE_ONLY报告的原字节阅读预算相符。这是远端**SHA1 Blob/大小**核验，不是对42个Windows本机文件重新计算SHA256；42个raw_sha256来自Codex固定输入认证回执。
- 从冻结GitHub源直接检查`boundaries.py`(63/99参数默认False)、`hjb.py`(43默认numerics=None，`HJBNumerics()`位于函数内)、`kfe.py`(数值文字默认值)、`multi_province/annual.py`(顶层`re.compile`)、`multi_province/provenance.py`(dataclass、六个元数据实例及`__post_init__`)、`corrected_diagnostic/selector.py`(`field(default_factory=dict)`类字段)，所述局部静态处置有实际源码支持。**源码静态证据只解释局部表达式，不证明第三方库、dataclass或原生初始化运行无副作用**。
- 三份**非空**根/子包`__init__.py`固定Blob `d99cf2762787ed6999e63745903116f95fe02ab9`、`c937c4aa4c6cf0ce4638e113d5d732f69b909923`、`58484859799b3fd3c79d33f93b5a26fa6d7c0193`继续逐字保留，拒绝空stub/删除eager imports。
- JSON的`default_or_annotation_lines`在**部分没有定位内容**的条目中保留`[null]`占位；属**非阻断的数据规范化问题**，以后机读报告应采用空数组而非null元素，不能以此把未知风险列归空。所有42条仍持UNKNOWN、没有因此自行放行。

## 三、架构设计实质性验收与不能接受的事项

**可限域接收的设计构件：**
1. 双信任根`git_identity_root` vs `source_assembly_root`，保留真实4条Git身份+第5条固定Commit inventory的nonce/audit/Job/reap绑定；纯源码根没有.git，**不能**取代Git cwd或放松身份守门。每份module需以`fixed commit/tree/path/mode/Git SHA1 header/byte length/SHA256`及same-open-handle/volume/fileID绑定，并进行start/end readback。
2. `UNINITIALIZED→GIT_IDENTITY_VERIFIED→INVENTORY_AUTHENTICATED→SEMANTICS_REVIEWED→RUNTIME_IMAGE_VERIFIED→OS_ISOLATION_VERIFIED→BINDING_SEALED→SOURCE_HANDLE_AUTHENTICATED→IMPORT_LOADING→IMPORT_EXECUTED→NINE_LOADER_BOUND→END_READBACK_SEALED→WAIT_INDEPENDENT_REVIEW`的门控设计；异常不得把`LOADING`冒充`EXECUTED`，不能在九模块未实际加载的情况下凭source存在宣布通过。
3. `RB1-RB9`路径/reparse/TOCTOU防御的分层方案，`DG1-DG6`对`Python/stdlib/numpy/scipy/wheel/PYD/DLL/BLAS/OpenMP`来源、初始化与Windows OS enforce的待验证清单；35外部静态名字分组为**1 compiler directive、26 STDlib_by_name、6 third-party/native、2 out-of-scope repo namespace**，后者不可假装已安装外部包。`H0-H7`分阶段明确哪些是DOCUMENTARY、UNKNOWN、NOT_RUN、CLOSED。
4. 编译/exec需在未来真正导入时受控，dataclass可能生成代码；仅依靠旧`sys.setprofile`函数名禁令/审计Hook、原5个Git child正常退出或Job分配并非native IO隔离证明。源根防替换、一次性签名capsule的issuer/nonce/寿命及新鲜Git identity到客体VM的证据传递必须经过**独立方案验证**。

**明确不接受的推断：**`IMPORT_GUARD_DESIGN_COMPLETE`、`OS_NATIVE_ISOLATION_VERIFIED`、`FULL_IMPORT_CLOSURE_READY`、`LOADER_RUNTIME_PASS`、`FULL_RUNNER_IO_CLOSURE=PASS`、`HA/GE/IRF/Results`。Windows VM无host共享/网络/凭据是**可考虑的未来隔离目标**，不是当前已经安装并可用的环境；host identity broker + guest loader更改当前进程/证据布局，须Owner认可可信计算基TCB后另行设计审查。其`DG4`明确`IMPORT_GUARD_OS_NATIVE_ISOLATION_UNRESOLVED`，`H4 N13/active timeout kill-reap`、`H5 dependency-only import`、`H6 九源码真实loader`均未运行。不得把合成68 PASS或原成功5 child拿来冒充这次门的实际运行PASS。

## 四、历史资源、保护及下一门

本轮报告`read_only_git_calls=4`、`source_objects=44`（42源码+pyproject+runner）、`raw_source_bytes=576591B`、`non_git_artifact_bytes_at_preseal=949954B`、`elapsed_seconds_at_preseal=573.419`、静态格式脚本失败1次修正，所有`Python/AST/model import/runner/HA/HJB/KFE/selector/GE/IRF/real data=0`。Git内部spawn写`UNKNOWN_NOT_MONITORED`。**这些Windows本地执行计数、实际物理工作目录是否未触及、最终文件大小与本地SHA只来自Codex脱敏原件/报告**，不能以网页审稿人在GitHub读取文件替代Windows实机取证。本次GitHub候选的唯一父/树/两文件哈希则已独立确认。

上一源图任务`SOURCE_ONLY_PARTIAL_IMPORT_CLOSURE_WITH_OPEN_GATES__DOCUMENTARY_LIMITED_ACCEPT`和上一Windows B–E`PARTIAL_ENGINEERING_DIAGNOSTIC`、旧科学实施pytest4/6-driver1/4-HA1/26-selector1626-roots1642、两次单点Python各1/1/HA0、首次43,519,638B超旧32MiB 9,965,206B、受保护原8dirty/index/staged/untracked/ignored/external common-dir及旧失败证据保持。`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`real C8 A–D REQUEST_ONLY`、`V011 NOT_STARTED`持续。原V010冻结科学plan blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、模型经济/税/GovInv/资产回报/lagged-NKPC不变。

**新的Owner决策待办**：`WAIT_OWNER_V010_WINDOWS_OS_ISOLATION_AND_TRUST_BROKER_CHOICE / STOP`。如Owner愿继续，只授权前置OS隔离可行性与broker信任架构的静态比选/风险取舍，再根据可用环境决定是否分阶段工程实现；本报告本身不派发执行、不重新使用旧工程3/4与runner1/2额度，也不启动HA。
