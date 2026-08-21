# CH5 Two-Asset HANK R2 Productivity State Domain and Boundary Law Review

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task:

`CH5_TWO_ASSET_HANK_R2_PRODUCTIVITY_STATE_DOMAIN_AND_BOUNDARY_LAW_REVIEW`

Gate:

`R2_PRODUCTIVITY_STATE_DOMAIN_AND_BOUNDARY_LAW_REVIEW`

---

# Objective

Review the compatibility between the frozen productivity diffusion authority, positive synthetic z-domain construction, and computational boundary law after repeated R2 HJB truncation acceptance failures.

This is a scientific authority review task.

It does NOT authorize HJB implementation changes or KFE implementation.

---

# Current Scientific Question

R2 HJB reruns have passed:

- productivity refinement diagnostics;
- KKT/complementarity diagnostics;
- true HJB residual convergence;
- deterministic reproducibility.

However, buffered-core truncation remains highly sensitive to z-domain expansion.

The review must determine whether the issue is:

1. insufficient computational domain support;
2. incompatibility between positive synthetic domain and mean-reverting diffusion authority;
3. endpoint closure interpretation problem;
4. another unresolved scientific contract.

---

# Required Output

Create:

`docs/CH5_TWO_ASSET_HANK_R2_PRODUCTIVITY_STATE_DOMAIN_AND_BOUNDARY_LAW_REVIEW_REPORT.md`

The report must freeze:

1. economic interpretation of productivity state support;
2. relationship between continuous diffusion and computational truncation;
3. endpoint closure role and limitations;
4. authorized z-domain family for future R2 rerun;
5. acceptance criteria impact;
6. whether equation authority changes are required.

---

# Required Inputs

Read:

- `docs/CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE_FINAL_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_NUMERICAL_AND_KKT_AUTHORITY_COMPLETION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_TRUNCATION_PROTOCOL_REVIEW_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_RERUN_BUFFERED_CORE_REPORT.md`

---

# Allowed Scope

Allowed:

- scientific interpretation review;
- numerical protocol specification;
- documentation only.

---

# Forbidden Operations

Do NOT:

- modify HJB implementation;
- modify KFE implementation;
- tune calibration parameters;
- relax acceptance thresholds without scientific justification;
- run dissertation experiments;
- modify dissertation sources;
- modify MATLAB sources.

---

# Acceptance Criteria

PASS requires:

- truncation failure interpretation resolved;
- z-domain and boundary law decision documented;
- future R2 rerun acceptance contract frozen;
- no unresolved scientific authority gaps.

If unresolved:

Return:

`BLOCKED_R2_PRODUCTIVITY_DOMAIN_AUTHORITY_UNRESOLVED`

---

# Next Gate

After acceptance:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_RERUN`

R3 KFE remains unauthorized.
