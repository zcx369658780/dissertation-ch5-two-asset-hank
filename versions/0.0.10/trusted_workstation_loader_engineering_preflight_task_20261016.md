# V010：Trusted Workstation VerifiedLoader 集中工程集成与受界Windows import预检

**唯一任务ID：`V010_ENGINEERING_ONLY_TRUSTED_LOADER_INTEGRATION_PREFLIGHT`。**
**权限来源：**2026-10-16 Owner明确决定“本项目不需要保密，C盘与D盘是两块物理SSD，既有C盘备份＋GitHub备份够用；连接GitHub使用SSH key；隔离环境中的Python Loader由Astra决定；请继续。” Astra选择受界的**可信工作站工程隔离**（不是VM/高保密安全沙箱），并为本**ENGINEERING_ONLY**预检冻结独立、不可自动结转的工程资源。
**本任务合法目标：**一次集中修正/验证由固定Git模型源码构造的可信导入链，重点实测真实非空三`__init__.py`与九份受监测模块的Git来源、`VerifiedFinder / VerifiedLoader`、五Git子进程和实际Windows受界工程过程。**不启动单点corrected HA，不运行HJB/KFE、selector/root/GE/IRF/真实数据，不更改原学科数学，不自动V011。**
**任务发行commit/tree/blob**：签发后由后续`TASK_CURRENT`登记，Codex须读取此文件在固定发行Commit中的准确Git blob，而非信赖动态HEAD。不得二次发布本任务或修改冻结任务原件。
**终点**：`WAIT_ASTRA_V010_TRUSTED_LOADER_ENGINEERING_REVIEW / STOP`。Codex不自授`FULL_RUNNER_IO_CLOSURE=PASS`、A16解除、HA/科学权限。

## 0. 前置冻结与Owner风险接受记录

- 仓库`zcx369658780/dissertation-ch5-two-asset-hank`，治理`migration/astra-workflow-20261012`。
- **本任务上位风险与技术选择**：[CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md](../../docs/CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md)，Owner/Astra正式决策commit `e15b874b955883e754dee8b3e5543705ed0706a8`、blob `7f1ee509d35343521e79e5df318aa164cd513261`。不新增第三备份、强制Windows VM或高保密机制；C盘现有物理独立SSD备份**不得更改/清理**，GitHub已有备份照旧。**不得把这项风险接受写成`OS_NATIVE_SECURITY_SANDBOX_VERIFIED`或放宽数据/模型防误写门。**
- 冻结模型代码commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`、唯一parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`；冻结V010科学plan commit `bf091da33d59293f147d52c11580327d3ac2a85d` / blob `85138d8859d53295262fe13bf5bc277bca95ed3f`，fixture blob `40915658d93403cfc21b33a6b864b332b7857749`，单点input manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`，全部不改、不计算。
- 上一[import guard独立限域主审](import_guard_dependency_design_github_primary_review_20261016.md) blob `8d2dad9d4e915fceda498329434e0956300c89e5`：42冻结模型入口候选path/Blob/bytes，20 UNRESOLVED、14 IMPORT_TIME_SIDE_EFFECT_RISK、8 PURE_DEFINITION词法标签，35 external（含6 NumPy/SciPy native相关）、3真实非空包init；双根、binding+native隔离仅原**SOURCE_ONLY设计**，`IMPORT_GUARD_OS_NATIVE_ISOLATION_UNRESOLVED`保持未认证，不能用报告代替本轮执行。上轮[Windows B–E工程审议](runner_io_windows_be_github_primary_review_20261016.md)blob `67c15e010c4a90b9773899cd699222d756fe5772`留存：68 synthetic PASS/N13 NOT_EVALUATED、五Git child正向、loader被Stage A稀疏clone缺init阻断，工程Python3/4和runner1/2余额不结转。
- 原最后`review_runner_io_windows_be_static_draft_20261016.txt`固定review commit `9bcd61fc88ace3b8e2c1c07753c610e2e4b5c75e`，Blob `79b8e6b8eb9bd7138c3c23aa6a997a0bc1272d3e`，**不是可直接运行的自动任务**；可在本轮新隔离scratch复制其中runner/launcher的**工程部分**作为受审起点，修正loader根、状态账与相关有界I/O，不改原模型的70份源代码或科学数学。
- Owner最新[GitHub临时审阅协议](../../docs/CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md)及V1.2强制约束：脱敏`_review_tmp/ch5/<task-id>/`仅能在**远端review分支Git Tree**，**不得加入任何本地项目worktree/index/staging或在其中创建此目录**。Codex对GitHub Git读写只使用已有SSH key，首选SSH443，不要求PAT、不修改global/system Git config；Astra通过连接器独立远端验收和清理。

## 1. 许可对象、隔离策略与绝对禁止

- **本次仅允许可信工作站ENGINEERING_ONLY**：新独占项目外scratch `D:\ProjectTemp\ch5_v010_trusted_loader_engineering_20261016_01`，不存在/reparse到受保护资产即STOP。仅新增独立`source_assembly_root`（无.git）、`output_root`、工程runner和有限外部进程/字节账；模型70源码需从精确固定commit Git raw blob恢复，保持三份**真实非空init**及全部原字节、模块目录结构。**读取和恢复70份不是运行全部70份**，程序只按任务批准的导入路径加载。装配过程不得引用实时HEAD或旧未验源副本。
- 已通过Stage A的**只读`git_identity_root`**必须实际定位在原独立Stage A clone，并当场核HEAD/tree/parent/common-dir/object/alternates，不能读写旧受保护`D:\ProjectTemp\c5k1bturn56`、其8 dirty tracked/index/staged/untracked/ignored/外common-dir、旧失败证据目录、真实C8/2017/2018/B3、历史V009坏数组。原Stage A clone Git objects/worktree/index/config全程只读，无新模型`clone/fetch/pull/checkout/reset/clean/sparse-checkout`、不共享Git worktree/common-dir。若冻结对象不可达，STOP，不能补取。
- source assembly从模型Git blob独立恢复、先SHA1 Git blob header/size/SHA256逐项认证，目录树排除symlink/reparse/UNC/ADS/hardlink及项目保护路径别名，不做源文件LF转码；完成后为本工程进程提供**真实只读源根及可信排他写入控制**（受信任同一用户目录替换无法有效阻断时降级`SOURCE_ROOT_OS_WRITE_EXCLUSIVITY_UNKNOWN`并STOP，不能以仅设readonly attribute宣称完整OS安全）。C盘备份不作为scratch、不可自动修改；不能读取任何真实数据/生成任何科学结果。
- 子进程使用固定可信`python.exe`、非提权、受控环境，建议`-I -B -S -X utf8`；只允许被独立哈希认证的Python/stdlib目录与**现有**NumPy/SciPy site-packages和必要native DLL受控入口（在`-S`下只能显式按审查的路径导入，禁止自动site/.pth）；记录准确解释器/位数/包版本和文件身份、环境/sys.path限制。不得pip/install/从网络获取软件、更改全局Python依赖或关闭原守门。若当前环境无法可信满足已有依赖，`DEPENDENCY_BOOTSTRAP_BLOCKED / STOP`，不为PASS切换不明环境。
- **残余风险明确**：此为`TRUSTED_WORKSTATION_ENGINEERING_CONTAINMENT`，不是强制VM/AppContainer/恶意native进程OS沙箱；只准 import-only 工程诊断且模型冻结源码来源可信。Python audit hook/Job不能证明阻断一切native文件/网络副作用，标`OS_NATIVE_SECURITY_SANDBOX_NOT_CLAIMED`。出现疑似保护路径访问/写入、意外启动网络子进程、import-time科学求解或严重来源不明即STOP，不能因“不需保密”忽略代码/数据完整性。

## 2. 集中工程执行流程（各门失败立即STOP）

**E0 0-Python准备门**：PowerShell/git read-only核冻结task/当前授权/Owner备份策略、Stage A独立git身份证据、完整70源码raw Git blobs可读取，`pyproject`只作最低版本声明，不伪称已有包安装可用。新scratch创建在保护根外、外部Python启动前持久额度扣账/应急预算保留；对原C盘备份**不执行检查/修改**（Owner有备份即可，不新增阻塞依赖）。构造70源码原字节只写新独立装配根，预装配与封存后全源70/70 SHA1/SHA256/size/relative path复核，Git source map从固定commit tree认证。E0不运行Python，失败STOP无Python扣账。

**E1 严格工程Loader修正及静态检查**：只修改新工程scratch中的runner/VerifiedFinder/VerifiedLoader/gate-binding/harness和启动器。将GitGate的根继续只读锁在原Stage A独立Git clone，但finder加载只从新装配源根；保持原4真实Git身份child＋第5`ls-tree -r <frozen commit> -- src/ch5_two_asset_hank`这五个准确只读子命令、audit nonce及bounded PIPE/Job/reap契约；不得用预设成功布尔值代替四身份/第五inventory。按`Git fixed commit/tree/parent+relative module path+mode100644+blobSHA1+bytes+SHA256+begin/end`绑定，`VerifiedLoader.exec_module`用**同一已认证raw byte buffer编译执行**，不重新按不可信路径开文件。路径/句柄同一性不能静态证实时标具体`TOCTOU_TRUST_LIMIT`；原`finder.loaded`必须在`exec_module`**成功返回后**才记`EXECUTED`，异常`LOADING_FAILED`不得误记成功。审`module.__file__ / __path__ / spec.origin / loader / sys.modules`路径及module对象身份；禁止预加载`ch5_two_asset_hank`。`ONE_HA`和任何40位“科学授权字符串”无条件硬拒、调用solver/selector/root/HA/KFE的运行入口仍为0。
- 首先只读AST/compile工程runner**源码文本**，不import/执行模型；synthetic负例包括source byte corruption/九文件缺失/多余模块/原包init重写/重复hook/错误Python模式和Git额外child，审计写日志和配额合规。

**E2 真实Windows ENGINEERING_ONLY import smoke**：新的受界工程进程先对**原canonical入口**
`from ch5_two_asset_hank.multi_province import mainline_household_runtime`
执行**仅import**，明确记录真实被加载的冻结模块列表及three init eager imports、native/stdlib依赖状态；不调用模型公开API或单点HA。原九模块如未全部在canonical入口自然加载，记录`CANONICAL_ENTRY_NINE_NOT_ALL_LOADED`（不能把失败伪称九个全部自然加载）。在独立、明确标签`ALLOWLISTED_NINE_IMPORT_ONLY_SMOKE`下，仅允许固定九受监测模块额外显式import作工程身份认证；九源每个需真实`VerifiedLoader`成功返回后`EXECUTED`、`__file__/spec/loader/sys.modules`和实际raw字节hash二次认证。**不要“为凑九份”私自import超出已核42静态候选**；若九中某入口含未授权import-time科学计算则STOP。
- 记录 5 个真实Git children 及恰好对应的5组audit nonce/argv Windows string/list2cmdline/exit/stdout边界/Job分配/reap/reader join证明；每child≤30s，双PIPE有界，不能只证明退出0。
- 工程stdout/stderr/Writer正常与故障封存、外部进程账及终态回执必须做write-before-quota和fail-closed；已有前轮正常路径证据可引用，但新双根和实际import期间的新异常不得凭旧审阅推定已测。
- N13及真实活动进程timeout/descendant kill-reap可用**项目外独立dummy child的非模型负例**在本次工程过程预算内验证；若该负例不运行，保持`NOT_EVALUATED`，不得将其当已关闭。Jobs/Hook不是OS filesystem isolation。外部杀进程不得破坏模型源或C backup。

**E3 停止、报告、独立审查**：逐阶段给`PASS/PARTIAL/FAIL_CLOSED/NOT_EVALUATED`，且只在**真实canonical import**通过时声称`CANONICAL_LOADER_IMPORT_AUTHENTICATED`；九源需记录是否为同一真实入口自然加载或单独白名单smoke证据。`LOADER_ENGINEERING_IMPORT_CANDIDATE_READY_FOR_ASTRA`最多表示工程候选达目标，Astra仍须独立读证后给限域接受；`OS_NATIVE_SECURITY_SANDBOX_NOT_CLAIMED`保持为残余风险，科学`HA_SCIENCE_NOT_RUN`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`直到其他独立工程门明确通过。任一关键错误STOP、不给自己追加预算、保留旧失败原证，绝不启动V011。

## 3. 新的一次性资源上限（与所有旧账隔离）

- **工程Python进程最多6个**（成功/失败/终止均在启动前由可信PowerShell外部ledger持久扣账）：纯静态/负例验证≤2、真实canonical/dry import工程smoke≤2、真实runner含五Git child启动≤2，合计≤6；任何二级`python.exe/py/Jupyter/pytest`也必须计数且仍禁止pytest。每个工程Python进程外部wall ≤180s，总工作wall≤**4h**；记录PID/exit/elapsed/max RSS（不可得记UNKNOWN）/唯一脚本SHA256，不自动重启。**新科学Python=0；HA/HJB/KFE/selector/scalarRoots/GE/IRF/MATLAB/真实数据全部调用0**。如工程import本身触发科学函数立即STOP，不可转成HA。
- 新scratch所有非Git新增物理工件累计**≤32MiB（33554432B）**，含真实70源码、runner、harness、stdout/stderr、失败事务、外部账与final/emergency预留≥2MiB；源70约1.1MB不构成追加模型预算。Git前置只读调用≤**150**（模型网络0），真实runner每次Git child≤5；对每条Git审计stdout/stderr/exit/time。
- **项目外独占bare Git临时发布对象库总占用≤1.5GiB**（另列，不算非Git工件，且不可共享原common-dir）。模型原Git clone/fetch/checkout=0；允许仅在发行任务已冻结后通过固定Owner SSH-key认证在bare库里取得**完整**task发布Git基线对象以供单父review（GitHub SSH443；不改全局Git配置/known_hosts安全校验）；禁止重用旧`--filter=blob:none`残缺基线。所有新增工件写前实际计费、不得清理历史失败以“降账”。
- 原实施pytest4/6、driver1/4、HA1/26、selector1626、roots1642、两笔单点各Python1/1且HA0及第一次超过原32MiB 9965206B，前一Windows工程3/4 Python、runner1/2，SOURCE_ONLY任务0Python等历史账全部保留，不结转。科学原V010合同、A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER UNRESOLVED/model_activation=False/Results FALSE/C8 REQUEST_ONLY、原保护8dirty/index/common-dir、V011 NOT_STARTED全部不动。

## 4. Owner SSH GitHub远端临时审阅交付与Astra后续清理

**Owner硬约束：临时审阅目录绝不在任何本地科研/模型/治理项目worktree或Git index出现。** 只可在**GitHub远端独立review分支的树**创建`_review_tmp/ch5/v010-trusted-loader-engineering-20261016/`；本地仅项目外D盘scratch平铺`result.md/manifest.json/loader_candidate.txt`（无`_review_tmp`目录），项目外独占bare对象库无checkout/staged项目index/共享.git。不得通过改`.gitignore`隐藏审阅目录。
- 唯一目标ref `review/ch5-temp-v010-trusted-loader-engineering-20261016`，必须先核不存在；candidate commit**唯一parent是本任务发行commit**，只有以下3个经严格脱敏的远端文件：`result.md`≤32KiB、`manifest.json`≤128KiB、`loader_candidate.txt`≤96KiB（非可执行静态工程源文本，不作为自行执行许可）。不泄露SSH key、token、真实路径、用户隐私或研究数据。
- 连接使用Owner已有SSH key（SSH-over-443），固定远端/known_hosts严格验证；禁止PAT、新令牌、修改global/system Git。最多**一次普通non-force push**；失败则`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED/STOP`，不追加fetch/重试/force。
- push成功后remote readback exact branch/commit/tree/sole parent，三文件GitBlob/SHA256/UTF8原字节/大小及白名单路径。Codex不自授PASS。
- Astra收到候选后从远端独立审阅，**先**永久保存审议/动态状态、远端readback通过，再仅删除本临时review分支里的三份临时文件/创建cleanup commit并远端回读；原候选commit历史不改写。这一例行清理不改本任务科学/工程授权。

**STOP=`WAIT_ASTRA_V010_TRUSTED_LOADER_ENGINEERING_REVIEW / STOP`**。禁止继承此任务额度去运行任何科学HA；Owner不保密/C盘+GitHub双备份选择只用于简化**受界工程import**门，不构成模型经济或科学数字验收。
