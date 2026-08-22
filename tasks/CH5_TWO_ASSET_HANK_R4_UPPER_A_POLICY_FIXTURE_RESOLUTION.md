# CH5_TWO_ASSET_HANK_R4_UPPER_A_POLICY_FIXTURE_RESOLUTION

## Task

Resolve the R4 frozen fixture upper-a policy-selection failure after the accepted zero-liquid certification and interior-a zero-drift candidate repairs.

## Authority

This task is the sole execution authority for bounded R4 upper-a policy fixture resolution work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Zero-liquid certification repair accepted.
- Interior a-zero-drift candidate construction accepted.
- Frozen R4 rerun failed at upper illiquid asset boundary state `(a,b,z)=(1.0,0,0.8125)`.
- Diagnostic classified blocker as upper computational truncation boundary contract incompatibility.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- R4 policy resolution reports
- R4 upper-a diagnostic report
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- define an explicit upper-a boundary candidate/KKT contract;
- implement bounded upper-a policy construction consistent with frozen economics;
- preserve transfer mechanism and household equations;
- add regression tests reproducing `(a,b,z)=(1.0,0,0.8125)`;
- verify boundary and KKT gates;
- generate implementation evidence report.

## Required scientific checks

The repair must verify:

- frozen fixture remains unchanged;
- upper-a no-outflow rule remains enforced;
- candidate satisfies unchanged economic equations;
- liquid lower-boundary conditions remain valid;
- KKT residual remains within existing gates;
- no candidate is accepted solely by relaxed constraints.

## Forbidden operations

Do not:

- modify fixture parameters;
- change grids;
- change calibration;
- modify economic equations;
- silently alter upper truncation interpretation;
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

If upper-a closure cannot satisfy existing economic, boundary and KKT contracts without changing economics, stop and report a scientific blocker.

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
