# C9 新预算与旧失败扣账：零科学提案（2026-09-26）

**状态：`PROPOSED_ONLY`，待 GPT Work 独立 ACCEPT/REJECT。** Owner 选择了制定提案，尚未采纳额度或授权执行。`C9_TIMED_RISK_RUN001` 已消耗；旧输出根受保护，最终账本为 `CALL_LEDGER_UNRESOLVED`。本提案不把它改称免费重试或可恢复的部分 turn。C10 和 Results 仍关闭，Results eligibility 为 `FALSE`。

## 建议的新增预算与精确数值

建议仅在 Owner **另行明确采纳**后，设立新命名空间 `C8_START_C9_POST_FAILURE_NEW_ATTEMPT_001_C10_PROSPECTIVE`，候选执行 ID 为 `C9_POST_FAILURE_NEW_ATTEMPT_001`、候选独占根为 `reports/ch5_k1b_turn9_post_failure_new_attempt_001`（本任务核验不存在，未创建）。它是额外授予的一次新尝试预算，不能从旧 `C8_START_C9_C10_WINDOW` 扣出“剩余额度”；旧 ID、旧合同、旧根均不可复用。

完整 39 类 C9 每类别、5 项逐省和 39 类 C9 加未来 C10 累计的**逐键数值**在 `EVIDENCE/ch5_k1b_c9_new_budget_failed_ledger_policy_zero_science_proposal_20260926/proposed_budget.json`。三张表逐键等于旧合同 `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_INACTIVE_CONTRACT.json` 中已采纳的上限：分别以旧 `per_category_attempt_ceiling`、`per_province_attempt_ceiling`、`c9_c10_cumulative_ceiling` 为候选模板；未上调任何单次或逐省上限，也保留零许可类别及冻结 K1B allocation/feedback 单事件别名。理由仅是拟从同一封存 C8 输入运行结构相同的一轮 C9，并保留未来 C10 的原有限上限；这不证明运行时长、成功率或旧失败实际调用已核清。若未来科学实现或输入身份改变，须重新论证这些数值，不能沿用本模板。

三张**单独映射**采用 UTF-8、键排序、无空格紧凑 JSON（Python `sort_keys=True, separators=(',', ':'), ensure_ascii=False`）计算的 SHA-256 依次为：

| 提议映射 | 键数 | 规范 SHA-256 | 与旧已采纳表 |
| --- | ---: | --- | --- |
| C9 每类别最大尝试 | 39 | `F76B958C8D57CEAD22B61A497FCCFBF45143E1DC2AA07CCC656EBA6252464C20` | 逐键相同 |
| C9 每省最大尝试 | 5 | `FDA5A76D45B639FD0B793E6270D051255CCFC0F85E7E982A152A4AA7743D7028` | 逐键相同 |
| 新 C9 加未来 C10 累计 | 39 | `3E2DF35B6D867A0680E1ABBBB778205982F1845139D775A63A9D4672B7D6CA3A` | 逐键相同 |

数值例：新 C9 的 `turn9_household_calls=1`、`corrected_policy_maps=1581`、`selector_evaluations=1264800`、`terminal_kfe_attempts=31`；每省相应为 `51`、`40800`、`1`；新累计 `turn9_household_calls=1`、`turn10_household_calls=1`。全表只构成**额外预算候选**；其中 C10 数值不授予 C10 调用权，新的 C9 调用权也尚为零。

## 旧失败的三层证据与两种治理扣账

机器文件逐类列出 39 行及逐省 5 行：`guard_confirmed_attempts`、`source_observed_calls`、`province0_recorded`、`reserved_province0_exposure_not_calls` 分列；`null` 表示该层无记录，不能读作零。每行实际旧消耗统一为 `UNRESOLVED`。旧失败收据确认 C9 household `1`、13 次 corrected maps、12 次 direct HJB、1 次省 0 terminal KFE；source 另观察 1 次 native initialization、800 次 labor roots、10,400 次 selector evaluations、4,932 次 scalar selector roots、13 次 D2/Q 等。省 0 的预留暴露包含 51 maps、40,800 selector evaluations、20,000,000 scalar roots、50 direct updates、1 terminal KFE；**预留不是实际调用**。日志 `attempt_journal_0000129` 记录省 0 的 selector 等局部累计，`0000131` 记录 KFE 入门前尝试，`0000132` 仅记录后续类别的预留。不能将这些层相加，也不能从 guard 零值推断实际零或已核清余额。298 项部分清单读回 `PASS` 只保护文件字节。

| 旧失败治理选项 | 如何计入旧命名空间 | 对新授予预算的影响 |
| --- | --- | --- |
| **推荐：完整旧 C9 turn 保守扣账** | 对旧 C9 每类别计入其全部上限，对 31 省的五项逐省上限也作完整治理占用；这是**行政扣账，不是声称已发生的模型调用**。旧窗口冻结，旧 C10 机会保持关闭。 | 在旧预算和旧项目总量内，新完整 C9 仍被挡住；只有 Owner 明确批准**额外**新命名空间和更高项目生命周期治理总量，才可能继续。机器文件给出逐类 `旧完整 C9 扣账 + 新 C9/C10 累计上限` 的候选生命周期上界，仍非实际调用数。 |
| 省 0 已知预留暴露扣账 | 对已确认、source 观察或省 0 已预留的类别取治理性最大值；未覆盖类别与其他省份保持 `UNRESOLVED`，不填零，不宣称这是全部调用的严格上界。 | 若仍约束于旧窗口，已确认的 household `1/1`、省 0 KFE `1/1` 已阻止新完整 C9；若 Owner 另授新预算，还须明确未知项如何计入项目总量，否则不能执行。 |

推荐完整旧 turn 扣账，因为它不依赖从失败现场推断精确余额，且能清楚显示新增授权的成本：旧窗口保留一笔完整治理占用，新窗口独立记账，项目生命周期治理上限按两者之和显式增加。旧 C9 的真实科学调用始终保持三层证据与 `UNRESOLVED`；不得把治理扣账写回收据充当实际数。新窗口的**每类别、逐省、每 turn、C9 加 C10 累计**限制需同时约束每次科学入口；失败尝试先计、首失败即停、零重试，不借用别省、别日期或未来 C10 额度。旧窗口不得清零；新窗口不得吸收或掩盖旧 `RUN001`。若 Owner 不接受新增项目总量，则该路线在现有上限下阻塞。

## Owner 必须明确回答的采纳问题

1. 是否采纳三张精确数值表及其规范 SHA-256，作为**新增**命名空间的上限，而非重置旧窗口？若不采纳，应给出逐键额度及依据；本提案没有替代值。
2. 是否采纳**完整旧 C9 turn 治理扣账**并冻结旧命名空间、关闭旧窗口的 C10 机会？若选择省 0 暴露法，未知类别、其余省份及项目总量如何保守处理？在答案前不得推算余额。
3. 是否采纳项目生命周期治理上界为“旧完整 C9 扣账 + 新 C9/C10 累计候选”，并清楚区分治理额度与实际调用？这实质增加总科学风险暴露，需要独立 Owner 决定。
4. 是否为**新 C9 一次性尝试**单独采用 36,000 秒协作式单调进程资源墙、首失败零重试及人工中断后 `CALL_LEDGER_UNRESOLVED` 即停规则？资源墙只阻挡到期后的下一科学入口，在途调用可越墙、跨午夜；它不是完成时间上界，不能自动开放 C10。
5. 是否在上述预算独立审查后，另行授权新 runner/delegate/合同及身份链的零科学准备？任何模型调用仍须更晚的独立一次性 Owner 执行决定。

## 未来静态身份与数值门

先独立审查本预算提案，再由 Owner 逐项采纳或驳回。若采纳，后续另立精确任务：新 runner 与 delegate 必须共同绑定新 ID、独占且仍不存在的根、新命名空间、已采纳数值、36,000 秒规则及各自新字节哈希；新 runner 独立审查绑定两者；新合同绑定审查、冻结 C8 manifest/readback/JSON/NPZ 和预算；Owner 执行采纳、逐字节相同且已提交的 `TASK_CURRENT.md`/单一任务副本，最后独立最终身份审查，均须完成后才能向 Owner 请求新一轮科学授权。旧 live 合同仍绑定旧 wrapper/review 哈希；仅换哈希或路径无法复用 `RUN001`。本任务不创建这些文件或输出根。

未来只有**完整、合法、独立封存并读回通过**的新 C9 才可与已封存 C8 作九项、每项严格 `<1e-6` 的第一轮比较；失败的部分 C9 不计。可能的第二轮 C9→C10 仍须单独 C10 授权与完整封存，连续两次全过也仅是待独立审查的有界数值候选，不直接给 Results 资格。科学、身份、预算、资源或封存的首个失败均停在原始终态并保全账本。

## 来源边界

旧 live 合同原始 SHA-256 `65992776BFBED510F5C59DBC14B8CBE0B65DCCBAD08C5E0559491303D5A5B466`；本预算机器提案原始 SHA-256 `66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460`。Owner 选择文件 `3D33AA6C12792E7D6B229EA2F54808F463F61F1F01A6FC7E99AD6A117D6FE619`。旧失败的 `first_failure`、`terminal_receipt`、`partial_artifact_readback`、`timing_failure` 原始 SHA-256 依次为 `138DBF7601BF84568E22EBF752EB400D612348575C559495D1A87F562A4A3260`、`A687671A0F1866A663C8F3D6E6FC44B965CC5385AFF468F831CE13C673DE409E`、`EA341BD793619D6125662C4F4C079661C116F0E6FD603088150525E572803EF1`、`21D7579449AD0DCDE532B9D7695E83FF188AD3E09D9D02A798D574000DEED2E0`。
