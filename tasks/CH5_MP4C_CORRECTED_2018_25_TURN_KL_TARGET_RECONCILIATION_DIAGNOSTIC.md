# Chapter 5 MP4C corrected-2018 25-turn K/L target reconciliation diagnostic

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Run exactly one bounded corrected-2018 trajectory, using the newly accepted Python runtime input-binding repair, for at most 25 outer turns. The sole scientific objective is to quantify how model-implied province capital and labor compare with the 2018 data targets after the early transient, especially turns 20-25, before any further redesign of `GovInv` initialization or `Lt_seperate`.

This task answers the Owner's question:

- Is total firm capital `Kt_supply + GovInv` systematically above/below the 2018 PIM capital target after the early transient?
- Is destination firm labor from the existing migration/allocation mechanism systematically above/below the initialization population/labor proxy?
- Which component, private household capital supply or GovInv, dominates any K gap?
- Is the current `GovInv0=Ktarget` source-faithful initialization likely to mechanically overshoot total K once private capital supply becomes nonzero?

This is a diagnostic, not parameter tuning, not production steady-state acceptance, and not Results.

## 2. Required authority

Fresh-read live `origin/main`, then read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_REPORT.md`;
- `docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_ACCEPTANCE.md`;
- `src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py`;
- the corrected single-/multi-turn execution harnesses currently used by the repaired route;
- accepted raw-NBS rebuild, unit-normalized initialization probe, firm-price forensic, and MATLAB multi-province logic audit.

The rejected old-scale 100-turn candidate `242e853708d3d0d4f891c7a043d7d4e3fba05c50` is historical diagnostic evidence only and must not be reused as runtime authority.

## 3. Frozen runtime contract

The scientific run must use only the accepted corrected-2018 runtime route:

- actual 2018 GDP;
- actual 2018 population;
- raw-NBS GFCF Track-A PIM capital;
- `delta_pim=.096`;
- `alpha_raw=alpha_used=.7380939146868483`;
- `MU=10万元`;
- `NU=100 persons`;
- GDP and capital: 亿元 `×1000 -> MU`;
- population: 万人 `×100 -> NU`;
- same-year `Zt0` identity;
- firm depreciation `.025` remains separate;
- source bounds unchanged;
- source-lagged `rah` unchanged;
- `beta_a=1` remains `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`;
- no new `w/rah` damping;
- no new hysteresis;
- no new GovInv damping;
- no new price bounds;
- no HJB/KFE repair.

The accepted hard pre-science validator must run successfully before any scientific state is advanced.

## 4. GovInv rule for this diagnostic

Preserve the current source-faithful initialization rule exactly for this one diagnostic:

`GovInv0 = Ktarget_2018_TrackA_MU`.

Do not redesign it in this task.

This run is specifically intended to test whether, after household private capital supply appears, the identity

`firm_K = Kt_supply + GovInv`

creates systematic overshoot relative to `Ktarget`.

For every province and turn, preserve and report separately:

- `Ktarget_2018_MU`;
- `Kt_supply_private_MU`;
- `GovInv_MU`;
- `firm_K_total_MU`;
- `firm_K_total / Ktarget`;
- `Kt_supply_private / Ktarget`;
- `GovInv / Ktarget`.

## 5. Labor contract and comparison

Do not redesign `Lt_seperate`.

Use the existing source-faithful labor allocation route. For every province and turn, keep distinct:

- household labor per-capita / household aggregate object;
- origin population proxy `N0_NU`;
- migration/allocation matrix `Lt_mat(destination, origin)`;
- destination firm labor supply `firm_Lt_supply = row sum of Lt_mat`;
- initialization comparison target `Ltarget_proxy = N0_NU`.

The task must explicitly state that `Ltarget_proxy=N0` is only the initialization population/labor proxy and is not observed interprovincial employment by workplace.

For every province and turn, report:

- `Ltarget_proxy_NU`;
- `firm_Lt_supply`;
- `firm_Lt_supply / Ltarget_proxy`;
- net destination labor gain/loss relative to proxy;
- top origin contributions if already available without additional model calls.

Also verify the national conservation/aggregation identity implied by the source allocation routine, if source algebra supports one. Do not impose a new conservation law that is not in source.

## 6. Execution budget

Exactly one scientific trajectory.

Maximum:

- 25 outer turns;
- at most 775 province household updates;
- no second trajectory;
- no parameter-cell comparison;
- no rerun after a scientifically completed trajectory;
- no post-hoc tuning.

Engineering retry is allowed only if failure occurs before scientific state advances and must be logged.

Stop early only for:

1. source final steady-state predicate; or
2. hard scientific failure preventing continuation.

Do not stop merely because price bounds are hit or because K/L gaps are large.

## 7. Mandatory per-turn national diagnostics

For each completed turn record at least:

- turn;
- 31/31 household convergence count;
- `ra` lower/interior/upper counts;
- `wjt` lower/interior/upper counts;
- max/median `firm_K_total/Ktarget`;
- min/max `firm_K_total/Ktarget`;
- max/median `Kt_supply_private/Ktarget`;
- max/median `GovInv/Ktarget`;
- count of provinces with `firm_K_total/Ktarget > 1.05`, `>1.25`, `>2`;
- count below `.95`, `.75`, `.5`;
- max/median/min `firm_Lt_supply/Ltarget_proxy`;
- count of provinces with labor ratio outside `[.8,1.2]`;
- national sum of target K, private K supply, GovInv, total firm K;
- national sum of Ltarget proxy and destination firm labor;
- KN gap, Y/Yprev gap, GDP level gap;
- Zt adjustment count;
- GovInv decrease/increase/hold count;
- KFE/HJB diagnostic status already produced by the current runtime.

## 8. Province ledgers

Create one machine-readable row per province per turn with at least:

- turn;
- province_index;
- province_name;
- `Ktarget_2018_MU`;
- `Kt_supply_private_MU`;
- `GovInv_before_MU`;
- `GovInv_after_MU`;
- `firm_K_total_MU`;
- K ratios above;
- `Ltarget_proxy_NU`;
- `firm_Lt_supply`;
- labor ratio;
- household At, Bt, Lt, Ct;
- raw/used ra;
- rah;
- raw/used wage;
- household composite wage;
- Y;
- Zt;
- controller action;
- KFE/HJB diagnostic labels.

## 9. Required turn-20-to-25 analysis

The report must focus on turns 20, 21, 22, 23, 24, 25 if reached.

For each province provide either a compact table or a summarized mean/median over turns 20-25 for:

- `firm_K_total/Ktarget`;
- `Kt_supply_private/Ktarget`;
- `GovInv/Ktarget`;
- `firm_Lt_supply/Ltarget_proxy`.

Classify each province's late-window K status as:

- `K_NEAR_TARGET` for ratio in `[.9,1.1]`;
- `K_MODERATELY_HIGH` for `(1.1,1.5]`;
- `K_SEVERELY_HIGH` for `>1.5`;
- `K_MODERATELY_LOW` for `[.5,.9)`;
- `K_SEVERELY_LOW` for `<.5`.

Classify late-window L status analogously with the same ratio thresholds, but label explicitly as comparison to the proxy, not observed workplace labor.

## 10. Anhui trace

Provide full Anhui rows for turns 1,2,3,5,10,15,20,21,22,23,24,25 if reached, including:

- Ktarget;
- private K supply;
- GovInv;
- total firm K;
- all K ratios;
- Ltarget proxy;
- firm Lt supply;
- labor ratio;
- At/Bt/Lt/Ct;
- ra/rah;
- wage/composite wage;
- Y/Zt;
- KN/GDP gaps.

## 11. Interpretation questions

The report must answer directly:

1. After turn 20, is total firm K generally above, near, or below the Track-A K target?
2. If K is high, how much is due to GovInv and how much to private `Kt_supply`?
3. Does `GovInv0=Ktarget` mechanically imply initial/early K overshoot once private capital is added?
4. Does the existing GovInv controller reduce this overshoot fast enough by turn 20-25?
5. Is destination firm labor materially different from the population proxy after migration allocation?
6. Which provinces gain/lose the most labor relative to proxy?
7. Would an initialization redesign `GovInv0=max(Ktarget-Kt_supply0,0)` be mechanically better aligned with Ktarget, based only on accounting—not convergence? Do not implement it; only evaluate the accounting implication.
8. Would using migration-adjusted destination labor as a calibration/reference object plausibly reduce firm-price scale mismatch? Again, do not implement or tune; report only what the observed ratios imply.
9. Are HJB/KFE validity blockers still present independently of K/L calibration?

## 12. No tuning / no redesign

This task must not modify:

- production runtime economics;
- `Lt_seperate` formula;
- GovInv initialization rule;
- GovInv controller;
- price bounds;
- alpha;
- PIM depreciation;
- firm depreciation;
- asset bridge;
- HJB/KFE;
- grid;
- damping/hysteresis.

The task may add diagnostic instrumentation/harness code only if it does not alter scientific state or equations.

## 13. Evidence outputs

Use a fresh evidence root such as:

`D:\ProjectTemp\ch5-corrected-2018-kl-reconciliation-25turn-20260910-001`

Required repository-safe outputs:

- `docs/CH5_MP4C_CORRECTED_2018_25_TURN_KL_TARGET_RECONCILIATION_DIAGNOSTIC_REPORT.md`;
- `reports/mp4c_corrected_2018_25turn_kl_reconciliation_20260910/province_turn_kl_ledger.csv`;
- `.../national_turn_summary.csv`;
- `.../late_window_20_25_province_summary.csv`;
- `.../anhui_trace.csv`;
- `.../govinv_k_decomposition_summary.csv`;
- `.../labor_migration_proxy_summary.csv`;
- `.../scientific_validity_ledger.csv`;
- `.../call_ledger.json`;
- runtime input receipt proving corrected Track-A route;
- source/hash receipt;
- tests/static checks;
- manifest/readback;
- reproducible bounded execution harness/invocation receipt.

Do not commit private raw workbooks or protected MATLAB files.

## 14. Allowed verdicts

- `CORRECTED_2018_25TURN_KL_RECONCILIATION_PASS__LATE_WINDOW_KL_GAPS_QUANTIFIED`;
- `CORRECTED_2018_25TURN_KL_RECONCILIATION_PARTIAL__EARLY_HARD_FAILURE_BEFORE_LATE_WINDOW`;
- `CORRECTED_2018_25TURN_KL_RECONCILIATION_BLOCKED__RUNTIME_CONTRACT_OR_LEDGER_INCOMPLETE`.

A PASS means the diagnostic comparison is complete; it does not mean the model converged.

## 15. Git boundary

Use a dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit and non-force push candidate;
- do not merge main;
- do not publish successor scientific task;
- Results eligibility remains FALSE.

Return to ChatGPT Reviewer with verdict, branch, candidate SHA, actual turns completed, late-window K/L findings, Anhui trace summary, scientific validity status, and report path.
