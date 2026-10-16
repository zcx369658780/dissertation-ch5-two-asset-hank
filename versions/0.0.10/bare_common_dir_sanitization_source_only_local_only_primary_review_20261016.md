# V010：BARE_COMMON_DIR / 脱敏规则 SOURCE_ONLY 取证的独立限域审议

**日期：**2026-10-16（Asia/Shanghai）。
**任务：**`V010_BARE_COMMON_DIR_AND_SANITIZATION_SOURCE_ONLY_FORENSIC`。
**冻结发行Commit：**`5b66d6e3c0b3ad6e292009e13bbe9c19472dde1e`；任务文件`versions/0.0.10/bare_common_dir_sanitization_source_only_forensic_task_20261016.md`；Git Blob `085412aaee3df3067540c4336ff37eb4b07f9383`。
**提交状态：**`CODEX_DELIVERED__LOCAL_ONLY__NO_PUBLIC_CANDIDATE`；**上一任务关闭：**`DELIVERED__STOPPED`，**ACTIVE_TASK=NONE**。
**独立裁决：**`SOURCE_ONLY_DOCUMENTARY_LIMITED_ACCEPT_WITH_REPORTED_PROCESS_DEVIATION__NO_ENGINEERING_RUNTIME_OR_SANITIZATION_ACCEPTANCE`。
**下一许可门：**`WAIT_OWNER_FRESH_V010_BARE_IDENTITY_AND_SANITIZER_ENGINEERING_CORRECTION_AUTHORITY / STOP`。本审议不自签新任务、Python/科学进程、E0重跑、Git写入、mktree或发布权限。

## 1. GitHub现地事实和证据界限

Astra通过已连接GitHub工具按**固定发行Commit**完整读取原任务，核Blob `085412aaee3df3067540c4336ff37eb4b07f9383`确切一致。治理分支`migration/astra-workflow-20261012`在本轮主审前live HEAD `0c63cb0b53e90fd49c0785f3be672f010a6149d5`，与上一登记HEAD比较`ahead=0, behind=0, status=identical`；实时CURRENT/TASK_CURRENT仍指向本轮取证ACTIVE（现由本正式主审关闭）。GitHub分支查询`bare`没有发现对应新review分支；**本次任务本来明文禁止GitHub review发布**，因此无远端Codex候选符合本任务的发表禁令，但不足以证明本机全部中间临时文件状态。

本轮仅收到Owner转述的Codex短摘要，而非该Windows原始`result.md/evidence_manifest.json/proposed_correction.txt/DELIVERY_RECEIPT.json`四份文件的实际字节；也未直接读前次PowerShell脚本、四次Git子进程stdout/stderr、扫描器源码或中间台账。因此所有本机执行数、原byte SHA256、路径及未泄露断言属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`；Astra不能声明`INDEPENDENTLY_VERIFIED_WINDOWS_RUNTIME`或“扫描误报已证实”。

Owner提供本轮`DELIVERY_RECEIPT.json` SHA256：`AD4C071D72DC08A93D5B4867DB0DF2575653EAE07D20445342058C884D8BE5DD`，目前**未取得原字节、未独立计算或确认该哈希**。

## 2. 分门验收，不将局部证据升级为PASS

### A. BARE_COMMON_DIR身份误拒

Codex报告分类`READONLY_IDENTITY_CORROBORATED__STATIC_STRING_SEPARATOR_DEFECT`：
- 四次**获批上限内的只读Git身份探针**均exit 0；据报告，Git输出使用正斜线`/`，PowerShell脚本预期使用反斜线，直接字符串比较造成拒绝；本轮`common-dir`输出哈希与旧现场一致。
- 就有限诊断而言，“路径分隔符的表示形式不一致导致字面比较false”是有明确具体机制且得到本机只读证据支持的**合理归因**；可用于下一工程修复的草案依据。未提供两边原始身份对象或脚本具体表达式给Astra，故独立级别仍为`CODEX_REPORTED__STATIC_CAUSE_SUPPORTED`，**不是**独立亲验算法已纠正。
- exit0只证明探针结束成功，不自动证明新bare与Stage A身份根独立、绝无alternates/共用objects、完整commit/tree/blob可达，或不存在junction/reparse/同用户并发替换。特别是由字符串规范化处理跨过拒绝条件之前，必须保留真实目录/句柄身份、独占与非共享检查，不得用无条件`replace("\\","/")`或宽松大小写比较替代整个防护闭环。

**裁决：**`BARE_CAUSE_DOCUMENTARY_LIMITED_ACCEPT`；`BARE_GUARD_RUNTIME_FIX=NOT_RUN`；`GIT_OBJECT_REACHABILITY=UNVERIFIED`。

### B. 旧脱敏扫描拒绝

Codex报告分类`POTENTIAL_FALSE_POSITIVE_NEEDS_REVIEW`：
- 扫描规则会拒绝连续双反斜线，这是可能与JSON路径等字符串转义冲突的合理**静态假设**。
- 旧拒绝现场没有留下命中**文件、字段、规则及数量**；因此无法证明上次具体DENIED就是双反斜线导致，也无法判定那些原拟发布材料是否真实无秘密、绝对路径/原argv/个人数据或模型私有数据。
- 本次未获授权也没有实际重跑扫描；原拒绝结果必须继续有效。`SANITIZATION_DENIAL_ORIGINAL_CAUSE=UNKNOWN`、`ORIGINAL_CANDIDATE_PUBLICATION_DENIED=TRUE`、`FALSE_POSITIVE_CONFIRMED=FALSE`。
- 后续工程只能拟定“明确拒绝字段类别/规则ID/匿名文件键/统计和mask”的受界结构化诊断，在仅合成fixture中做正反例验证；不能取消通用转义匹配或重新提交旧被拒原件来取得表面PASS。

**裁决：**`SANITIZER_CAUSE_HYPOTHESIS_ONLY`；`SANITIZER_RUNTIME_PASS=FALSE/NOT_RUN`。

### C. 中间台账过程偏差

Codex主动报告：中间台账**曾复制短源码行及原argv**，最终四份文件后来改用语义锚点及匿名参数，偏差仍被保留。冻结任务明确禁止将原始源码、敏感argv或日志复制到新报告/新scratch工件；故这里必须单独标记：
`INTERMEDIATE_LEDGER_CONTENT_HANDLING_DEVIATION=REPORTED__UNRESOLVED_INDEPENDENTLY`。

这不等于已证实向外网泄露秘密，因为本任务GitHub发布及网络为0且缺外传证据；同样**不能**凭最终文本声称先前原文字节已从所有中间/备份/文件历史消失，或宣布全流程完全合规。不得删除/重写旧中间记录以“消除违规”，也不得将它们加入公开Git。下一轮应在Owner认可的精确只读范围内核定中间台账的所在类别、原文是否仅低敏源语义、已采取的脱敏与保留方法；如遇疑似凭据，单独上报而不外传原字节。

**裁决：**`PROCESS_COMPLIANCE=NOT_FULLY_ACCEPTED`，属于限域审议的保留条件和下一工程设计必须关闭的证据卫生缺口。

## 3. 资源与未运行对象

Codex本轮自报：
- read-only Git身份探针：**4/4**，额度上限已到，下一任务不得续用；
- 旧文件实际读取：**83,707B**，低于冻结`2MiB`总字节上限；**具体文件数UNKNOWN**（任务最多8）；
- 新四个文件合计：**25,100B**，低于冻结`512KiB`增量上限；预留`64KiB`的实际写前账、wall≤90分钟、确切来源hash链及路径隔离仍**未独立核证**；
- `E0_RETEST=0`，`MKTREE=0`，`GIT_FETCH/PUSH/COMMIT/PUBLICATION=0`，`PYTHON/REAL_RUNNER=0`，`MODEL_IMPORT=0`，`HA/HJB/KFE/selector/root/GE/IRF/REAL_C8=0`；
- 从本任务产生的未用上限随`STOP`关闭，不能自动下轮结转；以前所有V010实验/工程、两次单点Python各1/1（HA均0）及最初GBK写日志超9,965,206B的历史实物、账本和封闭性均不变。

## 4. 科学冻结与下一决策

此次唯一可接受的是**受限源码/只读诊断方向**：已缩小bare守门可能的字符串缺陷，提出脱敏可能误报的候选原因，并如实披露过程偏差。它**没有**实现或验收未来工程脚本修复、真实Windows runner、`VerifiedLoader`、`mktree`、GitHub审阅发布、完整Python I/O闭环及HA科学。

旧科学权威：V010冻结科学plan commit `bf091da33d59293f147d52c11580327d3ac2a85d` / blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；原模型候选commit `94de4501dec051b969bee9d852eba2d4591f30ef`/tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`不改。修正MATLAB的corrected两资产HA→多省顺序单轮→GovInv收益边界乘0.9/1.1与Zt→冻结GDP目标≤1%→lagged-NKPC递推主线、目的地工资税一次、same-S/lagged raw ra0、人口/家庭与firm劳动分账、phi_max=.3、HJB/KFE网格/阈值均冻结。旧双省synthetic F-order25`NO_ADMISSIBLE_POLICY`和Owner新单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`corrected HA仍`UNTESTED`，没有GE/正式IRF/论文Results资格。

Owner双备份（独立C SSD现有备份＋GitHub）、SSH Key/443、可信工作站双根VerifiedLoader、不强制VM或额外第三备份的正式风险取舍仍有效；不可把这等同OS-native安全沙箱。远端`_review_tmp/ch5/<task-id>/`仅允许远端review分支Git tree，不进原本地worktree/index，未经脱敏不得外传。

继续保护原`D:\ProjectTemp\c5k1bturn56`原8 dirty tracked/index/staged/untracked/ignored/外Git common-dir、C盘备份、所有旧失败原件、真实C8/2017/2018/B3以及V009失败数组。持续保持`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`real C8 A–D REQUEST_ONLY`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`V011 NOT_STARTED`。

建议未来在Owner**新授权**后，用一个独立`ENGINEERING_ONLY`的小任务集中修复标准化身份比较（同时保留真实目录/非共享身份和负例防护）、为脱敏拒绝追加结构化不含原文的diagnostics和合成JSON转义/真秘密用例，并披露中间台账源字段处理。**新脚本运行、Python、bare mktree、Git push及HA科学许可均不由本审议自动开放**。