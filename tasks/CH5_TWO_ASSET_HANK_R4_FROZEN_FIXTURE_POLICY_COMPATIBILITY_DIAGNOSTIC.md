# CH5_TWO_ASSET_HANK_R4_FROZEN_FIXTURE_POLICY_COMPATIBILITY_DIAGNOSTIC

## Task

Diagnose why the pre-authorized R4 steady-state fixture fails at the first HJB policy-selection gate.

## Authority

This task is the sole execution authority for R4 frozen fixture policy compatibility diagnostic work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- R4 steady-state implementation failed closed because no admissible self-consistent candidate exists at one frozen state.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE operator implementation report
- R3 stationary uniqueness diagnostic report
- R3 stationary uniqueness resolution report
- R4 steady-state authorization report
- R4 implementation failure evidence
- current HJB, policy, generator, indexing, contracts and economics sources

## Allowed operations

Allowed:

- diagnose policy-selection failure at the frozen state;
- inspect admissible candidate generation;
- classify whether the failure comes from:
  - fixture-policy incompatibility;
  - boundary constraints;
  - candidate construction;
  - existing economic restrictions;
- generate a diagnostic evidence report.

## Required scientific checks

The diagnostic must report:

- failing state and economic coordinates;
- candidate availability status;
- violated constraints or missing admissible conditions;
- whether the issue is fixture design or implementation defect;
- recommended next scientific decision point.

## Forbidden operations

Do not:

- modify fixture parameters;
- rerun with changed grids;
- change calibration;
- modify economic equations;
- modify policy functions;
- modify generator;
- relax constraints silently;
- create artificial transitions;
- solve steady state;
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
- scientific diagnosis;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Next gate candidate

CH5_TWO_ASSET_HANK_R4_POLICY_FIXTURE_RESOLUTION
