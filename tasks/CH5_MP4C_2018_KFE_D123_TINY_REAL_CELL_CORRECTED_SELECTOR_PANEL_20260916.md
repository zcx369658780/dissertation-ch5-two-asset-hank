# CH5 MP4C 2018 KFE D1-D3 tiny real-cell corrected selector panel

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder implementation + preregistered scientific selector validation

## Objective

Extend the already accepted isolated corrected-diagnostic target with the minimum real-cell constrained policy selector required by the Owner-adopted D1+D2+D3 contract, then execute exactly the preregistered ten-cell panel. This gate asks one question only: can the corrected target produce admissible, KKT-consistent, closed-face-feasible policies on the designated historical boundary cells without floors, caps, clipping, solver tuning or production-path modification?

This is not an HJB, KFE, production, GE or Results task.

## Required startup authority

Fresh-fetch `origin/main` and read in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_DIAGNOSTIC_BUNDLE_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_ACCEPTANCE.md`
9. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`
10. the exact accepted snapshot manifests/receipts and directly relevant source needed to bind the ten cells.

If live authority or the exact panel provenance materially differs from this task, stop before scientific execution.

## Frozen scientific contract

Keep the authority identifier `CH5_MP4C_2018_KFE_D123_OWNER_ADOPTED_20260916`.

D1: artificial upper `a`/`b` truncations are numerical state constraints. At every binding face use joint feasibility/complementarity rather than sequential source-label overrides. Lower `a` and lower `b` remain the existing economic bounds.

D2: the downstream corrected generator consumes only the selector's total drifts `g_b,g_a`, uses actual neighbor distances, rejects any outward closed-face drift, retains nonnegative rates and closes the diagonal by the retained outgoing sum. Do not run a KFE solve here.

D3: use the existing cost `C(d,a)=chi0*abs(d)+chi1*d^2/(2*s(a))`, `s(a)=max(a,a_bar)`, and the corresponding transfer subgradient/KKT everywhere. No derivative floor, transfer cap, new coefficient, new technology or alternative zero-asset law.

The written joint Hamiltonian/KKT authority in `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md` controls this implementation: consumed `c,l,d,cost,g_b,g_a`, utility/Hamiltonian, derivative-domain flags, active constraints, slacks, multipliers, complementarity and zero-transfer kink status must be returned for each evaluated cell.

## Exact preregistered panel

Recover the exact historical state/derivative/input arrays from the accepted call725 snapshot receipts. Do not recompute them through an HJB or policy map.

Panel = exactly 10 cells:
- the eight asset-boundary corners of the accepted `M143_FINAL` snapshot: all four `(b lower/upper, a lower/upper)` combinations for each of the two productivity states;
- accepted MATLAB trajectory cell `row799` from step 52;
- accepted MATLAB trajectory cell `row379` from step 57.

The row labels above must be resolved using the repository's accepted indexing/order authority and recorded as both source row label and explicit `(b_index,a_index,z_index)`/F-order flat index. If row numbering is ambiguous or does not resolve uniquely from repository authority, stop and report `BLOCKED_PANEL_IDENTITY_AMBIGUOUS`; do not infer a replacement.

These call725 cells are a historical diagnostic panel and must not be silently remapped to the later `I=20,J=160` practical HJB grid.

## Selector implementation boundary

Implement only inside `src/ch5_two_asset_hank/corrected_diagnostic/` plus focused tests/fixtures/evidence/report. Do not edit source-faithful MATLAB/Python files or production integration.

A corrected selector may enumerate the finite joint face-active sets and the three transfer-sign regimes `{negative, zero-kink, positive}`. For every candidate it must verify domain validity, feasibility, complementarity, derivative-direction consistency, KKT/subgradient conditions, and admissible Hamiltonian comparison before selecting a policy. A KKT root by itself is not a selection certificate.

No generic optimizer, damping, tolerance tuning, derivative floor, transfer cap, post-hoc projection, clipping or drift repair is authorized.

## Preregistered execution budget

Real corrected-target selector evaluations: **at most 10 total, exactly one per designated panel cell**.

Within each cell:
- at most 4 face-active sets;
- at most 3 transfer-sign regimes per active set;
- at most 1 scalar root invocation per regime;
- therefore at most 12 root invocations per cell and **at most 120 root invocations overall**;
- no adverse-numerics retry and no repeated selector evaluation of a cell.

A branch/regime that is analytically ruled out need not call a root. Report actual counts. Root failures/invalid domains are evidence and must not be converted into extra calls.

Before the first real selector evaluation, finish implementation, synthetic tests and panel identity binding. Once the first real selector evaluation begins, freeze selector/scientific code for this task. If a scientific-code defect is then discovered, stop and report; do not patch and rerun the panel under the same task.

## Scientific/model call budget

- corrected real-cell selector evaluations: <=10
- scalar root invocations inside those selector evaluations: <=120
- HJB policy maps/iterations/direct solves: 0
- KFE solves: 0
- outer loop: 0
- firm block: 0
- wage/return recalculation: 0
- MATLAB processes: 0
- GE: 0
- annual/downstream production: 0
- shock: 0
- IRF: 0
- Results: 0

Reading accepted arrays and pure post-evaluation checks do not add scientific calls.

## Required per-cell evidence

For every one of the 10 cells record:
- exact provenance, hash-bound source object and resolved indices;
- all bound state and derivative inputs consumed by the selector;
- selected `c,l,d,cost,g_b,g_a` if a candidate is selected;
- utility/Hamiltonian and the admissible comparison set;
- active constraints and face kinds;
- slacks, multipliers and complementarity residuals;
- `q_b` domain status and transfer branch/kink residual;
- closed-face drift feasibility under D1;
- D2 assembler admissibility of the selected total drifts, without KFE solve;
- active-set/regime count and actual scalar-root count;
- explicit outcome `SELECTED_ADMISSIBLE`, `NO_ADMISSIBLE_POLICY`, `ROOT_FAILURE`, or another narrowly defined fail-closed code supported by evidence.

Use prospectively derived floating-point bounds from the accepted specification; do not fit tolerances to panel outcomes.

## Acceptance target

A scientific PASS requires all 10 cells to resolve uniquely and each to produce one selected admissible corrected-target policy satisfying the frozen D1/D3 selector contract and passing the D2 closed-box assembler-admissibility check, within the preregistered call budget and without code changes after panel execution begins.

Any cell with no admissible selected policy, invalid derivative domain, unresolved identity, budget breach or scientific-code mutation after execution begins prevents PASS. Preserve the exact failure and stop before HJB/KFE.

Even a PASS does not establish HJB convergence or KFE validity and does not authorize production replacement.

## Allowed writes

- isolated corrected-diagnostic selector implementation under `src/ch5_two_asset_hank/corrected_diagnostic/`;
- focused tests under `tests/`;
- bounded evidence under `reports/ch5_mp4c_2018_kfe_d123_tiny_real_cell_selector_panel_20260916/`;
- one report: `docs/CH5_MP4C_2018_KFE_D123_TINY_REAL_CELL_CORRECTED_SELECTOR_PANEL_REPORT.md`.

Do not modify the accepted static report/evidence, source-faithful paths, production calibration/grid/domain/tolerances, pin semantics, HJB/KFE code, or downstream integration.

## Required report

Report verdict, fresh-start main SHA, branch/candidate SHA, exact changed paths, panel identity/provenance table, selector implementation map, synthetic preflight tests, per-cell scientific evidence, per-cell and total active-set/regime/root counts, D1/D2/D3 checks, frozen-code-after-first-call proof, complete call ledger, limitations, remote readback and worktree status.

## Git

Use an isolated worktree if useful. No reset/clean/stash/force-push. Stage only allowed paths. Commit and non-force push the task branch, verify remote readback and clean worktree. Do not merge main and do not publish a successor task.
