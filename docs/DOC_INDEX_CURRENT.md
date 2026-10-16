# 第五章动态目录（2026-10-16 V010 import guard设计任务已发行）

**唯一 ACTIVE：V010_IMPORT_GUARD_AND_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN**；OWNER批准纯SOURCE_ONLY静态设计，**新Python、runner与科学HA均为0**。

| Authority入口 | 固定路径 | 身份/用途 |
|---|---|---|
| **新ACTIVE冻结任务** | [V010 import guard & dependency gate](../versions/0.0.10/import_guard_dependency_design_source_only_task_20261016.md) | commit`79f82934184292e7d021cbef8d4322c02c9cc0bc`、Blob`1bdb77a12d4494cae3052ba52392125a94bf0413`，已发行 |
| **Owner临时交换及本地worktree禁令** | [CH5_TEMP_SANITIZED_REVIEW_EXCHANGE](CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md) | 只远端独立review分支临时目录；不进入本地Git索引/worktree |
| CURRENT | [当前状态](../CURRENT.md) | 已授权静态设计、研究锁及资源账 |
| TASK_CURRENT | [唯一任务](../TASK_CURRENT.md) | 待Codex静态交付，不重复签发 |
| 上一SOURCE_ONLY独立主审 | [import graph review](../versions/0.0.10/source_only_import_closure_uploaded_primary_review_20261016.md) | 70 Git Blob、42候选、20/14/8风险，仍PARTIAL |
| 上一Windows B–E主审 | [partial engineering review](../versions/0.0.10/runner_io_windows_be_github_primary_review_20261016.md) | 5 Git child正向、loader尚未通过 |
| V010科学决定/版本 | [SCIENTIFIC_DECISIONS](../SCIENTIFIC_DECISIONS.md)、[VERSION](CH5_VERSION_REGISTER_CURRENT.md) | 原模型科学和Results资格冻结 |
| V1.2工作流/长期知识 | [workflow](CH5_ASTRA_WORKFLOW_CURRENT.md)、[knowledge](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md) | Owner交付偏好已写项目长期记忆 |
 
临时交付`_review_tmp/ch5/v010-import-guard-design-20261016/`只在**远端**`review/ch5-temp-v010-import-guard-design-20261016`审核分支存在；Codex不可checkout到本地模型工作树、不可stage、git add或污染原dirty/index。冻结科学计划blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、旧科学/资源超额、A16/window/C9/CALL_LEDGER、Results FALSE、V011 NOT_STARTED保留。
