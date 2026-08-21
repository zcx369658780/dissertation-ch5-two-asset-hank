# CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION

## Task

Implement steady-state computation only after the accepted R4 stationary-validation fixture authorization.

## Authority

This task is the sole execution authority for R4 steady-state implementation work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization completed with frozen fixture:
  `R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1`.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE operator implementation report
- R3 stationary uniqueness diagnostic report
- R3 stationary uniqueness resolution report
- R4 steady-state authorization report
- current HJB, generator, indexing, contracts, policy and KFE sources

## Frozen fixture requirement

Execute only the pre-authorized fixture.

Do not change:

- a grid;
- b grid;
- z grid;
- productivity boundary;
- test-only parameters;
- transfer mechanism;
- calibration values.

## Allowed operations

Allowed:

- run steady-state solver using the frozen fixture;
- connect accepted HJB, generator and KFE components;
- verify stationary distribution;
- verify aggregate moments;
- generate steady-state evidence report.

## Required scientific checks

Must verify:

- unique closed recurrent class;
- left nullity equal to one;
- endogenous illiquid-asset connectivity;
- stationary KFE residual;
- normalization;
- non-negative mass;
- mass/density consistency;
- HJB/KKT/generator/truncation compatibility;
- report synthetic A_hh and B_hh.

## Forbidden operations

Do not:

- tune fixture parameters after observing results;
- change calibration;
- modify economic equations;
- modify policy functions silently;
- modify generator silently;
- select recurrent class;
- create invariant mixture manually;
- add artificial transitions;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Failure rule

Any failure in residual, connectivity, uniqueness, truncation or accounting checks must stop execution. No same-task parameter adjustment is allowed.

## Output requirements

Report:

- verdict;
- files read/written;
- tests executed;
- steady-state diagnostics;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Next gate candidate

CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE
