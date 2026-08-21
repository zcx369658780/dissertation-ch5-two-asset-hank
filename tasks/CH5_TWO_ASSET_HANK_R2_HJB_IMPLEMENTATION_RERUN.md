# CH5 Two-Asset HANK R2 HJB Implementation Rerun

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_RERUN`

Gate:

`R2_HJB_IMPLEMENTATION_RERUN`

---

# Objective

Re-run the bounded HJB implementation review after completion of the missing numerical and KKT scientific authority contracts.

This task authorizes only the previously bounded R2 HJB scope.

No expansion to KFE or full model experiments is authorized.

---

# Required Authority Inputs

Read first:

- `docs/CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE_FINAL_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_PLANNING_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_NUMERICAL_AND_KKT_AUTHORITY_COMPLETION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_REPORT.md`

Scientific authority remains frozen:

- state ordering `(a,b,z)`;
- canonical flattening;
- controls `(c,l,d)`;
- budget constraint;
- adjustment cost;
- boundary KKT/complementarity contract;
- productivity discretization contract;
- shared HJB/generator consistency.

---

# Allowed Scope

Only bounded R2 HJB implementation rerun:

Allowed:

- refine existing HJB implementation according to accepted contracts;
- update diagnostics required by frozen KKT/productivity contracts;
- update tests for accepted scientific contracts;
- produce implementation evidence report.

---

# Required Validation

Evidence must include:

- productivity discretization diagnostics;
- z-grid/refinement evidence;
- truncation evidence according to frozen protocol;
- KKT/complementarity residual diagnostics;
- HJB residual reporting;
- deterministic reproducible tests.

Engineering tests alone do not establish economic validity.

---

# Forbidden Operations

Do NOT:

- implement stationary KFE solver;
- implement transition solver;
- run dissertation experiments;
- calibrate final parameters;
- generate Results claims;
- claim MATLAB/Python parity;
- modify dissertation source files;
- modify legacy MATLAB source directories.

---

# Acceptance Criteria

PASS requires:

- implementation follows frozen R1/R2 authority;
- KKT and productivity contracts are evidenced;
- no scientific authority gaps remain;
- no scope leakage into KFE.

If unresolved:

Return:

`BLOCKED_R2_HJB_IMPLEMENTATION_SCIENTIFIC_AUTHORITY_GAP`

---

# Next Gate

After independent acceptance:

`CH5_TWO_ASSET_HANK_R3_KFE_IMPLEMENTATION`

KFE implementation requires separate authorization.
