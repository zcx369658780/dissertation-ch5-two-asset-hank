# CH5_TWO_ASSET_HANK_R4_UPPER_A_LOWER_B_POLICY_SELECTION_FAILURE_DIAGNOSTIC

## Task

Diagnose the next frozen R4 steady-state primary HJB policy-selection failure after accepted zero-liquid certification, interior-a zero-drift construction, upper-a boundary contract resolution, dual upper-corner boundary closure resolution, and intermediate upper-b closure resolution.

## Authority

This task is the sole execution authority for bounded R4 upper-a/lower-b policy-selection diagnostic work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Zero-liquid certification repair accepted.
- Interior a-zero-drift candidate construction accepted.
- Upper-a policy boundary contract resolution accepted.
- Dual upper-corner boundary closure accepted.
- Intermediate upper-b interior-a zero-drift closure accepted.
- Frozen R4 rerun failed at `(a,b,z)=(1.0,0.0,0.6875)`.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- R4 policy fixture resolution reports
- latest R4 rerun failure report
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- reproduce the failing policy-selection state for diagnosis only;
- inspect candidate generation;
- inspect upper-a/lower-b boundary interactions;
- inspect multiplier, direction and complementarity checks;
- classify whether failure originates from:
  - candidate construction;
  - boundary closure;
  - numerical certification;
  - economic restrictions;
- generate diagnostic evidence report.

## Required scientific checks

Report:

- failing state and coordinates;
- generated candidates;
- rejected candidates and reasons;
- upper-a contract consistency;
- lower-b boundary consistency;
- interaction with existing dual contracts;
- KKT consistency;
- whether this is a new blocker class;
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
- force candidate acceptance;
- rerun frozen steady-state after modifications;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Failure rule

If diagnosis requires changing economics or frozen contracts, stop and report a scientific blocker.

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
