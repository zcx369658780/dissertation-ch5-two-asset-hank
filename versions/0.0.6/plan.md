# V0.0.6 版前目标草案：C8真实来源—31省输入—经济量纲联合绑定

日期：2026-10-14（Asia/Shanghai）

**状态：OWNER_STARTED__V006_DRAFT__WAIT_CODEX_CONSOLIDATED_SOURCE_ONLY_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED**

**版本定位：** Owner本轮明确启动V0.0.6，作为已采纳“论文成果优先”战略的首个科研长版本，目标属于M1数据/接口科学合同，不是启动C9/GE、经济结果制作或恢复已耗尽的科学/数据预算。当前仅是**Astra版前目标草案**；须由 Codex 基于真实本地源、未提交差异及科学原件交付一份完整只读实施建议，Astra审议及必要Owner取舍后**另行冻结计划并独立授权实现**。DRAFT文本及本次GitHub文档提交不构成科学调用、源码修改或真实资产读取授权。

## 1. 当前版本基线和需保留的科学事实

原 V0.0.5 已在GitHub治理提交 8de1fcd3aef63a541bea72075fbf61c793b6fe4f 以“有限工程备份和对齐接受、可信敌对实验根G0未证、清理延期”关闭。Codex报告B3时点保全90,766普通文件及外部Git common-dir字节、SHA全部匹配；外链不恢复/全树同一时点未证；无需再次备份、创建物理隔离盘或在V0.0.6重复旧Windows实验。

唯一模型实际本地工作树（Codex上版报告，非Astra独立Windows验证）：D:\ProjectTemp\c5k1bturn56，原 branch codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922，HEAD a1db8c114dec0ab69d69a5576e153a7f868cba0e；为linked worktree，其 Git common-dir在 D:\ResearchCode\dissertation-ch5-two-asset-hank\.git。模型HEAD、远端main、GitHub治理发布branch和接受候选并非一事。上版最后报告staged0、dirty tracked8（六治理文档及两源码）、untracked5948、ignored4553，均为**历史本地报告而非当前新扫描**，不得因为开启新版本清理/覆盖或自动引入。

**已采纳而不可重新辩论的经济基础：**
- 两资产(b,a)、31省、已接受的HJB/KFE与K1B资本网络和lagged raw-ra0 payoff及既定参数/时序、C1残差律保留；
- 固定原C8 household outputs、完成C7后entering-C8的省份状态及冻结资本份额S。C8 option1仅设计/有条件准备原年度labor和composite wage系数来源的target2018/observed2017条件对照，原人口N、参数和distance/migration transform不变；**不以条件对照冒充新工资条件下家户重新求解的自洽均衡**，不重算HJB/KFE、shares、K2或同轮return反馈；
- 原已采纳的 SOURCE_ONLY 31省“0-based model简称轴 ↔ 1-based 年度全名轴”显式绑定，以及9项synthetic联合轴测试历史接受，**不等于原C8 JSON/NPZ/receipts已经在本地live重新绑定**；
- Owner撤销户均，保留人口/人均；不 N=P/3。个体l、household Lt、迁移矩阵、firm Lt_supply及效率劳动经济单位须分开；历史NU_100_PERSONS、MU_10WAN_YUAN标签存在不等于新鲜的输入经济单位认证；
- observed2017/target2018为历史回溯对照、非2018实时信息集。价格方法学 current_price_methodologically_attributed 已采纳，direct_price_verified=False、price_verified=False、release UNKNOWN、baseyear None仍然有效，不能无来源自动改为真；
- C8、K1B九分量R2、C9/数据资格、Objective A及fullouter/GE/Results区分。旧C8实时science/actual-data/consumer budgets为0、C9 PAUSED/CALL_LEDGER_UNRESOLVED、A16 16 UNRESOLVED/FAIL_CLOSED、final-check-to-mutation window UNACCEPTED、model_activation=False、Results FALSE；旧CLOSED额度不会因立版或更名回补。

## 2. 本版科研目标：一次性完成可审议、可实现的输入链闭环设计

以“原C8固定中间状态 → 真实年度输入准备 → 同一master进入两个消费者 → 保持原经济单位/份额/时序 → 明确运行许可缺口”为一条链，**不将每个字段、目录或转换写成微版本**。

A. **原C8完整输入源身份。** 从已接受固定源合同和当前已发布源码，建立 original household receipt/result → original C8 mass_form batch字段Ct、At、AtTax、household Lt（同时识别完整batch的Bt）、entering-C8 state/N、S原字段及配套参数/distance在生产caller处的逐跳精确绑定表。每跳明确source artifact/commit/field、producer与consumer调用阶段、类型/axis/形状/布局/单位/日历/已证证据层；无法证明则UNKNOWN，绝不以历史C7聚合、旧Turn4构造器或名字相同替代 original C8 runtime identity。
B. **31省轴与年度输入资格。** 复用已接受的简称/全称/0↔1映射，分别判明年度观测轴、原C8批次轴、历史receipt各省身份、S目的行×来源列的经济角色及归档声明。保留 float64/C-order年度master 与 little-endian float64/F-order的S的差别。必要年份/价格basis、source timestamp、哈希/provenance、万元/万人/人均与模型内部NU/MU转换形成明确合同；不得重新问Owner人均/户均选择，不从元数据标签直接宣布真实经济单位通过。
C. **双消费者及生产接口一致性。** 静态核 annual master（不可变同源）到migration labor与composite wage两个边界的准确函数入口、对象身份/生命周期、origin tau 与 destination tau、migration-wedge与share-distance角色、frozen S allocation/C1/31 firms以及最小import/副作用/输出边界。沿用已接受劳动与K1/C1公式，不替换真实household、S或原模型参数。不把synthetic spy PASS当live consumer PASS。
D. **最小工程成果与验收。** Codex在版前指出现有已接受SOURCE_ONLY实现里哪些能直接复用，哪些是目前真实缺口，提出一份完整的冻结后实现/聚焦测试/可能的精确科学D3/D4权限与资源方案。预计正式实施版可在安全与科学合同允许的SOURCE_ONLY/纯合成层内完善绑定和拒绝契约；**任何真实JSON/NPZ/科学数据读取、原C8消费者运行、动态import/模型调用、新输出root以及完整A16保护使用均须单独的Owner批准与可审证据**。本版不为了PASS偷偷降低原安全目标。

**预期可验收成果分层**：SOURCE_CONTRACT_ACCEPTED（固定来源/类型/单位/时点合同）、SOURCE_ONLY_IMPLEMENTATION_ACCEPTED（确实完成并受检的代码）、SYNTHETIC_ENGINEERING_ACCEPTED（仅经过授权的新测试），REAL_INPUT_BOUND_AND_CONSUMER_AUTHORIZED（需要新的实际来源/保护准入）。任何一层未达到则独立记UNKNOWN/BLOCKED，不能直接跳到RESULTS/GE。

## 3. 版前给Codex的单份 SOURCE_ONLY 长任务范围（当前唯一新行动）

Codex先读取此GitHub固定 DRAFT 和 CURRENT / 版本登记 / V1.2 / SCIENTIFIC_DECISIONS 原件，及以下**已存在的限定参考合同**，不能把标题/索引当实际已核内容：
- docs/CH5_DOT_FIXED_C8_INPUT_SAFETY_CONTRACT_20261002.md 和 docs/CH5_DOT_FIXED_C8_INPUT_BINDING_SOURCE_ONLY_RESULT_20261002.md；
- EVIDENCE/ch5_frozen_c8_conditional_design_20261001/owner_design_adoption.md、owner_conditional_execution_scope.md、consolidated_conditional_design.md、remaining_binding_requests.md、independent_consolidation_review.md；
- docs/knowledge/published/CH5_LABOR_UNIT_HISTORY_AND_EVIDENCE_20261010_145723Z.md；
- 最新论文成果优先战略docs/CH5_PUBLICATION_FIRST_STRATEGIC_ROADMAP_20261014.md、V0.0.5终验；必要其他原science accepted文档按精确来源最小展开。

**允许仅针对模型仓的SOURCE_ONLY静态检查**，以已经存在的明确src/validators路径为首选候选，实际名称/代码版本须Codex确认：
- src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py
- src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py
- src/ch5_two_asset_hank/multi_province/province_contracts.py
- src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py
- validators/multi_province/annual_observed_labor_diagnostic/fixed_c8_input_binding.py
- validators/multi_province/annual_observed_labor_diagnostic/integration.py
- validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py
及这些接口实际引用的同仓已跟踪、明确源码/测试文本。可以用有界Git read-only metadata和静态文本搜索确认真实call graph、候选路径、原模型HEAD/dirty类别，**禁止自动跨reparse/另仓/真实reports或private data_local递归探测**。若某历史文件不在此版本，应标NOT_PRESENT/UNVERIFIED，不构造替代locator。

本次**源码正文仅限静态代码与治理合同**，不读取受保护的历史JSON/NPZ/MAT/CSV、真实研究数据或private receipts正文，不计算它们的哈希、不解析、不开任何科学consumer；对外部引用只能记录“引用待新许可”，不得follow目标。禁止Python import/执行代码、动态loader、模型运行、测试进程、VSS、任何Windows敌对文件系统实验，以及Git写入/commit/push/pull/checkout/reset/stash/clean；不动原HEAD/index/dirty/untracked/ignored、C盘B3快照或任何保护源。建议源代码文本检查总量控制在最多60个准确源/测试文件及2MiB，最大120分钟，一次集中只读回报；实际触及新保护门时马上STOP该部分、不中断已授权静态方案整理。以上是**单份提案任务的权限上限**，不是后续真正科学执行的预算。

## 4. 一次性版前交付与冻结前决策

交付唯一 \`V0.0.6_M1_C8_SOURCE_AXIS_UNITS_AND_CONSUMER_CONSOLIDATED_PROPOSAL\`，在当前对话内报告：
1. 原代码 Git HEAD/branch与治理HEAD、accepted code candidate/main的身份及未同步dirty影响；\`NEXT_BASELINE_ADOPTION\`建议与理由，绝不假称当前main已集成;
2. 已接受 vs UNKNOWN/BLOCKED的“source/receipt/result → C8 batch → 31 axis → 年度master → labor/frozen S/C1/firm/wage consumer”的逐跳实证表，带source文件及行段/函数、合同级证据与资格，不复制敏感真实文件内容；
3. 人口/人均、劳动/工资、S目的行/来源列、2017观测/2018目标及方法学价格 vs direct验证逐项差异及最小修正建议，不能改变已采纳经济公式；
4. 一份**完整、可执行但尚未授权**的未来版本内实现大任务建议：准确代码/测试变更路径、最小新功能、拒绝/错误合同、合成验证和资源预算、protect/data/budget依赖，是否必须由Owner决定任何实质科学选择；
5. 主要风险、不会为凑验收重开的旧已消耗调用、真实可达到的验收等级；新实质阻塞一次集中提出，避免微任务与频繁GitHub操作。

**停止点：WAIT_ASTRA_V006_CONSOLIDATED_PROPOSAL_REVIEW / STOP。** 此时原版V0.0.6仍DRAFT、没有冻结实现计划、候选代码或科学执行权限。Astra统一审查和必要Owner决定后才固定正式版本和单独发出实现授权。不得自动启动V0.0.7。
