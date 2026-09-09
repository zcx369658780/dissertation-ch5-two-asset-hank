# CH5 MP4C corrected-2018 input single-turn validation

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Run the first bounded scientific validation using the accepted corrected 2018 data identity.

Execute **exactly one source-faithful 2018 multi-province ordered turn** using the accepted final static 2018 input identity, then stop. The purpose is to establish whether the corrected calendar/data contract can enter the existing runtime and complete one full ordered province turn without data-identity, household, firm, or update-order failure, and to measure how the corrected 2018 inputs alter the key observables previously implicated in the old mixed-year diagnosis.

This is NOT a steady-state run, NOT a convergence experiment, and NOT Results.

## 2. Accepted input authority

Use the accepted canonical workbook identity only if its exact SHA-256 matches:

`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`

Expected local artifact:

`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`

If the file is absent or hash mismatches, stop `BLOCKED_CANONICAL_INPUT_IDENTITY` without scientific calls.

Accepted temporal contract:

- `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`;
- steady year 2018;
- analysis index / data_MAT index = 10 / 10;
- level row 19 / year 2018;
- PLM vintage19, rolling window 2009–2018;
- same-year Zt.

Accepted Anhui final static identity:

- GDP = `34010.9` 亿元 -> `34010900.0` transformed;
- population = `6076` 万人 -> `607600.0` transformed;
- PIM CAP = `1357314108.2013683` -> `1357314108201.3684` transformed;
- alpha = `0.772866243094144`;
- same-year `IND_Zt = 0.0006934644495858679` at report display precision;
- Anhui indices: MATLAB 12, Python zero-based 11, Excel column N.

Do not substitute the old mixed-year 2018 state or the protected provisional `34010.91` final-use field for the official final-use `34010.9` value.

## 3. Frozen model contract

Do not change:

- model equations or province order;
- `At*N` productive-capital route;
- household `Lt` vs firm `Lt_supply` separation;
- PIM formula/parameters;
- PLM estimator;
- same-year Zt formula;
- household asset grid I20 b[-2,5], J20 a[0,10], Nz2 z[.8,1.3];
- `a_bar`, rate bounds, wage bounds, GovInv rule, migration logic;
- solver/tolerances/HJB/KFE algorithms;
- boundary laws, KKT rules, D1–D3 proposals.

No parameter tuning is permitted.

## 4. Runtime binding

Prefer existing accepted annual/pre-model and one-turn constructors. If the canonical workbook is not yet directly consumable by the runtime, a narrow validator/test harness may translate the accepted canonical rows into the existing immutable runtime input structures **without changing numeric values or economic meaning**.

Allowed harness code belongs under `validators/` and tests. Production model code should remain unchanged unless a purely representational input-binding defect makes one-turn execution impossible; if so, stop and report `CORRECTED_2018_RUNTIME_BINDING_GAP` rather than inventing a new economic mapping.

No silent fallback to old MAT/unversioned caches.

## 5. Scientific execution budget

Authorize exactly:

- canonical input identity/hash verification: unlimited static reads;
- one corrected-2018 ordered one-turn execution: **1**;
- the province-level household/firm/wage/migration/controller operations entailed by that single turn only;
- no second corrected turn;
- no old/mixed-year model rerun;
- no MATLAB model execution;
- no annual steady-state loop;
- no GE fixed-point/convergence loop;
- no IRF/dynamics/Results.

If the one-turn fails at province k or inside a household/HJB/KFE call, persist the full failure evidence and stop. No scientific retry. Engineering launch failures before any scientific entry may be repaired once if no scientific call occurred; count and report clearly.

All actual model calls, including failed calls, must be counted.

## 6. Required capture

Before execution persist the exact canonical 2018 runtime payload and hashes sufficient to reproduce it without embedding the private workbook.

For the single turn capture, at minimum, for all 31 provinces and in source order:

- entering state key fields used by one-turn;
- GDP, POP, CAP, alpha, initialized/same-year Zt, GovInv;
- firm raw `ra0`, used/clipped firm `ra`, `rk`, `wjt` raw/used where available;
- household carried/input `rah`, `rb`, composite wage, `Lt_prev`, destination `lt_supply`;
- household solver converged flag, iterations/statistic where available;
- returned aggregate C, effective L, A, B, A+B where valid;
- controller/gap/adaptation observables produced by the existing turn;
- exact province at which any failure occurs.

For Anhui, produce a compact forensic record comparable to the old accepted 2018 mixed-year diagnosis.

## 7. Required comparisons using saved evidence only

Do not rerun the old mixed-year model.

Where predecessor evidence already contains old turn-1 / early-prefix observables, compare corrected-turn values to saved old evidence and label the comparison `DESCRIPTIVE_INPUT_CORRECTION_EFFECT_ONLY`.

At minimum compare accepted old mixed-year vs corrected input identities for Anhui:

- GDP;
- POP;
- CAP;
- alpha;
- Zt;
- first-turn firm raw/used return if saved old turn-1 value is available;
- first-turn wage if available;
- household `rah` if available.

If a saved old observable is not recoverable, report `NOT_AVAILABLE_FROM_SAVED_EVIDENCE`; do not rerun it.

## 8. Numerical diagnostics

For each household call that returns, preserve available existing diagnostics without changing algorithms:

- HJB converged/statistic/iteration count;
- KFE return/failure status;
- aggregate validity;
- any existing generator/operator warnings already emitted by the accepted code path.

Do not add a new boundary law, source term, clipping rule, or tolerance to make the turn complete.

One-turn completion does not imply HJB/KFE global numerical validity or steady-state convergence.

## 9. Stop / verdict logic

Primary verdict must be one of:

- `CORRECTED_2018_SINGLE_TURN_PASS__FULL_ORDERED_TURN_COMPLETED`;
- `CORRECTED_2018_SINGLE_TURN_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER`;
- `CORRECTED_2018_SINGLE_TURN_FAIL__UPSTREAM_FIRM_OR_STATE_BLOCKER`;
- `CORRECTED_2018_RUNTIME_BINDING_GAP`;
- `BLOCKED_CANONICAL_INPUT_IDENTITY`.

Separately report:

- provinces attempted/completed;
- household calls attempted/returned/failed;
- HJB/KFE call/solve counts;
- firm/wage/controller call counts;
- corrected Anhui raw/used return and wage;
- whether any rate clips are active in turn1;
- whether one-turn output is finite;
- whether downstream steady-state execution is authorized: always `NO` in this task;
- Results eligibility: `FALSE`.

## 10. Evidence and outputs

Use a fresh external evidence root:

`D:\ProjectTemp\ch5-corrected-2018-single-turn-20260909-001`

If occupied use a fresh suffix; never overwrite.

Repository outputs may include:

- `docs/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION_REPORT.md`;
- machine-readable runtime-input receipt;
- per-province one-turn observables CSV/JSON;
- Anhui forensic JSON;
- saved-old comparison JSON;
- call ledger;
- tests and validator/harness code;
- manifest/readback.

Do not commit the private canonical workbook or protected source datasets.

## 11. Git closure

Run focused tests/static checks appropriate to changed harness code. Commit and non-force push a dedicated branch. Verify remote SHA and clean worktree. Do not merge main and do not start a second turn or any steady-state/GE/IRF experiment.

Results eligibility remains `FALSE` regardless of outcome.
