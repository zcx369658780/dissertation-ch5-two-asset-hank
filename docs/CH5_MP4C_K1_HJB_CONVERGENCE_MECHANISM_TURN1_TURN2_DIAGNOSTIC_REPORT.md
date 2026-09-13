# CH5 MP4C K1 — HJB convergence-mechanism turn1/turn2 diagnostic report

Date: 2026-09-13

Task: `CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC`

Baseline: `79ced4f7a2f5e05722a77d23d75e37ee4eada058`

Classification: `POLICY_CHATTERING_WITH_VALUE_UPDATE_OSCILLATION_AND_LATER_DERIVATIVE_FLOOR_AMPLIFICATION__NOT_PURE_TWO_CYCLE__NOT_MONOTONE_SLOW`.

The classification is `POST_HOC_DESCRIPTIVE_FROM_PREREGISTERED_CONTINUOUS_METRICS__NOT_A_GATE`. The direct facts are the exact replays and their traces; the group contrasts are associations; event ordering is temporal evidence; no causal intervention was run.

## 1. Outcome

The accepted G2 control collapse is reproduced exactly: turn 1 converges in `20/31` calls and turn 2 in `2/31`. The dominant failed-call signature is persistent policy-label chattering with non-monotone value updates and frequent two-step label reversions. It is not a pure two-cycle: the failed-group median last-20 `two-step/one-step` value-distance ratios are about `1.35` (turn 1) and `1.27` (turn 2), not near zero. It is not uniformly monotone-slow: the failed-group median last-20 decrease fractions are only `0.526` and `0.579`, and the turn-2 failed median final/initial statistic ratio is `1.474`.

Derivative-floor activation becomes much stronger in failed calls, but it is later than the earliest policy/value instability and is neither necessary nor sufficient for failure. Operator signed off-diagonals and boundary row-sum defects are present early in both converged and failed accepted calls. Direct-solve absolute residuals begin in the same `4.39e-14` to `9.25e-14` range for all 62 calls, so the evidence does not support a linear-solve failure as the initiating event.

## 2. Exact-input identity and parity

The accepted D1-control manifest is `C60C353FE1ABC24509F5753E808F837BA19C9856B98FAE9998AB59DAC9BCE6BE`. All task-relevant persisted entering states, traces, HJB returns, runtime payload and runtime receipt were checked against that sealed manifest.

Exact reconstruction coverage is `62/62`. Each receipt binds province, turn, entering-value hash, source-faithful baseline-labor hash, grid hashes, economic/numerical parameters, raw and consumed `r_a`, composite household wage, guarded `wjt`, transfer income, borrowing gap, D1 OFF state and source identities. No approximate or synthetic input was used.

The first zero-HJB preflight used an incompatible array-hash encoding and correctly classified all calls as unproven. It was preserved under evidence root `-001`. The one authorized pre-HJB engineering retry changed only the serialization/hash header to the accepted dtype/shape convention; root `-002` then proved `62/62`. No scientific call had begun.

The parity gate consumed exactly two HJB calls on accepted turn-1 Beijing input:

- OFF versus ON: all scientific arrays, labels, iteration operator, post-convergence operator, iteration count, convergence flag and statistic exact-equal;
- OFF versus accepted NPZ: exact-equal for all non-pickled scientific fields;
- result: `PASS`.

## 3. Scientific call ledger

- parity HJB calls: `2` exactly;
- cross-section replay HJB calls: `62` exactly, one per proven province-turn;
- total HJB calls: `64`;
- scientific retries: `0`;
- HJB direct solves: `4,689` (`34` parity solves plus `4,655` replay solves);
- KFE calls: `0`;
- outer trajectory advancements: `0`;
- household steady-state calls: `0`;
- firm calls: `0`;
- MATLAB, K1B, K2, GE, annual downstream, shock, IRF and Results calls: `0`.

All `62/62` replay scientific outputs and `62/62` final iteration operators are exact-equal to accepted artifacts.

## 4. Four-group summaries

Values below are group medians. The derivative-floor share is the sum of forward and backward liquid-derivative hit shares, so its range is `[0,2]`.

| Group | n | iterations | final/initial stat | last-20 decrease fraction | two-step/one-step | label switches | two-step reversions | final floor share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| turn1 converged | 20 | 17 | 1.25e-8 | 0.789 | 2.968 | 38.5 | 2.0 | 0.0000 |
| turn1 failed | 11 | 100 | 1.37e-1 | 0.526 | 1.354 | 68.0 | 9.0 | 0.1675 |
| turn2 converged | 2 | 79.5 | 2.36e-9 | 0.579 | 2.012 | 28.5 | 2.25 | 0.28875 |
| turn2 failed | 29 | 100 | 1.474 | 0.579 | 1.270 | 179.0 | 35.5 | 0.3475 |

Turn-2 failures have much larger persistent label switching/reversion than the two turn-2 converged calls and the turn-1 converged group. Their last-20 statistic range is also material (median `35.21`) and their median final statistic exceeds their initial statistic. The two turn-2 converged calls are Chongqing and Guizhou; both had failed at turn 1, so they do not provide a stable province-level success subset.

## 5. Province transitions

All `20/20` provinces that converged at turn 1 fail at turn 2. In this transition set:

- policy switching first appears at iteration 2 in all 20;
- the first non-decreasing value-update statistic appears at iteration 2/3/4 in `11/8/1` calls;
- the first derivative-floor hit appears only at iteration 3/4/5 in `9/7/4` calls;
- turn-2 return state is upper-hit for 9 and unsaturated for 11;
- turn-2 guarded-`wjt` state is upper/lower/unsaturated for `14/4/2`.

This sequence shows that policy switching and usually value-update reversal precede derivative-floor activation. It is a sequential-state association, not a same-state causal comparison.

## 6. Derivatives, policies, values, operators and solves

Across all 40 failed calls, policy switching precedes the first derivative-floor hit in `40/40`; value-statistic non-decrease precedes it in `38/40`; two-step label reversion precedes it in `21/40`. Floor activation is therefore better described as a later amplifier/co-traveller than as the common initiating event. It is not sufficient for failure because one turn-2 converged call has final combined floor share `0.5775`; it is not necessary for convergence because converged calls can finish with or without hits.

The accepted safeguard floors only the liquid forward/backward derivatives used for consumption/labor. Illiquid forward/backward derivatives have no separate floor in the accepted solver, so their diagnostic `raw` and `used` records are identical and their floor-hit/deviation fields are zero by construction; no derivative formula or floor was changed.

The turn-2 failed group has median last-20 `179` label switches and `35.5` two-step reversions, versus `28.5` and `2.25` in turn-2 converged calls. The value-distance ratio does not identify an exact two-cycle, but the non-monotone statistic and repeated label reversions support a broader oscillatory/chattering fixed-point map.

All 62 calls have a nonzero accepted boundary row-sum defect at iteration 1 and a signed negative stored off-diagonal by iteration 3. These are known properties of the accepted iteration operator, appear in successful calls, and do not by themselves identify a new operator defect. Absolute solve residuals are uniformly small at iteration 1. Some failed calls later show large absolute residuals together with large operator/value scales, but the retained absolute residual alone is not a scale-normalized backward-error proof; it does not temporally lead the instability.

## 7. Return and wage associations

At turn 2, return-upper calls fail `16/18` while unsaturated calls fail `13/13`; both converged calls are return-upper. Guard saturation therefore does not separate success from failure within turn 2.

For entering guarded `wjt`, upper calls fail `22/24`, lower calls `4/4`, and unsaturated calls `3/3`; both converged calls are upper. At turn 1 all 31 entering `wjt` values are upper while outcomes split `20/11`. The wage guard state likewise does not explain the convergence split.

The scientific HJB consumes the composite household wage `w`, not `wjt`. The initial run metadata accidentally tested the composite wage against `[.8,1.3]`. This metadata-only issue was adjudicated offline against the accepted entering state, with no scientific rerun or output change; both consumed `w` and the correct guarded-`wjt` state are retained separately.

## 8. Ceiling and interpretation

A longer 100-iteration ceiling is not supported by this evidence. Failed calls are not uniformly approaching tolerance slowly: they show persistent switching/reversion, non-monotone updates and, in turn 2, a median final/initial statistic above one. Increasing the ceiling without changing or understanding the fixed-point mechanism would extend a chattering/oscillatory map rather than address a demonstrated slow contraction.

Direct replay facts establish exact reproduction and trace values. Cross-group differences establish association. Earliest-event comparisons establish ordering. No causal claim is supported because no same-state mechanism intervention was authorized or run.

## 9. Evidence and next authority

External evidence root:

`D:\ProjectTemp\ch5-mp4c-k1-hjb-mechanism-t1-t2-evidence-20260913-002`

External sealed-manifest file SHA-256:

`82A979E15DF22A651348F8C4E35FFE5688513E635877269DA98DF0755D03AF77`

Compact evidence is under `docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2/`.

Exactly one recommended future Owner gate, conditional on independent acceptance:

`OWNER_HJB_ITERATION_FIXED_POINT_MECHANISM_INTERVENTION_DESIGN_FREEZE`

That gate should design one isolated, same-input diagnostic intervention on the HJB map; it does not authorize a method, tolerance, ceiling, pseudo-time, derivative, price, boundary or economic change by itself.

KFE was not run and remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers. Standalone KKT residual remains unavailable. Results eligibility=`FALSE`.
