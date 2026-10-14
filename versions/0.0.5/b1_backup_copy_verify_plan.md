# V0.0.5 B1 正式冻结：完整本地项目非覆盖保全复制、全字节校验与隔离恢复

**日期：** 2026-10-14（Asia/Shanghai）  
**状态：`FROZEN_B1_BACKUP_COPY_VERIFY__AWAIT_SEPARATE_ASTRA_CHAT_AUTHORIZATION`**  
**用途：** `BACKUP_OPERATIONS_ONLY`；不是旧 A16/window 安全实验，不是论文数据来源认证，也不是 V0.0.5 可信根主计划整体冻结。

## 1. Owner 已同意的 D3-backup / D4-backup 和不可追改边界

Owner 已确定 **整个第五章本地项目**全量保全，随后验证、清理旧版本目录，并接续 V0.0.5 主目标。B0有限回报 [已另行归档](b0_acceptance.md)。Owner进一步**明确同意**：
- **D3-backup-byte**：只为原字节保全，允许在下述两个固定源根内对普通文件（包括历史 `sealed/run004`、dirty、untracked、ignored、Git元数据）读取/复制、计算SHA-256，并在目标中验证；不得 JSON/NPZ/MAT等科学解析或调用科研consumer。与 D3-real/D4-real 科学访问无关，旧三文件2.125MiB限额不转移；
- **D4-backup-local**：新备份只在指定 C盘快照、沿用 C盘现有安全配置（**可能是明文、可能包含敏感内容**）；不擅自更改ACL、不启用磁盘或目录加密、不生成网络/云端副本。完整路径清单、敏感文件摘要、原始 stdout/错误、私有身份数据保持 `LOCAL_ONLY`，保存至 Astra 验收及 Owner 后续决定，**不自动销毁**；公开仅脱敏计数、容量、错误类别和证据等级；
- 仅对 B0 已发现的**唯一目录reparse对象自身**查询 reparse 类型及指向信息，**不跟随链接访问目标**。如果涉及两个允许源根以外的依赖，记 `UNAUTHORIZED_EXTERNAL_DEPENDENCY`，不得自动读取或扩大范围；
- 0文件删除/清理，0 VSS/提权/管理员配置/Windows攻击，完整 D2/A16原合同继续 `FAIL_CLOSED`。**本版普通备份不被认定抗完整D2攻击的安全读窗口；若不能在实际对象和权限边界内安全打开某个受保护成员，必须在读取前停住或将本次备份判为PARTIAL，绝不以“备份许可”冒称A16 PASS。**

本门冻结后不得为取得成功修改上限、扩大源或改变排除/安全标准。授权只在固定提交公布后由 Astra **单独在同会话签发**，无额外GitHub微提交。

## 2. 固定绝对源根、唯一目的及写入集合

**源A**：`D:\ProjectTemp\c5k1bturn56`；**源B**：`D:\ResearchCode\dissertation-ch5-two-asset-hank\.git`。由Codex本地Git身份/此前B0回报确定。源根本身不得增删移改、改变index/refs/dirty/mtime或主动运行生成科学输出；不在其上级目录、新增repo或别人的checkout中写入。

**目的根**：`C:\CH5_Research_Backup`（此前 Codex 报告已空建）。**唯一新快照**：
`C:\CH5_Research_Backup\CH5_FULL_20261014_GATEB_01`

准许新建的**顶级子容器仅限** `project_tree\`（源A副本）、`git_common_raw\`（源B副本）、`inventory\`、`receipts\`、`restore_check\` 和可选 `tools\`；前两容器内部按照登记源目录建立必要的复制子结构。完整原字节/原始受保护manifest不得在其他位置创建。**目标已存在、根为reparse/不可信、创建竞争、容量异常即STOP**；不改快照名、不覆盖、不删旧快照、不使用 `/MIR`、`/PURGE`、`/MOVE`。目标对象写入可用当前普通账户与既有OS配置，**禁止更改本机ACL/账户/加密设置**。

源或目标内不自动跟随symlink、junction、mount/reparse，不运行链接指向目标的代码。源链接对象本身允许作只读元数据/链接payload记录，若不能安全在副本中保存其恢复语义，清晰记 `LINK_RESTORE_UNVERIFIED/PARTIAL`；禁止在目标创建会主动指向真实 D盘的活跃 reparse 链接。未知ADS、hardlink关系或必要NTFS属性无法无额外越权保全/核验时同样记录缺口，不能称完整可恢复备份。

## 3. 一次长任务内完整流程及 fail-fast

`AUTHORITY → SOURCE_IDENTITY_AND_REPARSE → CURRENT_INVENTORY → DESTINATION_AND_CAPACITY → EXCLUSIVE_SNAPSHOT_CREATE → COPY → PER_FILE_HASH → SOURCE_SET_RECHECK → RESTORE_ISOLATED → FINAL_RECEIPT`。

**A. Preflight/准入，写入0**：只读核精确两个源根及目标根的目录身份/非reparse属性、Windows当前用户合法读取条件、单个reparse对象自身类型/链接字节（不得跟随）；核任何链接/ADS/hardlink类型与源root外依赖。只允许源根内不跟随链接的重新成员登记、容量及所需Git元数据身份核对，不扫描其上级或第三方checkout。不得运行带副作用的 Git checkout/status hooks/fetch。任一根替换、不可解释跨根依赖、权限/容量/未批准技术能力、无法防止危险链接解析时在**创建前停下**，留下 `BLOCKED_PRE_COPY`。B0历史统计不是实时快照，也不强制新数量等于旧计数，但必须报告新增/减少/变化及其一致性影响。

**B. 创建独占快照**：先核冻结目标唯一、父目标普通且非reparse、容量准入；目标必须原先不存在。只允许建立上述新快照及其内部目录、LOCAL_ONLY清单/回执/必要复制工具。目标写前至少满足当次登记普通源逻辑字节`S` 加恢复/工具/回执配额并预留`max(20%×S,10GiB)`，不能仅凭B0早期剩余空间代替此刻准入。所有子目录/文件均拒绝已存在目标、拒绝路径穿越、拒绝不受控reparse、禁止自动重命名冲突件。

**C. 复制、逐成员SHA256与集合复查**：按B0定义的完整源成员，不按Git ignore过滤，覆盖普通文件、空目录、dirty、所有封存科研原证和shared/private Git字节；固定结构里所有可安全读取的普通成员逐个以源句柄读入副本并在复制时计算源SHA256，随后从**副本独立读回一次**核SHA256/size；必要时源文件二次只读hash/元数据对照，确认未变化。**每个文件源正文最多两次完整读取、副本校验正文最多一次**，不得隐含其他 hash/download/retry；失败即停止依赖复制链，保留 `INCOMPLETE`。复制前后再做有界源集合身份/size/mtime类别复查，若发生新增/删除/源中途修改、竞争替换或不能证明同一对象身份，则 `INCONSISTENT_OR_PARTIAL_BACKUP`，不能拿逐文件hash断言全树同一时间点。保持原Git HEAD/index/dirty/refs与受保护文件不被主动修改，若观察到其它进程在写则报告一致性限制，不擅自终止进程。

**D. 被动链接与外部依赖**：唯一reparse可记录类型与链接payload（仅LOCAL_ONLY），**不跟随**。不自动访问/复制链接目标、不构造会指向真实 D盘的目标链接；无法证明完整链接恢复则 `PARTIAL_LINK_SEMANTICS`。Git alternates/LFS/submodules、ADS/hardlinks等若发现尚未获准的外部来源或流无法可靠保全，先记录缺口，必要时停止；**不作无声排除**。

**E. Git隔离恢复**：不能在原样拷贝的 linked worktree `.git` 指针上直接执行可能指向原D盘的Git命令。只在 `restore_check\` 下受限构造**回指目标备份common-dir**的恢复视图（不修改 `project_tree\` 或 `git_common_raw\` 原始备份），禁用 hooks、联网、GC及 refs写入；确认所有恢复命令解析的Git-dir/common-dir/work-tree均指向C快照内部，**若不能保证立即STOP**。使用只读机制检验HEAD/index/refs及必要object完整性、一般源码/dirty/untracked/ignored代表样本；不得科学解析protected内容，恢复读预算详见下节。全量对象完整/实际可运行恢复与样本恢复不同，不足则只能 `RESTORE_PARTIAL`。

**F. 最终证据**：保留本机 `inventory\`、`receipts\`、`restore_check\`（直到Owner后续指示，不自动清理），仅通过当前对话回传一份脱敏集中结果。不得为汇报编造Web独立复测，严格区分 `COPIED_BYTES`、`PER_MEMBER_HASH_VERIFIED`、`SOURCE_SET_STABLE`、`GIT_RESTORE_READINESS`、`TIMEPOINT_CONSISTENCY`、`FULL_D2_PROTECTION`。Codex成功自测也不能自授Astra最终验收。

## 4. 资源及对账硬上限

依据B0 Codex本地报告：源非reparse 90,766普通文件、6,325目录（含2源根）、1,804,958,786 B≈1.681GiB，最大深度8，reparse目录1，C盘可用643,058,806,784 B≈598.895GiB（**历史测量，不等于本轮准入**）。

- **整个源允许集上限**：普通/特殊文件`<=100,000`、目录`<=7,000`、源普通文件逻辑字节`<=4GiB`、深度`<=128`；reparse目标及外部未获批准依赖字节**不自动计入允许源范围**。受保护源文件亦计入同一文件/byte额度，不能另开旧许可账。
- **实施时限**：单次连续 B1 最长`2小时`；**零自动重试、零自动扩大配额、最多2个并发复制/校验进程**（优先单进程），无未经许可的VSS或外部快照写入。软调试只能在相同冻结额度内进行，不得绕过失败/硬停点重复扫描全部源。
- **读写**：每普通文件源正文`<=2`全次、目的哈希核验`<=1`次，失败读取也要记账；恢复视图内必要额外副本读取须单列并计入恢复预算，不得通过 `Git` 命令偷偷无界读取源。除允许创建C快照下的备份/清单/临时工具/恢复视图，**源、其它C/D位置、Git原repo写入=0**。
- **源普通数据副本逻辑字节<=4GiB**；额外 `tools/临时`<=64MiB、LOCAL_ONLY `inventory+receipts`<=512MiB、`restore_check` 新建内容<=128MiB；其它空间使用若超出冻结界限则STOP。目标物理分配/目录元数据/NTFS开销为UNKNOWN，容量准入需留**至少10GiB余量**，实际执行保留0额外卷/VM供应预算。公开报告≤128KiB，原始敏感数据只存指定快照，不上传 GitHub。
- 超限、未知外部依赖、权限拒绝、reparse意外目标、异常路径、重要数据流/链接保真不可实现、源成员变化或目标检查异常，立即保留现有副本和失败记录，**不可清理、覆盖或换快照名继续**。若安全情况下可以完成有限普通文件复制，但缺某个保护资格/链接语义，终态仅 `PARTIAL_BACKUP`，不得判 `FULL_VERIFIED_BACKUP`。

## 5. 必须分开的四种结果

- `BLOCKED_PRE_COPY`：创建前保护/容量/身份不成立，写入0。
- `INCOMPLETE/PARTIAL_BACKUP`：已复制某些字节，但有受保护读取/外部依赖/reparse/ADS/并发/存储/验证缺口；**永不能将这一快照标为完整可恢复**。
- `NON_REPARSE_BYTE_VERIFIED_BACKUP_WITH_LIMITATIONS`：所有本门可访问普通源字节逐个比对完成，但至少有链接保真/时间点/恢复性证据上限；不等于完整项目的原状态复原。
- `FULL_VERIFIED_BACKUP`：仅在批准源集合、所有必要链接和流/属性覆盖、全成员完整字节摘要、源集合稳定及能隔离恢复必要 Git 结构都可依据本地回执证明时成立；如没有可认证的时间点窗口，必须另标 `POINT_IN_TIME_UNPROVEN`，**不能将此结果用于证明全树同瞬间一致或旧A16/window。** 证据不足写 UNKNOWN/NOT_VERIFIED，不可为 PASS 改冻结标准。

备份后，Codex**只可提交旧版本冗余目录只读分类建议**（可以在同一集中结果附带宏观类别）；任何实际 `Remove-Item`、git clean/reset/stash、移动或重命名、删除旧目录/快照仍需未来精确Owner取舍和另门。不因Owner原“备份后清理”意向自动得到破坏性许可。

V0.0.5 可信独立可弃用实验根主 `plan.md` 仍 DRAFT/NOT_FROZEN，当前项目目录中的子树亦未证明G0。V0.0.4 CLOSED/BLOCKED、D1历史北京仅未来科学拟核验、D2全威胁范围保留、D3-real/D4-real科研消费NOT_AUTHORIZED；A16 UNRESOLVED/FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧科学/数据额度和不`N=P/3`不变。

**集中交付：`V0.0.5_B1_FULL_BACKUP_COPY_VERIFY_RESULT`，然后 `WAIT_ASTRA_B1_ACCEPTANCE_AND_CLEANUP_INVENTORY_REVIEW / STOP`。不为每个正常工程步骤创建GitHub微提交。**
