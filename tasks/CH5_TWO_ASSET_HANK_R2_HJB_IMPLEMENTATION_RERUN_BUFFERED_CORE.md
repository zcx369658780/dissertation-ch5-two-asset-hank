# CH5 Two-Asset HANK R2 HJB Implementation Rerun Buffered Core

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_RERUN_BUFFERED_CORE`

Gate:

`R2_HJB_IMPLEMENTATION_RERUN_BUFFERED_CORE`

---

# Objective

Re-run the bounded R2 HJB implementation after the truncation protocol review froze a revised buffered-core evaluation contract.

This task authorizes only the existing R2 HJB scope under the revised truncation geometry.

No KFE expansion is authorized.

---

# Required Authority Inputs

Read first:

- `docs/CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE_FINAL_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_PLANNING_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_NUMERICAL_AND_KKT_AUTHORITY_COMPLETION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_TRUNCATION_PROTOCOL_REVIEW_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_RERUN_REPORT.md`

Scientific authority remains frozen:

- state ordering `(a,b,z)`;
- canonical flattening;
- controls `(c,l,d)`;
- KKT/complementarity diagnostics;
- productivity discretization contract;
- buffered-core truncation protocol;
- shared HJB/generator consistency.

---

# Allowed Scope

Only bounded R2 HJB rerun:

Allowed:

- apply accepted buffered-core evaluation protocol;
- update diagnostics required by revised truncation contract;
- update tests/evidence reporting;
- produce rerun evidence report.

---

# Required Validation

Evidence must include:

- Buffer 2 / Buffer 3 core comparison on identical `[0.5,1.5]` coordinates;
- candidate identifier consistency;
- tie exception reporting if applicable;
- productivity diagnostics;
- KKT/complementarity residual diagnostics;
- true HJB residual reporting;
- deterministic reproducibility.

---

# Forbidden Operations

Do NOT:

- implement stationary KFE solver;
- implement transition solver;
- widen domains beyond frozen family;
- change spacing to force acceptance;
- tune parameters to force PASS;
- run dissertation experiments;
- calibrate final parameters;
- claim MATLAB/Python parity;
- modify dissertation sources;
- modify legacy MATLAB sources.

---

# Acceptance Criteria

PASS requires:

- revised buffered-core protocol followed exactly;
- truncation acceptance passed under frozen thresholds;
- no scientific authority gaps;
- no KFE scope leakage.

If unresolved:

Return:

`BLOCKED_R2_HJB_IMPLEMENTATION_TRUNCATION_ACCEPTANCE_FAILED`

---

# Next Gate

After independent acceptance:

`CH5_TWO_ASSET_HANK_R3_KFE_IMPLEMENTATION`

KFE implementation requires separate authorization.
