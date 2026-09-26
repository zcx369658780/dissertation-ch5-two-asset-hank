# C9 active 合同提案（零科学）

状态：`BUILDER_ACTIVE_CONTRACT_PROPOSAL__AWAITING_INDEPENDENT_GPT_WORK_ACCEPT_REJECT`。本文件是提案记录，不是 Owner 执行采纳或一次性 C9 授权。Results eligibility 为 `FALSE`。

## 入口与依据

- 唯一工作树 `D:\ProjectTemp\c5k1bturn56`；入口 HEAD `6eb2ab34857f2bc4a79f8240697eab204e3ada18`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。任务当前件和归档件逐字节相同且已提交；跟踪文件干净，仅四份受保护输出根未跟踪。
- Owner 文件 `docs/CH5_K1B_C9_TEN_HOUR_COOPERATIVE_RESOURCE_WALL_OWNER_ADOPTION_20260926.md` 明确采用 C9-only `resource_wall_seconds=36000` 的协作进程资源墙。它阻止到期后的**下一次**科学入口，不能强行终止正在运行的调用，也不是可信的 C9 完成时长上界；不授予 C10 墙钟或执行权。
- 已提交的 `docs/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_RUNNER_INDEPENDENT_REVIEW.md` 给出静态 verdict `ACCEPT__C9_TIMED_RISK_EXCEPTION_RUNNER`，精确列明 wrapper 路径和原始 SHA-256 `0E43522B64F7BD34C46C92A967F41FBDD373C3DD15DCC188821CB0EDB3AB368B`，delegate 路径和原始 SHA-256 `A4B4985DAE8C15E5F21125A0A82FCE39D1B08D975929250186D941D691C4E7BB`。两者已直接按文件字节读回且 Git blob 与 HEAD 一致；审查文件原始 SHA-256 为 `EA21124F8E01470D2D03DE1FB6B496CCA7EDDC584EF7270796EB01DD08C94354`。

## 提案与 live 合同的规范逐键差异

提案路径为 `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_ACTIVE_CONTRACT_PROPOSAL_20260926.json`。它由当前已提交 live inactive 合同的字节副本生成，仅替换以下六个顶层键值；提案原始 SHA-256 为 `65992776BFBED510F5C59DBC14B8CBE0B65DCCBAD08C5E0559491303D5A5B466`。

| JSON 键 | live inactive 值 | 提案值 |
| --- | --- | --- |
| `active` | `false` | `true` |
| `execution_id` | `null` | `"C9_TIMED_RISK_RUN001"` |
| `attempts` | `0` | `1` |
| `resource_wall_seconds` | `null` | `36000` |
| `wrapper_sha256` | `null` | `"0E43522B64F7BD34C46C92A967F41FBDD373C3DD15DCC188821CB0EDB3AB368B"` |
| `independent_review_sha256` | `null` | `"EA21124F8E01470D2D03DE1FB6B496CCA7EDDC584EF7270796EB01DD08C94354"` |

逐键 JSON 比较仅发现上表六项。`delegate_sha256` 保持已接受重绑值；输出根、`retries=0`、预算命名空间、全部类别/逐省/C9+C10 上限、C8 冻结输入身份、正常时长门、无自动 C10 和 Results false 均与 live 合同相同。live `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_INACTIVE_CONTRACT.json` 未修改，仍为 inactive。

## 惰性读回与剩余门

- 提案 JSON 解析和字节读回通过；五份依据文件的已提交身份通过。实际 live `future_gate()` 返回 `BLOCKED__INACTIVE_CONTRACT`。live 默认前检退出码 `0`，状态 `BLOCKED__INACTIVE_CONTRACT`，delegate hash、全部 wrapper 与 delegated 检查为真，科学/C9/C10 计数均为 `0`。
- wrapper `--execute` 退出码 `1`，终态 `BLOCKED__INACTIVE_CONTRACT`；delegate 直接执行 CLI 退出码 `1`，终态 `BLOCKED__C9_WRAPPER_REQUIRED`。没有创建 C9 timed-risk 或 outer 输出根。
- 四份受保护输出清单 SHA-256 依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`。

本任务字面模型、科学、C9、C10 与重试调用均为 `0`。正常时长门仍是 `BLOCKED__DURATION_BOUND_UNAVAILABLE`。仅在 GPT Work 独立 ACCEPT/REJECT 及后续另行 Owner 采纳后，才可能讨论将提案复制到 live 合同；本任务不创建 Owner 执行采纳、active 执行任务或 C9 输出。
