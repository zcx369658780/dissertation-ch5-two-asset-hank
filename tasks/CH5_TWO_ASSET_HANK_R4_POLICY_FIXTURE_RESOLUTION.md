# CH5_TWO_ASSET_HANK_R4_POLICY_FIXTURE_RESOLUTION

## Task

Resolve the second R4 frozen fixture policy-selection failure caused by missing interior a-direction zero-drift candidate construction.

## Authority

This task is the sole execution authority for bounded R4 policy fixture resolution work.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Zero-drift certification repair accepted.
- Second R4 rerun failed at crossing-upwind state `(a,b,z)=(0.5,0,0.75)`.
- Diagnostic classified blocker as missing interior a-zero-drift candidate construction.

## Read first

- project_rules/PROJECT_RULE_INDEX_CURRENT.md
- accepted R2 HJB reports
- R3 KFE reports
- R4 fixture authorization report
- R4 policy resolution report
- R4 second policy-selection diagnostic report
- current HJB, policy, derivative, boundary, contracts and economics sources

## Allowed operations

Allowed:

- add bounded interior a-direction zero-drift candidate construction;
- preserve existing economic equations;
- preserve transfer mechanism;
- preserve existing certification contracts;
- add regression tests reproducing `(a,b,z)=(0.5,0,0.75)`;
- verify boundary and KKT gates;
- generate implementation evidence report.

## Required scientific checks

The repair must verify:

- candidate is generated from unchanged household equations;
- zero-a-drift condition is endogenous:
  `mu_a = r_a*a + d = 0`;
- liquid drift and boundary conditions remain valid;
- KKT residual remains within existing gate;
- previous zero-liquid certification remains unchanged;
- no artificial transition or regularization is introduced.

## Forbidden operations

Do not:

- modify fixture parameters;
- change grids;
- change calibration;
- modify economic equations;
- relax constraints;
- force candidate acceptance;
- modify generator;
- select recurrent classes;
- create invariant mixtures;
- run steady state solver;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Failure rule

If the candidate cannot satisfy existing economic, boundary and KKT contracts without changing economics, stop and report a scientific blocker.

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
