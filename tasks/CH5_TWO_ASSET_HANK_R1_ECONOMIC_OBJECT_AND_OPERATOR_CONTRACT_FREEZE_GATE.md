# CH5_TWO_ASSET_HANK_R1_ECONOMIC_OBJECT_AND_OPERATOR_CONTRACT_FREEZE_GATE

Repository:

zcx369658780/dissertation-ch5-two-asset-hank

Stage:

R1 Scientific Specification Freeze

## Objective

Freeze the economic object and numerical operator contracts before any two-asset HANK implementation.

This is NOT a coding task.

No solver implementation is authorized.

## Required Freeze Items

### 1. Economic object

Freeze:

- household state variables;
- asset meanings;
- controls;
- budget constraint;
- adjustment cost specification;
- income/productivity process.

Required household state:

(a,b,z)

where:

- a = illiquid asset;
- b = liquid asset;
- z = productivity state.

## 2. Legacy MATLAB migration mapping

Create a retain/redesign/drop/unresolved map.

MATLAB is economic provenance, not numerical oracle.

## 3. State indexing contract

Freeze explicitly:

- state ordering;
- flattening convention;
- array layout;
- matrix ordering.

Language default memory ordering must not determine economics.

## 4. HJB contract

Freeze:

- value function state;
- controls;
- drift equations;
- Hamiltonian construction;
- policy candidate selection;
- upwind rules;
- boundary/KKT conditions.

## 5. Generator contract

Freeze:

G = G_a + G_b + G_z

The same operator must support:

- HJB;
- KFE.

## 6. KFE contract

Freeze:

- stationary equation;
- mass normalization;
- positivity checks;
- uniqueness diagnostics.

## 7. Parity framework

Define acceptance layers:

Structural parity:
- economic object equivalence.

Algorithmic parity:
- solver/operator equivalence.

Numerical parity:
- residuals and output comparison.

## 8. MATLAB-Python comparison plan

After HA module implementation, establish manual comparison between MATLAB and Python outputs.

Comparison must include:

- policy functions;
- distributions;
- asset aggregates;
- residual diagnostics;
- steady-state quantities.

No claim of parity before comparison evidence.

## Forbidden Operations

Do not:

- implement code;
- modify solver;
- run HJB/KFE;
- run MATLAB;
- calibrate parameters;
- create Results claims.

## Output

Produce:

- Economic Object Contract;
- Operator Contract;
- MATLAB Migration Map;
- Validation Plan.

Terminal classification:

- CH5_TWO_ASSET_HANK_R1_FREEZE_COMPLETE
- CH5_TWO_ASSET_HANK_R1_BLOCKED_MISSING_SPECIFICATION
