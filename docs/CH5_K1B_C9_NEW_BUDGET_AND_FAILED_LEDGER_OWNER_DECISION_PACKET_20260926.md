# C9 失败后的新预算与账本处置：Owner 决策包

状态：`DECISION_PACKET_ONLY__NO_NEW_C9_AUTHORITY`。零科学设计 `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ZERO_SCIENCE_DESIGN_20260926.md` 已获独立 **ACCEPT（仅决策证据）**。旧 `C9_TIMED_RISK_RUN001` 消耗了一次 C9 household 额度，省 0 terminal KFE 也达到旧逐省上限；最终账本为 `CALL_LEDGER_UNRESOLVED`。旧执行 ID 和输出根不能复用。C10 与 Results 均关闭。

## 待决定事项

**推荐 A：允许制定另一套新 C9 尝试的零科学预算与旧失败扣账政策提案。** 下一任务只提出逐类别、逐省、单轮及与未来 C10 累计的明确额度与保守账本处置，说明新旧预算命名空间如何并列记录和如何防止漏计。它还需检视新 ID/独占根及 runner/合同重绑范围，并经 GPT Work 独立审查。此决定**不采纳额度、不改 live 合同、不运行 C9**；提案验收后仍须 Owner 分别决定新预算与一次性科学执行。

**B：暂不继续新 C9。** 保留已封存的失败输出和 `CALL_LEDGER_UNRESOLVED`，不再准备新预算或执行身份链。

若选 A，需要承认旧窗口没有可直接支取的 C9 household 或省 0 KFE 额度；不能将 source 观察数、guard 确认数和预留暴露相加成“核清余额”，也不能把旧失败视为免费重试。新预算额度及对旧失败的精确/保守处理仍是下一份提案中的**待采纳科学决定**。现有 36,000 秒协作墙不是完成时间上界，未来若沿用也须为新尝试单独绑定。Results eligibility 始终为 `FALSE`。
