# CH5_TWO_ASSET_HANK_R3_KFE_STATIONARY_UNIQUENESS_RESOLUTION

## Task

Resolve the scientific decision after R3 stationary uniqueness diagnostic.

## Authority

This task is the sole execution authority for stationary uniqueness resolution work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator implementation engineering pass accepted.
- Current fixture is non-ergodic because accepted policy generates multiple closed recurrent classes.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE operator implementation report
- R3 stationary uniqueness diagnostic report
- current generator, indexing, contracts, policy and KFE sources

## Allowed operations

Allowed:

- analyze scientifically valid resolution options;
- determine whether current fixture should be redesigned;
- identify required economic mechanism for illiquid-asset connectivity;
- document whether a unique stationary distribution is required for the final model;
- generate a resolution recommendation report.

## Forbidden operations

Do not:

- select an arbitrary recurrent class;
- create an invariant mixture without scientific authority;
- pin rows to force uniqueness;
- add artificial transition probabilities;
- silently modify calibration;
- silently modify policy functions;
- silently modify generator implementation;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Output requirements

Report:

- verdict;
- files read/written;
- scientific diagnosis;
- considered options;
- recommended next gate;
- forbidden-operation check;
- git status;
- acceptance level.

## Next gate candidate

CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION
