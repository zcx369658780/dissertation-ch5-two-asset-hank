# CH5 MP4C K1 — HJB value-update relaxation omega=0.5 same-input diagnostic report

Date: 2026-09-13.

Task: `CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC`.

## Classification

`PARTIAL_SUPPORT__SYSTEMATIC_CHATTERING_REDUCTION__NET_ONE_CONVERGENCE_GAIN__TURN2_NONE_AND_ENDPOINT_DIVERGENCE_OUTLIERS`

Fixed `omega=0.5` systematically reduced policy switching, two-step reversions and raw-gap non-monotonicity, and restored eight previously failed turn-1 calls. It did not produce a robust convergence improvement: five previously converged turn-1 calls and both previously converged turn-2 calls ceased to converge, every turn-2 treatment call hit the 100-iteration ceiling, and only five of fifteen both-converged calls had near-identical values and identical labels. The evidence partially supports policy chattering/value oscillation as a fixed-point blocker, but does not justify a production HJB solution-method contract.

Results eligibility=`FALSE`.

## Authority, checkout and exact inputs

- actual fresh-fetched baseline: `f905a7236084b2f23d54894fa336e074874d0c26`;
- branch: `codex/ch5-mp4c-k1-hjb-omega05-same-input-20260913`;
- isolated worktree: `D:\ProjectTemp\ch5-mp4c-k1-hjb-omega05-20260913-001`;
- accepted source evidence: `D:\ProjectTemp\ch5-mp4c-k1-transfer-d1-1e5-evidence-20260913-001`;
- accepted mechanism evidence: `D:\ProjectTemp\ch5-mp4c-k1-hjb-mechanism-t1-t2-evidence-20260913-002`;
- treatment evidence: `D:\ProjectTemp\ch5-mp4c-k1-hjb-omega05-evidence-20260913-002`.

The treatment external sealed-manifest file SHA-256 is `C1FDF69841B410BD3370F5066F2E7980E3F757C5A4A51ABDF1223F4486E1D09B`. The compact-evidence sealed-manifest file SHA-256 is `E50E84F81ABB33E44A00A4B7D797C35D5D0B1F7E5F81D998FB0AFEAC6697FFA9`.

The accepted D1-control sealed-manifest file SHA-256 is `C60C353FE1ABC24509F5753E808F837BA19C9856B98FAE9998AB59DAC9BCE6BE`; the accepted mechanism sealed-manifest file SHA-256 is `82A979E15DF22A651348F8C4E35FFE5688513E635877269DA98DF0755D03AF77`. All entries in both roots were reverified. Exact-input coverage is `62/62`; no approximate, interpolated, replacement or synthetic input was used. D1/K1B/K2 remained OFF.

One permitted pre-HJB engineering retry was consumed. The first preflight compared two already adjudicated legacy wage-guard metadata fields and therefore marked all inputs unproven; no HJB had begun. The retained second fresh root recomputed guarded `wjt` from sealed entering states, established `62/62`, and recorded the metadata adjudication. Scientific inputs were unchanged.

## Omega=1 equivalence gate and ledger

The two parity inputs were preregistered before science: turn-1 Beijing (accepted converged) and turn-1 Anhui (accepted ceiling failure). Each was executed exactly once through the generalized wrapper with `omega=1`.

- Beijing: all scientific arrays, final value, controls, labels, iteration operator, post-convergence operator, iteration count (`17`), convergence flag, raw statistic (`8.547302199346518e-09`) and deterministic receipts exact-equal;
- Anhui: the same objects exact-equal, including `100` iterations, `converged=false`, and raw statistic `0.18862667495966345`;
- gate: `PASS`; treatment began only after both calls passed.

The complete ledger records `64` HJB calls: `2` omega=1 parity plus `62` omega=0.5 treatment calls. Direct solves were `4,823`: `117` parity plus `4,706` treatment. Scientific retries=`0`. KFE, outer trajectory/turn advancement, MATLAB, firm runtime, household steady-state, K1B, K2, GE, annual downstream, shock, IRF and Results calls were all `0`.

## Baseline versus omega=0.5 convergence

| Group | Accepted omega=1 | omega=0.5 | Delta |
|---|---:|---:|---:|
| turn1 | 20/31 | 23/31 | +3 |
| turn2 | 2/31 | 0/31 | -2 |
| all 62 | 22/62 | 23/62 | +1 |

Eight baseline-failed turn-1 calls converged under treatment (安徽、江西、河南、湖北、湖南、广东、重庆、四川), while seven baseline-converged calls failed under treatment (turn1 内蒙古、辽宁、吉林、海南、云南; turn2 重庆、贵州).

All 23 treatment-converged calls used the unchanged raw criterion and satisfied `||V_solve-V_old||_inf < 1e-7`. The eight recovered raw gaps range from `5.103359912439487e-08` to `9.72344453842311e-08` and converged in 33–36 iterations. No turn-2 call converged; failed final raw gaps ranged from `4.067066416268972e-05` to `71.47891779275778`.

## Trajectories, raw gap and derivative floor

Across the 62 exact pairs, mean policy switching decreased in `57/62` calls, mean two-step reversion decreased in `59/62`, and raw-gap non-decrease fraction decreased in `58/62`.

Median policy-switch means changed from `168.83` to `83.06` for baseline turn1-converged calls, `205.85` to `82.67` for baseline turn1-failed calls, `138.89` to `115.58` for baseline turn2-converged calls, and `229.88` to `122.67` for baseline turn2-failed calls. Corresponding median reversion means changed from `30.03` to `8.13`, `39.33` to `6.34`, `21.36` to `16.65`, and `41.30` to `16.76`. For the 20 accepted turn1-converged-to-turn2-failed provinces, treatment reduced both means in `18/20`, but restored none at turn2.

Every iteration separately records raw fixed-point gap and relaxed state update. For `omega=0.5`, the maximum absolute deviation from `raw_gap = 2 * relaxed_update` was `9.094947017729282e-13`; the convergence branch reads only the raw gap. This excludes mechanical false convergence from the halved stored update.

Policy switching preceded derivative-floor activation in 40 treatment calls; 22 treatment calls never hit the floor. All eight newly converged calls had no derivative-floor hits. Their convergence improvement therefore occurred without changing or activating the derivative floor and supports an upstream value-state/policy-stability effect. It does not show that floor behavior is irrelevant to the remaining failures.

## Output normality and endpoint comparison

Independent offline revalidation found all `62/62` treatment outputs and all retained per-iteration scientific arrays finite, with correct shapes and accepted liquid/transfer label domain `{"0","B","F"}`; scientific exceptions=`0`, unauthorized clipping=`0`, and manufactured candidates=`0`.

The runtime summary initially reported only `14/62` normal calls because its output-only allowlist omitted accepted liquid label `"0"`. `output_normality_adjudication.json` preserves that receipt and proves the metadata-only correction to `62/62`; no HJB was rerun. The task-owned HJB wrapper was unchanged, and `execution_source_adjudication.json` binds the executed and candidate source hashes.

Fifteen calls converged under both maps. Across their 12,000 cells:

| Object | max abs | median abs |
|---|---:|---:|
| value | 0.14776673094318982 | 7.945588631486089e-11 |
| consumption | 991.0433012381624 | 9.745036244623861e-08 |
| labor | 0.5969042397534937 | 3.3467204563208952e-09 |
| transfer | 26.311205280482174 | 4.326490009309847e-08 |
| adjustment cost | 1306.2778609419938 | 1.289332111215069e-08 |
| mu_a | 26.311205280482174 | 4.326490007922068e-08 |
| mu_b | 2279.267742224832 | 2.526369318189836e-07 |

Liquid labels differed in `624/12000` cells (`5.2%`) and transfer labels in `647/12000` (`5.3917%`). Only `5/15` calls had value max-absolute difference below `1e-6` and identical labels. Medians are close, but large localized endpoint/control differences rule out a general same-fixed-point conclusion and prevent calling the treatment production-ready.

## Interpretation and sole next gate

The same-input intervention identifies the effect of fixed `omega=0.5` on these isolated accepted HJB maps: it strongly reduces chattering/reversion/non-monotonicity and restores a subset of turn-1 fixed points. The turn-2 regression, seven lost convergences and endpoint outliers show that chattering/value oscillation is a major blocker for some calls, not a sufficient universal explanation or a validated production cure. The evidence redirects away from immediate production adoption and toward unresolved turn-2 and endpoint-coherence review; it does not authorize omega tuning, a ladder, adaptive damping, derivative/price/guard changes or a longer ceiling.

Exactly one recommended next Owner gate is `OWNER_HJB_RELAXATION_MIXED_EVIDENCE_AND_TURN2_FIXED_POINT_COHERENCE_REVIEW`.

KFE was not run; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers. Standalone KKT residual remains unavailable in accepted evidence. No steady-state, GE, KFE-admissibility, production-solver or Results claim is made.
