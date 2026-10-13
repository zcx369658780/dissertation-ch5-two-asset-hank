# V0.0.5 Owner 备份优先及项目内实验目录建议

日期：2026-10-14（Asia/Shanghai）

**现行：`OWNER_REQUESTED_BACKUP_FIRST__THEN_V005_MAIN__PROJECT_LOCAL_FIXTURE_PROPOSED_ONLY`**。

Owner 明确指示：在已建立的 `C:\CH5_Research_Backup` **开始备份**，完成后继续 V0.0.5 的可信实验根主目标；并**推荐**在“当前项目目录”下新建一个**可弃用**实验目录。当前已知实际模型项目目录为 `D:\ProjectTemp\c5k1bturn56`，但 Owner 的“当前项目目录”也可能指不同的项目工作区，需先由执行端确认所指；不能凭意向自行创建/攻击。

## A. 备份方向已决定，但源资产范围必须限定

C 盘是系统/启动卷，`C:\CH5_Research_Backup` 依据 Codex 本地回报已经创建为空目录，并由 Astra 有限接受；该目录是**不可弃用的保全目标**。本次新指令授权**开始备份方案与受界预检**，不是重新打开已关闭的空目录创建门，也不默示读取所有 5947 untracked/4553 ignored、真实历史封存 run004、LOCAL_ONLY receipt、敏感凭据、全部模型实证数据或 8 个 dirty tracked 文件正文。以前 D3-real/D4-real 的精确访问门并未由“备份”二字取消。

备份源分三层，必须在新的独立 backup freeze/authorization 里明示：
1. **SAFE_GIT_OBJECTS**：来自明确 Git commit/tree 的公开已跟踪 Git blob，可优先形成第一批有限基线保全；这不等于保存了最新本地 dirty/未跟踪状态；
2. **LIVE_TRACKED_DIRTY**：原 worktree 中 8 个 dirty tracked 的当前真实字节；如 Owner 选此层，必须事先逐一界定路径/敏感性、读取类别/次数与目标配额，不能改写/暂存 Git；
3. **UNTRACKED/IGNORED/SEALED_REAL**：原 5947 untracked、4553 ignored、历史 run004 封存与任何真实科研原证/敏感内容；**全部默认不开放读取/复制/全量扫描**，需独立明确的特定对象、principal、许可、bytes/次数和 D4 生命周期门，不能以递归 `robocopy /MIR`、`Copy-Item -Recurse` 规避。

任何备份应 `COPY_ONLY / SOURCE_IMMUTABLE`，目的端新建唯一不冲突快照、校验源/副本摘要、计数和相对目录映射、失败停止，不能删除旧快照、不覆盖，不把源内容/LOCAL_ONLY路径/明文敏感资料传 GitHub。本轮未明确可复制的文件全集、大小、配额及权限，故尚无真实文件复制/验收资格。网页 Astra 无法操作 Windows，必须由本地 Codex 按后续批准范围执行并报事实。

## B. 项目内可弃用目录仅登记为 Owner 的“建议位置”，未获得 G0 资格

真实研究项目 `D:\ProjectTemp\c5k1bturn56` 含原 HEAD/index、8 dirty、数千 untracked/ignored 和历史数据。它的任一子目录都共享 D 盘和项目根的**不可弃用祖先**。路径名不同或新建子树**不能证明**敌对进程无权替换项目根/父目录，亦不能把与原模型共用的命名空间标为可弃用。这正是 V0.0.4 `STOP__FIXTURE_ISOLATION_UNPROVEN` 的依据。因此：
- **只允许**作为未来*无敌对命名空间操作*的普通 synthetic unit-test/test-data **候选位置**，须另行允许精确创建、确保与 dirty/untracked 不冲突；
- **不允许**作为当前完整 D2 A16/window 的破坏性 rename/delete/reparse/ACL/handle hostile fixture 根；
- 若 Owner 确实希望在项目内开展完整敌对测试，则必须先提交在根和全部不可弃用祖先风险下有效的机制证明或 Owner 另选独立 sandbox/VM 资源，不能默默减少原 D2 威胁。

## C. 后续顺序与停止点

按 V1.2：**先** Codex 只读、元数据最小调查确定可备份源清单/排除对象/目标空间与预算的完整 proposal；随后 Astra 集中审议、必要 Owner 精确 source decision、固定备份门并单独授权，Codex才可实际 COPY + verify。收到 `BACKUP_VERIFIED` 的受界回执后，Astra 直接继续 V0.0.5 主目标的**版前安全审议**（不自动许可真实实验）；不等待另一轮笼统“是否继续”。

Codex 只读预检不能读取/探测真实 run004、既有模型目录祖先 ACL/reparse、untracked/ignored 的全量字节或备份目的未授权目录；不操作 Git 原 index/HEAD/dirty，不清理、覆盖、同步/镜像或推送敏感数据。每项命令必须真实 fail-fast、保留敏感明细 LOCAL_ONLY。

**状态：`WAIT_CODEX_BACKUP_SCOPE_PROPOSAL__NO_COPY_AUTHORIZED__V005_MAIN_G0_UNPROVEN`**。旧 V0.0.5 `plan.md` 仍 DRAFT、未全面冻结；`NEXT_BASELINE_ADOPTION=UNDECIDED`。原 D1/D2 保留，D3-real/D4-real NOT_AUTHORIZED；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧 CLOSED预算、人口口径与不 `N=P/3` 原样。
