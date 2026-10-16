# 第五章动态总目录（2026-10-16 V010 E0工程修复任务已签发）

**当前唯一ACTIVE_TASK=`V010_E0_LAUNCHER_UINT32_AND_TEMP_MKTREE_CORRECTION`**；固定发行commit `e474c0d25a7351b7510f6a9ba914cd8733dceffc`，任务Git Blob `a3683c751acf08d49d700422a63f264b61130e78`。Owner在新会话要求交接后直接发布下一任务，当前只准E0 PowerShell/新bare mktree的受界工程修复，**Python/runner/HA/GE/IRF/真实C8新许可均0**。旧Trusted Loader E0 FAIL_CLOSED LOCAL_ONLY已STOP，旧预算不结转。签发≠运行≠科学通过。

| 用途 | GitHub权威入口 | 现时状态 |
|---|---|---|
| **唯一ACTIVE新任务** | [V010 E0 Launcher + mktree纠错](../versions/0.0.10/e0_launcher_uint32_temp_mktree_correction_task_20261016.md) | 发行commit `e474c0d25a7351b7510f6a9ba914cd8733dceffc` / blob `a3683c751acf08d49d700422a63f264b61130e78`，待Codex交付 |
| CURRENT | [当前状态](../CURRENT.md) | 当前工作状态、权限和科学STOP |
| TASK_CURRENT | [当前任务](../TASK_CURRENT.md) | 精确执行/输出白名单 |
| **上一轮独立主审** | [Trusted Loader E0 FAIL_CLOSED](../versions/0.0.10/trusted_loader_e0_fail_closed_local_only_primary_review_20261016.md) | Blob `d9d5a3ea38fcff89633ce09fdf0d97d9e9e61293`，本机原证尚未直接读取 |
| 前轮长期交接 | [2026-10-16 E0 handoff](CH5_CONVERSATION_HANDOFF_20261016_TRUSTED_LOADER_E0_LOCAL_ONLY_STOP.md) | Blob `7865222ca9966720b9cc335a4e41facfc9a7fc8e`，交接时ACTIVE=NONE属历史 |
| 前一STOP工程task | [Trusted Workstation Loader](../versions/0.0.10/trusted_workstation_loader_engineering_preflight_task_20261016.md) | 发行commit `01129efd5220683d415bd1486f23f6ecd068cb53`、blob `1e6757fd235fd96d8b08130ca3fefb3b602c413c`，禁止重发 |
| Owner备份、SSH与Loader | [上位风险决定](CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md) | C盘独立SSD现有备份+GitHub；SSH key/443；可信双根，不强制VM |
| 临时审阅 | [remote-only review协议](CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md) | `_review_tmp`仅远端新review Tree，不进本地项目worktree/index |
| 工作流 | [V1.2](CH5_ASTRA_WORKFLOW_CURRENT.md) | Codex自主限域工程/Astra独立审议、停止条件严格 |
| 科学决定 | [SCIENTIFIC_DECISIONS](../SCIENTIFIC_DECISIONS.md) | 原MATLAB修错主线不变 |
| 版本登记 | [VERSION_REGISTER](CH5_VERSION_REGISTER_CURRENT.md) | V010中、V011禁启 |
| 长期知识 | [WEB_KNOWLEDGE](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md) | 时间序列与保护锁 |

冻结V010科学plan commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、模型代码commit`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`均不改。corrected HA单点仍UNTESTED、FULL_RUNNER_IO_CLOSURE BLOCKED、model_activation=False、Results FALSE、V011 NOT_STARTED；旧原8dirty/index/common-dir、A16/window/C9/CALL_LEDGER、real C8及所有历史账不变。GitHub不证明本地QMD/Basic Memory同步。
