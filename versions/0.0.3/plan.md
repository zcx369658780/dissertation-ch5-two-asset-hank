# V0.0.3 版本计划草案：Corrected Household 联合来源身份及受保护读取决策准备

日期：2026-10-13（Asia/Shanghai）

**`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`**

Owner 已明确启动 V0.0.3 的版前规划。本文件是 Astra 的候选目标，**尚非冻结版本、实施许可、真实数据读取许可或科学运行许可**。先由 Codex 有界只读反馈 `V0.0.3_EXECUTION_PROPOSAL_DRAFT`，Astra 审议并在必要时请 Owner 作科学/权限取舍，随后才能冻结目标和单独授权。未经两个门禁不可实施。

## 1. 版本位置与真实证据上限

- V0.0.1：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`，固定代码提交 `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`；只证明合成下游 aggregate→frozen→batch→one-turn→firm。
- V0.0.2：`CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`，固定代码提交 `8f5457947492eef552f4261f8630c6c886af9fa5`，tree `af2a6a3d85f7525d480ad7da1916eaa25bf349b1`；合成 typed identity、digest、manifest 不具有外部信任锚，不能认证真实 producer。其[来源 crosswalk](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/source_crosswalk.md)是本版最小知识起点，禁止从头重复同样的模拟哈希构建。
- 科学合同：`SCIENTIFIC_DECISIONS.md`、`docs/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_ACCEPTANCE_20260920.md`、`docs/CH5_MP4C_UNIQUE_CLOSED_CLASS_SUPPORT_KFE_OWNER_ADOPTION_20260920.md` 与必要 payoff/timing 原冻结，按更新后的时效阅读。历史固定 checkpoint-11 V11/P11/u11/Q11、same-Q terminal mass 与 corrected aggregate 的接受，只能应用于其原特定 fixture/时期和原证据范围，**不能推导现在磁盘、所有31省或后续 turns 已认证**。
- 旧 MATLAB-faithful contaminated-row KFE 与已采用的 corrected unique-closed-class terminal KFE 不等同，不能将 faithful 的标量结果当作 corrected full policy/mass/AtTax 的证明。
- 先前 source-binding 旧末任务 `DELIVERY_INCOMPLETE/NOT_ACCEPTED/CLOSED`、C9 和 Objective A16 等不能借本版“准备”名称恢复运行/读取预算。旧脚本中有字段 seal 验证源码，并不等于本轮已执行或获得读取权。

## 2. 目标：从模拟输入转向可申请真实认证的源头合同

**G1 · corrected producer 真实路线的受界事实矩阵（SOURCE_ONLY）**

明确正确科学路线上 HJB 政策 `C/l`、同 Q/checkpoint 的 `p/g` 终态质量、收敛 `B AND D`、生产 Q/网格/参数/旧状态、`omega`、uniform `rah` 与 used `effective_r_a`、province/turn/checkpoint/return-stage 的来源组合；区分历史特定 accepted fixture、现在的现存代码调用点、尚未定位的源对象、`UNKNOWN/BLOCKED`。提供准确源码相对路径/符号/行或 Git blob/证据类别及生命周期，不把哈希或字段名视作跨文件的真实来源认证。判别是否存在多个并行 producer 实现；对已被科学合同接受的 corrected 算法不得再次选成旧 faithful 方法。

**G2 · 联合来源身份与读取前拒绝合同（DESIGN_ONLY）**

形成完整 joint-provenance trust chain 设计：固定 source code/科学方法 → 受采纳 producer/checkpoint/省份与进入旧状态 → HJB (B,D) + 同 Q terminal KFE 支持与质量 → F-order `(b,a,z)`/网格/`omega` → 政策与两类资产收益 `rah/effective_r_a` → aggregates/frozen/batch。这只是未来的准入合同，不在本版激活真实 loader。特别区分内容 hash、自述模拟 seal、历史人工接受、独立可信的签发/原证回读、真实权限与科学/经济资格。定义拒绝条件：不同 checkpoint/Q、错省份、错阶段、无法认证的 manifest、错资产收益时序、缺原件、错误 p/g 身份、受保护路径不可读、经济单位未定义等。每种未知写 `UNKNOWN` 或 `REQUIRES_OWNER_AUTHORIZATION`；不可发明 `REAL_AUTHENTICATED` 的静默捷径。

**G3 · Owner 最小必要真实资产读取决策包（REQUEST_ONLY）**

提出**一个尽可能小**、有科学依据且可核验的代表性 corrected 省份/固定 checkpoint 源集合，说明选择理由、与历史 checkpoint-11 接受的关系及局限；逐个列准确已知 locator/根路径依据、文件类别/字段、当前已知 hash/manifest、读取目的、谁建立可信 anchor、精确候选读取次数/字节上限、内容保密和脱敏方式、是否需要新独立高风险评审。定位不到则标 `NOT_LOCATED/UNKNOWN`，不能猜测本地目录或请求打开全量31省资产。形成精简 `OWNER_DECISION_REQUIRED`（科学 producer 身份、真正的数据访问范围和 Objective A16 / window 条件），单独列劳动单位/人口分母/年份/价格/日历后续决策。**本包只是供 Owner 以后选择的请求草案，绝不自动解封文件、旧拒绝或旧耗尽预算。**

**G4 · 下一门分层验证及可实施路线**

拟定可验收阶段：`SOURCE_CODE_REVIEW → OWNER_SCIENCE_AND_PROTECTION_CHOICE → EXACT_PROTECTED_READ_AUTHORIZATION → AUTHENTICATED_JOINT_ASSET_READBACK → CONDITIONALLY_BOUND_SOURCE_LOADER → REAL_RUNTIME/SCIENCE_GATE`。各门写出最小输入、通过/拒绝与证据层级、目标保护、不允许的自动晋级，解释 V0.0.1/V0.0.2 只是消费结构参考。除非 Codex 有实际代码证据说明非新增一个独立静态检查就无法完成本版研究，否则优先 `DOCUMENT_ONLY`，不继续造模拟哈希/虚构 seal 或进行无必要重复合成测试。

## 3. 版前建议的验收要求（未冻结）

A. 真实 corrected producer 与历史 accepted 科学/具体 checkpoint 和导出 API 的**精确来源/缺口矩阵**，每个关键字段可溯 Git 固定源码；不假称读过受保护资产。
B. 一个可独立审议的联合身份 schema / pre-read fail-closed 合同，不改现有数学法则、KKT/selector、KFE 方法、报酬时序、资产/人口劳动口径。
C. 一个 Owner 能做明确授权或拒绝的最小资产许可决策包，包含准确已知 locator 与 unknown、风险和拟议边界；**不执行该包中的资产读取**。
D. 下一门具体科学/安全验证顺序、阻塞项和测度；区分 `INDEPENDENTLY_VERIFIED_GITHUB_CODE`、`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`、`HISTORICAL_ACCEPTED`、`SOURCE_ONLY`、`UNKNOWN`。版本内成果的最高资格依最终冻结方案可为 `DOCUMENTARY_SOURCE_CONTRACT`，而非 `REAL_AUTHENTICATED`、`SCIENCE` 或 `RESULTS`。
E. 如选择纯 DOCUMENT_ONLY，原则上不需要科学/模型/tests 进程预算，真实运行与读取次数保持0；若 Codex 提出有限 static-engineering，须先说明有别于 V0.0.2 的具体科学/审计价值、准确修改路径、证据与 V1.2 工程/存储分账，经 Astra 冻结才可实施。

## 4. 恒定禁区、存量保护与版本基线

- `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`model_activation=False`、`Results FALSE`；旧关闭账本及科学/数据读取预算不重开。人口/人均决策保持、户均封存，不 `N=P/3`。
- 不读取 protected JSON/NPZ/MAT/CSV、旧31省真实 consumer，不运行 HJB/KFE、K1B/C8/C9/C10、GE/IRF/福利/Results 或生产源 loader；不改变 D1/D2/D3、Q/KFE scientific solver、raw-ra0/S/lagged timing、C1、现有 labor route/量纲。历史已接受的科学 checkpoint 不是本版新一次 scientific runtime。
- 不修改既有 V0.0.1/V0.0.2 冻结合同/候选代码/验收复盘、不切 main、不重写 AGENTS/CURRENT/本地 route/dirty 数据，不 reset/rebase/stash/clean/强推/合并，不修改 Zotero/EliteSync/DeepLearning-HANK/全球环境。
- `NEXT_BASELINE_ADOPTION=UNDECIDED`：推荐 Codex 评估是否以 V0.0.2 fixed code commit `8f5457947492eef552f4261f8630c6c886af9fa5` 为下一版代码或文档基线，若文档-only 也说明源源码为何应固定此 commit；**不得在版前自行采纳、移动当前本地原 HEAD、合并 main**。
- Codex 最近报告的唯一模型 worktree `D:\ProjectTemp\c5k1bturn56`、原本地 HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e` 和 dirty/untracked 只是其上次回执，本轮网页不核本地磁盘。Code tree、ChatGPT 项目 cwd、Git common-dir、GitHub 文档分支和候选树不能混淆。

## 5. Codex 版前唯一任务

**本轮仅只读提交方案，不实施。** Codex 有界读取：本草案、V1.2 工作流与 CURRENT/版本登记前缀、V0.0.2 固定 crosswalk、必要现存 GitHub 源码及对应原科学采纳文档、绝对模型树中允许的静态代码/Git 元数据。不得反复全仓扫描、调用本地 QMD/Basic Memory 重建、查看或载入受保护产物。

交付 `V0.0.3_EXECUTION_PROPOSAL_DRAFT`，应包含：
1. 真实线程/host/projectId/cwd、唯一模型 top-level/origin、代码与文档固定 SHA、index/staged/dirty、untracked/ignored 保全（只读），V0.0.2 candidate/本地/head/main 区别，`NEXT_BASELINE_ADOPTION` 具体建议；
2. producer 路线与字段/同 Q/checkpoint/省份/进入状态/资产收益阶段的源码事实和未知项，以及为何选用建议 route 而不擅自推翻已采纳 corrected 科学法则；
3. `DOCUMENT_ONLY` 或确有必要 `STATIC_ENGINEERING` 的工作方案、最少新文件/职责、未来信任锚与联合身份校验/安全生命周期；
4. 一份可操作但尚未执行的最小受保护读取申请提案：精确已知资产 locator/字段/hash/目的/字节/次数/隐私、Owner 决定项、拒绝/停点；
5. V1.2 的只读与未来执行分层预算、文本 UTF-8/LF/命令 fail-fast/final-tree 证据方式、低成本集中交付方案、科学/数据 0 调用；
6. 真实证据的分类和下一门不会自动晋级、生产/Results/C9 保护保留。

提交完整草稿后立即 `WAIT_ASTRA_PLAN_REVIEW / STOP`。Astra 再决定是否冻结版本并授予 Codex 实施自主权。本轮**无代码修改、无测试、无真实数据访问、无候选创建/push**。

## 6. 本轮状态

V0.0.1 和 V0.0.2 各自已受界 ACCEPT/CLOSED；V0.0.3 `DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`；V0.0.4 NOT_STARTED。真实来源及经济量纲仍 UNKNOWN，受保护资产权限未解除。
