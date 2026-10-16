# 第五章 CURRENT：V010工程Windows preflight任务已签发

> **2026-10-16 最新独立审议优先于下方旧任务签发状态：** 原唯一ACTIVE `V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT` 已由Codex以 `ENGINEERING_PREFLIGHT_FAIL_CLOSED` 交付并STOP。GitHub review candidate `416cff6c00d2b865c3e9dda4088242d2b80969ce`，tree `1d5bc390774d68ea619f6ad263c99d0090486b37`，独立查证仅3白名单文件、sole parent `343c22132deb23ba6d913d70e132b43a00b95f1d`；[Astra独立审议](versions/0.0.10/runner_io_engineering_preflight_fail_closed_primary_review_20261016.md) 判为 `A_STAGE_GIT_REF_SCOPE_FAILURE`：隔离clone只取治理分支，未取得有效模型分支对象，导致checkout 128。远端模型分支 `codex/ch5-v010-matlab-first-20261015` 的HEAD/Tree真实存在。新工程Python 0/4、科学HA0属Codex回执，69例全部未评估。本轮当前没有后继ACTIVE执行任务，`WAIT_OWNER_FRESH_A_STAGE_GIT_OBJECT_REACHABILITY_AUTHORITY / STOP`。旧未用工程余额不能越过STOP自动继续，全部V010科学冻结/历史预算/保护不改。下方“任务已签发/待交付”是原发布时间快照。

更新：2026-10-16（Asia/Shanghai）。
**状态：`V010_ENGINEERING_ONLY_WINDOWS_PREFLIGHT_TASK_ISSUED__WAIT_CODEX_DELIVERY__NO_SCIENCE_RUNTIME`。**

Owner已在本会话正式授权由Astra确定边界的**ENGINEERING_ONLY Windows preflight**，并非授权第三次单点HA。唯一ACTIVE为 `V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT`；[冻结任务](versions/0.0.10/runner_io_engineering_only_windows_preflight_task_20261016.md) 在发行commit `343c22132deb23ba6d913d70e132b43a00b95f1d`、tree `2fbb740ba42e2367fb99de05a11eb533829ea72b`、blob `08fed792ee19329313dfc7402fa174035805a345`。本会话任务**已发行，不得再次下发**。下一个回执为 `V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT_RESULT`，停于 `WAIT_ASTRA_V010_ENGINEERING_PREFLIGHT_REVIEW / STOP`。

**新工程资源隔离账**：工程Python进程≤4（AST/结构≤1、负例harness≤1、真正Windows runner≤2，合计≤4）；每进程外部wall≤180s，任务总≤3h；每个真实runner最多5条只读Git child；新工程增量artifact≤16MiB，独立不共享原common-dir clone≤2GiB。工程外部启动器必须进程创建前持久扣账，不因runner I/O失败漏记。`HA/HJB/KFE/selector/root/GE/IRF/MATLAB/pytest=0`；模型代码不可修改。完整准确限制以发行任务原件为准。

**原静态任务已交付且限域审议完成**：review candidate `c207e866cf70d9d5ae6fb245f43cabfdeac1d32b` / tree `b4ba5b7939653a0cdb8524fa82743d9634d79083`；原review [独立静态审议](versions/0.0.10/runner_guard_io_offline_github_primary_review_20261016.md) blob `c8f4b938c87fd3ea7b0443fa2be32793e5733917`，`STATIC_DESIGN_READY=CONDITIONAL_LIMITED_ACCEPT`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`ENGINEERING_RUNTIME_NOT_RUN`。46主例＋23变体定义可读，但前一轮未执行；新preflight尚无Codex执行结果。

**原科学边界**：修正MATLAB错误并Python恢复两资产HA→多省顺序单轮→原GovInv收益边界0.9/1.1与Zt有界迭代→冻结目标GDP≤1%验证→原lagged-NKPC递推；目的地工资税扣一次、家庭人均/财政省总量与家庭/firm劳动分账、same-S、lagged raw ra0、max_phi=.3。正式计划commit `bf091da33d59293f147d52c11580327d3ac2a85d` / blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；原模型candidate `94de4501dec051b969bee9d852eba2d4591f30ef`；原单点manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7` 均不可变。

**旧证据与消耗不重置**：原实施报告pytest4/6、science driver1/4、HA1/26、cells1626、roots1642；单点两次预检各Python1/1、HA0，首笔GBK异常产物43519638B、超旧32MiB 9965206B，第二笔argv守门117446B。单点corrected HA仍`UNTESTED`，原双省首HA checkpoint2/F25 `NO_ADMISSIBLE_POLICY`，KFE/GE/IRF没有合格运行。原受保护8dirty/index/staged/外Git common-dir/untracked/ignored及原失败回执不覆盖，真实C8/2017/2018/B3与旧V009失败数组不访问。

`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。长期`CH5_ASTRA_WORKFLOW_V1.2`不变；GitHub同步不等于本地QMD/Basic Memory同步。[交接原快照](docs/CH5_CONVERSATION_HANDOFF_20261016_V010_RUNNER_IO_OFFLINE_PENDING.md)仍为固定历史权威，不用于覆盖最新ACTIVE。
