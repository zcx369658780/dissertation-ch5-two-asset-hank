# V0.0.5 Owner C/D 存储拓扑只读检查许可

日期：2026-10-13（Asia/Shanghai）

**状态：`OWNER_APPROVED__C_D_STORAGE_TOPOLOGY_READ_ONLY__NO_CREATE__NO_REAL_DATA_PROBE`**。

Owner明确告知：C、D 位于**两块不同的物理 SSD**。此为 `OWNER_ASSERTED`，并非 Astra/Codex 独立硬件验证。Owner 另明确批准 Windows 自带 Storage cmdlets 对 C/D 的只读磁盘、分区、卷映射检查。C 盘仍仅为未来**保全备份**候选位置，既不是独立可弃用整卷，也不是获准的攻击 fixture；实验可信首次根仍 `UNPROVEN`。

## 精确只读权限（最多6次 cmdlet，零重试）

在普通本地 PowerShell、无需管理员提权，仅限：
1. `Get-Partition -DriveLetter C -ErrorAction Stop`
2. `Get-Partition -DriveLetter D -ErrorAction Stop`
3. `Get-Disk -Number <本轮C分区返回的DiskNumber> -ErrorAction Stop`
4. `Get-Disk -Number <本轮D分区返回的DiskNumber> -ErrorAction Stop`（若同号可复用，不做多一次调用）
5. `Get-Volume -DriveLetter C -ErrorAction Stop`
6. `Get-Volume -DriveLetter D -ErrorAction Stop`

每个 `<DiskNumber>` 必须直接来自当轮对应 `Get-Partition`，不允许 `Get-Disk` 无参枚举。逐项检查 PowerShell 错误并且必须恰好取得对应一个分区/磁盘/卷；任一失败立即停止后续依赖，不回退、不重试、不换命令绕过。只允许在内存中加工结果并向 Astra 返回**脱敏文本**：`C_D_OS_DISK_OBJECTS_DISTINCT=true/false/unknown`、两卷各自文件系统类别、两磁盘的 BusType/IsSystem/IsBoot（若字段存在）、总命令次数和失败类型。Windows DiskNumber 不同仅支持当次 OS 层面的不同磁盘对象，不能替代 Owner 的物理 SSD 声明或证明隔离可信根。

不得发布/上传序列号、磁盘唯一 ID、卷 GUID、SID、完整物理/设备路径、机器或账户身份、ACL/token、卷名或私人目录；如原生对象包含这些属性，**仅选择上述白名单字段**。不创建本地 receipt 文件；原始命令输出不保存或传送到 GitHub。

## 明确禁止

本许可**不是** V0.0.5 正式冻结实施计划、目录创建许可或科学保护探测许可。本轮对历史 run004、原模型工作树或它们的任何祖先实施 `stat/exists/ACL/reparse/open/read/hash/probe` 权限仍为0；不能运行 `Get-ChildItem`、`Test-Path`、`Resolve-Path`、`Get-Acl`、无参 `Get-Disk/Get-Volume`、`Get-PhysicalDisk` 等范围外命令。

不建立 C 盘备份文件夹、不复制数据、不格式化/分区/挂载卷、不创建VHD/VM/账号、不提权/改ACL、不运行任何 fixture/12场景或科学模型、不写代码/修改原 Git worktree 或 push。C 盘若为系统/个人数据盘，不得视为**可弃用攻击卷**。Owner 早前同意考虑 C 备份区域，只代表备份意向，路径/首次写入及受保护范围须之后单独定义。

V0.0.4 CLOSED/BLOCKED、D1 历史北京拟核验对象和 D2 完整 A16/window 保护范围继续；D3-real/D4-real 未授权，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE 和旧 CLOSED 预算保持。V0.0.5 `DRAFT/NOT_FROZEN`、`NEXT_BASELINE_ADOPTION=UNDECIDED`。

**停点：`WAIT_ASTRA_C_D_STORAGE_TOPOLOGY_READBACK / STOP`**。
