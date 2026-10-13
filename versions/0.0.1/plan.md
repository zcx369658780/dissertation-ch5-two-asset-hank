# V0.0.1 正式冻结版本计划（2026-10-13）

- **状态：FROZEN — implementation limited to the explicit Astra approval referencing this freeze commit.**
- **冻结范围：合成家户劳动工程桥接，不含真实科学验证、生产接线或论文 Results。**
- 版前依据：Owner 明确启动第三阶段并授权 Astra 制定与审批版本；Codex 在 2026-10-13 提交 `V0.0.1_EXECUTION_PROPOSAL_DRAFT`，Astra 已审议其执行方案与既有科学保护边界。
- 代码基线身份：`a1db8c114dec0ab69d69a5576e153a7f868cba0e`，模型工作树 `D:\ProjectTemp\c5k1bturn56`，原分支 `codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922`。这是源头提交身份，**不包含其 dirty/untracked/ignored 修改**；Codex 必须再次确认该源头和保全状态。
- **冻结 SHA 不自引用**：此 `plan.md` 首次被设置为 FROZEN 的 GitHub 提交即正式冻结提交；版本登记和独立授权正文另行记录完整 SHA。后续不修改本文件。以下“2026-10-13版前草案”的原目标描述按本冻结增补的精确解释执行；草案旧时态的 preflight 步骤只作为历史准备说明，不是未来额外审批门。
- 本版本不改变 Owner 已采纳的任何科学法则；本次 Astra 批准保留既有两劳动路径，**不构成对未知经济单位的新科学取舍**。

## A. 冻结目标和经济身份

1. **G1 事实定位**：最小范围静态核对当前 source→corrected aggregate→frozen→batch→callback→one-turn→firm 实际入口，逐项区分源码调用点、历史验收、此次合成执行和 `UNKNOWN`。
2. **G2 工程装配**：不触动真实运行控制器或默认生产路径，新增显式 opt-in 的独立合成供应与一次调用装配；实际复用现有 `evaluate_corrected_household_aggregates`、`CorrectedHouseholdAggregates.frozen_output()`、`PreFrozenHouseholdOutputBatch`、`OneTurnInputs`、`run_source_faithful_one_turn`、`reconstruct_migration_labor` 及 `evaluate_firm`。真实 HJB/KFE 不运行。
3. **G3 一条真实合成调用链**：在同一集成测试，以完全虚构、源标签明确的 2–3 个省份输入，通过真实聚合/frozen/batch、明确合成 callback 和一次 source-faithful one-turn，观察到真正 firm 入参，使用观察 wrapper 委托**原 evaluate_firm**，不可用假的 firm result 冒充调用。测试必须同一身份明确、对象不别名、顺序/时点一致；必要的受控 fixture 采用既有 `20×20×2`、F-order `(b,a,z)` 网格规则，而小样本省份数量**不代表真实31省运行或 K1B 覆盖**。
4. **G4 证据与保护**：独立算术 oracle、主要错误拒绝、真实测试进程证据、明确未解决来源/经济单位/价格/时点/人口分母和全部保护状态。实现通过仅能主张 `SYNTHETIC_ENGINEERING`。

**不可混淆的两条劳动路径（冻结为对现行代码的忠实保留，不是新经济法则）：**

- 家户聚合 `Lt` → `batch.household_lt` → `firm_source["Lt_prev"]`，firm 使用它作为历史劳动参照。
- `Ct`、人口、旧工资、税、偏好与迁移成本 → 现有 source-faithful migration 的 `lt_supply` → firm 当前生产劳动 `Lt`。

两者**不要求相等，不允许直接赋值/强制归一化、不激活另行存在的 origin-preserving normalized route**。测试必须分别证明（i）单独改变 household Lt 可改变 Lt_prev 但不直接改变 migration.lt_supply，（ii）单独改变 Ct 按既有公式影响 migration 劳动；不据此声称劳动力统计经济单位已被识别。

## B. 获批实施路径及文件范围

仅新增以下代码/测试文件（必须先检查不存在；路径冲突则停并报告）：

- `src/ch5_two_asset_hank/multi_province/synthetic_household_bridge.py`：显式 `SyntheticHouseholdRecord`、`build_synthetic_household_batch`、`make_synthetic_household_callback`、`run_synthetic_bridge_once`，全部标识 SYNTHETIC/NOT_REAL_SOURCE，未提供生产默认绑定/导出。
- `tests/test_v001_synthetic_household_bridge.py`：同一测试的可观测完整合成路径、独立 oracle、关键拒绝场景和保护不变量。

另获批在**仅新建且无既有文件冲突**的 `EVIDENCE/ch5_v001_synthetic_household_bridge/` 下保存 synthetic fixture、candidate_view、stdout、stderr、exit code、Junit、哈希清单和必要私有本地细节；在 `versions/0.0.1/execution.md` 保存**公开脱敏**的执行结果、源码事实矩阵和保留的失败记录索引。此 `execution.md` 在冻结时不存在，Codex 负责候选证据而非最终验收。

Astra 负责后续 `versions/0.0.1/acceptance.md` 和 `retrospective.md`，Codex 不得自行写接受结论。禁止编辑 `plan.md`、当前科学合同、原 `AGENTS/CURRENT/TASK/REVIEW_GATE` 六份 dirty 治理/路线图文件、`government_assets.py` 和 `middle_stage.py`。禁止修改原有 `one_turn`、`firm`、`migration_labor`、`capital_allocation`、`corrected_household_adapter` 或真实 runtime；允许在测试中临时监测其现有调用但不能修改其源码或默认语义。

本版独立于 steady-state controller 和 K1B runner，**不代表** K1B `S`、raw-ra0、C1、反馈时序、资本网络或均衡正确；现有 source-faithful one-turn 和后续 K1B 经济结构不等同，合成环境下的 firm 运算不是科学承认。

## C. 合成输入与测试冻结标准

**必须通过：**
1. 人造省份标识唯一、按声明顺序映射，阶段与 entering_states/iteration 一致；该 synthetic callback **恰好一次**被显式入口调用；不得自动匹配、默默重排或容忍误标真实来源。
2. 真实 aggregate `Ct/Lt/At/Bt/AtTax` 与独立 oracle 核对，frozen 与 batch 拷贝/不可变；改变源数组不得追改快照。
3. firm 被观察 wrapper 真正调用并委托原算法；`Lt_prev` 与 household `Lt` 相符，`lt_supply` 与 migration 目的地矩阵行和相符；不得要求二者相等。
4. 关键错误拒绝覆盖来源/省份轴/重复缺失/阶段/形状/F-order 映射/非有限质量或 p-g 不一致/非法标志及向量、migration 负 power base 和 firm 非法输入。对于数值上无法辨别的有限转置，不伪称其必然由 guard 检出；以声明校验与非对称 oracle 区分。
5. 实际测试针对精确候选 Git tree 的受限 `candidate_view`，导出候选代码及必要导入闭包、单一配置与测试；验证测试输出引用的模块绝对路径必须在 `candidate_view` 下。不得从原 dirty workspace 动态导入来冒充 candidate test。
6. 完整源到 consumer 事实矩阵严格区分 `SOURCE_ONLY`、`SYNTHETIC_ENGINEERING`、`RUNTIME_REAL`、`SCIENCE`、`RESULTS`；记录实际脚本/库版本、命令、进程时间、STDOUT/STDERR、return codes、失败修复、最终 candidate commit/tree、SHA 和未闭问题。

**失败处理：** 以上关键项缺失时，不得改动冻结标准制造 PASS；结果记 `PARTIAL`/`BLOCKED` 或 `FAIL` 并集中提交现有证据。普通工程问题在以下限额内自行调试，不需要逐步批准。

## D. 资源、备份与授权停止条件

- 单一 V0.0.1 工程尝试墙钟 `<= 4h`，建议 2–3h；只限本版工作，不重新打开任何旧预算。
- 单个 focused pytest 子进程 `<= 120s`，总共 `<= 8` 次；失败尝试计入总数，不通过换名、另进程或新会话重置。
- 单进程；目标 RSS `<= 2 GiB`；本版新证据 `<= 10 MiB`（包含可发布回执，不包含已有证据；若 candidate_view 内容体积造成合理上限不符，在执行前停止并报告）。
- 禁止实际 HJB/KFE/稳态/受保护31省 consumer/C8/C9/C10/真实数据源/政策冲击/IRF/正式实验、部署：对应执行次数 `0`。
- 禁止安装依赖、操作共享全局 Python 环境/pytest 插件配置；对子进程使用局部 PYTHONPATH 和禁用第三方插件自动加载，固定明确 Python 解释器，并做真实 module file/path readback。
- 先核实际模型树、remote、代码 HEAD 与 dirty/ignored；保护原 staged 空和 8 个 tracked dirty/全部 untracked/ignored，备份/发布不等于科学接受。
- 只有科学定义、受保护读取、原文件冲突、范围外写入、无安全候选导出路径、预算耗尽、持续无法取得进展才停并集中报告。普通测试失败在范围与预算内自主修复。
- 旧 `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE`、人口与人均方向和不 `N=P/3` 保持；劳动人数/工时/效率、人口分母、源认证、日历/价格和真实运行仍 UNKNOWN。
- 不清理/reset/stash/rebase/force、无关目录不触碰；只读必要历史。Git 可在**已确认与原模型树一致的仓库**使用精确路径临时 index 创建候选分支 `codex/ch5-v0.0.1-synthetic-household-bridge`，从准确代码基线出发，仅添加两份新代码/测试和本版脱敏执行报告；允许一次普通 non-force push 并回读候选 commit/tree，**不合并 main，不改文档分支原冻结计划，不上传 EVIDENCE 私密或大文件**。如目标分支已存在或推送将非快进，停止并报告，禁止覆盖。
- 候选 branch 与文档发布 branch 不同，公开计划通过固定 SHA 链接。不要求全量测试，不额外引入多模型强制 review，不自动唤起旧 Work。

## E. 最终判定及实施入口

- `PASS` 只表示 G1–G4 的**合成工程闭环**通过，不能提升 `RUNTIME_REAL` / `SCIENCE` / `RESULTS` / `production`。
- Codex 交付一份可复核的执行报告、候选 SHA/tree、真实测试和失败记录、剩余 UNKNOWN/BLOCKED，停止等待 Astra **最终独立验收**。
- 本文件及固定冻结 SHA 不因执行结果变化追改。若本计划有错或科学需要变更，保留原件，关闭或另立版本，Owner 做必要的方向决定。
- 只有在 Astra 使用冻结 SHA 单独发表 `ASTRA_APPROVED_EXECUTION` 后，Codex 才可开始；发布冻结计划本身不代替批准。

---
# V0.0.1 版前计划草稿的历史记录（原草稿，已被上文冻结条款具体化）

- 项目：博士论文第五章·多省份两资产 HANK Python successor
- 版本：`0.0.1`（Owner 于 2026-10-13 授权开始第三阶段版前协商，暂定）
- 文档状态：`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`
- 发布用途：Astra 的候选目标与验收条件，供 Codex **只读**制定执行方案；**本文件当前不是正式冻结版本，不构成代码改动、测试或科学运行许可**。
- 所在文档分支：`migration/astra-workflow-20261012`
- 形成草案时的文档基线：`ed3c1780b0ac2fdf707c17347d8f0f25bbbd8d6d`
- 已报告的本地代码截点（必须由 Codex 再核）：`D:\ProjectTemp\c5k1bturn56`，分支 `codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922`，HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e`；本地 dirty 与未跟踪资料不可被此文档分支覆盖。
- 版本冻结依据、Owner 最终方向裁决、正式代码基线与执行授权：**尚未发生，待 Codex 方案审议后单独登记**。

## 1. 为什么选这版

根据 `docs/CH5_TWO_ASSET_HANK_ROADMAP_CURRENT.md`、`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`、`SCIENTIFIC_DECISIONS.md`、`docs/knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md` 和 2026-10-11 已发布证据账：
家户劳动局部 `sum(z*l*p)`、corrected adapter、frozen 投影候选、one-turn batch schema、callback 消费与 firm 局部路径已有不同层级的历史接受；但真实 solver 来源→聚合/frozen 调用→batch 实际构造→callback 装配→firm 的端到端链未获完整接受。末 binding SOURCE_ONLY 任务因交付缺失而 NOT_ACCEPTED/CLOSED；其 prepared/缓存信息不能充作已落盘或实际绑定。劳动人数/工时/效率及人口分母/时点尚未定性。科学计算与 Results 均未获得许可。

首版优先形成一条**受控合成输入的可核验工程桥接路径**，为后来真实来源认证和量纲/经济解释提供明确接点。**它既不声称修复全部真实数据桥，也不直接进入 C9、GE 或论文 Results。**

## 2. 计划目标（需由 Codex 以真实代码提出实现方法）

G1. **现状定位与差异账**：只对有根据的相关模块及调用点作有界核查，绘制当前 source→adapter→frozen→batch→callback→one-turn→firm 的实际调用图。区分 `IMPLEMENTED_AND_CALLED`、`IMPLEMENTED_NOT_BOUND`、`ONLY_DECLARED`、`NOT_LOCATED_WITHIN_CHECKED_SCOPE` 和 `UNKNOWN`，逐条给准确源码路径、符号、行/commit 与证据级别。不可因有相同字段名或 import 就认定真正接线，不得复活末 binding 旧失败任务。

G2. **局部工程贯通**：在保留已有科学 law、公开 API 与原数据不变的前提下，优先复用已存在的 adapter/batch/callback 组件，对缺失的**纯工程传递/调用装配**提出最小实现。允许为合成演示添加显式 opt-in/in-memory harness 或小型测试辅助；不能激活生产默认路径、改真实 runtime 科学计算或回填缺失经济单位。若真实代码显示贯通需要改变科学对象、参数、时序、劳动力经济定义或受保护数据接口，则该部分应以准确 BLOCKED/UNKNOWN 报告，不作为随意工程修复。

G3. **可重现的合成证据**：用明确标记 `SYNTHETIC/NOT_REAL_SOURCE` 的内存小样本，通过真实可用的非科学 adapter、构造器、callback 及 firm 入参边界（可使用受控的真实函数与 stub solver/firm 边界），证明数据按声明映射传递、拷贝/形状/省份顺序和状态时点约束受检查，输入错误 fail closed。不得仅通过将若干未连接的单元测试拼接声称端到端，也不得把受控 stub 结果表述为真实 HJB/KFE、31省生产或经济闭环。测试数量不作机械门槛，以覆盖已识别的重要正/负路径为准。

G4. **证据与接口边界说明**：交付一份易查的 source-to-consumer 事实矩阵、合成测试结果及准确命令/进程/耗时/依赖/哈希，明示未认证的来源、全量人口映射、劳动单位、价格与时间语义、保护状态、生产启用条件及剩余阻塞。已有同等质量、可核验的组件直接复用；若根本无须代码改动，可凭真实贯通证据说明，但不得以陈述代替验证。

## 3. 强约束与排除

- **本版科学基线不变**：原两资产模型、20×20×2/F-order、HJB/KFE、D1/D2/D3 selectors、已冻结的 K1/K1B/S 矩阵与 raw ra0/lagged 回报、C1、资产基金、网格/容差/停止律、人口/人均方向不改；不 `N=P/3`，不默认归一化劳动，不悄悄将 `Lt` 认作人数/工时/效率劳动；不调整 fiscal/price/shock/GE 方程。
- `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、`window UNACCEPTED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、`model_activation=False`、`Results FALSE` 及闭合预算保持。不可换名、换入口重跑旧任务。
- 禁止本版读取/运行被关闭授权的真实31省产物与 consumer、受保护 JSON/NPZ/CSV/MAT、真实 solver/HJB/KFE/outer turns、C8/C9/C10、GE、正式试验、IRF、福利、Results 或部署；不得通过 stub 模拟假装真实验证。
- 不改两个既有 dirty 源码（交接列出的 `government_assets.py`、`middle_stage.py`）及无关私有/untracked/ignored 文件；若经核查必须触碰，由 Codex 在执行方案中单列冲突/保护提案，未获新授权不得实施。
- 不改科学合同或冻结计划；不修改默认环境、全局配置、Zotero/DeepLearning-HANK/EliteSync 仓库；不清理、stash/reset、force push、合并 `main`、上传敏感数据/原始日志。
- 学科真实性优先于 PASS：真实未连通可保持未通过，明确证据断点即可；不得以降低 guards、伪造 source provenance/标签或改变目标验收条件来造成功能完整的表象。

## 4. 预拟验收标准（冻结前可经版前协商准确化）

A. 真实代码基线及修改范围可追溯：记录模型 worktree/remote/HEAD、dirty/保全状态、新候选 SHA/tree、显式变更路径，证明不覆盖原有资料与历史合同。
B. 实际调用关系有源码和受界执行证据，至少完成一条同一测试中贯通的**合成输入**链，从家户端模拟输出经实际 adapter/frozen/batch/callback 到最终 firm 劳动入参边界；若组件确实不存在或需科学越界，不造假，通过 BLOCKED 分类并经 Astra 判定是否部分接受，而不假称完整 PASS。
C. 合成正向与关键错误拒绝测试由实际命令执行，结果、异常和输入标签可检查；保留一条可复现的测试命令及明确运行依赖，不允许按旧固定次数门复制繁琐行政审查。
D. 一份区分 `SOURCE_ONLY` / `SYNTHETIC_ENGINEERING` / `RUNTIME_REAL` / `SCIENCE` / `RESULTS` 的证据矩阵。除合成工程外一律不自动授予更高资格。
E. 原指标、科学 law、关闭状态与真实数据保护不变；未擅自更改模型默认生产行为、旧回执或本地其他成果；候选及验收材料在 GitHub 以明确、可读、脱敏的固定身份交付。
F. Codex 完成后只集中交付候选、测试回执、失败修复和未知项；Astra 按**正式冻结后**标准做最终独立验收与复盘。计划草案不得被当成已经批准的科学运行许可。

## 5. 版前必须先完成的 Codex 执行方案草稿（当前唯一行动）

当前准许：Codex 对唯一模型工作树及 GitHub 已授权公开/脱敏正文进行**最少必要只读核查**，编写并在会话中返回 `V0.0.1_EXECUTION_PROPOSAL_DRAFT`；不得写代码/修改文件、运行测试、创建候选提交或开始模型求解。

草稿须包括：
1. 真实线程/host/projectId/cwd、模型绝对 worktree、branch/HEAD/dirty 状态；`projectId=null` 只列未确认证据，不冒充网页项目资格。说明拟采用安全的模型工作目录/隔离方式，不从聊天 CWD 推论权限。
2. 有界源码定位及上述 G1 现有实现/缺口，逐符号列预计触及的具体路径、已有 dirty 路径可能冲突、可使用与不可使用的输入；不以全仓反复扫描代替定位。
3. 拟实施的最小变更、可观测测试链路与 positive/negative cases；说明如何避免通过 stub 虚构真实链、如何保留 scientific-law 不变量、如何标记 SYNTHETIC。
4. 预计依赖、确切测试命令类型、合理资源/时间上限、失败后自主修复策略与必须停点；不重新申请历史科学预算。
5. 交付文件、Git 提交/发布策略和拒绝敏感产物的办法；会话 context 续接只延续同一冻结目标。
6. 任何科学、数据、权限与保护分歧列入 `OWNER_DECISION_REQUIRED`，不擅自选法则。

返回草稿后 `WAIT_ASTRA_PLAN_REVIEW / STOP`。Astra 审核，可要求一次性集中澄清或与 Owner 作实质取舍；之后另行生成**固定提交的正式冻结计划**并明确批准 Codex 执行方案。只有看到明确 `ASTRA_APPROVED_EXECUTION` 和对应冻结 SHA，Codex 才能无实时监督自主实施与正常工程调试。未经此门**不执行、不测试、不发代码候选**。

## 6. 里程碑和边界

- 目前：`DRAFT / NOT FROZEN / NO ENGINEERING EXECUTION`。
- 接下来：Codex 只读执行方案草稿；Astra 审议与必要 Owner 科学取舍；冻结版 `0.0.1` 的计划 SHA/代码基线/资源约束；Codex 自主实施；集中验收与复盘。
- `versions/0.0.1/execution.md`、`acceptance.md`、`retrospective.md` 为拟议后续位置，当前**未创建**，不将空文件视为完成。
- 本版不是成果论文、正式版本发布、科学 fixed-point/GE 接受；后续路线依据本版证据再决定。
