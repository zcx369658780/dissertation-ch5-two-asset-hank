# V0.0.2 正式冻结版本计划：家户来源契约与合成输入准入

**版本：** `0.0.2`　**Owner启动：** 2026-10-13　**状态：** `FROZEN__AWAIT_SEPARATE_ASTRA_AUTHORIZATION`

**不可追改原则：** 这是 V0.0.2 唯一现行冻结合同。原 `DRAFT` 只保留在此前 Git commit `5cfe41fd0a66877565accca3c8e7dc9a71fa35ee` 的历史文件，不能作为实施许可或与本文件混用。**本冻结提交即计划 freeze SHA**，由后续版本登记/授权文档记录其完整 commit，不将自身 SHA 写回本文件。实施还必须有独立 `ASTRA_APPROVED_EXECUTION` 授权。验收按本版原冻结目标，不为获取 PASS 更改合同。

## 一、立版依据与科学目的

Owner 已要求在 V0.0.1 `CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS` 及 CH5_WORKFLOW_V1.1 本地同步完成后继续研究。Codex 经有界只读检查交付 `V0.0.2_EXECUTION_PROPOSAL_DRAFT`，Astra 已审议其字段来源、经济限制、五文件方案和分层资源建议。

本版要从 V0.0.1 合成下游 aggregate→frozen→batch 工程闭环向上迈一步，明确定义家户政策/质量/收益数据能否被准入 corrected aggregate 的**类型、来源声明与内在一致性**。**这不是**真实 solver、真实来源身份、产物 seal、31 省生产 callback、科学运行、GE、Results 或生产启用资格认证。

## 二、固定代码基线与未合并事实

- **`NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA`**；V0.0.2 **仅新候选构造**的代码基线为 V0.0.1 accepted candidate commit `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`，tree `39e7a91ca473ba770bd65518607c3f78f4b9fe24`，源自上一代码截点 `a1db8c114dec0ab69d69a5576e153a7f868cba0e`。
- 唯一有效项目仓库 `zcx369658780/dissertation-ch5-two-asset-hank`。Codex 已报告模型工作树 `D:\ProjectTemp\c5k1bturn56`、当前原分支 `codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922`，该本地 HEAD 仍是原截点；这些仅为其只读实测，开工前重新核验。
- 此采纳**不允许**在原工作树执行 merge/rebase/reset/checkout/clean/stash，也不证明 `main` 已包含 V0.0.1。文档分支 `migration/astra-workflow-20261012` 与代码基线分离。候选须从上述固定代码树**独立精确路径**构造。
- 2026-10-13 Codex 草案报告 staged0、tracked dirty8、untracked5405、ignored4553；真实本地数量可能随时间变化。既存 `AGENTS/CURRENT/TASK_CURRENT/REVIEW_GATE`、两份路线图及两个 dirty 源码 `government_assets.py`、`annual_observed_labor_diagnostic/middle_stage.py` 均不得修改/覆盖/清理。项目聊天 cwd、工作树与 Git common-dir 不等同，不能动用 Zotero / EliteSync / DeepLearning-HANK 的代码或远端。跨项目误发所涉其他仓库的 FETCH_HEAD、远端跟踪引用问题**不属于本版**，不以本许可修复或审查它们。

## 三、冻结工作目标

**G1：有证据级别的逐字段来源 crosswalk。** 静态、有界读取家户真实/旧 MATLAB-faithful / corrected producer 的当前源码：`consumption`、`labor`、`b/a/z grid`、`effective_r_a`、`source_r_a`、`probability_mass`、`density`、`omega`、`Ct/Lt/At/Bt/AtTax`、`converged/statistic`、下游 batch/callback 等，逐字段列源码路径/符号、对象/形状/F-order/轴序、省份/期次/checkpoint/联合来源条件、seal/manifest 缺口、经济与数据年份/价格状态、证据资格。源文件“存在”或字段“名称相似”不能替代真实来源认证。区别 `SOURCE_ONLY`、`HISTORICAL_ACCEPTED`、`SYNTHETIC_ENGINEERING`、`LOCAL_ONLY`、`UNKNOWN/BLOCKED`。

**G2：独立 opt-in typed metadata + 默认拒绝边界。** 复用 V0.0.1 `SyntheticHouseholdRecord` 和已有 corrected aggregate validation，新增一个不接文件/网络/生产环境的来源元数据与**模拟一致性**验证模块。建议符号 `HouseholdSourceMetadata`、`assess_source_contract`、`admit_synthetic_household_record`；可在不改变职责的前提下细化内部辅助函数。必须联合声明并核对同 synthetic province、source_id、requested iteration/stage、simulated checkpoint/grid、字段引用与声明轴序 `(b,a,z)`、F-order、明确的 `source_r_a` 对 `effective_r_a` 角色区分及 `p≈omega*g`。simulated field digest/manifest 仅证明被测内存 payload 与元数据匹配；不得以 hash、字段字符串、自报 seal 或 `REAL_AUTHENTICATED=True` 认证真实对象。**只有明确 SYNTHETIC/NOT_REAL_SOURCE 可以被本版转换为现有合成记录并进入聚合/batch。** 其他 `SOURCE_ONLY`、`HISTORICAL_ACCEPTED`、`UNKNOWN`、`REAL` 等至多用于来源表或报告中的分类，计算准入一律 fail closed，不应存在隐含切换分支。原始输入应复制/冻结，不悄悄补字段、自动重排、密度再归一化或更改 returns。

**G3：同次合成准入→原聚合→batch 的受界测试。** 虚构2省、原合成 `20×20×2` F-order 网格，非对称 policy、少数非零但非均匀且单位总量的 `p`、`g=p/omega`，非科学统计标签。集成测试必须**真正调用**新准入对象、现有 corrected aggregate/frozen、V0.0.1 的 `build_synthetic_household_batch`，并由独立标量 oracle 验证 `Ct`、z 加权 `Lt`、`At/Bt/AtTax`，同时检验资格未提升与快照不别名。可依逻辑需要选择 2–3 省，规模不等于真实31省。重要拒绝场景：缺 simulated seal/字段、simulated digest 不一致、错误 provenance、cross-province/source/stage/checkpoint/grid 混配、重复/缺省份、虚假 REAL 标签/布尔认证、轴序/F-order 索引不符、错 `omega`、p/g 不一致、负/非单位/非有限质量、`source_r_a` 与 `effective_r_a` 角色混淆。合成转置与同被改写的 manifest 不能保证由 hash 检出，必须如实用非对称 oracle 与记录的声明边界表述。**本版不运行 one-turn/firm/K1B runner、real HJB/KFE**，下游只作源码 crosswalk；不更改 V0.0.1 的双劳动路径经济语义。

**G4：精确的下阶段风险/来源阻塞清单。** 区分 source-loader 所需真实 typed 输入、checkpoint/province/period/asset identity 合同、来源认证和数据保护缺口、所需 Owner 科学决定与精确未来数据读取请求建议（提案而非授权）；生成小型脱敏 candidate summary，区分 GitHub 独立可读、Codex 本地回执和 UNKNOWN。

## 四、允许文件范围（新增五项，不能修改既有源码）

只允许在代码候选中**新增**以下五个公开路径，若任何路径已存在/冲突，停止并报告：
1. `src/ch5_two_asset_hank/multi_province/household_source_contract.py` — typed 元数据、模拟一致性校验/拒绝/准入，不做 loader、solver 或默认接线；
2. `tests/test_v002_household_source_contract.py` — 真正单次准入至原 batch 的合成集成测试、独立 oracle、拒绝和模块隔离；
3. `versions/0.0.2/source_crosswalk.md` — 源码身份、字段表及未知/封闭资格；
4. `versions/0.0.2/execution.md` — 本版真实执行、失败修复、保护/资源/剩余问题；
5. `versions/0.0.2/acceptance_summary.json` — 小型脱敏测试/资源/哈希/未认证状态记录；不得自行宣告 Astra ACCEPT。

可在**本版专属无冲突的 LOCAL_ONLY 证据根**生成操作性 Git index、candidate_view、模拟 fixture、私有原始 stdout/stderr/JUnit、只读原代码路径/哈希/保护账和导出临时工具，所有新建临时材料遵守下面各类空间预算，禁止推送原始私有日志/受保护数据。无旧文件可被强制覆盖。Astra 负责后续独立的 `versions/0.0.2/acceptance.md` 与 `retrospective.md`，本版 Codex 不编辑它们、也不修改本 `plan.md`。

禁止修改已有 `__init__`、`corrected_household_adapter.py`、`household_adapter.py`、`synthetic_household_bridge.py`、`one_turn.py`、`firm.py`、HJB/KFE、原科学合同/validators/真实生产 controller/default 环境。**如发现实现必须触碰禁止项，停止并报告，不通过扩编文件范围或改冻结标准绕过。**

## 五、工程预算与分层存储（独立于全部旧 CLOSED/科学预算）

- 单版实施至候选集中交付总墙钟 `<= 3h`（含失败/修复）；普通 focused pytest 子进程 **累计最多12次**，每次 `<=120s`（无论通过与否均计），单进程目标 RSS `<=1GiB`，无法守住时停并报告。不要把这组数字作为所有以后版本的永久模板。
- 真实 HJB/KFE、K1B、C8/C9/C10、31省实际数据/consumer、GE、IRF/Results、真实 source-loader、受保护 JSON/NPZ/CSV/MAT、部署、修改本机/全局环境的调用或权限 **均为0**，不因本版工程预算解锁任何旧账。
- **本版新增存储总额** `<=168.25MiB`，下列类别预算按新建对象分别核算，**不重复计数、不得自行豁免**：① Git 操作性 index/new objects/临时构造材料 `<=128MiB`（必须明确隔离、不覆盖原 index）；② 从候选树导出的 `candidate_view`、所需代码闭包及合成 fixture `<=32MiB`；③本版原始 stdout/stderr/JUnit、进程/资源/失败/保护回执 `<=8MiB`；④公开发布的 crosswalk/execution/summary 合计 `<=256KiB`。既有 Git objects、既有受保护数据和历史 EVIDENCE 不是新建，但绝不自动清理。导出/创建临时 index 前预估大小。额外临时对象必须归入上述一类，不能以未知分类绕过总额。
- 运行须固定已核解释器和依赖版本、环境局部禁第三方 pytest 插件自动加载并验证 `__file__` 全部源于**精确候选 tree** 的隔离导出，不从 original dirty 工作区混入。Codex 可选择一致的隔离启动方法：注意 `python -I` 忽略 `PYTHONPATH`；仅在候选视图可正确导入且实际 readback 通过时使用，或采用受限 child `PYTHONPATH` + 模块来源断言，不更改全局环境。普通工程调试在原预算内自主完成，保留每次失败和重新验证身份，不逐阶段索批。
- 超过明确硬预算、文件冲突/需要改科学方程/真实数据/权限/禁止路径、候选隔离不可证或持续阻塞时 `STOP + 保存现场/回报`。不得借 Owner 曾经许可 V0.0.1 的轻微 Git index 修正自动放行新的越界修订；必须有与本版对象和范围对应的 Owner 单独授权。

## 六、冻结验收标准与交付身份

A. **G1 SOURCE crosswalk** 对每个关键输入有准确已读源码/固定代码身份，明确 route 对照及真实来源 UNKNOWN。来源标签/哈希≠真实性。
B. **G2 模拟准入边界** 禁止任何非合成输入进入聚合；字段/province/stage/checkpoint/grid/returns 一致性检查与主要错误拒绝有实际合成测试，禁止 synthetic 变 REAL、伪造签名晋级。
C. **G3 有限工程 test** 用准确 candidate tree 导出的受限模块运行测试，含真实 corrected aggregate/frozen/V0.0.1 batch 调用，独立 oracle/输入快照和标签资格验证；不把绕过源码的 stub 称为实际计算通过。
D. **G4 证据/资源/保护**：公开五文件范围、版本号+代码 baseline/最终候选 commit/tree、父节点和变更路径、完整测试次数与结果、准确或脱敏命令、依赖/模块来源、UTC+单调时间/进程退出/峰值（仅能测到的字段）、失败历史/修复、原本地回执哈希/界限；保护原 HEAD/index/dirty/untracked/ignored 并报告只读验证限制。所有报告明确区分 `INDEPENDENTLY_VERIFIED_GITHUB_CODE`、`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`、`UNKNOWN`。
E. **科学防冒认**：本版最高能授予 `SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING` 资格；真实 solver/源身份证书/经济单位/价格和日历/实际生产 callback/31省、稳态/GE/Results/生产发布均不通过。原 `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE` 不解除，人口/人均保持且不 `N=P/3`。
F. **候选发表**：从 `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4` 单父提交精确构造候选 `codex/ch5-v0.0.2-household-source-contract`；先核远端无同名分支/避免非快进，使用独立临时 Git index 仅入树五个新增允许路径（本地工作树原 branch/HEAD/index 保留），在最终 candidate tree 上 focused 验证后一次 normal non-force push 和远端 SHA/tree readback；不 merge `main` 或文档 branch，不上传本地 EVIDENCE。Codex 集中交付后停 `WAIT_ASTRA_FINAL_ACCEPTANCE`，由 Astra 按原计划独立验收和版本复盘。
G. **异常/部分接受**：受保护来源不能认证是本版本正常的明确 UNKNOWN，不算真实源成功；但本版列明的核心结构/拒绝/测试若未通过，不能据“BLOCKED”自动宣称 G2/G3 PASS。Codex 完成可核部分后报告 `PARTIAL/BLOCKED`，Astra 独立决定终态，不能事后放宽本版标准。

## 七、版本界面

本冻结只决定 `0.0.2` 的拟实施科学/工程边界及未来候选身份，不授权 V0.0.3 或任何后续版本。V0.0.1 继续 `CLOSED/ACCEPT_WITH_OBSERVATIONS`。旧 MATLAB-faithful scalar aggregates、corrected policy/mass、合成 wrapper 属不同证据对象；不重新运行旧 binding task、真实 consumer 或旧自动化。

**从 DRAFT 转 FROZEN 的提交身份以发布回执登记；正式实施必须有独立授权链接。**
