# CH5 MP4C corrected-2018 two-turn propagation validation

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Run a bounded corrected-2018 **two-turn** source-faithful ordered multi-province trajectory to observe the first propagation of the corrected current firm rate into subsequent household inputs.

Turn 1 has already been accepted and showed, for Anhui, entering household `rah=0.09` while current firm `ra0=-0.02496997113112164` and used `ra=0.02`. The scientific question in this task is therefore:

> When the corrected turn-1 state is propagated natively into turn 2, what household `rah`, firm return, wage, HJB/KFE status, gap and controller behavior appear?

This is not a steady-state task and must stop after turn 2.

## 2. Authority and baseline

Read live `main`, `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`, and `docs/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION_ACCEPTANCE.md` before execution.

Accepted single-turn candidate: `90ee5b29f3be070d9f8f28c9614e1b59fe798462`.

Canonical workbook identity remains:

`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`

SHA-256:

`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`

If the workbook is unavailable or hash-mismatched, stop before science with `BLOCKED_CANONICAL_INPUT_IDENTITY`.

## 3. Frozen corrected-2018 input contract

Keep unchanged:

- temporal contract `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`;
- `steady_year=2018`;
- analysis/data_MAT index `10/10`;
- level row `19`;
- PLM vintage `19`, rolling window `2009–2018`;
- Anhui GDP final-use `34010.9`亿元 / transformed `34010900.0`;
- Anhui population `6076`万人 / transformed `607600.0`;
- Anhui PIM capital `1357314108.2013683` / transformed `1357314108201.3684`;
- Anhui alpha `0.772866243094144`;
- same-year Zt `0.0006934644495858679`;
- source province order and all other accepted 2018 province inputs.

Do not fall back to old mixed-year or unversioned cache state.

## 4. Frozen model/numerical behavior

Do not change:

- equations;
- `At*N` productive-capital route;
- household `Lt` vs firm `Lt_supply` distinction;
- PIM, PLM or same-year Zt formula;
- rate/wage clipping rules;
- GovInv/Zt controller law or gate;
- `a_bar`;
- asset/productivity grids;
- HJB/KFE algorithm;
- boundary law;
- solver choice, tolerances, iteration limits;
- D1–D3 redesign status.

Production grid remains I20, b[-2,5], J20, a[0,10], Nz2, z[0.8,1.3].

## 5. Scientific execution budget

Execute exactly one fresh scientific trajectory containing **turn 1 and turn 2**, in the original 31-province source order.

Authorized maximum:

- scientific processes: 1;
- trajectories: 1;
- turns: exactly 2 unless an earlier failure stops execution;
- province updates: at most 62;
- no scientific retry;
- no third turn;
- no steady-state loop;
- no GE convergence loop;
- no annual batch/model;
- no MATLAB model;
- no IRF/dynamics/Results.

A failed model call counts. Preserve the failure and stop; do not relaunch science.

## 6. Turn-state propagation requirement

Do not manually substitute `rah=0.02` for turn 2. Use the native source-faithful state transition exactly as implemented.

The task must record, for every province, the actual turn-2 entering household `rah` and the state field(s) from which it was constructed. If `rah` remains `0.09`, changes to another value, or depends on an interprovince/composite return rule, document the exact runtime provenance without changing it.

This is the central acceptance object of the task.

## 7. Required observables by turn

For turns 1 and 2, record all 31 provinces in source order:

- entering `ra`/`rah`-related state fields;
- household `rah`, `rb`, composite wage, `Lt_prev`;
- firm `ra0`, used/clipped `ra`, `rk`;
- raw/used wage;
- GDP, POP, CAP, alpha, Zt, GovInv;
- HJB convergence, iteration count, statistic;
- KFE returned/failure;
- C, L, A, B, A+B if valid;
- `nk_gap`, `yt_gap` and controller-relevant max gaps;
- Zt/GovInv action before/after;
- any clipping flags.

## 8. Anhui forensic requirement

Produce one explicit turn-1 vs turn-2 Anhui record containing at least:

- household `rah` and exact state provenance;
- firm `ra0` and used `ra`;
- raw/used wage;
- `rk`;
- `GovInv` and Zt before/after controller;
- `Lt_prev`, destination `lt_supply`;
- HJB iterations/statistic;
- KFE status;
- aggregates;
- `nk_gap`, `yt_gap`;
- clip flags.

Answer explicitly:

1. Did turn-1 `ra=0.02` propagate into turn-2 household `rah`? If not, what native composite/lag rule determined turn-2 `rah`?
2. Did turn-2 firm raw return remain below the lower bound, move interior, or approach the upper bound?
3. Did wage clipping improve, worsen, or remain similar?
4. Did HJB/KFE remain executable after state propagation?
5. Did the adaptation gate open on turn 2?

## 9. National transition summary

For each turn report:

- number of provinces at lower/interior/upper firm-rate regions;
- number at lower/interior/upper wage regions;
- min/median/max raw `ra0` and province names for extrema;
- min/median/max `nk_gap` and `yt_gap`;
- HJB iteration distribution;
- HJB/KFE failure count;
- controller actions count.

Report changes from turn 1 to turn 2 descriptively. Do not claim convergence from two observations.

## 10. Accepted turn-1 evidence reuse

The previously accepted one-turn outputs may be read for comparison, but the authorized science trajectory is a fresh two-turn trajectory. Do not run a separate new turn-1-only science job.

If the fresh trajectory's turn-1 observables materially disagree with the accepted turn-1 evidence under identical canonical input and code, stop with:

`CORRECTED_2018_TWO_TURN_FAIL__TURN1_REPRODUCTION_MISMATCH`

and do not proceed to turn 2 unless the discrepancy is demonstrably non-scientific serialization/representation noise within already frozen exact contracts. Do not loosen tolerances.

## 11. Call ledger

Record exact actual counts:

- scientific processes;
- trajectory calls;
- turns entered/completed;
- province updates;
- household calls attempted/returned/failed;
- native initializations;
- labor roots/brentq;
- HJB calls/direct solves;
- KFE calls/direct solves;
- aggregate, firm, wage, migration, capital-allocation and controller calls;
- retries;
- MATLAB/GE/annual/IRF/Results counts.

## 12. Output and evidence

Use fresh evidence root:

`D:\ProjectTemp\ch5-corrected-2018-two-turn-20260909-001`

If occupied, use a fresh suffix; never overwrite prior evidence.

Produce repository-safe artifacts including:

- `docs/CH5_MP4C_2018_CORRECTED_INPUT_TWO_TURN_PROPAGATION_REPORT.md`;
- turn-by-turn per-province CSV/JSON;
- Anhui turn-1/turn-2 forensic JSON;
- transition summary JSON;
- runtime/canonical input receipt;
- call ledger;
- tests;
- manifest/readback.

Do not commit the private canonical workbook.

## 13. Verdicts

Use exactly one primary verdict:

- `CORRECTED_2018_TWO_TURN_PASS__TURN2_PROPAGATION_OBSERVED`;
- `CORRECTED_2018_TWO_TURN_FAIL__TURN1_REPRODUCTION_MISMATCH`;
- `CORRECTED_2018_TWO_TURN_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER`;
- `CORRECTED_2018_TWO_TURN_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER`;
- `BLOCKED_CANONICAL_INPUT_IDENTITY`.

Even if PASS:

- third turn authorized = NO;
- steady state authorized = NO;
- Results eligibility = FALSE.

Commit and non-force push a dedicated branch. Do not merge main and do not start successor science.
