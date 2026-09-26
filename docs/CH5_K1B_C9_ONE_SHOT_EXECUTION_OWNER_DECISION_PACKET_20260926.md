# C9 一次性执行：Owner 最终决策包

状态：`DECISION_PACKET_ONLY__NO_EXECUTION_AUTHORITY`。截至本包编制时，C9 科学调用为零，预定输出根不存在；live 合同通过的是**静态身份**审查，执行任务门仍关闭。本包及此前的提案采纳都不等于“现在运行 C9 一次”。Results eligibility 为 `FALSE`。

## 已冻结的单次 C9 范围

- 已提交 live 合同原始 SHA-256：`65992776BFBED510F5C59DBC14B8CBE0B65DCCBAD08C5E0559491303D5A5B466`；执行 ID：`C9_TIMED_RISK_RUN001`；唯一预定输出根：`reports/ch5_k1b_turn9_timed_risk_exception_run001`。
- 最终静态 runner 审查 `docs/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_RUNNER_INDEPENDENT_REVIEW.md` 原始 SHA-256：`EA21124F8E01470D2D03DE1FB6B496CCA7EDDC584EF7270796EB01DD08C94354`，verdict：`ACCEPT__C9_TIMED_RISK_EXCEPTION_RUNNER`。wrapper `validators/multi_province/k1b_turn9_timed_risk_exception/run.py` 原始 SHA-256：`0E43522B64F7BD34C46C92A967F41FBDD373C3DD15DCC188821CB0EDB3AB368B`；delegate `validators/multi_province/k1b_turn9_outer_r2/run.py` 原始 SHA-256：`A4B4985DAE8C15E5F21125A0A82FCE39D1B08D975929250186D941D691C4E7BB`。
- 冻结的 C8 entering-C9 身份（依次为 manifest、readback、输入 JSON、计划 NPZ）：`40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65`、`E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85`、`FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB`、`E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD`；均已按对应文件字节读回。
- 合同绑定 39 类 C9 尝试上限、5 类逐省上限和 39 类 C9+C10 累计上限。按 UTF-8、键排序、无空格 JSON 计算的三个预算对象 SHA-256 依次为 `F76B958C8D57CEAD22B61A497FCCFBF45143E1DC2AA07CCC656EBA6252464C20`、`FDA5A76D45B639FD0B793E6270D051255CCFC0F85E7E982A152A4AA7743D7028`、`3E2DF35B6D867A0680E1ABBBB778205982F1845139D775A63A9D4672B7D6CA3A`；全部数值以该原始哈希绑定的 live 合同为准。逐省五项上限为 policy maps `51`、selector evaluations `40,800`、scalar selector roots `20,000,000`、direct HJB updates `50`、terminal KFE attempts `1`。C9 的 `turn9_household_calls=1`、`turn10_household_calls=0`；两轮累计的 `turn10_household_calls=1` 不授予本次 C10 调用。
- C9 **最多一次尝试、重试零次**。C9-only 资源墙为自未来 wrapper 尝试开始计的单调时钟 `36,000` 秒，协作式阻止到期后的下一次科学入口；没有自动 C10 授权。

## Owner 决策前须知

36,000 秒是资源上限，**不是** C9 完成时长上界。跨本地午夜不自动停止在途调用；只要进程仍运行，它可能在下一个安全点前超过墙钟或计划关机时刻。手动中断可能留下 `CALL_LEDGER_UNRESOLVED`，已尝试调用和失败尝试消耗预算，不产生免费重试或部分续跑权。只有完整 C9 outer turn 的输出全部封存并读回后，才可能形成安全跨天暂停；C10 仍需另行授权。

**下一项独立 Owner 决策（尚未作出）：是否明确授权“现在运行 C9 一次”？** 若 Owner 暂不授权，保持执行任务门关闭。若将来明确授权，须先另行形成并提交 runner 识别的执行 Owner 采纳文件及与 `TASK_CURRENT.md` 逐字节一致的一次性任务，再由独立审查复核最终已提交身份链：任务/采纳/合同/runner 审查/wrapper/delegate、冻结输入、预算、输出根不存在和零重试。只有该最终门通过，才可讨论一次性 dispatch。本决策包不创建这些文件，也不触发执行。
