# 2026-10-02 DOT 审查与任务交付

本次治理文档经独立原review/delta PASS及父DOT终裁ACCEPT/CLOSED，非科学ACCEPT；本节覆盖旧角色/路由/交接表述，原科学裁决与风险门保留，保护改变不得降级。

| 角色/风险 | 职责/流程 |
|---|---|
| Owner | 最终科学权威；实质科学选择、保护目标与具体科学/实验预算采纳 |
| DOT承接Work | 规划、发单、状态管理、科学路线建议，组织独立审查并记录最终裁决；综合判断不代替真正独立科学审查 |
| Builder | 单任务受界实现/必要修正/验证/记录；不自受、不发科学successor |
| LOW日常文档 | 既有事实文档/索引自检；本次治理已依明确要求完成独立原review/delta确认和父DOT终裁 |
| MEDIUM工程 | 已采纳合同下聚焦轻审，精确路径/不变量/运行预算先行；科学或保护改变升级 |
| HIGH科学/保护 | 明确授权→受界执行→真正独立科学审查→DOT记录→必要Owner采纳；不能降为LOW文档/机械修复/优化 |

单任务一可验收问题，范围内必要修正、验证和记录一并完成；不无限拆为API字段任务。仅未来任务可事先列明确有限行政纠错预算（数字、允许对象/错误、终止条件、分账）；不得重开旧STOP或续用模型/受保护读取/SDK/native/数据/实验预算。未明确纠错额度不得自行补发，科学首败和failed calls计账保留。

HIGH Reviewer独立于候选Builder/作者，须有自己的证据核对和裁决；同一Builder换标签不构成独立。工程实现、数值有效、科学接受、Results资格分开。本次独立原review/delta均PASS，父DOT已终裁治理文档ACCEPT，Builder仅记录、不自受；见docs/CH5_DOT_GOVERNANCE_ROUTE_REVIEW_20261002.md。

DOT本地资格按仓库/绝对目录/任务/证据和角色隔离核定，不沿旧app成员资格门，不声称本线程属于旧项目。当前执行01a0fa7d-9573-7496-a6eb-a633c70fd0fd，旧Builder不自动路由。
约30次实际用户助手对话或上下文不可靠时DOT主动保全进度/裁决/证据/保护/预算/未知账本和下一门，再继任只读核对；内部工具不算轮数，不要求Owner搬主聊天。交接本身不授予、新增、重置或恢复科学预算。若原任务明确允许接续且预算未耗尽，继任完成只读核对后仅可沿用该任务原有剩余额度与停点；已关闭、耗尽、账本不明或需Owner决定的任务不得接续。新科学任务仍须相应具体授权。交接不解除Owner或独立审查门。

科学/保护/预算冲突先停交DOT/Owner；不暗改法则或弱化Objective A。本轮仅文档差异/链接/范围/状态检查。来源见CURRENT与docs/CH5_DOT_GOVERNANCE_ROUTE_PLAN_20261002.md、docs/CH5_DOT_GOVERNANCE_ROUTE_RESULT_20261002.md。

以下原审查条款无损保留，旧角色/app交接表达按本节更新，其余禁止保持。

---

# Work / Codex / Owner Review Gate

Updated: 2026-09-23.

## Roles

- **Owner**: final scientific authority; adopts or rejects economic definitions, calibration, mathematical contracts, and Results claims.
- **GPT Work**: Project Lead, Orchestrator, L3 independent Reviewer, and scientific-route advisor; creates `TASK_CURRENT.md`, reviews evidence, and records acceptance or the next gate.
- **Codex**: bounded Builder/executor; implements only the active task, runs authorized checks, preserves evidence, and reports the first failure. Codex does not independently accept its own high-risk scientific change.

## LOW RISK

Examples: local documentation synchronization, formatting, paths, manifests, evidence indexing, deterministic readback, tests that do not invoke model science, and mechanical fixes after the cause and target behavior are already accepted.

Flow:

`Work authorization -> Codex execute -> self-check -> update local state`

Independent scientific review is normally unnecessary. A local commit is sufficient unless backup/publication is explicitly requested.

## MEDIUM RISK

Examples: solver implementation under an already adopted specification, numerical bug fixes that preserve equations and tolerances, integration plumbing, adapters, performance, persistence, and reproducibility changes.

Flow:

`Work task -> Codex bounded execution -> focused evidence -> Work lightweight review`

The task must name allowed source paths, invariants, test/runtime budget, and stop conditions. Codex may fix ordinary engineering defects inside scope but may not change the accepted scientific object.

## HIGH SCIENTIFIC RISK

Includes household equations, utility, constraints, FOCs, KKT, boundary economics, HJB/KFE mathematical contracts, payoff definition, return/migration mechanism, calibration, convergence law, GE, shocks, IRFs, welfare, Results, and dissertation economic interpretation.

Required flow:

`Work/Owner scientific authorization -> Codex bounded execution -> independent Work review -> Owner adoption when the decision is substantive`

The Builder terminal establishes only execution evidence. It does not by itself establish independent acceptance, equilibrium, calibration validity, or Results eligibility.

## Escalation rules

- If evidence exposes a choice among scientifically different laws, stop for Work/Owner.
- If a defect is representational or mechanical and the intended accepted behavior is already exact, handle it at the task's stated risk level.
- Never tune parameters, tolerances, grids, solver families, damping schedules, or retry counts merely to recover PASS.
- Review existing immutable evidence when sufficient; do not rerun expensive science only to reproduce already sealed evidence.
- After an ACCEPT or REJECT, Work updates the local decision/state and, when the next bounded action is determined without an Owner decision, issues the next `TASK_CURRENT.md` automatically. A consumed budget, first-failure stop, or substantive scientific choice remains a gate.
- A handoff is a timing exception to immediate task issuance: the handoff response contains only the prompt. The new conversation first verifies local state, then issues the next eligible task without asking for redundant permission.
- Under the Owner's standing 2026-09-27 instruction, GPT Work proactively performs Codex conversation handoff within the named app project at the 30-record threshold, unreliable context, or a replacement-requiring error. It need not ask the Owner to designate each successor. Preserve current authority and evidence first; verify the successor's project membership and read-only intake before any writing task. Handoff itself never authorizes scientific execution, resets consumed calls, changes a safety objective, or replaces an independent ACCEPT/REJECT gate. An unresolved Owner decision or protected-action gate keeps `TASK_CURRENT.md` closed.
