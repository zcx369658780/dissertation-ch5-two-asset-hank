# 第五章当前版本登记（2026-10-16）

**V010_WINDOWS_GIT_GUARD_PRIMARY_FILES_REVIEWED__IO_BLOCKED__OFFLINE_STATIC_INTEGRATION_ISSUED**。

| 对象 | 科学/工程事实与下一个gate |
|---|---|
| 上传原件独立验收 | [Astra源码验收](../versions/0.0.10/windows_git_guard_uploaded_primary_review_20261016.md)：MD 9998B SHA256`27CD9B23FC7032E523E0D397D2E7FAF05BD99B500E4CB8E6487AA98B20EC1151`，py 7540B SHA256`A021AFD81CE1342290A8C8387C0B49383CAE20C66B00F46336F220DB546B1C5C`，AST parse PASS，未执行 |
| 原始argv | 旧receipt未捕获，Codex仅从旧runner重构请求端tokens；真实audit argv及child身份未知 |
| Guard草案 | 子命令最小白名单、固定exe/cwd/env、exact list2cmdline匹配及一次性capability静态方向可用；真实output/caller绑定、stdout/stderr、源磁盘bytes、完整audit未闭环 |
| 24例 | MD仅含8个ALLOW+16个DENY分组预期；本轮未上传逐例JSON/未执行，不可称24 PASS |
| ACTIVE新任务 | [runner_guard_io_offline_integration_task](../versions/0.0.10/runner_guard_io_offline_integration_task_20261016.md)：在新隔离目录静态集成I/O，**0 Python/pytest/HA调用**；仅脱敏静态候选可推新review分支 |
| 模型candidate | `94de4501dec051b969bee9d852eba2d4591f30ef` tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5` 仅工程有限接受，scientific仍FAIL_CLOSED/UNTESTED |
| 单点manifest | `rah=.0675,w_eff=15.5,rb=.02`，blob`c23d331bed34e5ca478324cdc05034609ecb91b7`未改 |
| 原V010 plan | commit`bf091da33d59293f147d52c11580327d3ac2a85d`、blob`85138d8859d53295262fe13bf5bc277bca95ed3f`不可追改 |
| 两次失败进程 | 第1 Python1/1、HA0、GBK及旧32MiB超9965206B；第2 Python1/1、HA0、argv guard误拒、artifact117446B |
| 工程runtime/HA | 未获新的科学/工程Python进程许可；完整runner I/O BLOCKED，第三次实验不得执行 |
| 版本/结果 | V011 NOT_STARTED、Results FALSE、model_activation=False |

A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、real C8 A–D REQUEST_ONLY、原8dirty/index/common-dir/旧回执保护持续。
