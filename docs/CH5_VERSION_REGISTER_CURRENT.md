# 第五章当前版本登记（2026-10-16 import guard SOURCE_ONLY设计门）

**VERSION=V010 / V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=V010_IMPORT_GUARD_AND_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN**。
**AUTHORITY=OWNER_20261016_SOURCE_ONLY_DESIGN__PYTHON_0__RUNNER_0__HA_0**。
**NEXT_STOP=WAIT_ASTRA_V010_IMPORT_GUARD_DESIGN_REVIEW / STOP**。

新任务[IMPORT_GUARD_AND_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN](../versions/0.0.10/import_guard_dependency_design_source_only_task_20261016.md)正式发行commit`79f82934184292e7d021cbef8d4322c02c9cc0bc`、tree`80a18652013613f883d4d8b48a87cb2a36c882f7`、blob`1bdb77a12d4494cae3052ba52392125a94bf0413`；不重复执行或重写固定task。只设计42个入口词法候选（20 UNRESOLVED/14 SIDE_EFFECT_RISK/8 PURE_DEFINITION）、非空init及动态/第三方native依赖、原Git身份根与未来独立源码根的逐文件绑定契约，不做源码装配或Python实验。前`SOURCE_ONLY_PARTIAL_IMPORT_CLOSURE_WITH_OPEN_GATES__DOCUMENTARY_LIMITED_ACCEPT`的70/70 Git树、1056边记录/1049去重和42词法候选保持；不能据此声称导入通过。

Owner[长期临时审阅协议](CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md)最新约束：临时MD/JSON仅能经GitHub Objects API或项目外独占bare元数据发布到**远端独立review分支**，绝不创建/纳入项目本地worktree或index；永久验收归档再清理临时文件。禁止修改既有protected dirty与Git配置。新静态预算≤55源文件/4MiB、≤120只读Git、≤8MiB artifact、≤2h；新Python/AST/import/pytest/runner/HA/HJB/KFE/GE/IRF/C8=0。

V010原科学plan commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、模型commit`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`不改，corrected HA UNTESTED、FULL_RUNNER_IO_CLOSURE BLOCKED、model_activation=False、Results FALSE。历史pytest4/6、science driver1/4、HA1/26、selector1626、roots1642、两次单点Python1/1与GBK首超限9965206B，旧工程3/4 Python、1/2 runner余额不能结转；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、real C8 REQUEST_ONLY、原8dirty/index/common-dir/历史失败保护及V011禁令继续。
