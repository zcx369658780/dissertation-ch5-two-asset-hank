# TASK_CURRENT：V010 IMPORT_GUARD SOURCE_ONLY设计

2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_IMPORT_GUARD_AND_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN**。
**STATUS=ISSUED__AWAIT_CODEX_DESIGN_DELIVERY**。
**PERMISSION=SOURCE_ONLY_STATIC_REVIEW__NO_PYTHON_OR_MODEL_IMPORT_OR_HA**。
**STOP=WAIT_ASTRA_V010_IMPORT_GUARD_DESIGN_REVIEW / STOP**。

唯一冻结task：[全文](versions/0.0.10/import_guard_dependency_design_source_only_task_20261016.md)。发行commit`79f82934184292e7d021cbef8d4322c02c9cc0bc`、tree`80a18652013613f883d4d8b48a87cb2a36c882f7`、task blob`1bdb77a12d4494cae3052ba52392125a94bf0413`，**已经发行，不重发或改SHA**。Codex先读原SOURCE_ONLY independent primary review，再只读前轮两脱敏本地图文件（hash见task），优先42个词法入口中20 UNRESOLVED+14 SIDE_EFFECT_RISK，静态设计根身份-源码根双绑定、第三方native/NumPy/SciPy与import-time安全门、未来分层可审计验证路径。若UNKNOWN未解除标PARTIAL，不自动执行。

唯一审阅发布分支`review/ch5-temp-v010-import-guard-design-20261016`，临时目录`_review_tmp/ch5/v010-import-guard-design-20261016/`，只允许脱敏`result.md`≤32KiB和`manifest.json`≤128KiB。**这个目录只存在GitHub临时review commit，禁止本地项目或模型任何worktree/index/staging创建、Git add、checkout**，不写protected树或更改.gitignore；首选GitHub Git Object API直接commit，备选项目外exclusive bare repo，无共享common-dir。一次nonforce交付，sole parent必须本任务发行commit；Astra验收永久归档并回读后清理远端临时副本。精确规则见[Owner批准的临时交换协议](docs/CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md)。

本轮额外源只读≤55文件/4MiB、Git只读调用≤120、非Git工件≤8MiB、2h；**Python、AST、pytest、model import、Windows runner、science HA/HJB/KFE/selector/root/GE/IRF/C8均0**。旧STOP工程预算不结转。冻结科学合同/历史超限、Results FALSE、A16/window/C9/CALL_LEDGER、原8dirty/index/common-dir、V011禁启持续。
