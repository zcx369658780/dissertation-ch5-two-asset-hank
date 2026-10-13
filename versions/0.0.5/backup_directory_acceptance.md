# V0.0.5 Astra 空备份目录子门独立验收

日期：2026-10-14（Asia/Shanghai）

**有限裁决：`ACCEPT__SCOPED_EMPTY_BACKUP_DIRECTORY_CREATION__CODEX_REPORTED_ONLY`**

仅接受 V0.0.5 的**附属空备份目录首次创建子门**；此文件不是 V0.0.5 整体最终验收或可信独立实验根 G0 通过证明。原核心 `versions/0.0.5/plan.md` 仍 DRAFT/NOT_FROZEN，未签发整体实施许可。

## 1. 冻结依据及证据等级

- [首次创建子门固定冻结计划](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/13dc04ca85b5a17692871862f5bf25e25a7799fa/versions/0.0.5/backup_directory_gate.md)，commit `13dc04ca85b5a17692871862f5bf25e25a7799fa`，blob `d96af89ce774e39242bd68af11888afee7eb1b3d`。
- [独立操作授权](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/463da12feda60a8efad8e42be0d35068f7a586f2/versions/0.0.5/backup_directory_authorization.md)，commit `463da12feda60a8efad8e42be0d35068f7a586f2`，blob `a472737f034bd6573350b0055e1ec52631146f89`。
- Astra 独立核查 **GitHub 固定许可文档和治理提交/分支**；无法直接访问 Owner Windows C: 或执行 PowerShell。所有目录创建、当前属性、无越界行为、耗时、退出码与操作次数均来自 Codex 在会话提交的 `V0.0.5_C_BACKUP_DIRECTORY_CREATION_RESULT`，证据级别为 **`CODEX_REPORTED_WITH_LOCAL_REPORT`**。本子门本就禁止新增本地落盘回执；无可独立验证的目录对象 SHA/原始日志。

## 2. 有限操作验收

唯一目标：`C:\CH5_Research_Backup`（Owner 已明确选定）。

| 冻结项 | Codex 汇报 | Astra 分类 |
|---|---|---|
| C 根 `Get-Item` | 1次 | `PASS__REPORTED` |
| 目标 `Test-Path` | 1次 | `PASS__REPORTED` |
| `New-Item` 单目录创建 | 1次、零重试、无 `-Force` | `PASS__REPORTED` |
| 成功后的新目录 `Get-Item` | 1次、普通非 reparse 目录 | `PASS__REPORTED` |
| 新目录 `Get-ChildItem` 非递归 | 1次，检查时为空 | `PASS__REPORTED` |
| 进程执行与错误 | exit0、错误无、约0.123秒 | `PASS__REPORTED` |
| 未修改其它既有目录/文件、未复制数据、未触碰模型/Git/科学调用 | Codex 报告均无 | `CODEX_REPORTED_ONLY` |

没有独立 Windows 本地读回，不能将 `PASS__REPORTED` 声称为网页实测。空目录是**检查当时**的状态，不承诺以后永久为空；此次不包含实际数据备份、目录持久保护认证或恢复测试。冻结计划承认普通 `Test-Path → New-Item` 存在潜在 TOCTOU，不据此认定完整 A16/window 通过。

**子门终态：`CLOSED__LIMITED_ACCEPT__EMPTY_BACKUP_DIRECTORY_REPORTED_CREATED`。** 单目录创建和附属有限检查许可已消费并结束，不能自动重复查询/创建、在目录中写文件或启用备份复制。若未来涉及复制/校验、数据来源和生命周期，Owner须另行明确范围。

## 3. 未关闭的 V0.0.5 主目标与科学停点

V0.0.5 可信独立**可弃用攻击实验根** G0 仍 `OWNER_SUPPLIED_ANCHOR_REQUIRED / UNPROVEN`。C 盘是 Owner 的系统/启动盘；`C:\CH5_Research_Backup` 是**保全用途的非可弃用目录**，绝不可作为恶意 rename/delete/reparse/ACL 操作实验对象。不能将“C/D 不同 SSD”或“C 目录成功创建”升级为独立可信实验卷、全路径保护、真实 run004 安全读取或旧 Objective A 四种 output mutation 保护证明。

V0.0.4 仍 `CLOSED__BLOCKED__G0_FIXTURE_ISOLATION_UNPROVEN__NO_EXPERIMENT__WITH_OBSERVATIONS`。V0.0.5 仍 `DRAFT/NOT_FROZEN`、`NEXT_BASELINE_ADOPTION=UNDECIDED`，V0.0.6 `NOT_STARTED`。Owner D1 历史北京三元数据仅拟核验、D2完整A16/window不降级，D3-real/D4-real未批准；`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、window `UNACCEPTED`、`model_activation=False`、`Results FALSE`、旧 CLOSED科学/数据预算、人口/人均和不 `N=P/3` 原样保留。
