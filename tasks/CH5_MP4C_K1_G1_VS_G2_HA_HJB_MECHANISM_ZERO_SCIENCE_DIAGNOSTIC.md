# CH5 MP4C K1 — G1 vs G2 HA/HJB mechanism zero-science diagnostic

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: zero-science forensic/mechanism diagnostic.
Issuer: ChatGPT Reviewer after acceptance of candidate `ab6b19022d920a8929a2ee66cc5511be6f602557`.

## 1. Goal

Explain why widening the annual HJB illiquid-return safeguard from G1 `[-.05,.20]` to G2 `[-.10,.35]` restores partial cross-province return heterogeneity but reduces treatment HJB convergence from `18/124` to `6/124` and amplifies several transfer/adjustment-cost/drift extrema.

This task must use already persisted G1/G2 evidence and source inspection only. It must not run the model.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`, record actual SHA, verify this task remains active, then read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_ACCEPTANCE.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_REPORT.md`;
- compact G1/G2 evidence and, where needed, immutable external evidence referenced by the report;
- accepted HJB/KKT/boundary authority docs;
- active HJB/household source defining value derivatives, consumption FOC, transfer FOC, adjustment cost, drift construction, policy selection and boundary handling.

Do not restart historical parity, data, provenance, annual-calibration or K1 capital-network audits.

## 3. Scientific call budget

All new scientific/model calls must be zero:

- trajectory / outer turn: `0`;
- HJB: `0`;
- KFE: `0`;
- household runtime: `0`;
- firm runtime: `0`;
- MATLAB runtime: `0`;
- K1B/K2/GE/annual downstream/shock/IRF/Results: all `0`.

Allowed operations: persisted JSON/CSV/NPZ reads, hashing/readback, static NumPy/pandas calculations, source tracing, zero-science tests and report generation.

## 4. Matched G1/G2 panel

Use treatment turns 2-5 only for mechanism attribution, with turn 1 retained only as the exact common-bootstrap reference.

Match observations by:

- province;
- turn;
- and, where HJB arrays permit, `(i_b,i_a,i_z)` cell.

Do not compare unmatched path states as if they were same-state causal experiments. Distinguish:

- same province/turn path comparison;
- exact matched grid-cell comparison within each saved HJB result;
- path-history divergence.

All causal wording must remain conservative: this is a controlled guard-design comparison but state paths diverge after treatment begins.

## 5. Convergence-switch localization

Build province-turn classifications:

- converged in both G1/G2;
- G1 converged -> G2 nonconverged;
- G1 nonconverged -> G2 converged;
- nonconverged in both.

Report:

- all switch province names by turn;
- provinces repeatedly losing convergence under G2;
- iteration-ceiling hits;
- HJB statistic G2-G1 differences and ratios where defined;
- whether return saturation status (upper-hit vs unsaturated) predicts convergence-switch direction descriptively.

No post-hoc PASS threshold.

## 6. Return exposure and guard-regime transition

For every province-turn record:

- raw annual firm `ra0`;
- converted `rah_annual_raw`;
- G1 consumed `r_a`;
- G2 consumed `r_a`;
- G1/G2 upper/lower/unsaturated state;
- delta in consumed `r_a` from G1 to G2.

Partition G2 treatment observations into at least:

A. still upper-saturated at `.35`;
B. newly unsaturated under G2 after being G1-upper-saturated;
C. any lower-hit observations, if they exist.

Compare HJB/control/drift diagnostics between A and B descriptively. Determine whether the worst G2 instability is concentrated in newly unsaturated observations, still-saturated observations, or mixed.

## 7. Wage-safeguard interaction

The wage safeguard remains fixed at `[.8,1.3]` and must not be changed.

For each province-turn combine return-regime status with wage status:

- wage upper hit;
- wage lower hit;
- wage unsaturated.

Construct cross-tabs such as:

- G2 return unsaturated + wage upper;
- G2 return unsaturated + wage lower;
- G2 return unsaturated + wage unsaturated;
- G2 return upper + wage upper/lower/unsaturated.

Test descriptively whether convergence loss or large HJB statistics cluster in particular joint price-guard regimes.

This does not authorize a wage-relaxation conclusion by itself.

## 8. HJB cell-level mechanism localization

If persisted arrays support it, analyze G1/G2 HJB arrays for:

- value function `V`;
- consumption;
- labor;
- transfer `d`;
- adjustment cost;
- effective illiquid return;
- `mu_a`, `mu_b`;
- utility;
- liquid and transfer policy labels;
- any persisted value derivatives or directional derivatives;
- raw drift objects where available.

For each treatment turn identify top extreme cells for G2 and matched G1 values. Report province, turn, grid index/coordinate if recoverable from accepted grid authority, labels, boundary/interior status, G1 value, G2 value, difference and ratio where meaningful.

At minimum localize:

- top `|d|`;
- top adjustment cost;
- top `|mu_a|`;
- top `|mu_b|`;
- cells associated with worst HJB statistics where cell-level context is available.

## 9. Policy-branch transitions

Determine whether widening G1->G2 systematically changes policy branches/labels.

Count matched cell transitions such as:

- liquid label F->B, B->F, etc.;
- transfer label F->B, B->F, Z/other accepted labels as applicable.

Identify whether extreme G2 cells disproportionately occur in one branch transition.

Do not infer economic meaning from label letters without tracing accepted source definitions.

## 10. Boundary versus interior

Classify extreme/stressed cells by:

- lower-a;
- upper-a;
- lower-b;
- upper-b;
- interior.

Report G1 vs G2 outward-drift counts already derivable from persisted arrays and determine whether G2 deterioration is:

- primarily interior;
- primarily boundary-linked;
- or mixed.

Existing accepted drift tolerance must be respected. Exact-sign floating noise below tolerance must not be promoted to a material boundary failure.

Standalone KKT residual remains `UNAVAILABLE_IN_ACCEPTED_EVIDENCE` unless it is already persisted. Do not construct a new KKT PASS/FAIL from proxies.

## 11. Source-law trace

Give exact source-path/line evidence for the accepted chain from HJB `r_a` to numerical stress, including as available:

`r_a` -> effective illiquid return -> value derivatives / Hamiltonian objects -> transfer FOC -> `d` -> adjustment cost -> `mu_b` / `mu_a` -> policy selector / boundary selector -> HJB update/statistic.

Also trace wage entry into household liquid drift/labor-income terms so the report can distinguish return-guard and wage-guard channels.

Do not redesign equations.

## 12. Descriptive associations

Allowed descriptive statistics include Pearson/Spearman/rank tables among:

- consumed `r_a` change G2-G1;
- converted raw `rah`;
- wage raw/guarded level and boundary-hit state;
- HJB statistic;
- iteration ceiling;
- transfer/cost/drift maxima;
- policy-transition counts;
- boundary/outward counts.

Label every such statistic `DESCRIPTIVE_ONLY_NOT_CAUSAL`.

## 13. Required attribution split

The report must explicitly separate:

A. stress already present under G1;

B. G2 incremental stress after widening the return safeguard;

C. G2 observations that improve relative to G1;

D. stress associated with return-unsaturated states;

E. stress associated with still-binding wage safeguard;

F. unresolved interaction where persisted evidence cannot distinguish channels.

Do not attribute all G2 deterioration to return levels if wage/path-history evidence does not support that claim.

## 14. Final classification

Give one precise evidence-based classification, for example:

- `G2_CONVERGENCE_LOSS_CONCENTRATED_IN_NEWLY_UNSATURATED_RETURN_REGIMES_THROUGH_TRANSFER_COST_AMPLIFICATION__CALIBRATION_GATE_REQUIRED`;
- `G2_STRESS_PRIMARILY_ASSOCIATED_WITH_JOINT_RETURN_AND_WAGE_GUARD_REGIMES__PRICE_INTERFACE_RECALIBRATION_REQUIRED`;
- `G2_STRESS_REMAINS_MIXED_AND_NOT_IDENTIFIABLE_FROM_PERSISTED_EVIDENCE__BOUNDED_INSTRUMENTATION_TASK_REQUIRED`;
- or a more exact truthful variant.

Do not recommend G3 merely because G2 remains saturated.

## 15. Exactly one next gate

Choose exactly one based on evidence:

A. Owner scientific calibration decision on HA/HJB transfer-cost parameters or price-interface calibration;

B. bounded diagnostic runtime with additional instrumentation but no scientific parameter change, only if critical mechanism data are absent from persisted evidence;

C. return continuation remains viable but requires a newly frozen intermediate guard, only if evidence clearly supports that conclusion;

D. source/boundary authority review, only if an unresolved equation-authority defect is found.

Do not authorize longer G2, G3/G4, wage relaxation, K1B, K2, steady-state acceptance or Results inside this task.

## 16. Allowed tracked changes

Allowed:

- one zero-science mechanism analyzer;
- focused zero-science tests;
- report `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_mechanism/`;
- truthful CURRENT closeout docs if required.

Forbidden:

- any production `src/` scientific change;
- parameter or guard changes;
- HJB/KFE/boundary/KKT equation changes;
- annual calibration changes;
- wage-guard changes;
- capital-network/C1/labor science changes;
- grid/tolerance/solver changes;
- model runtime of any kind;
- K1B/K2/Results.

## 17. Git/local safety

Use a fresh isolated worktree from live main. Protect all accepted external evidence and source files. No reset/clean/stash/force push. Explicitly stage paths; no `git add .` or `git add -A`. One coherent commit, non-force push, one remote commit/report readback. Do not merge main and do not publish a successor task.

## 18. Final response

Return:

- classification;
- actual live-main baseline;
- worktree/branch/candidate SHA;
- changed paths;
- zero scientific-call ledger;
- convergence-switch localization;
- return-regime partition findings;
- wage-interaction findings;
- cell-level extreme findings;
- policy-branch transition findings;
- boundary/interior attribution;
- source-law trace;
- descriptive associations;
- G1-baseline vs G2-incremental attribution;
- KKT availability;
- exactly one recommended next gate;
- KFE caveat;
- Results eligibility=`FALSE`.

Stop. Do not run the model and do not enter G3/K1B/K2.
