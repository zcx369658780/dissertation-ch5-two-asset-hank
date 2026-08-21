# CH5 Two-Asset HANK R2 HJB Implementation

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION`

Gate:

`R2_HJB_IMPLEMENTATION`

---

# Objective

Implement the first bounded HJB reconstruction slice according to the accepted R1 equation specification and R2 implementation planning contract.

This is the first executable model gate.

Implementation is authorized only within the exact scope defined below.

---

# Required Authority Inputs

Read first:

- `docs/CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE_FINAL_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_PLANNING_REPORT.md`
- R1 C-02/C-05/C-08 conflict resolution report
- dissertation authority binding records

Scientific authority remains:

- state ordering `(a,b,z)`;
- canonical flattening contract;
- controls `(c,l,d)`;
- budget constraint;
- adjustment cost redesign;
- boundary KKT rules;
- productivity diffusion authority;
- shared operator consistency.

---

# Allowed Scope

Implement only the bounded HJB layer.

Allowed:

1. Python model package skeleton required for HJB implementation;
2. HJB module implementation;
3. derivative/upwind implementation;
4. household budget and control evaluation functions;
5. generator construction required by HJB;
6. synthetic small-grid fixtures;
7. unit tests and diagnostics required for HJB correctness.

---

# Required Planning Decisions Before Code Expansion

The implementation report must explicitly record:

- Python version and dependency versions;
- exact created/modified paths;
- initial grid scope;
- productivity-state discretization and endpoint closure;
- update method;
- tolerances;
- failure handling;
- refinement/truncation evidence plan;
- KFE boundary (interface only unless separately authorized).

---

# Forbidden Operations

Do NOT:

- implement stationary KFE solver;
- implement transition solver;
- run full dissertation experiments;
- calibrate final parameters;
- generate Results claims;
- run MATLAB as numerical oracle;
- claim MATLAB/Python parity;
- modify dissertation source files;
- modify legacy MATLAB source directories.

---

# Validation Requirements

Minimum evidence:

- deterministic synthetic fixture;
- operator dimension checks;
- state ordering checks;
- boundary-condition diagnostics;
- residual reporting;
- reproducible test execution.

Engineering tests alone do not establish economic validity.

---

# Acceptance Criteria

PASS requires:

- only authorized paths changed;
- HJB implementation matches frozen specification;
- no KFE/transition scope leakage;
- diagnostics included;
- no unsupported numerical claims.

If scientific authority is insufficient:

Return:

`BLOCKED_R2_HJB_IMPLEMENTATION_SCIENTIFIC_AUTHORITY_GAP`

---

# Next Gate

After independent review:

`CH5_TWO_ASSET_HANK_R3_KFE_IMPLEMENTATION`

KFE implementation requires separate authorization.
