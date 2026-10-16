# V010：修复链工程集成、首次/终版封存证明与合成 mktree 发布器门

**唯一任务 ID：** `V010_ENGINEERING_INTEGRATION_SEAL_CHAIN_SYNTHETIC_MKTREE_PREFLIGHT`  
**版本：** V0.0.10（V010）；**权限性质：** `ENGINEERING_ONLY_LOCAL_INTEGRATION_AND_EVIDENCE`；非科研数值版次。  
**Owner新授权：** 2026-10-16，上一三组件合成20/20的独立限域归档后，明确同意继续“受界工程集成与证据链验证”；本任务是一次**全新冻结**工程预算，不是旧任务残余额的继续。只允许明确列出的本地PowerShell/Git合成集成与证据核查；**不批准GitHub push、真实 Python import/runner、HA或V011**。  
**正式发行身份：** 签发后的 `TASK_CURRENT.md` 记载固定任务 commit/blob；不得修改本已发行文件。  
**交付 ID：** `V010_ENGINEERING_INTEGRATION_SEAL_CHAIN_SYNTHETIC_MKTREE_RESULT`。  
**结束：** `WAIT_ASTRA_V010_ENGINEERING_INTEGRATION_SEAL_MKTREE_REVIEW / STOP`。

## 0. Authority、上一轮结论和科学冻结

1. GitHub仓库 `zcx369658780/dissertation-ch5-two-asset-hank`，动态治理分支 `migration/astra-workflow-20261012`（不是main）。从**本任务发行固定Git commit**完整读取任务并核blob，然后读取 `docs/DOC_INDEX_CURRENT.md`、`CURRENT.md`、`TASK_CURRENT.md`、`docs/CH5_VERSION_REGISTER_CURRENT.md`、`docs/CH5_ASTRA_WORKFLOW_CURRENT.md`、Owner风险/备份/SSH/Loader决定、仅远端脱敏审阅协议。
2. 前一工程任务 `V010_BARE_IDENTITY_SANITIZER_LEDGER_ENGINEERING_ONLY_CORRECTION` 发行commit `2a252ec2627d9a1f48dcab0c1bab16cc6cf9d9fe`、Blob `6c31d861a9e15f1b5956dfdfa7132a074bdb2e5e`，已STOP。正式主审 `versions/0.0.10/bare_identity_sanitizer_ledger_engineering_local_only_primary_review_20261016.md` Git Blob `cbafd84d7e3149692938d0e601a1413142076714`：Codex报bare B01–08、脱敏S01–08、ledger L01–04总20/20合成预期匹配，**仅CODEX_REPORTED**。最早first seal summary存在null，原receipt据报保存，补正资源汇总但未重新测试；两版原字节/run-id/test-case关联`UNVERIFIED`。上轮最终回执Owner提供SHA256 `70622F5AF09089983639F81973837D7EF7D5E0CAA6B33E85D0C74B5B7EA74D23`，网页Astra未实际取本机字节复算。
3. 前次使用测试批次1/2、合成bare init1/1、只读Git4/4、旧文件2份16,826B、新6份58,657B、bare文件报告130B（**不能代表整个bare仓物理元数据**）；上轮全部剩额随STOP关闭，**不可结转**。更早E0 UInt32/源码装配未闭环、原真实bare身份/脱敏拒绝/empty-line mktree仍无真实验收。原被拒review材料公开`DENIED`、原扫描命中细节`UNKNOWN`、历史台账raw argv/短源码偏差`UNRESOLVED`。本轮必须保留所有首次失败、资源超额和receipt原件。
4. V010冻结科学plan commit `bf091da33d59293f147d52c11580327d3ac2a85d` / Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；冻结模型commit `94de4501dec051b969bee9d852eba2d4591f30ef` / Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，不可追改/导入/执行。Owner新单点 corrected HA `rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07` 仍UNTESTED，`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`Results FALSE`、`V011 NOT_STARTED`。

## 1. 全新工程scratch、精确只读来源和不变保护

唯一新项目外scratch：`D:\ProjectTemp\ch5_v010_integration_seal_mktree_20261016_01`。先查路径及祖先，必须新建前不存在、不能经reparse/UNC/ADS/硬链接/相似前缀指向原项目旧scratch、受保护旧Git common-dir、C盘备份、真实数据或任何已有worktree；若真实性不明就`FAIL_CLOSED`。仅此新scratch可写：新的PowerShell集成驱动、合成fixture、无原文字段的结构化报告/ledger、最终回执、一个全新**独占bare Git合成仓**。不允许把`_review_tmp/ch5/<task-id>/`放在本地模型/科研/治理项目worktree/index（本轮甚至不需构造远端同名目录），不触碰任何已有Git对象仓的config、index、objects、alternates、refs、工作树。

**只读精确白名单：**最近工程修复scratch `D:\ProjectTemp\ch5_v010_bare_sanitize_engcorr_20261016_01` 的本轮前次最终 `DELIVERY_RECEIPT.json`、证据清单、原first seal、修正final seal、脚本/测试case索引（**文件实际路径必须由前次最终回执/manifest精确指向，不扫描未知目录**），最多**10件**，实际累计读取**≤1MiB**。验证最终receipt**实际原字节**SHA256是否等于Owner转述 `70622F5AF09089983639F81973837D7EF7D5E0CAA6B33E85D0C74B5B7EA74D23`；如不符`RECEIPT_HASH_MISMATCH / FAIL_CLOSED`。如果某份原first seal不存在、路径无证据或因上轮六文件限额仅曾“口头保留”，明确`FIRST_SEAL_MISSING_OR_UNVERIFIABLE`，不得伪造它或填充新run-id。

这些旧文件与所有以前失败scratch必须**仅只读**，禁止覆写/重命名/修补/清理历史空值或中间台账raw内容，不能把旧原始argv/源码/日志复制到新scratch。对于可能包含敏感字段的旧证据只输出匿名字段/总字节/整体hash，绝不回显命中值、绝对私有路径、credential原文。保护原 `D:\ProjectTemp\c5k1bturn56` 8 dirty tracked、index/staged/untracked/ignored与外部Git common-dir、C盘独立SSD既有备份、真实C8/2017/2018/B3、V009错误数组；不能reset/stash/checkout/git add/清旧工作树。

## 2. 两条独立验收线：证据链 + 本地工程集成

### GATE S：先证明上轮 first/final 封存链、不是生成漂亮新报告

- 按读到的**真实原文件**核first receipt与corrected receipt的文件身份、各自SHA256/字节数、相应`run_id`、`case_manifest`/20项B/S/L结果的hash锚点、开始/终止计数、首版具体null字段，以及后版变更范围。要求`same_run_id`、`same_test_result_hashes`、`first_hash_is_preserved`；允许补正的字段**仅**资源汇总和明确审计增补指针，绝不能改test result/pass数或事后再运行。对无法从现存原件证明的字段记`UNRECORDED/UNKNOWN`，不得新造“首版”或代替真实hash。
- 如果first receipt是final里嵌套的历史快照或其hash被后版引用，必须先证明**可独立还原的原字节对象确实存在且对应hash**；只有文本/宣称没有实体，`SEAL_CHAIN=INCOMPLETE`。不要求为补证再运行上轮20项；**本轮禁止重跑上轮B/S/L原测试以追溯补证**。
- 对原上轮存在的null字段，区分`FIRST_SEAL_NULL_CONFIRMED`与`FIRST_SEAL_NULL_CODEX_REPORTED_ONLY`，并记录修改后的资源账是否完整；只接受`SEAL_CHAIN_CORROBORATED_WITH_RAW_BYTE_PROVENANCE`或`SEAL_CHAIN_UNVERIFIABLE`，均不代表Astra网页已独立读到D盘。
- 新本轮输出采用`run_id`、单向SHA256链接、结构化匿名事件；每次写入从首字节无秘密、UTF-8/LF、写前预算。有缺失就留存当前新失败receipt然后在本门STOP；B线若独立不依赖该缺口可继续**仅在总预算内**做合成门，但整体结果不得标`FULL_PASS`。

### GATE I：在全新bare与**新工程修复方案**上执行小型集成（不接旧真实发布链）

- 从前一冻结任务**只读现存新修复脚本与case结果，核来源hash**，仅在新scratch中复制`经静态审查的纯工程脚本段`（禁止带旧raw日志、argv及模型源码），实现统一的`GitIdentityGuard → StructuredSanitizer → SafeLedger → TreeInputSerializer`本地合成流水线。不可写/调用前次scratch或旧发布bare执行器。若前次实际修复脚本找不到或来源/哈希不明，报`FIXED_ENGINEERING_SCRIPT_SOURCE_UNVERIFIED`，不能临时杜撰一版逻辑并声称集成前次结果。
- 新独占bare物理建立后检`core.bare`、`--absolute-git-dir`、`--git-common-dir`、祖先路径/reparse、无alternates/共享对象、git-dir/cwd/env与引用对象；一组正常条件及至少三组明确否定条件（如错误common-dir、模拟共享alternates、junction/路径混淆）必须**按固定修复后守门器**实际拒绝。不能把路径string norm PASS替代OS级同用户恶意TOCTOU抵御。对本地可信工作站风险的结论最多`TRUSTED_WORKSTATION_ENGINEERING_INTEGRATION_WITH_LIMITS`。
- 仅用**安全合成字符串**测试 sanitizer 与 ledger 在一次流水线首写/诊断/拒绝中的联动：合法JSON转义保持可读，**解码后**模拟私有路径与凭据/原argv标志必须DENY且回执只保留匿名规则ID/类别/计数。不得把旧拒绝材料作为fixture/重新扫码，旧`ORIGINAL_SANITIZATION_DENIAL_CAUSE=UNKNOWN`持续。
- 额外纳入上一旧Git发布器`mktree`空行问题的**全新bare纯合成门**：仅用本任务自己生成的非模型两段文字分别`git hash-object -w`，发正例tree input和负例额外空行，对`git mktree`最多两个进程分别核`exit code`、tree object id/预期精确entry数量、最后一个LF与额外空记录，须留意Git不同版本对输入的实际语义，不能假定任何特定错误码或把某一Git允许尾空行视为自身过滤器安全PASS。正式修复后输入serializer须在调用前明确拒绝额外空行/重复路径/非法mode/type/不合法UTF-8，且单独证明正例tree内容吻合；如Git负例退出0，仅据工具行为记录，但我们自己的预校验仍必须`DENY`。**不构造Git commit/ref，不联网，不访问任何旧Git发布仓**。

### GATE D：交付物及分账语义

列 `SOURCE_SCRIPT_AUTHENTICATED`、`FIRST_SEAL_RAW_EXISTS`、`FIRST_FINAL_SAME_RUN_ID`、`CASE_MANIFEST_UNCHANGED`、`SEAL_CHAIN_PROVEN`、`BARE_NONSHARED_GUARD_INTEGRATION`、`SANITIZER_LEDGER_PIPELINE_INTEGRATION`、`MKTREE_SERIALIZER_SYNTHETIC`、`GITHUB_REVIEW_PUBLISH=NOT_AUTHORIZED`、`PYTHON_MODEL_IMPORT=NOT_AUTHORIZED`、`HA_SCIENCE=NOT_AUTHORIZED`，每一项用`PASS / FAIL_CLOSED / UNKNOWN / NOT_RUN`分开标注，写清证据来源是`LOCAL_RAW_HASHED`、`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`或`GITHUB_INDEPENDENTLY_VERIFIED`，不得跨级别。

## 3. 独立新资源与绝对STOP

- **PowerShell本地集成测试批次≤2个**，每批启动前记录实际账；成功/失败均消耗，严禁通过换进程名/嵌套PS重置。允许**1个新独占`git init --bare`**合成库，仅本轮新scratch。针对该库 `git rev-parse`只读Git身份子进程**≤6**；为了纯合成tree，`git hash-object -w`**≤2**（仅新库两份非模型安全bytes），`git mktree` **≤2**（正/负各≤1），`git ls-tree` **≤1**。额外read-only Git metadata命令总计**≤20**（含上述rev-parse/ls-tree，不含已计费的mktree/hash-object）；一律固定可信Git.exe、受界argv、无网络/隐式fetch、timeout/exit/reap/STDOUT/STDERR上限，stdout/stderr入匿名typed ledger。**禁止任何旧bare/原Stage A读写探针、本轮模型Git clone/fetch/checkout/commit/ref创建/GitHub SSH或push**。
- **Python进程0，py/pytest/py_compile/AST模型执行0，model import0，VerifiedLoader0，真实runner0，HA/HJB/KFE/selector/scalar roots/GE/IRF/MATLAB/真实C8全部0。** 不重跑前任务20项来伪证其封存。
- 总wall≤**150分钟**；从前一scratch精确只读文件**≤10份、总≤1MiB**；新scratch非Git**≤8个平铺文件且物理新增合计≤2MiB**（含脚本、合成fixture、test result、first/final本轮匿名receipt、manifest及失败应急记录），必须预留**≥128KiB**给最后封存；仅新bare Git元数据物理新增**≤32MiB**，独立全目录汇总包含隐藏/空配置/refs，而不是只报130B。每项写前有预算账、异常也保留不覆写失败first receipt。源/终原字节SHA独立实算并在结果注明作用域与可验证等级。
- 脱敏与GitHub：本次 Codex **不获GitHub candidate发布权**，不得创建任何新的`review/`分支或远端`_review_tmp/`、不得fetch/push、不能凭新sanitizer合成PASS解除旧`PUBLICATION_DENIED`。最终只在对话给**≤4KiB安全脱敏摘要**和本机receipt SHA，供Astra做文档级主审；如真需独立远端审阅，则另提Owner授权新parent/ref/file白名单/ssh443预算。禁止原argv、敏感日志/源码和绝对私有路径进入对话/GitHub。
- 硬门：身份源或hash不可信、读文件超上限、first/final数据不符、mktree正例对象意外、serializer接受多余空行、脱敏模拟凭据未DENY、任何超限/依赖失败即`FAIL_CLOSED`并停止受影响链；允许在不违反权限的情况下记录其他独立门的状态，但不可跨依赖强行执行。本轮任务结束时**所有未使用预算一律关闭、不跨任务继承**。

## 4. 永续科学与Owner保护

Owner明确不强制新VM/第三备份，C盘独立SSD既有备份+GitHub双层备份，Codex今后若另获远端发布许可用现有SSH Key/ssh.github.com:443（本轮**不连接**），可信工作站工程风险接受不等于原生OS沙箱认证。上一V010重大失败与Windows E0/GBK/原8dirty/窗口/A16/C9/CALL_LEDGER保留。本轮结果不能声称`FULL_RUNNER_IO_CLOSURE_PASS`、`CANONICAL_MODEL_IMPORT_AUTHENTICATED`、`HANK_HA_PASS`或`RESULTS_PASS`。原corrected HJB/KFE、GovInv收益边界控制×0.9/×1.1与Zt、目的地工资税一次、家庭人均/省财政总量及三劳动账、same-S/前完整轮lagged raw ra0、phi_max=.3、20×20×2、GDP冻结各省误差≤1%独立校验、lagged-NKPC原递推均未改。**A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY；model_activation=False；Results FALSE；V011 NOT_STARTED。**

**结果总分类：** 成功只能到`ENGINEERING_LOCAL_INTEGRATION_SUPPORTED_WITH_SEAL_CHAIN_EVIDENCE`（Codex本地），Astra未读取本机原字节不独立授工程PASS。结束`WAIT_ASTRA_V010_ENGINEERING_INTEGRATION_SEAL_MKTREE_REVIEW / STOP`，不得自行启动下一任务。
