# V0.0.5 B3 正式冻结：Python3.11 身份守卫修正、备份与文档集中对齐

日期：2026-10-14（Asia/Shanghai）

**FROZEN__V005_B3_IDENTITY_FIX_BACKUP_AND_DOC_ALIGNMENT__SEPARATE_CHAT_AUTH_REQUIRED**

这是现有 V0.0.5 内的一次**工程缺陷集中返修与完整备份长任务**，非新主版本。B2已按原合同 BLOCKED_PRE_COPY 关闭，其零重试许可不重开。本 B3采用新的单次独立预算，并须本文件固定 Git 提交 + Astra 独立会话授权。Owner希望先诚实结束 V0.0.5，已采纳论文优先战略从下一次由Owner手动启动的 V0.0.6起安排新科学目标。

## 一、聚焦错误与最低安全回归

Python3.11 官方文档规定 Windows 下 DirEntry.stat() 的 st_ino/st_dev/st_nlink 始终为零；不能将其与另一次 os.stat() 的身份字段直接比较，也不能据此推断无硬链接。

Codex必须在首次读取真实科研正文和首次新建C快照之前，**仅以内存中的合成数据/伪 stat_result 对象**修正并测试身份比较器：
1. DirEntry.stat只可作受界枚举与类型辅助；不将其三个零字段用作真实文件身份。
2. 对许可根内普通、非reparse文件，应评估 os.stat(path, follow_symlinks=False)、打开后 os.fstat(fd) 或等效只读句柄身份，取得同一可比较API语义的非伪造 dev/ino，核实最终打开对象仍为许可成员；前后身份/类型/有效性不符即 STOP。不得只依路径名、size/mtime一致便取消身份守卫；若Windows API或句柄可比性未获证实，标 SOURCE_IDENTITY_NOT_PROVEN 并停止。
3. 至少覆盖零值误报用例、真正不同对象ID、无有效ID、reparse不跟随、hardlink字段UNKNOWN不假冒无硬链接，以及异常必须阻断后续打开/复制。结果分类为在本机聚焦回归通过或缺证停止，不假定A16完整敌对保护通过。
4. 如果需要轻量运行态canary，可在不读取源内容的前提下，对**单个从允许集合中选出的普通非reparse文件**执行一轮只读 open + handle身份查询，计入单次许可；不扫描未知外部依赖、不读取正文。该canary失败应在任何C快照写入前停下。
5. 不能通过删除identity guard、强行接受零号、禁用源变化校验、取消reparse检查或引入默许外部访问取得PASS。对敌对同用户祖先替换等完整D2保护继续 FAIL_CLOSED。

## 二、文档对齐放在同一长任务

Astra此次集中更新 GitHub 动态文档，Codex须从本 B3 **固定提交**读取本计划、b2_acceptance.md、CURRENT.md最新前缀、CH5_VERSION_REGISTER_CURRENT、DOC_INDEX_CURRENT、CH5_PUBLICATION_FIRST_STRATEGIC_ROADMAP_20261014、V1.2工作流及旧B2固定计划。

核验并在最终报告分开写明：文档治理HEAD不是原代码工作树HEAD，不是main；B2已CLOSED/BLOCKED且新B3是独立授权；Owner采纳的论文优先战略已存在但下一科学主版本V0.0.6尚未启动；V0.0.5原可信敌对fixture G0仍未证明。任何冲突只生成脱敏的对齐差异建议，不直接改动本地原模型工作树的dirty治理文件/源码，不执行 git reset/clean/stash/checkout/pull、切分支、覆写索引或GitHub自动推送。原本未提交及ignored科研成果绝不可为“对齐文档”而被覆盖。

## 三、唯一允许的备份资源范围

源A：D:\ProjectTemp\c5k1bturn56 （linked worktree）；源B：D:\ResearchCode\dissertation-ch5-two-asset-hank\.git （Git common-dir）。只在两源根本身及内部读取获准普通文件，包括tracked dirty、untracked/ignored、sealed/run004、所有必要shared/private Git管理字节，仅用于COPY/SHA256/校验与恢复；不授权科学数据解析或消费者。仅允许唯一目录reparse对象自身的被动类型/链接原始描述（最多64KiB），**外部链接目标 open/stat/exists/read/list/hash 全部0**，不能在备份中重建指向原目标的活动链接。出现其它reparse/未知外部依赖即STOP。

目标根：C:\CH5_Research_Backup；唯一目标（必须创建前不存在）：
C:\CH5_Research_Backup\CH5_B3_IDSAFE_PASSIVE_LINK_20261014_01

仅允许在唯一新快照内创建 project_tree、git_common_raw、inventory、receipts、restore_check 和必要tools内部文件/目录；不覆盖/清理此前B1/B2目标或旧快照。不更改C卷现有ACL、加密、账户或系统配置，Owner已接受可能的同用户本地明文副本。私人文件名单、原摘要、原始reparse信息和错误回执只能在新C快照LOCAL_ONLY，保留待Owner后续处置；绝不上传GitHub或复制其它科研项目。

## 四、一次完整长任务和预算

执行顺序：固定权威 → 文档只读对齐 → 身份检查兼容修复与合成回归 → 单个无正文身份canary(必要时) → 两源根及链接无跟随清单 → C卷实时容量/目标不冲突准入 → 独占快照首次创建 → 全部批准普通文件从已核实源句柄复制并SHA256 → 各目标文件独立SHA256核验 → 源集合稳定性复查 → C快照内完全隔离的Git恢复核查 → 一份脱敏集中报告。

C实时空闲必须满足当前逻辑源容量S + 64MiB工具 + 512MiB私有清单 + 128MiB恢复副本 + max(20%×S,10GiB)；若身份或容量/目标准入失败，写入0。不得换备份名、覆盖或自动重试。

硬上限：源普通/特殊文件≤100,000、目录≤7,000、深度≤128、普通源逻辑字节和目的普通文件复制字节分别≤4GiB；单次≤2小时、同时复制/验证进程≤2、自动重试0。每文件源正文读取最多2次（失败预扣），目的完整哈希读取最多1次；恢复视图额外副本读取另记账并保证不回到原D源。tools/操作性材料≤64MiB，inventory+receipts≤512MiB，restore_check新建≤128MiB，公开脱敏报告≤128KiB。

目标链接只保全描述，不跟随。Git linked-worktree副本的 .git 指针会原样指回旧D时，严禁直接运行该副本的Git命令；只在 restore_check 复制视图中将Git-dir/common-dir/worktree绑定到新C快照，禁止hooks/fetch/GC及对原代码树、原始备份的修改。若无法证明真实D盘不会被读/写，恢复验证STOP。

任一异常（identity未验证、reparse变化、权限不足、锁占用、源集合变化、字节哈希不符、容量/时间/额度不足、Git外部依赖、路径竞争）立即STOP、保留当前现场，0自动重试和0额外目录替代。本轮不删除、迁移、git clean/reset/stash、创建VSS/VM/VHD、改ACL/提权、运行A16敌对攻击和 HJB/KFE/C8/C9/C10/GE/Results；模型激活和真实科学D3-real/D4-real许可不因备份升级。

结果分账：B3_BLOCKED_PRE_COPY；B3_INCOMPLETE_PARTIAL；或 B3_LOCAL_OBJECTS_BYTE_VERIFIED__EXTERNAL_LINK_UNBACKED__TIMEPOINT_UNPROVEN（必须全部允许普通成员字节校验并有足量Git恢复证据才可成立）。即使普通备份通过，外部链接目标仍UNBACKED、主动链接不重建、全树同一时点与完整D2/A16仍NOT_PROVEN；不得自称无保留FULL_VERIFIED_BACKUP。

仅在源普通文件备份有明确有效的恢复资格后，允许在同一最终报告附**非破坏性的旧版目录清理候选分类**，不得物理删除或迁移；具体清理须Owner单独审议准确对象和恢复路径。

一次性回报：V0.0.5_B3_IDENTITY_FIX_BACKUP_AND_DOC_ALIGNMENT_RESULT。包括身份修复合成测试、源/目标使用及预扣读账、成员数/字节数/哈希与Git恢复、链接保全限制、Doc alignment冲突类别、耗时/错误/预算及所有UNKNOWN。停点：WAIT_ASTRA_V005_CONSOLIDATED_REVIEW_AND_NEXT_VERSION_DECISION / STOP。

**若B3再次安全阻塞：不自动启动B4或不断重试；Astra应集中评定V0.0.5有限完成/阻塞并诚实保留原G0，待Owner手动立V0.0.6后执行成果优先路线。**
