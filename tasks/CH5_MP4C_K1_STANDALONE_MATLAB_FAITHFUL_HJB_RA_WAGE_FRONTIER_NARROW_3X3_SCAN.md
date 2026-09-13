# CH5 MP4C K1 — standalone MATLAB-faithful HJB ra×wage frontier narrow 3×3 scan

Date: 2026-09-13
Task ID: `CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN`
Type: bounded standalone household HJB/KFE parameter-domain refinement diagnostic.

## Goal

Test whether the narrower `ra` region around the accepted wage-dependent frontier contains a wage-robust nondegenerate interior illiquid-asset distribution, without changing the accepted MATLAB-faithful HJB/KFE algorithm and without running the full multi-province model.

## Mandatory authority

Read live `AGENTS.md`, rule index, CURRENT status/handoff, `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN_ACCEPTANCE.md`, `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_REFINEMENT_FREEZE_CURRENT.md`, accepted MATLAB-faithful HJB/KFE authority docs, accepted standalone household implementation, designated MATLAB source/provenance, and accepted coarse/refinement reports/evidence.

## Exact grid

Run exactly nine fresh standalone points:

- `rb=.02` fixed;
- `ra={.06,.0675,.07}`;
- household wage proxy `w={.8,1.05,1.3}`.

Cartesian product only. No adaptive/additional points after observing results.

## Frozen configuration

Use the exact accepted standalone configuration from prior scans. Only `inputs.r_a` and `inputs.wages[0]` may vary. Preserve `I=20`, `b∈[-2,5]`, `J=20`, `a∈[0,10]`, `Nz=2`, original productivity transition matrix, borrowing-rate gap `.07`, all accepted household parameters, fresh MATLAB-style initialization, HJB/KFE numerics, derivative floor, FOC, selector, boundary laws, pseudo-time/direct solve, convergence tolerance, 100-iteration ceiling, `homecrit=.01`, and contaminated-row KFE.

No warm start. No damping/relaxation. No price guard. No solver/tolerance/ceiling/grid/derivative-floor/FOC/selector/boundary/KFE change.

## HJB stage

Exactly one fresh HJB solve per point. Record convergence flag, iterations, final `max(abs(V_new-V_old))`, maximum `A2max=max(abs(sum(A,2)))` for `A=BB+AAH+Bswitch`, first legality failure if any, hard-error/nonfinite reason, finite/shape/label-domain receipts.

Classify exactly one of:

- `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`;
- `HJB_NOT_CONVERGED`;
- `HJB_CONVERGED`.

Do not run KFE for HJB hard-error/nonconverged points.

## KFE / distribution stage

For each HJB-converged point run exactly one accepted standalone contaminated-row KFE. Report:

- total stationary mass;
- `Ct,Lt,At,Bt`, plus `Bt_pos/Bt_neg` if available;
- full 20-bin `a` and `b` marginals;
- endpoint masses at `amin,amax,bmin,bmax`;
- total interior-a mass;
- modal `a` and modal `b`;
- top three `a` bins by mass;
- `amax/adjacent-interior` ratio where defined;
- finite/shape checks;
- contaminated-row residual and signed-density receipt.

Distribution labels:

- `LOWER_A_BOUNDARY_DOMINATED`;
- `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `UPPER_A_BOUNDARY_PILEUP`;
- `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`.

Use raw modal/bin ordering and marginals; do not fit a post-result cutoff.

## Questions

1. Are all nine HJB points legal and converged?
2. What is the distribution class at each `(ra,w)` point?
3. Is any tested `ra` interior across all three wages?
4. Does a connected wage-robust interior `ra` band exist in this narrower grid?
5. How does the frontier shift with wage?
6. For interior candidates, what are the `Ct,Lt,At,Bt` ranges?
7. Exactly one next gate: either provisional wage-robust health-band freeze/local-bound confirmation if supported, or two-dimensional wage-conditional `(ra,w)` health-region / provincial return-mapping review if no universal scalar band exists. Recommend only; do not run successor work.

## Runtime budget

- HJB: exactly 9 unless shared preflight corruption blocks execution;
- KFE: at most 9, only one after each converged HJB;
- scientific retries: 0;
- one pre-HJB engineering retry only for path/import/serialization/output-shape with unchanged scientific inputs;
- global outer turns, firm, MATLAB, K1B/K2, GE, downstream annual, shock, IRF, Results: all 0.

A single scientific failure is an intended point outcome and does not stop remaining independent points unless it proves shared provenance/implementation corruption.

## Required outputs

Create a 3×3 matrix, rows=`ra`, columns=`w`, showing HJB class + distribution class. Provide a per-point table with HJB/KFE receipts and complete raw distribution evidence.

Create:

- `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_wage_frontier_narrow_3x3/`;
- fresh external no-overwrite evidence root if needed;
- truthful CURRENT closeout docs.

## Hard stops

Stop on unauthorized HJB/KFE algorithm modification, damping, solver/tolerance/ceiling/grid/derivative-floor/FOC/selector/boundary change, alternative wage mapping, any point outside the exact nine-point grid, global-model call, or provenance/oracle mismatch.

## Git workflow

Fresh-fetch live main and record actual baseline. Use a fresh isolated worktree/branch. No reset/clean/stash/force push. Explicit stage paths only; no `git add .` or `git add -A`.

One coherent Builder commit, non-force push, one remote readback. Do not merge main and do not publish a successor task.

## Final response

Return outcome first; actual baseline/branch/worktree/candidate SHA; changed paths; exact grid; input-invariance receipt; HJB/KFE ledger; 3×3 matrix; per-point HJB/KFE/distribution evidence; whether a wage-robust interior band exists; interior-candidate aggregate ranges; exactly one recommended next gate; standalone-vs-multi-province KFE caveat; `Results eligibility=FALSE`.

Stop for independent ChatGPT Reviewer acceptance.
