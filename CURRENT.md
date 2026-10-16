# 第五章 CURRENT：V010 Trusted Workstation Loader ENGINEERING_ONLY预检已签发

2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_ENGINEERING_ONLY_TRUSTED_LOADER_INTEGRATION_PREFLIGHT**。
**STATUS=OWNER_APPROVED__ENGINEERING_ONLY_TASK_ISSUED__AWAIT_CODEX_DELIVERY**。
**RISK_PROFILE=TRUSTED_WORKSTATION_ENGINEERING_CONTAINMENT__OS_NATIVE_SECURITY_SANDBOX_NOT_CLAIMED**。
**SCIENTIFIC_RUNTIME_PERMISSION=0__HA_0__HJB_0__KFE_0__GE_0__IRF_0**。
**NEXT_STOP=WAIT_ASTRA_V010_TRUSTED_LOADER_ENGINEERING_REVIEW / STOP**。

Owner明确决定本项目**不保密**，现有**C盘实体独立SSD备份＋GitHub备份**两层足够、无需第三备份；Codex连接GitHub**使用已有SSH key/SSH443**而非新增PAT。隔离Python Loader交由Astra确定。新[Owner风险与备份/SSH/Loader决策](docs/CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md)发行commit`e15b874b955883e754dee8b3e5543705ed0706a8`、blob`7f1ee509d35343521e79e5df318aa164cd513261`，选择**轻量可信工作站工程import隔离**，不以新Windows VM/严格native恶意代码OS安全沙箱作为工程import-only前置门。现有C盘备份不检查或改写，本地C/D物理分盘事实来自Owner陈述，GitHub代码备份仅对实际已提交对象有效；native副作用残余风险必须准确披露，不能称`OS_NATIVE_SECURITY_SANDBOX_VERIFIED`或放宽科学门。

**唯一当前已发行冻结任务**：[trusted_workstation_loader_engineering_preflight_task_20261016.md](versions/0.0.10/trusted_workstation_loader_engineering_preflight_task_20261016.md)，发行commit`01129efd5220683d415bd1486f23f6ecd068cb53`、tree`75ca195ecc41b8e6fbd7f43a090d22aa4f170dea`、task blob`1e6757fd235fd96d8b08130ca3fefb3b602c413c`。**已经发布，禁止重新派发**。一次集中从固定模型commit`94de4501dec051b969bee9d852eba2d4591f30ef`真实Git Blob在新隔离scratch构建70份原样Python源码`source_assembly_root`（三真实非空init，不改Stage A独立只读Git clone`git_identity_root`），把VerifiedFinder/Loader分离Git身份根与源根；真实五Git子进程仍按原身份/nonce/audit/Job/reap有界回执。修复`LOADING→EXECUTED`正确账，实测canonical入口import与九份受监测模块明确分开标注的**IMPORT_ONLY**身份校验；绝不调用家庭模型科学求解或真实C8。

**独立新工程预算**：最多6工程Python进程（静态/负例≤2、canonical/dry import≤2、真实runner≤2），各≤180s、总wall≤4h，新增非Git工件≤32MiB、项目外独占bare发布metadata≤1.5GiB、模型网络clone/fetch/checkout=0；所有Python先外部持久扣账，失败STOP。**工程Python≠科学Python，后者新授权0**。如可信现有NumPy/SciPy依赖/源根排他性/导入期science guard不满足，报告`DEPENDENCY_BOOTSTRAP_BLOCKED`或`FAIL_CLOSED`，不可通过放开权限或自动pip获取新包取得PASS。

**临时审阅安全交换**仍在GitHub独立review分支`review/ch5-temp-v010-trusted-loader-engineering-20261016`，远端唯一路径`_review_tmp/ch5/v010-trusted-loader-engineering-20261016/`，三份已脱敏文件只存在远端候选tree；本地项目worktree/index/staged绝不出现该临时目录。Codex SSH443通过项目外独占bare对象库存Git metadata，不能用GitHub API/PAT替代其Owner指定SSH链，不改global Git config；Astra用GitHub连接器独立验收、永久归档后删除**远端**临时文件并回读，原Git历史仍保留。旧review候选与历史失败原件都不追改。

前一[Import Guard设计独立主审](versions/0.0.10/import_guard_dependency_design_github_primary_review_20261016.md)为`SOURCE_ONLY_GUARD_DESIGN_PARTIAL_WITH_OPEN_GATES__DOCUMENTARY_LIMITED_ACCEPT`：70源/42候选，20 UNRESOLVED、14 SIDE_EFFECT_RISK、8 PURE词法，尚无Windows/native OS安全证明。上一B–E工程5Git child真实正向回执、68 synthetic PASS/N13未评估、loader因稀疏clone缺init而未闭环，`FULL_RUNNER_IO_CLOSURE=BLOCKED`。原V010冻结plan commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、GovInv0.9/1.1、同S/lagged raw-ra0、目的地工资税一次和原lagged-NKPC递推不改。corrected单点HA仍UNTESTED、model_activation=False、Results FALSE、V011 NOT_STARTED。旧实施pytest4/6、driver1/4、HA1/26、selector1626、roots1642、两笔单点Python各1/1和首次存储超额9965206B、旧工程Python3/4与runner1/2余额不结转。A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER UNRESOLVED、真实C8 A–D REQUEST_ONLY及原8dirty/index/外common-dir/旧失败根保护永久保持。GitHub同步不等于本机QMD/ChatGPT Memory即时同步。
