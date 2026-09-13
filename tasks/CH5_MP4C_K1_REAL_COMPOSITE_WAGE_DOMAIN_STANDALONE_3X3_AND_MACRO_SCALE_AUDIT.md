# CH5 MP4C K1 — real composite-wage-domain standalone 3×3 scan + macro-scale audit

Date: 2026-09-13
Task ID: `CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT`
Type: bounded standalone household HJB/KFE diagnostic plus read-only dimensional-consistency audit.

## Goal

Extend the accepted standalone household health-map coverage to the actual provincial household composite-wage scale while preserving the accepted MATLAB-faithful HJB/KFE algorithm. In parallel, audit the model's macro quantity scales so that any later `wjt`/return recalibration does not mix incompatible normalizations or units.

## Mandatory authority

Read live `AGENTS.md`, rule index, CURRENT status/handoff, the accepted wage-conditional `(ra,w)` health-region/provincial-mapping audit and acceptance, all accepted standalone scan acceptances, the new freeze `docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_AND_MACRO_SCALE_CONSISTENCY_FREEZE_CURRENT.md`, accepted standalone MATLAB-faithful HJB/KFE authority, and designated MATLAB/Python wage/output/provenance sources.

## Exact standalone scan

Run exactly nine points:

- `rb=.02`;
- `ra ∈ {.06,.0675,.07}`;
- household composite wage `w ∈ {13.0,15.5,18.0}`;
- exact Cartesian product only.

These `w` values represent the household composite wage actually consumed by HJB. They are not `wjt` and do not modify the upstream firm wage range.

All non-scanned household parameters, grids, initialization, equations, numerics and KFE method must exactly match the accepted standalone oracle.

## No adaptive recalibration in this task

Do not change `wjt`, `ra`, `rb`, tax, transfer, productivity, GDP scaling, investment scaling, population scaling, grid, tolerance, solver, derivative floor, FOC, selector, boundary law, pseudo-time, KFE pin/contamination method, or any other science after observing results.

If the nine-point scan is poor, report it and transition the recommendation to a later joint recalibration gate. Do not add points or tune values in this task.

## HJB stage

For each point use a fresh accepted MATLAB-style initialization; no warm start.

Record:

- `(rb,ra,w)`;
- HJB classification;
- iterations;
- final `max(abs(V_new-V_old))`;
- maximum `A2max=max(abs(sum(A,2)))` and first legality-failure iteration;
- hard error/nonfinite reason if any;
- scientific-array finite/shape/label-domain receipts.

Classification must be exactly one of:

- `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`;
- `HJB_NOT_CONVERGED`;
- `HJB_CONVERGED`.

Do not run KFE after nonconvergence/hard error.

## KFE stage

For HJB-converged points only, run exactly one accepted standalone contaminated-row KFE.

Report:

- total mass;
- `Ct,Lt,At,Bt`;
- `Bt_pos,Bt_neg` if available;
- complete `a` and `b` marginals;
- masses at `amin,amax,bmin,bmax`;
- interior-a mass;
- modal `a`, modal `b`;
- top-three `a` bins;
- `amax/adjacent` ratio if defined;
- KFE residual;
- minimum density and negative-density count;
- finite/shape receipts.

Use descriptive labels only:

- `LOWER_A_BOUNDARY_DOMINATED`;
- `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `UPPER_A_BOUNDARY_PILEUP`;
- `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`;
- `KFE_NUMERICALLY_PATHOLOGICAL` if raw signed stationary evidence is materially non-probabilistic.

Do not fit a cutoff after results. Do not clip negative stationary weights.

## Macro-scale consistency audit

This audit is read-only. Use accepted repository source/evidence only; do not run the global model merely to fill gaps.

Trace, with file/function/formula identities:

1. province-level GDP/output object(s), including any data rescaling/multiplier/divisor;
2. province population object(s) and the model's per-capita GDP/output calculation if defined;
3. upstream provincial firm wage `wjt` object and range/guard;
4. household composite wage `results.w` / Python equivalent and aggregation formula;
5. investment/capital/GDP normalization multipliers or divisors that materially affect numerical scale;
6. productivity and labor normalizations that affect wage/output comparability.

Produce a scale table with, where supported:

- variable name;
- model object/source file;
- raw/statistical source unit if explicitly documented;
- model-normalized unit/status;
- transformation/multiplier;
- accepted numerical range/order of magnitude;
- whether directly comparable to GDP/per-capita GDP/household wage.

At minimum attempt to report the numerical order of magnitude of:

- provincial GDP;
- provincial per-capita GDP;
- household average/composite wage.

If a same-state consistent GDP/population/wage triple is not available from accepted evidence, write `UNAVAILABLE_FROM_ACCEPTED_EVIDENCE` and explain exactly what would be needed. Do not invent RMB/yuan interpretation or conversion.

## Required scientific questions

Answer:

1. Do the nine real-composite-wage HJB calls remain legal and converged?
2. Which `(ra,w)` points produce interior, ambiguous, lower, upper or pathological stationary distributions?
3. Does the health frontier at `w=13–18` differ materially from the earlier `w=.8–1.3` scans?
4. Is any `ra` among `.06/.0675/.07` robustly interior at all three real-scale wages?
5. What are the aggregate ranges for any interior candidates?
6. What model transformations explain the large numerical gap between `wjt≈O(1)` and household composite wage `w≈O(10)`?
7. What are the supported orders of magnitude for provincial GDP, per-capita GDP and household composite/average wage?
8. Are those three objects in a common interpretable monetary scale, normalized model scale, or unresolved mixed scale?
9. Is it scientifically defensible to modify `wjt` bounds now? If not, what exact scale/recalibration evidence is missing?
10. If the new scan is poor, which upstream relationship most clearly needs joint recalibration review: `wjt→w`, return mapping→`ra`, macro output scaling, or multiple jointly?

## Recalibration trigger and sole next gate

If real-scale scan is broadly healthy and dimensional audit is coherent, recommend exactly one next Owner gate for conservative provincial-state projection against the expanded observed map.

If scan is broadly nonconvergent/pathological or the macro scale remains dimensionally unresolved, recommend exactly one joint recalibration Owner gate that requires `wjt`, household `w`, `ra/rah`, provincial GDP, per-capita GDP and investment/output normalizations to be checked together before changing parameter ranges.

Do not execute the successor.

## Runtime budget

- HJB calls exactly 9 unless shared provenance blocker;
- KFE calls <=9 and only once after each converged HJB;
- scientific retries 0;
- engineering retry <=1 before first HJB only, with unchanged science;
- global outer turns 0;
- firm runtime 0;
- MATLAB runtime 0;
- K1B/K2/GE/downstream/shock/IRF/Results all 0.

## Required outputs

Create:

- `docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit/`;
- task-owned runner/finalizer/tests as needed;
- truthful CURRENT closeout docs.

Compact evidence should include at least:

- `input_invariance_receipt.json`;
- `points.csv`;
- `point_receipts.json`;
- `marginals.json`;
- `macro_scale_trace.json`;
- `macro_scale_summary.csv`;
- `source_identity.json`;
- `call_ledger.json`;
- sealed manifest.

## Git workflow

Fresh-fetch live main and record actual baseline. Use a fresh isolated worktree/branch. No reset/clean/stash/force push. Explicit staging only; no `git add .`/`git add -A`.

One coherent Builder commit, non-force push, one remote readback. Do not merge main and do not publish a successor task.

## Final response

Return terminal classification first, then baseline/branch/worktree/candidate SHA, changed paths, exact scan, complete HJB/KFE ledger, 3×3 classification, per-point receipts, macro-scale audit, supported GDP/per-capita-GDP/household-wage magnitudes, normalization/multiplier findings, whether `wjt` bounds may be reconsidered, exactly one next Owner gate, KFE caveat, and `Results eligibility=FALSE`.

Stop for independent ChatGPT Reviewer acceptance.
