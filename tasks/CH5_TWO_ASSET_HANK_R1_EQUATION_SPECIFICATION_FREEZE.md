# CH5 Two-Asset HANK R1 Equation Specification Freeze

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task:

`CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE`

Gate:

`R1_EQUATION_SPECIFICATION_FREEZE`

---

# Objective

Freeze the economic equation specification after dissertation source authority binding.

This gate converts source authority into an explicit reconstruction specification.

This is an equation governance task only.

No implementation is authorized.

---

# Accepted Source Authority

Primary dissertation authority:

`基于异质性新凯恩斯模型的中国经济区域均衡协调发展研究.pdf`

Chapter 5 authority:

- Chapter 5 multi-province HANK model;
- equations (5-1)–(5-3) as two-asset core authority.

Chapter 3 equations may be used only as referenced derivations and must not be silently merged with Chapter 5 authority.

---

# Required Output

Create:

`docs/CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE_REPORT.md`

The report must contain:

1. State variables and ordering contract.
2. Control variables.
3. Asset accounting definition.
4. Household budget constraint authority.
5. HJB equation specification.
6. Generator/operator contract.
7. KFE specification requirements.
8. Boundary condition requirements.
9. MATLAB provenance correspondence boundary.
10. Python reconstruction mapping boundary.
11. Conflict decisions C-01 to C-09.

Each conflict must be classified as:

- MATCH;
- REDESIGN;
- DEFER;
- UNRESOLVED.

---

# Required Conflict Review

Review at minimum:

- tempMat versus dissertation budget equations;
- transfer FOC and adjustment cost scaling;
- alpha parameter interpretation;
- boundary/KKT conditions;
- KFE uniqueness requirements;
- state ordering `(a,b,z)` versus source ordering;
- diffusion versus discretized productivity process;
- Chapter 5 transfer variable scope;
- any MATLAB implementation divergence.

---

# Forbidden Operations

Do NOT:

- implement HJB;
- implement KFE;
- modify solver;
- write Python model code;
- run MATLAB;
- run Python;
- calibrate parameters;
- generate numerical results;
- enter implementation planning beyond specification mapping;
- modify protected dissertation or MATLAB source directories.

---

# Acceptance Criteria

PASS requires:

- economic equation authority frozen;
- unresolved issues explicitly retained;
- implementation boundary documented;
- no scientific claims beyond source specification.

If a core equation authority conflict cannot be classified:

Return:

`BLOCKED_EQUATION_AUTHORITY_CONFLICT_UNRESOLVED`

---

# Next Gate

After acceptance:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_PLANNING`

Implementation remains separately authorized.
