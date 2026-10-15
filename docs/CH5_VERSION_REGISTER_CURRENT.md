# 第五章当前版本登记（2026-10-16）

**V010_SINGLE_POINT_CORRECTED_HA_PREFLIGHT_BLOCKED_STOP__ONE_PROCESS_CONSUMED__ARTIFACT_HARD_CAP_BREACHED__NO_NEW_SCIENCE_PERMISSION**。

| 项目 | 记录 |
|---|---|
| 新单点合同 | [fixed probe freeze](../versions/0.0.10/corrected_ha_price_probe_freeze_20261015.md) @`81181490495f827aa0e15e6a6efb186e8addee67`、blob`24dd985c2497b5aebe5774af925b4c4b9e84be9e` |
| 新人工manifest | `corrected_ha_price_probe_v1.json` blob`c23d331bed34e5ca478324cdc05034609ecb91b7`；`rah=.0675,w_eff=15.5,rb=.02` |
| 本轮科学结果 | **UNTESTED**：Python进程1/1启动后GBK读UTF8预检失败；完整9份源/输入预检未过；HA/HJB/KFE/selector/root=0 |
| 硬额超限 | Codex报告output `43,519,638B`＞32MiB `33,554,432B`，超额`9,965,206B`；原数据保留，禁止改账/清理掩盖 |
| 2026-10-16验收 | [Astra预检失败限定审议](../versions/0.0.10/corrected_ha_price_probe_preflight_review_20261016.md)：接受STOP事实报告，**不接受合同合规执行**，回执仍为Codex本地证据 |
| 旧代码候选 | `94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`仅工程限域接受，模型真实稳态/Results均FALSE |
| 当前任务与下个决定 | ACTIVE NONE；Owner显式决定是否对相同输入另发一次限域新Python进程和至多1个HA（同时修UTF8读/日志写上限） |
| 旧V010预算 | Codex报告原实现进程4/6 pytest、1/4 driver、1/26 HA、selector1626/root1642；不与本次新实验冲销 |
| V011 | NOT_STARTED |

真实C8 A–D REQUEST_ONLY，A16 FAIL_CLOSED，C9 PAUSED，window UNACCEPTED，CALL_LEDGER UNRESOLVED，model_activation=False，Results FALSE，原D盘8 dirty/index/common-dir保护保持。
