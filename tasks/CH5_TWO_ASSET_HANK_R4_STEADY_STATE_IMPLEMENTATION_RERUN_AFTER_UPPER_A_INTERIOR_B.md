# CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_UPPER_A_INTERIOR_B

## Task

Re-run the R4 frozen steady-state implementation after accepted upper-a/interior-b joint zero-drift closure resolution.

## Authority

This task is the sole execution authority for the bounded R4 frozen fixture rerun.

## Current state

- R2 HJB implementation accepted.
- R3 KFE operator engineering implementation accepted.
- R3 stationary uniqueness resolution accepted.
- R4 fixture authorization accepted.
- Zero-liquid certification repair accepted.
- Interior a-zero-drift candidate construction accepted.
- Upper-a policy boundary contract resolution accepted.
- Dual upper-corner boundary closure accepted.
- Intermediate upper-b interior-a zero-drift closure accepted.
- Upper-a/lower-b joint zero-drift closure accepted.
- Upper-a/interior-b joint zero-drift closure accepted.

## Frozen execution requirement

Execute exactly:

`R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1`

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

- run frozen steady-state implementation once;
- connect accepted HJB, generator and KFE components;
- verify stationary distribution;
- verify aggregate moments;
- generate evidence report.

## Required scientific checks

Must verify:

- HJB completion;
- endogenous illiquid-asset connectivity;
- unique closed recurrent class;
- left nullity equal to one;
- stationary KFE residual;
- normalization;
- non-negative mass;
- mass/density consistency;
- HJB/KKT/generator/truncation compatibility;
- synthetic A_hh and B_hh.

## Forbidden operations

Do not:

- tune parameters after observing results;
- change fixture values;
- modify economic equations;
- modify accepted policy repairs outside their contracts;
- modify generator silently;
- select recurrent classes;
- create invariant mixtures;
- add artificial transitions;
- implement transition solver;
- implement AR(1) shock engine;
- run IRF experiments;
- write Results prose;
- claim MATLAB-Python parity.

## Failure rule

Any failure in residual, connectivity, uniqueness, truncation or accounting checks must stop execution. No same-task adjustment is allowed.

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
