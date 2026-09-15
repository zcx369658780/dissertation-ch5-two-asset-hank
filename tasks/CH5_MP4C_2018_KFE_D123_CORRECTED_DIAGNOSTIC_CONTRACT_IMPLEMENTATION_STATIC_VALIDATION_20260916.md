# CH5 MP4C 2018 KFE D1-D3 corrected diagnostic contract implementation + static validation

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder implementation; no scientific solver execution

## Objective

Implement the Owner-adopted D1+D2+D3 bundle as a **separate corrected diagnostic target** and close the first contract-validation gate using synthetic arithmetic and saved-control/assembler-only evidence. Do not replace production or source-faithful MATLAB/Python paths and do not run any real selector/HJB/KFE solve.

## Required startup authority

Read, in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_DIAGNOSTIC_BUNDLE_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_OWNER_DECISION_RECOVERY_AND_OPTION_MATRIX_REPORT.md`
7. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_ACCEPTANCE.md`
8. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`
9. `docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_ACCEPTANCE.md`
10. directly relevant current source and saved-control provenance before editing.

Fresh-fetch `origin/main`; record the actual baseline. If live authority materially changes the adopted contract, stop and report.

## Adopted bundle to implement

### D1
Use explicit numerical state constraints at artificial upper `a`/`b` faces and corners on the existing finite box. Joint face/corner admissibility must prevent outward closed-face drift. Do not reinterpret this as an economic saving cap, reflection, absorption, exterior continuation, or household entry/exit process. Preserve the distinct existing economic lower bounds.

### D2
For the corrected target, assemble the generator from consumed total drifts and actual neighbor distances. Retained offdiagonal rates must be nonnegative; closed-face outward inputs must fail explicitly; the diagonal must equal minus the retained outgoing-rate sum. For admissible closed-box input, require `Q @ 1 = 0` to numerical arithmetic tolerance by construction. Do not call this MATLAB parity.

### D3
Retain the existing adjustment cost and coefficients with `s(a)=max(a,a_bar)` and derive the corrected-target transfer derivative/KKT/FOC consistently from that same regularized cost for the whole domain, including `a<a_bar` and `a=0`. Do not add a derivative floor, transfer cap, new coefficients, or a different adjustment technology.

## Isolation and allowed edits

Create the corrected target in a clearly separate namespace, preferably under `src/ch5_two_asset_hank/corrected_diagnostic/`, with new focused tests under `tests/`. A different minimal isolated name is allowed only if it avoids collision and is reported exactly.

Allowed writes are limited to:
- new corrected-diagnostic implementation files under `src/ch5_two_asset_hank/` that do not alter source-faithful behavior;
- focused tests/fixtures under `tests/`;
- task evidence under `reports/` if useful;
- one execution report: `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_REPORT.md`.

Do **not** edit the frozen MATLAB source, `exports/matlab_faithful_two_asset_ha.py`, `src/ch5_two_asset_hank/matlab_faithful_hjb.py`, `src/ch5_two_asset_hank/matlab_faithful_kfe.py`, production calibration, grid/domain constants, tolerances, pin-row semantics, accepted source-faithful tests/evidence, or downstream integration code.

## Required validation — no real solver calls

1. **D1 synthetic boundary contract**: cover upper-`a`, upper-`b`, dual-upper corner, active/slack cases and zero/kink cases as applicable. Legal inward/tangent inputs pass; outward closed-face inputs fail or are made feasible only through the adopted state-constraint control contract, never through silent edge deletion/diagonal retention.
2. **D2 synthetic generator invariants**: verify nonnegative offdiagonals, exact retained-rate diagonal construction, `Q @ 1` closure at floating-point arithmetic scale, coordinate drift consistency wherever representable, and explicit rejection of outward closed-face inputs.
3. **D3 low-`a` consistency**: verify cost and derivative/KKT use the same `s(a)=max(a,a_bar)` at `a=0`, `0<a<a_bar`, `a=a_bar`, and `a>a_bar`; include transfer-sign and zero-transfer-kink cases required by the accepted specification.
4. **Saved-control assembler-only check**: reuse the exact previously accepted saved-control snapshot set identified by repository authority (including the previously specified 14 saved snapshots if available). Loading/parsing saved artifacts and evaluating pure contract/assembler functions is allowed; do not invoke a real selector, HJB loop, KFE solve, outer loop, firm block or wage/return recalculation. If the exact saved set cannot be recovered, mark it `NOT_RECOVERED` and do not fabricate replacements.
5. **Frozen-reference preservation**: demonstrate that no source-faithful implementation file changed. Existing focused non-scientific unit tests may be run if they do not execute model/solver paths.

## Scientific/model call budget

All of the following must remain exactly zero:
- real selector/evaluator calls: 0
- HJB iterations/solves: 0
- KFE solves: 0
- outer loop: 0
- firm block: 0
- wage/return recalculation: 0
- MATLAB: 0
- GE: 0
- annual/downstream production: 0
- shock: 0
- IRF: 0
- Results: 0

Pure unit tests of new arithmetic/assembly helpers and reads of saved artifacts are not model calls, but the report must distinguish them clearly.

## Stop conditions

Stop without scientific execution if:
- implementing D1 requires a new economic boundary law beyond the adopted state constraint;
- implementing D3 requires a new cost/admissible-transfer assumption;
- source-faithful files would need behavioral edits;
- the exact saved-control provenance is ambiguous in a way that changes the intended test;
- any validation would require a real selector/HJB/KFE call.

Routine import/path/test-fixture issues may be repaired within allowed paths.

## Required report

`docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_REPORT.md` must contain:
- verdict;
- fresh-start main SHA, branch and candidate SHA;
- exact changed paths;
- implementation map D1/D2/D3 → code objects;
- explicit statement that the corrected target is separate from source-faithful reference;
- synthetic D1/D2/D3 test matrix and outcomes;
- saved-control snapshot provenance and assembler-only outcomes, or `NOT_RECOVERED` fail-closed result;
- `Q @ 1`, offdiagonal-sign and diagonal-construction evidence for tested admissible cases;
- all-zero scientific/model call ledger;
- exact tests/commands used, without dumping large logs;
- limitations and next permitted gate.

## Acceptance boundary

A PASS means only: the adopted corrected diagnostic contracts are implemented in isolation and pass static/synthetic/saved-control assembler checks. It does **not** establish selector correctness on real cells, HJB convergence, KFE stationary-density validity, production replacement, or Results eligibility.

## Git

Use an isolated worktree if useful. No reset/clean/stash/force-push. Stage only allowed paths. Work on a task branch, commit and push, verify remote readback and clean worktree. Do not merge to main and do not publish a successor task.
