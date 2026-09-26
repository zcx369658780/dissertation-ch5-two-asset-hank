# C9 失败后新尝试：零科学设计提案（2026-09-26）

**性质：仅供独立审查和 Owner 后续决策。** Owner 只采纳了设计路线，未授予新预算或执行权。`C9_TIMED_RISK_RUN001` 已消耗，旧输出根 `reports/ch5_k1b_turn9_timed_risk_exception_run001` 保持原样；最终终态 `CALL_LEDGER_UNRESOLVED`、`complete_outer_turn=false`、`safe_pause=false`、`retry_allowed=false`。C10 与 Results 均关闭，Results eligibility 为 `FALSE`。本提案不创建任何 runner 可识别的任务、合同、采纳文件或输出根。

## 1. 独立身份链（全部待新授权）

仅作为名称候选：新执行 ID `C9_POST_FAILURE_NEW_ATTEMPT_001`，独占新根 `reports/ch5_k1b_turn9_post_failure_new_attempt_001`。核验时该精确路径不存在；不得借用、清理、覆盖旧根，也不得称为旧尝试的重试或续跑。只有 Owner 作出新的实质科学决定后，这些名称才可能进入待审的正式文件。

现有 wrapper 的 `OUTPUT`、`TASK_ID`/`TASK_STATUS`、`TASK_COPY`、`OWNER_ADOPTION`、`CONTRACT`、`INDEPENDENT_REVIEW` 及 `future_gate()` 的执行 ID、提交哈希、输出根检查都绑定旧链（`validators/multi_province/k1b_turn9_timed_risk_exception/run.py:22-42,180-249`）。delegate 的 `FUTURE_TASK_ID`/`FUTURE_STATUS`、`FUTURE_TASK_RELATIVE`、`TIMED_CONTRACT`、`OUTPUT` 及其 task/contract/output 校验也绑定旧链（`validators/multi_province/k1b_turn9_outer_r2/run.py:27-37,527-614`）。若未来新尝试获准，需要独立审查新 wrapper 与 delegate 的**实际新字节哈希及两者相互绑定**；新 runner 静态审查必须绑定那些新哈希；新合同必须绑定新 ID/根、runner 审查、明确预算和冻结输入；新 Owner 执行采纳必须绑定新合同/审查/ID/根；新的 `TASK_CURRENT.md` 与其单一任务副本必须逐字节相同、提交并绑定上述所有身份。随后还需独立最终身份链审查和单独的“一次”科学授权。只改 live 合同的 wrapper/review 哈希不足以建立新身份，现有 runner 对旧 ID/根的硬编码也会拒绝新路径。本任务不改这些文件。

现有已封存 C8 输入可以作为**待复核的**新尝试起点：C8 执行清单 `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`；进入 C9 的 manifest/readback/JSON/NPZ 分别为 `40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65`、`E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85`、`FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB`、`E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD`。新链须重验这些原始字节及来源，不从 C9 部分产物接续。

## 2. 已发生调用与预算处置

下表是旧失败收据中的**不同证据层**；`—` 表示该层没有相应预留行，并非调用零。省 0 仍在途。`timing_failure.json` 的 guard 确认值不能与 source ledger 数字相加，省级读数也不能代替已完成的全局协调。

| 类别 | guard 已确认 | source 已观察 | 省 0 预留暴露（上限，非调用） |
| --- | ---: | ---: | ---: |
| C9 household entry | 1 | 1 | — |
| source native initialization | 0 | 1 | 1 |
| scalar labor roots attempted / returned | 0 / 0 | 800 / 800 | 800 / 800 |
| corrected policy maps | 13 | 13 | 51 |
| selector evaluations | 0（省级记录 10,400） | 10,400 | 40,800 |
| scalar selector roots | 0（省级记录 4,932） | 4,932 | 20,000,000 |
| D2/Q assemblies | 0 | 13 | 51 |
| direct HJB updates | 12 | 12 | 50 |
| checkpoint evaluations after update | 0 | 12 | 50 |
| relaxation helper / alpha candidates | 12 / 12 | 12 / 12 | 50 / 2,650 |
| terminal KFE | 1 | 1 | 1 |
| SCC / restricted SVD / stationary candidate / Qᵀp / aggregate evaluation | 0 each | 1 each | 1 each |
| full integration | 0 | 0 | — |

其余 guard 的零值仅代表未被 guard 确认；在账本未核清时，不得一律推断为实际零消耗或可用余额。`first_failure.json`、`terminal_receipt.json` 内局部 `call_ledger_resolved=true` 与最终 wrapper 终态不一致，不能覆盖最终 `CALL_LEDGER_UNRESOLVED`。298 项部分清单的读回 `PASS` 只确认现存文件的长度和哈希，无完整 C9 或安全暂停。旧尝试耗时 128.813 秒，不是未来上界。

**预算备选及结论：**

| 处置选项 | 对已采纳每类别、逐省、每 turn、C9+C10 累计上限的影响 | 当前可否启动新完整 C9 |
| --- | --- | --- |
| 沿用旧 `C8_START_C9_C10_WINDOW`，把未核清项视为零 | 会漏计已确认和已观察的调用，并复用一次性授权；违反失败调用计入上限的规则 | 否，不可采纳 |
| 沿用旧窗口，按证据可支持的保守上界或整次 C9 上限计入 | 逐类别、逐省及累计余额只会减少；全额计入将耗尽 C9 每 turn 额度。即使仅用确定下界，`turn9_household_calls` 已为 1/1，省 0 KFE 已为 1/1，新的完整 C9 也受阻；未知项保持 `UNRESOLVED` | 否，除非 Owner 另行改变预算权威 |
| 先做零科学账本取证，再提出精确扣账 | 可能收窄部分未知区间，但现有封存证据不足以证明全局协调或恢复旧一次性授权；不得提前结算剩余额度 | 否，须独立审查及新 Owner 决定 |
| Owner 明确设立**另一个**新尝试预算/命名空间 | 必须同时规定旧失败如何记入历史、哪些类别和省份可再消耗、每 turn 与未来 C10 累计如何共同约束，避免双计或漏计；旧 `C8_START_C9_C10_WINDOW` 不得悄然清零 | 仅在新预算和完整身份链另行采纳后才可能 |

**建议 Owner 的下一项明确决定：** 保持新科学关闭，先决定是否愿意为独立新 C9 尝试制定一套显式新增预算及旧失败扣账政策；若不愿新增预算，应止于当前 `CALL_LEDGER_UNRESOLVED`。本提案不填写新的额度，也不宣称有可用余额。现有证据与原上限下，没有可辩护的直接执行路径。

## 3. 数值判据、资源墙和验证顺序

只有未来**完整、合法、封存且读回通过**的新 C9 才能与已封存 C8 比较九项载体：沿已采纳公式，九项均严格 `<1e-6` 才构成新窗口的第一次 pass；合法未过归零，数据缺失或身份/预算/封存失败不更新计数。旧 C7→C8 与这次部分 C9 均不计入新的两次连续 pass。将来若 Owner 再单独授权完整 C10，且 C9→C10 同样全过，才可能得到两次连续候选，仍须独立审查；它不自动证明经济均衡或 Results 可用。C10 目前没有授权。

若 Owner 将来重新采纳同类 C9-only `36,000` 秒协作式单调进程资源墙，必须明确它从新 wrapper 开始计时，仅在到期后的**下一科学入口**拒绝；在途调用可越过 36,000 秒、午夜或计划关机时点。人工中断可能留下 `CALL_LEDGER_UNRESOLVED`，不得获得免费重试或部分续跑。首个失败即停，保存原始终态、guard/source/预留三层账本、部分清单及读回；只有完整 turn 的封存读回才允许安全跨天暂停。该墙不是 C9 完成时间上界，不能用 C8 单次 3,382.203 秒观测替代。

未来静态顺序：先独立审查本设计；Owner 明确旧失败扣账、新每类别/逐省/每 turn/累计预算、C9 资源与人工中断政策及 C10 是否继续关闭；另行精确任务准备新 runner/delegate/合同和惰性检查；独立审查字节身份、冻结 C8 输入和全部失败路径；Owner 采纳精确合同与新一次性任务/输出根；最终独立身份链复核；最后才可由 Owner 另行决定是否执行一轮科学。任何一步失败即停，不沿用旧 `RUN001` 的任务、合同、输出或预算余额。

## 原始证据身份

旧合同 SHA-256 `65992776BFBED510F5C59DBC14B8CBE0B65DCCBAD08C5E0559491303D5A5B466`（仍绑定旧 wrapper）；修复 wrapper `59A63E933BF13A4FC39EC583227B2E9724B5E06B510A1896CB1307DBCC8F1D06`；delegate `A4B4985DAE8C15E5F21125A0A82FCE39D1B08D975929250186D941D691C4E7BB`；当前 runner 静态审查 `4A42989DFCA0AF8A58CE529D094C4066AC3D5C4BB3CAE143201343BCF0B464D5`。旧 `first_failure`、`terminal_receipt`、`partial_artifact_readback`、`timing_failure` 原始 SHA-256 依次为 `138DBF7601BF84568E22EBF752EB400D612348575C559495D1A87F562A4A3260`、`A687671A0F1866A663C8F3D6E6FC44B965CC5385AFF468F831CE13C673DE409E`、`EA341BD793619D6125662C4F4C079661C116F0E6FD603088150525E572803EF1`、`21D7579449AD0DCDE532B9D7695E83FF188AD3E09D9D02A798D574000DEED2E0`。
