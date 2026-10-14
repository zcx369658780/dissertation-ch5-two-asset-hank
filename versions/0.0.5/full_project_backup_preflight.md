# V0.0.5 全项目备份容量/源集合与安全清理预检方案（版前 DRAFT）

2026-10-14（Asia/Shanghai）

**`DRAFT__OWNER_FULL_PROJECT_SCOPE_ADOPTED__BACKUP_COPY_NOT_AUTHORIZED__CLEANUP_DELETE_NOT_AUTHORIZED`**

参考 [Owner 全量备份与清理决定](owner_full_backup_cleanup_decision.md)。本草案取代此前仅考虑 Git tracked 快照的**备份来源方向**，但不会追改先前 `backup_scope_preflight.md` 及已冻结子门。整个第五章本地项目为目标，**不能擅自跳过 dirty、untracked、ignored、封存原证和必要 Git 元数据**。备份目标为 `C:\CH5_Research_Backup` 内新 snapshot，**当前未获准任何实际备份写入或清理删除**。

## Codex 下一份集中 SOURCE/CAPACITY Proposal 的具体要求

1. 仅核既有项目 Git 元数据及前次权限内的已知结构（尤其原工作树、git common-dir 指向形式、工作树是否 linked worktree、dirty/untracked/ignored 历史统计）。明确实际“整个本地项目”的包含边界：项目目录下所有普通文件/子目录；超出源根的 Git common-dir、LFS/object linkage、Symlink/junction/reparse、可变开放写入对象均标出需要额外许可的类型。不对受保护 run004/真实历史证据开展新的 `stat/exists/hash/read`，不递归打开所有私人文件直到后续备份 D3/D4 固定。
2. 提出一次完整、有界的只读**元数据容量/排除风险**门：源根身份/目录链接、不跟随 reparse 的文件类别与 size 总账、对象数、源是否活跃更改、是否有 Win32 长路径/权限/locked 文件、目标 C 卷可用空间、保密性、单卷 mount 异常等。严格分开`SAFE_GIT_OBJECTS` / `LIVE_DIRTY` / `UNTRACKED_IGNORED` / `PROTECTED_SEALED`，不要只备份前一层然后说“全量”。
3. 目标布局须是 `C:\CH5_Research_Backup\<独立单一快照名称>`；唯一不可覆盖、绝不删除旧备份，失败保留完整现场并标记 `INCOMPLETE`。实际文件保全遵循 `COPY_ONLY`，严禁 `/MIR`/`/PURGE`/`/MOVE`；避免 reparse 环路/越界及复制到自我路径；不让复制过程污染源项目。
4. 建议每类源字节的 read/open/hash 次数、占用容量/余量、非覆盖目标预检、复制步骤和验证（manifest、全文件摘要或按体积分层）、大文件/锁定/修改中的处理规则。若无法在一致窗口取得源，报告 `INCONSISTENT_OR_PARTIAL_BACKUP`，不以历史 manifest/hash 自动替代当前数据；无权访问的 sealed run004 必须明确预留 D3-backup/D4-backup 决策门。
5. `D4-backup` 对敏感内容明确：仅本机源→同用户受保护的本机 C 目标（属于系统盘，非安全隔离）；备份访问主体、原数据/临时明文可见性、私有日志、保留/擦除策略须列成实际选择，不许上传完整列表和敏感 SHA/路径到公共 GitHub。
6. 备份结束的恢复验证（至少恢复目录元数据/代表性非敏感固定源及 Git refs 校验，不在原 active checkout 恢复试写），把“Copy success/Hash match/Restore-ready/Whole project complete”严格分账。
7. 后续清理的**只读逻辑名单**：由 Git 元数据、历史版本任务索引、源码引用关系与源目录类别提出**待分类对象**；`TRIVIALLY_REGENERABLE` / `HISTORICAL_EVIDENCE_KEEP` / `PROTECTED_KEEP` / `ACTIVE_DIRTY_KEEP` / `UNKNOWN_KEEP`，不能用“文件夹名字像旧版本”判断可删。不操作 `git clean`、`Remove-Item`、源目录移动或重命名。
8. 回报 Codex 是否能在**单个新精确固定备份门**中满足真实保护资产读取的 A16/window 威胁约束。如果做不到，报告 blocker 和与完整性要求对应的缺项，不能悄悄切换低标准、以旧安全事件的 A16 FAIL_CLOSED 冒充 backup PASS。

下一步交付 **`V0.0.5_FULL_PROJECT_BACKUP_AND_CLEANUP_PREFLIGHT_PROPOSAL`**，至少含精确候选操作/权限/本金/代码路径、实际资源硬上限和坏路径/重解析/并发修改的 fail-fast 状态机。后续 Astra 评审再固定真实复制和核验实施范围，本 DRAFT 本身既不允许超范围探测也不允许开始复制。

科学状态不升级：V0.0.5主 G0仍 UNPROVEN；D1/D2及 D3-real/D4-real 保持，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、Results FALSE、旧预算和 V0.0.6 NOT_STARTED不变。
