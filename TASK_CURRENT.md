# Current Builder Task

Status: `AWAITING_OWNER_CONVERGENCE_DESIGN_DECISION`

## Objective

Preserve the independently accepted turn5-turn6 bounded trajectory, sealed turn7 input, and accepted zero-science convergence-design evidence dossier. Do not execute scientific work until the Owner adopts a dedicated fixed-point/convergence diagnostic design and Work replaces this file with one explicit bounded task.

## Allowed scope

- Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, `REVIEW_GATE.md`, the independent review decision, and directly relevant evidence.
- Report inconsistencies or missing authority.
- Make no source, model, or evidence changes under this waiting task.

## Inputs

- Current state: `CURRENT.md`
- Accepted science: `SCIENTIFIC_DECISIONS.md`
- Review routing: `REVIEW_GATE.md`
- Independent review: `docs/CH5_MP4C_K1B_TURN5_TURN6_INDEPENDENT_REVIEW_ACCEPTANCE_20260923.md`
- Design evidence review: `docs/CH5_K1B_CONVERGENCE_DESIGN_EVIDENCE_DOSSIER_INDEPENDENT_REVIEW_20260923.md`

## Required check

Confirm that no newer local task has replaced this waiting file.

## Evidence to persist

None.

## Stop conditions

Stop immediately because Owner convergence-design authority and a scientific Builder call budget are absent.

## Forbidden work

Turn7 household, later turns, HJB/KFE, integration, K1B sensitivity, K2, GE, annualization, shocks, IRFs, welfare, Results, scientific source changes, tuning, and successor creation.

## Expected terminal

`STOP__DESIGN_EVIDENCE_ACCEPTED__OWNER_CONVERGENCE_DESIGN_DECISION_PENDING`
