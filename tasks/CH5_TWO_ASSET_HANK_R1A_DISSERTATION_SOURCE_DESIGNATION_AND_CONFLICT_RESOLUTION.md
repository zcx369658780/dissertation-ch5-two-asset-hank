# CH5 Two-Asset HANK R1A Dissertation Source Designation and Conflict Resolution

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Project:

Chapter 5 Two-Asset HANK Reconstruction

Gate:

`R1A_SOURCE_PROVENANCE_BINDING`

Task:

`CH5_TWO_ASSET_HANK_R1A_DISSERTATION_SOURCE_DESIGNATION_AND_CONFLICT_RESOLUTION`

---

# Objective

Bind the dissertation equation authority for the two-asset HANK reconstruction.

This gate is source authority resolution only.

It does not authorize model implementation.

Goals:

1. identify dissertation source authority;
2. record version, pages and equation locations;
3. compare dissertation equations with MATLAB provenance;
4. classify conflicts before equation freeze.

---

# Current Accepted Context

Accepted:

- R0 Model Constitution;
- DSH forensic audit;
- HYBRID_RECONSTRUCTION_REQUIRED route;
- R1 operator contract partial freeze;
- MATLAB provenance manifest.

MATLAB provenance candidate:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

MATLAB source is provenance evidence only. It is not automatically the economic authority.

---

# Allowed Operations

Allowed:

- identify dissertation file;
- record version/date;
- record equation locations;
- create equation authority manifest;
- compare dissertation equations with MATLAB variables/modules;
- create conflict classification report.

Conflict categories:

- MATCH;
- IMPLEMENTATION_EXTENSION;
- LEGACY_IMPLEMENTATION_DIFFERENCE;
- UNRESOLVED.

---

# Forbidden Operations

Do NOT:

- implement HJB;
- implement KFE;
- modify solver;
- modify MATLAB files;
- run MATLAB;
- run Python model code;
- calibrate parameters;
- generate numerical output;
- write Results claims;
- infer dissertation equations from generic HANK literature;
- infer economic authority from MATLAB code alone.

---

# Required Evidence

Create a text-first report containing:

1. dissertation source identity;
2. source provenance/hash if available;
3. equation inventory;
4. variable mapping;
5. MATLAB correspondence map;
6. conflict table;
7. unresolved authority questions;
8. recommended next gate.

---

# Acceptance Criteria

PASS requires:

- dissertation source explicitly designated;
- equation authority recorded;
- MATLAB source classified relative to dissertation;
- unresolved questions listed.

If source is unavailable, return:

`BLOCKED_DISSERTATION_SOURCE_AUTHORITY_NOT_AVAILABLE`

Do not continue to implementation.

---

# Expected Next Gate

`CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE`

Only after equation authority is frozen may HJB/KFE implementation planning begin.
