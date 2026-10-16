# 第五章 CURRENT：Astra独立审原Windows Git守门草案，进入离线runner I/O集成

日期：2026-10-16（Asia/Shanghai）。
**状态：V010_UPLOADED_GUARD_SOURCE_INDEPENDENTLY_REVIEWED__RUNNER_IO_BLOCKED__OFFLINE_INTEGRATION_TASK_ISSUED__NO_RUNTIME_PERMISSION**。

Astra已直接读取Owner上传的`V010_WINDOWS_ARGV_GUARD_STATIC_REPAIR_RESULT.md`及`windows_git_guard_draft.py`原字节、分别得SHA256`27CD9B23FC7032E523E0D397D2E7FAF05BD99B500E4CB8E6487AA98B20EC1151`与`A021AFD81CE1342290A8C8387C0B49383CAE20C66B00F46336F220DB546B1C5C`；AST源码语法PASS（未import/运行）。[独立静态审议](versions/0.0.10/windows_git_guard_uploaded_primary_review_20261016.md)裁决guard设计可供后续离线集成，但真实Windows argv仍`NOT_CAPTURED`、24例只有MD分组预期非runtime PASS、完整runner I/O仍**BLOCKED**。

最重要的代码缺口：Git身份`identity_outputs()`没有绑定实际child有界返回；`ls-tree HEAD`不证明磁盘导入的9份Python源码字节；`Popen`缺有界stdout/stderr/timeout/reap；新hook不能叠加旧hook；旧runner异常/JSON配额/启动失败闭环尚需阅读原runner修复。故**不得再因局部STATIC_READY启动第3个Python进程**。

本轮唯一新ACTIVE为[离线整合runner守门/I/O任务](versions/0.0.10/runner_guard_io_offline_integration_task_20261016.md)；不运行Python/pytest/HA/HJB/KFE，Codex只在隔离scratch整合未执行的runner草案、静态case JSON。**task单独允许安全脱敏文档通过新review分支普通non-force GitHub交付**，不能公开上传原D盘私有日志/绝对路径；以后降低Owner手动搬运文件次数，不修改V1.2永久工作流。

旧两个单点进程各1/1已耗且HA均0；首个GBK故障output43519638B超32MiB 9965206B、第二Windows守门故障117446B在96MiB内。该`rah=.0675,w_eff=15.5,rb=.02`仍`UNTESTED`；旧V010首个两省synthetic HA checkpoint2另FAIL_CLOSED。原科学模型候选`94de4501dec051b969bee9d852eba2d4591f30ef`及原计划blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、单点manifest blob`c23d331bed34e5ca478324cdc05034609ecb91b7`不变。

A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE，real C8 A–D REQUEST_ONLY、原8dirty/index/common-dir/untracked/ignored保护、V011 NOT_STARTED不变。
