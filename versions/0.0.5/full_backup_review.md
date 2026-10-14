# V0.0.5 Astra 全量备份与清理预检技术审议

日期：2026-10-14（Asia/Shanghai）

**判定：`REVIEWED__ACCEPT_BACKUP_DESIGN__OWNER_B0_METADATA_DECISION_REQUIRED__NO_COPY__NO_CLEANUP`。**

依据：Owner [全量项目备份与备份后清理决定](owner_full_backup_cleanup_decision.md)、[预检草案](full_project_backup_preflight.md)及 Codex `V0.0.5_FULL_PROJECT_BACKUP_AND_CLEANUP_PREFLIGHT_PROPOSAL`。本文件为 Astra 设计级接受，**不是正式 B0/B1 冻结计划、独立磁盘访问许可、备份已完成或清理授权**。

## 1. 接受的源覆盖与恢复路线

固定的两个必要来源（地址来自 Codex 本地 Git 回报；网页无本机独立盘核）：
- 现用 linked worktree `D:\ProjectTemp\c5k1bturn56`：须包含 tracked 当前字节、全部 dirty、untracked、ignored、历史版本子目录、空目录及必要科研封存证据；
- 外置共享 Git common-dir `D:\ResearchCode\dissertation-ch5-two-asset-hank\.git`：objects、refs、packed refs、reflogs、config、worktrees/c5k1bturn56 的 private HEAD/index/管理数据；外置 alternates/LFS/submodules 如有，只记录引用后另批，不能跟随未知外部工作树。

Git 官方将 linked worktree 的私有 `$GIT_DIR/worktrees` 与共享 `$GIT_COMMON_DIR` 以及 worktree 根的 `.git` 指针区分：https://git-scm.com/docs/git-worktree 。复制仅工作树无法保证 Git 恢复。

认可 `SOURCE_INVENTORY → PROTECTION/CAPACITY → EXCLUSIVE_DESTINATION → COPY → PER_MEMBER_SHA256 → ISOLATED_GIT_RESTORE_CHECK`。目的备份根为 `C:\CH5_Research_Backup` 下单一新命名不可覆盖快照；**不复制时不能称为完成**，不遗漏 protected/ignored 后冒充完整；不使用 /MIR、/PURGE、/MOVE 或自动删除/重试。文件元数据、ADS/hardlink/reparse 关系及相关 Git 外部依赖的恢复性要分开结论，源可能在复制期间变化则不能声称单一时间点一致。

## 2. 三类不同证明不可混淆

- `PER_MEMBER_BYTE_EQUALITY`：仅证明各成员与其某次源读取匹配，不自动证明它们在某一瞬间整体一致。
- `POINT_IN_TIME_AND_APPLICATION_CONSISTENCY`：须证明一个覆盖实际源集合的窗口、快照和应用写入条件；VSS可评估但未被授权创建，且 writer 协调不足时不能认定应用级一致性。官方：https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service ；https://learn.microsoft.com/en-us/windows/win32/vss/shadow-copies-and-shadow-copy-sets 。
- `FULL_D2_A16_WINDOW_PROTECTION`：同用户敌对进程、祖先重命名/reparse、DELETE_CHILD、句柄生命周期及旧 C9 output mutation 的保护资格**仍 FAIL_CLOSED**。备份目的不解除任何科学安全边界；即使未来全量字节复制成功，也不能借此宣布旧A16/window被关闭。

VSS是否可用、能否只读进入卷快照、卷跨度及安全性全部 UNKNOWN。普通 live copy 无敌对稳定保护时只能取得相应受限证据，不得假造完整 D2 合规。

## 3. 拟议下一门 B0：只读源元数据和目的容量准入

**当前仍需 Owner 新的 `D3-backup-metadata` 与 `D4-backup-inventory`。** 建议一次性只读、非递归跟随式登记以上两个**精确源根内**目录成员（包括 sealed/run004 的 FS **元数据**）的类型、相对路径、大小、reparse/hardlink/必要属性与 Git 管理依赖；遇 reparse/junction 只登记链接对象，禁止跨根追随；绝不打开文件正文、JSON/NPZ/hash，也不解析科研原证或修改源。允许仅查询 C备份根的准确状态与 C卷可用容量，不创建、复制、删除、修改ACL或提权。

**D4约束建议**：完整成员名单、敏感路径/属性留 `LOCAL_ONLY`；公开/发送Astra只脱敏汇总计数、源逻辑字节量/目录数、容量是否足够和异常类别，不上传安全日志、原SHA/原数据。若需要落盘原始私有清单，应另定唯一位置、上限、保留/清理办法，不能自动写到 C空目录或公共 GitHub。

建议将 30分钟、普通文件至多150,000、目录至多20,000、深度至多128、正文读取0、自动重试0作为 B0 **可审议上限**；并非已经冻结的任务额度。触碰受保护目录的 metadata 亦属于新的访问，不能沿用 V0.0.4 的三文件提议或旧 CLOSED 额度。超限、权限不足或链接越界要 STOP，不能声称清单完整。

## 4. B1、清理与主任务

Codex提出的复制源总逻辑容量128GiB、6小时、每文件2次源读和一次副本读、目标留出 `S+max(20%S,10GiB)` 等是 **REQUEST_ONLY**；实际源容量/成员数/C可用空间均 UNKNOWN。B0之后还须明确 D3-backup真实正文字节、D4-backup备份介质明文/加密保留政策、敏感主体访问、VSS/一致性与真实窗口准入，才能由 Astra冻结 B1并**独立发出实施授权**。

隔离恢复时复制 linked-worktree 的 `.git` 指针可能仍指向原 D盘 common-dir，**只能在隔离恢复视图内修正/重绑定并确认所有 Git 命令没有回写原checkout**。未执行恢复验证不得报 `FULL_VERIFIED_BACKUP`。

备份后清理仍仅 Owner批准的**审计与分类**：已验证重复/可重建候选 vs 历史/科研原证/dirty/active Git/unknown KEEP；删除、迁移及重命名须精确对象清单与单独 Owner 决定，不允许 `git clean/reset/stash` 等。

**当前终态：`WAIT_OWNER_B0_D3_D4_METADATA_SCOPE__NO_COPY__NO_CLEANUP`。** V0.0.5 原可信敌对实验根 `DRAFT__OWNER_SUPPLIED_ANCHOR_REQUIRED` 不变；V0.0.4 已 BLOCKED，D1北京历史三文件仅拟科学核验，D2完整威胁不降级、D3-real/D4-real无科学读取许可；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧 CLOSED 预算和不N=P/3保持，V0.0.6 NOT_STARTED。
