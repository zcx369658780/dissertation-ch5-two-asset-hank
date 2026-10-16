# TASK_CURRENT：V010 ENGINEERING_ONLY Windows preflight

> **2026-10-16 实时最优先：`ACTIVE_TASK=NONE__WAIT_OWNER_NEW_A_STAGE_AUTHORITY`。** 上一任务 `V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT` 已交付 `ENGINEERING_PREFLIGHT_FAIL_CLOSED` 并终止，不再处于执行中。Review candidate `416cff6c00d2b865c3e9dda4088242d2b80969ce` / tree `1d5bc390774d68ea619f6ad263c99d0090486b37`，独立审议[全文](versions/0.0.10/runner_io_engineering_preflight_fail_closed_primary_review_20261016.md)。阶段A clone未拿到冻结模型对象，checkout exit128、工程Python=0/4(报告)、HA=0、69个静态/变体均NOT_EVALUATED。本审议不是继续执行命令，不产生新工程clone/fetch/Python/科学预算，不重复旧任务；Owner未来决定是否授权单独Git对象可达性修复。下文历史ACTIVE字段为任务发出时点记录。

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=`V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT`**。
**STATUS=`OWNER_APPROVED__TASK_ISSUED__AWAIT_CODEX_RESULT`**。
**PERMISSION=`ENGINEERING_ONLY_WINDOWS_PREFLIGHT_BOUNDED__NO_HA_OR_SCIENCE`**。

唯一任务原件：[runner_io_engineering_only_windows_preflight_task_20261016.md](versions/0.0.10/runner_io_engineering_only_windows_preflight_task_20261016.md)，发行commit `343c22132deb23ba6d913d70e132b43a00b95f1d`，tree `2fbb740ba42e2367fb99de05a11eb533829ea72b`，blob `08fed792ee19329313dfc7402fa174035805a345`。已经正式发布，**不得二次派单**。Codex在新的隔离scratch集中完成单轮预检，严格从已批准文本candidate `c207e866cf70d9d5ae6fb245f43cabfdeac1d32b`及冻结模型代码 `94de4501dec051b969bee9d852eba2d4591f30ef`构造，只修改新的工程runner与最小harness，不触原模型算法或保护资产。

核心预算：工程Python总≤4（AST≤1、isolated harness≤1、真正Windows runner≤2），每进程≤180s，总任务≤3h；每次真实runner≤5次精确只读Git child；新工程artifact≤16MiB，隔离不共享common-dir clone≤2GiB。全部工程进程**先扣外部持久账**再启动；任何失败/超额STOP。仅允许工程导入/真实Windows Git身份、source bytes、audit形态、I/O/Job回收与负例验证，`HA/HJB/KFE/selector/roots/GE/IRF/MATLAB/pytest=0`，科学进程新许可=0，真实C8读取=0。未来HA需要工程独立验收后再次请求Owner单独授权。

旧ACTIVE `V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_AND_SANITIZED_GITHUB_HANDOFF` 已DELIVERED并由Astra [静态限域接受](versions/0.0.10/runner_guard_io_offline_github_primary_review_20261016.md)，不再是当前派单。旧original任务及失败回执/冻结plan/blob不修改、预算不重置。

唯一最终交付 `V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT_RESULT`，终态 `WAIT_ASTRA_V010_ENGINEERING_PREFLIGHT_REVIEW / STOP`。仅能向新`review/v010-runner-io-engineering-preflight-20261016`安全脱敏发布3种指定review文件，单父为本任务发行commit，普通nonforce一次并回读；脱敏不通过LOCAL_ONLY STOP。不推main、治理或旧review分支，不自主启动HA或V011。旧8dirty/index/common-dir、A16/window/C9/CALL_LEDGER/Results保护保持。
