# V0.0.5 B3 Astra 集中验收：获准普通对象逐文件备份成功（有限）

日期：2026-10-14（Asia/Shanghai）

**裁决：CLOSED__ACCEPT_B3_LOCAL_OBJECTS_BYTE_VERIFIED__EXTERNAL_LINK_UNBACKED__TIMEPOINT_UNPROVEN__WITH_OBSERVATIONS**

## 固定计划与本轮证据来源

B3 冻结计划 commit 198a9204fbc3b73da1cd3f59095d5ecc54e4f06b，blob e4e70109e3401b455ef00fd0a603a86eb95c613d；固定路径 versions/0.0.5/b3_identity_correction_backup_plan.md。原 B2 冻结与安全停点不追改。Astra通过GitHub独立核对治理分支、固定计划及源文件，不具备本地Windows主机和C盘原始receipts读取能力。以下所有执行、文件哈希和恢复操作结果来自 Codex 交付的 V0.0.5_B3_IDENTITY_FIX_BACKUP_AND_DOC_ALIGNMENT_RESULT，统一标 CODEX_REPORTED_WITH_LOCAL_RECEIPTS，不使用 INDEPENDENTLY_VERIFIED_WINDOWS 字样。

## 一、已报告的实际结果与冻结核对

唯一C盘快照：C:\CH5_Research_Backup\CH5_B3_IDSAFE_PASSIVE_LINK_20261014_01。

| 来源 | 文件 | 目录含根 | 普通字节 |
|---|---:|---:|---:|
| D:\ProjectTemp\c5k1bturn56 (linked worktree) | 76,625 | 5,877 | 1,150,549,423 |
| D:\ResearchCode\dissertation-ch5-two-asset-hank\.git (shared/private Git) | 14,141 | 448 | 654,409,363 |
| 合计 | **90,766** | **6,325** | **1,804,958,786 B** |

获准普通文件全部复制，目标SHA256 90,766匹配、0失败；每文件源最多2次完整读、目标一次完整hash读。实际读取预算预扣 181,532 (= 2 × 90,766)，目标完整哈希读取90,766。源前后枚举成员、句柄真实身份、size/mtime/nlink及唯一链接被动描述报告一致，观察变化数0，但**不证明全树同一时点一致、恶意祖先替换不可能或完全D2的A16/window安全**。

身份修复：不用Windows os.DirEntry.stat的虚零ID，采用只读 Windows GetFileInformationByHandle 的卷身份+文件ID且核类型/reparse/opened handle/最终路径；9项内存合成回归PASS、0失败，1个无正文身份canary通过。只支持本次备份身份保护。普通文件多硬链接计数报告未发现，ADS未枚举、ACL/完整NTFS属性未验证。源工作树/HEAD/index/refs据Codex报告未主动写入；本次不借它主张全部原始源字节可独立证明永久未变。

唯一reparse对象以332B LOCAL_ONLY被动描述入库且回读验证，未激活链接、外部目标访问0，保留 EXTERNAL_DEPENDENCY_UNBACKED / ACTIVE_LINK_NOT_RECREATED。**不能将副本宣称完全自包含的项目运行环境**。

隔离Git恢复在C快照内：Git-dir/common-dir/work-tree报告均指向C内、HEAD正确、staged0、refs检查和git fsck --full exit0，5个代表样本hash一致（含2 dirty源码、普通源码、untracked文档和ignored候选）；ignored语义未重判。Git内部读取字节量 UNKNOWN，此处仅限已获准恢复视图的结构/对象检查，不是原外链可运行恢复的科学验收。

主体942.672秒/exit0/错误0/重试0；最多2个并发复制或核验进程；6个Git恢复子进程串行。峰值工作集291,258,368B；inventory+receipts 46,521,454B (低于512MiB)；restore_check 15,001,368B (低于128MiB)；tools0B。唯一reparse链接描述332B (低于64KiB)。相对于B3上限100k文件、7k目录、4GiB普通源/复制字节、2小时，所报告计数均未超限。Git隐式恢复读取统计UNKNOWN、系统访问时间影响未独立认证，不虚构其PASS。

## 二、精准资格判定

**有限通过**：获准两个本地源根中全部非reparse普通文件的逐个源→副本字节匹配（按Codex本地原回执）；Windows身份误报已得到受界实现修正；Git结构/对象完整性及少量样本隔离恢复；外链被动元数据保存且不访问外部目标。

**不通过/未验证**：外部reparse目标内容、活动链接恢复、ADS、所有ACL及NTFS元数据精确恢复、原科研消费来源认证、全树真实时间点/应用一致性及完整A16/D2/窗口保护。不得写 FULL_VERIFIED_BACKUP、SCIENCE_ACCEPTED、Results TRUE、GE或C9已恢复。

按冻结标准，此次 B3 子门关闭并有限接受，消耗预算不再自动重用、不自动开启B4。旧目录删除/移动尚未发生，Codex仅作六类宏观分类，**没有具体绝对删除对象清单**，所以不能进行物理清理；原科研证据、active dirty、Git依赖、protected及UNKNOWN均KEEP。

## 三、V0.0.5主目标及最终收尾门

原 V0.0.5 主 plan.md 可信首次可弃用敌对fixture根尚属 DRAFT/UNPROVEN，未有 G0安全实验PASS；V0.0.4仍CLOSED/BLOCKED。当前 V0.0.5 **仅剩本地文档时态对齐、旧版本目录准确只读清理候选与 Owner最后不可逆取舍**，不得将这些完成与主G0科学目标混同。

Owner采纳论文成果优先路线，**只在Owner手动启动V0.0.6后正式开启后继科研任务**。本门没有任何科学solver/真实D3-real/D4-real、HJB/KFE/C8/C9/C10/GE/Results或攻击实验授权，旧A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧CLOSED科学预算及不N=P/3不变。

本裁决不授权再次复制、对唯一已接受快照作覆盖或清理，也不授权D盘项目目录物理删除。