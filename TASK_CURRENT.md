# TASK_CURRENT：V010 Stage A 模型 Git 对象可达性修复

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_STAGE_A_FROZEN_MODEL_GIT_OBJECT_REACHABILITY_RECOVERY**。
**STATUS=ISSUED__WAIT_CODEX_DELIVERY**。
**PERMISSION=GIT_OBJECT_REACHABILITY_ONLY__NO_PYTHON_OR_HA_OR_RUNNER**。

**唯一已发布任务**：[固定任务全文](versions/0.0.10/stage_a_model_git_object_reachability_recovery_task_20261016.md)。
- 正式签发commit：`68530b3f121952b4382d08dc9ff964c7f6c7ab75`。
- Tree：`70a7662ba654dff6acbe05e3a8b0444324b8f346`。
- Task Blob：`3688674363aa8a0c45a7a322c9c2098baed62fae`。
- 任务已发布，Codex集中执行一次，不得重复签发/重做前一已STOP的工程preflight。

**实施范围**：Windows PowerShell与Git静态身份核对；新隔离单个model-branch clone明确指向 `codex/ch5-v010-matlab-first-20261015`，确认HEAD `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`、sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`、九份Git源blob及新磁盘bytes、独立common-dir。Stage A失败即STOP，无补fetch、无第二模型clone、无python。允许一份受界脱敏发布，分支 `review/v010-stage-a-model-ref-reachability-20261016`，只2文件，从本发行commit单父创建，一次non-force push与GitHub远端readback；不安全LOCAL_ONLY。

**新预算**：阶段A模型网络ls-remote一次+clone一次；一次全新模型clone，新Git工作区总≤2GiB（含限域review发布元数据）、新非Git artifact≤16MiB，总墙钟≤2h。Python/pytest/AST/import/HA/HJB/KFE/selector/root/GE/IRF/MATLAB/真实数据/runner均0；前一任务工程Python0/4属于已经STOP的历史账，不能再用。

**上个执行任务已结束**：`V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT` 的A阶段checkout128，[独立审议](versions/0.0.10/runner_io_engineering_preflight_fail_closed_primary_review_20261016.md)结论 `ENGINEERING_PREFLIGHT_FAIL_CLOSED`。本任务不是第二次旧runner preflight，不修改V010冻结模型或安全contract；以后Stage B-E仍需Owner另授权。

最终交付：`V010_STAGE_A_MODEL_GIT_OBJECT_REACHABILITY_RECOVERY_RESULT`，停在 `WAIT_ASTRA_V010_STAGE_A_GIT_OBJECT_REACHABILITY_REVIEW / STOP`。A16/window/C9/CALL_LEDGER、model_activation=False、Results FALSE、C8、原受保护树、旧失败/超额、V011 NOT_STARTED不变。
