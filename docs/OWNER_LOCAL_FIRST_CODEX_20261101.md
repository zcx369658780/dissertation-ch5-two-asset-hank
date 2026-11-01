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

## 2026-11-01 第二阶段：GitHub 治理导航整合（Owner 再授权）
AUTHORITY=OWNER_CONFIRMED_EXECUTION_OF_CH5_GITHUB_GOVERNANCE_PROMPT
AUTHORIZATION_TEXT_SHA256=9f72eb07c7969e53901bb3a1b20430112ca9f42fef41534c8214f3e553675a59
PHASE2_GOVERNANCE_BASE=38d60e9c55f809cd699a56646250abc8610295cc
PHASE2_MAIN_REFERENCE=b7e595ceb1cd7ffb5adfbf54e2de4e65f01090a5
PHASE2_BRANCH=governance/ch5-codex-local-first-20261101
PHASE2_WRITE_SCOPE=EXACT_TEN_GOVERNANCE_NAVIGATION_FILES_IN_ISOLATED_WORKTREE
上节“后续定点治理清单（未执行）”保留为第1阶段原始记录；本节记录后续独立授权的履行，不追溯改写第1阶段。

现场复核：本地治理 HEAD、parent、tree、干净状态和第1阶段回执逐文件一致；原模型 HEAD/index 与既存 tracked 状态保持。治理线相对 migration 基线 ahead 1 / behind 0；相对 main diverged、ahead 835 / behind 4，属于历史祖先关系，不是本阶段新增835提交。只在本治理分支安全 fast-forward 增量，不 PR/merge main、不 rebase、不强推。
原模型工作树本阶段不写。此前已应用的 Local-first 根规则仍在；第2阶段导航增量只存在于独立治理工作树及其 GitHub 副本，不宣称已铺到原模型工作树的旧副本。TEMP31 完整工作树/基线仍待 Owner 决定。
tracked、staged 和治理范围 untracked/ignored 已定点核对；为保持 WASM/保护门，不递归盘点原模型受保护 untracked/ignored。全量覆盖 UNKNOWN，未作保护基线重绑定。

### 本阶段精确分类和动作
| 入口 | 分类 | 本轮动作 |
|---|---|---|
| AGENTS.md、唯一工作流、唯一短状态、本 Owner 决策 | CURRENT_GOVERNANCE | 连接分类导航、记录阶段身份和适用范围；不另造角色权威 |
| CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025.md | SUPERSEDED_WORKFLOW ＋ SCIENTIFIC_CONSTRAINT | 仅标识旧日常派单/工程网页终验被覆盖；原字节正文及来源、预算、隐私、STOP要求保留 |
| CH5_INDEPENDENT_REVIEW_RULES_20261025.md | SCIENTIFIC_CONSTRAINT；普通工程网页门禁为 SUPERSEDED_WORKFLOW | 不整体作废，不降低特定科学独立审查门；原字节正文保留 |
| CH5_OFFLINE_WORKFLOW_AUTHORITY_CURRENT_20261023.md | SUPERSEDED_WORKFLOW / HISTORICAL_EVIDENCE | 加正确当前入口；保留历史正文 |
| CH5_REVIEW_TASK_TEMPLATE_CURRENT.md | SUPERSEDED_WORKFLOW ＋ SCIENTIFIC_CONSTRAINT | 标为历史模板，不能机械发单、激活科学或恢复额度；正文不改 |
| DOC_INDEX_CURRENT.md | CURRENT_GOVERNANCE 导航；下方 HISTORICAL_EVIDENCE | 新增唯一当前导航和五类分流，旧索引正文不改 |
| CH5_PROJECT_MEMORY_CURRENT.md | HISTORICAL_EVIDENCE | 只加按需读取导航前缀，原研究记忆正文逐字节保留 |
| CURRENT.md、TASK_CURRENT.md、历史任务/审查/STOP/证据 | HISTORICAL_EVIDENCE ＋ SCIENTIFIC_CONSTRAINT | 不写、不删、不移动，固定身份保持 |
| 当前宿主 instructions/skills 的实际注入与选择 | UNKNOWN（运行时适用性） | 只核根规则、宿主提供入口与既用 Git 工作流技能入口；不扫描工具缓存或修改全局规则 |

本阶段所有新增导航目标均定点核对。旧档案内部的全部链接、宿主完整运行时注入顺序和保护状态全量盘点不在本轮覆盖，不宣称已验证；有具体需要时再在相应授权内处理。
公开内容检查覆盖全部新增/修改的治理范围与新增文本；原长记忆、旧索引和旧约束正文保留，不上传 LOCAL_ONLY 回执或私有原件，不新增敏感本地路径。旧正文和新前缀分别核对字节身份，Git 历史可恢复。
本阶段自主验收仅限治理导航工程；不是外部独立科学审查，不接受旧科研候选。实际新 commit、remote HEAD、文件列表、字节/Blob/哈希回读由 Git 及本地阶段交付回执固定，失败为 PENDING_SYNC，不写自引用 SHA。

G1=ISSUED / COMPLETION_NOT_VERIFIED；本轮不执行、不补做、不关闭、不修改 G1。九月首次复现和实际 TEMP31 修正源保护、WASM STOP、OWNER_BASELINE_REBIND=NOT_AUTHORIZED、R12 STOP、R13 NOT_AUTHORIZED、16项义务、已耗预算及全部科研硬门保持。
模型/测试/MATLAB=NOT_RUN；main 合并、rebase、PR、归档/复制/移动/删除/清理科研资产、改变 snapshot/worktree/branch 历史、Desktop/CUA/node_repl/mirror/安全配置修改=NOT_DONE。完成此治理整合后 STOP，不自动进入下一阶段。

## 2026-11-01 项目源交接进度核对与本地对齐
AUTHORITY=OWNER_REQUEST_TO_ALIGN_G1B_HANDOFF_PROGRESS_AND_EXPLAIN_ROADMAP_POSITION
ALIGNMENT_PARENT=351b456c8866e36e5dbc92bcd8c338e0d8d0bff8
ALIGNMENT_SCOPE=GOVERNANCE_AND_PROGRESS_RECORDS_ONLY__NO_ASSET_PUBLICATION_OR_SCIENCE
Owner 本次确认后续日常执行由 Local Codex 负责。本轮先核交接、对齐本地进度并报告路线位置/下一目标；不是直接执行原件恢复、科研运行或科学采纳。Owner 最终科学权威不变；交接中旧 GPT 派单、逐任务终验职责按 Local-first 决定理解，不再充当普通工程门禁。

### 交接与当前记录的差异
- 交接中的 migration/astra-workflow-20261012@758954a31e1dff7e3d6c8eafef6af62ead11314c 是历史治理锚点。当前工程治理线为 governance/ch5-codex-local-first-20261101，本次对齐以351b456c8866e36e5dbc92bcd8c338e0d8d0bff8为父。不得据旧交接向 main 合并、重放835条历史或覆盖当前分支。
- “本地模型仓库是 shallow bare”仅适用于已知 TEMP31 对象库，不能概括本地全部模型仓库；旧登记代码工作树、common-dir、TEMP31 snapshot 和治理工作树是不同对象。
- G1 限额内盘点报告已在本聊天交付，Owner 本次确认其完成。登记为 REPORT_COMPLETED_BOUNDED__OWNER_CONFIRMED；资产身份/完整原件/恢复资格尚未闭合。交接所称182行仅为 OWNER_REPORTED，未重新计行。原 G1 合同 ISSUED 文本、零写预算及既有终态不改写，不补做 G1，也不把报告完成升级为资产归档接受或科学接受。
- 九月9日父源码提交725cbcc86756eb92bd50f477875ca30d53e88c5e与结果提交90ee5b29f3be070d9f8f28c9614e1b59fe798462必须共同保留；后者还新增运行器/finalize/测试。完整原始 checkout 的确定仍未闭合。
- 交接被截断的九月10日身份可由现场 Git 元数据补全：登记工作树 HEAD=a7bd3b1a705ff42e2933b22a8c6563ec47248ce4，tree=1490e63dda5da128306e4a1dbc9f071f94170837，分支 codex/ch5-python-runtime-input-binding-repair-20260910。本轮只核祖先安全和 Git 身份，不认证其实际源码完整性、dirty 状态或科学资格，也不以此替代九月9日里程碑。
- TEMP31 六文件字节身份、R4/Bootstrap19/HJB调用修补/价格R3/机制R4/源码R5的分离、R2/R3缓存重复但保留来源证明等，沿用已交付 G1 报告，未重哈希或重读科学原件。任务命名中的 R2/R3/R4 有复用，后续须用完整 TASK_ID＋日期＋commit，不能只写轮次。

### 路线图位置：工程已有积累，当前处于可信资产/来源恢复前置门
定点读取的旧本地路线图保留原件及哈希，未复制到公开治理线、未改写冻结路线。旧路线图的迁移顶注停留在2026-10-12；历史家户基础、K1B turn5/6等仅适用于其原合同，不自动认证当前 TEMP31。
| 依赖层 | 当前定位 | 证据强度/限制 |
|---|---|---|
| Local-first 日常治理与导航 | 已完成两阶段治理提交 | 本地回执和远端固定提交直接核对 |
| 旧家户/K1B 与 TEMP31 隔离工程 | 有既有代码、有限轨迹和工资税修补积累 | 旧路线图/既有报告；本轮未运行或重新科学验收 |
| G1 归档前盘点 | 限额内报告已交付并获 Owner 确认 | 资产身份、完整性和可恢复性未全部闭合 |
| G1B 缺件恢复准备 | 下一工程目标；精确缺件/公开范围未冻结 | 候选分支本次 fresh 查询不存在；未创建、未上传 |
| 正式 TEMP31 工作树/来源与生产接线 | 尚未通过 | formal source freeze false；生产输入/consumer闭合、严格驻定仍阻塞 |
| 完整31省稳态/GE、动态IRF/福利与论文 Results | 未放行 | 各自独立科学门；Results false |

这是一张对既有状态的依赖映射，不是重新冻结研究路线或撤销旧限定接受。当前不能给出科学完成百分比。既有保护“16”按旧路线图的4×4分类格身份保留，不在本轮重新定性或解除。

### 下一任务目标：CH5_TEMP31_G1B_MISSING_ASSET_RECOVERY
目标是把“哪份原件、GitHub是否确实缺失、能否公开、如何完整恢复”形成可追溯闭合，而非批量上传全部 LOCAL_ONLY 文件或重跑模型。
1. 用精确 locator 和既有 Git 身份区分九月9日/10日、TEMP31单税模块、Bootstrap19、调用修补、后续诊断；先形成逐件身份与缺口表，不把六文件一致宣称成整棵模型一致。
2. 逐件判断远端已有对象/仅缺导航/确实缺件；已存在资产优先记录固定引用，避免重复上传。缓存重复不等于可删，科学原件仍按保护范围保留。
3. 建立精确公开白名单和排除项：文件路径、用途、bytes、Git Blob、SHA-256、来源/依赖、原件或脱敏副本、公开依据。新私密数据、R12 LOCAL_ONLY、敏感源/矩阵、凭据和保护门未开的资产禁止访问或发布；不明确的公开资格交 Owner 对具体原件作决定。
4. 只有范围与公开资格明确后，才按新的受界恢复授权使用独立候选分支；建议名称 codex/ch5-temp31-g1b-missing-asset-recovery-20261031，开工重新核基线和 ref。本轮没有创建该分支。G1B 不沿用 G1 已耗读取/哈希额度或零写合同。
5. 恢复后核 commit/parent/tree/路径/Blob/大小/哈希及必要依赖完整性，区分工程恢复验收、独立科学评议和 Owner 接受。恢复不等于正式来源采用、生产接线、驻定、归档接受或科学 Results。

精确白名单与科学/隐私边界是后续原件恢复的必要条件，不是等待 Web GPT 派单。当前消息要求的进度对齐完成后先向 Owner 报告，不自动进入 G1B 上传或科研运行。
本次只更新当前治理记录和安全的本地入口；原模型 HEAD/index、未编辑文档、旧路线图和既存源码 dirty 状态保留。本地四个当前入口同步新治理版本，DOC_INDEX 只同步当前导航前缀并保留本地历史正文；不复制科研原件或将治理工作树采纳为模型树。
G1 合同、WASM STOP、OWNER_BASELINE_REBIND=NOT_AUTHORIZED、R12 STOP、R13 NOT_AUTHORIZED、所有旧预算和科学硬门保持。模型/测试/MATLAB/G1重跑/G1B原件上传=NOT_RUN。

## 2026-11-01 G1B 公开范围核对：工程发现，非新的科学决策
AUTHORITY=OWNER_REQUEST_TO_CONTINUE_PROJECT_UNDER_EXISTING_LOCAL_FIRST_BOUNDARIES
SCOPE_CHECK_PARENT=700383670711dc218451ba6e001709f81db556dd
SCOPE=FIXED_REF_PUBLIC_MANIFEST_RECONCILIATION_AND_EXISTING_PRIVACY_POLICY_METADATA_ONLY

| 资产子集 | 固定提交 | 本轮核对与限制 |
|---|---|---|
| 九月9日 repository_files | 90ee5b29f3be070d9f8f28c9614e1b59fe798462 | 11/11存在；11份重算Git Blob匹配远端身份；10份原始字节大小/SHA-256匹配清单，1份CSV经CRLF表示转换匹配 |
| 九月10日 files | a7bd3b1a705ff42e2933b22a8c6563ec47248ce4 | 7/7存在；7份重算Git Blob匹配远端身份；6份原始字节大小/SHA-256匹配清单，1份CSV经CRLF表示转换匹配 |
| TEMP31价格域R2公开载荷 | ffb156712e56bd2fe24924ba40295858ad67e18f | 101/101路径、Git Blob匹配；100份可返回大小匹配，1份工具未返回大小；不宣称新逐件SHA-256验证 |
| TEMP31分布切换R3公开载荷 | e194e44be4287cc447fdc3d83adb0dbd01bcb9d0 | 103/103路径、Git Blob匹配；102份可返回大小匹配，1份工具未返回大小；不宣称新逐件SHA-256验证 |

九月9日清单为 reports/mp4c_2018_corrected_single_turn_20260909/manifest.json，Blob=ad83d69578943843acface6b1da953afcd95f327；其中含一份目录外的报告，已单独回读。九月10日清单为 reports/mp4c_python_runtime_input_binding_repair_20260910/manifest.json，Blob=c1cedfdb1496865906e9a633d20eb2aca1480faf。目录中的清单和readback自身不计入18份载荷。

两份CSV均保留现有原件；只在内存中计算换行转换哈希，不写回、不解析数值：
- 九月9日 per_province_observables.csv：Git Blob=2be3ba3706b8f37b5737931e5711d1b490a3ed80；Git字节15486，SHA-256=e9ca1d7705735a24cee7d25e353a1118512392a3e1a8b652c6e98a2196f3853d；CRLF表示15518字节，SHA-256=12cd4c359ddc6a655dc81c1dff5b2a5c7f77c000480f7a60bf94131cc49851b5，与历史清单一致。
- 九月10日 runtime_reconciliation_31province.csv：Git Blob=57589714dfffc1a37fa312f675086f71d15fd353；Git字节14277，SHA-256=63ec896e7544d7e8398d946fac836e48af4f14dc51097e5995e6681651757be9；CRLF表示14309字节，SHA-256=445b7f6b44cd1a24713496fe8edcb4408d2d5d0806cbf23604efde05e52c607c，与历史清单一致。

R2完整任务为 CH5_TEMP31_MATLAB800_THREE_PRICE_LOCAL_DOMAIN_MAP_R2_20261030，manifest Blob=d9e5b56d6af26b94b4f3a85bc4a3a19edea37f19；R3为 CH5_TEMP31_MATLAB800_PRICE_NEIGHBORHOOD_DISTRIBUTION_SWITCH_R3_20261030，manifest Blob=bc657aae19917303e32434375dcdd93878cde1bd。各自既有privacy_report明确：完整数组/密度/CSR、原始stdout/stderr、源码缓存及操作脚本保留LOCAL_ONLY；公开日志是已认证脱敏派生件。原mandatory privacy assert和无ignore/skip要求不降低。本轮只读这些既有清单/隐私说明，不打开数组、缓存源码或R12材料。

结论仅为上述子集未识别出公开缺件，不是整个仓库或完整原始checkout的恢复认证。九月外部manifest列出的137份外部资产及62份NPZ只是清单元数据，不因未列入仓库载荷就获得公开资格；本轮不读取内容、不上传。六份TEMP31源码身份不升级为完整模型快照一致。

建议恢复分支本轮fresh查询仍不存在，未创建，无原件上传。继续使用已有固定引用，避免重复复制。完整原件/checkout可恢复性与私有备份完整性仍未闭环；若需受限备份，应由Owner对具体原件范围、目标存储和访问权限作决定，不能用一般工程自主权覆盖LOCAL_ONLY。无需补交已有路径或等待GPT派单。

本轮工程验收仅覆盖公开子集身份核对和治理记录；不是数值验证、独立科学评议、归档接受或正式Results。模型/测试/MATLAB=NOT_RUN；无科学源码变更、保护重绑定、清理、main合并或G1预算复活。既有科学STOP保持；后续正式基线选择和科研运行不自动启动。

## 2026-11-01 G1B 完整工作树与依赖核对：工程证据，非来源采纳决定
AUTHORITY=OWNER_HANDOFF_TO_CONTINUE_READONLY_GIT_METADATA_EXACT_INVENTORY_AND_NECESSARY_STATIC_DEPENDENCY_CHECKS
CHECK_PARENT=9299d90cee4423c965249659ebc2d30075088667
SOURCE_ADOPTION=OWNER_DECISION_PENDING
ENGINEERING_SCOPE=BOUNDED_FIXED_OBJECT_METADATA_AND_STATIC_ANALYSIS_ONLY

治理分支/parent/tree、登记代码HEAD/tree/index和远端main启动刷新均与交接一致；治理工作树干净，代码工作树432条默认porcelain记录及既存改动保留。六条相关历史分支fresh ls-remote均指向已登记的九月9/10、Bootstrap19、HJB ladder、机制R4和来源恢复R5提交。未重开G1，不重复核对既已交付的R2/R3和九月载荷清单。

### 固定来源与正式基线候选
| 候选/用途 | 身份与核对 | 尚未证明 |
|---|---|---|
| 九月9日纠正复现 | source 725cbcc86756eb92bd50f477875ca30d53e88c5e / tree5032974d251926d802267c7cc5bcb0a64cdad6d4；result 90ee5b29f3be070d9f8f28c9614e1b59fe798462 / tree7cf2741803bde15c4eaee3cbcf46d53fabcfc32c。限定src/exports/validators/tests/pyproject清单分别208/212路径、207/211不同Blob，既存模型对象库均有对应blob类型/大小元数据。result另加3份validator与1份test，不能只保留父源码而丢结果提交。 | 全部原始工作文件、外部输入、原始证据和恢复可执行性；本轮未认证原始物理checkout |
| 九月10日输入绑定里程碑 | a7bd3b1a705ff42e2933b22a8c6563ec47248ce4 / tree1490e63dda5da128306e4a1dbc9f071f94170837；限定清单252路径、251不同Blob均有本地元数据。对应登记工作树现场HEAD/tree/branch匹配、porcelain为空。 | clean Git状态不是私有输入或完整原件认证，不取代九月9日 |
| TEMP31来源候选锚点 | 建议56447829ce0e6c3c85552c53c351b26a2452a4bd，parent a51c2e7ff6548340a1ee86857b0ee55792fa69b4，root tree7b7cb29dd5b37be92561e7f1bc688c0d29789732；src subtree8ac1458f0586f1fad58e7bcb85d8acf1a3ef0600，exports subtreef0614665143257e024cc7857afc3bbaf08e730c0。 | NOT_ADOPTED；完整工作树、生产接线、科学资格未认证 |

上述src/exports/pyproject在ffdb7fcd41019bed7ce4652ee01c753bff6fcec8（调用修补seal）、56447829、5e1933e4c166fa40b95c82bed377538d843c7576（机制R4）、cd6ef027dc0c7242e4f62ae648ca83641fc6f1c6（来源恢复R5）中身份相同；后两者没有新的src/exports/pyproject变化。Bootstrap19@10ee7973713c547faa581388aa97fbfd898809de到调用修补仅改temp31_netwage_hjb.py；R4单税模块e99c622b...不是完整TEMP31生产源。这里是固定候选间的身份结论，不是全仓库“最新版本”认证或历史科学终审。

### 缺口分类与依赖范围
| 分类 | 本轮结论 | 后续边界 |
|---|---|---|
| 已有资产、主要缺物化/导航 | 固定56447829清单：src74、exports1、validators308、tests181、pyproject1，共565路径；每个Blob的类型/大小元数据可在两个既存对象库合集中找到，无新fetch或源码物化。snapshot仅存在13/74源码路径、0/1 export、8/308 validator、4/181 test及0/1 pyproject；本轮未重哈希这些工作文件。 | 对象分散存在不等于完整对象图、可恢复checkout或完整原件认证；不上传重复文件，不建空恢复分支 |
| 确失且明确可公开的原件 | 该固定源码/工程清单未发现本地对象不可用项；原R2/R3及九月载荷结论沿用。 | 不是全仓库或外部原件零缺失声明 |
| LOCAL_ONLY或资格不明 | R2/R3数组/密度/CSR/原始日志/源码缓存/操作脚本及九月外部137资产、62 NPZ保持原边界；内容未读、未拷贝、未上传。R12材料未读。 | 尚未产生必须选择私有备份位置的具体恢复动作；不要求Owner重复提供已有路径 |
| 身份已定位、依赖/工作树未认证 | 以六个TEMP31模块及export为种子，35个静态import/package-initializer节点可映射到固定路径和本地原始Blob；23个未物化。35份对象重算Blob/bytes/SHA-256后做AST分析；另对有界生产入口/辅助入口静态核对。 | AST无未映射目标只适用于这35节点；不覆盖全部生产validator动态加载、文件输入、运行环境或实际调用。普通package初始化亦未执行 |

pyproject Blob5c778f7ccbbabfaf1046d4696cf843dc0adbb34c声明Python>=3.11、NumPy>=2.0、SciPy>=1.14、setuptools>=68；它是版本下限，不是锁定且已认证的运行环境。本轮不安装、不导入第三方或模型模块。目标snapshot无可用图谱索引，未自动索引；采用固定Git路径与有界AST。三份公开固定文件（pyproject、temp31_netwage_hjb.py、exports/matlab_faithful_two_asset_ha.py）经GitHub connector新回读并重算Blob/bytes/SHA-256，与本地固定对象一致；未扩大为565文件远端逐件字节认证。

### 明确生产入口阻塞及Owner门
固定生产入口mp4c_python_annual_production.py（Blob7473e04418744d745000afb21d84588273cc5bca）依赖mp4b_python_empirical.py（Blobb1710ae3c5d8d7baf96e85c932d777fa5f3b908c）。后者第19行ORACLE_SHA为B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3；其bootstrap在导入前要求.git、src和export存在并检查此pin。

同一固定提交的export Blob=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf，GitHub与本地均为31143字节、SHA-256=a7539eb6ba076176b81f832c1800d38d8d170dad8f3619d3b0f3893c5a163fff。仅内存转换为CRLF后31859字节、SHA-256=f6007c1166c951b4a0c98b0fbf551921a2664d2e3943e7d77f847634261524f8，仍不等于pin。故该入口存在静态身份合同冲突，不把它归因于简单换行，也不声称本轮运行观察到异常。未改pin、未替换export、未恢复旧错误、未运行loader。私有primary输入、canonical、runtime cache的可用性和采纳资格仍未认证，未访问其内容。

供Owner审阅的具体决定是：是否将上述56447829固定源树采纳为后续完整TEMP31工作树的来源锚点，以及export/loader身份合同冲突应依据哪份获准科学来源处理。在作出对应决定前，不采纳、不创建或hydrate模型工作树、不改科学源码或pin、不启动生产接线或科研运行。该候选本身不具备可运行/科学接受结论。

ENGINEERING_VERDICT=PASS_BOUNDED_SOURCE_LOCATION_AND_GAP_REPORT_ONLY
FULL_CHECKOUT_AND_DEPENDENCY_CERTIFICATION=NOT_ESTABLISHED
SCIENTIFIC_ACCEPTANCE=NOT_GRANTED
MODEL_IMPORTS_RUNS_TESTS_MATLAB=NOT_RUN
R12=STOP__R12_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED；R13=NOT_AUTHORIZED；OWNER_BASELINE_REBIND=NOT_AUTHORIZED；FORMAL_SOURCE_FREEZE=FALSE；Results/model_activation/REAL_GE=FALSE。原WASM STOP和全部旧预算保持。完整路径清单、静态依赖边、私有路径映射、回滚原件与核对记录仅保存在本地隔离证据中；公开同步只包含这两份治理文档。
