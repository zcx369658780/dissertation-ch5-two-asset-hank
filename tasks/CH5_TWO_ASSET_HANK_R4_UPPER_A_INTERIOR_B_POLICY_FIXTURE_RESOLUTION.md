# CH5_TWO_ASSET_HANK_R4_UPPER_A_INTERIOR_B_POLICY_FIXTURE_RESOLUTION

## Task

Resolve the upper-a/interior-b policy-selection blocker at `(a,b,z)=(1.0,2.5,0.8125)` after accepted zero-liquid certification, interior-a zero-drift construction, upper-a boundary contract resolution, dual upper-corner boundary closure resolution, intermediate upper-b closure resolution, and upper-a/lower-b joint zero-drift closure resolution.

## Authority

This task is the sole execution authority for bounded R4 upper-a/interior-b policy fixture resolution work.

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
- Upper-a/lower-b joint zero-drift closure accepted.
- Upper-a/interior-b diagnostic classified a joint zero-drift candidate construction gap.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- R4 policy fixture resolution reports
- upper-a/interior-b diagnostic report
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- add bounded upper-a zero-drift + interior-b zero-direction shadow/control joint candidate construction;
- preserve existing lower-boundary, upper-a, upper-b, dual-upper and upper-a/lower-b contracts;
- add regression tests reproducing `(a,b,z)=(1.0,2.5,0.8125)`;
- verify direction, boundary, multiplier, complementarity and KKT gates;
- generate implementation evidence report.

## Required scientific checks

The resolution must verify:

- economic equations unchanged;
- transfer mechanism unchanged;
- interior-b controls follow existing KKT logic;
- upper-a multiplier contract remains valid;
- no candidate is accepted solely by relaxed tolerance;
- no artificial mobility is introduced.

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

If the joint upper-a/interior-b closure cannot satisfy existing economic, boundary and KKT contracts without changing economics, stop and report a scientific blocker.

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
