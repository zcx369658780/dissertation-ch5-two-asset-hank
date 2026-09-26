# C9 live 合同精确激活（零科学身份链）

状态：`BUILDER_LIVE_CONTRACT_ACTIVATION_CANDIDATE__AWAITING_INDEPENDENT_GPT_WORK_ACCEPT_REJECT`。Owner 在 `docs/CH5_K1B_C9_EXACT_ACTIVE_CONTRACT_OWNER_ADOPTION_20260926.md` 采纳精确提案，仅授权零科学最终身份链；未授权一次性 C9 执行。Results eligibility 为 `FALSE`。

## 入口与精确复制

- 唯一工作树 `D:\ProjectTemp\c5k1bturn56`；入口 HEAD `af050f573d7719bbc3e264c5a77e0cd03d34ad21`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。任务当前件和归档件逐字节一致且已提交，入口跟踪文件干净，仅四份受保护输出根未跟踪。
- 将已审查提案 `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_ACTIVE_CONTRACT_PROPOSAL_20260926.json` 的**原始字节**复制到历史命名的 live `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_INACTIVE_CONTRACT.json`；没有重新序列化 JSON。复制前提案 SHA-256 与任务指定的 `65992776BFBED510F5C59DBC14B8CBE0B65DCCBAD08C5E0559491303D5A5B466` 一致，复制后两份文件逐字节相同，原始 SHA-256 均为该值。
- live 内容现为 `active=true`、`attempts=1`、`execution_id="C9_TIMED_RISK_RUN001"`、`resource_wall_seconds=36000`、`retries=0`，并保留精确 wrapper、delegate、独立审查、预算和冻结输入身份。36,000 秒只是 C9 协作资源墙，不是完成时长上界；C10 无自动授权。

## 提交后的静态核验

- 先提交合同和两份惰性测试，再调用 `static_preflight(repo, require_inactive=False)`：`PASS__ACTIVE_PREFLIGHT_ONLY`，全部 wrapper 与 delegated 身份/预算检查为真，科学、C9、C10 计数均为 `0`。
- 使用固定已提交 delegate 对象直接调用 `future_gate(repo, "C9_TIMED_RISK_RUN001", delegate)`：首个终态为 `BLOCKED__FRESH_C9_TASK_GATE`。delegate 自身的执行任务门也在 `BLOCKED__FRESH_EXECUTION_TASK_GATE` 拒绝。runner 识别的执行 Owner 采纳文件和一次性任务文件均不存在；`TASK_CURRENT.md` 仍是本零科学任务。
- 只运行不调用 `--execute`、`execute_once`、`run_timed_action` 或 `_execute_after_gate` 的聚焦惰性测试：`13 passed`。既有预算、身份、失败封存测试代码保留；本任务没有运行其中会触及被禁止执行入口的测试。
- 四份受保护输出清单 SHA-256 依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`。C9 timed-risk 与 outer 输出根均不存在。

本轮模型、科学、C9、C10、重试调用字面账本均为 `0`。active 静态前检通过不等于执行就绪；尚需本候选的 GPT Work 独立 ACCEPT/REJECT、另行 Owner 执行采纳和明确的一次性任务授权。正常时长门仍为 `BLOCKED__DURATION_BOUND_UNAVAILABLE`，Results eligibility 仍为 `FALSE`。
