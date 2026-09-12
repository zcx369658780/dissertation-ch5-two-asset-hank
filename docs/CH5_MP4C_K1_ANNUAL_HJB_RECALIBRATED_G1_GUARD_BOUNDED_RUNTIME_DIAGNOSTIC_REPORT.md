# CH5 MP4C K1 annual HJB recalibrated G1-guard bounded runtime diagnostic

Date: 2026-09-12
Task: `CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC`

## Classification

`ANNUAL_RECALIBRATED_K1A_G1_DIAGNOSTIC_GUARD_SHORT_HORIZON_ROUTE_SUPPORTED`

Both annual paths completed the authorized five outer turns without NaN/Inf, scientific exception, return-provenance failure, same-turn feedback, same-S failure, capital-conservation failure, or C1 accounting failure. Path U is executable over turns 2-5, but its HJB results remain strongly nonconverged and numerically stressed. G1 improves aggregate HJB convergence counts and sharply reduces the worst HJB statistic in turns 3-5, but it is not a uniformly stabilizing treatment: transfer, adjustment-cost and drift extrema are larger than U in turns 2-4 and smaller only in turn 5.

Most importantly, all `124/124` G1 treatment province-turn HJB return inputs hit the upper `.20` guard. G1 therefore removes all cross-province return-level variation at the HJB interface during turns 2-5. The route is supported only as short-horizon, guard-dependent diagnostic scaffolding and as a possible basis for a future **provisional** steady-state design. This is not evidence of a steady state, guard-free stability, final payoff calibration, KFE validity, K1B/K2 validity, or Results eligibility.

## Authority and identity

- fresh live-main baseline: `69f3800f78e1f792bcd09f2ad683fc5bf25952fc`;
- worktree: `D:\ProjectTemp\ch5-k1-annual-hjb-g1-guard-20260912-001`;
- branch: `codex/ch5-k1-annual-hjb-g1-guard-20260912`;
- accepted runtime payload SHA-256: `EBB9FD91F3D3CE5D46476FE7BF1D0662E26EEA5C87357E4B13907CC76EBE9355`;
- external evidence root: `D:\ProjectTemp\ch5-k1-annual-hjb-g1-guard-evidence-20260912-001`;
- external manifest: `1041/1041 PASS`, SHA-256 `FAA6246CCFA8828E6F936A0CCACA340697BB79197E29A211048D26E96F43ACE0`;
- Results eligibility: `FALSE`.

## Pre-run gate and implementation boundary

The zero-science gate passed before either trajectory. The two runtime payload files are byte-identical and have the same accepted SHA. Turn 1 uses the common accepted entering payoff bootstrap; U/G1 differ only by path/guard metadata, and no G1 return guard is applied in turn 1.

The executed annual contract was:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`, `rb=.02/year`, borrowing gap `.07/year`;
- firm/HJB `delta=.10/year` from turn 1;
- productivity-generator off-diagonal intensity `1/3/year`;
- corrected annual `Y/K` and after-tax profit/K retained without `/4`, `*4`, compounding or log conversion;
- `ra0_annual=rk_annual+after_tax_profit_over_K_annual-.10`;
- `rah_annual_raw=ra0_annual @ S_destination_origin`;
- `chi0=.1`, `chi1=2 years`;
- unchanged annual household-model-unit interpretation and asset numeraire.

Both paths use `beta_distance=2`, `beta_return=0`, fixed theta, source-faithful labor, no normalized labor, no smoothing/partial adjustment, and C1 `GovInv=max(Ktarget-Kprivate,0)`. K1B and K2 are off. The accepted grid, tolerance, solver, HJB/KFE equations, boundary/KKT law, capital-network formula and C1 formula were not changed. The implementation is confined to a task runner/finalizer, receipts, focused tests and this report; the production firm continues to expose its historical clipped `ra` for diagnostics, but portfolio aggregation in this task uses unclipped annual `ra0` from turn 2 onward.

The existing firm wage guard `[.8,1.3]` is unchanged and classified only as `TEMPORARY_NUMERICAL_DIAGNOSTIC_SCAFFOLDING`.

Focused zero-science tests: `39/39 PASS`.

Post-run independent diff review found two receipt-only issues in the reused K1A augmentation. First, inherited `firm_ra0_reconstruction_residual` used the old `.025` diagnostic identity and therefore equals approximately `.075` in all 310 immutable external rows. Second, the first task-specific `raw_ra0_formula_abs_residual` was tautological because its profit component was algebraically recovered from `ra0`; it is not used as formula proof. Neither field entered any model calculation, guard, controller, accounting check, summary statistic, or scientific conclusion. Independent zero-science recomputation instead uses the separately persisted firm `profit/K * (1-.25)` component: its maximum difference from the persisted after-tax component is zero, and the annual `.10` formula residual is at most `5.551115123125783e-17`. The external evidence was preserved without overwrite; compact evidence explicitly adjudicates both fields, and the final runner keeps the independently persisted profit component and overwrites the legacy residual with the annual `.10` definition. No scientific retry was performed. Post-correction zero-science focused tests: `40/40 PASS`.

## Call ledger and turn-1 equivalence

| Item | U | G1 | Total |
|---|---:|---:|---:|
| trajectory invocations | 1 | 1 | 2 |
| completed turns | 5 | 5 | 10 |
| province updates | 155 | 155 | 310 |
| HJB calls | 155 | 155 | 310 |
| HJB direct solves | 13,660 | 13,362 | 27,022 |
| KFE calls/direct solves | 155/155 | 155/155 | 310/310 |
| labor-root/Brent calls | 124,000 | 124,000 | 248,000 |
| scientific retries | 0 | 0 | 0 |

MATLAB, standalone KFE experiment, K1B, K2, GE, annual downstream, shock/IRF and Results calls are all zero. No engineering retry was used.

Turn 1 was exactly equivalent. All compared province aggregates, raw/converted/consumed returns, firm outputs, HJB statistics and iterations had maximum absolute difference zero; every saved HJB value/control/drift/utility/policy-label array had zero changed cells. Both paths had `20/31` HJB returns converged in turn 1. No turn-1 difference is attributed to G1.

## Annual returns and depreciation comparison

Turn-1 annual `.10` raw `ra0` was exactly `.075` lower province-by-province than the accepted `.025` evidence, up to floating-point roundoff: difference min/median/max `-0.07500000000000001/-0.07499999999999996/-0.07499999999999996`. Later descriptive median differences were `-.072371`, `-.068456`, `-.070340`, and `-.075623` in turns 2-5. Those later differences also include endogenous path evolution and are not a clean depreciation-only causal estimate.

Treatment-turn pooled distributions were:

| Path/object, turns 2-5 | min | median | max |
|---|---:|---:|---:|
| U raw firm `ra0_annual` | 0.014297 | 0.347283 | 1.053200 |
| U converted `rah_annual_raw` | 0.207674 | 0.432957 | 0.966461 |
| U HJB-consumed `r_a` | 0.207674 | 0.432957 | 0.966461 |
| G1 raw firm `ra0_annual` | 0.187994 | 0.440280 | 1.074223 |
| G1 converted `rah_annual_raw` | 0.207674 | 0.434407 | 0.984468 |
| G1 HJB-consumed `r_a` | 0.200000 | 0.200000 | 0.200000 |

Each G1 treatment turn retained 31 distinct pre-guard converted `rah` values, so the raw/converted layer preserves cross-province geographic variation. Because every value exceeded `.20`, the HJB-consumed layer is constant and does not preserve that ranking. Raw firm `ra0`, converted `rah`, and HJB-consumed `r_a` remain separate receipts; no raw or converted object is overwritten.

G1 saturation over turns 2-5 is exactly:

- upper `.20`: `124/124` province-turns (`100%`);
- lower `-.05`: `0/124`;
- unsaturated: `0/124`;
- grid/cell counts: not applicable because `r_a` is one scalar input per province HJB, not a cell-varying guard.

## HJB and household comparison

| Turn | U converged | G1 converged | U max statistic | G1 max statistic |
|---:|---:|---:|---:|---:|
| 2 | 3/31 | 2/31 | 93.6085 | 108.2633 |
| 3 | 2/31 | 3/31 | 2190.0239 | 41.7196 |
| 4 | 3/31 | 7/31 | 320.7677 | 12.4504 |
| 5 | 3/31 | 6/31 | 296.3198 | 70.4255 |

Treatment-horizon convergence is U `11/124` versus G1 `18/124`. G1 therefore improves the count modestly and materially lowers the worst statistic after turn 2, but both paths remain far from full HJB convergence. Every finite nonconverged return remains `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`.

Median consumption for U/G1 in turns 2-5 was `9.5002/8.7368`, `9.5627/8.1423`, `9.8466/7.9734`, and `9.3283/8.1165`. Maximum absolute transfer `d`, adjustment cost, `mu_a`, and `mu_b` were all larger under G1 in turns 2-4; in turn 5 they were lower under G1:

| Turn | U/G1 max `|d|` | U/G1 max cost | U/G1 max `|mu_a|` | U/G1 max `|mu_b|` |
|---:|---:|---:|---:|---:|
| 2 | 2.53e6 / 6.68e6 | 8.69e11 / 6.52e12 | 2.53e6 / 6.68e6 | 8.69e11 / 6.52e12 |
| 3 | 4.66e6 / 9.65e6 | 2.29e12 / 1.18e13 | 4.66e6 / 9.65e6 | 2.29e12 / 1.18e13 |
| 4 | 8.71e6 / 1.19e7 | 1.03e13 / 2.98e13 | 8.71e6 / 1.19e7 | 1.03e13 / 2.98e13 |
| 5 | 1.59e7 / 6.34e6 | 3.02e13 / 4.25e12 | 1.59e7 / 6.34e6 | 3.02e13 / 4.25e12 |

Thus G1's HJB-statistic improvement cannot be described as a uniform reduction in control/drift stress. The task establishes feasibility of the exact guarded interface, not robust numerical stability.

## Wage guard, K1, C1 and provenance

The wage guard is highly saturated. Over treatment turns 2-5, U recorded `85` upper hits, `25` lower hits and `14` unsaturated province-turns; G1 recorded `96` upper hits, `16` lower hits and `12` unsaturated province-turns. G1 therefore had `112/124` (`90.3%`) treatment province-turn wage-guard saturation. The unguarded raw wage was available and is persisted separately from guarded `wjt`.

All `310/310` province-turn rows passed quantity/payoff same-S and source-faithful-labor markers. Same-turn feedback count is zero. From turn 2 each path uses only its own immediately prior completed annual `ra0`, with no cross-path borrowing.

Across both paths:

- maximum absolute origin capital-column residual: `5.587935447692871e-09 MU`;
- maximum absolute national private-capital conservation residual: `1.4901161193847656e-08 MU`;
- maximum absolute C1 accounting residual: `1.4901161193847656e-08 MU`;
- total firm K/target stayed in `[0.9999999999999998,1.0000000000000002]`;
- all saved HJB arrays had zero NaN/Inf entries.

Outer residuals are not converged: the maximum recorded `nk_gap` is `11.67973404214395` and maximum `yt_gap` is `2.715689591397689`. This reinforces the short-horizon diagnostic-only interpretation.

## KFE and route decision

All `310/310` KFE returns remain `DIAGNOSTIC_ONLY`. The finite-box upper-`b` leakage and MATLAB-style pinning blocker is unchanged. No KFE acceptance is claimed.

G1 supplies a plausible, executable basis for a later **provisional** steady-state route only in the narrow sense that the guarded five-turn path completed and improved some HJB metrics. It does not yet justify a longer run automatically: the return guard is 100% upper-saturated, the wage guard is heavily saturated, HJB convergence remains low, and control/drift improvements are mixed.

The only recommended next gate is a fresh independent ChatGPT L3 ACCEPT/REJECT of the exact candidate and external evidence, specifically deciding whether this fully saturated G1 should receive a fresh bounded longer-horizon provisional-route task or whether the Owner must revisit the annual payoff/numeraire calibration first. Do not enter G2, K1B, K2, or Results from this Builder task.

Results eligibility=`FALSE`.
