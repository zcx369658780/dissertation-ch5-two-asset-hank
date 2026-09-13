# CH5 MP4C K1 — standalone MATLAB-faithful HJB ra × wage coarse 3×3 scan

Date: 2026-09-13
Task ID: `CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN`
Type: bounded standalone household HJB/KFE parameter-domain diagnostic.

## Goal

Identify a first coarse healthy convergence region for the original MATLAB-faithful two-asset household block without running the global multi-province model and without modifying the HJB algorithm.

The task must classify each preregistered `(rb,ra,w)` point as HJB hard error/invalid transition matrix, HJB nonconvergence, or HJB convergence; for converged HJB points only, compute the standalone stationary distribution and aggregate/boundary receipts needed to distinguish boundary-dominated versus apparently healthy steady-state candidates.

## Mandatory authority

Read live `AGENTS.md`, rule index, CURRENT status/handoff, `docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC_ACCEPTANCE.md`, `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_CONVERGENCE_DOMAIN_FREEZE_CURRENT.md`, accepted annual-HJB/KFE MATLAB-faithful authority docs, the accepted standalone MATLAB-faithful household implementation, and the designated MATLAB source/provenance docs.

## Frozen science and numerics

Do not redesign HJB or KFE. Use the accepted MATLAB-faithful standalone household block and frozen original settings, including:

- `I=20`, `bmin=-2`, `bmax=5`;
- `J=20`, `amin=0`, `amax=10`;
- `Nz=2`, `zmin=.8`, `zmax=1.3`;
- original MATLAB productivity transition matrix;
- `rb=.02`;
- borrowing-rate gap `.07`;
- accepted annual household preferences/technology/tax/transfer/baseline-labor inputs required by the standalone oracle;
- accepted MATLAB-faithful derivative floor, upwind selector, transfer FOC, boundary rules, HJB pseudo-time/update equation, direct solve, convergence tolerance and iteration ceiling;
- accepted MATLAB-faithful stationary KFE contaminated-row solve.

Do not use the prior `omega=.5` relaxation in this task. The HJB update is the unmodified accepted MATLAB-faithful algorithm.

## Exact preregistered grid

Run exactly nine standalone household points:

`rb=.02`

`ra ∈ {.02, .055, .09}`

`w ∈ {.8, 1.05, 1.3}`

Cartesian product only: 3 × 3 = 9 points.

No additional/adaptive points after observing results. No full multi-province trajectory or provincial loop.

## Input construction

Use the standalone oracle's actual household wage input. For this first scan, directly set that scalar household wage to the preregistered values `.8`, `1.05`, `1.3` as Owner-approved proxies for the original multi-province `wjt` range. Do not call the global wage aggregator in this task.

All non-scanned inputs must be identical across the nine points and match the accepted/original MATLAB-faithful standalone configuration. Persist an input receipt proving that only `ra` and `w` vary.

## HJB stage classification

For each point, execute exactly one fresh standalone HJB solve from the original/accepted MATLAB-style initial-value construction appropriate to that standalone solver.

Record:

- convergence flag;
- iterations used;
- final accepted `max(abs(V_new-V_old))` statistic;
- MATLAB-equivalent transition-matrix legality statistic for `A = BB + AAH + Bswitch`, including first failure iteration if any;
- any MATLAB-style hard-error signal / scientific exception / nonfinite event;
- final scientific arrays finite/shape/label-domain receipts.

Classify exactly one of:

- `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`;
- `HJB_NOT_CONVERGED`;
- `HJB_CONVERGED`.

Do not continue to KFE when HJB is hard-error or nonconverged.

## KFE and aggregate stage for HJB-converged points only

For each `HJB_CONVERGED` point, execute the accepted standalone MATLAB-faithful stationary KFE solve and report at least:

- stationary mass normalization / total mass receipt;
- `Ct`;
- `Lt`;
- `At`;
- `Bt`;
- `Bt_pos` / `Bt_neg` if available from the accepted household output;
- marginal probability over each `b` grid point;
- marginal probability over each `a` grid point;
- mass share exactly at `bmin`, `bmax`, `amin`, `amax`;
- upper-end mass compared with nearby interior bins;
- modal `b` and modal `a` grid locations;
- finite/nonfinite and expected-shape checks.

Do not modify the KFE or grid to improve these receipts.

## Preliminary steady-state quality labels

For each HJB-converged/KFE-completed point, assign one descriptive label using only the preregistered receipts:

- `BOUNDARY_CONVERGED_CANDIDATE` if there is clear artificial endpoint pile-up in `a` or `b`;
- `GOOD_STEADY_STATE_CANDIDATE` if aggregates/mass are finite/coherent and the marginals show no obvious artificial upper-bound pile-up;
- `QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED` if evidence is mixed.

Do not create a post-result numeric cutoff solely to force one of the first two labels. Always publish the raw boundary shares and marginals so Owner/Reviewer can inspect them.

## Runtime budget

Exactly 9 HJB calls unless a hard preflight blocker stops the task.

KFE calls: at most 9, and only one per HJB-converged point.

No retries after a scientific point begins. One pre-HJB engineering retry is allowed only for path/import/serialization/output-shape defects with unchanged scientific inputs.

Global multi-province outer turns=0.
Firm runtime=0.
MATLAB runtime=0 unless the task cannot prove the accepted standalone oracle configuration from repository authority; do not silently substitute MATLAB execution.
K1B/K2=0.
GE/annual downstream/shock/IRF/Results=0.

## Required outputs

Produce a compact 3×3 matrix/table with rows=`ra`, columns=`w`, showing the HJB class and, where available, the preliminary steady-state quality label.

Also report for every point:

- `(rb,ra,w)`;
- HJB classification;
- convergence iterations/statistic or hard-error reason;
- transition-matrix legality receipt;
- whether KFE ran;
- `Ct,Lt,At,Bt` where KFE ran;
- four asset-boundary mass shares;
- modal asset locations;
- final preliminary quality label.

Create:

- report `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_wage_coarse_3x3/`;
- external no-overwrite evidence root for detailed marginals/receipts if needed;
- truthful CURRENT closeout docs.

## Questions to answer

1. Which of the nine points are hard-error/invalid-transition-matrix, HJB-nonconverged, boundary-converged candidates, good steady-state candidates, or ambiguous?
2. Is there already a connected coarse region of good candidates in the original `ra∈[.02,.09]`, wage `∈[.8,1.3]` rectangle?
3. Along which `ra` or wage direction does failure/boundary behavior first appear?
4. What are the observed `Ct,Lt,At,Bt` ranges among good candidates?
5. What next small refinement grid is scientifically justified near the observed transition boundary? Recommend it only; do not run it.

## Hard stops

Stop on any unauthorized HJB/KFE algorithm modification, relaxation/damping, tolerance/grid change, price guard, global-model call, parameter value outside the nine preregistered points, provenance mismatch, or unexpected source/config mutation.

A hard-error at one parameter point is an intended scientific outcome and does not stop the remaining independent points unless the error indicates shared implementation/provenance corruption.

## Git workflow

Fresh-fetch live main and record actual baseline. Use a fresh isolated worktree/branch. No reset/clean/stash/force push. Explicit stage paths only; no `git add .` or `git add -A`.

One coherent Builder commit, non-force push, one remote readback. Do not merge main and do not publish a successor task.

## Final response

Return outcome first and include actual baseline/branch/worktree/candidate SHA; changed paths; exact nine-point grid; input-invariance receipt; complete HJB/KFE call ledger; 3×3 classification table; per-point HJB error/convergence evidence; per-converged-point `Ct,Lt,At,Bt`; boundary mass/marginal summary; any clear good coarse region; exactly one recommended refinement gate; KFE caveat distinguishing standalone accepted MATLAB-faithful KFE from the unresolved multi-province corrected-2018 blocker; and `Results eligibility=FALSE`.

Stop for independent ChatGPT Reviewer acceptance.
