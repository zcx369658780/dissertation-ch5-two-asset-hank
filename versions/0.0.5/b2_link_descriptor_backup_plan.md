# V0.0.5 B2 正式冻结：方案A被动链接保全 + 全普通文件非覆盖复制校验

日期：2026-10-14（Asia/Shanghai）

**`FROZEN__V005_B2_PASSIVE_LINK_DESCRIPTOR_AND_NONREPARSE_BACKUP__AWAIT_SEPARATE_CHAT_AUTHORIZATION`**

本文件是继 B1 `CLOSED__BLOCKED_PRE_COPY__UNAUTHORIZED_EXTERNAL_DEPENDENCY` 后的新冻结备份子门，不是对 B1 的修改/重试。本门用一份**完整长任务**涵盖准入、复制、全员哈希、集合复核、链接限制登记、隔离恢复与非破坏性清理候选建议，不使用GitHub微提交中转。

## 1. 精确 Owner 决定与受限资格

Owner 已于 2026-10-14 同意**方案A**：仅保全第五章项目源树中唯一一个目录 reparse 链接对象的**位置、类型、reparse tag/可获得的原始链接描述及目标描述**，**绝不读取、枚举、复制或访问链接指向的外部内容**；同时明确披露链接和环境无法自动恢复的限制。敏感的相对路径及目标路径/原始 reparse payload **仅写入本机 C盘私有 inventory**，不得发GitHub、聊天公开原串或将它转变为能主动指向真实D盘的复制链接。允许对当前唯一链接对象自身做必要不跟随只读查询；不许可外部目标 stat/exists/resolve/open/read/hash。

此前 Owner 批准的 `D3-backup-byte / D4-backup-local` 仅**备份目的**继承为本次 B2 的单独授权范围：两个批准源根中的所有普通文件，包括 dirty/untracked/ignored、sealed/run004 和 shared/private Git 元数据可按下列硬配额仅做原字节复制、SHA256与保全验证；不得科学解析、调用模型/consumer或取得历史D3-real/D4-real科研使用权。Owner 接受 C卷现有保护条件下可能存在的**本地明文副本**，但本任务不得更改ACL、加密、账户/卷/VSS或提权；所有敏感清单、日志和文件SHA只在新 C快照 LOCAL_ONLY 保存，直到Astra验收及Owner以后作保留/销毁决定。不得发布原始日志/文件/敏感名称到GitHub。

这次**仅修改因Owner新批准所允许的链接处理政策**：外部链接目标是`DECLARED_EXTERNAL_DEPENDENCY__NOT_COPIED`而非必须在复制前阻断；除此之外仍遵照原 B1 对普通文件、源/目的资格、时间窗口、失败和科学保护的严格标准。**不能因新政策把丢失链接依赖的快照称为完整可复现的全部科研环境**。

## 2. 唯一允许源根、备份路径与链接处理

源A：`D:\ProjectTemp\c5k1bturn56`（linked worktree完整本地字节，含全部未提交/ignored）；  
源B：`D:\ResearchCode\dissertation-ch5-two-asset-hank\.git`（Git shared common-dir及本工作树private Git-dir/index）。  
仅对这两个源根自身和内部做不跟随链接的读取及枚举；外部依赖 **0 access**。不得触碰其它checkout树、修改原Git/HEAD/index/refs、源历史封存或其它C/D路径。

目标根：`C:\CH5_Research_Backup`；唯一新、必须预先不存在的独占快照：
`C:\CH5_Research_Backup\CH5_PROJECT_LINK_DESCRIPTOR_20261014_B2_01`

该快照下只允许建立 `project_tree\`、`git_common_raw\`、`inventory\`、`receipts\`、`restore_check\`、必要时 `tools\` 容器及内部复制/保全/隔离验证对象，不覆盖已有内容、不重命名换路径、不删除或清理失败现场。

**唯一目录reparse**：在本次严格非跟随登记中如果且仅如果识别出同一允许项目内的**唯一**目录reparse，才允许从该对象本身捕获链接类型/描述（最大单对象描述64KiB；原始位置及目标详细文字LOCAL_ONLY），把它作为**被动清单记录**保存在 `inventory\link_descriptor` 命名空间下；project_tree 内对应位置不可递归穿透，不创建任何能激活外部指向的 junction/symlink/mountpoint，不得假装实际还原。若类型未知/无法无越界读到对象本身的必要描述，记`LINK_DESCRIPTOR_INCOMPLETE`、视对保全资格的重要性转入PARTIAL/安全停止；如果发现第二个或全新的其它链接、链接目标需要实际访问才能解释、安全读对象不可实现、竞态/根身份改变，`STOP`，不自动扩权。**方案A的区别是：已知的一处外部链接仅登记并允许普通源文件继续复制；不是允许跟随或跳过未报告依赖。**

原始链接对象在普通目录树副本的重现资格明确记为`PASSIVE_LINK_ONLY`、`ACTIVE_LINK_NOT_RECREATED`。对于未备份的目标内容，后续恢复者需独立供应/重建目标资源，且须重新批准其身份/权限；`EXTERNAL_DEPENDENCY_UNBACKED` 不因复制成功消失。

## 3. 一次长任务的执行与验证

Codex 在原第五章 Windows 普通用户环境中，以**一项任务自主完成**：
`FIXED_AUTHORITY → ROOT/SOURCE_AND_LINK_PREFLIGHT → CURRENT_SOURCE_INVENTORY → REALTIME_C_CAPACITY → EXCLUSIVE_CREATE → COPY_AND_HASH → SOURCE_SET_RECHECK → ISOLATED_RESTORE_TEST → SANITIZED_FINAL_RESULT`。

**前置零写**：验证仅两个源根及C备份根的对象身份、非reparse根、合法读/写能力、源文件数/目录数/逻辑S及唯一reparse自身描述；使用不会追随junction/symlink的系统API，禁止探测其外部目标。识别额外外部 Git alternates/LFS等依赖时只登记元信息并按必要性BLOCKED或标限制，不自动打开/获取。查看C卷当前可用空间、准确目标是否存在和当前目的父目录非reparse，确认写入许可及容量`>= S + 64MiB + 512MiB + 128MiB + max(20%S,10GiB)`，拒绝容量未知/目标已存在/来源不可审议。预检通过后创建唯一新快照，否则**0写/STOP**；不得重用B1快照名。

**复制与哈希**：按当前精确 inventory 复制所有两源根内普通文件、空目录及必要项目元数据，不按Git ignore过滤；复制时计算源SHA256，并独立从每份目的普通文件**完整读取一次**复核SHA256和逻辑size。每源普通文件可完整正文读最多**2次**（含重验/变更检测），目的核验正文最多**1次**，失败读也计数。全过程绝不删除源、改原Git工作树或覆写副本；若源对象替换、文件增减/修改、路径溢出、权限/锁/ADS/硬链接或Git外部依赖所需信息越出许可，立即STOP并保留`INCOMPLETE`现场，若安全可得到有限普通文件副本也只能报PARTIAL，不能重跑已耗预算。

**恢复性**：仅在 C快照 `restore_check\` 内对备份视图作隔离的 Git可用性/HEAD/index/refs/objects检查。原样复制的linked worktree `.git` 指针指向真实D盘时**禁止直接运行Git**；必须在隔离视图内令 Git-dir/common-dir/worktree 全部解析到同一新C快照内部，防联网/fetch/hooks/GC及源Git写入。恢复检查选择代表性普通源码/dirty/untracked/ignored副本，不能对sealed科研文件作内容消费。原始副本 `project_tree\`/`git_common_raw\` 不得为验证而修改；对 `restore_check\` 操作计入限额。

**时点/保护**：逐文件SHA和源集合两次枚举一致，不等于全树同一时间点，也不等于完整D2的恶意同用户攻击保护；VSS/提权/进程终止仍0许可。Codex 必须按实际证据单独报告 `SOURCE_SET_STABILITY`、`PER_MEMBER_BYTE_EQUALITY`、`GIT_RESTORE_READINESS`、`POINT_IN_TIME_CONSISTENCY`、`EXTERNAL_LINK_RESTORE_LIMitation` 与旧 `A16/window`。未验证的条件不能自行PASS。

完成备份验证后只允许**基于本次获准的源集合清单**提交非破坏性旧版本目录分类概述（可重建/重复候选 vs 必须保留的科学原证/dirty/git/protected/UNKNOWN），**不允许实际清理、移动、重命名或重新读取旧 protected 正文作删除取舍**。

## 4. 精确资源上限及硬停止

- 单任务时限 `<=2小时`、复制/核验进程`<=2`（优先单个）、自动重试0；超过硬预算不换新版本名补跑，不扩权限。
- 普通/特殊文件 `<=100,000`，目录`<=7,000`，源普通文件逻辑字节`<=4GiB`，目录深度`<=128`。唯一被动链接元数据单对象`<=64KiB`，链接目标实际读取0。任何新增其它reparse或未批准外部依赖必须停止/汇报。
- 每普通文件源字节完整读取`<=2`次、目的完整hash-read`<=1`次；普通数据目的字节`<=4GiB`。
- 工具/操作性材料`<=64MiB`，本地私有清单与回执合计`<=512MiB`，C盘隔离恢复检查新建`<=128MiB`，公开脱敏报告`<=128KiB`。额外NTFS元数据/物理分配不可先验精准预测，C卷容量须满足10GiB以上保留余量。
- `/MIR`、`/PURGE`、`/MOVE`、`git clean/reset/stash/checkout`、破坏/覆盖真实数据、任意文件删除、额外卷/账号/VSS/VM/ACL更改、对外链目标访问、Windows敌对攻击与科学 HJB/KFE/C8/C9/C10/Results 调用均 **0**。
- 任一步根身份异常、非跟随遍历失效、链接对象类型超过本许可、权限/容量不足、超时、失败/竞争、恢复视图可能访问真实D目录，**必须 STOP 并保留现场**，不可借“全量备份”目的绕过。

## 5. 证据等级及终止

B0 历史数字仅参考：90,766普通文件/6,325目录/1,804,958,786 B普通数据、C可用643,058,806,784 B（来自Codex本地报告）。**实际覆盖与一致性须本次重新只读登记**。

仅可按实际证据报告：
- `B2_BLOCKED_PRE_COPY`：未创建快照或实际写入前安全门失败；
- `B2_INCOMPLETE_OR_PARTIAL`：复制中断或部分成员不符；
- `B2_APPROVED_LOCAL_OBJECTS_BYTE_VERIFIED__EXTERNAL_LINK_UNBACKED`：允许源根中全部普通文件全量字节核验、被动链接描述保存与限定Git恢复检查达到实际报告等级，**但链接目标内容、活动链接恢复、完整时间点与旧D2均不得宣布PASS**。

**不得使用不带资格范围的 `FULL_VERIFIED_BACKUP` 结论**。若任何源普通成员未覆盖或Git恢复未验证则进一步降低结果资格。无论何种终态，C盘备份不能充当 V0.0.5 主任务的可信可弃用攻击 fixture。原 V0.0.5 版本主plan继续DRAFT，`NEXT_BASELINE_ADOPTION=UNDECIDED`，D3-real/D4-real科研消费、旧A16/window/C9/Results和V0.0.6都不因备份而解封。

单次集中交付：`V0.0.5_B2_LOCAL_OBJECT_BACKUP_WITH_PASSIVE_LINK_RESULT`，必须报告脱敏成员/字节/hash/链接/外部依赖/ Git隔离恢复/预算/失败类别/未知项，以及旧版本目录仅分类**建议**。**停点：`WAIT_ASTRA_B2_BACKUP_ACCEPTANCE_AND_CLEANUP_REVIEW / STOP`**。本版内不再为每个普通步骤提交GitHub。
