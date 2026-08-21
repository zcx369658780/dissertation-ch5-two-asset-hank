# CH5 Two-Asset HANK R2 HJB Implementation Planning

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_PLANNING`

Gate:

`R2_HJB_IMPLEMENTATION_PLANNING`

---

# Objective

Translate the frozen R1 equation specification into an implementation planning contract for the future HJB reconstruction.

This is a planning-only gate.

No model implementation is authorized.

---

# Accepted Context

Required inputs:

- `docs/CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE_FINAL_REPORT.md`
- R1 C-02/C-05/C-08 conflict resolution report
- dissertation equation authority binding records

Frozen scientific authority:

- state ordering `(a,b,z)` with explicit flattening contract;
- controls `(c,l,d)`;
- asset accounting and budget constraint;
- adjustment technology and boundary KKT;
- productivity diffusion authority;
- shared HJB/generator/KFE operator requirement.

---

# Required Output

Create:

`docs/CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_PLANNING_REPORT.md`

The report must define:

1. HJB module architecture;
2. variable and array contracts;
3. derivative/upwinding implementation plan;
4. generator construction plan;
5. KFE dependency plan;
6. MATLAB-to-Python correspondence boundary;
7. testing and diagnostic requirements;
8. implementation order and blockers.

---

# Forbidden Operations

Do NOT:

- write HJB code;
- write KFE code;
- modify solver implementation;
- run MATLAB;
- run Python model;
- calibrate parameters;
- generate numerical results;
- modify dissertation source;
- modify MATLAB source directories.

---

# Acceptance Criteria

PASS requires:

- planning boundary clearly separated from implementation;
- all R1 frozen equations mapped to future modules;
- no scientific authority changes;
- no executable model artifacts created.

If equation authority is insufficient:

Return:

`BLOCKED_R2_HJB_PLANNING_EQUATION_AUTHORITY_GAP`

---

# Next Gate

After independent acceptance:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION`

Implementation requires separate authorization.
