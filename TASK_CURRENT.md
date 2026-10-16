# TASK_CURRENT：V010 runner I/O未执行离线静态集成（跨会话继续）

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_AND_SANITIZED_GITHUB_HANDOFF**。
**STATUS=ISSUED__AWAIT_CODEX_DELIVERY__NEW_SESSION_TO_REVIEW_RESULT**。
**PERMISSION=OFFLINE_STATIC_DRAFT_ONLY__NO_PYTHON_OR_HA_SCIENCE_RUNTIME__SANITIZED_GITHUB_REVIEW_BRANCH_ONLY**。

权威唯一本：[runner_guard_io_offline_integration_task_20261016.md](versions/0.0.10/runner_guard_io_offline_integration_task_20261016.md)；发行commit `50fece7d51bbcbb7e4384b0a5a8833b81dcbf76b`、tree `c79f874a1ea60f3a880114fd5d80b0861e6ca21e`、task blob `0070437d83eccaaf4a1c38838e9ce2b1a2fb5634`。**任务已发布，不能因本会话交接再次重发或更换SHA。**

[交接全记录](docs/CH5_CONVERSATION_HANDOFF_20261016_V010_RUNNER_IO_OFFLINE_PENDING.md)；[最新独立静态验收](versions/0.0.10/windows_git_guard_uploaded_primary_review_20261016.md)。工作内容仅是离线整合守门/runner I/O：真实Git子进程结果绑定、磁盘9源实际字节和`__file__`、有界PIPE/timeouts、audit、错误脱敏、写前配额、终态保底，以及24个静态用例和新增反例。新独立scratch≤5文件/2MiB、原小文件只读≤12件/5MiB、≤3小时；无Python/pytest/import/HA/HJB/KFE/root/selector/GE/IRF/MATLAB运行；旧工作树/真实数据不触。

只限经脱敏3种文件向新`review/v010-runner-io-offline-20261016`分支普通non-force一次推送，远端准确回读。若无法安全去敏，提交LOCAL_ONLY报告而不是公开raw。最终交付`V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_RESULT`，`WAIT_ASTRA_V010_RUNNER_IO_STATIC_INTEGRATION_REVIEW / STOP`；下一会话收到Codex结果后Astra独立验收，不允许Codex自授PASS、不得自动进入新科学预算。

冻结V010模型plan/fixture/代码candidate与原单点input全部不追改。旧单点两次Python1/1、HA0、首次存储超限永久记账，第三次新科学Python需Owner未来单独授权。A16/window/C9/CALL_LEDGER/Results FALSE、V011 NOT_STARTED、原8dirty/index/common-dir保护不变。
