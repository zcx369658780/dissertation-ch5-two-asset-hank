# V010 Windows ENGINEERING_ONLY runner I/O：Stage B–E独立工程预检（正式任务）

**ACTIVE_TASK=V010_RUNNER_IO_WINDOWS_ENGINEERING_STAGE_B_E_PREFLIGHT**
**Owner许可来源**：2026-10-16 Owner要求“补上刚才缺失的github验收，然后继续”；此前对ENGINEERING_ONLY Windows preflight的独立授权和范围委托、现阶段Stage A完成验收提供明确上下文。**本授权严格解释为再次执行受界工程预检，不是批准HA/HJB/KFE、真实数据、旧进程额度结转、自动V011或Results资格。**

**本任务只允许Codex在Windows本地执行；Astra仅独立审阅GitHub候选。任务已经冻结后不得重发或自修原冻结文本。**
**终点**：`WAIT_ASTRA_V010_RUNNER_IO_WINDOWS_BE_REVIEW / STOP`。即使工程用例全部PASS，Codex不得自授Astra PASS/科学许可。

## 0. 起点与权威

- 仓库`zcx369658780/dissertation-ch5-two-asset-hank`，治理分支 `migration/astra-workflow-20261012`。**必须从本任务发行的固定Git Commit及task blob回读任务原件**，不得用动态HEAD代替；在发行后的`TASK_CURRENT`取得准确身份。
- Stage A源码对象准备已经完成、独立审议：固定模型branch `codex/ch5-v010-matlab-first-20261015`，commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`、sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`。九份模型源实际Commit Blob、SHA256和字节数曾由Astra按远端固定Commit重新计算9/9一致，**但本机启动前仍须重新验证当前实际磁盘来源**。
- Stage A官方review分支 `review/v010-stage-a-model-ref-reachability-20261016` HEAD=`d84cc76b19cbb81e097f502348b5073633fbda6e`，tree=`5a03f952ba471352a685b327e79a33176e8bd7b6`，唯一父为Stage A发行commit `68530b3f121952b4382d08dc9ff964c7f6c7ab75`；两脱敏文件已远端独立哈希100%匹配此前用户上传原件。验收补遗 `versions/0.0.10/stage_a_github_publication_recovery_followup_review_20261016.md`，Stage A原上传主审 `versions/0.0.10/stage_a_git_reachability_uploaded_primary_review_20261016.md`。**SSH443是否通、未修改global Git config来自Codex本地声明，不是Astra实时验证**。
- 当前runner设计候选固定在此前review commit `c207e866cf70d9d5ae6fb245f43cabfdeac1d32b`：`versions/0.0.10/review_runner_io_offline_static_draft_20261016.txt` blob `dac0cf74364843f7e0f8b5cbebdbb3481a4ff329`、SHA256 `3FF7B5D6FBEF57CE851C327EA5C6E6CA8200C852A3C1629586F3AC584FACFF11`；static cases JSON blob `8d221ad63471427223b81087121b0067f649b23f`，SHA256 `5B7D1B661FFF84F5844B15AE5104307B0FDEA0A23F70B809FBAC7A29E351A1CC`（46主例+23变体）；该TXT是**未经执行的非发布工程草案**，仅能复制到新scratch并在本任务授权范围内修工程部分，不能视为已可运行或科学可采纳。
- 原V010冻结科学计划commit `bf091da33d59293f147d52c11580327d3ac2a85d`、plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`，原synthetic fixture blob `40915658d93403cfc21b33a6b864b332b7857749`，单点manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`，不追改、不计算。

## 1. 唯一新Windows范围及禁止事项

新独立输出目录`D:\ProjectTemp\ch5_v010_runner_io_windows_BE_20261016_01`；若不全新、无法保证排他/无reparse、路径指向原受保护树即STOP，不清理、复用、重命名旧证据。**只读复用已签出的独立Stage A模型clone**（源于`D:\ProjectTemp\ch5_v010_stage_a_git_reachability_20261016_01`，准确model clone子路径只从其固定本地交付回执确定）；不再`git clone/fetch/pull`任何模型分支。不对Stage A clone进行config、checkout、reset、clean、index写入，禁止嵌套新Git worktree、shared object/alternates和任何写操作。若签出clone不存在/被改/身份不符，**STOP**，不在本轮补clone/fetch。
- 保护原D工作树`D:\ProjectTemp\c5k1bturn56`、8dirty tracked、staged/index、外Git common-dir、untracked/ignored、全部旧失败日志/回执、C8/2017/2018/B3、V009失败数组、其他项目。只核新隔离clone和runner草案/静态cases的已公开源。不允许GitHub main、治理branch或历史review变更。
- **模式唯一 `ENGINEERING_ONLY`**。runner及外层launcher都须显式拒绝`ONE_HA`；原草案只检查“任意40位new_science_authorization_blob”的逻辑必须在新受控副本中改成无条件fail-closed（不可自行推断科学许可）。不得调用`solve_conditioned_household`、`construct_v0`、selector/root/HJB/KFE/GE/IRF、scipy solver或真实数据reader；`HA/HJB/KFE/selector/scalarRoots/GE/IRF/MATLAB/pytest/realC8=0`，新科学Python进程`0`。**工程Python进程≠科学Python进程**，必须单独计账。
- 工程副本允许限于Git子进程审计/日志/I/O/异常/loader身份和独立test harness的修正；不得改原9 Python模型源码、数学方程、税/政府投资/人口/资产收益和scipy算法，也不得对历史文件追改、删减安全deny条款救PASS。

## 2. 新独立资源预算（旧额度全部不结转）

- **新工程Python进程上限4个，总启动次数连失败/kill都在启动前持久扣账**：最多1个pure AST+静态cases结构验证过程；最多1个isolated negative harness（69预期案例可在单进程中调度）；**最多2次真实Windows `ENGINEERING_ONLY` runner启动**。任何再次调试/二级Python/pytest/ipynb都占此4次、不得绕账。各进程外部wall限`180秒`，总体wall限`3小时`；使用外部PowerShell持久进程ledger（创建前先扣），记录PID/exit/elapsed/适用的峰值RSS/工程目的与严格SHA256。脚本失败后不自动重试，剩余额度也不用于科学。
- 新scratch所有非Git工件增量（工程copy、harness、stderr/stdout、JSON/log/失败事务、外部账本、应急封存、全部测试素材）**合计≤32 MiB（33,554,432字节）**，写前外部检查并为最终/应急回执预留≥2 MiB。runner内部`Writer`的CAP/RESERVE须与本限额**一致且更严格**（不能维持原草案96MiB来假装外部32MiB已安全）；紧急退出时本机外部ledger必须保留，不能因runner内部故障漏计。禁止把异常原始stdout/stderr复制成GB级日志。单文件本地final建议≤1MiB。
- 无新模型clone或network model fetch。最多新建一个**单独非共享Git发布元数据工作区**（仅在需要发布脱敏候选时；≤1GiB额外Git对象+metadata），只定向取得本任务发行commit用于按任务原parent制成review提交，不能趁机补取模型源码，不能读取原保护树。候选发布最多一次普通non-force push，可用Codex刚修好的受控SSH443路径，**不得修改global/system Git config**；若认证或对象准备失败，`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`，STOP不重试。公有审阅合计文件大小按下文另设小预算。
- 运行前/后对所有新增实际bytes、Git child数、Python launch计数、elapsed做**双来源外部ledger**；超过硬限额立刻fail-closed并保存证据，不可在超限后清理文件把总账伪装成未超。原旧V010实施pytest4/6、driver1/4、HA1/26、selector1626、roots1642，两次单点Python各1/1且HA0、首次43,519,638B超32MiB的历史、先前工程preflight 0/4 STOP和Stage A 0Python均原样保留，不重置/转移。

## 3. 强制先后验证门（全部在本任务范围内）

**B0：Windows工程preflight前置身份，无Python。** 只读核本任务固定Git blob、草案TXT/JSON exact Git blob、已发布Stage A review来源、模型clone的HEAD/tree/sole parent、独立Git common-dir、九份源文件`git hash-object --no-filters`及SHA256/bytes等于Stage A manifest，clone没有alternates/shallow/promisor，模型clone/source路径不可重解析指向原受保护树；固定Python及Git exe绝对路径/签名/hash、可信启动环境；全新runner scratch与外部进程账。失败`NO_PYTHON_STARTED / STOP`。

**B1：一次AST与用例定义核查（工程Python≤1）。** 在新scratch使用`ast.parse`/compile源码但不import/执行模型；核runner唯一受控入口、工程-only mode及ONE_HA硬拒、UTF8/bytes/固定身份和hook注册点。核46主ID（A01–A08，D01–D16，N01–N22）+23 `variant_cases`完整映射，需逐条确认对象结构、不把静态expected当执行PASS。不得生成模型pycache、不能调用scientific solver。

**B2：一次合成负例harness（工程Python≤1）。** 可以使用受控fake child与封闭纯工程I/O模拟，不访问真实model数据，用69项JSON ID逐例记录`PASS/FAIL/NOT_EVALUATED`，重点Windows审计event shape差异、argv/cwd/exe/env注入、带外Git第六调用、伪造4身份输出、9源bytes身份不符、dual PIPE overflow、child nonzero/timeout/reap、writer超额/pending事务/异常终态、reparse与路径别名、重复hook/其它hook不可枚举、未经允许ONE_HA。只执行本文件实际被覆盖用例，绝不因静态anchor存在记PASS；核心负例不能通过则STOP，允许在4过程配额剩余时修工程副本，但不重置B1/B2已扣次数。

**B3：真实WindowsENGINEERING_ONLY runner最多2次。** 单个新鲜、可信解释器（建议`-I -B -X utf8`；`-S`与否需基于可信依赖/证据作工程决定，任何sitecustomize/.pth/hook环境可信性未知即FAIL_CLOSED）。必须在真正进程实际收集/脱敏Windows `subprocess.Popen` audit event结构和list2cmdline argv形态，严格验证真实Git child exit/stdout/stderr/reap：
  - 每次真实runner仅四条身份Git命令`rev-parse HEAD`、`rev-parse HEAD^{tree}`、`show -s --format=%P HEAD`、`rev-parse --path-format=absolute --git-common-dir`，其stdout/exit与实际固定clone闭环；随后至多第五条只读`ls-tree -r 94de4501dec051b969bee9d852eba2d4591f30ef -- src/ch5_two_asset_hank`，与九源码实际disk bytes/Blob匹配。禁止Git网络、checkout、status写索引、hash-object -w/其它非白名单子进程。
  - `shell=False`、固定Git exe/cwd/env；每个child timeout≤30秒，identity stdout≤4KiB，inventory stdout≤1MiB，各stderr≤4KiB，双PIPE有界reader、Job Object kill-on-close/超时kill/reap/join并留可复核匿名化状态；不得允许Git Hook不可信外部exec。
  - 真正启动必须记录`sys.addaudithook`来源：同一受控进程中唯一**本项目注册点**可定位，但Python无API列举历史hook，不能伪称OS内绝对无其它hook；要从trusted fresh-launch及site环境证据支持`HOOK_PROVENANCE_BOUNDED`，缺失标UNKNOWN/STOP。
  - 九份真实模型源的实际磁盘bytes重新认证并校加载器`__file__`、loader签名与可信sys.modules; **仅import-only smoke（安全时）**，绝不调用任何数值函数。第三方依赖使import不可用时记录`LOADER_IMPORT_NOT_EVALUATED`而不是越过安全hook或扩大学科范围；如果此项是完整闭环硬门，则工程结果不能宣称FULL PASS。
  - Writer有限成功封存+至少一种受控失败封存路径真实观察，保留外部账本，即使内层final失败仍需fail-closed；已知仅Python audit hook不构成原生进程/网络的OS沙箱，不能宣称A16解除。
- 真实Windows argv若仍与期望不同，只能在安全白名单**更严格或等效**前提下修复并使用剩余最多一次真实runner重测；如果任何关键门需要超4进程/32MiB/3h，立即STOP，**不得自增额度**。

## 4. 合格分类、脱敏review及终点

Codex可报告的唯一正向候选分类`ENGINEERING_RUNTIME_PREFLIGHT_CANDIDATE_PASS_REPORTED`，成立条件：固定Git四身份与第五inventory真实Windows双管道有界child全部exit0/timeout安全、九源磁盘与loader可信绑定、入口mode硬拒ONE_HA、关键合成负例真实运行且异常配额/封存受界、Windows Job/Hook证据分账、无科学调用、进程账与总字节账均闭合。否则据事实记录`PARTIAL_ENGINEERING_DIAGNOSTIC`、`ENGINEERING_PREFLIGHT_FAIL_CLOSED`或`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`；所有未执行用例标NOT_EVALUATED，不能把Python语法/JSON锚点当运行PASS。**Astra下一轮独立审阅后最多给工程限域接受，不自动启动ONE_HA/GE/IRF/V011。**

允许**一次**GitHub候选公开交付，仅全新review分支 `review/v010-runner-io-windows-engineering-b-e-20261016`，唯一parent是**本任务发行commit**（由发行Git固定SHA在后续`TASK_CURRENT`提供）；不得修改main、治理branch、旧review或模型冻结源码。新分支不存在时才允许创建，禁止force，单次普通nonforce push后远端commit/tree/唯一parent及文件SHA回读。仅三份经脱敏白名单文件：
1. `versions/0.0.10/review_runner_io_windows_be_result_20261016.md`（≤30KiB）；
2. `versions/0.0.10/review_runner_io_windows_be_manifest_20261016.json`（≤96KiB，运行用例矩阵+PID/exit/预算匿名摘要，不能公开真实D绝对路径、raw argv或秘密）；
3. `versions/0.0.10/review_runner_io_windows_be_static_draft_20261016.txt`（≤96KiB，非直接执行的脱敏工程runner新草案）。
不能安全脱敏或SSH凭据失败 => LOCAL_ONLY STOP，不允许追加push。旧Codex发布失败/补救的SSH元数据、本地raw日志/原材料保持私有，不直接传上GitHub；本机文件/受保护目录不作为公开候选。GitHub发布是备份/证据交换，不意味着HJB/HA实验合法、独立测试已通过或模型可用于论文结果。

**最终停点**：`WAIT_ASTRA_V010_RUNNER_IO_WINDOWS_BE_REVIEW / STOP`。冻结原科学合同、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、real C8 A–D REQUEST_ONLY、原8dirty/index/common-dir/全部旧失败和V011 NOT_STARTED严格维持。
