# 第五章 CURRENT：V010 import guard SOURCE_ONLY独立设计门已发行

2026-10-16（Asia/Shanghai）。**ACTIVE_TASK=V010_IMPORT_GUARD_AND_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN**。
**STATUS=OWNER_AUTHORIZED__SOURCE_ONLY_DESIGN_TASK_ISSUED__WAIT_CODEX_DELIVERY**。
**PERMISSION=READONLY_STATIC_DESIGN__PYTHON_0__RUNNER_0__HA_0**。
**NEXT_STOP=WAIT_ASTRA_V010_IMPORT_GUARD_DESIGN_REVIEW / STOP**。

唯一[新冻结任务](versions/0.0.10/import_guard_dependency_design_source_only_task_20261016.md)发行commit `79f82934184292e7d021cbef8d4322c02c9cc0bc`、tree `80a18652013613f883d4d8b48a87cb2a36c882f7`、blob `1bdb77a12d4494cae3052ba52392125a94bf0413`；已经发布，禁止重复派发。Owner授权解决上一SOURCE_ONLY审议后续的**IMPORT_GUARD 与第三方依赖门设计**，仅分析当前42个词法入口（其中20 UNRESOLVED、14 SIDE_EFFECT_RISK、8 PURE_DEFINITION），形成安全的双根`git_identity_root / source_assembly_root` Git源身份+字节/路径绑定、非空init及numpy/scipy/Windows Native副作用门禁，**不物化源码或执行任何import**。

前一[独立SOURCE_ONLY主审](versions/0.0.10/source_only_import_closure_uploaded_primary_review_20261016.md) blob`07371fbeb56097c74c02f8f4d1e9e86460f0550e`保留：70/70固定Git源Blob/bytes；6/6源码SHA256抽样；70 nodes/1056 edge records（7重复、1049唯一tuple）；42词法入口并不证明runtime。新任务只读复用前次**两份已经脱敏**图/报告的精确文件、SHA256，禁读私有旧receipt及失败日志；static budget≤55新增源码/4MiB、≤120个只读Git、wall≤2h、新非Git工件≤8MiB，0模型clone/fetch/checkout、0Python/AST/pytest/runner/HA/HJB/KFE/GE/IRF/真实数据。

**Owner新长期偏好已写入[GitHub临时脱敏交换协议](docs/CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md)**（Blob`a1833c4784bba3a90c79d84b7064286a01dcb541`）和V1.2、[项目知识入口](docs/knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md)：审阅文件`_review_tmp/ch5/v010-import-guard-design-20261016/`只允许出现在独立远端review分支commit tree，绝不进入原项目/治理/模型本地worktree、Git index/staging或dirty树。Codex优先GitHub Git Data API直传；备选项目外独占bare对象库无worktree。审议完成**先永久归档验收，再删除远端临时文件并回读**；Git历史并非彻底擦除。当前唯一可发布review ref`review/ch5-temp-v010-import-guard-design-20261016`，唯一parent新任务发行commit，仅脱敏result.md/manifest.json。原SOURCE_ONLY写树失败证据不自动补推、不结转。

**所有旧科学资格不变**：原V010 plan commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`，模型commit`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`。原MATLAB纠错、corrected HJB/KFE、GovInv 0.9/1.1、same-S/lagged raw ra0、目的地工资税仅一次、原lagged-NKPC主线不可变；corrected单点HA未测，FULL_RUNNER_IO_CLOSURE BLOCKED，model_activation=False，Results FALSE，V011 NOT_STARTED。旧pytest4/6、science driver1/4、HA1/26、selector1626、roots1642、两次单点Python各1/1与GBK首超限9965206B，前轮工程3/4 Python和1/2 runner未用额度不结转。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、真实C8 A-D REQUEST_ONLY、原8dirty/index/外common-dir/untracked/ignored及历史失败原证保护不变；本地QMD与ChatGPT Memory不能因为GitHub同步自动认定已更新。
