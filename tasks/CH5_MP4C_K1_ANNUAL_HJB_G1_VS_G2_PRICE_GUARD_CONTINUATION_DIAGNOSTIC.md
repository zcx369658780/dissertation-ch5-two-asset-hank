# CH5 MP4C K1 — annual HJB G1 vs G2 price-guard continuation diagnostic

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: bounded scientific runtime diagnostic.
Issuer: ChatGPT Reviewer under Owner-approved annual recalibration and price-guard continuation policy.

## 1. Goal

Compare the already accepted annual G1 return safeguard with the next preregistered G2 safeguard while holding the legacy wage safeguard fixed.

This task isolates only the return-guard widening:

- G1: `r_a in [-.05,.20]`;
- G2: `r_a in [-.10,.35]`.

The purpose is to identify whether widening the return continuation region restores meaningful cross-province payoff variation without causing unacceptable deterioration in the nonlinear HA/HJB block.

This is not a steady-state acceptance task and does not authorize G3, G4, K1B or K2.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`, record actual SHA, and verify this task remains active. Read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`;
- `docs/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC_REPORT.md`;
- accepted K1 capital-network/scoring/payoff freezes;
- active firm/HJB/household/K1A runner source required for bounded execution.

Do not restart prior data, parity, time-base, distance or provenance audits.

## 3. Frozen annual contract

Both paths must use exactly:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`;
- `rb=.02/year`;
- borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`;
- productivity-generator off-diagonal intensity `1/3/year`;
- corrected annual `Y/K` and after-tax profit/K unchanged, no `/4` or other rescaling;
- `ra0_annual=rk_annual+after_tax_profit_over_K_annual-.10`;
- `rah_annual_raw=S' * ra0_annual` using the accepted destination-by-origin `S`;
- `chi0=.1`, `chi1=2 years` as provisional annual calibration;
- annual wage/consumption/transfer/adjustment-cost flow interpretation in the unchanged household-model asset numeraire.

Do not use `.025`, `.0025` or PIM `.096` as the firm/HJB depreciation rate.

## 4. K1A contract

Both paths use:

- `beta_distance=2.0`;
- `beta_return=0`;
- fixed `theta_i=inter_prv_ratio_i`;
- accepted destination-by-origin `S`;
- source-faithful labor;
- normalized labor OFF;
- smoothing OFF;
- partial adjustment OFF;
- C1 `GovInv=max(Ktarget-Kprivate,0)` unchanged;
- same `S` for capital quantity and household payoff.

K1B and K2 are OFF.

## 5. Two-path symmetric design

Run exactly two paths from byte-identical accepted initialization.

### Path G1

- turn 1: common accepted entering-payoff bootstrap;
- firm uses annual `delta=.10` from turn 1;
- turns 2-5 compute same-path prior-completed `rah_annual_raw=S'ra0_annual`;
- HJB interface guard: `clip(rah_annual_raw,-.05,.20)`.

### Path G2

- turn 1: same common accepted entering-payoff bootstrap;
- firm uses annual `delta=.10` from turn 1;
- turns 2-5 compute same-path prior-completed `rah_annual_raw=S'ra0_annual`;
- HJB interface guard: `clip(rah_annual_raw,-.10,.35)`.

No other scientific input may differ between G1 and G2.

The legacy wage safeguard remains fixed in both paths:

`wjt in [.8,1.3]`.

It is diagnostic scaffolding only and must not be widened or removed in this task.

## 6. Turn-1 equivalence

Turn 1 is a common bootstrap and must be scientifically identical across G1/G2 apart from path label / future guard metadata.

No return guard treatment is attributed to turn 1.

Completed turn-1 firm state produces annual `ra0`; only from turn 2 may the path-specific G1/G2 guard be applied to the same-path prior-completed annual portfolio payoff.

No cross-path borrowing and no same-turn return feedback.

## 7. Mandatory three-layer return receipts

For every province/turn persist separately:

1. raw annual firm `ra0_annual`;
2. converted annual portfolio payoff `rah_annual_raw=S'ra0_annual`;
3. HJB-consumed `r_a` after the path-specific guard.

Also persist:

- lower-hit flag;
- upper-hit flag;
- unsaturated flag;
- province names in each category;
- counts and shares by turn and path;
- number of distinct converted `rah` values before guarding;
- number of distinct HJB-consumed `r_a` values after guarding.

Do not overwrite raw or converted objects with guarded objects.

## 8. Mandatory MATLAB-style wage-bound monitoring

For every province and completed turn persist the wage safeguard diagnostics, explicitly mirroring the legacy MATLAB intent:

- raw/pre-guard wage if available from the accepted route;
- guarded `wjt` actually used;
- lower-hit indicator for `.8`;
- upper-hit indicator for `1.3`;
- province names in lower-hit and upper-hit sets;
- counts and shares by turn and full path;
- unsaturated province names/counts.

Use the active implementation's true clipping criterion. If an equality test is used, preserve that exact criterion; if a tolerance is required, state it in the report and keep it fixed before science.

Do not modify `[.8,1.3]`.

## 9. Ideal steady-state benchmark

The task must explicitly report distance from the long-run target:

`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`.

That target means a later accepted steady state should have no binding diagnostic return guard and no binding diagnostic wage guard, unless a separate structural-economic authority later justifies a bound.

This task does not require zero hits; it measures progress toward that target.

## 10. Pre-run gates

Before scientific execution prove:

1. live baseline/task authority is correct;
2. annual recalibration values exactly match the freeze;
3. G1/G2 starting payloads are byte-identical except path/guard metadata;
4. turn-1 bootstrap is identical;
5. firm/HJB depreciation is exactly `.10` in both paths;
6. raw annual `ra0` is not legacy-clipped before portfolio aggregation;
7. G1 turn2 wiring = own turn1 `ra0@S`, then `[-.05,.20]` interface guard;
8. G2 turn2 wiring = own turn1 `ra0@S`, then `[-.10,.35]` interface guard;
9. same-S quantity/payoff identity is preserved;
10. wage safeguard `[.8,1.3]` is unchanged in both paths;
11. MATLAB-style wage hit monitoring is wired before science;
12. K1B/K2/smoothing/normalized labor are OFF;
13. C1 unchanged;
14. solver/grid/tolerance unchanged.

Any failure blocks science.

## 11. Runtime budget

Maximum:

- trajectory invocations: 2 total;
- G1: at most 5 completed turns;
- G2: at most 5 completed turns;
- HJB calls: at most 310 total;
- KFE calls: at most 310 total;
- MATLAB: 0;
- standalone KFE: 0;
- K1B/K2/GE/annual downstream/shock/IRF/Results: 0.

No scientific retry after state advancement. One pre-state-update engineering retry is allowed only for path/serialization/output-shape defects with byte-identical scientific inputs.

## 12. Stop conditions

Stop the affected path and preserve evidence on:

- NaN/Inf in HJB values, controls or key aggregates;
- scientific exception;
- same-turn return feedback;
- wrong prior-return provenance;
- same-S failure;
- capital-conservation failure beyond accepted tolerance;
- C1 accounting failure beyond accepted tolerance;
- unauthorized parameter, guard, solver, grid or tolerance change.

Do not tune after a stop.

## 13. Mandatory diagnostics

For both paths report by turn/province:

- annual raw `ra0` and components `rk`, after-tax profit/K, `delta=.10`;
- converted raw portfolio `rah`;
- HJB-consumed guarded `r_a`;
- return-guard lower/upper/unsaturated hit counts and province lists;
- raw/pre-guard wage where available;
- guarded `wjt`;
- wage lower/upper/unsaturated hit counts and province lists;
- entering/next payoff provenance;
- `S` identity/share-column sums;
- Kprivate and origin/national capital conservation;
- GovInv and total K/target;
- HJB convergence count/statistic/iterations;
- consumption, transfer `d`, adjustment cost, effective illiquid return, `mu_a`, `mu_b`, liquid/illiquid drift extrema if persisted;
- available boundary outward counts / policy labels;
- NaN/Inf counts;
- Y, wage and outer residual diagnostics;
- KFE classification/caveat.

## 14. Questions to answer

1. Does G2 reduce return-guard saturation materially relative to G1?
2. Does G2 restore nontrivial cross-province variation in HJB-consumed `r_a`?
3. Does HJB convergence improve, deteriorate or remain similar under G2?
4. Does G2 cause a material increase in HJB statistic, transfer, adjustment cost or drift extremes?
5. Which provinces repeatedly hit the G1/G2 return upper/lower bounds?
6. Which provinces repeatedly hit `wjt=.8` or `wjt=1.3` under each path?
7. Is the wage safeguard still heavily binding when only the return guard changes?
8. Are same-S, capital conservation, C1 and source-faithful labor preserved?
9. Does G2 look suitable for a later provisional longer-horizon route, or should the next gate instead inspect HA/HJB mechanisms?
10. How far is each path from the ideal `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS` target?

No post-hoc threshold invention.

## 15. Decision logic

A G2 path is not accepted merely because it executes.

Reviewer-relevant evidence should distinguish:

- **G2 still near-fully saturated:** continuation region remains too tight; likely next stage is G3 only after review, not a longer G2 steady-state attempt;
- **G2 materially unsaturated with tolerable HJB behavior:** G2 may become a candidate provisional steady-state scaffold;
- **G2 widening sharply worsens HJB/control stability:** stop continuation widening and recommend a focused HA/HJB mechanism diagnostic before G3;
- **wage safeguard remains heavily saturated:** record this explicitly; do not alter wage bounds inside this task.

## 16. Interpretation boundary

The strongest permitted classification, if supported, is something like:

`ANNUAL_K1A_G2_RETURN_CONTINUATION_SHORT_HORIZON_SUPPORTED__WAGE_GUARD_FIXED`.

This does not establish:

- 25-turn convergence;
- steady state;
- zero-bound dependence;
- final payoff calibration;
- KFE validity;
- K1B/K2;
- Results.

## 17. Allowed changes

Allowed only as task-bounded plumbing/diagnostics:

- G1/G2 HJB-interface guard selector;
- MATLAB-style return/wage boundary-hit receipts;
- bounded runner/finalizer;
- focused tests;
- report `docs/CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_annual_hjb_g1_vs_g2_price_guard/`;
- truthful CURRENT closeout docs.

Do not modify production economic equations, capital-network formula, HJB/KFE equations, boundary/KKT law, C1, labor science, annual calibration, wage guard, grid, tolerance, solver semantics, K1B/K2 or Results.

## 18. Publication safety

Use a fresh isolated worktree from live main. Explicit stage paths; no `git add .` or `git add -A`. No reset/clean/stash/force push. One coherent commit, non-force push, one remote commit/report readback. Do not merge main and do not publish a successor task.

## 19. Final response

Return:

- classification/verdict;
- actual baseline, branch/worktree/candidate SHA;
- changed paths;
- pre-run gate;
- exact annual calibration and G1/G2 guards;
- G1/G2 call ledgers and completed turns;
- turn-1 equivalence;
- raw/converted/guarded return distributions;
- return-guard saturation counts and province lists;
- wage-guard saturation counts and province lists;
- HJB convergence/statistics comparison;
- transfer/cost/drift/control comparison;
- K1/C1 accounting and provenance;
- NaN/Inf/hard-stop status;
- KFE caveat;
- distance from `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`;
- whether G2 is suitable for a later provisional steady-state route;
- exactly one recommended next gate;
- Results eligibility=`FALSE`.

Stop. Do not enter G3/G4, K1B or K2.
