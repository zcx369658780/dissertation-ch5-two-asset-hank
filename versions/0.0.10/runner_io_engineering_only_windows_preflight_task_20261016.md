# V010：ENGINEERING_ONLY Windows runner I/O 受界预检（Owner正式授权）

**唯一新ACTIVE任务ID：`V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT`**。
**权限来源：**2026-10-16 Owner在新会话明确批准“ENGINEERING_ONLY Windows preflight”，并把条件范围委托Astra决定。本文件是该许可的**上限**，不是科学实验、历史预算恢复、完整安全认证或V011启动。
**终点：**`WAIT_ASTRA_V010_ENGINEERING_PREFLIGHT_REVIEW / STOP`，Codex只可报告候选结果；**不得自授 `FULL_RUNNER_IO_CLOSURE=PASS`、科学许可或后继任务**。

## 0. 固定权威、前置状态

- 仓库 `zcx369658780/dissertation-ch5-two-asset-hank`；治理分支 `migration/astra-workflow-20261012`；先从live目录确认本任务唯一ACTIVE。该任务在本文件发布的**固定Git commit/blob**中冻结，运行前需要从GitHub回读准确身份；不得以动态HEAD替代本任务对象。
- 原V010科学计划commit `bf091da33d59293f147d52c11580327d3ac2a85d` / plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；合成fixture blob `40915658d93403cfc21b33a6b864b332b7857749`；模型代码candidate `94de4501dec051b969bee9d852eba2d4591f30ef` / tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；单点HA输入manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`。全部只读、不追改。
- 已交付且独立静态核验的runner文本：review commit `c207e866cf70d9d5ae6fb245f43cabfdeac1d32b` / tree `b4ba5b7939653a0cdb8524fa82743d9634d79083`，`versions/0.0.10/review_runner_io_offline_static_draft_20261016.txt` blob `dac0cf74364843f7e0f8b5cbebdbb3481a4ff329` / SHA256 `3FF7B5D6FBEF57CE851C327EA5C6E6CA8200C852A3C1629586F3AC584FACFF11`；46例JSON blob `8d221ad63471427223b81087121b0067f649b23f` / SHA256 `5B7D1B661FFF84F5844B15AE5104307B0FDEA0A23F70B809FBAC7A29E351A1CC`，23个变体；原报告blob `73daf247c2a6bcf44e9ca65dcbc0af893e72ec55`。这些文件原本**均未执行**。
- 上一轮独立验收 `versions/0.0.10/runner_guard_io_offline_github_primary_review_20261016.md` blob `c8f4b938c87fd3ea7b0443fa2be32793e5733917`，分类 `STATIC_DESIGN_READY=CONDITIONAL_LIMITED_ACCEPT`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`。旧任务已交付、静态有限接受并结束；本轮不重复派发旧任务。
- Codex自报上轮本地产物269165B、0 Python/HA与一次普通push；GitHub可独立证明3文件/parent/tree/blob，但不可直接核实D盘交付回执。原 `DELIVERY_RECEIPT.json` 只能在本机作为既有只读原证，不能因网页已有GitHub候选便称已独立核实。

## 1. 授权的准确对象与禁止事项

**只为证明工程Windows预检链**：固定candidate下真实 `subprocess.Popen` audit形态、Git 4条身份输出的实际child/exit/reap绑定、第五条固定commit的 `ls-tree`、九份模型Python源码**本机磁盘原字节**及导入模块 `__file__`/loader、I/O预算/路径/异常保护、Windows Job Object与timeout、writer正常和故障回执，以及工程-only启动/退出见证。

Codex可在**新独立scratch**内复制并修改上述**尚未执行的runner文本**、专用ENGINEERING_ONLY launcher、最小负例harness、机读receipt、静态对照报告；仅限runner和执行基础设施。不得修改原静态review提交、原MATLAB、模型15文件/科学数学、corrected selector/HJB/KFE、参数/网格/阈值、单点manifest、原两次失败日志/旧回执。不得为通过守门而放宽Git argv白名单、删除/忽略audit、解除IO配额或用不真实的stub替代真实Windows正向Git证据。

**本任务科学执行硬限制：`HA=HJB=KFE=selector=scalar_roots=GE=IRF=MATLAB=0`；`pytest=0`；真实C8/2017/2018/B3/旧V009失败数组读取=0。** 禁止调用 `solve_conditioned_household`、`construct_v0`、`select_constrained_policy`、`terminal_kfe`、`brentq` 等科学函数。只允许工程导入与输入字节核验；不得构建或运行单点HA、合成双省GE、稳态或响应。引入新模式的能力字符串、任意40位授权blob、`mode=ONE_HA`等均**不是科学运行权限**：本次测试使用的独立runner副本必须把ONE_HA明确fail-closed，外部launcher亦只能传ENGINEERING_ONLY。

新隔离工程目录：`D:\ProjectTemp\ch5_v010_runner_engineering_preflight_20261016_01`。任何读写`D:\ProjectTemp\c5k1bturn56`、其8项dirty tracked、staged/index、外部Git common-dir、untracked/ignored或任何旧失败目录中的**写操作**均禁止；旧回执只允许精确文件read-only、小体积读取且不得外传raw内容。候选模型必须在**不共享原common-dir**的独立clone签出，不能使用worktree/shared objects、原dirty树或原私有数据仓。未能构造真正隔离/可信工作目录即STOP。

## 2. 预算与严格扣账

- **工程Python进程总上限4次**，所有本任务 `python.exe`、`py`、AST脚本、import或任何Python子进程（成功/失败/被kill）**从创建尝试前持久扣账**；不得把Python嵌在PowerShell/pytest/Jupyter/二级launcher中绕账。指定用途：最多1次语法/机读结构验证；最多1次非真实模型的守门负例harness；剩余**最多2次**真实Windows ENGINEERING_ONLY runner启动（可在本任务限额内修复后再测）。若前两类不需要某次可不运行，余额不会扩大真实runner两次的上限。
- 每个工程Python进程的**独立外部wall timeout≤180秒**，总任务wall≤3小时。启动前由PowerShell/可信宿主把任务ID、准确runner/launcher哈希、用途、时间、计数写入新scratch的**持久外部进程账**；无法扣账就禁止启动。运行后记录PID、exit code、elapsed、可获取的峰值RSS（未知标UNKNOWN，不推测）、准确原始摘要哈希。即使runner自己的final.json写失败，外部启动账和STOP必须保存。监控/中止不依赖runner自身log或watchdog；不可静默自动重启。
- 真正runner每次**最多5条Git child**：4条身份精确命令 + 在身份全部确认后仅一条固定commit `ls-tree -r 94de4501dec051b969bee9d852eba2d4591f30ef -- src/ch5_two_asset_hank`，必须是已批准精确token/Windows list2cmdline等价形式，Git exe/cwd/env固定，`shell=False`。每child timeout≤30秒且kill/reap/双PIPE reader全部必须有界；身份stdout≤4096B、source inventory stdout≤1MiB、stderr≤4096B；不准联网、Git写入、可变HEAD的inventory、`status/fetch/checkout/reset/clean/hash-object -w`（独立clone准备阶段按下款单列）。
- 新增**所有工程artifact与scratch增量**（runner草案、test fixtures、日志、receipts、外部进程账、未完成事务文件）总量**≤16MiB**，写入前预估和检查，未完成/failed写入也计数，final与emergency留可实现的硬预留；超限立即STOP并保留原证。必要的**一次独立clone**及其Git对象另设≤2GiB实体上限；clone不得指向或复用原保护common-dir。公开GitHub审阅内容不含私有原件/绝对路径/秘密。单一preflight回执推荐≤1MiB。
- 原V010科学/实现历史账永久不变：Codex报告pytest4/6、science driver1/4、HA1/26、selector cells1626、scalar roots1642。前两次单点Python各1/1耗尽，HA均0；第一笔43,519,638B超32MiB 9,965,206B，第二笔117,446B在96MiB内。**本次新4次仅工程Python进程**，不回填、抵扣、重置或替代科学进程/HA额度。

## 3. 集中工程步骤及顺序门

**A. 不运行Python的前置核验（必要）。** 用PowerShell和只读Git检查既有静态候选3 blob、原冻结model SHA/tree、原单点manifest、当前任务准确Git身份；确认受保护原tree未触及的能力边界、绝对路径与reparse安全、可信pinned `python.exe`/`git.exe`二进制及hash、独立clone `.git`为自身common-dir；确认工程输出root是全新独占目录。失败保持`NO_ENGINEERING_PROCESS_STARTED`。clone建立只能在单独新目录，不得读/写原dirty树/历史对象；读取Git/clone操作与真正runner的5 Git child分别计账。

**B. 可用工程进程1：纯AST/结构与源码检查。** 对新独立runner草案用`ast.parse/compile(...,dont_inherit=True)`验证Python语法，**不import/执行模型、无py_compile生成文件**；JSON解析46唯一原例(A01–A08/D01–D16/N01–N22)和23个variant，检查每条输入/预期/唯一case id与映射；静态回读无自动main、科学模式禁用、唯一launcher/唯一hook注册位置、9份expected blob、UTF-8/LF以及不含私有绝对路径。任何异常/假证据STOP，不启动正向runner。

**C. 可用工程进程2：隔离负例与I/O故障验证。** 在同一ENGINEERING_ONLY process中用纯harness/可控伪child验证最关键拒绝分支：Popen argv list/tuple/Windows渲染差异，注入命令/环境/cwd与nonce复用，伪identity输出、dirty源码字节、stdout/stderr超额、超时未reap、非零exit、非法UTF8、路径/reparse/写前配额、log pending事务失败/final预留不足、重复hook标志、未经批准科学mode与第六Git child；按46+23 spec逐项报告`PASS/FAIL/NOT_EVALUATED`，不允许仅引用JSON期望便称69运行PASS。harness不可执行真实HA、不得启动任何二级Python或真实非白名单child。失败则先限域修复、用**剩余**授权预算重新检验；关键负例未闭环不得进入D。

**D. 最多2次独立真实ENGINEERING_ONLY Windows runner。** 全新、可信解释器，以绝对pinned Python、隔离参数（`-I -B -X utf8`或同等已验证隔离）、受控环境和唯一独立runner源码起动；不导入旧runner，不叠加旧hook。先静态/启动上下文证明未预置受保护旧hook、无未知 `sitecustomize`/`.pth`注入或环境劫持；若无法证明，只可`HOOK_PROVENANCE_UNKNOWN / STOP`，不得伪称单hook安全。对真实Windows的audit事件实际观察**事件类型/argv形态/净化哈希**（不得外发私有原始argv或机器路径），完成四次真实只读Git结果绑定、Git-commit/tree/parent/common-dir与第五次source map。对九份模型实际磁盘bytes计算Git Blob与必要raw哈希，真实受控loader导入并核`__file__`、preloaded-module/pycache路径、同一固定candidate，不能只读`ls-tree`就当来源闭环。**仅允许import-only工程smoke，绝对不调用solver**。失败准确stop并保留外部launch扣账/有界raw本地证据。

**E. 路径/日志/Windows过程真实观察。** 确认Job Object分配与kill-on-close/timeout/reap/reader join可信；测试正常小型writer和至少一类受控故障封存路径，不向原保护目录写入；未测试的故障分支明确标UNKNOWN。runner曾声明可信机器假设不等于OS沙箱；`sys.addaudithook`不能证明拦截所有原生I/O/第三方模块网络活动；不得宣称A16解除。Windows真实argv如果与草案预期不同，记录形态/哈希并STOP或在**不放宽白名单与权限**的条件下限域修复后用剩余预算一次重测。

**依赖失败必须停。** 禁止忽略`$LASTEXITCODE`、负例失败继续正向、超额后抹除/重命名证据、修改冻结经济或数值阈值救PASS。允许本任务工程预算内集中修复runner草案并重跑**仅明确尚有余额的工程门**；一旦超过配额、保护/OS信任边界或必须改科学代码，立即`STOP_AND_REPORT`，不向Owner自动追加预算。

## 4. 验收门及准确表达

仅满足全部真实工程正向身份/磁盘来源/界内IO/exit证据、关键负例真实测试、无越权/无科学调用/完整外部进程账，Codex方可**报告**`ENGINEERING_RUNTIME_PREFLIGHT_CANDIDATE_PASS_REPORTED`。Astra仍须独立核GitHub可读源与脱敏回执才考虑限域工程接受；其他可分类`ENGINEERING_PREFLIGHT_FAIL_CLOSED`、`PARTIAL_ENGINEERING_DIAGNOSTIC`、`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`；任何未执行case逐项标`NOT_EVALUATED`。不把模拟harness假child当真实Windows child，也不因退出码0便判`FULL_RUNNER_IO_CLOSURE`。

**本任务无科学授权**：即使全部preflight通过，`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`的corrected HA仍`UNTESTED`；新的HA科学进程必须由Owner另行明确授权、单独固定资源与独立preflight门，不可自动启动。V010冻结计划不改；V011不启动；`model_activation=False`、`Results FALSE`。

## 5. 交付、GitHub限域和STOP

唯一最终报告：`V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT_RESULT`，至少含：本任务固定commit/blob、runner草案与实际执行脚本SHA256、基准树与9份磁盘源码真实hash/导入路径认证、所用机器/解释器/真实Git child audit事件**脱敏结构**及exit/reap、46+23的case实际执行矩阵、工程Python 4次累计账及每次用途/PID/exit/wall、Git child调用数、所有新增文件实际字节/限制、writer失败/应急路径、匿名化本地保护证据与未观测内容。记录`engineering_process_count`与`science_process_count=0`及`HA_calls=0`分别，不以有余量为由再运行。

可以专为本轮**一次**普通non-force发布GitHub `review/v010-runner-io-engineering-preflight-20261016`（若分支已存在，须核验并STOP，禁止force改写），从**本任务发行commit**作为唯一父节点建立；仅以下3份已脱敏且UTF-8/LF的review材料：
1. `versions/0.0.10/review_runner_engineering_preflight_result_20261016.md`（≤30KiB）；
2. `versions/0.0.10/review_runner_engineering_preflight_manifest_20261016.json`（≤64KiB，仅安全hash/子进程状态/案例摘要，无原始argv/path/raw字节）；
3. `versions/0.0.10/review_runner_engineering_preflight_static_draft_20261016.txt`（≤96KiB，仅脱敏、不得从GitHub直接运行）。
禁止公开D盘原runner、绝对目录/用户名、raw log、secret、真实数据、大型测试回执；不写main/治理分支/旧review分支/冻结源码。发布后远端回读唯一parent、tree、3 blob及SHA256；如果任何资料脱敏不安全则完全`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`，由Owner选择手工交付，绝不为push而越权。

最终必须`WAIT_ASTRA_V010_ENGINEERING_PREFLIGHT_REVIEW / STOP`；不自动启动单点HA、不更改原数学、不自动V011。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、真实C8 A–D REQUEST_ONLY、原8dirty/index/common-dir与历史失败不变。
