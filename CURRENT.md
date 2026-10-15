# 第五章 CURRENT：V010 corrected HA单点实验一次性UTF-8与日志恢复任务已签发

日期：2026-10-16（Asia/Shanghai）。
**状态：V010_CORRECTED_HA_ONE_SHOT_RECOVERY_ISSUED__AWAIT_CODEX_EXECUTION_RESULT**。

当前唯一ACTIVE：[单点UTF-8预检/日志受界恢复任务](versions/0.0.10/corrected_ha_price_probe_recovery_task_20261016.md)，任务ID`V010_CORRECTED_HA_UTF8_LOG_GUARD_ONE_SHOT_RECOVERY`。Owner新批准**单独1个Python进程+最多1次synthetic HA**与更高新存储：**96MiB output硬限/2GiB新独立clone硬限**；固定[补充恢复freeze](versions/0.0.10/corrected_ha_price_probe_recovery_freeze_20261016.md)commit `9aca1018c77d19e9489f2baf59c02bc654923999`、tree`4a04fd536b1cd4dd82b07dbdc23b5d73d1c8f6cc`、blob`95843d1ec838f52b056a8ca768d3f4cc55022b6f`。

原单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`的manifest仍为blob `c23d331bed34e5ca478324cdc05034609ecb91b7`，代码仍唯一候选`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`。只修新隔离runner的显式UTF-8、异常有限日志、写前总字节限制，源HJB/KFE、selector、网格、参数、原V010合同/两省fixture全不改。模型实际科学结果仍`UNTESTED`，此任务不允许宏观外层、IRF、真实C8或生产激活。

上次单点任务`21c736d4163a12978486c3b8256f4db8b9bd6c76`**Python1/1已耗、HA0**；旧输出`43,519,638B`超出32MiB `9,965,206B`不追溯豁免、清理、重计0。详见[2026-10-16限定失败验收](versions/0.0.10/corrected_ha_price_probe_preflight_review_20261016.md)。新额度完全新账，不混入以前V010旧预算4/6 pytest、1/4science、1/26HA、1626 selector、1642 roots。

V010主线仍是原MATLAB HA→有界外层GovInv/Zt→逐期冲击；Owner原GovInv0.9/1.1、目的地税只扣一次、财政总量原则保持。V011 NOT_STARTED，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY、D盘历史8dirty/index/common-dir保护、V1.2均不改变。Codex集中回报后Astra独立验收，不自动续跑。
