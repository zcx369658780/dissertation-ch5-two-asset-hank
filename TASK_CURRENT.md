# TASK_CURRENT：V010 SOURCE_ONLY全传递import闭包

**ACTIVE_TASK=V010_SOURCE_ONLY_IMPORT_DEPENDENCY_CLOSURE_AND_READONLY_ASSEMBLY_PLAN**。
**STATUS=ISSUED__AWAIT_CODEX_RESULT**。
**PERMISSION=READ_ONLY_GIT_BLOB_AND_STATIC_POWERSHELL__NEW_PYTHON_0__RUNNER_0__HA_0**。
唯一任务：[固定SOURCE_ONLY task](versions/0.0.10/source_only_import_dependency_closure_task_20261016.md)；发行commit`a2c9bf4b57aa9ce8f0c9ae5a1d920e141ee57ebd`、tree`364bb9184c554caa5ecf3b273ef5bd8b6d7271e9`、blob`7affb983e000c487dc306852383d747420400a63`；**已签发，不得重发或替换冻结原文**。
Codex集中读取冻结模型`94de4501dec051b969bee9d852eba2d4591f30ef`：从原runner真实入口递归核三个非空__init__.py、九受监测模块、传递依赖、第三方库声明和import-time风险；产出静态module→path→Git Blob图及未来新隔离装配蓝图。只读现有Stage A clone Git对象，不得写clone、clone/fetch/checkout、新运行Python/AST/import或任何HA科学求解。
新预算：2h、≤90文件/5MiB原始源、≤150只读Git/PowerShell调用、新scratch≤8MiB；仅安全脱敏review分支`review/v010-source-only-import-closure-20261016`、一次nonforce发布、2文件、唯一parent本任务发行commit。失败立即STOP不越权。
旧Windows B–E PARTIAL工程诊断保留，loader未完成，旧工程Python3/4与runner1/2不能续用；`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`Results FALSE`、`V011 NOT_STARTED`。**STOP=WAIT_ASTRA_V010_SOURCE_ONLY_IMPORT_CLOSURE_REVIEW / STOP**。
