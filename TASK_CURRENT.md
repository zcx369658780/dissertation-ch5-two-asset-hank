# TASK_CURRENT：V010 runner Windows argv+I/O 完整离线静态集成

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_AND_SANITIZED_GITHUB_HANDOFF**。
**PERMISSION=OFFLINE_STATIC_DRAFT_ONLY__NO_PYTHON_OR_HA_SCIENCE_RUNTIME__GITHUB_SANITIZED_REVIEW_BRANCH_ONLY**。

唯一任务：[runner_guard_io_offline_integration_task_20261016.md](versions/0.0.10/runner_guard_io_offline_integration_task_20261016.md)。必须先读取[Owner上传原件的Astra独立审议](versions/0.0.10/windows_git_guard_uploaded_primary_review_20261016.md)，补齐真实child Git身份/实际磁盘源码bytes/完整stdout-stderr/timeout/异常/IO quota/终态保证；24例只作为静态断言而非已运行PASS。旧`recovery_runner.py`和既有配套case JSON由Codex**只读**用于集成。

本任务**无Python/py_compile/pytest/HA/HJB/KFE/root/selector/宏观/IRF运行权**；只在新隔离scratch编辑离线文本候选。为避免Owner再手动传文件，本task唯一批准经严格去敏的静态报告/草案文本/逐例JSON发布到新`review/v010-runner-io-offline-20261016`分支，普通非force一次、远端回读；严禁原私有runner/raw数据/系统路径直接公开，禁止写main、治理accepted/原工程代码树。如果无法去敏，STOP不push。

完整runner I/O仍`BLOCKED`，原两次science进程各1/1 HA0；第三次Python/HA必须Owner未来分开授予工程及科学许可。V011 NOT_STARTED、Results FALSE，原A16/C9/window/CALL_LEDGER/8dirty与真实C8/B3保护不动。
