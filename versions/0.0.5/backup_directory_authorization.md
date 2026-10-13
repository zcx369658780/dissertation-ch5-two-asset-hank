# V0.0.5 Astra 单独许可：仅建立一个 C 盘空备份目录

2026-10-14（Asia/Shanghai）

**实施许可：`ASTRA_APPROVED_EXECUTION__V005_SCOPED_EMPTY_BACKUP_DIRECTORY_ONLY`**

Owner 确认唯一目标 `C:\CH5_Research_Backup`，第一步**只创建一个空目录，任何文件及备份复制为0**。正式冻结子门 [backup_directory_gate.md](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/13dc04ca85b5a17692871862f5bf25e25a7799fa/versions/0.0.5/backup_directory_gate.md) 的固定 SHA 为 `13dc04ca85b5a17692871862f5bf25e25a7799fa`，blob `d96af89ce774e39242bd68af11888afee7eb1b3d`。本授权仅限该子门，**不冻结 V0.0.5 原计划 `plan.md`，不启动可信实验根的 bootstrap 或旧 Windows fixture**。

## 允许的完整有限动作

- 执行环境：原第五章 Codex 的 Windows 本地普通用户 PowerShell；**一次 PowerShell 执行尝试**；不得请求或取得管理员特权，不设置全局系统参数。
- 唯一允许操作根：`C:\`，最多一次非递归 `Get-Item -LiteralPath 'C:\' -ErrorAction Stop`，确认目录、非 `ReparsePoint`。
- 唯一目标：`C:\CH5_Research_Backup`，最多一次 `Test-Path -LiteralPath ... -PathType Any -ErrorAction Stop`；已存在、异常或未知均立即停止。
- 只有前置完成且目标不存在时，**最多一次** `New-Item -Path 'C:\CH5_Research_Backup' -ItemType Directory -ErrorAction Stop`，禁止 `-Force`。不得改名、重试、补建其它路径或覆盖旧对象。
- 仅在成功新建后，允许对唯一目标最多一次 `Get-Item` 和一次非递归 `Get-ChildItem -Force`；只核目录属性与当前空成员状态，不读取任何文件正文。创建后核验失败保留原状，不删除。
- 前置条件/实际错误/必要输出必须逐步验证；**任一步失败即停止依赖下游**，没有 Python/PowerShell 连续命令失败后继续执行的例外。墙钟目标不超过120秒；超时、返回异常或不能安全限定单次执行则 STOP 和报告，不换方法扩大权限。
- 仅以当前对话回传一个脱敏简短结果（`CREATED_EMPTY` / `ALREADY_EXISTS_STOP` / `BLOCKED`、执行步骤及调用次数、非敏感错误类型）。不创建任何回执文件或日志目录，不记录/发布 ACL、token、SID、设备/卷 GUID 或其它私人文件名。

## 绝对禁止

目录外任何 `stat/exists/read/ACL/reparse/hash`，特别是 D 盘模型树、其祖先和 run004 真实资产；不得复制/备份任何材料，不写新文件、Git提交或全局脚本，不修改现有目录、删除/重命名、更改 ACL，不创建 VHD/VM/隔离攻击根，不启动 V0.0.4 12场景、HJB/KFE、C8/C9/C10、Results、生产/部署。若权限不足或目标冲突，**安全停止，不允许执行替代指令**。C 系统盘和新备份目录绝非完全可弃用的攻击卷。

## 证据/终态

即使 Codex 报告 `CREATED_EMPTY`，Astra 的网页端也未亲自访问本地 C 盘，必须记录 `CODEX_REPORTED_WITH_LOCAL_REPORT`，待集中回报后才作该子门有限验收。此行为只是常规备份路径初建，不能认证可信 fixture root、A16/window、真实来源、C9 或 Results。

执行完毕 `WAIT_ASTRA_V005_BACKUP_GATE_ACCEPTANCE / STOP`。D1历史 run004 北京拟核验对象和 D2完整保护继续；D3-real/D4-real未批准，全部旧科学/数据预算仍 CLOSED；V0.0.6 NOT_STARTED。
