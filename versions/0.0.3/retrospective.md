# V0.0.3 Astra 版本复盘（DOCUMENT_ONLY）

日期：2026-10-13（Asia/Shanghai）；最终 `CLOSED__ACCEPT__DOCUMENTARY_SOURCE_CONTRACT_ONLY__WITH_OBSERVATIONS`。

证据：
- [冻结计划](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/768a3181fcbc9d367ccce08b1d69458353a48229/versions/0.0.3/plan.md)，原 blob `1bf80332586a4e3beeeb355d90b5ec049c7e503c`，保持不变。
- [独立实施授权](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/2ec13ea41e7bb86eacb19f4601d243a1298bd4bd/versions/0.0.3/authorization.md)。
- [Codex 文档候选](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/cf74384f151427f0b7071ac0461cede6ad6cdf11)；[来源矩阵](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/producer_source_contract.md)；[Owner 决策请求](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/owner_read_request.md)；[执行记录](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/execution.md)。
- [Astra 独立验收](acceptance.md)。

## 1. 版本目标与真实闭合内容

本版选 `DOCUMENT_ONLY` 而非继续构建合成 SHA 或设计 loader，避免把工程外壳冒充真实资产认证。独立核 GitHub 接受 G1 corrected producer 路线/14公开源引用、G2 joint provenance schema/拒绝条件、G3 run004 北京三文件 `REQUEST_ONLY`/Owner 决策与零当前读取、G4 后续风险/资格门和执行记录。V0.0.1/V0.0.2 仍保留其有限合成工程证据范围；本版没有任何新的科学数值、政策结果或外部经济量纲认证。

关键研究发现：当前 `policy_identity` 主要为政策 marker，`checkpoint_identity` 只含部分 V/policy/Q；真正联合身份必须在可信历史 producer code/version、run/province/stage/进入状态、Q/KFE/support/p/g、完整 C/l 数值、grid/omega/returns、可靠独立权威锚及读取权限之间建立跨对象证据。北京历史 run004 三文件只是**下一门提出精确请求的可讨论起点**，不证明当前盘上文件存在或可读。

## 2. V1.2 成本/流程指标

| 维度 | 本轮 Codex 交付/独立核验 |
|---|---|
| Codex 版前执行方案 | 一次完整 `V0.0.3_EXECUTION_PROPOSAL_DRAFT`，Astra 集中审议 |
| 正式文档候选 | 单父固定 V0.0.2 commit，新增严格三文件；GitHub 独立确认 commit/tree/路径/branch |
| 文档最终校验 | Codex 报 `exit0`、耗时1.859秒；GitHub Astra 独立确认三文档正文及14/14源码/历史blob |
| 墙钟计费 | Codex 报 `1303.69/5400s`，含保守前置300秒；本地原钟不可由网页复算 |
| 存储 | Codex 报总 `16,143,662B`；Git操作14,981,305B、候选文档27,765B、本地回执1,106,827B、公开27,765B；各在分层硬上限内 |
| 测试/科学/受保护真实数据 | 报告0，本版无科学进程许可，网页未复核完整本机进程史 |
| 用户额外审批/人工微管理 | 本版方案冻结后无另一次流程豁免；最终人工 Owner 数据读取决策尚未作出 |

## 3. 必须留存的两次失败与处理

**第一项是实质性的执行流程偏差**：原回执命令遗漏 `import sys`，退出1，两个文档在失败后仍发生依赖续写。与 V1.2 的 fail-fast 规则不一致；Codex 后续保留错误/部分文档 bytes、修正命令后核定14个公开原证并校验准确候选树。最终接受的理由是目标合同、文件范围和独立来源核验合格、没有发现科学或受保护数据越界，**不是**将违规继续当作符合流程。未来实施前可将命令与文档生成之间的依赖关系落实到自动化退出码阻断，避免只在 Prompt 中提出原则。

第二项是普通引用验证器语义错误：表格标题已声明 `docs/` 目录，而 checker 初版没有按此解析六个历史 basename；初次检查 exit1，依赖的 Git tree/commit/push 当时未开始。修正解析器后14/14 blob/path 通过，保留原失败，不是偷偷更改来源身份标准。

**无需为这两项偏差重开 V0.0.3**：在当前受限 DOCUMENT_ONLY 验收标准下，它们不使来源合同或候选 Git 身份失效。未来版本如存在依赖失败仍继续的现象，须严格判断是否触发冻结硬门；更高风险的 protected/science 任务不应因此默认有限接受或视为先例。

## 4. 对后续研发的建议（不自动派单）

研究价值最大的下一阶段是让 Owner **明确决定是否选择这个历史 run004 北京元数据对象**，并在实际授权前独立查明可信历史 anchor、Objective A16/window 防护、路径解析与可观测的文件大小/次数上限。原则上先申请极少数可核的元数据，不立即解锁完整 policy/Q/p/g 数组或31省/科学求解。不要将本版三文件文档合同自动变成数据读取计划或新 loader 的生产 API。

治理层面 V1.2 已包含依赖失败即停和 UTF-8/LF 规则；本次显示**执行脚本未有效强制**。可以在后续合适版本或独立普通治理任务中检查一份小型 fail-fast 命令执行策略，但不得因此创建复杂框架、强制多审查或追改 V0.0.3 冻结计划。

对于网页无法读取的本地原始 receipts，继续采用 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS` 与 `INDEPENDENTLY_VERIFIED_GITHUB_CODE` 分账，保留第一次失败及其修复过程。DOCUMENT_ONLY 不需要人为添加 pytest 来展示 PASS。

## 5. 版本封存

V0.0.3 `CLOSED__ACCEPT__DOCUMENTARY_SOURCE_CONTRACT_ONLY__WITH_OBSERVATIONS`；文档候选维持独立分支，不合并 main、不开保护资产访问许可。V0.0.4 `NOT_STARTED`，未选定候选基线、没有独立授权。C9/ledger/A16/window/Results FALSE 和旧 CLOSED 预算/人口口径继续有效；劳动人口分母/价格/日历与实际 source identity 仍 UNKNOWN。
