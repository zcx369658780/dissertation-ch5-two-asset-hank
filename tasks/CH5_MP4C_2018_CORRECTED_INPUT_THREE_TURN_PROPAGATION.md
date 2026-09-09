# CH5 MP4C corrected-2018 three-turn propagation gate

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Observe exactly one fresh corrected-2018 three-turn ordered trajectory, because turn 3 is the first household turn in which the corrected turn-1 firm used rate can enter the household composite illiquid return through the native lag/capital-allocation timing.

This is a bounded propagation diagnostic only. It is not a steady-state or convergence run.

## 2. Frozen input identity

Canonical workbook:

`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`

Required SHA-256:

`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`

If missing or mismatched, return `BLOCKED_CANONICAL_INPUT_IDENTITY` with scientific calls 0.

2018 contract remains:
- steady year 2018;
- analysis/data_MAT index 10/10;
- level row 19;
- PLM vintage 19;
- rolling window 2009–2018;
- same-year Zt;
- Anhui GDP 34010.9亿元, POP 6076万人, PIM CAP 1357314108.2013683万元, alpha 0.772866243094144.

Do not fallback to mixed-year or unversioned cache state.

## 3. Accepted predecessor evidence to reproduce

Fresh turns 1 and 2 must reproduce the accepted two-turn candidate `406d4132836e08d30b42b41e09f8237e6aac66a9` before entering turn 3.

Key Anhui accepted values include:
- turn1 household rah 0.09; firm ra used 0.02;
- turn2 household rah 0.0829892058879816;
- turn2 entering firm ra 0.02;
- turn2 firm raw ra0 -0.024968505109415375; used ra 0.02;
- turn2 raw/used wage 2.1373365306922518 / 1.3;
- turn2 nk_gap 0.34756612158493083;
- national turn2 max nk_gap 0.45946738761290562;
- no adaptation through turn2.

If fresh turn1 or turn2 materially mismatches accepted evidence, return `CORRECTED_2018_THREE_TURN_FAIL__PREDECESSOR_REPRODUCTION_MISMATCH` and stop before turn3.

## 4. Exact scientific budget

Allow exactly:
- one scientific Python process;
- one fresh source-faithful corrected-2018 ordered trajectory;
- turns 1, 2, and 3 only;
- 31 provinces in source order each turn;
- at most 93 province updates;
- scientific retries 0.

Disallow:
- turn 4 or later;
- steady-state loop;
- GE/annual model;
- MATLAB model;
- IRF/dynamics/Results;
- parameter/tolerance/grid/boundary/GovInv/PLM/PIM changes.

Every attempted scientific call, including failures, counts.

## 5. Central turn-3 question

Do not manually set turn3 `rah`.

Use the native state transition and prove the exact provenance of turn3 household `rah` for Anhui and, where practical, the 31-province vector.

Answer explicitly:
1. What is Anhui turn3 household `rah`?
2. Which source `ra` vector and turn produced it?
3. Does the corrected turn1 firm used `ra=0.02` now materially enter turn3 household `rah` under the native capital-allocation/composite rule?
4. How much residual legacy `.09` information remains, if any, and why?

Preserve vector SHA-256/source fields needed to prove the timing.

## 6. Per-turn observables

For turns 1–3 and all provinces record at least:
- household rah, rb, composite wage, entering Lt_prev;
- entering firm ra;
- firm raw ra0, used ra, rk;
- raw/used wage and clip flags;
- GDP/POP/CAP/alpha/Zt/GovInv;
- HJB converged/iterations/statistic;
- KFE returned/failure and saved raw residual if already available without new solver work;
- C/L/A/B/A+B if aggregate returns;
- nk_gap, yt_gap;
- controller/adaptation actions.

No new diagnostic solver calls beyond the native three-turn trajectory.

## 7. Anhui forensic transition

Produce a compact turn1/turn2/turn3 table and machine-readable forensic record.

Explicitly classify turn3 firm raw return as:
- LOWER (`ra0<0.02`),
- INTERIOR (`0.02<=ra0<=0.09`), or
- UPPER (`ra0>0.09`).

Also answer:
- wage raw/clip evolution;
- HJB/KFE execution after direct corrected-rate propagation;
- household aggregate evolution;
- whether the adaptation gate opens at turn3.

## 8. National transition summary

For each turn report:
- firm rate lower/interior/upper counts;
- wage lower/interior/upper counts;
- raw ra0 min/median/max;
- household rah min/median/max;
- nk_gap min/median/max;
- yt_gap min/median/max;
- HJB iteration min/median/max and failures;
- KFE failures;
- Zt/GovInv action counts.

The key route question is whether turn3 moves toward the existing `<0.1` adaptation gate or away from it. Do not infer convergence from three points.

## 9. Stop-on-failure

If any turn3 household/HJB/KFE/firm/state propagation fails, save all existing turn1–3-prefix evidence and stop. No scientific retry.

Use:
- `CORRECTED_2018_THREE_TURN_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER`, or
- `CORRECTED_2018_THREE_TURN_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER`.

Do not tune to obtain PASS.

## 10. Evidence and outputs

External evidence root:

`D:\ProjectTemp\ch5-corrected-2018-three-turn-20260909-001`

Use a fresh suffix if occupied; never overwrite prior evidence.

Repository outputs may include:
- `docs/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION_REPORT.md`;
- `reports/mp4c_2018_corrected_three_turn_20260909/turn_by_turn_observables.csv/json`;
- `.../anhui_forensic.json`;
- `.../turn3_rah_provenance.json`;
- `.../transition_summary.json`;
- `.../predecessor_reproduction.json`;
- `.../runtime_input_receipt.json`;
- `.../call_ledger.json`;
- tests, manifest and readback.

Private canonical workbook stays outside Git.

## 11. Verdicts

Use one primary verdict:
- `CORRECTED_2018_THREE_TURN_PASS__DIRECT_CORRECTED_RATE_PROPAGATION_OBSERVED`;
- `CORRECTED_2018_THREE_TURN_FAIL__PREDECESSOR_REPRODUCTION_MISMATCH`;
- `CORRECTED_2018_THREE_TURN_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER`;
- `CORRECTED_2018_THREE_TURN_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER`;
- `BLOCKED_CANONICAL_INPUT_IDENTITY`.

Even on PASS:
- turn4 authorized = NO;
- steady state authorized = NO;
- Results eligibility = FALSE.

Commit and non-force push a dedicated branch. Do not merge main. Do not launch a successor experiment.
