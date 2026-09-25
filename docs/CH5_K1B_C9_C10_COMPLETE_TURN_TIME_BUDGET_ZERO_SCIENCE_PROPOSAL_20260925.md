# C9/C10 完整外层 turn 跨日时间与调用预算提案（零科学调用）

任务 `CH5_K1B_C9_C10_COMPLETE_TURN_TIME_BUDGET_ZERO_SCIENCE_PROPOSAL_20260925`；派发 HEAD `2d3d62d50cfaf281ec6f3c051077690bba1cecb9`，冻结 `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。本文全部新调用上限标记为 **`PROPOSED_NOT_ADOPTED`**；不是 Owner 批准的 C9/C10 预算，也不是执行任务。旧 C6→C8 两轮预算已耗尽，终态 `VALID__LEVEL_NOT_MET_AT_BUDGET`；C9 尚未运行。Results eligibility `FALSE`。[1–4]

## 已采纳的边界与未来比较

Owner 已采纳**完整外层 turn** 检查点及**协作式** Asia/Shanghai 当地 00:00 暂停：预启动门不通过时不开始新科学单元，已在运行的操作不由午夜强制杀停，可越过 00:00 运行到下一个安全边界；Owner 可手动停止。[1] 只有 31/31 HJB/KFE、一次完整集成、当轮 raw `ra0`、下一轮进入束、完整 attempted ledger、输出清单与独立读回都合法封存，才可称为可跨日保存的完整 C9。省级 terminal、HJB 清单或半途操作不是可恢复检查点。[1,2]

以已接受且封存的 C8 为起点，未来新计数器从零开始。C8→C9 与 C9→C10 各须是完整合法相邻比较，沿用已采纳的九项载体、公式与每项严格 `<1e-6`；九项全过才加一，合法未过则归零。两次**新的连续全过**只构成待独立审查的有界数值判据候选，最多 C9/C10 两个新完整 turn；旧 C6→C7、C7→C8 不计入新计数。科学、身份、预算或封存失败在最早原始终态停下，不更新计数；C10 后未达两次连续通过是有界未达标，不得称为发散。clipped-`ra` 仅按新九项判据 report-only，原 MATLAB 零命中判据分开。[3,4]

## 唯一输出根、暂停与次日预检（拟议实施契约）

未来精确任务须预先指派**两个不同的、此前不存在的** C9/C10 输出根，记载每根规范化绝对路径、父目录与独占创建证据、文件身份及完整预期清单；禁止覆盖、重用、换根、链接/重解析点替换或清理 C6-prime/C7/C8 三个受保护根。C9 的输入只来自 C8 已封存且读回的进入 C9 束；C10 输入只来自未来完整 C9 的新封存。C8 的 `turn9_entering_bundle_manifest.json` 与 `turn9_entering_bundle_readback.json` 身份分别见收据；它们是输入来源，不是 C9 调用权。[1–3,5]

每轮严格按冻结输入与省序 → 31/31 合法 household → 一次集成 → 完整输出清单及 next-turn 输入/方案 → 独立读回 → 九项比较的顺序。计划暂停只能在整轮的账本、清单及读回**全通过**后写入暂停收据：执行 ID、冻结 `src`/输入/省序、C9 清单哈希、下一未进入 C10、滚动计数、两轮总额与各省/各类/各轮累计已尝试及余额、输出根身份、原始终态和时钟门。若 C9 合法完成而当日不宜启动 C10，停在 `SAFE_PAUSE_AFTER_SEALED_C9`；跨日不重做 C9。若 C9 还未完整封存，则没有计划暂停或合法比较。[1,2]

次日 C10 **任何科学入口前**重新验证 C9 的独立读回及完整清单、C8/C9 链、冻结源码/进入束/省序/九项轴与 return 时序、输出根独占性、前日终态为计划暂停，以及持久账本 `已尝试 + 剩余额度 = 同一获批总额`（逐省、逐轮、两轮累计）。再用当日新门评估 C10 是否可开始。日期变化不清零、不借用额度；已完成、失败或可能已进入的调用均不得免费重做。身份、账本或读回不一致，保留最早失败并停机。[1,2]

每个科学调用应在进入前持久记载执行 ID、类别、省份、turn、尝试序号与预算扣减，再执行及持久化结果；类别别名 `k1b_feedback_calls` 与同一次 frozen K1B allocation **共用一次事件**，不可变成第二次反馈。首个身份、科学、时间门、调用额度、封存或读回缺陷均终止，失败尝试计数，重试为零。Owner 手动中止正在运行的操作时，只保留之前已完整封存的检查点，记录已确认的尝试；任何不确定或未完成总账标 `CALL_LEDGER_UNRESOLVED`，不推算余额、不从中断处自动继续、不重跑该调用。恢复须先有新的 Work/Owner 处理决定。手动中止不等于计划暂停。[1,2,4]

## 有限调用上限候选

下表每一个“候选”列均为 **`PROPOSED_NOT_ADOPTED`**。它把旧 C6→C8 已采纳但**已耗尽**的代数上限重新列为未来决策素材，并给出实际 C7/C8 计数以防把观察值当额度。`—` 表示该类别是轮级事件，不存在逐省额度；`0` 是禁止类别。31 省，最多每省 50 次 direct HJB update、51 次 policy/Q map；每图 800 次 selector evaluation；每更新最多 53 个 alpha 算术候选。[4,6–9] 未来执行任务必须逐项指定新的真实授权额与 guard 入口，不能直接引用此表替代 Owner 决定。

| 类别 | 候选/省/轮 | 候选/C9 或 C10 | 候选/两轮累计 | 已观察 C7 / C8 |
|---|---:|---:|---:|---:|
| source-native initialization | 1 | 31 | 62 | 31 / 31 |
| scalar labor root attempted | 800 | 24,800 | 49,600 | 24,800 / 24,800 |
| scalar labor root returned | 800 | 24,800 | 49,600 | 24,800 / 24,800 |
| corrected policy map | 51 | 1,581 | 3,162 | 409 / 409 |
| D2/Q assembly | 51 | 1,581 | 3,162 | 409 / 409 |
| selector evaluation | 40,800 | 1,264,800 | 2,529,600 | 327,200 / 327,200 |
| scalar selector root invocation（全部子类合计） | 20,000,000 | 620,000,000 | 1,240,000,000 | 141,129 / 141,125 |
| direct HJB solve/update | 50 | 1,550 | 3,100 | 378 / 378 |
| post-update HJB checkpoint | 50 | 1,550 | 3,100 | 378 / 378 |
| relaxation helper | 50 | 1,550 | 3,100 | 378 / 378 |
| alpha arithmetic candidate | 2,650 | 82,150 | 164,300 | 382 / 382 |
| terminal KFE attempt | 1 | 31 | 62 | 31 / 31 |
| SCC decomposition | 1 | 31 | 62 | 31 / 31 |
| restricted dense GESVD | 1 | 31 | 62 | 31 / 31 |
| normalized stationary candidate | 1 | 31 | 62 | 31 / 31 |
| full-Q stationary check | 1 | 31 | 62 | 31 / 31 |
| corrected aggregate evaluation | 1 | 31 | 62 | 31 / 31 |
| firm evaluation | 1 | 31 | 62 | 31 / 31 |
| household batch | — | 1 | 2 | 1 / 1 |
| full integration | — | 1 | 2 | 1 / 1 |
| source-faithful labor reconstruction | — | 1 | 2 | 1 / 1 |
| frozen K1B quantity allocation / feedback alias | — | 1 | 2 | 1 / 1 |
| C1 residual GovInv construction | — | 1 | 2 | 1 / 1 |
| composite wage batch | — | 1 | 2 | 1 / 1 |
| monetary assignment | — | 1 | 2 | 1 / 1 |
| fiscal diagnostic batch | — | 1 | 2 | 1 / 1 |
| completed raw `ra0` vector | — | 1 | 2 | 1 / 1 |
| deterministic next K1B preparation | — | 1 | 2 | 1 / 1 |
| same-S raw next-payoff construction | — | 1 | 2 | 1 / 1 |
| full-space 800×800 GESVD | 0 | 0 | 0 | 0 / 0 |
| scientific retry / solver substitution | 0 | 0 | 0 | 0 / 0 |
| K2 / GE / MATLAB / Results calls | 0 | 0 | 0 | 0 / 0 |

独立 selector root 子类如 interior-Z 只是上述同一总类的分解，**不另给额度**。每类失败尝试占额度；每省额度不可互借，两轮累计跨日延续。旧“third outer turn = 0”是旧窗口的终止边界，不可机械复制到 C9；新窗口只拟最多 C9/C10，并须由 Owner 明确采纳。[4,6–9]

## 午夜预启动门与尚缺的时间权威

接受的计时核查结果是 **`MEASURED_SCIENCE_RUNTIME_UNAVAILABLE`**：C7/C8 清单和进程结果没有绑定同一科学尝试的单调时钟起止、逐省/阶段耗时或 CPU/GPU 计时；文件 mtime、Git 提交时间、会话长度和调用计数都不能换算成时长。[8] 因此这里**不填写**预计分钟、开始时刻、安全余量或 `T_owner`。当前没有可信上界时，任何未来 C9 或 C10 科学单元的预启动门均为 `BLOCKED__DURATION_BOUND_UNAVAILABLE`；不能因为换到次日就假定可完成。[1,2,8]

未来门须使用时区感知的 `Asia/Shanghai` 下一次本地 00:00，映射到 UTC 与进程单调钟；每个拟启动单元需有适用于冻结输入、同类机器与执行环境的过程级时长上界 `E_upper`、测量方法、样本范围、启动/退出边界、失败与尾部不确定性及明确安全余量，并证明 `now + E_upper + margin < next_local_midnight`，同时满足新获批的有限进程级资源上限与全部调用余额。时钟或时区映射异常时停止新增入口。Owner 也可明确选择承担缺少可信预期上界的启动风险，但那是**新的资源政策决定**，不能由本文代替现行“预计不会跨 00:00”要求。协作式暂停不构成正在运行操作的硬午夜停止或硬墙钟上限；若 Owner 另要求硬上限，需要另行定义外部监护、终止及不确定账本后果。[1,2,8]

## 剩余决策与后续门

1. GPT Work 对本零科学候选独立 `ACCEPT/REJECT`；Builder 不自验收。
2. Owner 决定 C9/C10 **每个类别、每省、每轮和两轮累计**的新有限尝试额度、进程资源上限及其跨日口径，并给出可信过程级时间与不确定性证据，或明确改变无可信时长时的启动风险政策。任何测量科学尝试自身也须单独预算与授权。
3. Work 另发精确路径的**零科学 runner 实施**任务，静态检查独占输出根、先记账、C9 封存/暂停、次日 C10 只读前检、时钟变化、首错、手动中止与零重试；GPT Work 独立审查。本文不实现 runner。
4. 之后才可能有**单独一次性** Owner 科学执行授权和 Work 任务；C9 不自动授权 C10。无任务不得调用模型。数值判据候选仍须独立审查，不产生固定点、GE 或 Results 权威。

本任务科学/模型调用、失败尝试、重试均为 `0`。首个未解决门是缺少可信过程级时长上界或明确 Owner 启动风险决定；新的有限调用/资源额度也尚未获采纳。Results eligibility `FALSE`。

## 来源

[1] `docs/CH5_K1B_COMPLETE_OUTER_TURN_COOPERATIVE_PAUSE_OWNER_ADOPTION_20260925.md`；[2] `docs/CH5_K1B_DAY_BOUNDARY_CHECKPOINT_RESUME_ZERO_SCIENCE_DESIGN_20260925.md` 及独立审查；[3] `docs/CH5_K1B_POST_R2_PROSPECTIVE_ROLLING_RULE_OWNER_IN_PRINCIPLE_ADOPTION_20260925.md`；[4] `docs/CH5_FULL_OUTER_STATE_STOP_FAILURE_BUDGET_OWNER_ADOPTION_20260925.md`；[5] C8 根的 `turn9_entering_bundle_manifest.json` 与 `turn9_entering_bundle_readback.json`；[6] `docs/CH5_OUTER_STOP_FAILURE_BUDGET_CONTRACT_PROPOSAL_20260923.md`；[7] C7/C8 各自的 `turn7_scientific_ledger.json`、`turn8_scientific_ledger.json`；[8] `docs/CH5_K1B_POST_R2_TIMING_BUDGET_ZERO_SCIENCE_EVIDENCE_INDEPENDENT_REVIEW_20260925.md` 及其 `timing_receipt.json`；[9] `SCIENTIFIC_DECISIONS.md`。逐文件 SHA-256 与三份受保护清单 SHA-256 见同任务机器收据。
