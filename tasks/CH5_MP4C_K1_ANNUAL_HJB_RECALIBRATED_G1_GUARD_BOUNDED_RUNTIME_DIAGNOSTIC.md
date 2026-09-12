# CH5 MP4C K1 — annual HJB recalibrated G1-guard bounded runtime diagnostic

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: bounded scientific runtime diagnostic.
Issuer: ChatGPT Reviewer under Owner-approved annual recalibration contract.

## 1. Goal

Test the newly frozen annual continuous-time K1A calibration and determine whether the preregistered G1 HJB illiquid-return guard provides useful numerical scaffolding without breaking capital-network/accounting/provenance contracts.

This is the first bounded runtime after the annual time-base recalibration. It is not a steady-state acceptance run.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`, record actual SHA, and verify this task remains active. Read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE_ACCEPTANCE.md`;
- `docs/CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE_REPORT.md`;
- accepted K1 capital-network/scoring/payoff/bootstrap freezes;
- accepted raw-payoff safety/forensic reports;
- active firm/HJB/household/K1A runner source needed for bounded execution.

Do not restart earlier provenance, parity, distance or data audits.

## 3. Frozen annual contract

Use:

- `MODEL_TIME_BASE = ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`;
- `rb=.02/year`;
- borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`;
- productivity off-diagonal intensity `1/3 per year`;
- corrected annual `Y/K` and after-tax profit/K unchanged, with no `/4`;
- `ra0_annual = rk_annual + after_tax_profit_over_K_annual - .10`;
- `chi0=.1`, `chi1=2 years` as provisional annual calibration;
- annual wage/consumption/transfer/adjustment-cost flow interpretation in the unchanged household-model asset numeraire.

Do not use `.025`, `.0025` or PIM `.096` as firm/HJB depreciation in this task.

## 4. K1A contract

Both paths use only:

- pure-geographic `beta_distance=2.0`;
- `beta_return=0`;
- fixed `theta_i=inter_prv_ratio_i`;
- accepted destination-by-origin `S`;
- source-faithful labor;
- smoothing OFF;
- partial adjustment OFF;
- K1B OFF;
- K2 OFF;
- C1 `GovInv=max(Ktarget-Kprivate,0)`;
- same `S` for quantity and payoff.

## 5. Two-path design

Run exactly two paths from byte-identical accepted initialization.

### Path U — annual unguarded reference

- turn 1: common accepted entering payoff bootstrap;
- firm uses `delta=.10` from turn 1 onward;
- turns 2-5 HJB illiquid payoff uses same-path prior-completed annual `ra0 @ S` with no new HJB `r_a` guard.

### Path G1 — annual guarded diagnostic

- turn 1: same common accepted entering payoff bootstrap;
- firm uses `delta=.10` from turn 1 onward;
- turns 2-5 compute same-path prior-completed annual `ra0 @ S`;
- at the HJB interface only, guard converted annual `rah` to `[-0.05,0.20]`.

Both paths retain the existing firm `wjt` `[0.8,1.3]` guard only as temporary diagnostic scaffolding. Record its hit counts; do not modify it.

No other scientific input may differ between U and G1.

## 6. Three-layer receipts

For every province/turn where applicable persist separately:

1. raw annual firm `ra0_annual`;
2. converted annual portfolio payoff `rah_annual_raw = S' * ra0_annual`;
3. HJB payoff actually consumed:
   - U: equal to converted annual payoff;
   - G1: `clip(rah_annual_raw,-.05,.20)`.

Persist guard hit direction and saturation counts. Do not overwrite raw/converted objects with guarded values.

For wage, persist raw/current pre-guard value if available, guarded `wjt`, and lower/upper hit counts. If raw pre-guard wage is not available without changing scientific internals, report unavailable rather than redesigning firm equations.

## 7. Timing/bootstrap

Turn 1 is a common bootstrap and must be byte/scientifically identical across U/G1 except path label. No turn-1 difference is a guard effect.

Completed turn-1 firm state produces annual `ra0` under `delta=.10`. From turn 2 onward each path uses only its own immediately prior completed annual return state. No cross-path borrowing and no same-turn return feedback.

## 8. Pre-run gates

Before science prove:

1. live task/baseline identity;
2. annual contract values exactly match the freeze;
3. U/G1 starting payloads byte-identical apart from path/guard designation;
4. turn-1 common bootstrap identical;
5. firm depreciation is exactly `.10` in both paths;
6. annual raw `ra0` formula has no legacy `.02/.09` clip before portfolio aggregation;
7. U turn2 wiring = own turn1 annual raw `ra0 @ S`;
8. G1 turn2 wiring = same converted payoff, then HJB-interface clip `[-.05,.20]` only;
9. same-S quantity/payoff preserved;
10. existing `wjt [.8,1.3]` guard unchanged and classified diagnostic;
11. K1B/K2/smoothing/normalized labor OFF;
12. C1 unchanged;
13. no solver/grid/tolerance changes.

Any failure blocks science.

## 9. Runtime budget

Maximum:

- trajectory invocations: 2;
- U: at most 5 completed turns;
- G1: at most 5 completed turns;
- HJB calls: at most 310 total;
- KFE calls: at most 310 total;
- MATLAB: 0;
- standalone KFE: 0;
- K1B/K2/GE/annual/shock/IRF/Results: 0.

No scientific retry after state advancement. One pre-state-update engineering retry is allowed only for path/serialization/output-shape defects with byte-identical scientific inputs.

## 10. Stop conditions

Stop the affected path and preserve evidence on:

- NaN/Inf in HJB values, controls or key aggregates;
- scientific exception;
- same-turn return feedback;
- wrong prior-return provenance;
- same-S failure;
- capital-conservation failure beyond accepted tolerance;
- C1 accounting failure beyond accepted tolerance;
- unauthorized parameter/bound/solver/grid/tolerance change.

Do not tune after a stop.

## 11. Mandatory diagnostics

For both paths report by turn/province:

- annual raw `ra0` and components `rk`, after-tax profit/K, `delta=.10`;
- converted raw portfolio `rah`;
- HJB-consumed `r_a`;
- G1 lower/upper guard hit counts and shares;
- existing wage-guard hit counts;
- entering/next `rah` provenance;
- `S` identity and share-column sums;
- Kprivate, origin/national conservation;
- GovInv and total K/target;
- HJB convergence count/statistic/iterations;
- consumption, transfer `d`, adjustment cost, effective illiquid return, `mu_a`, `mu_b`, drift extrema if persisted by accepted route;
- boundary outward counts/policy labels already available;
- NaN/Inf counts;
- Y, wage, outer residual diagnostics;
- KFE classification/caveat.

## 12. Questions to answer

1. Does annual `delta=.10` materially lower firm raw `ra0` relative to the previously accepted `.025` diagnostic evidence, descriptively?
2. Does U remain executable over treatment turns 2-5 under the annual contract?
3. Does G1 materially improve HJB convergence/statistics or reduce transfer/cost/drift extremes relative to U?
4. What fraction of G1 province-turn HJB payoff inputs hit lower/upper guards? If nearly all hit the upper guard, say so explicitly.
5. Are geography ranking and same-S accounting preserved before the HJB guard?
6. Does the existing wage guard saturate materially?
7. Are any improvements clearly due to the guard rather than to annual depreciation recalibration? Keep attribution limited to the U/G1 difference.
8. Does either path provide a plausible basis for a later provisional steady-state attempt, without claiming one now?

No post-hoc threshold invention.

## 13. Interpretation

A successful G1 path may support only a classification such as:

`ANNUAL_RECALIBRATED_K1A_G1_DIAGNOSTIC_GUARD_SHORT_HORIZON_ROUTE_SUPPORTED`.

It does not establish final payoff calibration, guard-free stability, 25-turn convergence, steady state, KFE, K1B/K2 or Results.

If G1 survives but saturates heavily, recommend either staying at G1 for a longer bounded/provisional route or revisiting calibration; do not automatically advance to G2.

If U is stable and G1 unnecessary, report that truthfully; do not keep guards merely because they were preregistered.

## 14. Allowed changes

Allowed only as task-bounded plumbing/diagnostics:

- annual calibration override/plumbing for `delta=.10` and dimensional metadata;
- HJB-interface G1 return guard selector;
- guard/provenance receipts;
- bounded runner/finalizer;
- focused tests;
- report `docs/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_annual_hjb_g1_guard_diagnostic/`;
- truthful CURRENT closeout docs.

Do not modify production-science equations, capital-network formula, HJB/KFE equations, boundary/KKT law, C1, labor science, grid, tolerance, solver semantics, K1B/K2 or Results.

## 15. Publication

Use a fresh isolated worktree from live main. Explicit stage paths; no `git add .` or `git add -A`. No reset/clean/stash/force push. One coherent commit, non-force push, one remote commit/report readback. Do not merge main and do not publish a successor task.

## 16. Final response

Return:

- classification/verdict;
- actual baseline, branch/worktree/candidate SHA;
- changed paths;
- pre-run gate;
- exact annual calibration actually used;
- U/G1 call ledgers and completed turns;
- turn-1 equivalence;
- raw/converted/guarded return distributions;
- return-guard saturation counts;
- wage-guard saturation counts;
- HJB convergence/statistics comparison;
- transfer/cost/drift/control comparison;
- K1/C1 accounting and provenance;
- NaN/Inf/hard-stop status;
- KFE caveat;
- whether a provisional steady-state route is supported;
- exactly one recommended next gate;
- Results eligibility=`FALSE`.

Stop. Do not enter K1B/K2.
