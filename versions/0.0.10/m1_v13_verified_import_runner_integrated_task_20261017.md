# V010 M1：V1.3 可信源码装配、真实 Python import-only 与 Windows runner 工程预检

**任务ID：V010_M1_V13_VERIFIED_IMPORT_RUNNER_INTEGRATED_PREFLIGHT**
**版次：V010/V0.0.10；性质：ENGINEERING_ONLY__NO_SCIENTIFIC_SOLVE**
**Owner授权：**2026-10-17，Owner明确要求回到博士论文第五章改写并继续下达任务；采用已批准的V1.3工程快速通道，**新授**本任务内受界工程Python、import-only/runner I/O预检及一次条件式脱敏GitHub审阅交换。旧停止任务未用额度不结转。
**结果ID：V010_M1_V13_VERIFIED_IMPORT_RUNNER_INTEGRATED_RESULT**
**固定任务发行Commit/Git Blob：**由本文件首次发行后 TASK_CURRENT 登记，发行后本正文冻结不追改。
**终点：WAIT_ASTRA_V010_M1_V13_ENGINEERING_REVIEW / STOP**。Codex不得自授工程完全PASS、FULL_RUNNER_IO_CLOSURE或科学预算。

## 0. 权威、目标与不可跨越的科学边界

仓库：zcx369658780/dissertation-ch5-two-asset-hank；**治理分支** migration/astra-workflow-20261012（不是main）。先按 TASK_CURRENT 登记的**固定发行Commit**读取本文件全文并核其Git Blob，再核 CURRENT、DOC_INDEX、V1.3 docs/CH5_ASTRA_WORKFLOW_V1_3_20261017.md、Owner备份/SSH/Loader docs/CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md、remote-only协议和既有V010工程冻结输入；相冲突STOP。

本轮M1交付目标：**用真实冻结Git模型源码**完成Windows下受界Python包导入、VerifiedLoader身份、至少一次真实runner I/O导入工程smoke，以及可复核的独立审阅摘要；不是又做一轮纯静态/仅timestamp的专项，也不是承诺稳态或31省GE。旧timestamp String/Z→PowerShell7.6.6 DateTime/Utc有本地24/25+1 SPEC_UNRESOLVED报告，**不影响模型代码冻结、不作为本轮真实import的必须前提**；不重跑25/17/20历史测试、不补造旧缺的first/raw/run_id或执行脚本hash。

V010**科学计划**固定Commit bf091da33d59293f147d52c11580327d3ac2a85d、Blob 85138d8859d53295262fe13bf5bc277bca95ed3f；**模型代码候选**Commit 94de4501dec051b969bee9d852eba2d4591f30ef、Tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5、sole parent a1db8c114dec0ab69d69a5576e153a7f868cba0e。必须保持70份src/ch5_two_asset_hank原始Python源码与三份非空__init__.py真字节不变；不补写或改写冻结数学代码。原两资产HA/HJB/KFE、selector/scalar roots、双省/31省GE、GovInv/Zt稳态、冲击/IRF、原HA单点(rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07)、真实C8及所有真实数据**调用0**；model_activation=False、Results FALSE、V011 NOT_STARTED。

## 1. E0：写前只读Bootstrap、身份验证与源码装配

**唯一新可写工程scratch：**D:\ProjectTemp\ch5_v010_m1_v13_import_runner_20261017_01。该根必须之前不存在；已失败旧scratch绝不可重置后伪称新根。**BOOTSTRAP0**只用可信现有PowerShell/OS控制台内存指令，先只读核精确父路径/目标不存在、protected roots不重叠、reparse/junction/UNC/ADS/alias/device与符号链接风险；不能先写preflight脚本、日志、目录或错误receipt。父路径/对象实际身份不可证明即直接在终端匿名FAIL_CLOSED/STOP，本次不在不可信目录写任何字节。

仅当BOOTSTRAP0 PASS，**BOOTSTRAP1**创建唯一工程scratch，马上核对新根身份/父目录与preflight同一性；**BOOTSTRAP2**然后才允许写真实first receipt、run_id、最小sourceIndex以及工程脚本。对写前顺序记录真实事件时间和探测命令类别（不外传私有绝对路径）；仅事后生成时间戳不等于已独立证明写前成功。

使用已经存在的**独立Stage A只读git_identity_root**，核本机root/common-dir/objects/branch/revision与固定Git身份，不准clone/fetch/checkout/reset/sparse-checkout/修改任何既有Git index或common-dir。旧Stage A clone本地缺__init__.py工作树不等于固定Git Blob不存在；应从可访问的**真实固定Commit objects**只读取全70个源文件并到新scratch的source_assembly_root恢复它们的**未经转码原字节**及真实包目录，验证mode、blob SHA1、size、SHA256和pre/post读回；若固定对象/依赖不足，E2 STOP，不从实时其他工作树挪源码凑数。

原D:\ProjectTemp\c5k1bturn56的8 dirty tracked、staged/index/untracked/ignored与外Git common-dir、所有旧失败证据scratch、物理独立C盘已有SSD备份、真实C8/2017/2018/B3/V009失败数组永久禁止写入/清理/重命名/覆盖。Owner仍只要求C盘独立SSD+GitHub备份，无VM或第三备份。可信工作站允许有限ENGINEERING_ONLY import残余风险，但绝不声称OS_NATIVE_SECURITY_SANDBOX_VERIFIED；真实进程前源根需要只读/排他访问策略和before/after完整hash比对，不能静默容忍可观测文件漂移、重解析或保护根访问。

## 2. E1：双根 VerifiedLoader + 有界工程修复

依原已审工程基线 docs/CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md 与旧V010 trusted_workstation_loader_engineering_preflight_task_20261016.md的成熟设计，仅在**本次新scratch内**集中处理原Launcher UInt32、完整包三init、GitGate身份、VerifiedFinder与 VerifiedLoader、Windows Job/audit/PIPE/reader/reap工程bug；V1.3 E1普通错误可以在本轮总预算内修复并有限重复受界工程case，**不新增微任务**，保留每次失败证据/真实消耗，不碰原模型源码。

维持Git identity root≠assembly source root的双根绑定；五条真实Git只读child包括固定树的ls-tree inventory，计准确argv/nonce/exit/bounded stdout stderr、Job对象、子进程reap和reader join。每个冻结包模块需Git commit/tree/path/mode/blobSHA1/size/SHA256与读取前/执行后源字节同一性；VerifiedLoader只在exec_module确实成功返回后记EXECUTED，异常LOADING_FAILED，核module.__file__/__path__/spec.origin/loader/sys.modules。不得伪造已执行模块，也不能关闭安全门“为了让import通过”。

在任何Python进程前**只读确认可信受控python.exe与stdlib以及已存在的NumPy/SciPy和必要native DLL可获得**，不pip/install或使用临时来源不明解释器。Python建议受界-isolated参数 -I -B -S -X utf8（若实际环境不支持，须证明等效配置并记录残余风险），禁pycache/自动site/.pth，网络和未批准持久副作用0，科学求解函数的调用应由独立运行器显式hard-deny。静态闭包先检当前canonical入口的42源候选/20 UNKNOWN/14 IMPORT_TIME_SIDE_EFFECT_RISK旧标签：这些原标签不是运行PASS或永久禁令；本轮限受认证的import-only路径读取实际源码，若确认存在import-time科学调用或不可信来源/动态导入，E2 FAIL_CLOSED而不是执行碰运气。

## 3. E2：真实受界Windows ENGINEERING_ONLY import与runner I/O

仅在E0/E1满足身份/资源门后启动新的非提权Windows Job控制工程Python子进程。优先实测**canonical入口真实import-only**：
from ch5_two_asset_hank.multi_province import mainline_household_runtime

实际日志需区别canon入口自动加载的源码集合与另行明确白名单的九模块import smoke；禁止将“主动为凑九个”当成canonical自动import。工程smoke仅认证模块来源、依赖与运行器I/O：进程PID/退出码/RSS可得性、timeout、stdout/stderr双PIPE上限、Job children和reap、源hash前后均一致。不得调用solve_conditioned_household或公开模型求解API，HA/HJB/KFE/selector/root/GE/IRF调用计数必须真为0。如import本身触发求解/真实数据访问，立即E3停止。

若预算仍足且前述真实导入通过，至多两次**真实工程runner的import-only I/O smoke**（原Runner协议，不是只读代码检查）；受界dummy活子进程timeout/kill/reap负例N13若条件具备可在预置额度内验证，做不到就明确NOT_EVALUATED。真实engineer tests PASS只称ENGINEERING_IMPORT_IO_SMOKE_CODEX_REPORTED，不直接消除FULL_RUNNER_IO_CLOSURE=BLOCKED；完整闭环必须经Astra实际读取可信证据再限域决定，模型科学仍无资格。

## 4. V1.3分账、E1修复预算及失败STOP

- **唯一新预算**：总wall≤180分钟；工程Python subprocess≤6（其中static/synthetic≤2，真实canonical及九白名单import≤2，真实runner I/O≤2），单进程墙钟≤180秒；任何失败/早退均计费，重试仅在6次总额度内，必要时少做一类但绝不透支。PowerShell静态工程检查/普通修复可按任务内预算安排，不套用旧“2批PS”的微任务限制；最多3轮受界focused回归且每次进程/时间计数。旧科学Python与HA调用仍全部0，不继承任何已STOP额度。
- 新scratch所有非Git工程文件含70原源码、隔离runner、first/final、原始输出、资源账总≤32MiB，写前预留≥2MiB结尾/失败封存；项目外新独立bare Git元数据如进入第5节≤3GiB另计。既有Stage A Git只读commands≤120；每次runner只读Git child≤5（不能以额外命令隐匿），stdout/stderr、内存/进程状态明确上限并先计费；不可获取wall/RSS等记UNKNOWN。超额/无法保持源只读与不触保护根即E2 FAIL_CLOSED。
- **E1**的普通JSON/manifest/schema、stdout格式、无伤害工程程序错误在本任务已允许的新scratch路径内修改与重验，不必求一张新冻结任务；**E2**涉及写前路径/source hash/真实import-time副作用/受保护目录风险则STOP受影响执行，若尚未接触模型可写终态，不能为了PASS解除门；**E3**模型经济方程/数值阈值/真实数据/科学HA/敏感外传/未授权网络或保护资产写入须无条件STOP，另需Owner授权。
- 本轮真实first/final及资源记录必须用run_id和不可变单向SHA链接。历史B/S/L20初始seal raw/run_id缺失永久UNVERIFIABLE，原V010 timestamp 25案24预期匹配+1 SPEC_UNRESOLVED及历史执行源码hash UNKNOWN均不回填/升格。E0失败且尚未可信写入时仅在终端安全报告，不为收尾在不可信新scratch写回执。

## 5. 条件式GitHub脱敏证据交换（不阻塞已取得工程阶段）

仅在新scratch E0启动合法、源与敏感信息安全门完整通过后，尝试**本轮**受控远端审阅；若GitHub无法安全发布，单独标PUBLICATION_LOCAL_ONLY/FAIL_CLOSED，**不抹掉此前ENGINEERING gate已得到的真实局部结论**，但不得自授REMOTE_VERIFIED或Astra PASS。

**唯一review ref：** review/ch5-temp-v010-m1-import-runner-20261017
**仅远端Tree新增前缀：** _review_tmp/ch5/v010-m1-import-runner-20261017/
**sole parent：**本任务首次发行Commit。
**4份非可执行、UTF-8 LF、结构化脱敏白名单**：result.md≤32KiB、manifest.json≤128KiB、loader_report.json≤128KiB、runner_report.json≤128KiB。若E2/E3敏感性硬门触发则不得上传受影响原件；case/源码/原日志/个人路径/secret/token/SSH私钥/原argv/真实数据不得公开。manifest记冻结task/model哈希、stage状态、first/final raw SHA声明及匿名单向链接、文件表示 RAW_EXACT/SANITIZED_DERIVATIVE、4份原始来源/远端hash的可核范围；不可自含自身SHA256产生循环。无法安全发布投影就LOCAL_ONLY。历史任何拒绝候选仍PUBLICATION_DENIED。

远端路径只能在**独立review分支Git tree**，不得在本地任何模型、科研、治理worktree/index（包括新scratch）物理创建 _review_tmp 目录。仅允许新scratch内项目外独占不共享git --bare对象仓、无checkout/worktree/alternates；仅用Owner现有SSH Key经ssh.github.com:443严格host-key，禁止PAT/新凭据/global config更改、force。第一次发布前必须确认review ref不存在；完整固定parent对象闭包可达，不能用blob:none不完整promisor对象虚构tree。SSH精确ref检查≤1、SSH fixed-parent完整fetch≤1、普通nonforce push≤1、remote ref readback≤1，Git hash-object≤4、mktree≤8、commit-tree≤1；任何失败不追加同类网络次数或改ref重试。审核只能在**全部4份**通过sanitizer/树/预算门后发布；E1文件展示问题可在发布前总工程预算内修一次，不为旧错直接续任务。

Astra接到候选固定Commit/Tree/ref后只对真正远端字节做独立SHA与单父白名单审查，按V1.3重要工程审议集中存档；先保存永久必要证据，再按Owner协议仅删除审阅分支本次临时文件并核readback（Git历史不等于彻底擦除）。GitHub发布失效本地结果仍仅CODEX_REPORTED_WITH_LOCAL_RECEIPTS。

## 6. 集中交付与科学禁令

仅一次交付V010_M1_V13_VERIFIED_IMPORT_RUNNER_INTEGRATED_RESULT：逐gate E0(prewrite +70 source)/E1(gate+loader)/E2(canonical+九模块+runner/Job+N13)/E3(证据交换)实际PASS/PARTIAL/FAIL_CLOSED/NOT_RUN，首次失败和范围内修复、固定task/model SHA、执行环境和来源身份、实际非科学Python调用数及0科学solve计数、保护结论、first/final SHA及其是否可复算、进程/读字节/磁盘/墙钟/网络预算、所有UNKNOWN。若成功发布再给candidate SHA/tree/sole-parent+4 blobs/SHA256；若失败只给严格脱敏≤4KiB本地摘要，不要生成无止境的Markdown回执。终点一律WAIT_ASTRA_V010_M1_V13_ENGINEERING_REVIEW / STOP。

**持续永久门：FULL_RUNNER_IO_CLOSURE=BLOCKED直到Astra后续独立核准；model_activation=False；Results FALSE；V011 NOT_STARTED；A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY。** 本任务没有任何HA、真实多省稳态、GDP校准、冲击或论文Results授权。
