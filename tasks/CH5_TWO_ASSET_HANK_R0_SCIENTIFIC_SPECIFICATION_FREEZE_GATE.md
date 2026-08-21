# CH5_TWO_ASSET_HANK_R0_SCIENTIFIC_SPECIFICATION_FREEZE_GATE

## Objective

Freeze the scientific identity and scope of the new Dissertation Chapter 5 two-asset HA/HANK reconstruction before implementation.

This is a specification task, not a coding task.

## Required Decisions

Freeze:

1. Economic object:

- household state variables;
- asset definitions;
- productivity states;
- controls;
- transition semantics.

2. Household problem:

- HJB formulation;
- constraints;
- adjustment costs;
- boundary conditions.

3. Distribution block:

- generator construction;
- KFE formulation;
- stationary distribution requirements.

4. Asset accounting:

- liquid asset accounting;
- illiquid asset accounting;
- market clearing identities.

5. Reconstruction strategy:

Classify legacy elements as:

- retain;
- redesign;
- drop;
- unresolved.

## Forbidden Operations

Do not:

- implement solver code;
- translate MATLAB line-by-line;
- run full model;
- generate Results;
- claim MATLAB/Python parity.

## Output

Create a scientific specification report containing:

- model identity;
- equations to be reconstructed;
- unresolved decisions;
- implementation prerequisites;
- next recommended gate.

## Terminal Classification

Use one:

- CH5_TWO_ASSET_HANK_R0_COMPLETE_READY_FOR_IMPLEMENTATION_PLANNING
- CH5_TWO_ASSET_HANK_R0_BLOCKED_MISSING_SPECIFICATION
