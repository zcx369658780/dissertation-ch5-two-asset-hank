# 第五章 TEMP V010｜控制器来源溯源的两处限定恢复（长任务）

TASK_ID=CH5_TEMP_V010_CONTROLLER_LOCATOR_TWO_BLOCKER_RECOVERY_20261021
REVISION=ISSUED_20261021_R1
OWNER_APPROVAL=2026-10-21 同意仅针对两处阻断的有界修复
SCOPE=WINDOWS_IDENTITY_CAPTURE_AND_EXACT_GITHUB_OBJECT_READ_ONLY
OLD_TASK=CH5_TEMP_V010_CONTROLLER_SOURCE_PROVENANCE_LOCATOR_GATE_20261021__CLOSED_ON_RESOURCE_HARD_GATE
NO_HA_HJB_KFE_GE_IRF=TRUE

## 一、目标而非自动续跑
上一轮真实控制器来源溯源停止于`STOP_RESOURCE_GITHUB_DIRECTORY_METADATA_LIMIT_EXCEEDED`，Run`bb28bb74ec6f46c78287d82937eb1209`。冻结GitHub每prefix最多64条，然而`tasks`单次返回400条；另有Windows `DirEntry.stat().st_ino=0` 与 `Path.stat().st_ino!=0`导致旧P2取证错误、原观察值和游标未及时落盘。上一轮无Review候选、已归档`STOP_ACCEPTED__TASK_INCOMPLETE`，旧额度不可恢复。本任务**仅修复这两项可复用的检查手段及其限域验证**，不是继续P3/P4全流程搜真实控制器、不是执行任何旧科学测试。真实supervisor/reader源码仍UNVERIFIED。
完成标准不能凭合成/接口mock声称旧控制器已找到；新源码/测试全部在新scratch，原生产Budget、supervisor/reader、历史journal和V010不写、不执行。

## 二、冻结来源与启动门
唯一live治理分支 `migration/astra-workflow-20261012`，此任务初始baseline `5090d84c1cb4ae03b12a230b984bb312de92afeb`；先核live CURRENT/TASK_CURRENT/DOC_INDEX唯一ACTIVE，从发行后`ISSUE_MANIFEST`按固定issue_commit读取合同/参数以及旧硬停报告 `docs/CH5_TEMP_V010_CONTROLLER_SOURCE_PROVENANCE_RESOURCE_STOP_INDEPENDENT_REVIEW_20261021.md` (blob `626544b0ca0795de2c68898db418091b18814f93`)和本轮冻结四件Git file路径。只读探测路径、有限安全父目录、formal Git locator/index，必要的before-after SHA证据。原私有历史archive SHA256 `f3e8984fe4d2ef4be65692c27fa7594d96b870d372a8c45d029899f7891841d8`仅为历史身份参照；**本任务不重新读取archive，不重新扫描旧TEMP目录及其科学数据**。没有新的生产运行权限。
BOOTSTRAP0验证父目录、保护root、唯一新scratch`D:\ProjectTemp\ch5_temp_v010_controller_locator_two_blocker_recovery_20261021_01`不存在、旧Git locator/index，BOOTSTRAP1独占创建，BOOTSTRAP2首次原始证据写前核身份。禁止 symlink/reparse path 漏洞；不可信STOP，不能先创建scratch再验证环境。

## 三、A：Windows身份采集与先落盘后断言
在**新scratch任务自有正常文件/目录**中重现旧`DirEntry.st_ino`与`Path.stat.st_ino`的不同（若在本机不复现如实NO_REPRO）。在每次判断之前把两份原始API值、字段缺省、相对路径、安全目录身份、序号/游标、阶段及首错持久写入新scratch，`flush+os.fsync`成功才允许继续比较，失败即STOP，不得造补全日志。
不能机械地断言两种Windows API的st_ino必须相等，也不能“直接忽略不等然后放行”。仅对同一可信API、同一对象的安全handle/digest/稳定标识做可比判断；原始inode=0或不可读须明确`NONCOMPARABLE`并采取保护策略。独立测试恶意symlink/junction逃逸（如果安全可用）、合成文件写入期间变更、损坏/无法fsync元数据记录、不可比较的身份：这些必须fail-closed；**size+mtime一致不构成身份或字节不变证明**。对冻结已知历史根最多做2次精确根metadata-only只读stat；不得枚举历史目录子文件，不能取任何旧candidate内容。本轮的安全补丁是新scratch里可移植的采集函数与可审阅测试原件，不覆盖原工具链全局公共工具文件。

## 四、B：GitHub精确读取，不再列目录
必须彻底取消`GET /contents/tasks`及`list_directory('tasks')`、任意root recursive tree或读取响应400项后截断至64等做法。本轮不查询任何GitHub `tasks`目录树，**只请求已冻结的四个完整文件路径**（见TASK_PARAMETERS`repair_B_github_exact_objects.exact_file_fetches`），或者根据其已知40位Git Blob SHA直接取单一blob。读取前检查所选API确实用于单一文件或单一Git blob且源文件身份已知；不知道返回种类/限额就STOP。每次返回`type=file`、恰一个源对象，实际blob与固定ref/path/expected_sha一致，内容上限合计45000 bytes；不得借服务端不支持限制而无限读取元数据。每次请求的原始长度、类型、错误与成功对象完整落盘，再判断，不编造HTTP status。
四次精确读取只为证明接口已不违反64成员目录硬门，并且来源身份可以无目录枚举地认证。**不能据此宣称此前`tasks`目录已经合规检查完、旧P4已完成、生产控制器源码存在或已通过溯源。** 上一条硬门终态仍然保留为历史真实结果。

## 五、验收结果与配套证据
可达到`TWO_BLOCKER_RECOVERY_READY_FOR_OWNER_DECISION`的条件：A的取证先落盘、关键坏值不误判断、保护路径fail-closed和受控本地测试成功；B仅通过4项单文件/单blob精确取回，SHA/Blob一致，无一次超64的目录请求；全部新原件在唯一scratch。若安全接口不提供独立稳定身份，则诚实`IDENTITY_SOURCE_UNVERIFIABLE`并STOP，不以放宽路径保护换PASS。
至少交付原始Windows字段/扫描游标、可重现安全采集源与合成测试、GitHub四件精确响应类型/体积/Blob身份证据、禁止广泛tasks的实现规则、错误原件、资源/隐私/读写保护状态。公开片段需实质可审核，不能只交摘要哈希；私人原始目录全路径与旧root副作用不发布。
**不续扫**旧P2/P3/P4/P5、不找控制器、不新增源角色A/B/D结论。原GLOBAL_STOP和PRODUCTION_RUNTIME都UNVERIFIED。
资源总墙钟≤7200秒；verification900、engineering3900、delivery1800，最终180秒封存；工程Python≤16、direct≤54、E1≤3批，所有科学调用预算0，旧run额度0。异常负例不当事故，但E2/权限风险真实STOP。具体限制以冻结JSON为准。

## 六、Codex自动上传GitHub临时三件（强制）
Codex**必须自动**把逐项隐私检查的`result.md`、`manifest.json`和`evidence_sanitized.zip`上传到仓库**独立Review分支**`review/ch5-temp-controller-locator-two-blocker-recovery-20261021`、临时目录`_review_tmp/ch5/temp-controller-locator-two-blocker-recovery-20261021/`；candidate唯一parent=`5090d84c1cb4ae03b12a230b984bb312de92afeb`，仅这三件新文件。每件远端实际bytes/SHA/Git Blob和ZIP所有成员CRC/size/SHA、唯一parent与精确diff、全部隐私门须真实远端readback。只能用现有授权的Git Data API精准blob/tree/commit/ref，遇认证、策略、429禁止切换通道绕过，不force、不重建大publisher、不列root递归。
Codex不得自行清理新Review分支材料。Astra获得原字节并独立终审归档回读后才普通non-force精确删除白名单三件，PENDING保留。旧两份pending SHA `4e05976bbc8068b971ba5915133e9a6c3b73193d`和`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c`不得更改；Owner手动传ZIP不是默认交付。
如触发启动来源门、安全检测、真实资源硬门等STOP且没有合法候选，`NOT_APPLICABLE_NO_CANDIDATE`并保留全部自有原始本地首错与最终原字节回执，不能假造GitHub发布。

## 七、回执
最后记录真实run_id/actual_terminal、旧硬停身份、A/B各项PASS/FAIL及未观测/未复现区别、Windows原始元数据及先flush后校验的证据链、四份精确GitHub对象回读和保护根前后身份、资源多账与kernel descendants UNKNOWN、science calls 0。完整最终JSON原字节Base64+长度+SHA256、Git候选与三原件远端哈希（如已发布）、外部controller退出后的独立完成事件。停止点预定`WAIT_ASTRA_TWO_BLOCKER_RECOVERY_REVIEW`不替代实际终态；完成后不自动重开旧来源调查或执行HA。
