# CH5_TWO_ASSET_HANK_R3_KFE_OPERATOR_IMPLEMENTATION

## Task

Implement the R3 KFE operator layer after accepted R2 HJB implementation rerun.

## Authority

This task is the sole execution authority for R3 KFE operator work.

Current prerequisite:

- R2 HJB implementation rerun accepted.
- Productivity boundary law accepted.
- HJB boundary/KKT diagnostics accepted.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- current HJB implementation reports
- accepted R2 reports
- CH5_TWO_ASSET_HANK_R5 MATLAB-Python parity rules

## Allowed operations

Allowed:

- implement stationary KFE operator using accepted generator contract;
- connect existing policy drift and generator interfaces;
- add KFE operator diagnostics;
- add tests for:
  - transpose consistency;
  - mass conservation;
  - non-negativity;
  - stationary residual;
- generate evidence report.

## Required scientific checks

The implementation must verify:

- KFE uses the accepted generator/operator convention;
- stationary distribution satisfies the implemented operator condition;
- total probability mass is preserved;
- distribution remains non-negative;
- no drift or asset-accounting convention is silently changed.

## Forbidden operations

Do not:

- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- modify calibration;
- modify MATLAB sources;
- claim MATLAB-Python parity;
- write Results prose;
- execute R4H legacy route;
- create R4/R5 successor tasks.

## Output requirements

Report:

- verdict;
- files read/written;
- tests executed;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Next gate candidate

CH5_TWO_ASSET_HANK_R3_KFE_OPERATOR_ACCEPTANCE
