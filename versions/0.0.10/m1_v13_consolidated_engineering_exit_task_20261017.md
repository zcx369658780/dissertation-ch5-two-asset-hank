# V010 / V1.3 — M1 一体化工程闭环长任务

**任务 ID：V010_M1_V13_CONSOLIDATED_ENGINEERING_EXIT**
**任务类别：ENGINEERING_ONLY_LONG_TASK / NO_SCIENTIFIC_SOLVE**
**Owner授权：**2026-10-17，明确要求从反复“单错误→微任务”改为一次完整的V010 M1长任务，恢复Codex在预授权范围内对普通工程问题的自主诊断、修复、复测能力。
**交付 ID：V010_M1_V13_CONSOLIDATED_ENGINEERING_EXIT_RESULT**
**结束：WAIT_ASTRA_V010_M1_CONSOLIDATED_ENGINEERING_REVIEW / STOP**
**冻结依据：**本任务首次发布的GitHub Commit与本文件Git Blob由随后CURRENT/TASK_CURRENT登记；一经发布不追改正文。模型和科学合同仍在本任务之外冻结。

## 一、唯一工程目标和真正退出标准

一次性打通原MATLAB两资产HANK的冻结Python模型在可信Windows工作站的**源码身份→受控导入→VerifiedLoader真实执行→九监测模块→真实runner I/O**工程闭环。将过去数轮发现的bug作为同一M1工程交付的**内部待修清单**，不能再为普通platform/stdout/manifest/ledger/parser/fixture错误单独生成新GitHub任务单。

**必须在一次长任务内自主覆盖的工作：**
1. 可信重建和认证固定70份模型Python原始Git Blob（含三个非空init），区分原始源码数据流与诊断日志，修正实时字节预算/截流机制。
2. 实现可追溯、单写者、启动前计费的工程调用ledger，避免前次并发覆盖/启动前文件冲突；保存真实first/final、各次失败和复测来源。
3. 审计和在安全范围内处理Windows Python/NumPy→platform.machine→uname→win32_ver→_syscmd_ver→subprocess.Popen与本机版本探测、IO不存在缓存负探测、socket.gethostname事件、原合成四段版本expected错误等**全部相关普通工程兼容问题**；对新出现的同级别小错直接在本任务范围内修正。
4. 在固定源码和不开放任意子进程/网络的前提下完成至少一次真实canonical import-only，并准确采集已执行模块和source身份；完成显式九模块身份验证，明确区分canonical自动加载与额外白名单import。
5. 完成真实Windows runner import-only I/O smoke，验证五条原批准只读Git children、Job、PID、bounded PIPE、超时/reader/reap、前后源码hash；保留既有N13上轮4.039秒本机报告级正向证据，**仅修改Job/timeout/reader机制时**纳入本轮回归。
6. 集中交付工程候选、失败/修复与来源证据；安全满足时一次性交付GitHub临时review供Astra独立验收。证据传输失败不抹去合法本地工程进展，也不能冒充Astra远端PASS。

**工程退出标准是上述实际运行事实，而不是“所有安全脚本都写好了”。** 若最后canonical或runner仍遇真实E2/E3硬阻断，则局部结果照实交付\`PARTIAL/FAIL_CLOSED\`，不得伪造工程闭环；有预算的普通E1失败须Codex先自主定位修复而不是立即STOP/索要新微任务。

## 二、冻结源、Owner边界与单次可信启动

- 唯一仓库\`zcx369658780/dissertation-ch5-two-asset-hank\`，权威治理分支\`migration/astra-workflow-20261012\`（**不是main**）。Codex首先从\`TASK_CURRENT\`登记的**固定发行Commit**获取本文件并核Blob，另读\`CURRENT\`、V1.3工作流\`docs/CH5_ASTRA_WORKFLOW_V1_3_20261017.md\`、Owner决策\`docs/CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md\`及远端证据交换协议。普通旧历史ACTIVE不能覆盖本冻结任务。
- 原V010科学计划Commit \`bf091da33d59293f147d52c11580327d3ac2a85d\` / Blob \`85138d8859d53295262fe13bf5bc277bca95ed3f\`；冻结模型Commit \`94de4501dec051b969bee9d852eba2d4591f30ef\` / Tree \`205eab47c4e4f9c6292c2ead9947d94d1a7579a5\` / sole parent \`a1db8c114dec0ab69d69a5576e153a7f868cba0e\`。全部70份Python源及三init真字节、原已接受HJB/KFE/selector数值阈值与MATLAB经济方程不得改。旧源码中的历史问题不通过“为使import成功”篡改数学求解实现。
- 已STOP上轮主审\`versions/0.0.10/m1_v13_platform_syscmd_ver_local_only_output_cap_fail_closed_review_20261017.md\` / Blob \`cdc0f10eea4c4cefb5b7551ca479da6237764c1b\`：上轮NumPy→platform.*→Popen来源报告为\`LITERAL_VER\`/shell=True且原GIT_NO_CAPABILITY正确拒绝；无spawn适配语义UNRESOLVED；canonical未过、九模块与runner未运行；Git源码stdout 1,106,482B超过旧262,144B进程限额844,338B且延迟STOP，ledger并发覆盖/冲突保留。**该违规和所有历史旧缺失、STOP额度绝不追溯清零或继承。**
- **唯一新项目外可写根**优先\`D:\ProjectTemp\ch5_v010_m1_consolidated_20261017_01\`。如它在首写前已存在且本轮从未触写，允许唯一备选\`D:\ProjectTemp\ch5_v010_m1_consolidated_20261017_02\`；两者均须先在受信任Windows终端**零文件写入**核父目录/目标身份、目标不存在、不重解析、与保护根无交叉；创建后、第一字节写入前再次核新根身份。失败不能更换未授权第三根或对旧根补做“写前”记录。不要先在待验证根写preflight脚本/日志。
- 原\`D:\ProjectTemp\c5k1bturn56\` 8 dirty tracked/index/staged/untracked/ignored及外部Git common-dir、独立C SSD既有备份、全部历史失败scratch/封存、真实C8/2017/2018/B3/V009资产禁止写入/checkout/stash/reset/clean/rename。Owner已接受可信工作站风险和C SSD+GitHub备份，不要求额外VM或第三份备份；不能自称native OS sandbox。
- Stage A Git identity root仍**只读**，固定70源码从可达的冻结Git raw blob装配到本轮新scratch/source_assembly_root；认证Git SHA1 Blob/size/Mode与SHA256并在运行前后比对。可只读引用已确认证据作为定位线索，但不从旧运行scratch直接import，也不要求为每次普通测试都重装70源码；当前任务内一次认证源可在其身份未变且比对通过时复用。

## 三、工程实施原则：足够的自主修复空间，但不扩大科学权限

**A. 源数据流 vs 诊断日志**：上轮误将合法Git原始源码取字节通道并入256KiB日志上限。本轮允许\`git cat-file\`等**事先精确认证的固定Blob数据提取命令**走独立受计量的原始字节数据流：每个blob的实际字节须与固定tree预期长度匹配、实际SHA1/SHA256及大小复核，全部原始source/必要Git协议header字节累计上限**16MiB**，遇长度不符或总量超限需**边读边终止**；不可把任意Git stdout/异常/traceback事后重标为raw来源来逃避审计。其它程序的诊断stdout+stderr每子进程上限**1MiB**，独立实时截流、计费与保存截断事实。两类通道在manifest中明确分账。正常Git源≈1.1MB应不再天然触发旧的256KiB日志假门；本轮新合同不追改旧FAIL。
**B. 原子执行账**：一个拥有writer权限的进程负责ledger；每次Python/Git/Job/dummy启动前记\`run_id / seq / purpose / max budget / sourceSHA\`并读回，对并发写入用互斥/原子提交或单队列序列化；失败保留原始事件，禁止覆盖上次first/原final或并发冲突后凭重新生成“完美日志”回填。若有文件冲突，仅在当前新scratch内部按V1.3 E1调整设计并自测后继续，保护根未知则STOP。
**C. Windows平台/NumPy兼容**：前轮真实调用链可用作候选事实，不必为探针另立任务。先验证实际\`platform.py\`、依赖原始字节/当前版本及测试oracle是否错误。优先让原生导入在不授新权限下成功；确需替代版本信息时，**只准当前工程runner的最窄adapter**，以可信OS/Python原始元数据对导入时**实际消费字段**做可检验的观测等价性测试（不强求证明所有未使用Windows版本/locale组合的全域语义等价），保留原始来源、适配代码和适用条件/局限；不能捏造值、无条件返回常量或改系统stdlib/模型源码。适配导入必须标\`ENGINEERING_ADAPTER_ONLY\`，不冒充原生pass，更不授科学求解。原五条真实Git只读child有专用能力；其它shell/\`Popen\`及网络默认DENY。Numpy的\`platform._syscmd_ver\`不能成为开放任意\`cmd.exe\`/非Git spawn的理由。
**D. 真实import/runner**：非提权可信Windows工程Python\`-I -B -S -X utf8\`或有证据等效方式；现有受认证stdlib/NumPy/SciPy/native来源，禁pip/未知依赖下载。VerifiedFinder/Loader显式绑定Git identity root与新source assembly root，\`exec_module\`返回后才标EXECUTED；保留\`sys.modules/spec.origin/__file__/__path__/loader\`真实证据。canonical入口必须实际执行\`from ch5_two_asset_hank.multi_province import mainline_household_runtime\`且不调用任何公开solve方法；额外九源单独标记\`EXPLICIT_NINE_IMPORT_ONLY\`。原生与adapter模式分报。真实runner正向涵盖五条准确Git read-only child及nonce/exit、Job与双PIPE、reader join、reap、超时/负例和前后源码hash；若修改Job/N13关键机制应在本轮额度内重测dummy。
**E. E1/E2/E3判定**：E1包括Python/stdlib版本探针期望、path、普通适配器、传输格式、台账实现、fixture/测试oracle、runner工程I/O等**所有已授权新scratch中的普通工程问题**，允许Codex自主循环修复至预算/退出门，无需逐项回报Owner。E2仅对写前路径身份不可信、冻结源码或导入来源不能认证、实际未授权文件读写、预算越界/流式截流不可控等停止相关危险行为；能在任务剩额内通过**事先允许的安全fallback**修工程bug则可自行继续，绝不可事后把已发生超限追认为合法。E3对实际科学求解、真实C8读取、修改受保护资产/经济方程、未授权新子进程、实际危险外联、泄露凭据等立即STOP并向Owner报告。不得以“有备份”自动免门。

## 四、一次性长任务资源（不是命令/脚本微审批）

本次为独立的新总预算，与上一任何STOP都无结转：
- **总工作墙钟≤8小时**。**所有工程Python及其衍生Python子进程合计≤24次**（包括负例、失败与重试；不得再拆每类2次额度），单工程Python进程≤10分钟，非科学模型求解进程；必要的Git/PowerShell/Node受限工程辅助手段在总wall与磁盘预算内自主调试，**不设置通用PS批次数、测试轮数微上限**，但需真实记录所有外部process/PID及出口。超时/失控立刻Job取消/回收，不允许耗尽总量之后新开任务借旧额度。
- 现有Stage A Git对象读取仅限冻结commit/tree及白名单身份/70 raw blobs和五child元数据；新scratch非Git所有工件总≤**128MiB**，预留≥8MiB用于异常/终态first/final/receipt；累计认证Git raw stdout数据通道≤**16MiB**；诊断stdout/stderr≤**1MiB/子进程**，实时限流。工程Job RSS若可测应有界报告，单进程目标≤1GiB，意外持续上升或OS失控即停止并披露实际值；RSS无法取得标UNKNOWN。
- 允许对紧邻前三轮已明确授权身份的工程scratch只读提取**已有sourceIndex指向的最多24个不同小文件，实际重复读取总字节≤8MiB**；不允许全盘递归搜索或改写旧seal；如缺索引，允许对单个最新旧根至多一次depth0元数据盘点≤32项以确认精确源身份，不以相似文件名冒充真实执行字节。历史runner raw缺失继续\`UNVERIFIABLE\`。
- **科学调用数严格0**：HA/HJB/KFE/selector/scalar-root/outer GE/IRF、两省稳态、31省现实经济计算、真实C8/2017/2018/B3、MATLAB求解、\`solve_conditioned_household\`及其它公开求解API **全部不授权**。真实runner仅限import-only与进程/IO工程smoke；\`model_activation=False\`、\`Results FALSE\`、\`V011 NOT_STARTED\`。
- 所有当前任务原始first/final保留真实可取得字节、统一run_id和单向hash引用；原final若有偏差只能追加清楚标识的更正派生体，不覆盖原final。不补造旧B/S/L20 first/raw/run_id、原被拒sanitizer材料、历史脚本执行hash。资源账未证实以UNKNOWN标示，不把“有hash”当原始字节网页已复算。

## 五、一次安全交付，GitHub只是证据通道

**交付优先级：真实M1工程结果和可审源字节身份先行，GitHub连接/临时分支发布可选且不阻塞已合法取得的本机工程成果。** 准备最后输出一份简洁\`V010_M1_V13_CONSOLIDATED_ENGINEERING_EXIT_RESULT\`（推荐≤6KiB）：冻结task/model SHA、每个实质退出门状态、最早失败与本任务内修复摘要、数据流与日志流/ledger累计账、canonical native或adapter身份/原run bytes、九模块、runner Git child/Job/N13、保护与残余风险、first/final/manifest各原字节SHA与UNKNOWN、科学0、最终资源/STOP状态。结果最高只能\`ENGINEERING_CANDIDATE_AWAIT_ASTRA_REVIEW\`，不能Codex自授科学PASS。

若新任务工程运行具备安全证据发布条件，授权**唯一新独立远端review分支**\`review/ch5-temp-v010-m1-consolidated-20261017\`，远端tree仅新增\`_review_tmp/ch5/v010-m1-consolidated-20261017/\`路径；候选sole parent必须为**本任务首次发行Commit**。本地不得物理创建\`_review_tmp\`目录到任何工作树/index/scratch；仅项目外非共享\`git --bare\`objects、无checkout/worktree/hardlink/alternates。四个白名单非可执行UTF-8/LF静态文件：\`result.md\`≤32KiB、\`manifest.json\`≤128KiB、\`engineering_evidence.json\`≤128KiB、\`runner_candidate.txt\`≤256KiB（仅经认证且脱敏的工程runner/adapter源文本，不是模型源码/自动执行授权）。manifest记录其它三个公开文件的hash、大小、raw-vs-derivative与本地原bytes可验等级，自身SHA单独列交付摘要防循环。原完整argv/路径、token、SSH key、真实C8数据、原日志、历史拒绝材料不发布。

Codex只用Owner既有SSH Key、\`ssh.github.com:443\`严格host身份，不用PAT/改global配置，首先确认ref不存在且固定parent tree/blob可完全到达、审4文件通过严格sanitizer。**唯一普通nonforce push≤1次，SSH精确ref预查≤1、完整parent对象fetch≤1、远端ref readback≤1**；失败\`LOCAL_ONLY\`且不重试/ref更名/force、不切换到main或模型分支，也不抹去工程中已真实获得的证据。独占bare objects≤2GiB另计。Astra远端独立核验后依Owner协议先归档正式必要证据再清理仅本轮远端白名单文件并回读；Git历史仍可保留原候选字节。

## 六、完成定义与交付 STOP

逐项作状态而不是一枚总PASS：
- \`SOURCE_IDENTITY\`：70/70真实raw哈希和模型Git身份；raw数据流/普通日志分账实时限制可信。
- \`ENGINEERING_LEDGER\`：一次长任务内的进程计费和失败/修复链连续、原始证据不覆盖。
- \`CANONICAL_IMPORT\`：\`NATIVE_UNMODIFIED_PASS\` / \`SCOPED_ADAPTER_ONLY_PASS\` / \`BLOCKED\`；有真的成功返回和实际module名单才能称PASS。
- \`NINE_MONITORED_MODULES\`：canonical自然加载与显式白名单分别认证。
- \`REAL_RUNNER_IO\`：真实Git五children、Job/双PIPE/reader/reap、正反测试；N13可复用前次本机报告级证据或在本轮关键机制改动后补验。
- \`REMOTE_EVIDENCE\`：GitHub独立安全发布/纯LOCAL_ONLY，不因传输失败把本机工程诊断写成不存在。
- \`SCIENTIFIC_STATE\`：HA/HJB/KFE、steady state、GE、IRF、Results全部NOT_RUN；未来须Owner另批科学任务。

本长任务一旦STOP，未用额度全部关闭；**无后续微任务自动签发**。结束\`WAIT_ASTRA_V010_M1_CONSOLIDATED_ENGINEERING_REVIEW / STOP\`，Codex集中交付等Astra验收，不自行启动科学HA/V011。

原\`A16 FAIL_CLOSED\`、\`window UNACCEPTED\`、\`C9 PAUSED\`、\`CALL_LEDGER UNRESOLVED\`、\`real C8 A–D REQUEST_ONLY\`、旧FAIL_CLOSED/first缺字节永久照旧。
