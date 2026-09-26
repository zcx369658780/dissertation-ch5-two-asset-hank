# C9 一次性失败后的 Owner 决策包

状态：`DECISION_EVIDENCE_ONLY__NO_NEW_SCIENCE_AUTHORITY`。2026-09-26 获准的 `C9_TIMED_RISK_RUN001` 已且仅已执行一次，省 0 后因 wrapper/delegate 的 `reconcile` 参数不匹配退出。最终终态为 `CALL_LEDGER_UNRESOLVED`；完整外层 turn、九分量比较和安全暂停均不存在。部分文件清单 298 项读回通过，只证明现存文件保存完整。C10 与 Results 均未开放。

## 已完成的零科学处理

- 失败证据和五个未跟踪输出根均原样保留；独立审查见 `docs/CH5_K1B_C9_ONE_SHOT_EXECUTION_INDEPENDENT_REVIEW_20260926.md`。
- 根因诊断已独立 ACCEPT；仅将 `MeasuredGuard.reconcile` 补上可选 `province` 参数并转发的工程修复也已独立 ACCEPT，候选 wrapper 原始 SHA-256 为 `59A63E933BF13A4FC39EC583227B2E9724B5E06B510A1896CB1307DBCC8F1D06`。定向惰性回归 `1 passed`；没有新科学调用。
- runner 识别的静态审查已更新并提交，原始 SHA-256 为 `4A42989DFCA0AF8A58CE529D094C4066AC3D5C4BB3CAE143201343BCF0B464D5`。live 合同仍绑定旧 wrapper/旧审查哈希，因而不匹配修复候选。

## 新尝试前必须解决的三项身份与账本问题

1. `C9_TIMED_RISK_RUN001` 的一次性授权和预算已消耗；旧 C9 输出根现在存在，不得删除、覆盖或视为可恢复检查点。
2. 旧 live 合同和 runner 固定旧执行 ID、旧输出根及旧审查身份。只替换两个 SHA-256 不能使旧尝试重新合法；任何未来尝试需独占新 ID/根和整条新提交身份链。
3. 省 0 的 wrapper 最终账本为 `CALL_LEDGER_UNRESOLVED`。来源账本中的局部计数与 guard 确认数不能拼成已核清余额。未来预算如何对待这次已发生且不明的尝试，必须明确；不能把未核清项当作零消耗或免费重试。

## 推荐决定

**先授权零科学的新尝试设计与预算处置提案，不授权运行。** 让现有 Codex 会话在唯一工作树内提出新执行 ID/独占输出根、失败尝试的保守账本处理、预算边界、runner/合同重绑范围及静态验证方案；GPT Work 独立审查后，再由 Owner 决定是否采纳新的预算和是否另行授权一次科学执行。该路线可把新增科学风险与成本在运行前说明清楚，也保留当前失败的原始证据。

若暂不继续，保持 `CALL_LEDGER_UNRESOLVED`、C9 新尝试关闭、C10 关闭和 Results eligibility `FALSE`。以上任一选择都不授权现在运行 C9 第二次或 C10。
