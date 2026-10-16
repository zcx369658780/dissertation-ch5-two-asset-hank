# 第五章 CURRENT：V010第二次单点恢复预检STOP，转入Windows argv守门静态诊断

日期：2026-10-16（Asia/Shanghai）。
**状态：V010_WINDOWS_ARGV_GUARD_STATIC_TASK_ISSUED__TWO_PREFLIGHT_PROCESSES_EXHAUSTED__NO_HA_SCIENCE_PERMITTED**。

Codex已交[第二次恢复单点报告](versions/0.0.10/corrected_ha_recovery_argv_preflight_review_20261016.md)：其私有runner的Windows命令行subprocess守门误拒首次read-only Git核验，**本次新Python进程1/1消耗，HA/HJB/KFE/selector/root均0**。新artifact据Codex为117446B，处于恢复96MiB预算内；未新增clone、原17份上次失败证据size/SHA/mtime据Codex未变。Astra独立只核GitHub冻结和任务文件；无法读取Windows D盘原始报告、stdout、argv，全部本地事实`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不能将Windows argv的详细根因写成已经独立认证。该定价点`rah=.0675,w_eff=15.5,rb=.02`**仍UNTESTED**。

本次唯一ACTIVE任务：[Windows read-only Git argv守门SOURCE_ONLY静态诊断](versions/0.0.10/windows_git_argv_guard_static_repair_task_20261016.md)，`V010_WINDOWS_GIT_ARGV_PREFLIGHT_STATIC_FORENSIC_AND_GUARD_REPAIR`。只审已存在runner/报错及出一个限域静态修复与allow/deny矩阵，**0 Python、0任何科学HJB/KFE/selector/root/pytest、0模型源码变更**。新独立scratch有限，不改变原失败目录。任务结束Astra独立验收后才决定是否请求Owner新增明确进程许可，**本次无第三次科学授权**。

前次首次probe：GBK读UTF-8，Python1/1、HA0、输出43519638B超过原32MiB硬额9965206B；第二次恢复：Windows argv守门，Python1/1、HA0、产物117446B未超恢复96MiB。两次分别STOP、历史失败及账本不可删除/清零。原V010主线工程candidate `94de4501dec051b969bee9d852eba2d4591f30ef`/tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5` 已有限接受，但科学未PASS；原冻plan `bf091da33d59293f147d52c11580327d3ac2a85d`、旧科学输入manifest不改。

Owner原GovInv收益边界0.9/1.1、目的地一次工资税和财政总量桥接保持。原V010旧科学账据Codex pytest4/6、science1/4、HA1/26、selector1626/root1642未解封。A16 FAIL_CLOSED、C9 PAUSED、window UNACCEPTED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、real C8 A–D REQUEST_ONLY，V011 NOT_STARTED，D盘历史8dirty/index/common-dir/untracked/ignored保护，V1.2不变。
