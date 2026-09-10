# Chapter 5 MP4C G1 residual-GovInv initialization integration and isolated 25-turn diagnostic

Date: 2026-09-11. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Implement a separately named diagnostic corrected-2018 successor initialization route that replaces only the historical G0 start

`GovInv0 = Ktarget`

with the accepted diagnostic G1 rule

`GovInv0 = max(Ktarget - Kt_supply_initial, 0)`

where `Kt_supply_initial` is observed by exactly one predeclared household initialization pass and one existing At-only capital allocation under `beta_a=1` labelled `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`.

After zero-science implementation tests pass, run exactly one bounded 25-turn corrected-2018 trajectory to isolate the effect of the G1 initialization. Keep the historical GovInv controller unchanged. Do not simultaneously activate the newly accepted normalized-labor successor route in this task; preserve the same source-faithful labor route used by the accepted G0 25-turn comparison so the effect of GovInv initialization remains attributable.

This is a diagnostic integration, not production calibration and not Results.

## 2. Required authority

Fresh-read live `origin/main`, then at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE_REPORT.md`;
- `docs/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE_ACCEPTANCE.md`;
- accepted corrected-2018 runtime binding report/acceptance;
- accepted 25-turn G0 HJB-propagation/KL rerun report/acceptance;
- accepted GovInv/labor redesign spec/acceptance;
- accepted origin-preserving bilateral labor normalization implementation/acceptance;
- current corrected-2018 runtime, capital allocation, household/HJB/KFE and steady-state harnesses;
- protected MATLAB `HANK_mp_1eq.m`, `HANK_mp_1turn.m`, `HANK_firm.m` if locally accessible, read-only.

## 3. Frozen corrected-2018 data and numerical contract

Use the accepted active corrected-2018 route:

- actual 2018 GDP and population;
- raw-NBS GFCF Track-A PIM capital;
- `delta_pim=.096`;
- `alpha=.7380939146868483`;
- `MU=10万元`, `NU=100 persons`;
- same-year `Zt0`;
- firm depreciation `.025`;
- price bounds unchanged;
- source-lagged `rah` timing unchanged;
- HJB/KFE equations, tolerances, grids, solver families unchanged;
- `beta_a=1` only as `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`.

No parameter may be tuned after science starts.

## 4. Phase A: implement diagnostic G1 initializer with zero science

Add a separately named initializer/runtime route. Do not silently alter the source-faithful G0 route.

The G1 route must:

1. build and validate the accepted corrected-2018 initial state;
2. fix the accepted initial household prices/states;
3. perform exactly one labelled initialization household observation pass when scientific execution is later authorized;
4. obtain `At_initial` for 31 provinces;
5. call the existing At-only capital allocation exactly once;
6. compute `Kt_supply_initial`;
7. compute `GovInv0_G1=max(Ktarget-Kt_supply_initial,0)`;
8. replace only the initial GovInv state in the successor trajectory state;
9. leave Y/K/N/alpha/Zt/rah/rb/w/wjt/ra/tau/Tt and all controller parameters unchanged.

The implementation must make the pre-pass and outer-turn stage explicit so the initialization observation cannot be mistaken for turn 1.

## 5. G1 state receipt

Before outer turn 1, persist a 31-province initialization receipt with:

- Ktarget;
- observed At/Bt/Lt/Ct;
- HJB/KFE classifications;
- Kt_supply_initial beta1;
- G0 GovInv for comparison;
- G1 GovInv;
- accounting firm-K under G0 and G1;
- beta-star diagnostic geometry;
- exact initial state variables passed into outer turn 1.

Assert for beta=1 that all 31 G1 initial accounting firm-K values equal Ktarget within deterministic tolerance unless private K exceeds target, in which case GovInv must be zero and the overshoot explicitly retained.

## 6. Historical controller frozen

Do not modify the source-style controller:

- same `maxKNratiogap<0.1` adaptation gate;
- same Zt adjustment ordering;
- same clipped `ra`-based GovInv update;
- same `< ramin+0.02 -> *0.9` and `> ramax-0.02 -> *1.1` behavior;
- same tKNratio update.

The task must distinguish initialization effects from later controller effects.

## 7. Labor route frozen for isolated comparison

For this task, use the same source-faithful migration/labor route as the accepted G0 25-turn trajectory.

Do not activate `run_origin_preserving_normalized_one_turn` in the scientific trajectory. The normalized labor implementation remains accepted but scientifically deferred here so that G0-vs-G1 differences cannot be attributed to two simultaneous changes.

Record this isolation choice explicitly.

## 8. HJB nonconvergence propagation

Use the accepted continuation contract:

- finite, structurally usable `converged=false` HJB returns continue as `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`;
- false flags remain false for final source convergence;
- nonfinite/malformed/unusable returns fail closed;
- KFE validity remains independently classified.

## 9. Scientific budget

One scientific process only.

Initialization stage maximum:

- 31 HJB;
- 31 KFE;
- 31 aggregates;
- 1 At-only capital allocation.

Then exactly one trajectory, maximum:

- 25 outer turns;
- 775 province household updates.

No second trajectory, no second initialization observation, no beta cell, no parameter tuning, no scientific retry.

Engineering retry is allowed only before any scientific state advances and must be logged.

## 10. Required per-turn diagnostics

For each completed outer turn record at least:

- HJB converged/nonconverged counts and names;
- KFE classifications;
- raw/used ra and wage boundary counts;
- private K supply;
- GovInv before/after controller;
- total firm K;
- Ktarget;
- private/GovInv/total K ratios;
- KN gap;
- Y/Yprev gap;
- GDP level gap;
- Zt changes;
- controller GovInv increase/decrease/hold counts;
- At/Bt/Lt/Ct;
- source final predicate components.

## 11. G0 vs G1 comparison

Use the already accepted G0 25-turn evidence as historical comparison. Do not rerun G0.

At turns 1, 2, 3, 5, 10, 15, 20, 21, 22, 23, 24, 25 compare where available:

- median and min/max total K/Ktarget;
- median GovInv/Ktarget;
- median private K/Ktarget;
- ra lower/interior/upper counts;
- max KN gap;
- max GDP level gap;
- GovInv controller action counts;
- HJB convergence count.

Focus especially on whether G1 prevents the early `Ktarget + private K` duplication and whether the unchanged controller subsequently recreates a material GovInv overshoot.

## 12. Required scientific questions

Answer directly:

1. Does G1 produce an initial accounting K exactly at target for 31/31 under beta=1?
2. Does outer turn 1 still begin materially closer to target than G0?
3. Does the unchanged controller preserve that improvement, erode it, or reverse it over 25 turns?
4. By turns 20-25, what are total K/Ktarget, GovInv/Ktarget, and private K/Ktarget distributions?
5. Are ra boundary-hit counts improved relative to accepted G0 history?
6. Does `rah` remain in a materially more plausible/interior path, or still collapse/hit a problematic regime?
7. Are KN/Y/GDP paths less oscillatory or still unstable?
8. Is the current controller now the dominant remaining capital-side instability mechanism?
9. Do HJB/KFE blockers remain independent?
10. Is there enough evidence to justify a separate controller-redesign task without yet changing the controller here?

Do not equate a better trajectory with production validity.

## 13. Required outputs

At minimum:

- diagnostic G1 successor initializer/runtime source;
- focused zero-science tests;
- `docs/CH5_MP4C_G1_RESIDUAL_GOVINV_INITIALIZATION_INTEGRATION_AND_25TURN_ISOLATED_DIAGNOSTIC_REPORT.md`;
- `reports/mp4c_g1_residual_govinv_25turn_isolated_20260911/initialization_receipt_31province.csv`;
- `.../national_initialization_summary.json`;
- `.../province_turn_capital_ledger.csv`;
- `.../national_turn_summary.csv`;
- `.../g0_vs_g1_selected_turn_comparison.csv`;
- `.../anhui_trace.csv`;
- `.../hjb_convergence_path.csv`;
- `.../scientific_validity_ledger.csv`;
- `.../controller_action_summary.csv`;
- `.../call_ledger.json`;
- runtime/source hash receipts;
- focused/static test receipts;
- manifest/readback;
- bounded invocation receipt.

## 14. Allowed verdicts

- `G1_RESIDUAL_GOVINV_25TURN_PASS__INITIAL_CAPITAL_ALIGNMENT_IMPROVES_AND_BOUNDED_PATH_QUANTIFIED`
- `G1_RESIDUAL_GOVINV_25TURN_PARTIAL__INITIAL_ALIGNMENT_VALID_BUT_TRUE_HARD_FAILURE_BEFORE_LATE_WINDOW`
- `G1_RESIDUAL_GOVINV_25TURN_FAIL__INITIAL_ALIGNMENT_VALID_BUT_UNCHANGED_CONTROLLER_RECREATES_OR_WORSENS_INSTABILITY`
- `G1_RESIDUAL_GOVINV_INTEGRATION_BLOCKED__INITIALIZATION_OBSERVATION_CANNOT_BE_SAFELY_SEPARATED_FROM_OUTER_STATE`

These describe diagnostic behavior only.

## 15. Git boundary

Use a dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit and non-force push candidate;
- do not merge main;
- do not publish successor task;
- do not activate normalized labor in this scientific run;
- Results eligibility remains FALSE.

Return to ChatGPT Reviewer with verdict, branch, candidate SHA, Phase-A tests, initial G1 receipt summary, completed turns, G0-vs-G1 comparison, controller behavior, HJB/KFE validity, call ledger, and report path.
