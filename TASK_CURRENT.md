# Current Builder Task — K1B convergence-design evidence dossier

Task ID: `CH5_K1B_CONVERGENCE_DESIGN_EVIDENCE_DOSSIER_20260923`
Status: `ACTIVE`
Risk: scientific-route preparation only. Scientific/model calls: `0`. Results eligibility: `FALSE`.

## Objective

Prepare a source-grounded decision dossier for Work and Owner to design a future fixed-point/convergence diagnostic. Identify what the accepted turn3–turn6 evidence actually measures, which state or aggregate objects could be compared across turns, and which scientific choices remain open. Do not select or implement a convergence law. Do not run turn7 household.

The dossier is advice and provenance, not scientific adoption or execution authority. Stop before a substantive choice about object, norm, tolerance, stopping rule, maximum turns, or failure behavior.

## Start and inputs

- Worktree: `D:\ProjectTemp\c5k1bturn56`. Verify Git root, local HEAD, and worktree status before work. Dispatch baseline is the parent of this task's dispatch commit; report the actual dispatch HEAD observed at startup.
- Read in order: `AGENTS.md`, `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, `TASK_CURRENT.md`, `REVIEW_GATE.md`.
- Then read only the directly relevant accepted sources: `docs/CH5_MP4C_K1B_TURN5_TURN6_INDEPENDENT_REVIEW_ACCEPTANCE_20260923.md`, `docs/CH5_MP4C_K1B_TURN5_TURN6_BOUNDED_CONTINUATION_DIAGNOSTIC_REPORT.md`, and the named trajectory diagnostic and manifests under `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/`.
- Read production source only to identify existing output/state definitions and timing; do not execute or modify it. Cite exact file/line or sealed evidence path for every factual contract.

## Allowed work

1. Inventory the compared variables available at complete-turn checkpoints, their dimension, unit/normalization, timing, and provenance. Separate model state, policy/share, payoff, and reported aggregate quantities; mark any undefined or unavailable object `UNRESOLVED`.
2. Reproduce from sealed reports/JSON only the existing descriptive turn3→4, turn4→5, and turn5→6 change measures and their definitions. Do not extrapolate a contraction rate, estimate a fixed point, or infer convergence from shrinking changes.
3. Present a concise Owner decision matrix for the compared economic object, norm/scaling, tolerance, checkpoint timing, stopping rule, maximum turns/call budget, and failure behavior. For each, state what evidence supports, what remains a scientific choice, and consequences for a future bounded diagnostic. Recommendations may be labeled as proposals, never adopted defaults.
4. Write one human-readable dossier and one machine-readable source/decision inventory. Validate citations, identities and zero-call ledger with static checks. Commit only the two allowed output paths locally with explicit staging. If the app sandbox cannot write this worktree or its Git metadata, preserve the first error and stop; do not switch to another repository.

## Allowed write paths

- `docs/CH5_K1B_CONVERGENCE_DESIGN_EVIDENCE_DOSSIER_20260923.md`
- `EVIDENCE/ch5_k1b_convergence_design_dossier_20260923/decision_inventory.json`

`CURRENT.md` and `TASK_CURRENT.md` are Work-owned and must not be edited by Builder.

## Hard boundaries

- HJB/KFE, selector, root, D2/Q, integration, firm, K1B, K2, MATLAB, GE, annual, shocks, IRF, welfare, and Results calls: `0`. No turn7 household, no recalibration, no threshold tuning, no rerun, no new numerical trajectory.
- Do not edit `src/`, `reports/`, `tests/`, `validators/`, accepted evidence, `SCIENTIFIC_DECISIONS.md`, or `REVIEW_GATE.md`. Preserve production `src` tree `00682b2e1a7ba23665f6e16f6acf48ad35874883`.
- No GitHub fetch/push/remote readback, branch/issue/PR, global Codex setting, or unrelated project access. Do not enter `deep-learning-hank`.
- No adoption of a fixed-point/convergence law, steady-state or equilibrium claim, successor scientific task, or Results permission. First unsupported fact remains `UNRESOLVED`; do not fill gaps from memory.

## Terminal and review

Report observed HEAD, changed paths, source tree, static checks, first blocker if any, final local commit if made, and zero scientific-call ledger. Return `PASS__CH5_K1B_CONVERGENCE_DESIGN_DOSSIER__ZERO_SCIENCE__AWAITING_WORK_REVIEW` only when both outputs are committed and checked. Otherwise return `BLOCKED__CH5_K1B_CONVERGENCE_DESIGN_DOSSIER__FIRST_FAILURE_RECORDED`.

Work independently reviews the dossier. Owner decides any substantive convergence law before Work can issue a bounded turn7 or later scientific task.
