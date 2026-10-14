# V0.0.5 最终版本验收与限制性关闭

2026-10-14（Asia/Shanghai）

**终态：CLOSED__LIMITED_BACKUP_AND_ALIGNMENT_ACCEPTED__MAIN_G0_UNPROVEN__CLEANUP_DEFERRED__WITH_OBSERVATIONS**

这是 V0.0.5 的**行政/工程版本收尾**，不是原主计划已正式冻结并完成、可信可弃用敌对 Windows 实验根 G0 PASS，也不是 A16/window、C9 或 Results 接受。原主 \`versions/0.0.5/plan.md\` 始终 DRAFT；已冻结的 B0/B1/B2/B3 及 C 盘备份目录辅助门各自证据与终态保留不追改。

## 一、证据与范围

Astra 在 GitHub 上核对 V1.2、Owner 2026-10-14 的投稿成果优先路线、V0.0.5 子门固定计划、B3 有限验收及当前文档身份；**无法直接访问 Windows C:/D:、Codex 本地原始 inventory 或最新本地对齐说明的文件内容**。以下 B3、本地文档和清理分类事实都属 Codex 的 \`CODEX_REPORTED_WITH_LOCAL_RECEIPTS\` / \`CODEX_REPORTED_WITH_LOCAL_REPORT\`，不写成 Astra 独立运行验收。

B3 单独有限接受（[固定验收](b3_acceptance.md)）：按 Codex 回报两个准许源根**90,766 个普通文件、1,804,958,786B** 完成保全，目标每文件 SHA256 共90,766匹配、失败0；Windows源句柄身份守卫9个内存回归和一次 canary 通过；单reparse仅保存332B被动说明，外部目标0访问；C盘限定Git fsck及5样本恢复通过。**只接受已经证明的普通对象字节和有限恢复，不认可项目完全自包含恢复**：EXTERNAL_DEPENDENCY_UNBACKED、ACTIVE_LINK_NOT_RECREATED、POINT_IN_TIME_UNPROVEN、ADS/ACL/NTFS恢复未知和完整D2/A16 FAIL_CLOSED保持。B3额度消费完毕，不自动B4。

## 二、本轮最终对齐回报的审计

Codex \`V0.0.5_FINAL_ALIGNMENT_AND_CLEANUP_INVENTORY_RESULT\` 说明已读治理固定 \`177501e668981d9a6bf36613e7a56203f788912c\` 的7份正文：
- 仅新建本地 \`docs/CH5_LOCAL_AUTHORITY_ALIGNMENT_V005_20261014.md\`，3,369B；按本地报告 UTF-8/LF与中文内容可读、内容仅为治理指引；**这只是本地新增对齐说明，不是已有 \`CURRENT.md/TASK_CURRENT.md/REVIEW_GATE.md\` 或两旧路线图已被改写/全文同步**。本地 \`CURRENT.md\` 仍显示V0.0.2旧时态，原dirty受保护文档/2份dirty源码原位未动。
- 模型真实本地HEAD依Codex回报仍 \`a1db8c114dec0ab69d69a5576e153a7f868cba0e\`、staged0、tracked dirty 8；仅新增一份未跟踪说明，使untracked **5,947→5,948**，ignored 4,553未变。本地Git原index及dirty前后摘要报告相同。网页治理HEAD与此模型代码HEAD不是同一提交、branch或工作树。
- 上述**3,369B新说明是在B3源集合冻结/快照完成之后产生**，因此不在原 B3 的90,766个文件内。不能把最新实时本地文件集仍称作B3时点的完全快照；这不推翻B3已接受的**原时点**普通文件哈希证据。GitHub当前版本摘要和该本地说明属于并行治理通道，不能自动推断相互全文同步。
- Codex报告两次只读汇总步骤分别有终端编码与计数表达式错误，依赖写入均未触发，修正后退出0；未对B3快照作任何变更，原错保留于用户报告，不虚构独立原始执行链。

## 三、旧目录清理结论（STOP，删除0）

报告所列模型源 \`B3时点\` 互斥分类：
| 分组 | 文件数 | 普通逻辑字节 | 终态 |
|---|---:|---:|---|
| TRIVIALLY_REGENERABLE 缓存**候选** | 73 | 2,112,602 | UNKNOWN_DEPENDENCIES / KEEP |
| HISTORICAL_EVIDENCE_KEEP | 74,046 | 1,080,840,496 | KEEP |
| ACTIVE_DIRTY_KEEP / 代码及治理依赖 | 2,112 | 63,542,502 | KEEP |
| UNKNOWN_KEEP | 394 | 4,053,823 | KEEP |
| **和** | **76,625** | **1,150,549,423** | 分类账与B3模型树数值一致 |

\`PROTECTED_KEEP\`可能嵌于历史证据类，不能重复累计。没有获得目录级 \`DUPLICATE_CANDIDATE\` 独立证明；\`POTENTIAL_SAFE_CLEANUP=0\`。样本缓存候选 \`.pytest_cache\` 及15个 \`__pycache__\` 目录仍缺当前依赖/再生/源新增检查，暂留；本次**未删除、移动、重命名任何对象**。V0.0.1–0.0.3 历史执行证据、保护科学资产、active dirty、Git linked-worktree common-dir及其它56个登记的 worktree 管理记录均保留；所谓56只来自Git元数据列表，**未探测其它 checkout**。旧历史实验记录保留不等于重复冗余已证实。

Owner早前提出“备份之后清理”，但**没有满足足以支持不可逆删除的准确名单**。为了避免失去科研原证，Astra决定不追加清理微任务/不可逆动作；保留 \`CLEANUP_DEFERRED__ZERO_DELETIONS\` 并留未来独立维护窗口，经准确清单、恢复性与Owner逐项批准后方可处置。该决策不宣称完成了物理清理。

## 四、主目标及科学硬停

V0.0.5 主 \`TRUSTED_BOOTSTRAP_ROOT / ANCESTOR_ISOLATION\` 尚未取得独立供应可信可弃用根、祖先隔离实证，G0未通过，旧V0.0.4的12项 hostile fixture场景仍无有效通过记录。**原V0.0.5核心目标归类 \`BLOCKED_UNPROVEN / NOT_ACCEPTED\`，仅行政关闭子门和进度**；不冻结追认原DRAFT为PASS。不自动启动V0.0.6，也不把C系统卷备份目录或D科研树当可攻击fixture。

Owner已采纳 [投稿成果优先战略](../../docs/CH5_PUBLICATION_FIRST_STRATEGIC_ROADMAP_20261014.md)；下一科学版本需Owner手动启动并重新审议范围，不允许从B3的备份访问授权推导科研D3-real/D4-real权限。A16 UNRESOLVED/FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧CLOSED科学预算、人口/人均与禁止N=P/3仍有效。
