# C8 同冻结输入测时 runner Repair1：零科学候选

任务 `CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_REPAIR1_ZERO_SCIENCE_20260925`；入口 HEAD `076f5202e1c49d849a5c0da6bab93b4e6235891a` 是指定基线 `861789ed1dadedc40448443744309c43df63eba3` 的已提交后代，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。入口无跟踪文件改动，只有受保护 C6-prime/C7/C8 三个未跟踪输出根，清单哈希与交接文件相符；测量候选根始终不存在。GPT Work 对提交后静态测试证据给了独立 ACCEPT，但旧 runner 仍因两项代码缺陷 REJECT；本候选等待新的独立裁决。[1]

## 精确修复

1. **未来执行门绑定独立审查版本。** `future_gate` 现在取得新测量 wrapper 的**已提交工作树 SHA-256**，并要求后续独立 GPT Work 审查文档 `docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_REPAIR1_INDEPENDENT_REVIEW_20260925.md` 已单独提交、含明确 `ACCEPT__C8_SAME_FROZEN_TIMING_WRAPPER`、GPT Work 审查者、wrapper 路径与相同 SHA-256。未来当前任务单及其已提交副本、Owner 测量采纳文档、结构化测量合同必须逐一绑定该 wrapper SHA 与审查文档 SHA。任一文档缺失、未提交、脏、哈希不符或 verdict 非 ACCEPT，均在输出创建和科学调用前拒绝。已接受 C8 delegate 原有哈希门仍为 `10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831`，未放宽。[1]
2. **保留原 C8 数值终态。** 删除对 `c8.turn8_terminal` 的临时覆盖。重用的已接受 C8 runner 自行决定并封存其原始数值终态，`record["source_terminal"]` 与返回值保持相同；`COMPLETE_OBSERVED_ELAPSED_SAMPLE_ONLY` 仅留在未来计时收据的独立 `classification` 字段，不替代数值终态。原有失败和首错处理、独立测量预算命名空间及输出所有权检查不变。[1]

测试只使用惰性替身：模拟缺失/过期独立审查、任务单/Owner/合同中 wrapper 哈希不一致、当前编辑阶段的预提交身份拒绝、默认零科学入口和原数值终态保留。当前独立审查文档尚不存在，因此未来 `--execute` 门仍会 fail closed。本任务既不创建该文档，也不采纳测量预算或执行测量。

## 检查与边界

指定命令 `python -B -m pytest -q -p no:cacheprovider tests/test_mp4c_k1b_turn8_same_frozen_timing_measurement_preflight.py` 执行 **1/2 次**，退出码 `0`，结果 `14 passed in 6.63s`，失败 `0`、跳过 `0`；没有第二次测试。JSON、逐源/受保护清单/候选路径 SHA-256、四路径 diff 与 `git diff --check` 见收据。没有 `--execute`、模型导入/调用、HJB/KFE、集成、firm、K1B 分配或输出根创建；本任务科学/模型调用、失败尝试和重试均为 `0`。

下一门仅是 GPT Work 对这次四路径候选的独立 `ACCEPT/REJECT`。即使接受，未来独立测量预算、资源合同、精确 ID、审查文档及一次性科学授权仍须另外完成。`BLOCKED__DURATION_BOUND_UNAVAILABLE`、Results eligibility `FALSE` 保持。

[1] `docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_POSTCOMMIT_STATIC_VERIFICATION_INDEPENDENT_REVIEW_20260925.md`；任务边界见 `TASK_CURRENT.md`；受保护根身份见 `docs/CH5_K1B_CODEX_SESSION_HANDOFF_20260925.md`。逐项哈希见同任务机器收据。
