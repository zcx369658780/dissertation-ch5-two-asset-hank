# C9 新预算及旧失败扣账：Owner 决策包

状态：`OWNER_DECISION_REQUIRED__NO_SCIENCE`。零科学提案 `0b3e401837c647d49cf40b76dc92dd96d08a873c` 已获 GPT Work 独立 **ACCEPT（仅决策证据）**。旧 `C9_TIMED_RISK_RUN001` 已消耗，最终真实调用账本仍为 `CALL_LEDGER_UNRESOLVED`；不能从旧额度直接再开完整 C9。Results eligibility 为 `FALSE`。

**推荐整体采纳以下治理方案，仅授权后续零科学身份链准备，不授权运行：**

1. 为新 ID `C9_POST_FAILURE_NEW_ATTEMPT_001` 与尚不存在的独占根 `reports/ch5_k1b_turn9_post_failure_new_attempt_001` 设立额外命名空间 `C8_START_C9_POST_FAILURE_NEW_ATTEMPT_001_C10_PROSPECTIVE`。新 C9 逐类 39 项、逐省 5 项及新 C9 加未来 C10 累计 39 项上限，逐键采用 `proposed_budget.json` 的精确数值，三张表规范 SHA-256 分别为 `F76B958C8D57CEAD22B61A497FCCFBF45143E1DC2AA07CCC656EBA6252464C20`、`FDA5A76D45B639FD0B793E6270D051255CCFC0F85E7E982A152A4AA7743D7028`、`3E2DF35B6D867A0680E1ABBBB778205982F1845139D775A63A9D4672B7D6CA3A`。C10 额度只是未来累计上限，不授予 C10 执行权。
2. 对旧失败按**完整旧 C9 turn 上限作行政治理扣账**，冻结旧窗口并关闭其 C10 机会；保留 guard/source/预留三层原始证据和真实调用 `UNRESOLVED`，不得将治理扣账记作实际调用。这样无需猜测失败现场余额，也明确新增科学风险暴露。
3. 采纳机器文件中逐键列示的项目生命周期**治理上界**：旧完整 C9 turn 扣账加新 C9/C10 累计上限。它提高治理总量，不声称已发生调用。新窗口执行时每入口先扣尝试、逐类逐省及累计同时约束、首失败即停、零重试，不能跨窗口借额。
4. 为**新 C9 一次性尝试**单独采纳 36,000 秒单调进程协作墙：到限后阻止下一科学入口；在途调用可越限且可跨北京时间 00:00，手动中断后账本不明即停。它不是可信完成时长上界，也不开放 C10。

上述四项必须由 Owner 明确决定；若不同意任一项，请指出替代的逐键上限、旧失败治理处理或资源规则。采纳仅允许 GPT Work 后续派发**零科学**的新 runner/delegate、合同和身份链准备任务，仍须独立静态审查、单独一次性 Owner 执行授权及最终身份复核，才能考虑新 C9。完整封存且读回通过的新 C9 才可能进入 C8→C9 数值比较；旧部分 C9 不计。

精确提案与逐键表：`docs/CH5_K1B_C9_NEW_BUDGET_FAILED_LEDGER_POLICY_ZERO_SCIENCE_PROPOSAL_20260926.md` 和 `EVIDENCE/ch5_k1b_c9_new_budget_failed_ledger_policy_zero_science_proposal_20260926/proposed_budget.json`（原始 SHA-256 `66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460`）。
