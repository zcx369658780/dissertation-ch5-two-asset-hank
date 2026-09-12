# CH5 MP4C K1 — transfer-control admissibility safeguard zero-science design

Date: 2026-09-13.
Task ID: `CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: zero-science numerical-contract design.

## 1. Goal

Use only already accepted G1/G2 instrumented evidence to design a first preregistered **temporary transfer-control admissibility safeguard ladder** for the HA/HJB transfer candidate `d`.

This task does not run the model and does not activate any transfer bound.

The design must identify a defensible numerical continuation region that preserves ordinary transfer candidates while isolating the finite explosive tail that drives extreme quadratic adjustment costs.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`, record actual SHA, and verify this exact task remains active. Read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_TRANSFER_CONTROL_TEMPORARY_ADMISSIBILITY_SAFEGUARD_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`;
- `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC_REPORT.md`;
- compact instrumented evidence under `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_instrumented/`;
- active transfer FOC / adjustment-cost / policy source needed to interpret candidate semantics.

Do not redo capital-network, annual-time-base, data, parity, or prior G1/G2 audits.

## 3. Scientific call budget

All new scientific/model calls must be zero:

- trajectory: 0;
- outer turn: 0;
- HJB: 0;
- KFE: 0;
- household runtime: 0;
- firm runtime: 0;
- MATLAB runtime: 0;
- K1B: 0;
- K2: 0;
- GE: 0;
- annual downstream: 0;
- shock/IRF: 0;
- Results: 0.

Allowed: static reads, hashing, NumPy/pandas analysis of accepted evidence, symbolic/unit analysis, focused zero-science tests, and report/evidence generation.

## 4. Frozen science

Do not change or numerically retune:

- `chi0=.1`;
- `chi1=2 years`;
- annual calibration;
- `delta=.10`;
- `rho=.05`, `rb=.02`, borrowing gap `.07`;
- G1/G2 return guards;
- `wjt [.8,1.3]` wage guard;
- derivative floor;
- transfer FOC;
- HJB/KFE equations;
- selector/boundary/KKT laws;
- grid/tolerance/solver;
- K1 network/C1/labor science.

The task designs a safeguard only. It does not authorize implementation or runtime.

## 5. Candidate populations

From accepted instrumented traces, distinguish at minimum:

1. raw pre-selector transfer candidates by branch where persisted, e.g. `d_bb`, `d_bf`, `d_fb`, `d_ff` or the exact active-source names;
2. finally selected `d`;
3. province/turn/cell identity;
4. HJB iteration number;
5. G1 versus G2;
6. turn 2 common-entering-state versus turns 3–5 path-history propagation;
7. interior versus asset-boundary cells;
8. return-guard status;
9. wage-guard status;
10. converged versus nonconverged HJB calls.

Do not merge conceptually different candidate objects into one distribution without retaining branch identity.

## 6. Distribution diagnostics

For each relevant raw-candidate population and selected-control population, report where evidence permits:

- count;
- finite / NaN / Inf count;
- min / max;
- median;
- p50, p75, p90, p95, p97.5, p99, p99.5, p99.9;
- the same percentiles for `abs(d)`;
- positive/negative shares;
- positive-tail and negative-tail quantiles separately;
- largest finite values with province/turn/iteration/grid-cell identities.

Because extreme tails may dominate means/standard deviations, do not rely on mean ± kσ as the primary design rule.

## 7. Ordinary-region versus explosive-tail analysis

Identify whether the accepted evidence shows a visible scale separation between ordinary transfer candidates and explosive finite candidates.

Use descriptive tools such as:

- log10(abs(d)+epsilon) empirical distributions;
- quantile spacing;
- top-tail order statistics;
- gap ratios between adjacent ordered magnitudes;
- candidate-to-selected comparison;
- corresponding adjustment-cost magnitudes;
- corresponding HJB statistic / convergence state;
- turn-2 common-state examples.

Any proposed separation must be labelled `DESCRIPTIVE_NUMERICAL_CONTINUATION_DESIGN`, not a structural economic threshold.

Do not choose a cutoff solely because it would have made a previously failed HJB call converge; no counterfactual runtime exists in this task.

## 8. Symmetry audit

Before proposing symmetric `[-D,D]` bounds, test whether positive and negative transfer-candidate tails have materially different empirical scales.

Report:

- positive-tail quantiles;
- absolute negative-tail quantiles;
- extreme-sign frequencies;
- whether the largest explosions are predominantly one-sided;
- whether branch identity explains sign asymmetry.

If evidence is materially asymmetric, propose asymmetric candidate ladders or explicitly state that a symmetric ladder is only a simplification candidate requiring Owner approval.

## 9. Asset/grid scale context

Compare candidate transfer magnitudes with existing household model-unit scales without assigning structural meaning:

- `a` grid span and local `a` level;
- `b` grid span;
- annual consumption/labor-income/transfer-flow magnitudes if already persisted;
- one-period/continuous-time drift interpretation under the frozen annual HJB contract;
- adjustment-cost magnitude generated by candidate `d` under `chi0=.1`, `chi1=2`.

The purpose is to detect numerically absurd continuation scales, not to derive an economic portfolio-turnover restriction from the grid.

## 10. Candidate safeguard semantics

The report must compare at least these numerical semantics without implementing them:

### A. Candidate rejection

Raw FOC candidate outside admissible interval is marked inadmissible and excluded from selector competition. Raw value persists.

### B. Candidate clipping

Raw candidate is clipped to the admissible interval before selector/cost/drift evaluation. Raw and clipped values persist.

### C. Fallback-to-zero / no-transfer candidate

Out-of-range candidate is excluded and the existing zero-transfer candidate remains available according to accepted selector semantics.

For each, discuss:

- whether it preserves the accepted FOC candidate as a receipt;
- whether it changes candidate ranking semantics;
- continuity/discontinuity at the threshold;
- compatibility with existing `F/B/0` selector structure;
- whether it risks fabricating a candidate that does not satisfy the FOC;
- whether an Owner decision is needed.

Do not implement any of A/B/C in this task.

## 11. Ladder design

Propose a small preregistered ladder for future continuation, preferably 3–4 stages plus OFF where evidence supports it.

Each proposed stage must state:

- exact candidate interval(s);
- symmetric or asymmetric;
- expected hit share **computed statically on accepted raw candidates only**;
- branch-specific hit shares;
- G1/G2 and turn-2 hit shares;
- number of accepted raw candidates preserved unchanged;
- number classified inadmissible under the proposed rule;
- whether the stage preserves the central ordinary region identified above.

The ladder should progressively relax toward OFF. It must not be selected by optimizing a convergence outcome.

If the accepted evidence does not support exact numerical ladder values with adequate confidence, return `NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED` and provide bounded candidate ranges/options rather than inventing precision.

## 12. Priority checkpoints

Explicitly evaluate proposed candidate intervals against:

- 湖北 turn 2 extreme interior cell;
- 山东 turn 2 high-statistic case;
- 广东 turn 2 large cross-path amplification case;
- 四川 turn 4 later-history worst-HJB case;
- 云南 turn 4 G1-extreme / G2-improved case.

For each proposed stage, show whether the raw extreme candidate would be admissible, inadmissible, or clipped under each candidate semantic.

Do not claim that blocking an extreme would make the HJB converge.

## 13. Price-bound interaction

Keep return/wage safeguards conceptually separate.

For raw transfer-candidate hits under proposed intervals, cross-tab descriptively against:

- return upper/lower/unsaturated status;
- wage upper/lower/unsaturated status.

This is `DESCRIPTIVE_ONLY_NOT_CAUSAL`.

The transfer-control safeguard must not be used to hide the existing price-bound saturation problem.

## 14. Final decision table

Provide a compact candidate table containing, for each proposed safeguard design:

- semantics A/B/C;
- interval;
- static raw-candidate hit share;
- selected-control hit share;
- branch coverage;
- sign symmetry assessment;
- central-mass preservation;
- continuity property;
- FOC fidelity;
- selector fidelity;
- implementation complexity;
- strongest scientific caveat.

Then identify exactly one preferred design for Owner/Reviewer freeze **or** state that no unique preferred design is supported.

## 15. Final classification

Choose one precise truthful classification, e.g.:

- `TRANSFER_CANDIDATE_EXPLOSIVE_TAIL_SEPARATED_FROM_CENTRAL_REGION__TEMPORARY_REJECTION_LADDER_IDENTIFIED__OWNER_NUMERIC_FREEZE_REQUIRED`;
- `TRANSFER_CANDIDATE_TAIL_ASYMMETRIC__ASYMMETRIC_CONTINUATION_LADDER_RECOMMENDED__OWNER_FREEZE_REQUIRED`;
- `TRANSFER_CANDIDATE_DISTRIBUTION_HAS_NO_STABLE_SCALE_BREAK__NUMERIC_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED`;
- or a more precise evidence-based variant.

Classification itself does not authorize runtime.

## 16. Exactly one next gate

Recommend exactly one:

1. Owner/Reviewer freeze of exact safeguard semantics + numeric ladder, followed by a bounded runtime;
2. additional zero-science design if evidence is incomplete;
3. source-authority review if a genuine transfer-FOC contract inconsistency is found.

Do not authorize runtime yourself.

## 17. Allowed tracked changes

Allowed:

- one zero-science analyzer;
- focused zero-science tests;
- report `docs/CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_transfer_control_admissibility_design/`;
- truthful CURRENT closeout docs.

Forbidden:

- any `src/` scientific change;
- any parameter/guard implementation;
- any new transfer bound activation;
- `chi0/chi1` change;
- derivative-floor change;
- return/wage guard change;
- solver/grid/tolerance/equation/boundary change;
- model runtime;
- K1B/K2/Results.

## 18. Git/local safety

Fresh isolated worktree from live main. Explicit stage paths. No `git add .` / `git add -A`. No reset/clean/stash/force push. Preserve accepted external evidence. One coherent commit, non-force push, one remote commit/report readback. Do not merge main and do not publish a successor task.

## 19. Final response

Return:

- classification;
- actual baseline, branch/worktree/candidate SHA;
- changed paths;
- zero scientific-call ledger;
- raw-candidate distribution diagnostics;
- selected-control diagnostics;
- ordinary-region/explosive-tail finding;
- symmetry audit;
- asset/grid-scale context;
- A/B/C safeguard-semantics comparison;
- proposed ladder with exact static hit shares if justified;
- priority-checkpoint adjudication;
- return/wage cross-tabs;
- preferred design or unresolved Owner choice;
- exactly one next gate;
- KFE caveat;
- Results eligibility=`FALSE`.

Stop. Do not run the model.
