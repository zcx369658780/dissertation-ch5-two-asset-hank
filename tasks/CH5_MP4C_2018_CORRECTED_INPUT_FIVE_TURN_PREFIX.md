# CH5 MP4C corrected-2018 five-turn bounded prefix

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Run one fresh corrected-2018 trajectory for exactly five turns in the frozen 31-province source order, with no scientific retry, to observe whether the direct corrected-rate propagation seen at turn 3 continues toward a stable short-prefix pattern or reveals an asset-distribution / KFE validity blocker.

This is not a steady-state task. It does not authorize turn 6+, GE convergence, annual execution, IRF or Results.

## 2. Accepted predecessor

Read and bind:

- `docs/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION_REEXECUTION_ACCEPTANCE.md`;
- accepted candidate `3eb5f003b40c66e96a2b1a694e05b24fce9aa6e4`.

Turn 1–3 are accepted predecessor evidence and must reproduce before turn 4 is entered.

Key Anhui accepted values:

- turn1 `rah=.09`, raw `ra0=-.02496997113112164`, used `ra=.02`, raw wage `2.5721358283733027`, HJB iterations 64, `nk_gap=98575.17052447716`;
- turn2 `rah=.0829892058879816`, raw `ra0=-.024968505109415375`, used `ra=.02`, raw wage `2.137336530692252`, HJB iterations 31, `nk_gap=.34756612158493083`;
- turn3 `rah=.0184420457528848`, raw `ra0=-.024968792977977675`, used `ra=.02`, raw wage `2.205170377619017`, HJB iterations 11, `nk_gap=.16103719246632298`.

Accepted turn3 assets:

- `A=.013287859137578914`;
- `B=1.8786740319061375`;
- `A+B=1.8919618910437164`.

## 3. Canonical input identity

Use only:

`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`

Required SHA-256:

`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`

If missing or mismatched: `BLOCKED_CANONICAL_INPUT_IDENTITY`, scientific calls 0.

## 4. Scientific budget

Exactly one fresh scientific process and one trajectory.

Maximum:

- turns: 5;
- province updates: 155;
- scientific retries: 0.

Forbidden:

- turn 6 or later;
- steady-state loop;
- GE convergence;
- annual model;
- MATLAB model;
- IRF/dynamics/Results.

Failed calls count.

## 5. Reproduction gate

Fresh turns 1–3 must reproduce the accepted predecessor evidence before entering turn 4.

Compare all task-relevant observables, including household `rah`, composite wage, firm raw/used `ra`, raw/used wage, HJB iterations/statistic, KFE return, C/L/A/B, `nk_gap`, `yt_gap`, and controller actions.

If any accepted turn has a material mismatch, stop with one of:

- `CORRECTED_2018_FIVE_TURN_FAIL__TURN1_REPRODUCTION_MISMATCH`;
- `...TURN2_REPRODUCTION_MISMATCH`;
- `...TURN3_REPRODUCTION_MISMATCH`.

Do not relax comparator to continue.

## 6. Turn 4–5 core questions

Observe, do not infer:

1. Does household `rah` remain near/below `rb=.02`, rebound, or move materially elsewhere?
2. Do all firm raw returns remain in LOWER region, or do any provinces move to INTERIOR/UPPER?
3. Does wage clipping continue to relax?
4. Does national max `nk_gap` fall below the native `.1` adaptation gate by turn 4 or 5?
5. If adaptation opens, what native actions occur on that same turn?
6. Does the sharp turn-3 A/B transition stabilize, rebound, or deteriorate?
7. Are returned KFE densities numerically admissible enough for prefix interpretation, or do source-free stationarity / sign / boundary diagnostics reveal a blocker?

## 7. Required per-turn/per-province observables

For all 31 provinces, turns 1–5:

- household `rah`, `rb`, composite wage, entering `Lt_prev`;
- C, L, A, B, A+B;
- HJB converged, iterations, statistic;
- KFE returned;
- firm raw `ra0`, used `ra`, `rk`;
- raw/used wage;
- rate/wage clip region;
- `nk_gap`, `yt_gap`;
- Zt/GovInv before/action/after;
- key entering state identities.

## 8. KFE / distribution diagnostics

Without changing the existing solver or model, capture available diagnostics for each returned household density, especially turns 3–5.

At minimum, where the current code path exposes or permits pure post-processing from saved operator/density artifacts:

- normalized mass;
- density min/max;
- negative-entry count and weighted negative mass;
- raw contaminated-row residual if already available;
- source-free `||A.T @ density||_inf` or equivalent accepted operator residual when reconstructible from saved operator/density without another solve;
- denominator/scale used for any residual ratio;
- upper/lower b and a outward-leak counts/rates when reconstructible from saved drift/operator;
- upper-b face probability mass if density exists;
- whether diagnostics are `VALID`, `DIAGNOSTIC_ONLY`, or `NOT_AVAILABLE`.

Do not add a source, alter a boundary law, repair the generator, change pinning, or rerun KFE merely to obtain a better diagnostic.

If the existing returned density fails a material source-free stationarity or positivity/admissibility check, preserve the evidence and classify the prefix accordingly. Do not call aggregate changes economically valid merely because KFE returned.

## 9. Asset-transition focus

For Anhui and national summaries, explicitly track turn 1–5:

- A;
- B;
- A+B;
- change and ratio vs prior turn;
- `rah-rb`;
- whether A/B behavior coincides with a change in KFE admissibility diagnostics.

The turn-3 collapse in A and A+B is diagnostic and must not be silently smoothed or normalized away.

## 10. Adaptation gate

Keep native rule unchanged.

If national max `nk_gap >= .1`, record gate closed.

If the native gate first opens at turn 4 or turn 5, execute only the actions the source code naturally performs on that turn and save before/action/after evidence. Do not add another turn to observe consequences.

## 11. Frozen invariants

Do not modify:

- canonical data or temporal contract;
- GDP/POP/PIM/PLM/alpha/Zt formula;
- province order/distance matrix;
- At*N productive-capital route;
- household Lt vs firm lt_supply distinction;
- capital-allocation rule;
- GovInv/adaptation rule;
- rate/wage bounds;
- `a_bar`;
- grid;
- HJB/KFE equations/algorithms;
- boundary laws / D1–D3;
- solver/tolerances/max iterations.

No tuning for PASS.

## 12. Evidence root

Use fresh root:

`D:\ProjectTemp\ch5-corrected-2018-five-turn-20260909-001`

If occupied, use a fresh suffix. Never overwrite prior evidence.

Required repository-safe outputs should include:

- `docs/CH5_MP4C_2018_CORRECTED_INPUT_FIVE_TURN_PREFIX_REPORT.md`;
- `reports/mp4c_2018_corrected_five_turn_20260909/runtime_input_receipt.json`;
- predecessor reproduction receipts for turns1–3;
- turn-by-turn observables CSV/JSON;
- Anhui forensic JSON;
- national transition summary;
- asset transition summary;
- KFE/distribution diagnostics summary;
- controller/adaptation summary;
- call ledger;
- tests/static checks;
- manifest/readback;
- terminal result.

Do not commit the private canonical workbook or proprietary source data.

## 13. Allowed verdicts

- `CORRECTED_2018_FIVE_TURN_PASS__BOUNDED_PREFIX_EXECUTABLE_AND_DIAGNOSTICALLY_STABLE`;
- `CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER__KFE_OR_DISTRIBUTION_VALIDITY`;
- `CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER__ASSET_TRANSITION_INSTABILITY`;
- `CORRECTED_2018_FIVE_TURN_FAIL__TURN1_REPRODUCTION_MISMATCH`;
- `CORRECTED_2018_FIVE_TURN_FAIL__TURN2_REPRODUCTION_MISMATCH`;
- `CORRECTED_2018_FIVE_TURN_FAIL__TURN3_REPRODUCTION_MISMATCH`;
- `CORRECTED_2018_FIVE_TURN_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER`;
- `CORRECTED_2018_FIVE_TURN_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER`;
- `BLOCKED_CANONICAL_INPUT_IDENTITY`.

A PASS requires both execution through turn 5 and no newly established material distribution-validity blocker within the diagnostics available in this task. It still does not prove steady-state convergence.

## 14. Authority after completion

Even on PASS:

- turn 6+ unauthorized;
- steady state unauthorized;
- GE/annual/IRF unauthorized;
- Results eligibility FALSE.

Commit and non-force push a dedicated branch; do not merge main and do not start a successor scientific task.
