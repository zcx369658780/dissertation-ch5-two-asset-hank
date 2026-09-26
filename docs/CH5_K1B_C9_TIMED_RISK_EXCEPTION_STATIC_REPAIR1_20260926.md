# C9 计时风险例外静态 Repair1

状态：`BUILDER_REPAIR1_CANDIDATE__AWAITING_INDEPENDENT_GPT_WORK_ACCEPT_REJECT`。仅零科学修复 `REJECT__ACTIVE_GATE_AND_LEDGER_DEFECTS__ZERO_SCIENCE_REPAIR_ONLY` 的四项问题；没有运行 household、KFE、integration 或 C9/C10。Results eligibility 仍为 `FALSE`。

## 入口与只读边界

- 唯一工作树 `D:\ProjectTemp\c5k1bturn56`；入口 HEAD `62636398b764487221f21f74b9c9882b825e47ba`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。`TASK_CURRENT.md` 与归档 Repair1 任务均已提交且逐字节相同，SHA-256 `0E4F6376D32470C9A25E4D4BC276BE8AC7F280D6B142469C003AAE9FDF666F6B`。入口跟踪文件干净，只有四份受保护未跟踪根。
- 独立 REJECT 文档 SHA-256 `D9E1E0D90C8AD61B19EB593AAF5C6C1734E8310BF788E00B13F210345B8D9752`。只读 inactive 合同 SHA-256 `DED122DDE12E86D579B80C1FC4E268D3953A6A79009E713F3A05FE1FA272B91A`；`active=false`、`attempts=0`、`execution_id=null`、`resource_wall_seconds=null`。
- C6-prime/C7/C8/C8-timing 保护清单 SHA-256 依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`。C9 预定输出根及坏链接不存在。

## 四项修复

1. `run_timed_action()` 和 `_instrumented_action()` 在接触输出前重新执行完整 `future_gate()`；delegate 的 `run_after_valid_gate()` 与 `_execute_after_gate()` 也独立重查已提交的一次性任务、Owner 采纳、GPT Work 审查、合同和身份。生产 `run_timed_action()` 不再接受任意 action 参数；测试只在内存中替换私有 action 函数。调用方构造的 active-looking gate 在当前 inactive 合同下先被拒绝。
2. `BudgetGuard` 在逐省入口保存来源累计基线，将每次 map 返回的 selector evaluations / scalar selector roots 实际增量投影到该省，返回时及省结束时与来源账本协调。相同累计读数取最大值而不重复加账；逐省上限独立于 31 省总上限。journal 留存每省基线、预留暴露量和实际读数；暂停收据保留逐省已尝试及余额。
3. 拥有输出根的失败路径先对**当时已有的文件**生成 `partial_artifact_manifest.json` 和 `partial_artifact_readback.json`，再写 `timing_failure.json`，记录最早原始终态、已确认尝试、预留暴露量、读回结果和 `retry_allowed=false`。部分文件不构成完整 C9 或安全暂停；账本/读回不确定时终态为 `CALL_LEDGER_UNRESOLVED`。成功路径把 `pause_receipt.json` 放在最后写入，避免后续失败留下已宣称的安全暂停。
4. 进入 `_solve_province` 前分别记录 bounded envelope 和已确认计数；若源函数内部中断，即使可读出部分来源计数，也标记 `CALL_LEDGER_UNRESOLVED`，保存最早错误和确认数，不把预留最大值当成已调用数，不推断可重试余额。

## 静态验证与剩余门

- `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/test_mp4c_k1b_turn9_outer_r2_preflight.py tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py`：`18 passed`。覆盖伪造 gate、两类逐省实际值及超额、重复 map 读数、省内中断、内存 fake 输出文件清单/读回、失败终态及成功暂停写入顺序。修复中旧测试对新 inactive 状态的预期曾失败，更新后复测通过；没有科学调用。
- 默认 CLI 退出码 `0`，静态状态为 `BLOCKED__INACTIVE_CONTRACT__DELEGATE_REBIND_REQUIRED`；带 `--execute --execution-id INERT_TEST` 退出码 `1`，终态 `BLOCKED__INACTIVE_CONTRACT`。两者均未创建 C9 根。
- 仅修改任务允许的四个源码/测试文件，仅新增本报告和机器收据；具体提交、树和 blob 以交接及收据为准。`git diff --check` 和最终受保护哈希将在提交前复核。

本任务禁止改 inactive 合同，因此其中 `delegate_sha256=54D8E39684CD659B4208D120551A47D03FE28E59EB23C2C5DCFD8766A6FFADF3` 保留为被 REJECT 候选的旧值；修复后的 delegate SHA-256 为 `D88616CFBA2F07398A6375A1C055D9B7A3ACADD74987DD0C72677F1369E4F70A`。静态入口明确报告**待重新绑定**，future active 路径仍严格要求合同哈希匹配。只有 GPT Work 独立 ACCEPT/REJECT 后，另行 Owner 选择资源墙并采纳 active 合同、重绑这些身份，才可能讨论一次性 C9 执行。当前正常时长门仍为 `BLOCKED__DURATION_BOUND_UNAVAILABLE`，C10 不获自动授权。真实科学执行和不可捕获的进程强制终止未在本零科学任务中验证。
