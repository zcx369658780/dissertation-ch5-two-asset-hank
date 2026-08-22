# CH5_TWO_ASSET_HANK_R4_POLICY_FIXTURE_RESOLUTION

## Task

Resolve the R4 frozen fixture zero-drift candidate certification defect after policy compatibility diagnosis.

## Authority

This task is the sole execution authority for bounded R4 policy fixture resolution work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- R4 steady-state implementation failed closed due to zero-drift candidate certification mismatch.
- Diagnosis classified the blocker as numerical contract mismatch, not fixture economics failure.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- R4 frozen fixture compatibility diagnostic report
- current HJB, policy, derivative, contracts and economics sources

## Allowed operations

Allowed:

- define a shared zero-drift candidate certification contract;
- implement bounded numerical consistency correction;
- add regression tests reproducing the certified candidate;
- verify that economic, boundary and KKT conditions remain unchanged;
- generate implementation evidence report.

## Required scientific checks

The repair must verify:

- frozen R4 fixture remains unchanged;
- economic equations remain unchanged;
- zero-drift candidate remains the same economic candidate;
- KKT residual remains within existing gate;
- boundary conditions remain unchanged;
- no candidate is accepted solely by relaxed economic constraints.

## Forbidden operations

Do not:

- modify fixture parameters;
- modify grids;
- change calibration;
- modify economic equations;
- modify policy logic beyond certification contract;
- alter generator construction;
- add artificial transitions;
- select recurrent classes;
- create invariant mixtures;
- run steady state solver;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Failure rule

If the certified zero-drift candidate cannot pass without changing economics, stop and report a scientific blocker. Do not tune thresholds after observing results.

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
