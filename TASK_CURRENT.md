# TASK_CURRENT：V010 corrected HA单点恢复的新一次科学许可

日期：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_CORRECTED_HA_UTF8_LOG_GUARD_ONE_SHOT_RECOVERY**。
**PERMISSION=OWNER_REAUTHORIZED_ONE_PYTHON_PROCESS_AND_AT_MOST_ONE_CORRECTED_SYNTHETIC_HA_ONLY**。

准确任务：[versions/0.0.10/corrected_ha_price_probe_recovery_task_20261016.md](versions/0.0.10/corrected_ha_price_probe_recovery_task_20261016.md)；本次独立恢复freeze固定commit `9aca1018c77d19e9489f2baf59c02bc654923999` / tree `4a04fd536b1cd4dd82b07dbdc23b5d73d1c8f6cc` / blob `95843d1ec838f52b056a8ca768d3f4cc55022b6f`；不追改原科学probe manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7` 或固定候选代码 `94de4501dec051b969bee9d852eba2d4591f30ef`。

任务只能在新隔离目录修正runner UTF-8及异常日志保护，静态审核与写前存储硬门后**新增1个Python进程、最多1次HA**；output≤96MiB=100663296B（不包括但必须独立保留的历史超额文件）、新增clone≤2GiB=2147483648B、总墙钟≤2h；禁止pytest、旧任务重启、多个价格点、GE/IRF、模型代码改动、真实C8/B3读取。失败即STOP不重试。

历史违约永久并列：旧单点Python 1/1、HA0、原输出43519638B＞33554432B（超9965206B），该runner_result SHA仅Codex本地回执。原V010旧预算与A16/window/C9/CALL_LEDGER、Results FALSE、dirty/index/common-dir不动。

交付`V010_CORRECTED_HA_ONE_SHOT_RECOVERY_RESULT` / 终态`WAIT_ASTRA_V010_CORRECTED_HA_RECOVERY_REVIEW / STOP`，Codex不自授科学ACCEPT，V011 NOT_STARTED。
