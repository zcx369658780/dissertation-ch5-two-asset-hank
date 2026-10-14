# V0.0.5 B0：完整第五章项目只读元数据和容量登记冻结门

**日期：** 2026-10-14（Asia/Shanghai）  
**状态：** `FROZEN_B0_METADATA_ONLY__SEPARATE_CHAT_AUTHORIZATION_REQUIRED`  
**研究版本：** 仍属 V0.0.5 备份子门；本版本可信可弃用实验根主 `plan.md` 仍 DRAFT。  
**冻结用途：** 单次连续完成源集合类型/逻辑容量审计和目标空间准入，然后集中回报；**不能分拆成 GitHub 微任务、不能自动进入正文复制 B1**。

## 1. Owner 许可与科学边界

Owner 明确批准本次 **`D3-backup-metadata`**：仅对下述两个固定源根的全部目录成员（包括此前 protected/sealed/run004）获取目录项名称/相对路径、是否目录/普通文件/reparse/其它类型、逻辑文件大小及必要 FS 元数据，供将来完整备份覆盖判断。**此许可绝不包含这些文件的正文 open/read/hash/parse、任何科学 consumer、ACL/SID/token 内容或拓展为受保护祖先探测。**

Owner 同时批准本门 **`D4-backup-inventory`**：原始完整路径清单、metadata、私密例外应仅在执行进程内存中处理（`LOCAL_ONLY`），**本门不创建本地清单文件、日志、manifest、脚本、目录或快照**；传给 Astra/GitHub 的内容只能是脱敏聚合数值、错误类别和 UNKNOWN，不能有 private member names、SID/卷ID/序列号或 sensitive hash。以后若需持久私有 manifest，须由 B1 独立决定具体存放、容量与生命周期。

对已采纳的 D1（历史北京元数据仅未来拟核验）与 D2 完整 Objective A16/window 威胁范围**没有任何缩减**。B0 是备份用 FS 元数据登记，**不是**可对抗同用户恶意祖先替换的安全窗口证明，不能将 B0 完成升级为 `A16 PASS`、run004来源认证、科学数据读取或 Results。

## 2. 仅三个准许的精确位置

**源根A（linked worktree）：** `D:\ProjectTemp\c5k1bturn56`。  
**源根B（Git common-dir）：** `D:\ResearchCode\dissertation-ch5-two-asset-hank\.git`。  
**备份目标根：** `C:\CH5_Research_Backup`，本次仅核它的自身目录类型/是否reparse；**额外仅准许一次** `Get-Volume -DriveLetter C -ErrorAction Stop` 提取 `SizeRemaining`。不访问 C 其它文件夹。

仅由 Windows 上已存在的普通用户 Python/PowerShell/原生内置只读接口执行，不提权，不安装依赖、不调整 ACL/服务/NTFS 权限。Codex 以单任务自行选最佳无落盘实现，不需要每个路径或命令再来回审批。

## 3. 单次完整执行过程与硬预算

1. 在首次遍历前，对上述**三个精确根**各执行一次不跟随的自身元数据查询，确认预期目录、非reparse、对象可读；另一次固定 C卷 free-space 查询。任何源根异常、错误或不符则 `STOP`，**不得探测其上级目录作为补救**。
2. 在两个源根之内，使用不跟随目录链接的逐层有界枚举（如 OS `scandir` + `stat(follow_symlinks=False)`，结合 Windows reparse 属性）。仅处理返回的**目录项元数据**；发现 reparse/junction/symlink 只计数和分类，**不进入、不解析目标、不跨根打开链接目标**。登记文件/目录数、逻辑字节、最大深度、普通/特殊/不可读对象数、已枚举/未覆盖类别；必要时区分 worktree/common-dir 总账。hardlink/ADS/压缩/稀疏等无法从允许 metadata 中确认的属性保持 `UNKNOWN`，不得额外打开正文。禁止 full path/SID等私人对象明细出现在公开结果。
3. 对 C `SizeRemaining` 与源逻辑字节合计 S 作**估算性**准入：提出 B1 需保留的复制/验证/恢复及未计算的流与 FS 开销；**不把逻辑 S 等同物理占用、真实全量成本或已证明的文件集合时间点一致性**。原 B1建议 128 GiB/6h 非 B0 冻结许可。
4. 单次运行最多 **30分钟墙钟、150,000普通/特殊文件、20,000目录、源根以下深度128、自动重试0、同时执行进程1**；每个已到硬上限的下一次查询必须停止，不能用新进程或更名重新计数。**研究文件正文读取0、文件哈希0、科学进程0、所有源/目标文件系统写入0、Git写入0、VSS创建0、攻击进程0**。目的端可写可用容量由唯一 C卷查询判断，不能任意探测其它位置。执行内存以合理限额自主控制，无法量测则将资源遥测列 UNKNOWN，不凭空填 PASS。
5. 对开放修改、TOCTOU、无法读取条目/权限错误、根被替换、目录环路、超时、配额超额、意外跨根引用等要如实 `STOP/REPORT`，不重试、不启用管理员绕过、不以剩余已枚举成员声称全集。`reparse`本身若被准确登记且完全不跟随，可继续记录其它正常成员，但该链接目标的完整覆盖仍 `UNRESOLVED`。若安全的非跟随遍历不能实现，必须**在敏感枚举前停止**。本门不证明完整 D2 威胁下不存在竞态；发现可疑更名/竞态立即停且归为 UNKNOWN。
6. 结果**仅一次集中交付** `V0.0.5_B0_FULL_SOURCE_METADATA_AND_CAPACITY_RESULT`，包含两源各自计数、总体逻辑字节/C卷剩余量、reparse/不可读/外部链接对象分类数、阈值/已消费预算、是否完整到达全部允许源成员、异常以及 B1 所需精确缺口；**不创建本地 receipt，也不 commit/push/重复调整 GitHub 状态**。明确 `B0_METADATA_COMPLETE_FOR_NON_REPARSE_SCOPE`、`B0_PARTIAL_OR_BLOCKED` 和 `B1_COPY_NOT_AUTHORIZED`；不能自证备份完成。

## 4. 其它全部未授权

不读取受保护 JSON/NPZ/MAT/CSV/PDF/源码内容、不计算任何文件 hash；不执行 `git status` 无界扫描、`robocopy`、`Copy-Item`、`New-Item`、`Remove-Item`、`Move-Item`、git reset/clean/stash/checkout 或临时 index 操作；不创建目录/快照、不启动 VSS/VM/VHD、Windows安全攻击或数据模型；不接触其它仓库、原 worktree 的上级路径或 symlink 外部目标。不将本 B0 许可自动迁移到 B1/实验 fixture 或科学认证。

V0.0.4仍 `CLOSED__BLOCKED__G0_FIXTURE_ISOLATION_UNPROVEN__NO_EXPERIMENT`，V0.0.5整体仍主研究未冻结，`NEXT_BASELINE_ADOPTION=UNDECIDED`，D3-real/D4-real（科研验证）仍未授权，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧科学/数据预算不变。清理真实目录及 V0.0.6 也未获授权。

**终点：`WAIT_ASTRA_B0_CONSOLIDATED_REVIEW / STOP`**。B0 阶段内仅交付一次完整成果，下一次 GitHub 更新合并到下一个有实质进展的里程碑，不再为正常步骤分别提交文档。
