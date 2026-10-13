# V0.0.5 附属有限冻结门：首次建立 C 盘空备份目录

**日期：** 2026-10-14（Asia/Shanghai）  
**冻结时状态：`FROZEN_SCOPED_BACKUP_GATE__AWAIT_SEPARATE_ASTRA_AUTHORIZATION`**  
**唯一目标：** 如果确实尚未存在，则在 C 盘**只新建一个空目录** `C:\CH5_Research_Backup`；不复制资料、不创建文件、不修改既有目录/文件。

## 1. 既有权威和本门的独立边界

Owner 先允许以 C 盘为备份区域候选，随后明确确认 **`C:\CH5_Research_Backup` 是唯一目录、第一步只建立空目录、不复制资料**。C/D 拓扑报告：C 与 D 是不同的 Windows 磁盘对象、NTFS/NVMe；C `IsSystem=true/IsBoot=true`，此为 Codex 本地报告、非网页在 Windows 独立实测。参见 [原 V0.0.5 草案](plan.md)和 [C/D 只读审议](storage_topology_review.md)。

**本文件仅是 V0.0.5 内的 `SCOPED_BACKUP_DIRECTORY_CREATION_ONLY` 辅助门。V0.0.5 原主要目标——可信的完全可弃用攻击实验根及祖先隔离证明——仍未实现、原 `plan.md` 继续 DRAFT/未整体冻结。** 本门可局部关闭，但不得宣称 V0.0.5 G0 已经 PASS；也不准把 C 备份区作为有破坏性测试的 fixture 根。只有本文件的固定 Git SHA 和 Astra 另外签发的实施许可一起才构成本门执行权，冻结后不可追改。

本门无新模型源码/测试/Git 候选，无代码 `NEXT_BASELINE_ADOPTION`；`NEXT_BASELINE_ADOPTION=UNDECIDED`，建议的前版固定代码基线并非该目录操作的程序依赖。保留第五章原 Windows 模型工作树 HEAD/index/dirty/untracked/ignored、main、其它项目和 Git 科学合同全部不动。

## 2. 允许操作的精确位置、前置与原子创建

**唯一允许目标：** `C:\CH5_Research_Backup`；唯一允许非递归根检查对象：`C:\`。二者以外任何路径、卷、目录和文件不在本门许可范围内。

使用当前非提权 Windows PowerShell 和既有内置 FileSystem provider，**只允许一次执行尝试、零自动重试、单 PowerShell 进程**。不得生成独立脚本、编译工具或额外落盘日志。执行前只检查用户已指定的根和目标，固定流程：

1. 对 `C:\` 进行**最多一次** `Get-Item -LiteralPath ... -ErrorAction Stop`，确认它是目录且未标记 `ReparsePoint`。若异常、不可访问或结果不符，**STOP 且不创建**。该检查只支持常规备份目录创建，不认证任何 A16 安全属性。
2. 对准确目标做**最多一次** `Test-Path -LiteralPath ... -ErrorAction Stop`（`PathType Any`）；结果为 true 时 **`STOP__BACKUP_TARGET_ALREADY_EXISTS`**，不复用、不重命名、不删除、不覆盖。检查失败/结果未知也 STOP，不推测目录不存在。
3. 使用**最多一次**普通 `New-Item -Path 'C:\CH5_Research_Backup' -ItemType Directory -ErrorAction Stop`，**禁止 `-Force`、`-Name` 另造名称、`-Recurse`、`mkdir -p`、相对路径/变量拼接、预创建父目录**。目标直接位于 C 卷根。即便 preflight 已通过，创建时若另一个进程竞争创建而导致“已存在”，则 **STOP**，不改用其它名称重试。
4. 仅在创建 API 成功后，对**新建的准确目标**最多一次 `Get-Item -LiteralPath ... -ErrorAction Stop`，确认它是目录且非 `ReparsePoint`；仅对该新目标允许一次**非递归** `Get-ChildItem -LiteralPath ... -Force -ErrorAction Stop`，确认新建目录当前没有成员。这个枚举只限刚建立的空目录，不搜索其它路径、不读取文件正文。若状态异常或出现成员，**停止并保留原现场，绝不自动清理**。
5. 记录匿名化结论、每一步是否执行、错误分类、创建尝试数、核验是否为空；PowerShell 脚本的每个依赖步骤必须由异常/退出码真实阻断后继，不许续跑。整轮墙钟建议硬上限**120秒**，若无法可靠约束或中止单个调用，应 STOP/报告时间控制不可用；不得因时间终止而删除既有内容。

**重要限制：** 这是常规创建空备份文件夹，不是对同用户敌对命名空间替换的可证保护；`Test-Path` 和 `New-Item` 之间仍有竞态，最终若创建成功也只证明有限创建行为，不能宣称 C 卷或备份区满足原 A16/window。

## 3. 冻结的零权限与数据卫生

- **创建次数：** 最多1次仅有的目标 mkdir；失败也计数。**不会写入任何文件数据**；系统为创建目录配置的 FS 元数据开销可以为非零，无法预先精确计字节，记录 `UNKNOWN`，不通过复制文件补齐。
- **精确查询次数：** C 根 Get-Item 1、目标 Test-Path 1、成功后新目标 Get-Item 1 和该目标非递归 Get-ChildItem 1；没有额外权限查询或全盘扫描。**复用上一轮 C/D 存储映射证据，不重复旧六次已闭额度**。
- **绝对禁止：** `Copy-Item`、`Move-Item`、`Remove-Item`、ACL 修改、reparse 创建/更改、磁盘/卷/VM 操作、root/祖先 rename/delete、创建其它目录/文件、自动备份、本地 receipt 文件、Git staged/push、新命令安装或管理员提权。不得读取 `D:\ProjectTemp\c5k1bturn56`、真实 run004、模型父目录或其它私人路径的 stat/exists/ACL/open/read/hash；不执行任何 fixture、12场景、HJB/KFE、C8/C9/C10、GE/Results。
- 仅向 Astra 回传**简短文字**，允许目标路径本身（Owner 已指定）、`CREATED_EMPTY` / `ALREADY_EXISTS_STOP` / `BLOCKED`、各命令计数、非敏感错误类别、最终检查是否为空；不外传 SID/token/ACL、其它文件清单、卷 GUID/UniqueId、机器身份或私有日志。没有新的原始日志文件/备份文件，也没有获准在目标目录内存放回执。

## 4. 验收与终态

`PASS__BACKUP_EMPTY_DIRECTORY_CREATED_ONLY`：只有本次实际新建目标、读回确认为普通非 reparse 目录、即时非递归枚举空、越权操作零、原模型/数据未接触（本地证据仅由 Codex 说明），Astra 才可**有限接受空目录创建**。

`STOP__BACKUP_TARGET_ALREADY_EXISTS` / `BLOCKED__PREFLIGHT` / `BLOCKED__CREATE_OR_VERIFY`：未满足条件时可终止，不得对旧对象执行动作或为完成任务创建替代位置。若在创建后验证失败，**不得删除/清理新目录**，原情况如实报告。

执行完毕：`WAIT_ASTRA_V005_BACKUP_GATE_ACCEPTANCE / STOP`。本门的报告只支持常规备份目录的存在/当前空内容结论，**不是备份完成、真实资产保护通过、V0.0.5 G0成功或 Windows A16 PASS**。

V0.0.4 保持 `CLOSED/BLOCKED/NO_EXPERIMENT`，D1 北京初始三份历史元数据仅 REQUEST_ONLY、D2 完整 A16/window 不放松，D3-real/D4-real未批准；`A16 UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、`model_activation=False`、`Results FALSE`、旧科学/数据预算、人口/人均及不 `N=P/3` 全不变。V0.0.6 NOT_STARTED。
