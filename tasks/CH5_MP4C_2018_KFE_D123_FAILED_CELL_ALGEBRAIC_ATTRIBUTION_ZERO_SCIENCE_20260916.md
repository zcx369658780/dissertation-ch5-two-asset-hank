# CH5 MP4C 2018 KFE D1-D3 failed-cell algebraic attribution — zero science

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder forensic attribution; zero scientific execution

## Objective

Using only accepted frozen equations, source code and already persisted selector receipts, determine the exact failure mechanism of Cells 4, 8 and 10 from the accepted ten-cell reexecution. Do not repair or rerun the selector. The task must distinguish a genuine algebraic incompatibility of the frozen historical derivative state from an implementation/enumeration omission.

## Required startup authority

Fresh-fetch `origin/main` and read in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_TEN_CELL_REEXECUTION_FAIL_CLOSED_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_SELECTOR_ACTIVE_EQUALITY_CANONICALIZATION_AND_TEN_CELL_REEXECUTION_REPORT.md`
7. exact Cell 4, Cell 8 and Cell 10 receipts under `reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916/`
8. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`
9. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_ACCEPTANCE.md`
10. current isolated corrected selector implementation under `src/ch5_two_asset_hank/corrected_diagnostic/`.

## Frozen scientific law

Do not alter D1/D2/D3.

- D1: upper finite-box faces are numerical state constraints with joint feasibility/complementarity; lower bounds retain their economic identity.
- D2: strict closed-face outward drift rejection remains zero-tolerance after canonical representation of an accepted active equality.
- D3: transfer KKT/FOC uses the existing `s(a)=max(a,a_bar)` cost consistently with no derivative floor, transfer cap, new coefficients or alternate zero-asset law.
- At an upper face, use the accepted multiplier/sign convention from the written KKT authority. `q_b>0` remains a domain requirement.
- Derivative-direction consistency remains part of candidate admissibility.

## Required forensic questions

### A. Cells 4 and 8 — dual-upper corners
For each cell, prove or disprove from the frozen derivative inputs and upper-b multiplier law whether any admissible `q_b>0` can exist when upper-b is active. Separately prove or disprove whether any inactive-upper-b candidate can satisfy `q_b>0` and inward drift consistency.

Explicitly state whether the observed `q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR` and `UPPER_B_ACTIVE_HAS_NO_Q_B_POSITIVE_MULTIPLIER_DOMAIN` exhaust the frozen upper-b possibilities or whether the selector omitted a mathematically legal branch.

### B. Cell 10 — upper-b face with interior a
Reconstruct the candidate logic from the persisted comparison set without calling the selector. For each derivative branch / transfer-sign / upper-b active-or-slack case represented by the frozen contract, identify the decisive rejection inequality or KKT relation.

Determine whether the failure is:
- a genuine derivative-direction fixed-point conflict under the frozen directional derivatives;
- a transfer-KKT/sign conflict;
- an upper-b feasibility conflict;
- an incomplete active-set/regime enumeration;
- or a combination.

If the current selector failed to enumerate any mathematically legal frozen-contract branch, identify the exact missing branch. Do not implement it.

### C. Historical-derivative versus corrected-target meaning
State precisely what can and cannot be inferred from `NO_ADMISSIBLE_POLICY` when the derivative arrays were produced by the historical MATLAB-faithful path rather than by a corrected-target HJB fixed point. Do not call the failure an economic nonexistence result unless repository authority proves that interpretation.

### D. Next-route classification
Return exactly one of:
- `ATTRIBUTED_STRUCTURAL_INCOMPATIBILITY_OF_FROZEN_DERIVATIVE_INPUTS`
- `ATTRIBUTED_SELECTOR_ENUMERATION_OR_IMPLEMENTATION_OMISSION`
- `MIXED_FAILURE_CLASSES_WITH_SPECIFIC_REPAIRABLE_OMISSION`
- `UNRESOLVED_REQUIRES_OWNER_SCIENTIFIC_DECISION`

If a repairable implementation omission is found, specify the smallest possible future repair and the minimum fresh validation panel, but do not execute it.

If no implementation omission is found and failures are attributable to frozen historical derivative incompatibility, specify whether the next scientifically meaningful step should be a **single corrected-target HJB policy-map/direct-step gate** rather than another historical-derivative selector rerun. Do not authorize that step yourself.

## Allowed operations

- read-only Git/GitHub history and current repository text;
- read persisted JSON receipts and source code;
- symbolic/algebraic derivation on the recorded numbers;
- pure arithmetic checks that do not invoke selector/root/HJB/KFE/model functions;
- one forensic report.

## Forbidden operations and call ledger

All must remain exactly zero:
- real or synthetic selector invocations: 0
- scalar root invocations: 0
- HJB maps/iterations/direct solves: 0
- KFE solves: 0
- MATLAB: 0
- outer/firm/wage-return recalculation: 0
- GE/annual/shock/IRF/Results: 0

Do not edit scientific code, tests, calibration, grids, tolerances or prior evidence.

## Required report

Create:
`docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_REPORT.md`

It must contain:
- verdict/classification;
- fresh-start main SHA, branch and candidate SHA;
- exact files read and exact changed paths;
- algebraic proof table for Cells 4/8;
- complete frozen-contract branch accounting for Cell 10;
- selector-enumeration completeness conclusion;
- historical-derivative interpretation boundary;
- zero-call ledger;
- smallest next gate recommendation, without publishing a successor.

## Git

Use a task branch and isolated worktree if useful. No reset/clean/stash/force-push. Stage only the report. Commit and non-force push. Verify remote readback and clean worktree. Do not merge main and do not publish a successor task.
