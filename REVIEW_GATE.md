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
