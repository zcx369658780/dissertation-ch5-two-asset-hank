# CH5 MP4C K1 — standalone MATLAB-faithful HJB ra transition refinement 3×3 scan

Date: 2026-09-13
Task ID: `CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN`
Type: bounded standalone household HJB/KFE parameter-domain refinement diagnostic.

## Goal

Refine the illiquid-return transition interval identified by the accepted coarse scan, without modifying the MATLAB-faithful HJB/KFE algorithm and without running the full multi-province model.

The task asks whether an interior illiquid-asset stationary distribution exists between the accepted lower-bound regime at `ra=.055` and upper-bound pile-up at `ra=.09`.

## Mandatory authority

Read live `AGENTS.md`, rule index, CURRENT status/handoff, `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_ACCEPTANCE.md`, `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_FREEZE_CURRENT.md`, accepted MATLAB-faithful annual-HJB/KFE authority docs, accepted standalone household implementation, designated MATLAB source/provenance docs, and the accepted coarse-scan report/evidence.

## Frozen configuration

Use the exact accepted coarse-scan standalone configuration except for the preregistered `ra` values:

- `I=20`, `b in [-2,5]`;
- `J=20`, `a in [0,10]`;
- `Nz=2`, `z=[.8,1.3]`;
- original productivity transition matrix;
- `rb=.02`;
- borrowing-rate gap `.07`;
- household wage proxy `w ∈ {.8,1.05,1.3}`;
- all other economic parameters, transfer/tax/baseline-labor construction, HJB/KFE numerics, derivative floor, FOC, selector, boundary laws, pseudo-time/update equation, direct solve, convergence tolerance, iteration ceiling, transition-matrix legality criterion and contaminated-row stationary KFE exactly unchanged.

Do not use any damping/relaxation or global-model price guards.

## Exact refinement grid

Run exactly nine points:

`rb=.02`

`ra ∈ {.065,.0725,.08}`

`w ∈ {.8,1.05,1.3}`

Cartesian product only. No adaptive or additional point after observing results.

## HJB stage

For every point, construct a fresh original/accepted MATLAB-style standalone initialization; no warm start across points.

Execute exactly one HJB solve and record:

- converged flag;
- iterations;
- final `max(abs(V_new-V_old))`;
- maximum MATLAB-equivalent transition-matrix legality statistic `A2max=max(abs(sum(A,2)))`;
- first legality failure iteration if any;
- hard-error/nonfinite reason if any;
- finite/shape/label-domain receipts.

Classify as exactly one of:

- `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`;
- `HJB_NOT_CONVERGED`;
- `HJB_CONVERGED`.

Do not run KFE for nonconverged/hard-error points.

## KFE and steady-state evidence

For HJB-converged points only, run the accepted standalone MATLAB-faithful contaminated-row stationary KFE exactly once.

Report at least:

- total mass / normalization;
- `Ct,Lt,At,Bt`;
- `Bt_pos,Bt_neg` if available;
- full 20-bin marginal over `a`;
- full 20-bin marginal over `b`;
- exact endpoint mass at `amin`, `amax`, `bmin`, `bmax`;
- modal `a` and modal `b`;
- mass in interior illiquid bins `a∈(amin,amax)`;
- top three illiquid-asset bins by mass with locations;
- `amax` mass / adjacent-interior-bin mass where defined;
- finite/nonfinite, expected-shape and contaminated-row residual/signed-mass receipts.

## Pre-registered interpretation

The primary question is whether any refinement point displays an interior illiquid-asset regime.

Use descriptive labels only:

- `LOWER_A_BOUNDARY_DOMINATED` if essentially all/overwhelming mass remains at the structural lower bound;
- `INTERIOR_A_DISTRIBUTION_CANDIDATE` if the mode is interior and both endpoint concentrations are clearly secondary in the raw marginal;
- `UPPER_A_BOUNDARY_PILEUP` if artificial `amax` is the mode / clearly binds the distribution;
- `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` if the shape is mixed.

Do not create a post-result threshold solely to force labels. Always publish the raw marginal, endpoint shares, interior mass and modal bins.

## Runtime budget

- HJB calls: exactly 9 unless shared preflight corruption blocks execution;
- KFE calls: at most 9, only one per HJB-converged point;
- scientific retries after a point begins: 0;
- one pre-HJB engineering retry only for path/import/serialization/output-shape defects with identical scientific inputs;
- global outer turns, firm, MATLAB, K1B/K2, GE, annual downstream, shock, IRF, Results: all 0.

A failure at one independent parameter point does not stop the remaining points unless it reveals shared implementation/provenance corruption.

## Required outputs

Produce a 3×3 table with rows=`ra` and columns=`w`, showing HJB class plus illiquid-distribution label.

For every point report `(rb,ra,w)`, HJB iterations/statistic/A2max, KFE status, `Ct,Lt,At,Bt`, four endpoint masses, total interior-a mass, modal a/b, top three a bins, and final descriptive label.

Create:

- `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_transition_refinement_3x3/`;
- fresh external no-overwrite evidence root if detailed marginals/receipts require it;
- truthful CURRENT closeout docs.

## Questions to answer

1. Do all nine HJB points remain legal and converged?
2. At which `ra` values does the illiquid distribution remain lower-bound dominated, become interior, or move toward/onto `amax`?
3. Does the transition depend materially on wage within `.8–1.3`?
4. Is there a connected coarse interior candidate band that can be used as a provisional household `ra` health region?
5. What are the `Ct,Lt,At,Bt` ranges inside that interior candidate band?
6. What exactly one next gate is justified: narrower `ra` refinement, provisional `ra` health-band freeze, or unresolved review? Recommend only; do not run it.

## Hard stops

Stop on unauthorized HJB/KFE changes, damping, solver/tolerance/ceiling/grid/derivative-floor/FOC/selector/boundary changes, alternative wage mapping, any point outside the exact nine-point grid, global-model call, or provenance/oracle mismatch.

## Git workflow

Fresh-fetch live main and record actual baseline. Use a fresh isolated worktree/branch. No reset/clean/stash/force push. Explicit stage paths only; no `git add .` or `git add -A`.

One coherent Builder commit, non-force push, one remote readback. Do not merge main and do not publish a successor task.

## Final response

Return outcome first and include actual baseline/branch/worktree/candidate SHA; changed paths; exact grid; input-invariance receipt; full HJB/KFE call ledger; 3×3 classification; per-point HJB and KFE evidence; full illiquid-marginal transition summary; any interior candidate band; aggregate ranges for that band if present; exactly one recommended next gate; standalone-vs-multi-province KFE caveat; and `Results eligibility=FALSE`.

Stop for independent ChatGPT Reviewer acceptance.
