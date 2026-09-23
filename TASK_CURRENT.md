# Current Builder Task

Status: `AWAITING_WORK_REVIEW`

## Objective

Preserve the post-turn6 Builder candidate. Do not execute scientific work until GPT Work independently reviews candidate `392f07b2d803d5a0d8a2c5c270858cfdbef1db80`, records ACCEPT/REJECT, and replaces this file with one explicit bounded task when appropriate.

## Allowed scope

- Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, `REVIEW_GATE.md`, and directly relevant evidence.
- Report inconsistencies or missing authority.
- Make no source, model, or evidence changes under this waiting task.

## Inputs

- Current state: `CURRENT.md`
- Accepted science: `SCIENTIFIC_DECISIONS.md`
- Review routing: `REVIEW_GATE.md`

## Required check

Confirm that no newer local review decision or task has replaced this waiting file.

## Evidence to persist

None.

## Stop conditions

Stop immediately because independent Work review is pending and no scientific Builder objective or call budget is active.

## Forbidden work

Turn7 household, later turns, HJB/KFE, integration, K1B sensitivity, K2, GE, annualization, shocks, IRFs, welfare, Results, scientific source changes, tuning, and successor creation.

## Expected terminal

`STOP__TURN5_TURN6_BUILDER_CANDIDATE_PENDING_INDEPENDENT_WORK_REVIEW`
