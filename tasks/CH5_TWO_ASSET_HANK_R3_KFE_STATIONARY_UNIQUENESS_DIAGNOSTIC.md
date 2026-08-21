# CH5_TWO_ASSET_HANK_R3_KFE_STATIONARY_UNIQUENESS_DIAGNOSTIC

## Task

Diagnose the stationary uniqueness blocker discovered after R3 KFE operator implementation.

## Authority

This task is the sole execution authority for R3 stationary uniqueness diagnostic work.

Current prerequisite:

- R2 HJB implementation rerun accepted.
- R3 KFE operator engineering implementation completed.
- Current blocker: accepted generator contains multiple closed recurrent classes.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE operator implementation report
- current generator, indexing, contracts and KFE interface sources
- CH5 R5 MATLAB-Python parity validation rule if present in live repository

## Allowed operations

Allowed:

- analyze generator graph structure;
- identify recurrent classes;
- inspect communication structure of the accepted generator;
- diagnose whether the issue originates from:
  - fixture design;
  - boundary conditions;
  - missing transitions;
  - generator construction;
  - economic constraints;
- generate a diagnostic evidence report.

## Required scientific checks

The diagnostic must report:

- number of closed recurrent classes;
- states belonging to each class;
- transition connectivity evidence;
- whether non-ergodicity is caused by implementation or by current economic fixture;
- recommended next scientific decision point.

## Forbidden operations

Do not:

- select an arbitrary recurrent class;
- create an invariant mixture manually;
- pin a row to force uniqueness;
- add artificial transition probabilities;
- modify calibration;
- modify economic equations;
- modify policy functions;
- modify generator implementation;
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
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Next gate candidate

CH5_TWO_ASSET_HANK_R3_KFE_STATIONARY_UNIQUENESS_RESOLUTION
