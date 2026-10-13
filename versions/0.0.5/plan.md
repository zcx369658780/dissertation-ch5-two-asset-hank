# V0.0.5 版前草案：可信独立实验根获取与首次创建前隔离证明

日期：2026-10-13（Asia/Shanghai）

**`DRAFT__WAIT_CODEX_TRUSTED_ROOT_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`**

Owner 已明确启动 V0.0.5，研究目标仅为解决 V0.0.4 **首次创建前缺乏可信独立 fixture 根**而导致的 G0 安全阻塞。本文件是**版前目标草案，不是冻结合同、隔离环境创建许可、Windows ACL/卷探测许可、fixture 攻击许可、受保护数据读取或科学运行许可**。依据 `CH5_WORKFLOW_V1.2`，先由 Codex 在有界 SOURCE_ONLY / 已允许 Git 元数据内提交 `V0.0.5_TRUSTED_ROOT_EXECUTION_PROPOSAL_DRAFT`，再由 Astra 审议并将真正需要 Owner 批准的独立环境/根获取权限与单项用途集中呈交。未发布正式 freeze SHA 与单独授权前均不得实施。

## 1. 历史阻塞与不改变的 Owner 决策

- V0.0.1–V0.0.3 已各自有限 `CLOSED/ACCEPT_WITH_OBSERVATIONS`，不补写结果或更换 science contract。
- V0.0.4 正式终态：`CLOSED__BLOCKED__G0_FIXTURE_ISOLATION_UNPROVEN__NO_EXPERIMENT__WITH_OBSERVATIONS`，见 [最终验收](../0.0.4/acceptance.md) 与 [复盘](../0.0.4/retrospective.md)。冻结 `1b825948e69fcdfd30c1826be023d6963d2e9b25`、独立 fixture 授权 `7955fbbd1a5bc770124d3819a15f70638a4972a2` 均已随版本关闭；Windows `10.0.26300.0`、Python3.11.9/ctypes、NTFS 和 API exports 存在仅来自 Codex 本地报告，**没有实际 12 场景、没有两个 oracle 验证、没有 V0.0.4 代码候选**。
- 原 G0 的具体阻塞：已知拟议独立文件名不存在或与模型路径字符串不同，**不能证明**首次文件创建确实处于可信根下，也不能证明被攻击/替换的全部祖先和共享 namespace 均可弃用。不得把此结论误写成 `NtCreateFile` 方案不可行或旧 A16 取得 PASS。
- Owner D1（历史 run004 **初始北京三元数据仅为未来拟核验对象**）、D2（**完整 A16/window 威胁范围不得缩小**）继续有效。D3-real/D4-real 没有授权；本版本暂不新批任何 fixture-creation、实验 D3/D4 或外部环境配置。
- 原 Objective A16/C9 输出 mutation 的 root claim、recursive mkdir、JSON/NPZ creation、unlink 仍 `UNRESOLVED/FAIL_CLOSED`；即使未来只读 fixture 的部分属性得证，也**不**自动关闭这四类输出操作。

## 2. 本版真正的研究问题

**G1 / TRUSTED_BOOTSTRAP_ROOT：怎样在首次创建之前取得可审议的独立根身份？**

Codex 必须提出至少两条**物理上可区分**的取得/建立路线，区分证据来源和事后验证：
- 路线 A：已存在且 Owner 可独立指认/证明的**专用可弃用卷或预创建隔离空间**，由已获授权的 OS 原生身份/句柄证明 volume identity、对象身份、权限与非共享祖先边界；不得假定现有 D: 盘/默认 TEMP 就满足条件。
- 路线 B：由 Owner **未来单独批准**的外部可信环境供应（例如独立可弃用卷、已合法提供的 VM/隔离盘/已有沙箱），其创建权、位置、原资产隔离、身份签发与 attestation 验证路线必须明确；**本版不允许安装虚拟化软件、创建 VHD/VM、分区/格式化/挂载卷、创建系统账号、提权或修改 ACL**。
- 可比较路线 C：在已可信且**不允许攻击公共祖先**的根句柄下，按受限单组件 API 以明确排他/句柄策略首次创建子树，建立“创建时锚—新子树—后续固定可弃用祖先”的可信链；先严审其本身是否仍存在**循环前提**，不以 root 字符串或 create 后检查冒充先前已证明的根。若该路线不能解决初始根的问题，标 `INSUFFICIENT/DEPENDENT_ON_ROUTE_A`。

**G2 / ANCESTOR_ISOLATION_AND_ATTACK_BOUNDARY：** 画出首次创建时的 volume/root handle → 各级祖先 → 独立 fixture subtree → 叶人工文件的授权及可变路径层级，明确每层 ownership、reparse/rename/DELETE_CHILD、hardlink/mapping、ACL/token、同用户与获授权非管理员进程的影响；哪些是不可攻击的公共祖先，哪些是明确可弃用的内部祖先。区分 **对象句柄稳定**、**路径及祖先在窗口内不变**、**攻击只能打在许可 fixture 上** 三种独立断言。说明可信根锚需要哪项独立证据、谁产生与核实、哪些平台能力未证实。完整 D2 威胁不能靠缩小攻击者来造 PASS。

**G3 / MINIMUM_OWNER_ENVIRONMENT_DECISION：** 将每个候选方案转化为一个 Owner 可明确批准或拒绝的**最小权限包**，列准确建议根类别、谁预先提供、是否需要非默认 OS 配置、哪些环境身份/volume/ACL/reparse/handle 信息需未来单独批准读、查询对象、只读查询次数、是否涉及物理创建/格式化/挂载/变更、可变祖先界限、工具/principal、生命周期/LOCAL_ONLY/脱敏，以及权限不够的替代终态。对未定位实物标 `UNKNOWN / OWNER_SUPPLIED_ANCHOR_REQUIRED`，**不猜测现存可用根**。该包属于 **REQUEST_ONLY**，不自动许可探测/创建或真实受保护资产访问。

**G4 / ONE_GATE_EXECUTABLE_STOP_CONTRACT：** 提出一个可以独立验收的后续**可信根 bootstrap gate**，只解决 V0.0.4 G0，绝不重试其12项保护场景；定义从可信 Owner/OS 提供根到本版专属子树首次建立的无循环证据顺序、状态机、先验检查与失败即停止、最小权限/次数/存储及不扩权规则。清楚区分三种结果：
1. `BOOTSTRAP_ROOT_PROVEN_FOR_NAMED_SCOPE` 仅适用于明确实验范围/环境、**不是**完整 A16 PASS；
2. `OWNER_ROOT_CHOICE_REQUIRED` 现有信息不足而需要 Owner 提供/允许独立根；
3. `ROOT_TRUST_OR_ANCESTOR_ISOLATION_BLOCKED` 不能满足严格前置，停止而**不创建 fixture**。

## 3. 版前可验收交付和科学价值

Codex 的 **`V0.0.5_TRUSTED_ROOT_EXECUTION_PROPOSAL_DRAFT`** 应当产生可核的：
A. 实际可引用的 Microsoft 官方/API 或既有本项目固定合同所支持的 bootstrap 候选及其明确未验证前提（不将一般平台常识当成本机实测）。
B. “独立根首次创建—可信身份—祖先许可—后续攻击范围”的**证明义务矩阵**，指出 V0.0.4 究竟缺哪个 first trusted anchor，不能退回泛泛建议“换个目录”。
C. 排序后的 **一个首选方案 + 备选 + 完整阻塞退路**，写出其证据如何在**不接触受保护资产**的情况下取得，具体是否需 Owner 提供独立卷/环境。
D. 最少 Owner 权限选择，区分 OS环境能力查询、特定根身份/ACL/token 探测、创建可弃用命名空间、运行人为攻击 fixture、真实历史北京三文件读取——**这五者从不自动互相授权**。
E. 下一门有界实施方案：候选 Git 父基线、最少新文件和实际涉及的外部资源、临时存储/回执、单独 source/read/FS/attack 预算、UTC及 fail-fast 阻断；缺可行根/需提权等硬停，不应再单纯复制 V0.0.4 的12场景任务。
F. 完整的 `SOURCE_ONLY / HISTORICAL_ACCEPTED / OS_DOCUMENTED / CODEX_REPORTED_WITH_LOCAL_RECEIPTS / UNKNOWN / PROTECTION_BLOCKED` 分账。最高证据取决于未来新冻结与独立审验，不自授 `A16 PASS`。

这不是重复 V0.0.3 的真实数据联合来源合同，不是修复 HJB/KFE。应交付**方案之间的可行性淘汰理由和具体下一门**，如独立根不存在则明确 `OWNER_SUPPLIED_ANCHOR_REQUIRED`，不能以冗余文档宣称取得信任锚。

## 4. 冻结前绝对禁止与基线状态

- **本版目前仅版前 SOURCE_ONLY/已允许的非破坏性 Git 元数据调查，实际 Windows 文件系统、候选根、卷、真实资产祖先、ACL/SID/token/reparse 的新探测及读取均为0授权。** 不创建目录/fixture/VHD/虚拟机/卷，不编写/运行任何攻击、实验脚本、测试或代码候选；不调用 HJB/KFE、C8/C9/C10、31省 consumer、GE/Results、旧全量 verifier，也不恢复旧预算。不得对旧 run004 及模型树任何受保护路径 `stat/exists/open/read/hash/ACL/probe`。
- 保护原 worktree `D:\ProjectTemp\c5k1bturn56`、原 HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e`、staged0、dirty8、已知 existing untracked5947/ignored4553、index SHA-256 `28058A7E2D9AB773C5813205C75999E6C221533AEAE0B9BB094B9A83451BF7CC` 仅为**上次 Codex 报告快照**，实施端应自读 Git 状态且不能对全体旧未跟踪资产作正文扫描。聊天 cwd 不是模型 worktree；不要混入 Zotero/EliteSync/DeepLearning-HANK 或修改全局配置。
- `NEXT_BASELINE_ADOPTION=UNDECIDED`。由于 V0.0.4 `NO_EXPERIMENT` 且**没有代码候选**，建议 Codex 考察 V0.0.3 fixed accepted commit `cf74384f151427f0b7071ac0461cede6ad6cdf11` / tree `372c693ca3dccea716ae8caef382f513e5a2316e` 作为未来代码/文档基线；本草案不自动采纳、不 merge main、不改变旧本地 HEAD/index/dirty。GitHub 动态 docs 分支 `migration/astra-workflow-20261012` 独立。
- V1.2 fail-fast 已有规则；上一版 PowerShell 因 Git tree 表达式未引用而继续只读后继，不再仅写空泛“须 fail-fast”。Codex 需在后续建议中明确**真正阻断下游**的简短 supervisor/return-code 状态机，但版前不编码或运行。
- `A16 UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、`model_activation=False`、`Results FALSE`、旧科学/数据 CLOSED 预算与人口/人均方向、不 `N=P/3` 不变。D1 北京对象与 D2 完整威胁模型保持 Owner 已采纳，D3-real/D4-real 继续未授权，V0.0.6 NOT_STARTED。

## 5. Codex 版前单一任务与停止点

Codex 应实际读取本草案、V1.2 workflow、CURRENT/版本登记现行前缀、V0.0.4 G0 [验收](../0.0.4/acceptance.md)/[复盘](../0.0.4/retrospective.md)、既有 A16 保护原科学决策及必要官方 API 文档，只读核 Git 身份/旧 protected 列表类别，不访问真实资产内容、目录 metadata 或 candidate fixture 位置。

应一次性提交 `V0.0.5_TRUSTED_ROOT_EXECUTION_PROPOSAL_DRAFT`，至少回答：
- 目前真正缺失的 first trusted anchor 是什么，如何不依赖在目标祖先创建后再检验；
- 至少两条独立路线、首选与备选的最小可信来源/Windows API 与权限义务、实际阻塞；
- 可审议的**Owner 精确独立环境选择**，不将选择独立卷误当格式化/装载/读取许可；
- 未来可能的极小 bootstrap-only 代码/文档路径和测试环境、精确资源分账/预算建议、非递归路径与 fail-fast 门，是否已有现成工具能少写代码；
- 若 Windows 各种能力不足，如何在不触碰受保护资产的情况下恰当终止为 `ROOT_TRUST_OR_ANCESTOR_ISOLATION_BLOCKED`；
- `NEXT_BASELINE_ADOPTION` 推荐、原 checkout/index/dirty/Git 保护、证据等级与科学不升级。

完成方案即 **`WAIT_ASTRA_V005_PLAN_REVIEW / STOP`**。未经 Astra 先审议/必要 Owner 特定环境决定、正式冻结计划和独立授权，**不得**实作、创建、探测真实/实验目录或签发后续 V0.0.6。
