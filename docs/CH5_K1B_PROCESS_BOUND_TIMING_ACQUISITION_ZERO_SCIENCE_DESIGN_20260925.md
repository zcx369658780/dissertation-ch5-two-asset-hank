# K1B 过程级耗时证据获取设计（零科学调用）

任务 `CH5_K1B_PROCESS_BOUND_TIMING_ACQUISITION_ZERO_SCIENCE_DESIGN_20260925`，派发 HEAD `f780c7fb01878ef119a09624c31edbad88a385d1`；`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。本文只比较将来如何获取证据，**没有实施计时器、创建测量输出根或启动模型**。旧 C6→C8 预算已耗尽，C9 未运行，Results eligibility `FALSE`。[1–4]

## 当前权威与问题

Owner 已采纳完整外层 turn 检查点、协作式 Asia/Shanghai 00:00 暂停及 C8 起步、最多 C9/C10 的新逐省/逐轮/累计**最大尝试调用额度**。[1,2] Owner 同时明确保留 `BLOCKED__DURATION_BOUND_UNAVAILABLE`：在可信的过程级科学耗时及不确定性依据出现前，不同意启动 C9/C10；采纳调用额度本身不授予任何调用。[2,3] 已接受的 C7/C8 清单、账本和执行收据没有可绑定科学进程的单调钟起止，因此仍为 `MEASURED_SCIENCE_RUNTIME_UNAVAILABLE`。文件时间、提交时间、会话时间或调用次数都不是模型耗时。[4]

本工作树的 codebase-memory 图谱不可用（`index_status` 返回未索引）；下面涉及现有 runner 的事实仅来自精确路径的只读核对：`validators/multi_province/k1b_turn7_outer_r2/run.py`、`validators/multi_province/k1b_turn8_outer_r2/run.py`。后者在省份循环前建内存 `results=[]`，31/31 后执行一次集成，随后才写完整科学账本并封存下一轮束；现有运行流程没有可直接用作完整跨日恢复的过程级计时收据。本文不由这些源码推断历史运行秒数。[5]

## 将来测量必须定义的对象与收据

预启动门针对**一个完整外层 turn 能否在下一次本地 00:00 前预期完成**，故主要样本应测同一尝试从测量进程/子进程被正式放行、首个科学入口之前，到该 turn 的 31/31 household、唯一集成、当轮账本、完整清单、下一轮输入束及独立读回完成并返回终态的**总过程单调耗时**。另记首个科学入口至最后科学操作退出的核心区间，以及各省、HJB/KFE、集成、封存/读回区间；总区间不得以仅有成功计算的核心区间替代。测量须用同一机器上单调钟的整数纳秒起止与差值，明确包含预检后启动、等待、I/O、失败处理与收尾的范围；UTC 与 Asia/Shanghai 墙钟只用于执行 ID、日界和审计映射，不用于直接相减。若出现时钟跳变、计时进程或进程树身份不明，样本无效。[1,3,4]

每个未来收据还须绑定：唯一执行/任务 ID、父子 PID 与进程树、完整命令及退出码；冻结 `src`、runner/helper、进入束及 province 顺序/网格/参数哈希；Python、NumPy/SciPy/BLAS 版本、线程数、CPU/内存/存储与负载条件；新**独占且此前不存在**的输出根规范路径/所有权、清单及读回；逐省/逐类/全程先记账的 attempted ledger、被拒调用、失败位置与原始终态。计时观察者不得改变冻结方程、求解器或调用次序。路线 A 的**候选**输出身份是 `D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn8_same_frozen_timing_measurement_run001`，只属一次独立测量，现核对为不存在；未来授权任务须重新核对其不存在、明确采纳路径并独占创建，完成后以清单和读回绑定身份。本任务不创建它。C6-prime、C7、C8 原有三根保持只读。[1,5]

失败或 Owner 手动中止时，保留原始失败、可核实的尝试和测量区间；半途样本只可视为**删失的下界/失败耗时**，不能填成一次完整 turn 耗时。未落盘或模糊尝试须标 `CALL_LEDGER_UNRESOLVED`，首败即停、零重试，不从省级/HJB 中间文件恢复。一个未来测量若本身是完整合法外层 turn，只有在其单独授权、科学身份、清单和独立审查均满足时才可讨论其科学证据；“测到时间”本身既不使其成为 C9，也不自动更新 prospective 计数。[1,2]

## 可支持的两条科学测量路线

| 路线 | 可测到什么、所需新授权 | 对 C9/C10 预启动门的作用 |
|---|---|---|
| **A：另行预算的同冻结输入测量**。候选输入可取已封存 C7 的进入 C8 束（原 `turn8_entering_bundle_manifest.json` 与读回已核对），在全新独占输出根**只做一次**相同冻结输入的完整外层尝试并计时；不触碰受保护 C8 根。[4–6] | 可得到该输入、该运行环境下的一次完整过程样本；旧 C8 运行的预算和结果不能作为此次预算。必须先有新精确任务、单独 Owner 有限额度、输出身份、静态计时/guard 审查及一次性科学许可。若失败或账本不明，停在原始终态。 | 与 C9/C10 输入不同；一次 C8 型样本无法证明 C9/C10 的耗时上界或尾部不确定性。即使重复若干次，也须先采纳外推条件、样本设计和不确定性模型，不能把观察最大值当保证上界。它**可能贡献**证据，但当前不能令 C9/C10 门通过。 |
| **B：把计时附着在未来 C9 本身**，从 C8 的进入 C9 束做一个 instrumented 完整 turn。[1,5,6] | 样本输入最贴近 C9，却在启动 C9 前就必须通过 Owner 保留的耗时预启动门；此时没有可信上界，形成**循环阻断**。把它改名为“测时”不能免除 C9 的科学尝试、独立额度或原始首败账本。 | 当前不可能合法启动。若 Owner 将来明确批准一次**受限的计时例外/启动风险**，须先修改适用的预启动政策并另发精确、一次性任务；即便 C9 成功测得耗时，也只能是一次观察，不自动证明 C10 上界或给 C10 调用权。 |

非科学的静态计时器自检、假数据流程或文件读写基准可验证仪器及开销，却不能替代完整 HJB/KFE 与集成的科学过程耗时。两条科学路线目前均**未获授权**；A 缺少独立测量预算、执行/输出身份及独立审查，且测得样本是否能外推到 C9/C10 未证；B 还被现行 C9 预启动门先行阻断。本文不提出绕开该门的隐式路径。[2–4]

## 独立测量尝试的有限额度候选

以下是路线 A 的**单次、单个完整外层测量尝试**候选，与 Owner 已采纳的 C9/C10 表建立**独立账本**；全部标记 `PROPOSED_NOT_ADOPTED`。它不是旧 C8 的重试许可，不从 C9/C10 额度扣除，也不允许第二次测量。数值沿用已来源化的一个完整 turn 代数上限，作为 Owner 将来判断资源暴露的提案，非预期实际量。[2,6,7] `—` 表示轮级事件；所有省级上限逐省独立。每次失败尝试计数，首败即停。完整后仍需对照 guard 与源账本。

| 独立测量账本类别 | 候选/省/本次 | 候选/本次总额 |
|---|---:|---:|
| source-native initialization | 1 | 31 |
| scalar labor root attempted | 800 | 24,800 |
| scalar labor root returned | 800 | 24,800 |
| corrected policy map | 51 | 1,581 |
| D2/Q assembly | 51 | 1,581 |
| selector evaluation | 40,800 | 1,264,800 |
| scalar selector root invocation（子类共用总额） | 20,000,000 | 620,000,000 |
| direct HJB solve/update | 50 | 1,550 |
| post-update HJB checkpoint | 50 | 1,550 |
| relaxation helper | 50 | 1,550 |
| alpha arithmetic candidate | 2,650 | 82,150 |
| terminal KFE attempt | 1 | 31 |
| SCC decomposition | 1 | 31 |
| restricted dense GESVD | 1 | 31 |
| normalized stationary candidate | 1 | 31 |
| full-Q stationary check | 1 | 31 |
| corrected aggregate evaluation | 1 | 31 |
| firm evaluation | 1 | 31 |
| household batch | — | 1 |
| full integration | — | 1 |
| source-faithful labor reconstruction | — | 1 |
| frozen K1B allocation / feedback alias（同一事件） | — | 1 |
| C1 residual GovInv construction | — | 1 |
| composite wage batch | — | 1 |
| monetary assignment | — | 1 |
| fiscal diagnostic batch | — | 1 |
| completed raw `ra0` vector | — | 1 |
| deterministic next K1B preparation | — | 1 |
| same-S raw next-payoff construction | — | 1 |
| full-space 800×800 GESVD、科学重试、solver substitution、K2/GE/MATLAB/Results | 0 | 0 |

路线 B 如果将来被 Owner 作为计时例外采纳，也需要**另一份**与 C9/C10 账本隔离的有限尝试/输出合同，或 Owner 明确决定该尝试是否正是 C9 并如何计入 C9/C10 上限及 rolling 证据；本文不能一面称其“测量专用”一面把它作为免费 C9。不得先运行再补签。任何未来测量必须有有限过程资源限额及超限语义；目前没有可填写的秒数，也没有 hard `T_owner`。[2–4]

## 从样本到可用时长上界的独立判定

一次完整过程样本只证明**那一次**在其身份、环境和负载下的已观察秒数，不给 C9/C10 的确定性上界。要形成预启动用 `E_upper`，还需事先确定测量对象是否与 C9/C10 足够可比、冻结环境与输入差异、重复样本数和允许的科学预算、失败/删失如何纳入、负载/尾部波动和测时开销，以及上界的覆盖目标、推导方法、不确定性与安全余量；交由独立 Work 审查及 Owner 明确采纳。即使有经验上界，也不是数学保证或硬墙钟停止。协作式午夜政策允许**已启动**操作越过 00:00 到安全点，却不允许在缺少可信预计完成时间时新增入口。[1,3,4]

未来可执行的本地门须以时区感知 Asia/Shanghai 算出下一次当地 00:00，并用可信同机时钟映射判定 `now + E_upper + margin < next_midnight`，同时核对任务级资源与全部剩余额度。`E_upper`、margin 或时钟映射缺失即 fail closed；换日不制造证据。C10 若另日启动，需自己适用的上界与 C9 完整封存/读回及累计账本前检。当前 A/B 都**不能在现行权限与证据下**证明该谓词成立。[1–4]

## 裁决门

首个未解决门是：**Owner 如何准许取得第一份过程级科学耗时，而不暗中放松其保留的 C9/C10 预启动阻断**。较窄的待决选项是单独授权一次 C7 进入 C8 冻结输入的测量，连同独立有限预算、唯一输出根、资源和失败合同；该样本之后仍须单独判定能否外推。若坚持测 C9 本身，必须先由 Owner 明确决定一次受限计时例外及其是否计入 C9/C10，不能由 Builder 推定。无论哪条路径，先有零科学计时/guard 实施与独立审查，后有另行一次性科学许可；测量结果再经独立审查，才可能进入上界/不确定性与日界门的 Owner 决定。当前 C9/C10 不启动，亦无自动后续任务。[2–4]

本任务科学/模型调用、失败尝试和重试均为 `0`。`MEASURED_SCIENCE_RUNTIME_UNAVAILABLE`、`BLOCKED__DURATION_BOUND_UNAVAILABLE` 和 Results eligibility `FALSE` 保持。

## 来源

[1] `docs/CH5_K1B_COMPLETE_OUTER_TURN_COOPERATIVE_PAUSE_OWNER_ADOPTION_20260925.md`；[2] `docs/CH5_K1B_C9_C10_CALL_CEILINGS_OWNER_ADOPTION_20260925.md`；[3] `docs/CH5_K1B_PROCESS_BOUND_TIMING_EVIDENCE_OWNER_DECISION_20260925.md`；[4] `docs/CH5_K1B_POST_R2_TIMING_BUDGET_ZERO_SCIENCE_EVIDENCE_INDEPENDENT_REVIEW_20260925.md`、同任务 `timing_receipt.json`；[5] 上述两个精确 runner 源文件及 `docs/CH5_K1B_DAY_BOUNDARY_CHECKPOINT_RESUME_ZERO_SCIENCE_DESIGN_20260925.md`；[6] C7 根的进入 C8 封存/读回、C8 根的进入 C9 封存/读回；[7] `docs/CH5_K1B_C9_C10_COMPLETE_TURN_TIME_BUDGET_ZERO_SCIENCE_PROPOSAL_20260925.md` 及独立审查。逐文件 SHA-256、三份受保护清单和零调用账本见机器收据。
