# CH5_TWO_ASSET_HANK_R4_UPPER_A_LOWER_B_POLICY_SELECTION_FAILURE_LATEST_RESOLUTION_08125

## Task

Resolve the latest R4 frozen steady-state primary HJB policy-selection blocker at `(a,b,z)=(1.0,0.0,0.8125)` after accepted upper-a/lower-b resolution work.

## Authority

This task is the sole execution authority for bounded R4 latest upper-a/lower-b policy fixture resolution work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Zero-liquid certification repair accepted.
- Interior-a zero-drift candidate construction accepted.
- Upper-a boundary contract resolution accepted.
- Dual upper-corner boundary closure accepted.
- Intermediate upper-b closure accepted.
- Upper-a/lower-b earlier closure accepted.
- Latest rerun failure classified as a slack lower-b control recomputation gap.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- AGENTS.md
- accepted R2 HJB reports
- R3 KFE reports
- latest R4 rerun failure report
- latest 08125 diagnostic report
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- add bounded upper-a zero-drift + slack lower-b forward controls recomputation candidate construction;
- preserve existing upper-a, lower-b, upper-b and dual contracts;
- add regression test reproducing `(a,b,z)=(1.0,0.0,0.8125)`;
- verify direction, multiplier, complementarity and KKT gates;
- generate implementation evidence report.

## Required scientific checks

Must verify:

- economic equations unchanged;
- transfer mechanism unchanged;
- slack lower-b branch recomputes controls instead of reusing incompatible active multiplier;
- upper-a multiplier contract remains valid;
- no candidate accepted by relaxed tolerance;
- no artificial mobility introduced.

## Forbidden operations

Do not:

- modify fixture parameters;
- change grids;
- change calibration;
- modify economic equations;
- modify generator;
- silently reinterpret truncation;
- add artificial transitions;
- select recurrent classes;
- create invariant mixtures;
- run steady-state solver;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Failure rule

If the latest slack lower-b closure cannot satisfy existing economics and KKT contracts without changing economics, stop and report a scientific blocker.

## Output requirements

Report:

- verdict;
- files read/written;
- implementation changes;
- tests executed;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Next gate candidate

CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN
