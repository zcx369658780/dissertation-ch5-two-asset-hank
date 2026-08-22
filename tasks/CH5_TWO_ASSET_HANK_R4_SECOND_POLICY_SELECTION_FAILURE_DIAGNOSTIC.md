# CH5_TWO_ASSET_HANK_R4_SECOND_POLICY_SELECTION_FAILURE_DIAGNOSTIC

## Task

Diagnose the second frozen R4 steady-state policy-selection failure after the accepted zero-drift certification repair.

## Authority

This task is the sole execution authority for bounded R4 second policy-selection failure diagnostic work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Zero-drift certification repair accepted.
- Frozen R4 rerun failed at a new policy-selection state after repair.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- R4 policy fixture resolution report
- R4 steady-state rerun failure report
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- diagnose the failing policy-selection state;
- inspect candidate generation;
- inspect admissibility checks;
- classify whether failure originates from:
  - candidate construction;
  - boundary conditions;
  - numerical certification;
  - economic restrictions;
- generate diagnostic evidence report.

## Required scientific checks

The diagnostic must report:

- failing state and coordinates;
- available candidates;
- rejected candidates and rejection reasons;
- boundary/KKT consistency;
- whether this is the same class of zero-drift certification issue or a distinct blocker;
- recommended next scientific decision point.

## Forbidden operations

Do not:

- modify fixture parameters;
- change grids;
- change calibration;
- modify economic equations;
- modify policy logic;
- modify generator;
- relax constraints silently;
- accept forced candidates;
- rerun frozen steady-state after modifications;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Output requirements

Report:

- verdict;
- files read/written;
- diagnostics executed;
- scientific diagnosis;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Next gate candidate

CH5_TWO_ASSET_HANK_R4_POLICY_FIXTURE_RESOLUTION
