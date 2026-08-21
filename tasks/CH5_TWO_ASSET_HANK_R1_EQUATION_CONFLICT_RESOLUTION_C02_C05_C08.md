# CH5 Two-Asset HANK R1 Equation Conflict Resolution C02 C05 C08

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task:

`CH5_TWO_ASSET_HANK_R1_EQUATION_CONFLICT_RESOLUTION_C02_C05_C08`

Gate:

`R1_EQUATION_AUTHORITY_CONFLICT_RESOLUTION`

---

# Objective

Resolve the remaining scientific equation authority conflicts identified during R1 Equation Specification Freeze.

This is a scientific specification resolution task only.

No implementation is authorized.

The purpose is to convert unresolved equation authority items into explicit decisions before HJB/KFE reconstruction planning.

---

# Current Accepted Context

Accepted:

- dissertation source authority binding;
- Chapter 5 equations (5-1)-(5-3) as two-asset core authority;
- R1 equation specification partial freeze.

Current unresolved conflicts:

- C-02: adjustment cost and transfer FOC;
- C-05: boundary KKT and admissible control set;
- C-08: productivity process representation.

---

# Required Resolution Scope

## C-02 Adjustment Technology / Transfer FOC

Determine and document:

- adjustment cost definition chi(d,a);
- transfer direction convention;
- optimality condition authority;
- scaling consistency between dissertation equations and MATLAB provenance;
- whether MATLAB implementation is MATCH, REDESIGN, DEFER, or UNRESOLVED.


## C-05 Boundary KKT / Admissible Controls

Determine and document:

- asset lower bounds;
- borrowing constraints;
- admissible control set;
- KKT conditions;
- boundary treatment requirements for future HJB/KFE implementation.


## C-08 Productivity Process

Determine and document:

- dissertation productivity process authority;
- diffusion interpretation;
- MATLAB discrete Q_z interpretation;
- Python reconstruction mapping boundary;
- whether discretization is economic authority or numerical implementation detail.

---

# Required Output

Create:

`docs/CH5_TWO_ASSET_HANK_R1_C02_C05_C08_CONFLICT_RESOLUTION_REPORT.md`

Report must include:

1. conflict-by-conflict decision table;
2. supporting dissertation authority;
3. MATLAB correspondence boundary;
4. unresolved items if any;
5. implications for later HJB/KFE specification;
6. recommendation for rerunning R1 freeze.

Allowed classifications:

- MATCH;
- REDESIGN;
- DEFER;
- UNRESOLVED.

---

# Forbidden Operations

Do NOT:

- implement HJB;
- implement KFE;
- modify solver;
- write Python model code;
- run MATLAB;
- run Python model;
- calibrate parameters;
- generate numerical results;
- modify dissertation source files;
- modify MATLAB source directories;
- enter R2 implementation planning.

---

# Protected Sources

STRICT READ ONLY:

- `D:\Articles\2023年9月25日 博士毕业论文TEX稿件`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Only read, hash, and evidence extraction are allowed.

---

# Acceptance Criteria

PASS requires:

- C-02/C-05/C-08 decisions documented;
- economic authority separated from numerical implementation;
- unresolved items explicitly retained if evidence is insufficient.

If any conflict remains blocking:

Return:

`BLOCKED_EQUATION_AUTHORITY_CONFLICT_UNRESOLVED`

---

# Next Gate

After successful resolution and R1 freeze rerun:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_PLANNING`
