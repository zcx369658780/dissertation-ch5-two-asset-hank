# CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION

## Task

Authorize steady-state preparation only after R3 stationary uniqueness resolution.

## Authority

This task is the sole execution authority for R4 steady-state authorization work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- Current synthetic fixture non-ergodicity diagnosed.
- R3 resolution decision requires a redesigned stationary-validation fixture before any steady-state solve.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE operator implementation report
- R3 stationary uniqueness diagnostic report
- R3 stationary uniqueness resolution report
- current generator, indexing, contracts, policy and KFE sources

## Allowed operations

Allowed:

- freeze a new stationary-validation fixture specification;
- define test-only fixture parameters before solving;
- define required interior illiquid-asset connectivity conditions;
- verify that the proposed fixture can support a unique stationary distribution;
- prepare a steady-state authorization recommendation report.

## Required scientific checks

The fixture proposal must define:

- interior a-node existence;
- endogenous connectivity through accepted economic mechanisms;
- unique closed recurrent class requirement;
- left nullity target equal to one;
- compatibility with existing HJB/KKT/generator/truncation gates.

## Forbidden operations

Do not:

- solve steady state before fixture authorization;
- choose arbitrary recurrent class;
- construct invariant mixture manually;
- add artificial transition probabilities;
- modify economic equations silently;
- silently modify calibration;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Output requirements

Report:

- verdict;
- files read/written;
- proposed fixture design;
- scientific rationale;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Next gate candidate

CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION
