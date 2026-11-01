# Owner 决策：Chapter 5 Local-first Codex · 2026-11-01

## 决策身份与适用范围
AUTHORITY=OWNER_EXPLICIT_MESSAGE_2026-11-01
AUTHORIZATION_TEXT_SHA256=e5e8c25aae8ebcae1da718ad34746e5170c2129025ab2d9bfed6c8fcbcf244d6
GOVERNANCE_BASE=758954a31e1dff7e3d6c8eafef6af62ead11314c
GOVERNANCE_BASE_TREE=f05c149dd755a725d8e7341b9c36e7deaafce630
BASE_BRANCH=migration/astra-workflow-20261012
DELIVERY_BRANCH=governance/ch5-codex-local-first-20261101

本决定授权一次独立、仅治理文档的本地迁移与 GitHub 同步；同时确定后续长期职责。授权不覆盖科研合同、科学接受、保护门、历史 STOP、平台权限或已关闭预算。网页 GPT Project 顾问角色已确认、Project Sources 已替换，均为 OWNER_REPORTED；本轮没有直接核验网页后台。

## 忠实职责记录
Owner 为最终科研权威：决定研究路线、经济制度/机制、方程与 FOC/KKT/边界经济学、时序/payoff、参数校准、正式来源与数据口径、重大数值语义、科研运行预算、模型激活、科学接受、论文 Results、重要发布与高风险/不可逆事项。
Local Codex 是日常科研工程负责人：在既有合同、明确授权与保护边界内，自主规划分解、静态分析、源码维护、普通修复、获准检查/测试、工程质量审查与工程验收、版本/分支、进度和双端同步。普通工程不再等 GPT 派单或网页终验；不能靠自验创造科研权限。
Web GPT 是按需科研战略顾问：长期路线、经济数学机制、数值方法/架构第二意见、论文建议。Owner 可提供固定分支/commit 咨询。GPT 不日常派单、不掌任务账本、不作普通工程验收门禁；顾问建议不自动成为 Owner 决定。
工程验收、数值验证、科学合同符合性、独立科学评议、Owner 科学接受与正式 Results 必须分层。自身复核不能冒充外部独立审查。原合同中的特定科学独立门仍保留。

## 生效入口与旧文精确恢复索引
唯一默认执行入口为根 AGENTS.md；唯一当前工作流为 docs/CH5_ASTRA_WORKFLOW_CURRENT.md；唯一短状态为 docs/CH5_LOCAL_FIRST_STATUS_CURRENT.md。本轮不重写 CURRENT.md、TASK_CURRENT.md 或其历史状态。
冲突的 GPT 逐任务派单、候选默认网页终验、Codex 等待网页会话、离线 ZIP 默认交付流程，由本决定覆盖。旧候选、STOP/PENDING 与科研审查结论不被追认、删除或改写。

旧远端治理正文逐字节保留在以下固定 Git 对象，无需另上传长档案：
| 旧正文 | 固定提交路径 | Git Blob | bytes | SHA-256 |
|---|---|---|---:|---|
| AGENTS | 758954a31e1dff7e3d6c8eafef6af62ead11314c:AGENTS.md | 4a57dcddf4f7421f77f8f99d1cddf56f27ae6a8f | 18736 | 270ee579c7ea86342140ae4097d9234fca9226b5ffcc0818368bf3a70c277df5 |
| 旧工作流 | 758954a31e1dff7e3d6c8eafef6af62ead11314c:docs/CH5_ASTRA_WORKFLOW_CURRENT.md | ca6dbe9d254736a6fdbdf6a8f1cccbc8323f6c7f | 897 | e810105d6414131a8224318dd343eff9e4009722c6c9fa289106d2d6cef36faa |

活动本地工作树原件不同于上述远端版本，已另作仅本地治理回滚副本，原字节/hash 回读一致；这些副本不上传公开仓库：
| 本地原件 | bytes | SHA-256 |
|---|---:|---|
| 原 AGENTS | 132027 | d42041e26da7e795e3ae5c236e0029a8a356e14c8058ffa6f95383494f031b3e |
| 原工作流 | 15676 | b3cab64d249ff768f98403e8ccbc6f8aaf7d04b009f66255d41f26fb842ec2a7 |
精确私有位置及 before/after、原 index 身份、实际本地路径映射保存在迁移隔离目录的 LOCAL_ONLY_ROLLBACK 记录；公开文本不含敏感本地路径。局部治理回滚副本不是 G2 科研归档，不授权删除或搬迁科学资产。

## 科研与 G1 边界
Python 多省份 HANK/TEMP31 为唯一主动科研主线；MATLAB 仅历史参考，广泛 parity 不作 Python 前置，已纠正错误不得为 parity 恢复。本轮不改方程、工资税/财政语义、求解器、输入、网格、容差、参数或代码，不运行任何模型或真实/合成数值测试。
保护九月首次纠正复现的 Python 源码/证据和实际最新 TEMP31 工资税修正源。隔离 R4 模块不等于实际最新生产程序；完整 TEMP31 工作树/基线选择仍待 Owner 决定。
G1 是独立任务：ISSUED / COMPLETION_NOT_VERIFIED。本轮不验证其完成、不执行盘点、不改合同，不继承或扩大其 FILE_MUTATION_BUDGET=0、GIT_MUTATION_BUDGET=0、删除/移动预算0。聊天中已有交付叙述不自动成为完成认证。
CURRENT/TASK_CURRENT 末项 2026-10-28 WASM 安全 STOP 保留：13eff77c59f15011bbb563e283a6253d483f67b5；STOP_ACCEPTED__GITHUB_EVIDENCE_INTEGRITY_PASS__REPARSE_SAFETY_GATE__WASM_AND_BASELINE_BLOCKED。OWNER_BASELINE_REBIND=NOT_AUTHORIZED；未知 reparse 祖先不得穿越。
R12=STOP__R12_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED；R13=NOT_AUTHORIZED。所有原始/私有数据、旧保护基线、16项未解决义务及耗尽预算保留。
AUTO_NEXT=FALSE 仍禁未经授权的科学 successor、模型运行和 STOP 续跑；不再充当普通已授权工程必须等待 GPT 派单的理由。

## 本轮工程闭环与记录
已验证旧登记模型工作树、其 common-dir 和 main 工作树；TEMP31 是另一个 snapshot，Zotero 外层是另一仓库。只在独立稀疏治理工作树制作四文件提交；不将其采纳为模型源码基线。
活动模型工作树原 HEAD/分支/index 保留。仅同步这四份治理文件到安全、已核实的活动入口；既存源码 dirty、其他文档和未盘点 untracked 不纳入提交，也不重绑定保护状态。
最初一次稀疏物化使用了公共元数据位置；在无源码生成时取消本轮自有 Git 传输，改为工作树专属 sparse 路径。该工程纠正不涉及 Desktop、科研运行、旧任务重试或原模型 index。
本次仅作路径/祖先、文件身份、UTF-8/LF、链接、差异范围、保护状态、公开内容检查及 Git 回读。测试/模型/MATLAB=NOT_RUN；main 合并、G1、归档、清理、删除、科学资产重绑定=NOT_DONE。
单一治理提交的准确 SHA/remote HEAD 和逐文件 readback 由最终交付回执记录，避免在提交中写入自引用 SHA；远端失败即 PENDING_SYNC，不能称备份完成。只用既有合法身份，不绕过平台拒绝。

## 后续定点治理清单（未执行）
- docs/CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025.md：冲突日常派单角色已由本决定覆盖；科学/证据保护仍有效。
- docs/CH5_INDEPENDENT_REVIEW_RULES_20261025.md：保留特定科学独立门；普通工程不再默认网页终验。
- 旧离线 authority、任务模板、DOC_INDEX、长记忆和相关 Skills：仅按实际需要补导航，不批量重写，不从历史任务复活预算。
完成本治理迁移后 STOP。不自动进入 G1、研究运行、源码修改或仓库整理；此停点不恢复 GPT 日常派单制度。
