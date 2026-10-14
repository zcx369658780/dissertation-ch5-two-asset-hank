# V0.0.5 B0 元数据与容量门：Astra 有限验收

日期：2026-10-14（Asia/Shanghai）

**终态：`CLOSED__ACCEPT_B0_NON_REPARSE_SCOPE__CODEX_REPORTED_WITH_OBSERVATIONS`。**

固定 B0 冻结合同：commit `0459d9576b9294dc5cb1c5f238c7e56763babce9`，blob `c5f49f10da1214117c337956e849d601ca1f28aa`，文件 [b0_metadata_gate.md](b0_metadata_gate.md)。Owner 另批准了专门的 D3-backup-metadata / D4-backup-inventory；该预算只用于 B0，已经消费，不延伸为科学 D3-real/D4-real。Astra 经 GitHub 独立核对合同与版本状态，**并未在本机复跑 Windows 遍历、读取原路径清单或实际原始回执**。以下全部运行数值为 Codex 会话交付的 `CODEX_REPORTED_WITH_LOCAL_REPORT`。

| B0 项目 | 模型 worktree | 外部 Git common-dir | 合计 |
|---|---:|---:|---:|
| 普通文件 | 76,625 | 14,141 | **90,766** |
| 目录数（含根） | 5,877 | 448 | **6,325** |
| 已枚举目录 | 5,876 | 448 | **6,324** |
| 普通文件逻辑字节 | 1,150,549,423 | 654,409,363 | **1,804,958,786 B（约1.681 GiB）** |

C卷报告可用 643,058,806,784 B（约598.895 GiB）；最大深度8。一个**模型 worktree 内目录 reparse** 被登记、未跟随；因而登记目录6,325而实际枚举6,324；reparse目标和恢复语义**UNRESOLVED**。其它非目录 reparse、特殊条目、metadata不可读、已查属性的压缩/稀疏/加密/offline计数均为0；hardlink、ADS、具体 reparse 类型与指向、真实正文可读/锁、应用时间点一致性以及外部Git隐性依赖仍 UNKNOWN。

Codex 报告：单进程约10.382秒、exit0、0错误/0重试；自身根查询3次、C卷查询1次、6,324目录枚举、97,089成员返回、109,733元数据查询，未超冻结人数/深度/时间；正文读/hash/写/复制/Git写/科学/攻击均0。成员关系 `90,766+6,325-2=97,089` 一致。峰值内存 UNKNOWN。没有新增本地日志或上传完整成员清单。

**接受范围：`B0_METADATA_COMPLETE_FOR_NON_REPARSE_SCOPE`**，不是 reparse目标覆盖、全部NTFS流/保密一致性、安全窗口、任何实际复制或 `FULL_VERIFIED_BACKUP`。即使后续 B1 备份验证通过，科学 A16/window 仍 `UNRESOLVED/FAIL_CLOSED`、旧 C9 `PAUSED`，历史 run004来源认证与 Results 均不升级。原 B0 一次性权限关闭，无自动重新检查许可。

下一门 `B1` 是 Owner 2026-10-14 新批准的**仅备份目的正文字节** D3-backup / D4-backup，严格依照单独固定 [B1复制与验证计划](b1_backup_copy_verify_plan.md)及 Astra 会话实施授权。V0.0.5 原独立可弃用攻击根主计划仍 DRAFT；V0.0.6 NOT_STARTED。
