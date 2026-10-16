# 第五章当前版本登记（2026-10-16）

**V010_TWO_SINGLE_POINT_PREFLIGHT_PROCESSES_EXHAUSTED__HA_POINT_UNTESTED__WINDOWS_ARGV_STATIC_REPAIR_ACTIVE**。

| 对象 | 当前真实状态 |
|---|---|
| 原V010 frozen plan | 恢复freeze固定commit `9aca1018c77d19e9489f2baf59c02bc654923999`；原`plan.md`固定commit `bf091da33d59293f147d52c11580327d3ac2a85d`、blob `85138d8859d53295262fe13bf5bc277bca95ed3f`，不追改 |
| 原代码候选 | `94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，仅工程代码有限接受，HA/GE/Results未通过 |
| 单点科学freeze及input | `81181490495f827aa0e15e6a6efb186e8addee67` / manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`，`rah=.0675,w_eff=15.5,rb=.02`未改 |
| 首次probe | Python1/1、HA0，GBK预检停止，artifact43519638B超32MiB `9965206B`（CODEX本地回执） |
| 第二次恢复 | [Astra最新审议](../versions/0.0.10/corrected_ha_recovery_argv_preflight_review_20261016.md)：Python1/1、HA0，Git argv守门预检停止；新增117446B低于96MiB，clone0；原17份文件回执不变（CODEX本地回执） |
| 当前唯一任务 | [windows_git_argv_guard_static_repair_task_20261016](../versions/0.0.10/windows_git_argv_guard_static_repair_task_20261016.md)：只读既有私有runner/报错，静态源码及有限scratch，**Python科学进程0** |
| 原V010旧预算 | Codex报告pytest4/6、science1/4、HA1/26、selector1626/root1642，不与两次单点调用冲销 |
| 实时权限 | 第三次Python/HA未授权，只有非科学静态guard修复取证；不能修改真实C8/旧代码/历史合同 |
| V011/Results | NOT_STARTED / FALSE |

Owner GovInv收益边界0.9/1.1、目的地税只扣一次、财政总量桥不变。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、real C8 A–D REQUEST_ONLY、D盘8dirty/index/external common-dir保护仍生效。
