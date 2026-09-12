# CH5 MP4C K1 annual HJB G1 vs G2 price-guard continuation diagnostic report

## Verdict

Classification: `ANNUAL_K1A_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_COMPLETED__DO_NOT_EXTEND_G2__FOCUSED_HA_HJB_MECHANISM_DIAGNOSTIC_RECOMMENDED`.

G2 materially reduced return saturation and restored some cross-province HJB input variation, but it did not produce a stable improvement: treatment-turn HJB convergence fell from 18/124 under G1 to 6/124 under G2, while several transfer, adjustment-cost and drift extrema increased sharply. G2 is therefore not supported as an automatic provisional longer-horizon scaffold. This is a bounded diagnostic only; `Results eligibility=FALSE`.

## Authority and frozen setup

- Actual baseline: `b5ba365d0e21329d81828c466fcc7010a429aa09`.
- Worktree: `D:\ProjectTemp\ch5-k1-annual-hjb-g1-vs-g2-20260912-001`.
- Branch: `codex/ch5-k1-annual-hjb-g1-vs-g2-20260912`.
- External evidence: `D:\ProjectTemp\ch5-k1-annual-hjb-g1-vs-g2-evidence-20260912-001`.
- External manifest SHA-256: `FC176A6B2809A012D36BE79428630C9E371C9262ABCA4AF1CFAA57295B9676CB`; 1041-file readback PASS.
- Pre-run gate: PASS with science calls before gate = 0. The two payloads were byte-identical; turn 1 used the same bootstrap; annual continuous-time values were `rho=.05`, `rb=.02`, borrowing gap `.07`, firm/HJB `delta=.10`, `Q_z` off diagonal `1/3`, `chi0=.1`, `chi1=2`. No `/4`, `*4`, log or compounding conversion was used.
- Both paths used `beta_distance=2`, `beta_return=0`, fixed theta, accepted destination-by-origin `S`, same `S` for quantities and payoffs, source-faithful labor, no normalized labor, smoothing or partial adjustment, and C1 `GovInv=max(Ktarget-Kprivate,0)`. K1B/K2 were off. Wage guard remained exactly `[.8,1.3]`.

Only the HJB-interface return guard differed from turn 2 onward: G1 `[-.05,.20]`; G2 `[-.10,.35]`. Each path used its own prior-completed annual raw `ra0 @ S`; raw/converted receipts were not clipped or overwritten.

## Execution ledger

Both paths completed 5/5 turns and 155/155 province updates. G1 used 155 HJB calls, 13,362 HJB direct solves, 155 KFE calls and 155 KFE direct solves. G2 used 155 HJB calls, 13,834 HJB direct solves, 155 KFE calls and 155 KFE direct solves. Total: 2 trajectory invocations, 310 HJB calls, 27,196 HJB direct solves, 310 KFE calls, 310 KFE direct solves, 248,000 labor roots/Brent calls and 310 completed province updates. Scientific retry = 0; engineering retry = 0. MATLAB, standalone KFE experiment, K1B, K2, GE, annual downstream, shock/IRF and Results calls were all 0.

The zero-science finalizer initially rejected turn-1 return flags because turn 1 correctly had `NOT_APPLIED_BOOTSTRAP`, not a treatment hit category. The external scientific evidence was not changed and no trajectory was rerun. The finalizer was corrected to represent bootstrap-not-applied explicitly. Later zero-science adjudications corrected an overly permissive preliminary route field and clarified the wage-hit label. Because existing evidence was not overwritten, `summary_authority.json` is the authoritative compact index and points to `route_adjudication.json` and `wage_criterion_adjudication.json` for the two superseded fields.

## Turn-1 equivalence and return distributions

Turn-1 scalar observables and saved HJB arrays were exactly equal: all reported max absolute differences and all array changed counts were zero.

Across treatment turns 2–5:

| Metric | G1 | G2 |
|---|---:|---:|
| raw annual firm `ra0`, min / median-of-turn-medians / max | 0.187994 / 0.440280 / 1.074223 | 0.013660 / 0.434700 / 1.062023 |
| converted raw `rah`, min / median-of-turn-medians / max | 0.207674 / 0.438475 / 0.984468 | 0.207674 / 0.436344 / 0.974326 |
| HJB-consumed `r_a`, min / median-of-turn-medians / max | 0.200000 / 0.200000 / 0.200000 | 0.207674 / 0.350000 / 0.350000 |
| converted distinct counts by turn | 31, 31, 31, 31 | 31, 31, 31, 31 |
| consumed distinct counts by turn | 1, 1, 1, 1 | 14, 10, 10, 10 |
| upper hits | 124/124 (100%) | 84/124 (67.742%) |
| lower hits | 0/124 | 0/124 |
| unsaturated | 0/124 | 40/124 (32.258%) |

G1 upper-hit provinces were all 31 provinces in every treatment turn. G2 turn 2 had 18 upper-hit provinces and 13 unsaturated provinces; turns 3–5 each had 22 upper-hit and 9 unsaturated provinces. G2 repeatedly upper-hit: 上海、云南、北京、四川、天津、宁夏、安徽、山西、广东、新疆、江苏、江西、浙江、海南、湖北、湖南、甘肃、福建、西藏、贵州、重庆、陕西. No return lower hit occurred. Exact per-turn province lists are preserved in `summary.json`.

## Wage-boundary monitoring

The criterion was frozen before execution exactly as task section 7 states: lower hit iff guarded `wjt == .8`, upper hit iff guarded `wjt == 1.3`. Existing external rows separately preserve the firm's strict clip-activation flags `wage_clipped_lower/upper`; a zero-science label adjudication makes this distinction explicit without changing counts. G1 treatment totals were: lower 16/124, upper 96/124, unsaturated 12/124. G2 totals were: lower 25/124, upper 84/124, unsaturated 15/124. Thus wage saturation remained very high: 112/124 (90.323%) for G1 and 109/124 (87.903%) for G2.

For G1, 海南、西藏、青海、宁夏 hit the lower boundary in all four treatment turns; 24 provinces hit the upper boundary in all four turns; 吉林、黑龙江、甘肃 were unsaturated. For G2, 海南、西藏、青海、宁夏 repeatedly hit the lower boundary. The repeated upper-hit provinces were 上海、云南、内蒙古、北京、四川、天津、安徽、山东、山西、广东、广西、新疆、江苏、江西、河北、河南、浙江、湖北、湖南、福建、贵州、辽宁、重庆、陕西. Turn 5 shifted to 13 lower, 12 upper and 6 unsaturated provinces. Exact per-turn lower/upper/unsaturated lists are preserved in `summary.json`.

## HJB, controls and drifts

Treatment HJB converged counts by turn were G1 `2,3,7,6` and G2 `2,1,3,0`, totaling 18/124 versus 6/124. Maximum HJB statistics by turn were G1 `108.2633, 41.7196, 12.4504, 70.4255` and G2 `50.9359, 170.4551, 203.2134, 31.8314`. This is mixed by statistic but clearly worse by convergence count.

G2 also produced material control/drift instability. At turn 2, adjustment-cost and illiquid-drift absolute maxima rose from about `6.52e12` to `1.92e14`; liquid-drift/transfer maxima rose from about `6.68e6` to `4.27e7`. At turn 4, adjustment-cost/illiquid-drift maxima rose from about `2.98e13` to `6.08e13`, and liquid-drift/transfer maxima from about `1.19e7` to `2.26e7`. Some turns improved individual extrema, so the finding is not uniform; the full turn-by-turn table is `treatment_turn_comparison.csv`.

## K1/C1, provenance, finiteness and KFE caveat

All 310 province-turn rows preserved same-S quantity/payoff identity, own prior-completed return provenance, no same-turn return feedback and source-faithful labor. Across treatment turns, capital column residual absolute maxima were at most `3.725290298461914e-09` MU; national capital residual maxima were G1 `1.4901161193847656e-08` MU and G2 `2.9802322387695312e-08` MU; C1 accounting maxima were G1 `7.450580596923828e-09` MU and G2 `2.9802322387695312e-08` MU. Total K/target remained within `[0.9999999999999998,1.0000000000000002]`.

Saved HJB NaN/Inf count was zero and neither path raised a scientific exception. Every KFE result remained `DIAGNOSTIC_ONLY`; finite/direct-solve completion is not KFE admissibility or steady-state acceptance.

## Decision

1. G2 significantly reduced return saturation and restored partial cross-province HJB `r_a` variation.
2. G2 did not improve HJB convergence overall and materially enlarged several control/drift extrema.
3. Wage guard remained highly binding after changing only the return guard.
4. K1, C1, same-S, provenance and capital accounting continued to close within the accepted numerical scale.
5. Neither path reached `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`: G1 had 124 return hits and 112 wage hits; G2 had 84 return hits and 109 wage hits across 124 treatment province-turns.
6. Do not automatically run longer G2 or enter G3/G4. The only next gate is fresh independent ChatGPT Reviewer ACCEPT/REJECT of the candidate, including whether the next exact task should be a focused HA/HJB mechanism diagnostic. No successor task is published here.

`Results eligibility=FALSE`.
