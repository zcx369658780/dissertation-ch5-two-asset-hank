# V0.0.2 版本计划草案：家户求解输出来源契约与输入准入边界

**日期**：2026-10-13（Asia/Shanghai）

**状态**：`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`。

**版本性质**：Owner 已在 V0.0.1 正式关闭并同步 V1.1 后，明确要求开始规划下一版本。此文件仅为 Astra 版前目标草案，供 Codex **只读核查并提交执行方案**。**没有冻结计划，没有实施授权，没有任何新测试或科学运行许可。**

## 1. 版本位置与严格代码基线

- 研究项目：第五章多省份两资产 HANK Python successor；唯一模型工作树此前由 Codex 报告为 `D:\ProjectTemp\c5k1bturn56`，执行前须自行重新核对。
- 当前工作流：[V1.1](../../docs/CH5_ASTRA_WORKFLOW_CURRENT.md)，当前状态：[CURRENT](../../CURRENT.md)，科学接受合同：[SCIENTIFIC_DECISIONS](../../SCIENTIFIC_DECISIONS.md) 及需要的原采纳文件。
- V0.0.1 `CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`，冻结提交 `6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8`，接受的代码候选提交 `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`、tree `39e7a91ca473ba770bd65518607c3f78f4b9fe24`，位于 `codex/ch5-v0.0.1-synthetic-household-bridge`。其接受不包括真实上游来源或经济单位认证。
- 更早模型代码截点 `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，原本地分支 `codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922`；本地此前报告有未提交代码与大量 untracked/ignored 资产。
- 当前 GitHub 对比显示 `main` 并未包含 V0.0.1 候选；禁止默认从 `main` 开始或把已接受等同于已集成。
- **`NEXT_BASELINE_ADOPTION=UNDECIDED`**：Astra 倾向在不冲突且有复用必要时以 V0.0.1 的固定候选为 0.0.2 的候选代码起点，但该建议**不是采纳或合并命令**。由 Codex 在草稿中对比分支、未提交成果、路径/依赖和最小变更方案，再由 Astra 在正式冻结时明确 `ADOPTED_FROM_EXACT_SHA` 或 `NOT_ADOPTED`。不得 reset、merge、rebase、clean 或覆盖原 worktree。

## 2. 本版科学问题与已有源码事实

V0.0.1 已受界验证：明确标记的虚构省份政策/质量 → `CorrectedHouseholdAggregateInputs` → `evaluate_corrected_household_aggregates` → `FrozenHouseholdOutputs` → batch → 合成 callback → 一次 source-faithful one-turn → firm 的工程路径。它不是实际生产接线。

本次审查到的 **静态源码** 显示：
- `exports/matlab_faithful_two_asset_ha.py` 的 `HouseholdSteadyStateResult` 暴露 `hjb`、`kfe`、`aggregates`，其 `solve_household_steady_state` 会调用真实 HJB/KFE；**本版不能调用**。该 API 对应的 MATLAB-faithful 路线不可自动视为已采纳 corrected checkpoint 的同一结果源。
- `src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py` 明确要求 `consumption`、`labor`、`b_grid/a_grid/z_grid`、`effective_r_a`、`probability_mass`、`density`、`omega` 和 `source_r_a`；`AtTax` 由既有公式计算，不能假定是全部 HA solver 直接输出的字段。
- `src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py` 和 `scripts/ch5_mp4c_2018_corrected_household_aggregate_binding.py` 含受保护真实 checkpoint/receipt 的既有聚合装配例子。它们可作为**有界只读源码来源**，不能因存在源码而重新读取 protected NPZ/JSON、执行旧脚本或复活 `NOT_ACCEPTED/CLOSED` 任务。
- 量纲/人口分母、数据年份/价格、真实结果身份、HJB/KFE 到 corrected 数组的完整 producer→consumer 链仍 `UNKNOWN`。人口/人均决策保持，户均封存，不 `N=P/3`。

所以本版的目标是定义上游边界的**可审查、可拒绝的输入条件**，而不是宣称已找到、认证或执行了真实 source。

## 3. 候选版本目标（Codex 需实地核实可行性）

**G1 · 实际字段来源与权威交叉表**：对可能被采用的 HA result、corrected policy、mass/密度、effective return、frozen 与后续消费者做有界源码交叉，逐字段写明源符号/路径/形状/轴序、必须联合的 checkpoint 与省份标识、所需来源 seal/manifest、年份/期次、数值/经济解释及当期证据资格。清楚区分 `SOURCE_ONLY`、`HISTORICAL_ACCEPTED`、`SYNTHETIC`、`LOCAL_ONLY/UNKNOWN`。对无法认证的输入标 `UNRESOLVED`，不能以字符串/文件名或旧回执存在推导其真实性。

**G2 · 受限 typed boundary 提案**：优先复用 corrected adapter 现有字段及 validation，设计一个**独立 opt-in 的外部输入身份与契约检查对象**（最终文件和 API 由 Codex 提案）。明确提供者类别、假想/历史/未验证身份、同省份/同阶段/同来源的引用完整性、(b,a,z) F-order / p–g–omega 映射、uniform vs effective illiquid return、输出资格。来源不明必须 fail closed，不能把 `SYNTHETIC` 自动改称真实。若此处需要查看受保护资料才能确定关键字段，则此版本可将对应字段保持 `REQUIRES_OWNER_AUTHORIZATION`，而非造一个“REAL_AUTHENTICATED”布尔字段绕过验证。

**G3 · 只读源码 + 合成负向验证方案**：若 G2 可在不碰现有科学源码的前提下完成，拟允许新增有限、纯内存/明示模拟记录的单元/集成测试，证明声明一致时的结构传递、来源冲突/省份轴混乱/错期/缺字段/错 omega/错误 provenance 的明确拒绝。严禁真实 HJB/KFE、C8/C9/C10、31省实际 producer/consumer 或 protected source loader。不能把只读源码检查的 `PASS` 写成真实运行时 `PASS`。

**G4 · 留下进入下一门的精确问题清单**：交付一份 future source-loader/真实来源认证需要的 typed 输入、需要 Owner 科学或数据选择的最小事项、保护资产读取许可清单（**仅建议，未批准**）、允许验证与禁止验证的清晰区分，以及最小脱敏验收摘要。不得自行安排下一步真实数据调用或自动开始 V0.0.3。

## 4. 版前拟定的验收原则（当前不构成冻结标准）

A. 一份可逐字段审查的 producer→corrected aggregate/frozen→下游 consumers 来源表；每项带真实源码位置/版本身份/证据级别，不能使用历史合成桥掩盖真实来源缺口。

B. 如批准实施 typed boundary，结构约束应 fail closed，拒绝错 source、错 axis/F-order 声明、跨省混配、跨阶段、缺 seal 与假冒认证。**不过无法仅凭字段名、摘要 hash、标签或 synthetic 数据证明外部真实来源可信**；认证不足必须明确表述。

C. 如实施合成 focused 测试，使用精确 candidate Git tree 的限定视图/模块来源回读，做独立 oracle 和必要错误拒绝。保证既有 HJB/KFE、K1B、C1、劳动路径 `Lt_prev` vs `lt_supply`、收益/时序与科学 guards 不变。不重开旧额外科学测试预算。

D. 交付完整但精简的脱敏证据摘要：代码 baseline/candidate/tree、实际新增/修改路径、运行级别、精确或脱敏命令/退出码/耗时/进程次数、失败/纠正、SHA/原回执本地界限、经济/来源 UNKNOWN，区别 GitHub 独立已核、Codex 本地报告与未验证事项。

E. 本版仍只可能接受 `SOURCE_CONTRACT/SYNTHETIC_ENGINEERING` 有界成果，不可能据此给予 `REAL_RUNTIME`、`SCIENTIFIC_VALIDITY`、`GE`、`RESULTS`、生产或安全放行。若经核查工程变更需更改已采纳科学法则或受保护数据访问，则提出 `BLOCKED` 与替代路线，Astra 不要求造假完成 G2。

## 5. 明确禁区与现有停点

- 现阶段**仅 Codex 版前只读调查**，不能修改文件、运行测试、创建/推送候选、启动旧任务或碰真实科学数据。
- 未来若批准实施，须先冻结 G1–G4 的实际 scope、允许文件路径、资源预算和证据门，明确哪类“测试/诊断/科学调用”为 0；`main` 合并与旧本地代码切换不是本草案隐含权限。
- `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、`model_activation=False`、`Results FALSE` 及旧 CLOSED 预算不变。不得读取/写入真实31省回执和旧保护 JSON/NPZ/CSV/MAT，不能通过更换路径/测试名绕行。
- 不能改 HJB/KFE 数值法则、KKT/边界、参数/网格/容差、`S` 矩阵、payoff/raw-ra0/lagged timing、C1、经济劳动单位/人口分母，不能把旧 MATLAB 顺序静态演算作为已证的动态政策结果。
- 不改两个历史 dirty 源码、历史工作树其他成果、global 配置、Zotero 独立仓库、DeepLearning-HANK 或 EliteSync。用户手动决定科学/权限实质取舍。

## 6. 当前唯一授权的 Codex 交付：执行方案草稿

Codex 只读实际核验以下项目并回报 `V0.0.2_EXECUTION_PROPOSAL_DRAFT`：
1. 当前线程/host/projectId、真正模型 top-level/remote/branch/HEAD、staged/dirty/untracked 保全与当前发布分支 SHA；读取 V1.1 规则和**本完整草案**，对比 V0.0.1 已接受代码与原工作树，以源码证据提出 `NEXT_BASELINE_ADOPTION` 推荐。
2. 有界逐字段来源图：real/accepted/corrected 结果路线的实际差异、需要静态 crosswalk 的现存源码位置、可能可复用组件。对缺失真实来源的准确 `UNKNOWN` 清单，不索取或读取旧 protected archive。
3. 最小 typed boundary/metadata/checker 的建议职责、精确新增文件/测试路径、positive/negative 的模拟场景、明确不可认证的类型；若不应编码则建议 DOCUMENT_ONLY 的替代。
4. 符合 V1.1 的分层资源预算提议（普通工程/测试、科学调用 0、Git operational index、candidate_view、local receipts、公开脱敏证据），不机械沿用 V0.0.1 的4小时/8次/10MiB。
5. 版本冻结后交付的 candidate/tree、脱敏 receipt/hash 与 Git 不破坏路径方案；必须停的科学/数据/权限问题与需要 Owner 决定的事项。

Codex 回复完整草稿后 `WAIT_ASTRA_PLAN_REVIEW / STOP`。**Astra 未发布固定冻结计划 SHA 与独立 `ASTRA_APPROVED_EXECUTION` 前，不得实施。** 草案不是科学规则采纳、真实 source 认证、测试授权或新工程 candidate。

## 7. 当前状态

- V0.0.1：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`，无需要补交/重跑/返工的本版义务。
- V0.0.2：`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`，未冻结。
- `NEXT_BASELINE_ADOPTION=UNDECIDED`，Codex 推荐后由 Astra 冻结正式决定。
- V0.0.3 及后续：NOT_STARTED。
