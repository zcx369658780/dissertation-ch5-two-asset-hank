# CH5 MP4C 2018 KFE D1-D3 selector active-equality canonicalization + ten-cell reexecution

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder repair + preregistered scientific selector reexecution

## Objective

Repair the two accepted implementation defects from candidate `05082f8af82afc90b8c0c168d9aeb8f345f8336a` without changing the Owner-adopted D1/D2/D3 science: (1) make active state-constraint equalities hand off an exact mathematical zero drift to the strict D2 assembler only after their raw floating equality residual passes the preregistered arithmetic bound; (2) persist the complete selector receipt before D2 post-selection validation. Then rerun the same exact ten-cell panel once under a fresh budget.

This is not an HJB, KFE, production, GE or Results task.

## Required startup authority

Fresh-fetch `origin/main` and read in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_TINY_REAL_CELL_SELECTOR_PANEL_FAILURE_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_TINY_REAL_CELL_CORRECTED_SELECTOR_PANEL_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_2018_KFE_D123_DIAGNOSTIC_BUNDLE_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
9. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`
10. exact accepted panel receipts/manifests used by the prior run.

If live authority materially differs, stop before scientific execution.

## Frozen scientific contract

Authority remains `CH5_MP4C_2018_KFE_D123_OWNER_ADOPTED_20260916`.

D1 upper artificial faces/corners are numerical state constraints; D2 remains consumed-total-drift conservative assembly with **strict zero-tolerance outward closed-face rejection**; D3 remains the existing `s(a)=max(a,a_bar)` cost/KKT law. Do not relax D2, alter the economic boundary law, change grid/calibration, add floors/caps, or tune tolerances to the observed Cell 2 value.

## Authorized repair 1 — active-equality canonical representation

When and only when a face is part of the candidate's selected active constraint set:

1. Compute and retain the raw consumed drift/equality residual from the selector arithmetic.
2. Compare `abs(raw_residual)` against the same prospectively derived floating-point arithmetic bound already defined before panel outcomes.
3. If the raw residual exceeds that bound, reject the candidate as an active-equality failure.
4. If it is within the bound, the final mathematical consumed drift handed to downstream D1/D2 checks for that active face shall be exact floating `0.0`.
5. Persist separately: raw residual, arithmetic bound, canonicalized final drift, active-face identity, and a marker such as `ACTIVE_EQUALITY_CANONICAL_ZERO`.

This rule is not permitted on slack/inactive faces. Slack-face drifts remain raw and any strictly outward sign must still fail the D2 zero-tolerance contract. Do not use `abs(drift)<tol` to zero arbitrary drifts.

Apply the same representation rule consistently to active `b` and active `a` equalities where applicable. Hamiltonian/KKT/complementarity reporting must remain scientifically coherent and must preserve the raw equality residual for audit.

## Authorized repair 2 — durable selector receipt before D2

After each real selector evaluation returns, durably persist the complete selector result and comparison set, cumulative budget counters, cell identity and code-freeze identity **before** calling the D2 assembler check. Then append/persist the D2 result. If D2 raises, the already-written selector receipt must remain complete and the task must stop without repeating the cell.

## Synthetic preflight requirements

Before any real-cell call, add focused tests proving at minimum:

- an active upper-`b` equality with a positive raw roundoff residual inside the prospective bound records the raw value but hands exact `0.0` to D2 and passes the sign boundary;
- the analogous active `a` equality behavior;
- an active equality residual outside the bound is rejected, not zeroed;
- an inactive/slack upper face with `nextafter(0,+1)` remains rejected by D2;
- no lower/economic boundary identity changes;
- receipt-before-D2 ordering is testable: a forced D2 failure still leaves the complete selector receipt durable;
- previously accepted static D1/D2/D3 tests continue to pass.

Do not derive a new tolerance from `2.162339589068668e-16` or any real-cell outcome.

## Exact panel and fresh execution budget

Use exactly the same 10 preregistered historical cells and indexing/provenance as the accepted failure report:
- eight `M143_FINAL` asset corners (two z states);
- MATLAB trajectory step52 `row799`;
- MATLAB trajectory step57 `row379`.

No remapping to the later practical grid.

After implementation + synthetic tests + exact panel binding are complete, freeze all scientific selector code/hashes. Then execute the full ten-cell panel from Cell 1 under a **fresh task budget**:

- corrected real-cell selector evaluations: exactly one per designated cell, <=10 total;
- at most 4 face-active sets per cell;
- at most 3 transfer-sign regimes per active set;
- at most 1 scalar root invocation per regime;
- <=12 root invocations per cell and <=120 overall;
- adverse-numerics retries: 0;
- no repeated cell evaluation.

Once the first new real selector evaluation begins, scientific/selector code is frozen. A defect discovered after that point requires stop; do not patch and rerun under this task.

## Other scientific/model call budget

HJB policy maps/iterations/direct solves=0; KFE solves=0; outer=0; firm=0; wage/return recalculation=0; MATLAB processes=0; GE=0; annual/downstream=0; shock=0; IRF=0; Results=0.

## Acceptance target

PASS requires all ten panel identities to remain exact and all ten cells to produce one selected admissible corrected-target policy satisfying D1/D3 and passing strict D2 assembler admissibility after the active-equality representation rule, within all call budgets and with no post-freeze code mutation.

Any unresolved identity, no-admissible-policy result, active raw equality residual beyond the prospective bound, slack-face outward drift, D2 rejection, root/budget failure, or post-freeze scientific-code mutation prevents PASS and stops before HJB/KFE.

Even PASS does not establish HJB convergence, KFE stationary density validity, production replacement or Results eligibility.

## Allowed writes

- minimal repairs under `src/ch5_two_asset_hank/corrected_diagnostic/`;
- focused tests under `tests/`;
- fresh evidence under `reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916/`;
- one report: `docs/CH5_MP4C_2018_KFE_D123_SELECTOR_ACTIVE_EQUALITY_CANONICALIZATION_AND_TEN_CELL_REEXECUTION_REPORT.md`.

Do not overwrite the accepted prior failed-run report/evidence. Do not edit source-faithful or production paths.

## Required report

Return verdict; fresh-start main SHA; branch/candidate SHA; exact changed paths; repair diff map; synthetic tests; exact panel identity; per-cell selected-policy evidence; raw equality residual/bound/canonicalized drift for every active face; D2 result; root/selector counts; receipt-ordering evidence; frozen-code proof; complete call ledger; limitations; remote readback; worktree status.

## Git

Use isolated worktree if useful. No reset/clean/stash/force-push. Stage only allowed paths. Commit and non-force push task branch, verify remote readback and clean worktree. Do not merge main and do not publish a successor task.
