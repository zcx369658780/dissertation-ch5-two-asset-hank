# C8 同冻结输入测时 runner：零科学准备候选

任务 `CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_ZERO_SCIENCE_PREPARATION_20260925`；入口 HEAD `bba8d44d01c4ab9768593fa95e7917bc50f05874` 为指定基线 `d1ab05a7880516d6ac3c20d5a22c84502c64f8a8` 的已提交后代，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。入口无跟踪文件改动，受保护 C6-prime、C7、C8 是仅有的三个未跟踪输出根，三份完整清单 SHA-256 与交接记录一致；候选测量根 `reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/` 不存在。本候选未创建该根，也未运行 `--execute`。Results eligibility `FALSE`。

## 设计与权威边界

Owner 选择**独立预算、一次 C8 同冻结输入测时**路线，只允许本次零科学仪器准备；该路线的测量调用额度、资源合同、执行 ID 和输出根仍需另行采纳及一次性授权。既有 C9/C10 调用上限属于另一账本，不能供此测量使用。`BLOCKED__DURATION_BOUND_UNAVAILABLE` 仍阻止 C9/C10。[1–4]

新 `validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py` 默认入口及模块导入不运行模型。静态前检绑定冻结 `src`、C7 完整清单、进入 C8 束清单和读回、已接受 C8 runner 的精确哈希；本工作树没有可用代码图谱，因此按这些明确路径只读核对。[5–7] 未来 `execute_once` 在任何输出创建前要求已提交且完全一致的 `TASK_CURRENT.md`/任务副本、执行 ID、Owner 独立测量采纳文档及带其 SHA-256 的结构化合同、单次独立预算与协作式进程资源额度，并复核 C7 进入束及输出根缺席。现行任务单不满足该门。

未来科学路径在内存中委托**未改动的已接受 C8 runner**，只重定向到全新测量根、独立测量账本及未来测量任务绑定；不修改经济、HJB/KFE、网格、求解器或受保护 C8 根。独立合同的每类/每省额度必须与候选表同键、为非负整数且不超过候选最大值；`budget_namespace=SEPARATE_C8_TIMING_ONLY`，不读取或扣减 C9/C10 窗口。受保护 C8 runner 与冻结 `src` 的工作树文件保持不变。已接受 runner 本身仍执行完整 31 省及一次集成，沿用既有输入/输出身份与首次失败处理。[5–7]

测时以同机单调时钟记录进入一次完整外层科学尝试前到科学输出清单独立读回后的总区间；另记录 UTC/Asia-Shanghai 映射、household、省、integration、seal/readback 区间、进程 PID/命令及运行环境。工程用时钟一致性检查拒绝单调倒退、墙钟倒退或超过 2 秒的二者差异；它不是科学容差或 C9/C10 时长上界。资源秒数由**未来 Owner 合同**给定，runner 仅在可控入口做协作式检查，长调用可能越过额度；不得称此机制为强制硬墙钟停止。输出清单排除后写入的计时收据；总测时终点是科学输出的完整清单及读回，随后写入的收据需另行独立审查。

进入科学类别前写独占尝试日志，省级最多额度先保留、成功后与源账本核对；失败尝试仍计账，省内突发中断如不能精确确定嵌套调用，标 `CALL_LEDGER_UNRESOLVED`。原始失败位置单独保存；手动中断不得重试或把省级/HJB 中途产物称为完整 turn。即便将来成功测得完整样本，也只标 `COMPLETE_OBSERVED_ELAPSED_SAMPLE_ONLY`，`c9_c10_upper_duration_bound=null`，不清除 C9/C10 午夜预启动阻断。[1–4]

## 静态测试终态与首缺陷

仅执行了任务单指定测试文件两次，均使用 `python -B -m pytest -q -p no:cacheprovider`，没有执行测量 runner 的 `--execute`。

| 次数 | 结果 | 最早缺陷 |
|---|---|---|
| 1/2 | `11 passed, 1 failed` | 模拟未来任务单的静态测试替身用 `dict.get(key, read_text(...))`，默认参数被提前求值，导致临时 `TASK_CURRENT.md` 的 `FileNotFoundError`。这是测试替身缺陷，未到科学路径。 |
| 2/2 | `11 passed, 1 failed` | 修正替身后，`test_current_task_and_wrong_execution_id_refuse_before_output` 预期 `BLOCKED__FRESH_MEASUREMENT_TASK_GATE`，实际先返回 `BLOCKED__MEASUREMENT_AUTHORITY_DIRTY_OR_MISSING`：准备中的新 runner 尚未提交，而新身份门按设计先核对其已提交状态。 |

第二次未通过后按任务单停止测试，不再重跑或扩大测试范围。**当前候选不能报告静态测试 PASS，也不能请求科学执行。**第一次测试缺陷及第二次首个身份拒绝均保留在机器收据。未来独立 GPT Work 应先对这一身份门与测试期望作 `ACCEPT/REJECT` 裁决；若要求修正，须发精确修复任务，并重新限定测试预算。所有测试都未建立测量时长或上界。

## 后续门

本次只提交四个允许路径供 GPT Work 独立 `ACCEPT/REJECT`；包含未通过的静态测试事实。Owner 仍需独立采纳单次测量专用的逐类/逐省调用上限、进程资源/超限语义、唯一执行 ID 和输出根；新的实施候选需独立复核，再有单独一次性科学许可。C8 同冻结输入的一次耗时样本也不自动给出 C9/C10 的可信上界或启动权。科学/模型调用、失败尝试和重试均为 `0`，`MEASURED_SCIENCE_RUNTIME_UNAVAILABLE`、`BLOCKED__DURATION_BOUND_UNAVAILABLE`、Results eligibility `FALSE` 保持。

## 来源

[1] `docs/CH5_K1B_SEPARATE_C8_FROZEN_INPUT_TIMING_ROUTE_OWNER_SELECTION_20260925.md`；[2] `docs/CH5_K1B_PROCESS_BOUND_TIMING_ACQUISITION_ZERO_SCIENCE_DESIGN_20260925.md` 及独立审查；[3] `docs/CH5_K1B_PROCESS_BOUND_TIMING_EVIDENCE_OWNER_DECISION_20260925.md`；[4] `docs/CH5_K1B_C9_C10_CALL_CEILINGS_OWNER_ADOPTION_20260925.md`；[5] `validators/multi_province/k1b_turn8_outer_r2/run.py` 与原测试 `tests/test_mp4c_k1b_turn8_outer_r2_preflight.py` 及接受审查；[6] C7 根的 `turn8_entering_bundle_manifest.json`、`turn8_entering_bundle_readback.json`；[7] `AGENTS.md`、`CURRENT.md`、`SCIENTIFIC_DECISIONS.md`、`REVIEW_GATE.md`、`TASK_CURRENT.md`。上述来源与四个候选路径的哈希见机器收据。
