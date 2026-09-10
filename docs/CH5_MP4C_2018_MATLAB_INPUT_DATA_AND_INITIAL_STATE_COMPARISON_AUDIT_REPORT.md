# Chapter 5 MATLAB 2018 input-data and initial-state comparison audit

Verdict: `MATLAB_2018_INPUT_DATA_AUDIT_PASS__MATERIAL_EXTERNAL_SCALE_DIFFERENCES_IDENTIFIED`

## Seven required answers

1. **The original MATLAB path is clear, and the label is not the consumed level year.** `multi_prov_HANK_12sts(10,0)` labels the run 2018 through `year=ii+2008`, then passes both `data_MAT{10}` and `data_year=10`. Because the cached level panels begin in 2000, GDP, CAP and POP row 10 are **2009**, not 2018. The cache is `数据估计结果_1000_100_0.mat`; the directly named `Multi_Province_12sts_2018.mat` steady-state cache is absent.
2. **Yes, there are material level differences.** Relative to corrected canonical 2018, all 31 GDP levels and all 31 capital levels differ by at least 10% in absolute value; 11 population levels and 15 Zt values do. Alpha is an exact 31/31 match at `0.772866243094144`. The differences are principally a mixed-year representation: 2009 GDP/CAP/POP, fixed-2020 level-derived Zt, and PLM vintage 19 alpha, versus corrected 2018 levels/same-year Zt and the same vintage 19 alpha.
3. **Largest absolute relative differences:** GDP 贵州 `-74.880432%`; PIM capital 贵州 `-89.205415%`; POP 西藏 `-16.384181%`; Zt 江苏 `-82.371344%`. 安徽 is also material: GDP `10864.68` versus `34010.9` 亿元 (`-68.055300%`), PIM capital `228121755.48548824` versus `1357314108.2013683` 万元 (`-83.193149%`), POP `6131` versus `6076` 万人 (`+0.905201%`), and Zt `0.000641551386937363` versus `0.0006934644495858679` (`-7.486045%`).
4. **Yes.** There is a proven year/vintage mixture and a cache-provenance issue: the regression cache freezes Zt from row 21 (2020) for every `mydata2{ii}`, while the 2018 label consumes row 10 (2009) levels. The source documents capital in 万元 but applies the same `x1000` multiplier used for GDP in 亿元; the source gives no dimensional conversion rationale. This is a documented scale ambiguity, not a corrected unit conversion invented by this audit.
5. **The strongest outer-loop scale channels are N, capital/GovInv and Zt.** N multiplies saved household `At` in capital allocation and migration labor; GovInv is initialized equal to the mismatched Kt0 and is added directly to Kt_supply; Zt and alpha enter the firm production and price equations; GDP/Y0 is the controller target. Initial `ra=.09` is already at its upper bound, and initial `wjt=.6` lies below the firm-output lower bound `.8` before the first firm call. These facts can amplify or clip transitions, but this audit does not identify the cause of turn3 asset collapse.
6. **Unavailable objects:** original MATLAB 2018 persisted At/Bt/Lt/Ct, Kt_supply, Kt_total, first-turn firm ra/wjt, and next-turn rah/household wage are `NOT_AVAILABLE_WITHOUT_SCIENTIFIC_RERUN`, because the 2018 steady-state MAT cache is absent. Accepted corrected and legacy replay values are shown only in separately labelled columns; they are not substituted for missing original MATLAB results.
7. **All scientific/model calls are exactly 0.** Only source inspection, read-only XLSX/MAT extraction, hashing, deterministic arithmetic, serialization and static assertions ran. No MATLAB/Python household, HJB, KFE, firm, wage, migration, allocation, outer turn, steady state, GE, annual, IRF, Results, root, direct, iterative or eigen scientific solve was invoked.

Results eligibility remains `FALSE`. This PASS is only a data/provenance audit result.

## Authority and identities

- Fresh live baseline: `origin/main=31b8de0ef897e3edd8b88115e5cd64be2b8aa80c`.
- Exact task: `tasks/CH5_MP4C_2018_MATLAB_INPUT_DATA_AND_INITIAL_STATE_COMPARISON_AUDIT.md`.
- The current rule index activates this task with a zero-call budget. The status and handoff documents still say no active task; this inconsistency is preserved rather than silently harmonized.
- Canonical workbook SHA-256: expected and observed `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`.
- Protected MATLAB root remained read-only: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.
- Final external evidence root: `D:\ProjectTemp\ch5-2018-matlab-input-data-initial-state-audit-20260910-005`. Earlier `-001` through `-004` roots are superseded static-extraction/finalization attempts and were not overwritten.

## Reconstructed MATLAB data route

`main.m` calls `multi_prov_HANK_12sts(ii,0)`. In `multi_prov_HANK_12sts.m:118-133`, `ii=10` creates the 2018 filename but passes `data_MAT{10}` and `data_year=10`. With a missing steady cache, `load_GDPdata` reads the processed workbook and then loads the regression cache.

The source chain is:

`2000年后各省数据_填充NA.xlsx`
→ GDP/总资本存量/常住人口 panels
→ `x1000 / x1000 / x100`
→ `数据估计结果_1000_100_0.mat::mydata2{10}`
→ GDP/CAP/POP row 10 (workbook-labelled 2009)
→ initialization of Yt0/Kt0/N.

The independent cache-to-workbook readback is exact for all 31 provinces: maximum absolute differences after the declared transforms are `0` for GDP, CAP and POP.

For alpha and Zt, `load_GDPdata.m:115-137` selects `总面板回归系数_19_行业4`, repeats that scalar alpha across provinces, and computes every Zt from **row 21**. The cache reconstructs from the static formula

`Zt = GDP(row21) * CAP(row21)^(-alpha) * POP(row21)^(alpha-1)`

with maximum absolute difference `1.0842021724855044e-19`. Row 21 is 2020. Thus the original 2018-labelled object is not simply “old 2018”; it is a mixed 2009-level/2020-Zt/vintage19 object.

Province order is exact across the MATLAB cache, processed workbook and canonical `PROVINCE_ORDER`: 31/31 match; 安徽 is MATLAB index 12 / Excel column N.

The PIM source was also followed through its direct helper: `It_to_Kt.m` defines `K0=I0/.1` and `Kt=(1-delta)K(t-1)+I(t-1)`, with `delta=.096` passed by the loader. `load_distdata.m` and its explicitly named distance workbook were read and hashed because the resulting migration-cost matrix enters labor allocation, but that matrix is outside the requested province-level GDP/CAP/POP/Zt numeric comparison.

## Unit and scale findings

| Object | MATLAB original 2018-labelled route | Corrected canonical 2018 | Classification |
| --- | --- | --- | --- |
| GDP | 2009 raw 亿元, then `x1000` | 2018 raw/final-use 亿元, then `x1000` | `YEAR_OR_VINTAGE_MISMATCH` |
| POP | 2009 raw 万人, then `x100` | 2018 final-use 万人, then `x100` | `YEAR_OR_VINTAGE_MISMATCH` |
| alpha | PLM vintage19 scalar | PLM vintage19 scalar | `EXACT_MATCH` |
| Zt | 2020 levels with vintage19 alpha | 2018 levels with vintage19 alpha | `YEAR_OR_VINTAGE_MISMATCH` |
| PIM capital | 2009 万元, then `x1000` | 2018 万元, then `x1000` | `YEAR_OR_VINTAGE_MISMATCH`; dimensional scaling caveat |
| GovInv | `Kt0 * 1`, therefore 2009 transformed capital | corrected 2018 transformed capital | inherited year/scale mismatch |

The transformed capital scale is especially consequential. The code describes total capital in 万元 but multiplies it by `GDP_multiplier=1000`, even though GDP is in 亿元. Because both original and corrected Python-bound objects preserve this implemented transform, the 31-province ledger separately records raw capital, transformed capital and year-driven comparison. No undocumented rescaling was applied.

Deterministic initial K/Y, K/L and Y/N ratios are diagnostic scale summaries, not equilibrium ratios. Original-route extremes are: K/Y 湖南 `13268.605703167113` to 西藏 `33342.511991047664`; K/L 贵州 `182997.16216324037` to 上海 `1301888.2464286773`; Y/N 贵州 `10.903760248798417` to 上海 `71.2237363591943`. The full ledger also records corrected canonical counterparts.

## Initial-state and saved-object audit

Source initialization is common across provinces: `At=2`, `Bt=1`, `Lt=.8`, `Ct=4`, `ra=.09`, `rah=.09`, `rb=.02`, `wjt=.6`, household composite wage `w=20`. The equilibrium initializer then replaces Lt with N, Kt/Kt0 with the selected capital row, Yt/Yt0 with the selected GDP row, and GovInv with `Kt0*1`.

- Initial ra is at the configured upper bound `[.02,.09]` in 31/31 provinces.
- Initial rah equals `.09`, but rah has no native firm-rate clipping rule; equality with the ra upper bound is descriptive only.
- Initial wjt `.6` is below the configured firm-output bound `[.8,1.3]` in 31/31 provinces. It is an entering state, not evidence of a returned clipped wage.
- In accepted corrected turn 1, firm ra clips lower in 31/31 provinces; wage clips lower/upper/interior in `5/22/4` provinces. 安徽 raw/used ra is `-0.02496997113112164/.02`, and raw/used wage is `2.5721358283733027/1.3`.
- Corrected turn1 persisted At and Bt are available and labelled as corrected evidence. Corrected Kt_supply was not persisted in the repository-safe turn1 table and remains unavailable here.
- Accepted legacy replay turn1 At/Bt/Kt_supply/GovInv/Kt_total are included in dedicated `legacy_replay_*` columns only. Its GovInv/private-supply ratio ranges from 西藏 `60.36422276744836` to 山东 `1732.1270936845806`; this demonstrates the saved route's state-capital dominance but is not an original-MATLAB-2018 cache result.

## Outer-loop entry map

`GDP / N / alpha / Zt / GovInv / initial ra-rb-rah-w`
→ household inputs
→ saved `At, Bt, Lt, Ct`
→ migration and `At*N` capital allocation
→ `Kt_supply + GovInv`
→ firm `Yt, ra, wjt`
→ wage aggregator and next `w`
→ old-ra portfolio composite and next `rah`
→ controller Zt/GovInv updates.

The static role ledger identifies each object as exogenous data, regression-derived calibration, initialized state, household output, allocation output, firm output or controller-updated object. N and At meet multiplicatively; GovInv enters firm capital additively; Zt and alpha enter production; GDP/Y0 controls later Zt adjustment. These are propagation locations, not a causal attribution of the accepted turn3 collapse.

## Outputs and verification

Repository-safe evidence is under `reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/`:

- `province_comparison_ledger.csv` and `.md`: 31 provinces, all requested available fields and explicit missing markers;
- `data_source_lineage.csv`;
- `unit_scaling_audit.csv`;
- `largest_discrepancy_summary.csv`;
- `outer_loop_variable_role_map.csv`;
- `source_data_hash_receipt.json`;
- `call_ledger.json`;
- `audit_summary.json`;
- `tests.txt`, `tests_receipt.json`, `static_checks.txt`;
- `manifest.json` and `manifest_readback.json`.

Private workbook/MAT source files are not committed. The report and ledgers disclose only the minimum derived province-level values required by the task.

## Scientific boundary

The audit establishes material external-input and initialization discrepancies and their entry points. It does not establish that any one discrepancy caused turn3 asset collapse, validate HJB/KFE, prove outer-loop convergence, authorize boundary/controller changes, or make Results eligible.
