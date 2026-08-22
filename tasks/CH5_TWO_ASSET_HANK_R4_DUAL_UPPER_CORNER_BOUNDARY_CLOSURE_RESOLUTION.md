# CH5_TWO_ASSET_HANK_R4_DUAL_UPPER_CORNER_BOUNDARY_CLOSURE_RESOLUTION

## Task

Resolve the final R4 HJB policy-selection blocker at the joint upper-a/upper-b corner after accepted zero-liquid certification, interior-a zero-drift construction, and upper-a boundary contract repairs.

## Authority

This task is the sole execution authority for bounded R4 dual upper-corner boundary closure resolution work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Zero-liquid certification repair accepted.
- Interior a-zero-drift candidate construction accepted.
- Upper-a policy boundary contract resolution accepted.
- Final R4 rerun failed at `(a,b,z)=(1.0,5.0,1.5)`.
- Diagnostic classified blocker as missing joint upper-a/upper-b boundary closure contract.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- R4 policy fixture resolution reports
- final R4 HJB failure diagnostic report
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- define an explicit upper-b boundary contract if scientifically justified;
- implement bounded dual upper-corner policy construction consistent with frozen economics;
- preserve household equations and transfer mechanism;
- add regression tests reproducing `(a,b,z)=(1.0,5.0,1.5)`;
- verify direction, boundary, multiplier, complementarity and KKT gates;
- generate implementation evidence report.

## Required scientific checks

The resolution must verify:

- upper-a contract remains unchanged;
- any upper-b closure follows explicit KKT/complementarity logic;
- no candidate is accepted solely by relaxed tolerance;
- economic equations remain unchanged;
- no artificial mobility is introduced.

## Forbidden operations

Do not:

- modify fixture parameters;
- change grids;
- change calibration;
- modify economic equations;
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

If the upper-corner closure cannot satisfy existing economic, boundary and KKT contracts without changing economics, stop and report a scientific blocker.

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
