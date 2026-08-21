# CH5 Two-Asset HANK R2 Numerical and KKT Authority Completion

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task:

`CH5_TWO_ASSET_HANK_R2_HJB_NUMERICAL_AND_KKT_AUTHORITY_COMPLETION`

Gate:

`R2_HJB_NUMERICAL_AND_KKT_AUTHORITY_COMPLETION`

---

# Objective

Complete the missing scientific authority contracts identified during R2 HJB implementation review.

This is an authority completion and contract-freeze task.

It does NOT authorize expansion of HJB implementation scope.

---

# Current Blocker

R2 prototype cannot be accepted because two scientific contracts remain incomplete:

1. Productivity-state discretization:
   - exact discretization formula;
   - fixture domain;
   - grid refinement protocol;
   - truncation acceptance thresholds.

2. Boundary optimality:
   - KKT multiplier recovery method;
   - or equivalent constrained optimality residual definition.

---

# Required Output

Create:

`docs/CH5_TWO_ASSET_HANK_R2_NUMERICAL_AND_KKT_AUTHORITY_COMPLETION_REPORT.md`

The report must freeze:

1. productivity discretization authority;
2. z-state grid/domain contract;
3. refinement and truncation evidence protocol;
4. lower-bound KKT/complementarity diagnostic contract;
5. acceptable residual definitions and tolerances;
6. impact on future R2 rerun acceptance criteria.

---

# Allowed Scope

Allowed:

- scientific contract clarification;
- numerical diagnostic specification;
- documentation updates.

---

# Forbidden Operations

Do NOT:

- modify HJB implementation;
- modify KFE implementation;
- expand model scope;
- run dissertation experiments;
- calibrate final parameters;
- generate Results claims;
- modify dissertation sources;
- modify MATLAB sources.

---

# Acceptance Criteria

PASS requires:

- productivity discretization contract frozen;
- KKT/complementarity evidence contract frozen;
- no unresolved scientific authority gaps remain;
- implementation boundary remains unchanged.

If authority cannot be resolved:

Return:

`BLOCKED_R2_NUMERICAL_KKT_AUTHORITY_UNRESOLVED`

---

# Next Gate

After acceptance:

`CH5_TWO_ASSET_HANK_R2_HJB_IMPLEMENTATION_RERUN`

R3 KFE remains unauthorized.
