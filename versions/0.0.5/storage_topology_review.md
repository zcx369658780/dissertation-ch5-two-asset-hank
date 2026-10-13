# V0.0.5 Astra C/D 限定存储拓扑回读审议

日期：2026-10-14（Asia/Shanghai）

**裁决：`ACCEPT__C_D_STORAGE_TOPOLOGY_READBACK__LIMITED_OS_EVIDENCE`**

本裁决只验收 2026-10-13 [Owner 指定的 C/D 六次只读 Storage 映射许可](owner_cd_topology_read_scope.md)下的 Codex **脱敏集中回报**，不表示 Astra 独立操作 Windows、本地 raw receipts 可获取或真实实验根可信。V0.0.5 仍为 **`DRAFT__STORAGE_TOPOLOGY_REVIEWED__BACKUP_AND_FIXTURE_SEPARATE__NOT_FROZEN`**。

## 1. 授权执行符合范围的已报告证据

Codex 自述实际使用本轮 C/D 各一 `Get-Partition`、来源于此的各一 `Get-Disk -Number`、各一 `Get-Volume`，**六次均取得恰好一对象、退出0、错误0、重试0**；未新建 log、目录、候选，未复制数据、未探测模型/历史受保护资产、未运行 fixture/科学模型。因为 raw PowerShell/OS 和本地进程原证未交给 Astra，以上归类为 **`CODEX_REPORTED_WITH_LOCAL_REPORT`**，不能冒称 `INDEPENDENTLY_VERIFIED_WINDOWS_OS`。

| 卷 | FileSystem | BusType | IsSystem | IsBoot |
|---|---|---|---|---|
| C | NTFS | NVMe | true | true |
| D | NTFS | NVMe | false | false |

`C_D_OS_DISK_OBJECTS_DISTINCT=true`；与 Owner “C/D 在不同物理 SSD” 声明方向一致，并从 OS 层面提供有限佐证。**Windows 不同 DiskNumber 不等于独立可弃用供应卷、可信首次根、不可替换祖先或完整物理/保护隔离证明**。

Astra 通过 GitHub 独立核验：当前许可文档、治理分支 commit/文件路径与 V0.0.5 原草案的 source identity；没有通过网页执行 Windows 指令。权威来自固定许可 `064e38d46a7b3ec9905358487fa4c3a2bb0742dd`、blob `bbe88c132c73212b1ad4f06b6e618cef2d388e5e`。此六次调用包已被报告完成，不再默认重新支用或扩大。

## 2. C 盘备份和合成攻击 fixture 必须分开

**A．C盘备份区域**：C 为报告中的 OS system/boot volume，Owner 允许考虑未来建立备份区域供数据保全。即便 C、D 是不同 NVMe SSD，备份目录及 C 盘公共祖先均**不可弃用**、不可成为恶意 rename/delete/reparse/ACL 修改的实验攻击目标。创建之前需要 Owner 批准**唯一确切目录路径**、不跟随 reparse 的准确允许 preflight/冲突处理、首次 mkdir 行为、信息生命周期及失败 STOP；不自动复制模型、受保护科学回执、dirty/untracked/ignored 或个人数据。可作为**常规保全目标**，不是 D2 下的可信攻击实验根。
**B．实验根**：原 V0.0.5 可信根任务仍缺 Owner/平台可验证的专用可弃用独立卷/隔离环境供应证据。系统 C 盘及其备份区不能取代此锚。若无合格现存独立专用卷，应继续讨论新供应的隔离环境（路线 B）并对其宿主后端、共享/重定向与普通同用户攻击者能力进行独立审查；不自动创建/安装 VHD、VM、SDK、用户或卷。

## 3. 下一次最小 Owner 决策（无自动创建许可）

建议备份目录候选为 `C:\CH5_Research_Backup`，**该路径只是提议，不宣称当前不存在或已通过保护检查**；只准在 Owner 对此唯一位置和明确单目录创建范围作新确认、V1.2 固定冻结与独立实施授权后才允许实际 preflight / 创建，且仍须禁止自动复制资料。

如果 Owner 此时希望优先解除 V0.0.5 的可信 fixture G0 阻塞，应**另选有独立供应身份的专用可弃用卷/隔离 VM**，而非拿 C 系统卷的备份目录实施并发攻击。备份路径批准和攻击实验/真实 run004 读取许可**互不继承**。

## 4. 科学/版本停点

V0.0.4 `CLOSED__BLOCKED__G0_FIXTURE_ISOLATION_UNPROVEN__NO_EXPERIMENT__WITH_OBSERVATIONS`，未创建或验证 12 项场景，旧额度不恢复。V0.0.5 `NOT_FROZEN`、`NEXT_BASELINE_ADOPTION=UNDECIDED`，无代码候选/实施许可；D1 run004 初始北京元数据拟核验对象和 D2 完整威胁范围已采纳，D3-real/D4-real 没有许可。Objective A16 `UNRESOLVED/FAIL_CLOSED`、window `UNACCEPTED`、C9 `PAUSED`、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧数据/科学预算、人口/人均决策和不 `N=P/3` 全不变。V0.0.6 NOT_STARTED。
