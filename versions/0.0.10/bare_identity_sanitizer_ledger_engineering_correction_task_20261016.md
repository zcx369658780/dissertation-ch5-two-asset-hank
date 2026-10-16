# V010：bare身份比较 + 结构化脱敏 + 中间台账三项集中ENGINEERING_ONLY修复

**唯一任务ID：** `V010_BARE_IDENTITY_SANITIZER_LEDGER_ENGINEERING_ONLY_CORRECTION`  
**版本与性质：** `V010 / V0.0.10`；`ENGINEERING_ONLY_LOCAL_SYNTHETIC`。2026-10-16 Owner在上一`SOURCE_ONLY`独立主审归档后明确同意执行一次集中工程修复。**这不是新模型版本，不是Python/科研数值或GitHub候选发布许可。**  
**正式发行身份：** 本文件首次发表的Git commit、tree、Blob由签发后的`TASK_CURRENT.md`登记；冻结后不得追改本文或已停任务。  
**交付ID：** `V010_BARE_IDENTITY_SANITIZER_LEDGER_ENGINEERING_CORRECTION_RESULT`。  
**终态：** `WAIT_ASTRA_V010_BARE_SANITIZER_ENGINEERING_CORRECTION_REVIEW / STOP`。

## 0. 固定上位权威与历史失败

- 仓库`zcx369658780/dissertation-ch5-two-asset-hank`；治理分支`migration/astra-workflow-20261012`，不以main替代。先读取本任务**固定发行commit下的全文与Git blob**，再只读动态`docs/DOC_INDEX_CURRENT.md`、`CURRENT.md`、`TASK_CURRENT.md`、V1.2、Owner风险/SSH/Loader决定及`docs/CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md`。
- 最新固定独立主审`versions/0.0.10/bare_common_dir_sanitization_source_only_local_only_primary_review_20261016.md`，Git Blob `9fe0549a7c02656cbf646de2a74daa47757f0205`，裁决`SOURCE_ONLY_DOCUMENTARY_LIMITED_ACCEPT_WITH_REPORTED_PROCESS_DEVIATION`。此前取证任务发行commit`5b66d6e3c0b3ad6e292009e13bbe9c19472dde1e`、任务Blob`085412aaee3df3067540c4336ff37eb4b07f9383`，已经STOP；只读Git探针4/4、读取83,707B、新文件25,100B，旧额度**不结转**。其回执SHA256由Owner转述`AD4C071D72DC08A93D5B4867DB0DF2575653EAE07D20445342058C884D8BE5DD`，Astra尚未直接读取原件/重算。
- 已知但尚未真正修复：Git stdout按`/`表示common-dir，旧PowerShell期望反斜线；前次只读输出哈希与旧现场一致，支持**路径字面比较缺陷**，不证明非共享Git对象库或抗重解析。脱敏器对连续双反斜线可能误判**JSON转义**，然而旧拒绝现场命中**文件/字段/规则/次数均UNKNOWN**；原被拒候选仍严禁发布。中间台账曾复制短源码行与原argv，后续最终文件据Codex称已匿名；该过程偏差`PROCESS_COMPLIANCE_OPEN`，不得擦除或宣称全过程已合规。
- V010科学计划`bf091da33d59293f147d52c11580327d3ac2a85d` / Blob`85138d8859d53295262fe13bf5bc277bca95ed3f`；原冻结模型代码commit`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`与输入manifest/fixture，**一律不改、不导入、不运行**。原MATLAB科学主线、真实C8与历史各预算禁令完整保留。

## 1. 本轮唯一可写位置与集中实施

新独立scratch：`D:\ProjectTemp\ch5_v010_bare_sanitize_engcorr_20261016_01`。创建前核不存在、源路径祖先/reparse/UNC/ADS/alias不落入旧D盘保护树、Git common-dir或C盘备份；失败立即`FAIL_CLOSED`。只修改本scratch中的**新PowerShell工程脚本、合成test harness、去敏meta报告与回执**；不得写原脚本、原仓、旧失败回执、任何已有clone/index/object、模型或真实数据。所有旧文件仅精确只读，不能复制旧原始日志/源码/argv至新scratch。

最多读取已知两轮旧scratch（E0修复与最近SOURCE_ONLY）的**确切最多10件小文本，实际读字节合计≤2MiB**；优先`FINAL_STOP.md`、`DELIVERY_RECEIPT.json`、`result.md`及紧邻的工程脚本/规则，不遍历陌生目录、大型日志或C8。读之前做字节预算与普通路径身份检查，异常停止。旧中间台账含原argv/短源码的部分只允许在原位置精确只读查其**匿名字段类型/字节量/来源类别**，不得回显原文、新建明文副本、覆写原件或以“修正违规”为由删除历史。

采用一次集中完成的三类修正，不新增经济模型、数值参数或求解接口：
1. **B：bare身份比较**。将`git --git-common-dir`等输出解释为可核验目录身份：限定受信任Git.exe、git-dir/cwd/env/exit/stdout边界与只读nonce，消除slash/backslash**仅表层表示差异**；仍要求经可信路径检查的`new_bare_root`与自身common-dir一致、与Stage A identity根/所有受保护Git common-dir/alternates、link/reparse路径实际分离，不把相对路径、UNC/device、ADS、dotdot、prefix欺骗、同对象共享、大小写/符号链接歧义解释为PASS。若缺少真实目录/句柄信息，标`BARE_IDENTITY_STILL_BLOCKED`，不得只做`replace("\\","/")`后宣布安全。避免静态字符串相等替代实际非共享约束；只能在**新synthetic bare根**做真实工程smoke，旧bare/Stage A只读且不在本轮重试旧任务。
2. **S：脱敏器**。只在新scratch实现**结构化、零明文输出**拒绝回执：匿名文件ID、数据类型/字段类别、规则ID、命中数量、失败阶段、是否JSON转义，且任何异常/stdout/stderr/临时ledger均不含命中原文、原argv、私有路径或真实secret。先解析JSON语义并逐字段执行敏感信息和路径核验；合法JSON字符转义不应单独证明是秘密，**但解码后真实绝对私有路径、口令/token/SSH private key、原始审计argv仍必须DENY**。对旧扫描拒绝根因继续标`UNKNOWN`，不得把合成测试成功回溯当旧候选已安全；不降低默认拒绝行为、不做全局allowlist或无条件旁路。
3. **L：中间台账安全**。从初始写入到封存全部实行typed fields/枚举值和匿名语义锚点；将错误、子进程argv、源码摘录与异常文字转为规则ID/事件ID/受界计数、允许的固定安全schema，无中途落盘再替换的raw数据窗口。原本地偏差证据**保留不删不覆盖**，在报告中列为`HISTORICAL_LEDGER_DEVIATION_UNRESOLVED`，未来只认定“**新**管线合成回归通过”而非追溯原台账干净。临时写入也必须显式UTF-8/LF、写前字节预算、无异常原文扩散。

## 2. 最小工程测试与通过标准

只用本轮scratch自建**非敏感合成fixtures**。必须覆盖以下受界用例组，逐项输出ID/预期/实际状态，任何未跑项`NOT_EVALUATED`：
- B01–B08：`/` vs `\\`字面差异的合法等价、错误共同目录、共享alternates、相似前缀、相对/UNC/reparse/ADS、错误bare flag/环境污染（适用的Windows可测门记录真实证据；无法可靠构造的拒绝并标UNKNOWN，不伪造系统权限）。
- S01–S08：无秘密的JSON转义、解码后私有绝对路径、合成凭据结构、模拟SSH密钥标记、原argv字段、无效JSON、重复键/嵌套对象和超大失败回执。真实凭据**禁止作为fixture**。只要某项不能在不泄露原文下评估，就FAIL_CLOSED/NOT_EVALUATED。
- L01–L04：正常事件仅匿名schema；异常含长模拟stdout/argv；失败写入/配额不足；历史含原文中间台账只报告存在性类别、并保证新目录不存在原始副本。任何中间生秘密片段必须如实报告过程FAIL，而不是最后换字节后宣称全程通过。

单个组别**只对真实运行的受界合成测试**给ENGINEERING_SYNTHETIC_PASS；`B`仅通过本轮合成身份测试仍不代表原发布bare真实已恢复，`S`合成PASS不代表旧候选可公开，`L`新规则PASS不追溯旧历史。关键否定例失败即`FAIL_CLOSED`，禁止放宽校验、静默删日志/忽略旧台账缺口。

## 3. 新一次性资源：与全部历史STOP账隔离

- **工程测试仅限新scratch PowerShell合成验证**：最多**2次受界PowerShell测试批次/子进程**（即便异常、退出1或中止都在启动前计费）。允许创建**1个新独占synthetic `git init --bare`**测试库，针对该新库只读`git rev-parse`身份children总≤**4**，固定Git.exe、只读env、无网络；其本机对象/配置只写新scratch的synthetic bare。严禁在旧E0裸仓、Stage A身份仓、治理/模型仓执行任何Git写入/初始化。**不允许mktree、fetch、push、commit、branch创建、checkout或网络。**
- 新Python/py/Jupyter/pytest/py_compile/AST模型执行/VerifiedLoader/真实runner/HA/HJB/KFE/selector/scalar roots/GE/IRF/MATLAB/真实C8全部**0**；不能借PowerShell测试间接调用上述对象。不做旧E0的70源码装配/真实守门器重跑/原扫描拒绝材料重扫；仅工程fixture和新脚本的合成测试。
- 墙钟≤**150分钟**。新scratch新增**最多6份平铺UTF-8/LF非Git静态/证据文件**（包括完整新PowerShell修复草案、合成测试源与case清单、短报告、manifest、最终receipt），新增非Git产物合计≤**2MiB**且在任何追加写之前预留最终/紧急回执≥**128KiB**；合成bare元数据独立≤**32MiB**。每个子命令有限时/有限stdout/stderr，不成功的前置停止依赖步骤；不能清理旧文件以重置预算。旧本机物理保护及前次GBK/argv/E0/4探针消费均原样保留。
- GitHub本轮**只有Astra创建正式冻结任务/治理文件**的权限；Codex`GITHUB_REVIEW_PUBLICATION=NOT_AUTHORIZED`，新/旧临时review分支创建与push=0。Owner历史远端`_review_tmp/ch5/<task-id>/`只准远端独立review Tree，禁止出现在任何本地科研/model/治理worktree/index。本任务只收`LOCAL_ONLY`**≤4KiB、严格脱敏**短摘要供Astra文档级审查；原始脚本/旧拒绝材料和旧raw日志不外传。将来如要GitHub review发布必须另获Owner明确授权并固定新单父/白名单及SSH443。

## 4. 交付、验收与STOP

Codex应交`V010_BARE_IDENTITY_SANITIZER_LEDGER_ENGINEERING_CORRECTION_RESULT`，列准确固定任务身份、受限新scratch与文件hash、每一B/S/L用例真实`PASS/FAIL_CLOSED/NOT_EVALUATED`、两次测试批次/合成bare及四Git child准确已耗、读取文件数/字节、非Git和bare物理工件、wall、失败回执与未知项；本机实际结果保持`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不自称Astra独立执行。若需Owner直接补证，另询问精确最小脱敏文本，**不能自行解除旧脱敏拒绝/恢复Git push**。

分账状态：
`BARE_NORMALIZED_COMPARATOR_SYNTHETIC`、
`BARE_NONSHARED_IDENTITY_GUARD`、
`SANITIZER_STRUCTURED_DIAGNOSTICS_SYNTHETIC`、
`INTERMEDIATE_LEDGER_NEW_PIPELINE`、
`ORIGINAL_SANITIZATION_DENIAL_CAUSE=UNKNOWN`、
`FULL_RUNNER_IO_CLOSURE=BLOCKED`、
`ENGINEERING_PYTHON_NOT_RUN`、
`HA_SCIENCE_NOT_RUN`。
任何一项运行未覆盖就明确`NOT_EVALUATED`。工程合成结果完成后只到`WAIT_ASTRA_V010_BARE_SANITIZER_ENGINEERING_CORRECTION_REVIEW / STOP`；**不得借剩余额度自动运行mktree、恢复真实bare发布、开始新Python/import、调用单点HA，或启动V011**。

## 5. 永久保护

原科学顺序`corrected两资产HA→多省顺序一轮→GovInv收益边界控制×0.9/1.1及Zt→冻结GDP各省误差≤1%的独立门→原lagged-NKPC递推`，目的地工资税只一次、家庭人均/省财政总量、来源/双边/firm劳动、same-S/lagged raw ra0、phi_max=.3、20×20×2/F-order/HJB/KFE既有阈值全部冻结。Owner单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`仍UNTESTED；原两省`NO_ADMISSIBLE_POLICY`及旧科学额度不清零。受保护原`D:\ProjectTemp\c5k1bturn56`8 dirty/index/staged/untracked/ignored、外Git common-dir、旧失败目录、现有C盘独立SSD备份、真实C8/2017/2018/B3与V009失败数组均不得触写或越权访问。Owner不强制VM/第三份备份、现有C盘SSD备份+GitHub、SSH Key/443与可信工作站风险接受仍适用，但不构成原生OS沙箱PASS。

**保持`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`real C8 A–D REQUEST_ONLY`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`V011 NOT_STARTED`。**
