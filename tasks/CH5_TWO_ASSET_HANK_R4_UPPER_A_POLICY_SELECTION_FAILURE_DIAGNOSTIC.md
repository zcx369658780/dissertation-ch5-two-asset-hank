# CH5_TWO_ASSET_HANK_R4_UPPER_A_POLICY_SELECTION_FAILURE_DIAGNOSTIC

## Task

Diagnose the third frozen R4 steady-state primary HJB policy-selection failure after the accepted zero-liquid certification and interior-a zero-drift candidate repairs.

## Authority

This task is the sole execution authority for bounded R4 upper-a policy-selection failure diagnostic work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Zero-drift certification repair accepted.
- Interior a-zero-drift candidate construction accepted.
- Frozen R4 rerun failed at upper illiquid asset boundary state `(a,b,z)=(1.0,0,0.8125)`.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- R4 policy fixture resolution reports
- R4 steady-state rerun failure report
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- diagnose the failing upper-a policy-selection state;
- inspect candidate generation;
- inspect upper-a boundary conditions;
- inspect admissibility checks;
- classify whether failure originates from:
  - candidate construction;
  - upper boundary conditions;
  - numerical certification;
  - economic restrictions;
- generate diagnostic evidence report.

## Required scientific checks

The diagnostic must report:

- failing state and coordinates;
- available candidates;
- rejected candidates and rejection reasons;
- upper-a boundary consistency;
- KKT consistency;
- whether this is a new blocker class or a previous repair class;
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
