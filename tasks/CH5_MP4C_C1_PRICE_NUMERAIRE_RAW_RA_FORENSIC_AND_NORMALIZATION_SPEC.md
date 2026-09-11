# Chapter 5 MP4C C1 price/numeraire and raw-ra upper-pressure forensic/spec

Date: 2026-09-11

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Use the accepted C1 25-turn evidence to identify why raw firm return `ra0` remains above the historical upper bound in 30/31 provinces at turn 25 even though C1 holds productive capital at the corrected 2018 target. This is a zero-science forensic/specification task.

The task must separate:

- economic return level implied by corrected Y/K and current labor/productivity;
- historical numerical clipping bounds `[ramin,ramax]`;
- firm wage and household composite-wage numeraires;
- the role of `mt`, `rk`, profit, depreciation and taxes in `ra0`;
- whether `ra0` pressure is a true economic-level implication or a unit/numeraire mismatch.

Do not change any production parameter or run any scientific model call.

## 2. Required authority

Fresh-read live `origin/main`, then read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- accepted C1 25-turn report and acceptance;
- accepted firm-price normalization forensic/report;
- accepted corrected-2018 initialization/unit reports;
- accepted GovInv controller forensic/spec;
- `src/ch5_two_asset_hank/multi_province/firm.py`;
- `src/ch5_two_asset_hank/multi_province/wage.py`;
- corrected runtime and current C1 integration source;
- protected MATLAB `HANK_firm.m`, `wage_caculate.m`, and surrounding caller code if locally accessible, read-only.

## 3. Zero-science boundary

Do not call:

- HJB/KFE/household;
- migration or normalized migration;
- firm runtime on new states;
- wage runtime on new states;
- controller runtime;
- outer turn/trajectory/steady state;
- MATLAB runtime;
- root/Brent;
- GE/annual/IRF/Results.

Allowed: static source inspection, accepted-ledger parsing, deterministic algebraic decomposition of already-saved rows, unit conversions, tests, hashes, serialization.

## 4. Accepted facts to freeze

The accepted C1 path already establishes:

- turns 20–25 firm total K/target exactly 1;
- no private-K floor binding;
- turn-25 raw-ra lower/interior/upper = `0/1/30`;
- pooled rah remains near the historical upper region;
- KN/Y/GDP paths improve strongly;
- Zt adjustments cease in the late window;
- late HJB is 31/31 converged;
- KFE remains independently diagnostic-only.

Do not reopen the GovInv residual definition in this task.

## 5. Exact `ra0` decomposition

For every accepted C1 province-turn row for which the necessary saved objects are available, reconstruct from source equations the components of:

`ra0 = rk - delta + profit*(1-corptau)/Kt`

and:

`rk = mt * alpha / (Kt/Yt)`.

Persist separately:

- `Yt/Kt`;
- `Kt/Yt`;
- `mt`;
- `alpha`;
- `rk`;
- `delta`;
- profit/K;
- after-tax profit/K contribution;
- `ra0`;
- clipped `ra`;
- distance from `ramax`;
- clipping amount.

Static reconstruction must match the accepted saved raw `ra0` to deterministic tolerance. If required components are not in the saved ledger, identify the exact missing object instead of fabricating it.

## 6. Return-level benchmark geometry

Statically derive the implied `K/Y` required for selected return levels under simplified and full decompositions, clearly separated:

- pure marginal-product term `mt*alpha*Y/K`;
- `rk-delta`;
- full `ra0` including after-tax profit/K.

Do not choose a new `ra_target`.

At minimum report what K/Y would correspond to:

- current `ramin=.02`;
- current `ramax=.09`;
- observed accepted corrected-2018 K/Y.

These are geometry/comparison objects only, not calibration recommendations.

## 7. Bounds provenance

Recover whether `ramin=.02`, `ramax=.09`, wage `[.8,1.3]` have explicit economic/data provenance or are historical numerical safeguards.

Classify each as one of:

- `ECONOMICALLY_IDENTIFIED`;
- `EMPIRICAL_NUMERICAL_SAFEGUARD`;
- `SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`;
- `UNKNOWN`.

Do not silently promote a safeguard into a structural target.

## 8. Wage/numeraire chain

Recover the dimensional chain for:

- firm raw wage `wt0`;
- clipped firm wage `wjt`;
- household composite wage `w`;
- population/labor units;
- GDP/capital MU units;
- any implicit period scaling.

Explain whether firm wage and household wage are directly comparable levels. Reconcile this with the earlier accepted finding that the initial firm wage raw level was far above `[.8,1.3]` while household composite wage was around 18.

## 9. Static counterfactuals allowed

Using accepted saved C1 rows only, calculate deterministic counterfactual classifications such as:

- fraction of ra0 explained by `rk-delta` vs profit/K;
- number of provinces that would remain above `.09` if profit contribution were zero;
- number that would remain above `.09` if `mt` were set to the source steady markup `mstar` only, **only if this is pure algebra on saved Y/K and not a new model call**;
- sensitivity of ra0 to K/Y holding other saved components fixed.

These are diagnostics, not parameter recommendations.

## 10. No tuning

Do not choose or alter:

- alpha;
- delta;
- epsilon/theta;
- ramin/ramax;
- wage bounds;
- Zt;
- Ktarget;
- beta_a;
- labor normalization;
- controller gains;
- any price normalization scalar.

## 11. Required questions

The report must answer:

1. Why are 30/31 raw-ra values above `.09` at C1 turn 25 when K is correctly held at target?
2. Is the upper-pressure mainly from corrected empirical Y/K, `mt`, profit/K, depreciation, or another source term?
3. Are `.02/.09` economically identified return bounds or historical numerical safeguards?
4. Would simply widening/removing the clips be economically justified by current evidence? Answer `YES/NO/INSUFFICIENT_EVIDENCE` and explain.
5. Is there evidence of a firm-price/household-wage numeraire mismatch that can contaminate the return path indirectly?
6. Does normalized labor need to be activated before price/return units are resolved, or should price/numeraire identification remain the next gate?
7. What is the lowest-risk next scientific experiment after this forensic?

## 12. Outputs

At minimum:

- `docs/CH5_MP4C_C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_AND_NORMALIZATION_SPEC.md`;
- `reports/mp4c_c1_price_numeraire_raw_ra_forensic_20260911/ra0_component_ledger.csv`;
- `.../turn25_ra0_component_summary.csv`;
- `.../return_bound_provenance.md`;
- `.../wage_numeraire_dimensional_chain.csv`;
- `.../ky_return_geometry.csv`;
- `.../static_counterfactual_summary.json`;
- `.../owner_decision_matrix.csv`;
- zero-scientific-call ledger;
- source/hash receipt;
- focused-static-test receipt;
- manifest/readback.

## 13. Allowed verdicts

- `C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_PASS__RETURN_PRESSURE_DECOMPOSED_AND_NEXT_GATE_IDENTIFIED`
- `C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_PARTIAL__KEY_UNIT_OR_SOURCE_OBJECT_REMAINS_UNIDENTIFIED`
- `C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_BLOCKED__ACCEPTED_EVIDENCE_INSUFFICIENT_FOR_STATIC_DECOMPOSITION`

PASS/PARTIAL do not authorize a new price normalization, clip change, labor activation, or production trajectory.

## 14. Git boundary

Dedicated branch/worktree; no force push/reset/clean/stash; preserve unrelated files; explicit staging only; commit and non-force push; do not merge main; do not publish successor scientific task; Results eligibility remains FALSE.

Return verdict, branch, candidate SHA, raw-ra decomposition summary, bound provenance, wage/numeraire conclusion, remaining Owner decisions, lowest-risk next experiment, and report path.
