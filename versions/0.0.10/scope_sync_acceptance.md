# V010主线纠偏文档同步：Astra限定验收

日期：2026-10-15（Asia/Shanghai）。
**裁决：ACCEPT__DOCUMENT_SYNC_AND_SCOPE_ACK__LOCAL_RECEIPTS_REPORTED。**
**结论：Owner要求的“先让Codex同步一次”停点已经完成限定验收；不是V010科研实施、模型运行或版本关闭。**

## 1. 来源及独立核验范围

源仓库zcx369658780/dissertation-ch5-two-asset-hank；固定同步commit 916e2b47d3489f6eacd814b55cc568d92be4c9fb，tree 7e2cd1b8110e9cf837f3e19e0de63dd0b7afd133，parent db2c2e289419ecab7921667e210bd510ff3c447b。Astra本轮通过已授权GitHub连接器核实治理分支仍指向该commit、实际Git commit/tree及当前主线、V010计划和原MATLAB方法审计正文。源身份属于INDEPENDENTLY_VERIFIED_GITHUB_SOURCE。

Codex回报的本地原始字节、SHA-256、回读一致性与范围ACK属于CODEX_REPORTED_WITH_LOCAL_RECEIPTS。Astra没有访问D盘同步根或实际读取两份本地回执，不能声称在Windows独立复测。以下逐文件MATCH为Codex报告，不混同远端源身份核验。

## 2. Codex报告的16文档和收据

| 同步路径 | 字节 | Codex回读 |
|---|---:|---|
| CURRENT.md | 2076 | MATCH |
| TASK_CURRENT.md | 1450 | MATCH |
| SCIENTIFIC_DECISIONS.md | 4015 | MATCH |
| docs/CH5_OWNER_SCOPE_REALIGNMENT_20261015.md | 5995 | MATCH |
| docs/CH5_PUBLICATION_FIRST_STRATEGIC_ROADMAP_20261014.md | 5305 | MATCH |
| docs/CH5_VERSION_REGISTER_CURRENT.md | 2104 | MATCH |
| docs/DOC_INDEX_CURRENT.md | 3156 | MATCH |
| docs/CH5_OWNER_CONTINUOUS_VERSION_DIRECTIVE_20261015.md | 3310 | MATCH |
| docs/CH5_ASTRA_WORKFLOW_CURRENT.md | 15786 | MATCH |
| docs/knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md | 3273 | MATCH |
| versions/0.0.10/plan.md | 4784 | MATCH |
| versions/0.0.10/owner_scope_document_sync.md | 5340 | MATCH |
| docs/history/scope_realignment_20261015/README.md | 1190 | MATCH |
| docs/history/scope_realignment_20261015/CH5_VERSION_REGISTER_BEFORE.md | 85241 | MATCH |
| docs/history/scope_realignment_20261015/SCIENTIFIC_DECISIONS_BEFORE.md | 20151 | MATCH |
| docs/history/scope_realignment_20261015/TASK_CURRENT_BEFORE.md | 27273 | MATCH |

上表数量为16，按报告字节数相加为190449B。Codex报告共18个新增文件、212234B，差额21785B对应两份收据的合计体积，但Astra未独立检查它们的实际文件大小。

同步根（CODEX_REPORTED）：D:\ProjectTemp\ch5_owner_scope_sync_20261015_01。
SYNC_RECEIPT.json SHA256：8EE6AC370FDCA17F032727DEAA9528BC6E97BF0B07E9D2C928DB73FF47158448。
CODEX_SCOPE_ACK.md SHA256：FB26751133C2344352F3326360366539DBA29F4301168F838BA99F344E0B8621。

Codex报告4.8分钟、错误0/修复0、科研/模型/测试/真实数据/C8/B3/旧V009失败数组读取0、Git写0；总量在已批准8MiB/60分钟范围内。原HEAD、branch、8项dirty路径、index大小和时间观察前后一致，但未作dirty/index字节哈希、未扫描untracked/ignored；不认证完整文件字节未变或其它会话已停止。QMD、Basic Memory及其它记忆系统明确NOT_UPDATED。

## 3. 主线ACK与后续

接受Codex明确确认：恢复原MATLAB修错、HA条件稳态黑箱、有界多省顺序迭代、GovInv/Zt自适应校准及原递推冲击目标；V008/V009人工研究非活跃辅助、不自动作主线基线。其本会话旧V010 Newton取证未开始且已停用；其它会话未经本轮核查，不声称全局停止。

原同步任务owner_scope_document_sync.md已完成，不重复发同步微任务、不覆盖原同步快照。Astra在本次治理提交另外下达同V010的mainline_alignment_task.md：仅原方法的精确源码/基线/最小修错与兼容性集中方案。这个新任务才是下一步有限SOURCE_ONLY许可；同步PASS不构成任何HJB/KFE/模型/测试/真实数据权限。

V010仍DRAFT、未科学冻结；V011 NOT_STARTED。原C1/GovInv冲突未自动解决、原工作树未被推广新基线、旧数值与数据预算未恢复。V1.2角色及Owner连续推进规则不改。
