# C8 同冻结输入测时 runner：提交后一次静态核验

任务 `CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_POSTCOMMIT_STATIC_VERIFICATION_20260925`，派发 HEAD `db25734d55a9aa6cf15035c5554949f8a3a50134`，父提交 `45ba72ea611af9a72fb23f33b4f3cf8b5b13b2cf`，派发树 `1d5c2650f4478b7127bca5865e779b2254404c2f`。这是对已提交、未修改的旧候选进行**新的、仅一次**静态核验；不追认旧任务两次测试为 PASS。GPT Work 对原候选的 `REJECT` 仍是当前独立审查记录，待本证据再审。[1]

## 入口与产物身份

HEAD 是候选 `45ba72ea611af9a72fb23f33b4f3cf8b5b13b2cf` 的已提交后代。runner/test 在当前 HEAD 与该候选中的 Git blob 分别相同：

| 路径 | Git blob | 工作树 SHA-256 |
|---|---|---|
| `validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py` | `2af59b24296579a67a3e16fcb5c53d65ed67ba64` | `29FDB9D7E4CF4AAB7BEBA1029AF8D8EDE2EE5D3923F2FFF9062C6AAD46AD474B` |
| `tests/test_mp4c_k1b_turn8_same_frozen_timing_measurement_preflight.py` | `0c8fcb553b65f7076b293c6bc470f0018737e157` | `34C425D7BAB14C626E6C34F83070851E1795B1F67D8726E5999CD7AB9416393C` |

`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`；入口及测试后均无跟踪文件改动。唯一未跟踪输出根仍为受保护 C6-prime、C7、C8，其 `execution_artifact_manifest.json` SHA-256 依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`，入口与测试后相同。候选测量输出根 `reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/` 始终不存在。已读取原候选的独立 `REJECT`。[1]

## 唯一一次核验

执行且只执行：

`python -B -m pytest -q -p no:cacheprovider tests/test_mp4c_k1b_turn8_same_frozen_timing_measurement_preflight.py`

命令退出码 `0`；标准结果为 `12 passed in 6.86s`，失败 `0`、跳过 `0`。这给出**本次提交后静态验证 PASS**，不建立 runner 独立 ACCEPT、未来执行任务有效性、过程级科学耗时或 C9/C10 上界。没有运行 `--execute`、HJB/KFE、集成、firm、K1B 分配或任何科学/模型调用；失败尝试、重试均为 `0`。

## 下一门

本任务只提交报告和机器收据供 GPT Work 独立 `ACCEPT/REJECT`。即使本次静态 PASS，Owner 尚未采纳独立 C8 测量预算/资源合同、执行 ID 或一次性科学许可；测量根仍未创建。`BLOCKED__DURATION_BOUND_UNAVAILABLE`、Results eligibility `FALSE` 保持。原候选的 REJECT 只能由新的独立裁决处理，不由 Builder 自行撤销。

[1] `docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_PREPARATION_INDEPENDENT_REVIEW_20260925.md`；任务约束见 `TASK_CURRENT.md`。来源与报告 SHA-256、零调用账本见同任务机器收据。
