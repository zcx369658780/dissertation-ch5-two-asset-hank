# 第五章 V010：Owner 风险边界、既有双备份、GitHub SSH 与 Python Loader 决策（2026-10-16）

**Authority：Owner直接决定风险/备份范围，并将实际工程 Python Loader 方案交由 Astra选择；Astra确定以下新工程设计基线。**
**生效范围：**V010下一项限域`ENGINEERING_ONLY` **导入与身份工程预检**及其后新任务的默认架构建议。**不**自动授权任何HA/HJB/KFE/GE/IRF、真实数据、Results、V011，也不追改既有冻结任务或历史失败。具体每轮Python进程/科学资源仍以未来单个固定任务为准。

## 1. Owner 的实际风险/备份决定

Owner于2026-10-16明确确认：
- **本科研项目没有保密需求**；不为模型代码/科研报告临时审阅建立额外的保密设施或强制高保密安全沙箱。
- 既有备份是**本地C盘备份＋GitHub备份**；C盘和D盘是**物理上两块独立SSD**。Owner认为这两层足够。**不增加第三套备份**，不把Windows VM快照等当新常规备份要求。
- Codex GitHub连接通过Owner现有**SSH key**；以经独立验证的`ssh.github.com:443`路径或严格等效固定SSH凭据/known_hosts为默认，不需要PAT，不改global/system Git config，不外传private key。
- **隔离环境中的Python Loader由Astra决定**，按既有接受的V010科学合同与最新工程风险适配，优先使项目恢复实质进展。

以上是Owner的资源/机密性风险取舍，**不等于已经证明C盘实际备份在某时刻完全可恢复**；GitHub远端备份只能覆盖其确实存储的已提交对象。物理两SSD也不保证应对同一OS进程的恶意同时修改，因此不把双备份宣传成OS sandbox。

## 2. Astra 选择：轻量Windows工程隔离＋受认证源码Loader，而非强制完整VM

对于**仅ENGINEERING_ONLY的受界import smoke**，选择：
1. 复用**原Stage A独立、只读Git身份根**，固定源模型commit `94de4501dec051b969bee9d852eba2d4591f30ef` / tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5` / sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`；原冻结九源码以及三个真实非空`__init__.py`身份不可改。原Stage A clone不能checkout/fetch/变更index。
2. 在**全新项目外隔离scratch**中创建只读`source_assembly_root`，优先从固定Git raw blobs恢复全部70份`src/ch5_two_asset_hank`的**真字节原样文件**（合计约1.1MB），完整原包目录、三真实非空init；`pyproject.toml`单独证明源码第三方依赖声明。**70份物化不是70份必须import**，真实加载仅以受审批入口和九份白名单作有限工程预检。原科研项目工作树/旧模型Git索引/受保护dirty树均不可写。
3. 由单个新鲜、**非提权**的Windows工程子进程以受控绝对解释器`-I -B -S -X utf8`（若环境有已验证等效隔离，可给审计证据）运行，显式允许**精确认证的Python/stdlib及现有NumPy/SciPy site-packages路径**，不改全局环境、不在本任务pip联网安装、不修改原C盘备份；原模型包只能通过`VerifiedFinder/VerifiedLoader`从装配源根导入。先在PowerShell静态检查第三方包可用的文件/哈希，若缺失STOP，不绕到原污染env。
4. 保持`GitGate`在**只读git_identity_root**对真实五条Git只读children做nonce/audit/exit/reap绑定。将`VerifiedFinder`的源码读取根显式改为`source_assembly_root`，用`Git fixed commit/tree/path/mode/blobSHA1/size/SHA256`及before/end readback精确绑定。源装配前、导入前后均验raw字节；无自动pycache。Windows路径防混淆、源目录/文件不可reparse、源根无同用户不可信并发写入的证据必须做工程检查；不能因`git_root != source_root`而删除身份门。
5. `VerifiedLoader`区分`LOADING`与`EXECUTED`，**必须在真正`exec_module`成功返回之后**才能记录已加载。审计真实`module.__file__ / module.__path__ / spec.origin / loader / sys.modules`身份；先执行冻结`from ch5_two_asset_hank.multi_province import mainline_household_runtime`的入口导入，额外需认证九个监测模块时只能在已经审查的白名单内显式做`IMPORT_ONLY_NINE_SMOKE`，不得把它伪装成原入口自然加载九个、不得调用`solve_conditioned_household`或任何科学函数。
6. 原Windows Job Object、真实五Git child、双PIPE有界、外部PID/超时/RSS/产物账、日志错误封存、N13与活子进程实际超时负例仍按**独立工程验收**执行；只有项目新任务实际授予预算后才可启动。保留`ONE_HA` **硬拒**，不更改任何原模型算法/经济参数/网格/阈值。

**明确风险归类**：这是一种受界的**`TRUSTED_WORKSTATION_ENGINEERING_CONTAINMENT`**，**不宣称`OS_NATIVE_SECURITY_SANDBOX_VERIFIED`**。受信任但含NumPy/SciPy native库的import可能访问当前Windows进程可访问的文件/注册表/环境，Python audit hook/Job不能独立阻断所有native IO或恶意DLL。Owner降低的是**保密/备份级别要求**；如发现实际模型非预期修改、native读写危险、目录完整性无法证明，必须STOP，不能因“不需保密”忽略原数据/代码防误写。此前`IMPORT_GUARD_OS_NATIVE_ISOLATION_UNRESOLVED`作为**未认证native sandbox的真实事实仍然成立**；对本次明确受界工程import-only可由Owner接受残余风险继续，但不能将该结论作为科学HA、真实C8或Results的OS安全PASS。

## 3. GitHub Git-only审阅交换的SSH与本地工作树禁令

- Owner最新批准的[GitHub脱敏临时交换协议](CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md)继续严格有效：`_review_tmp/ch5/<task-id>/`**仅在远端独立review分支的Git Tree**，不得出现于本地任何项目工作树、模型源码树、既有.git index/staged、main/治理/模型branch。代码审阅完成先治理永久归档再删远端临时审阅文件并回读，Git旧Commit历史仍保留。
- Codex与GitHub远端通信**优先使用已有SSH key + GitHub SSH-over-443**（例如可信配置下`ssh://git@ssh.github.com:443/zcx369658780/dissertation-ch5-two-asset-hank.git`），严格验证host key；不要求PAT/新token或修改global/system Git config，SSH私钥与已载入agent凭据都不得纳入回执/临时Git提交。Astra现有GitHub连接器用于独立远端readback/永久审议/清理，不代表Codex改变SSH连接方式。
- Codex只可在**原项目工作树之外**的新独占`bare Git`发布元数据对象库中通过SSH创建独立review分支，`core.bare=true`，无checkout，不使用`git worktree add`、共享.git或alternates。创建含`_review_tmp`路径的**远端commit tree**需要对应Git对象完整，禁止重用历史`--depth=1 --filter=blob:none`残缺基线而导致`write-tree`对promisor缺blob。若独占bare准备/认证失败，即`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED / STOP`，不擅自补取/重试。
- 本次已有的C盘备份及GitHub备份**不会**因工程临时产物自动获得新覆盖证明；不要清理、重建或重写Owner C盘备份。后续可单独只读核验备份存在性，但本决策不授权替代Owner备份管理。

## 4. 仍冻结的科学权威与后一工程门

上一V010`SOURCE_ONLY_GUARD_DESIGN_PARTIAL_WITH_OPEN_GATES__INDEPENDENT_DOCUMENTARY_LIMITED_ACCEPT`及[独立主审](../versions/0.0.10/import_guard_dependency_design_github_primary_review_20261016.md)保留。上一SOURCE_ONLY图70源/42词法候选、20 UNRESOLVED/14 SIDE_EFFECT_RISK/8 PURE_DEFINITION、第三方native未知与源双根设计为输入，不重新规划宏观模型。

原V010计划commit `bf091da33d59293f147d52c11580327d3ac2a85d` / blob `85138d8859d53295262fe13bf5bc277bca95ed3f`，corrected HA至今`UNTESTED`，`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、真实C8 A–D REQUEST_ONLY、原8dirty/index/staged/untracked/ignored/外Git common-dir/全部旧失败证据及旧模型预算（两次单点Python各1/1、首次输出超额等）完全不变。新阶段如要工程Python进程必须通过新固定任务明确分配；**任何科学模型求解必须Owner再次独立授权**。

**下一授权动作：**发布一个紧凑的`V010_ENGINEERING_ONLY_TRUSTED_LOADER_INTEGRATION_PREFLIGHT`任务，集中完成上述装配与有界import工程smoke，结果再由Astra独立审查。不能自动进行HA。
