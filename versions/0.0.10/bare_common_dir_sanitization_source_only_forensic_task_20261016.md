# V010 BARE_COMMON_DIR 身份与脱敏拒绝原因：单轮最小化 SOURCE_ONLY 取证

**唯一任务 ID：** `V010_BARE_COMMON_DIR_AND_SANITIZATION_SOURCE_ONLY_FORENSIC`  
**项目：** 知识库博士论文第五章-GPT顾问；`V010/V0.0.10`（不启动 V011）  
**任务性质：** `READ_ONLY_FORENSIC + SOURCE_ONLY_DRAFT`；只诊断前次本机证据，**不运行修复、不补推旧任务、不开展科学运算**。  
**Owner 新授权：** 2026-10-16，Owner在最新 E0 失败主审归档后明确同意继续，授权仅此紧凑取证范围。工程/科学执行、Git发布和旧失败额度仍须逐任务另行批准。  
**冻结身份：** 本文首次发布的完整 Git commit、Blob、parent 由发布后的动态 `TASK_CURRENT.md` 登记；不预填未来对象 SHA，也不可追改此文件。  
**预计终点：** `WAIT_ASTRA_V010_BARE_SANITIZATION_SOURCE_ONLY_REVIEW / STOP`。

## 0. 先核权威，不能误续上次 STOP 任务

- 仓库 `zcx369658780/dissertation-ch5-two-asset-hank`；治理分支 `migration/astra-workflow-20261012`（不是默认 main）。先按本任务**固定发行 commit**读取全文并核 Blob，再只读核现行 `docs/DOC_INDEX_CURRENT.md`、`CURRENT.md`、`TASK_CURRENT.md`、V1.2、Owner备份/SSH/Loader决定与 `docs/CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md`。
- 前一STOP任务 `V010_E0_LAUNCHER_UINT32_AND_TEMP_MKTREE_CORRECTION`，发行commit `e474c0d25a7351b7510f6a9ba914cd8733dceffc`，task Blob `a3683c751acf08d49d700422a63f264b61130e78`。最新[独立限域主审](e0_launcher_mktree_fail_closed_local_only_primary_review_20261016.md) Blob `3f675de31449ce946a2ecb3b51ed6c9a55850197`，旧本机最终回执由Owner转述SHA256 `AC06ECCFAA023AC4593017CC18C4AD4FAC644BC52C00FA2F71B5FD82C54C4816`（Astra未亲验）。
- 前任务 Codex 回报 UInt32 修正后24类型例匹配、E0 PowerShell 1次受界成功；但新bare的 `BARE_COMMON_DIR` 实际比对失败，封存脱敏扫描拒绝候选；旧任务 `mktree/fetch/push/Python/runner/HA` 全部0，审议时GitHub新review ref不存在。本任务**不是重做24例或E0，也不是对旧mktree错误的复验**。
- 冻结V010 plan commit `bf091da33d59293f147d52c11580327d3ac2a85d`/blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；模型commit `94de4501dec051b969bee9d852eba2d4591f30ef`/tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；不能更改、checkout、import或执行。历史两次单点probe耗尽、首次GBK超限、原实施科学账及全部旧Windows E0历史原样保留；所有旧剩余额不自动结转。

## 1. 新隔离只读取证位置与允许读取的原证

新建**唯一项目外独立scratch**：`D:\ProjectTemp\ch5_v010_bare_sanitize_forensic_20261016_01`；先只读确认不存在、不是 junction/symlink/reparse/共享Git对象的别名、也不处于保护根。新建仅此scratch和其平铺输出（见第4节）；严禁在旧项目worktree、既有Git index、C盘备份或旧证据目录中写入。

本任务允许从**上一失败scratch** `D:\ProjectTemp\ch5_v010_e0_launcher_mktree_20261016_01` 精确只读最多 **8 份小文件、全部实际读取总计≤2MiB**：
- `FINAL_STOP.md`、`DELIVERY_RECEIPT.json` 两份优先，按原件确认文件大小、UTF-8/JSON结构、SHA256与Owner给出的回执值；若与预期不符记录 `RECEIPT_IDENTITY_MISMATCH / STOP`。
- 若回执明确给出准确文件路径，再各读取至多2份与bare身份校验直接相关的PowerShell脚本/小型回执、至多2份与脱敏扫描直接相关的扫描规则/命中元数据/待发布文件的**最小必要局部**；其余最多2份同一失败任务所需的局部静态文件，不遍历全旧scratch，也不读取未知内容的大日志。文件过大、异常权限、外链、超额或涉及真实研究数据即STOP。
- 原始被拒的脱敏候选文本/日志中的**敏感字段不得复制、打印到console或新报告**。如确需查看命中周边，只在读取字节内存范围中定位，输出仅规则ID、匿名字段序号、类别、长度、计数与拒绝阶段；不输出原文、用户信息、可反推秘密的短哈希。只对**文件整体**计算并记SHA256和原字节大小（必要时在本地回执保留），不将原始文件提交GitHub。
- 原 `D:\ProjectTemp\c5k1bturn56` 的8 dirty tracked、staged/index、untracked/ignored、外Git common-dir、全部历史失败根，C盘备份、真实C8/2017/2018/B3及V009坏数组绝不写/清理/reset/stash；除上述精确旧scratch白名单外不扫描它们。不得请求安装软件、改变Windows/全局或系统Git配置。

## 2. 问题A：BARE_COMMON_DIR守门失败的证据链

从**失败现场的既有回执/代码**分别提取并明确来源：
- 守门器比较的实际 `expected` 和 `observed` 分别来自何处（静态预期、过程输出、环境、cwd、Git参数、路径对象或回执），失败的检查分支/比较表达式与原始退出阶段；未记录则标`UNRECORDED`，**不得逆向想象实际上执行了什么子命令或stdout**。
- 是否存在 bare `--git-dir` 与`--git-common-dir`、`-C` /cwd、工作树/common-dir、`GIT_DIR/GIT_COMMON_DIR/GIT_WORK_TREE`环境变量、相对/绝对/大小写/尾部分隔符、junction/reparse/UNC/8.3路径及目录身份混同。仅列**适用的实证项**；不把Windows普通字符串相等或PowerShell`Resolve-Path`当充分防同用户恶意TOCTOU证明。
- **重要区分：**发布使用的新独占bare对象库与原Stage A只读 `git_identity_root`设计上应为两个不同根；守门目的是证明新bare未共享旧对象/common-dir，而非强行要求两者相同。若源脚本实际比较方向相反，作为静态假设标明，不擅自修改守门器。
- 在原回执缺少实际bare身份输出，且已经精确认证旧独占bare所在路径属于**上一任务scratch内部**、未指向原受保护仓库/外部common-dir/未知reparse时，**本任务仅新增至多4次只读Git身份探针**，例如 `git --no-optional-locks --git-dir=<VERIFIED_OLD_BARE> rev-parse --is-bare-repository`、`--absolute-git-dir`、`--git-common-dir`、`--is-shallow-repository`。必须固定受信任Git.exe、shell=false、准确argv/cwd、禁隐式网络和可写命令，每次保留exit与有界stdout/stderr的脱敏摘要。Git身份探针只读**既有**bare且不得改动其objects/config/index；**不是旧任务的mktree补试**。一旦路径真实性无法确定，Git探针=0，留下UNKNOWN；不得为了取PASS创造新bare根或复用原模型.git。
- 将`FAIL_CLOSED_CONFIRMED`、`STATIC_GUARD_DEFECT_POSSIBLE`、`READONLY_IDENTITY_CORROBORATED`与`UNRESOLVED`清楚区分。即使找到明显字符串/规范化差异，也只能提交**未执行**修复草案，不能重新运行E0/守门/发布工作流。

## 3. 问题B：脱敏拒绝的具体规则与最小安全候选

- 查原扫描策略/上次封存拒绝回执，明确扫描发生在何阶段、命中目标是报告/manifest/草案的哪类字段、规则ID/校验类型/命中数量/错误代码、是否由误将占位符/任务标识/字面Windows路径等视作秘密引起。所有结论必须有已读取的源码/回执锚点，未记录明写UNKNOWN。
- 将命中区分为 `REAL_REDACTION_REQUIRED`（明确不宜公开）、`POTENTIAL_FALSE_POSITIVE_NEEDS_REVIEW`（只提出证据）、`UNKNOWN`；**不擅自放松正则、全局绕过脱敏扫描、替换敏感原文为看似无害字符串后直接推送**。
- 静态提出真正最小可交付`result.md + manifest.json`字段集合：只含任务身份、布尔门、规则ID/匿名字段、归因等级、资源账和原件整体hash；能不含路径就不含路径，保留数据层级与审计后可恢复性。对原被拒材料，不证明安全前一律维持`PUBLICATION_DENIED`。
- 不执行原脱敏器或git发布器，不重新封存被拒候选；所有重新筛查/模拟规则的实际执行仍需要后续单独工程权限。输出一份`PROPOSED_SANITIZED_MINIMUM_NOT_PUBLISHED`的文字/JSON字段蓝图，不把它称为扫描PASS。

## 4. 新资源硬限、输出及停止点

- **0次**新Python/py/pytest/py_compile/AST模型执行/model import/VerifiedLoader/真实runner、0次HA/HJB/KFE/selector/scalar-root/GE/IRF/MATLAB/真实C8、0次mktree/fetch/push/clone/checkout/commit/branch创建、0次新E0保护试验、0次实际脱敏扫描重跑、0次模型源修改。PowerShell仅限只读文件/路径/哈希与文字编辑，若需要最多4次前述只读Git身份探针；禁止后台循环、额外安装或网络。GitHub不授Codex新写权限。
- **墙钟≤90分钟**；上一scratch读取≤8文件且累计≤2MiB；新scratch最多4份UTF-8/LF平铺小文件，总新增物理工件**≤512KiB**（包含最终回执/保底预留≥64KiB）。无复制原始日志/源码到新scratch，硬界超额FAIL_CLOSED；每次实际Git探针和大文件读取前写本轮资源账并保留失败，不补领前任务额度。
- 必须保留真实旧证据并**不更改其原字节**。新增本轮`result.md`（精确事实/假说/仍UNKNOWN，≤20KiB）、`evidence_manifest.json`（文件身份/哈希与匿名证据、预算、时间、各门真值，≤80KiB）、`proposed_correction.txt`（非可执行静态伪代码/比较及脱敏最小方案，≤40KiB）、`DELIVERY_RECEIPT.json`（≤16KiB，引用所有新文件hash和明确STOP）。上限计入所有临时/失败输出，不留超额Exception。
- 因**bare身份/原脱敏封存仍阻断审阅发布**，本轮专门规定 `GITHUB_REVIEW_PUBLICATION=NOT_AUTHORIZED`，不创建新review分支、不对旧分支补推、不将拒绝的原件上传。Codex最终回复只提供**不超过约4KiB的脱敏短摘要**（每一问题：可证事实/证据锚点/UNKNOWN/推荐下一工程门），无需Owner复制原件；若无法安全脱敏，则只输出`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`及规则ID等不敏感字段。Astra验收时本机证据仍属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，除非后续得到原始字节。
- **交付 ID：** `V010_BARE_COMMON_DIR_SANITIZATION_SOURCE_ONLY_FORENSIC_RESULT`。必须标`BARE_COMMON_DIR_CAUSE_CLASS`、`SANITIZATION_DENIAL_CLASS`、`READONLY_PROBES_USED`、`MKTREE_NOT_RUN`、`PUBLICATION_NOT_AUTHORIZED`、`ENGINEERING_PYTHON_NOT_RUN`、`HA_SCIENCE_NOT_RUN`与剩余UNKNOWN。完成或遇守门失败统一`WAIT_ASTRA_V010_BARE_SANITIZATION_SOURCE_ONLY_REVIEW / STOP`，不自授工程修复或数值许可。

## 5. 永续科学/Owner保护

原MATLAB修正主线`corrected两资产条件HA→多省顺序单轮→GovInv收益边界×0.9/1.1及Zt有界调整→冻结GDP≤1%独立验证→原lagged-NKPC递推`未改变。家庭人均/省财政总量、目的地税只征一次、origin/双边/firm劳动分账、`same-S`、前一完整轮raw `ra0`、`max_phi=0.3`及HJB/KFE原网格/容差/阈值继续冻结；原双省synthetic`NO_ADMISSIBLE_POLICY`与单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`未执行HA的事实不变。V008/V009人工Newton/CES等不恢复。Owner C盘独立SSD既有备份+GitHub两重足够、Codex使用已有SSH Key/443、未认证OS native沙箱不宣称通过；原保护树/全部历史失败原证不触写。

**保持：**`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`real C8 A–D REQUEST_ONLY`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`V011 NOT_STARTED`。任务发出不等于修复验收、测试PASS、运行许可或科学结果。
