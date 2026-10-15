# 第五章当前版本登记（2026-10-16）

**V010_CORRECTED_HA_UTF8_LOG_GUARD_ONE_SHOT_RECOVERY_ISSUED__WAIT_CODEX__NO_REAL_GE_OR_RESULTS**。

| 对象 | 准确权限与证据 |
|---|---|
| 当前ACTIVE任务 | [单点恢复任务](../versions/0.0.10/corrected_ha_price_probe_recovery_task_20261016.md)，任务ID`V010_CORRECTED_HA_UTF8_LOG_GUARD_ONE_SHOT_RECOVERY`；新增**1 Python进程、≤1 synthetic HA** |
| 新恢复freeze | [2026-10-16 UTF8+logging freeze](../versions/0.0.10/corrected_ha_price_probe_recovery_freeze_20261016.md) @ commit `9aca1018c77d19e9489f2baf59c02bc654923999` / tree `4a04fd536b1cd4dd82b07dbdc23b5d73d1c8f6cc` / blob `95843d1ec838f52b056a8ca768d3f4cc55022b6f` |
| 新任务存储 | **96MiB=100663296 B artifact**，**2GiB=2147483648 B clone**；2h，均只约束本次新恢复工作区，写前guard |
| 原单点manifest | [corrected_ha_price_probe_v1.json](../versions/0.0.10/corrected_ha_price_probe_v1.json) blob `c23d331bed34e5ca478324cdc05034609ecb91b7`；`rah=.0675,w_eff=15.5,rb=.02`不变 |
| 唯一model candidate | `94de4501dec051b969bee9d852eba2d4591f30ef`，tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；仅原15路径代码工程接受，science依本次实际HA |
| 旧GBK错误与超额 | [2026-10-16限定验收](../versions/0.0.10/corrected_ha_price_probe_preflight_review_20261016.md)：Python1/1已用，HA0，原43519638B/32MiB超9965206B；永不删除/追溯豁免 |
| 原V010实施冻结 | [plan](../versions/0.0.10/plan.md) @ commit `bf091da33d59293f147d52c11580327d3ac2a85d`，blob `85138d8859d53295262fe13bf5bc277bca95ed3f` |
| 原V010历史账 | Codex报告4/6 pytest、1/4 science、1/26 HA、1626 selector、1642 roots；与新恢复分账 |
| 后继/论文结果 | V011 NOT_STARTED；Results FALSE、真实C8 A–D REQUEST_ONLY |

Owner GovInv 0.9/1.1、目的地税一次和财政总量桥接不变。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False与历史8dirty/index/external common-dir保持。
