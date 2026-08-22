# CH5_TWO_ASSET_HANK_R4_UPPER_A_LOWER_B_POLICY_SELECTION_FAILURE_LATEST_DIAGNOSTIC_08125

## Task

Diagnose the latest frozen R4 steady-state primary HJB policy-selection failure at `(a,b,z)=(1.0,0.0,0.8125)` after prior upper-a/lower-b resolution work.

## Authority

This task is the sole execution authority for bounded read-only R4 upper-a/lower-b diagnostic work for the latest failure state.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Accepted zero-liquid certification, interior-a zero-drift, upper-a, dual-upper, intermediate upper-b, upper-a/lower-b, and upper-a/interior-b policy resolutions remain unchanged.
- Latest frozen R4 rerun failed at `(a,b,z)=(1.0,0.0,0.8125)`.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- AGENTS.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- latest R4 rerun failure report
- latest upper-a/lower-b related resolution reports
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- reproduce the latest failing policy-selection state for diagnosis only;
- inspect candidate generation;
- inspect upper-a/lower-b boundary interaction;
- inspect multiplier, direction, complementarity and KKT checks;
- classify whether failure originates from candidate construction, boundary closure, numerical certification, or economic restrictions;
- generate diagnostic evidence report.

## Required scientific checks

Report:

- exact failing state and coordinates;
- generated candidates;
- rejected candidates and reasons;
- upper-a consistency;
- lower-b consistency;
- interaction with existing contracts;
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
