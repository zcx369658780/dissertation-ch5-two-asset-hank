# V0.0.5 B1：Astra 正式安全停点验收

日期：2026-10-14（Asia/Shanghai）

**`CLOSED__BLOCKED_PRE_COPY__UNAUTHORIZED_EXTERNAL_DEPENDENCY__SAFE_STOP`**

## 冻结权威和证据等级

B1 固定冻结提交 `abf66d69165e3f4279e8e2cc3ef073ca3bae7f9a`，plan blob `1ccd9db281fd04932959d98c4d55fd22d8ad42e8`，合同 [b1_backup_copy_verify_plan.md](b1_backup_copy_verify_plan.md)，Owner 的 D3-backup-byte / D4-backup-local 和 Astra 会话实施授权均限此 B1。Astra 已核对 GitHub 合同与提交，但无法直接访问 Windows C/D、完整原始日志；Windows 执行事实只有 Codex 的 `V0.0.5_B1_FULL_BACKUP_COPY_VERIFY_RESULT`（`CODEX_REPORTED_WITH_LOCAL_REPORT`）。

Codex 报告：B1 preflight 单进程约 2.671秒，exit1 / `RuntimeError`，0重试；两个源根加目标根各自属性检验通过；模型 worktree 唯一目录reparse的链接目标**位于两个固定批准源根之外**。仅查链接对象自身信息1次、不跟随或打开链接目标（访问0）。读取所批准 linked-worktree `.git` 指针1次并报告指向已批准的外部 Git common-dir 管理位置。B0集合汇总再次符合：普通文件90,766、目录6,325、普通逻辑1,804,958,786 B、目录reparse 1。实时空间准入未启动，未建 C快照、没有文件复制/hash/恢复、没有清理或Git写入（均报告0）。

合同第3节A明确要求：无法解释/未经授权的跨根依赖必须在创建前 `STOP/BLOCKED_PRE_COPY`，因此这次是**符合合同的安全停点**，绝不重新分类为备份成功。原快照 `C:\CH5_Research_Backup\CH5_FULL_20261014_GATEB_01` 按 Codex 报告没有创建；此报告不能代替本机客观证明。

## Owner 新决定与 B2 边界

Owner 随后明确同意**方案A**：仅保全项目内该 reparse 链接对象及其类型/目标描述，不复制它指向的两个允许源根之外的文件或目录，并明确保留恢复限制。此项新授权适用于**新冻结的 B2**，不追改 B1 已冻结标准或消耗过的旧 B1 许可。方案A不是漏报外部依赖；必须 `LINK_TARGET_NOT_COPIED`、`EXTERNAL_DEPENDENCY_UNRESOLVED`、`ACTIVE_LINK_NOT_RECREATED`，不可因普通文件全部复制就称原项目环境完整独立恢复。

本次 B1 审议后旧创建/访问授权关闭；任何后续 B2 备份行为都必须依据 [另行固定的新计划](b2_link_descriptor_backup_plan.md)和 Astra 后续会话单独授权，不使用旧任务重试。B1未备份成功，**不得启动旧版本目录的破坏性清理**。

V0.0.5 核心可信可弃用敌对实验根任务继续 `DRAFT/UNPROVEN`，V0.0.4 CLOSED/BLOCKED，D1历史北京元数据和D2完整A16/window保持；科研 D3-real/D4-real仍无许可，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧科研预算不改变。V0.0.6 NOT_STARTED。
