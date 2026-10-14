# V0.0.5 Owner 全量备份和备份后本地清理决定

日期：2026-10-14（Asia/Shanghai）

**`OWNER_ADOPTED__FULL_LOCAL_PROJECT_BACKUP__CLEANUP_AFTER_VERIFIED_BACKUP`**

Owner 明确更正先前“仅按 Git tracked 范围讨论备份”的选项：**应备份整个第五章本地项目**，并要求**备份后由 Codex 清理一次本地目录**，理由是旧工作流惯于新版本创建子文件夹。此决定为本版本新增方向权威，不修改原 V0.0.5 `plan.md` DRAFT、此前固定冻结和验收原件；旧方案只代表当时尚未选择范围的阶段。

## 1. 完整备份的定义

源根（来自 Codex 历史已确认的唯一模型 tree）：`D:\ProjectTemp\c5k1bturn56`；目标保全根：`C:\CH5_Research_Backup`（此前单空目录子门报告已创建并有限接受）。备份应按实际源边界形成**新的唯一命名、非覆盖、可复核的完整快照**，包括：
- 所有 Git tracked 当前工作树字节（**包含尚未提交的 tracked dirty**），及版本历史必要 Git 元数据、refs/objects/index（注意 worktree .git 文件/common-dir 可能在源根之外，外部引用必须核查并经明确范围许可）；
- 所有 untracked / ignored 的本地项目文件，包括旧版本子目录、模型代码和研究产物；应将本项目内的历史研究证据和既有封存资产**列入覆盖资格要求**，不能因忽略规则或大小而默默跳过；
- 本地 receipt、manifest、科研实验原证等应以保全为目的，允许的读取主体、精确文件对象与原数据生命周期仍须通过独立 D3-backup / D4-backup 门。**Owner 的“完整备份”确定保全目的和预期覆盖范围，不等于解除既有 A16/window 完整敌对威胁模型，也不等于授予未指定工具/次数的真实 run004/protected 文件任意探测或读取**。

备份完成资格必须是实际源集合/副本路径/大小与哈希可审计一致、必要 Git 工作树和 refs 可恢复；若某个 protected/reparse/locked/external git common-dir 文件不能复制，**必须披露缺口，分类为 `PARTIAL_BACKUP`，不得自称 `FULL_VERIFIED_BACKUP`**。

禁止 `robocopy /MIR`、`/MOVE`、`/PURGE`、`git clean`、`git reset`、stash、强制覆写、删除旧快照、跨 reparse/junction 任意跟随和自动外传。备份不改变源 HEAD/index/dirty、原有科学目录/版本合同和 LOCAL_ONLY 秘密。敏感原字节全部留本机，GitHub只可发布范围/计数/哈希摘要等脱敏信息，若摘要本身有泄露风险须省略。

## 2. 两层动作必须严格串行

**Gate B — `BACKUP_COPY_AND_VERIFY`**：先独立核实际源对象类型/大小、链接、目的空闲空间及存在性；明确完整快照读权限、目录/对象限制、复制工具、容量/时间、密码/敏感内容存储和 D4 保存/恢复/访问政策，然后 **按 V1.2 独立冻结、再次单独授权 Codex**。本次只更新 Owner 的目的与范围选择，不擅自创建快照或复制受保护源。V0.0.4 的局部合成实验许可不能复活为备份读许可。

**Gate C — `POST_VERIFIED_BACKUP_CLEANUP`**：仅在 Gate B 核验完成，且 **`FULL_VERIFIED_BACKUP`** 或 Owner 对明确备份缺项另作处理后，启动清理审计。Codex 先对旧版本子文件夹和可重建临时产物做分类清单/引用关系/保留策略，明确哪些是重复、哪些包含科学原证、哪些受保护或 git worktree/Git objects 等依赖；必须保证保留 active checkout、全部未提交修改、必要日志/回执和 restore 能力。

Owner 已授权**开展清理规划**，但未指明具体路径、删除/移动/重命名名单、不可逆动作或消费额度。**本决定不授权任何实际文件删除、`git clean`、`Remove-Item`、`rmdir`、旧版本子目录迁移/重命名、修改 Git refs/index 或一键“清理”工具。** 如需实施实际物理清理，必须由 Astra 提交精确清理清单、预期恢复路径及不可逆风险，再取得 Owner 明确取舍及独立实施许可。

## 3. 模型保护与 V0.0.5 主任务

V0.0.5 可信可弃用攻击根主任务仍 `DRAFT__OWNER_SUPPLIED_ANCHOR_REQUIRED__NOT_FROZEN`。Owner 曾建议在当前项目目录建子目录供实验，但项目树及公共祖先存在真实科研/dirty/untracked/历史产物，**仅在项目目录新建子目录不能满足同用户/祖先重解析或替换下的完整 D2 A16/window 敌对保护**。可作为未来无敌对文件系统操作的 synthetic 测试位置建议，不能作为当前完整保护攻击 fixture；新隔离方案仍需独立供应/证明。

流程按 Owner 指示：`BACKUP_SOURCE_SCOPE_AND_CAPACITY_PREFLIGHT → backup freeze + separate auth → COPY/VERIFY → CLEANUP_INVENTORY → (若涉及删除，Owner决定) → V0.0.5 主目标续审`。若需要在危险清理批准前推进主研究的纯静态计划，可以在备份已成功封存后开展，但绝不运行原 A16 攻击或触碰 run004。

本地 SRC `C:\/D:\` 无法由网页 Astra 直接读写；Owner 本次命令不等于已完成备份。当前真实文件复制数 `NOT_STARTED`，目录清理数 `NOT_STARTED`。

D1历史 run004 北京三文件仅拟核验、D2完整 A16/window不放宽；D3-real/D4-real **仍未批准**。本次新提的是 **D3-backup/D4-backup** 独立保存合同，**科学读取许可与备份保存许可不混同**。V0.0.4 CLOSED/BLOCKED；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧 CLOSED预算、人口/人均及不N=P/3全保持。V0.0.6 NOT_STARTED。
