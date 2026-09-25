# K1B prospective C9/C10 计时证据与预算门（零科学调用）

任务 `CH5_K1B_POST_R2_TIMING_BUDGET_ZERO_SCIENCE_EVIDENCE_20260925`。起始 HEAD `172fb2197aff2d20fb3e87c76bd299d223ba757b` 为派发基线 `fe94e8d55e2d29a0b88e6a4388a95137bfba3ade` 的已提交后代；`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`，开始时无跟踪文件改动。Owner 仅原则同意从 C8 开始、最多 C9/C10 两轮的 prospective rolling 设计基础，并授权本次**零科学计时核查**。新调用额度、硬超时、runner 和 turn9 均未获授权；Results eligibility 为 `FALSE`。

## 封存范围和计时载体清单

核查严格限定在本工作树内三份既有未跟踪输出根、其封存文件，以及任务单点名的接受文档和收据。三根各有 5,142 个文件（3,442 JSON、1,700 NPZ），均无名为 log、timing、elapsed、duration、runtime、process、stdout、stderr 或 clock 的文件。清单 SHA-256 已重核：

| 输出根（完整路径前缀 `reports/`） | 完整清单 SHA-256 | 顶层已查计时候选 |
|---|---|---|
| `ch5_turn6_same_frozen_input_repeat_20260923_run001/` | `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61` | `preflight.json`、`terminal_receipt.json`、`turn6_scientific_ledger.json`、`comparison_receipt.json`、进入 turn7 的封存/读回 |
| `ch5_k1b_turn7_outer_r2_20260925_run001/` | `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91` | 对应 turn7 四项收据、进入 turn8 的封存/读回 |
| `ch5_k1b_turn8_outer_r2_20260925_run001/` | `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301` | 对应 turn8 四项收据、进入 turn9 的封存/读回 |

对三根各 3,442 份 JSON 的**键名**作只读定向检索：`elapsed`、`duration`、`timestamp`、`started_at`、`finished_at`、`start_time`、`end_time`、`cpu_time`、`gpu_time`、`process_id`、`wall_clock`、`monotonic`，以及独立的 `pid/start/end` 等精确键，均无匹配。对三根各 1,700 份 NPZ 只读检查成员名；没有计时数组；`q_times_one.npy` 中的 `times` 是矩阵乘法命名，不能解释成时间。接受的 turn7/turn8 执行报告及机器收据只给单次调用、进程退出码、科学账本、输出读回和数值终态，未给科学进程的开始/结束时间、同一单调时钟的耗时、CPU/GPU 计时、逐省/阶段耗时、PID 绑定或命令级计时收据。C6-prime 顶层收据亦无这些字段。逐文件哈希、检索表达式和字段分类在机器收据中。

| 候选信息 | 证据分类 | 对耗时的意义 |
|---|---|---|
| 三根封存清单、读回、terminal 和 attempted-call ledger | 有效的**产物与调用**身份；非计时载体 | 证明哪些调用和文件被接受，不能推出耗时 |
| turn7/turn8 报告的单次命令与退出码 `0` | 有效的进程结果；没有对应起止钟点或 monotonic 区间 | 不能计算该命令耗时 |
| 文件系统创建/修改时间、Git 提交时间、Codex/Work 会话时长 | `NON_AUTHORITATIVE_FOR_MODEL_RUNTIME` | 可含前检、写盘、人工交接或事后提交；不绑定精确科学尝试、同一时钟和边界，不能转成模型秒数 |
| 封存根内可校验的 monotonic 起止、CPU/GPU 时间、进程/PID 或阶段耗时 | `ABSENT` | 没有可做差、求和或归因的数值 |

**判定：`MEASURED_SCIENCE_RUNTIME_UNAVAILABLE`。** C7 与 C8 各自的实测 science wall/CPU/GPU 秒数、两轮合计实际值、可信下界和上界均为 `UNAVAILABLE`。缺少同一科学尝试入口与退出的计时字段、时钟来源、PID/执行 ID 绑定、失败/停顿覆盖说明及同类机器环境证据。不能用文件或 Git 时间戳、输出文件大小或会话长度填补这些缺口，也不能推出批处理加速比、科学达标概率或一个硬 `T_owner`。

## 调用成本和有限资源决策

科学调用数与时间是不同量。独立接受的 C7/C8 各有 31/31 HJB/KFE、一次集成、零重试；两轮实际合计为 62 原生初始化、49,600 次 labor-root 尝试、818 次 policy map/D2、654,400 次 selector evaluation、282,254 次 selector-root 调用、756 次 HJB update、62 次 terminal KFE、两次集成、62 次 firm。每轮的 selector roots 为 141,129/141,125，其余示例数见机器收据中的完整逐类表。过去两轮的额度已耗尽。被独立接受的 rolling 规格把旧单轮**上限**复制成未来最多两轮的提案，例如两轮候选上限 3,100 次 direct HJB update、62 次 terminal KFE、两次集成；它们既不是历史实际量，也不是获批的新预算，更不能推算运行秒数或未来期望成本。旧 10/20-turn 例子依然只是比较交接次数与风险的示意。

在没有实测耗时的情况下，Owner 有两个可区分的后续选择，均须另行决定，当前不执行：

1. **独立资源容忍度**：Owner 依据可使用的机器占用/日程，明确给定有限的进程级 monotonic wall 上限 `T_owner`，并分别决定是否还要 CPU/GPU 时间或货币上限。此上限控制最多愿意投入的资源，**不保证**完成 C9/C10、数值通过或得到可比科学结果；当前没有任何秒数可代填。若需要真正的硬墙钟上界，单靠调用前检查不够，还须外部监护进程在截止时终止长时间未返回的单个科学操作，并把未落盘账本标为 `CALL_LEDGER_UNRESOLVED`。CPU/GPU 硬上界也需可验证的监测与强制停止机制；调用次数上限不能替代它。
2. **另行授权的计时测量**：Owner/Work 可另发精确、有限、独立审查的 instrumented 科学任务，在已授权的一次未来科学尝试中记录执行 ID/PID、单调起止、wall 与 CPU/GPU 定义、逐省/阶段区间、暂停/失败计入方式、环境及完整调用账本。该测量本身消耗新的科学预算，不能在本任务偷偷重跑 C7/C8；单次测量也不保证未来两轮耗时相同。取得并独立接受的计时证据之后，再由 Owner 选硬上限，而不是由 Codex 代定。

未来 runner 若获单独授权，应在**每个科学入口之前**与省份、HJB/KFE、集成、封存/读回等阶段之间用同一 monotonic deadline 检查剩余时间，同时执行每省/每轮/累计 attempted-call 上限。若时间到达且已有完整原子封存并读回的检查点，只保留该检查点作为可信进度；若发生在 turn 中，记 `FAIL__OUTER_INCOMPLETE_CHECKPOINT__TIMEOUT`，保留最早原始失败位置、已持久化尝试账本和未完成现场，不形成合法比较。监护进程强制终止时若账本可能尚未落盘，显式记 `CALL_LEDGER_UNRESOLVED`；不得据部分日志称剩余额度未用。首败即停、失败尝试计数、零重试、零恢复、无预算借用仍有效。任何恢复或补跑需要新任务与授权。

本任务的首个证据阻断是缺少可信科学运行时间，**不是**源身份或清单损坏；它只阻止证据推导的时间上限，不阻止交付零科学审计。静态核对通过后，下一门为 GPT Work 独立 ACCEPT/REJECT，再由 Owner 决定资源容忍度或是否授权新的 instrumented 测量。新调用预算、runner、turn9、K2、GE 与 Results 均仍关闭。科学/模型调用、失败尝试、重试全为 `0`；Results eligibility `FALSE`。
