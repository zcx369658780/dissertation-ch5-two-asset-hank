# C9 一次性执行任务草案

**`DRAFT_ONLY__NOT_AN_AUTHORITY`**。本文件仅供 Owner 与独立审查预览；它不是 `TASK_CURRENT.md`，不是 runner 识别的 `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_EXECUTION.md`，也不是执行 Owner 采纳。当前零科学任务保持有效，C9 执行未获授权。

下列为未来任务必须精确绑定的字段形状，**不是当前任务状态**：

```text
Task ID: `CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_EXECUTION`
Status: `ACTIVE__ONE_SHOT_C9_TIMED_RISK_EXCEPTION`
Execution authorization ID: `C9_TIMED_RISK_RUN001`
Authorized output root: `reports/ch5_k1b_turn9_timed_risk_exception_run001`
Owner adoption SHA-256: `PENDING`
C9 contract SHA-256: `65992776BFBED510F5C59DBC14B8CBE0B65DCCBAD08C5E0559491303D5A5B466`
Independent review SHA-256: `EA21124F8E01470D2D03DE1FB6B496CCA7EDDC584EF7270796EB01DD08C94354`
Wrapper SHA-256: `0E43522B64F7BD34C46C92A967F41FBDD373C3DD15DCC188821CB0EDB3AB368B`
Delegate SHA-256: `A4B4985DAE8C15E5F21125A0A82FCE39D1B08D975929250186D941D691C4E7BB`
```

`Owner adoption SHA-256` 必须在 Owner 另行明确决定“现在运行 C9 一次”且未来执行采纳文件真实存在、已提交后再计算，当前为 `PENDING`。未来 one-shot 任务与 `TASK_CURRENT.md` 的逐字节/已提交身份为 `PENDING`；最终独立身份链审查为 `PENDING`。不得把本草案复制到 runner 识别路径来跳过这些门。

未来最终核验还须确认：live 合同仍精确绑定上述身份、C8 entering-C9 四项哈希及 39 类/5 类逐省/两轮预算不变；C9-only 协作墙为 `36,000` 秒、最多一次尝试、重试零次；C9 输出根尚不存在；C10 不自动授权。墙钟到期只阻止下一次入口，在途调用可能越过午夜或资源墙；手动中断可能使账本 `CALL_LEDGER_UNRESOLVED`，不得视为免费重试。Results eligibility 仍为 `FALSE`。
