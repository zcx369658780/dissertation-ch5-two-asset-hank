# Chapter 5 Two-Asset HANK MP4A 2009 Provenance Resolution, Primary Data Binding, and Annual Route Preparation Report

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Live task authority: `c52016b47ae2e56e550f8b0a180cddbd744c377b`

## 1. Verdict

`MP4A_2009_PROVENANCE_RESOLUTION_PRIMARY_DATA_BINDING_AND_ANNUAL_ROUTE_PREPARATION_BLOCKED`

Required sub-classification:

`YEAR_MAPPING_SOURCE_CONFLICT_BLOCKED`

The workbook calendar axis is unambiguous, but the current MATLAB annual route couples three meanings to `ii` that cannot identify calendar 2009 simultaneously. In the call with `ii=1`, MATLAB labels the output 2009 while selecting `data_MAT{1}` and passing `data_year=1`; the downstream economic data are consequently workbook calendar 2000. Selecting workbook calendar 2009 requires `data_year=10`, but passing `ii=10` selects `data_MAT{10}` and labels the output 2018. MP4A therefore stopped before annual implementation or canonicalization, as the live task requires.

No PASS freeze marker is claimed. In particular, `MP4A_2009_CALENDAR_DATASET_INDEX_MAPPING_ACCEPTED`, `MP4A_2009_CANONICAL_PREMODEL_INPUT_IDENTITY_ACCEPTED`, and `MP4A_MP4B_STATIONARY_PARITY_CONTRACT_ACCEPTED` are not established.

## 2. Live authority and continuity

- Fresh-fetched start: `HEAD == origin/main == c52016b47ae2e56e550f8b0a180cddbd744c377b`.
- Accepted MP3 commit `dbd80110a6d4d055c0326a309cdce214abfd50ce` is an ancestor.
- Owner-decision commit `0af28e227a3438a72e3f69f5985a3d707b0e5432` is an ancestor.
- Worktree was clean at execution start.
- No `src/` or `exports/` path differs between accepted MP3 and the MP4A authority commit.
- Accepted standalone household oracle SHA-256 remains `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.
- Accepted multi-province source identities observed: `province_contracts.py` SHA-256 `3E5DBA93C6283588447A2A4E507F5C9425B8A5335C63E97FE78B9C38F82C90D1`; `one_turn.py` SHA-256 `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`.

The controlling Owner markers were read and retained: multi-year 2009--2023 is the intended final contract; 2009 is the first controlled anchor; single-year stationary parity precedes batching; the MAT calibration cache is non-primary; primary calibration authority is the source workbooks, regression inputs, and `load_GDPdata` transformation.

## 3. Source-line contract and exact calendar/index adjudication

The filled workbook has a header at physical Excel row 1 and explicit calendar years 2000--2023 at physical rows 2--25. Therefore calendar 2009 is physical row 11, zero-based data index 9, and one-based MATLAB data-row index 10.

| Representation | Source-defined value for route call `ii=1` | Value required for workbook calendar 2009 | Evidence |
|---|---:|---:|---|
| Workbook calendar value | 2000 | 2009 | `2000年后各省数据_填充NA.xlsx`, first column |
| Physical Excel row | 2 | 11 | header is row 1 |
| Zero-based data index | 0 | 9 | calendar series 2000--2023 |
| One-based MATLAB data row | 1 | 10 | numeric arrays returned by `xlsread` |
| `main.m` loop `i` / callee `ii` | 1 | no single consistent value | `main.m:8,90-93` |
| Filename calendar formula | `1+2008 = 2009` | `ii=1` is required | `multi_prov_HANK_12sts.m:118-119` |
| Calibration cell | `data_MAT{1}` | unresolved calibration-vintage choice | `multi_prov_HANK_12sts.m:128,133` |
| Downstream `data_year` | 1 (reads 2000) | 10 (reads 2009) | `multi_prov_HANK_12sts.m:133`; `mpHANK_equilibrium_2000.m:27-43` |
| If `ii=10` is used | filename 2018, `data_MAT{10}`, row 2009 | row is correct but label/calibration identity is not 2009 | same lines |

There is no source offset or subset operation between `load_GDPdata` and `mpHANK_equilibrium_2000` that changes the 24-row 2000--2023 arrays into a 2009-based axis. The comment `maxyear=15; % 2009-2023` and filename formula do not transform the workbook arrays. Thus no current source value of `ii` simultaneously gives output/calendar label 2009 and workbook calendar row 2009.

The calibration object also has an independent vintage convention: for `reg_method=0`, `data_MAT{ii}` is constructed from regression coefficient/intercept sheets suffixed `ii+9` (`load_GDPdata.m:112-124`), while `IND_Zt` always uses array row 21, calendar 2020 (`load_GDPdata.m:129-137`). Consequently the source-labelled 2009 call mixes output label 2009, economic row 2000, regression suffix 10, and Zt base year 2020.

## 4. Province axis

`GDP!C1:AG1` supplies 31 provinces in this order:

北京市, 天津市, 河北省, 山西省, 内蒙古, 辽宁省, 吉林省, 黑龙江, 上海市, 江苏省, 浙江省, 安徽省, 福建省, 江西省, 山东省, 河南省, 湖北省, 湖南省, 广东省, 广西, 海南省, 重庆市, 四川省, 贵州省, 云南省, 西藏, 陕西省, 甘肃省, 青海省, 宁夏, 新疆.

This is substantively the accepted 31-province contract order; workbook labels retain their original 市/省 suffixes. The source consumes columns 3--33 of the workbook header and numeric province columns 2--32 after `xlsread` removes the text year column (`load_GDPdata.m:74,93-104`).

## 5. Source and data identities

### Protected MATLAB sources

| File | SHA-256 |
|---|---|
| `main.m` | `5C49CEAEDA9B43ED615E5DD376498D45F0E01D9A2F469C0FBB617C02110D5E12` |
| `multi_prov_HANK_12sts.m` | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` |
| `mpHANK_equilibrium_2000.m` | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` |
| `load_GDPdata.m` | `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5` |
| `load_distdata.m` | `18F594DD7D1ED090CA2AF576DEBCD8DCAA73C012608A8921F8D5BD6CC24F478B` |
| `It_to_Kt.m` | `4A407DE29F2DCD370932DAE35436A1B9D3C0432A360D94ABC0F78E1F94FEBE50` |

### Primary candidates and derived cache

| File | Role | Bytes | SHA-256 |
|---|---|---:|---|
| `2000年后各省数据_填充NA.xlsx` | current filled primary workbook input | 171292 | `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929` |
| `2000年后各省数据.xlsx` | raw primary workbook used only if filled workbook is absent | 119265 | `09814A45D933B2685A35238A15C0C7BB501F00A63597796B3CADCE15C230ECB3` |
| `R语言估计结果_plm估计.xlsx` | primary regression-result input | 361927 | `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68` |
| `中国各省省会地理距离矩阵.xlsx` | primary migration-distance input, not needed to resolve the year axis | 39895 | `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566` |
| `数据估计结果_1000_100_0.mat` | derived compatibility cache, non-primary | 2421344 | `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A` |

No `Multi_Province_12sts_<year>.mat` steady-state file was found. Old image filenames containing 2009 were not treated as calibration or year-mapping authority.

## 6. Primary calibration transformation chain

The designated call is `load_GDPdata(1000, 100, 0.096, 0, 0)`.

1. `writefile` is `2000年后各省数据_填充NA.xlsx` (`load_GDPdata.m:5`). Because it exists, the raw-data generation branch at lines 7--69 is skipped in the present runtime route.
2. The filled workbook supplies GDP, total capital stock, resident population, and the sector capital/employment/GDP-share sheets (`load_GDPdata.m:74-90`).
3. For total economy / industry index 4, `GDP = GDP[:, provinces] * 1000`, `CAP = 总资本存量[:, provinces] * 1000`, and `POP = 常住人口[:, provinces] * 100` (`load_GDPdata.m:93-104`). Each is a binary64 24-by-31 year-by-province array.
4. `log_pgdp = log(GDP/POP)` and `log_pcap = log(CAP/POP)` (`load_GDPdata.m:126-127`).
5. If the cache did not exist, `reg_method=0` would read `总面板回归系数_<ii+9>_行业<j>` and `总面板回归截距_<ii+9>_行业<j>`. The last numeric coefficient is `IND_alpha`; the second-last is the recorded `time20`. For `data_MAT{1}`, industry 4, these are respectively `0.539451671764441` and `0.492083661228024`.
6. For every regression vintage, `IND_Zt` is computed from calendar-2020 row 21 as `GDP * CAP^(-alpha) * POP^(alpha-1)` (`load_GDPdata.m:129-137`). It is therefore transformed/estimated, shape 1-by-31, and not annual-row-specific.
7. `prvname` is primitive workbook header text. `GDP_multiplier`, `POP_multiplier`, and `delta` are call parameters. `GDP`, `CAP`, `POP`, logs, `IND_alpha`, and `IND_Zt` are transformed fields; the MAT object is cached.
8. If the filled workbook were absent, the historical construction would read `B2:AG25` from the raw workbook, apply MATLAB `fillmissing(...,'makima')`, and derive capital with `K(1)=I(1)/0.1`, then `K(t)=(1-delta)K(t-1)+I(t-1)` (`load_GDPdata.m:7-69`; `It_to_Kt.m:1-10`). This branch was audited but not run.

The present MATLAB runtime does not reconstruct the regression fields from primary workbooks: because `数据估计结果_1000_100_0.mat` exists, `load_GDPdata.m:107-110` loads `mydata2` directly. This runtime shortcut is exactly why the Owner's non-primary-cache decision matters; compatibility cannot confer primary authority.

Fields consumed before model iteration by `mpHANK_equilibrium_2000.m:23-43` are `IND_Zt`, `IND_alpha`, `CAP`, `POP`, `GDP`, `log_pcap`, `log_pgdp`, and `prvname`. `Zt` additionally receives `param.Ztratio`; `GovInv` is `Kt0 * param.GovInv_ratio`. The migration distance matrix is loaded at line 17, but no solver or distance transformation was executed here.

## 7. Derived MAT cache compatibility audit

The cache is MATLAB v7.3/HDF5. Its top-level `mydata2` is a 15-by-1 cell object with fields `CAP`, `GDP`, `GDP_multiplier`, `IND_Zt`, `IND_alpha`, `POP`, `POP_multiplier`, `delta`, `log_pcap`, `log_pgdp`, and `prvname`. GDP/CAP/POP/log arrays logically have shape 24-by-31; alpha and Zt logically have shape 1-by-31.

Read-only comparison for `mydata2{1}`, industry 4:

| Field | Primary-source comparison |
|---|---|
| GDP | exact match to filled workbook times 1000 |
| CAP | exact match to filled workbook times 1000 |
| POP | exact match to filled workbook times 100 |
| `IND_alpha` | exact match to regression coefficient `0.539451671764441` |
| `IND_Zt` | maximum absolute difference `6.938893903907228e-18`; passes `rtol=atol=1e-12` |

The Zt difference is consistent with binary operation ordering and is non-material for this compatibility check. Classification: compatible derived representation for the inspected fields, but non-primary and incapable of resolving which combination of output year, annual data row, and calibration vintage the Owner intends.

## 8. Annual implementation and canonical artifact

- `src/ch5_two_asset_hank/multi_province/annual.py`: **not created**.
- Canonical 2009 pre-model input artifact: **not created**.
- Canonical artifact SHA-256: `NOT_CREATED_YEAR_MAPPING_SOURCE_CONFLICT`.
- Raw/private workbook content committed: none.
- Accepted MP1--MP3 production source modified: none.

Creating an annual API or serializing values would require guessing whether “2009” controls the output label, the workbook row, the regression-sheet vintage, or some decoupled combination. That is prohibited by sections 5 and 8 of the live task.

## 9. MP4B contract status and proposed post-adjudication contract

MP4B is **not executable and not frozen as accepted**. After Owner/L3 adjudication, a successor may freeze a contract that explicitly and separately persists:

1. calendar/output year, workbook row, calibration-cell/sheet vintage, province order, all source hashes, and the role of the fixed-2020 Zt construction;
2. initialization of Zt, GovInv, household prices/returns, and controller state;
3. province household Ct, Lt, At, Bt, AtTax, convergence statistic, and diagnostics;
4. migration `Lt_mat` and `Lt_supply`;
5. productive-capital contributions, `Kt_supply`, and `rah`;
6. firm `Yt`, `Kt`, `Lt`, `wjt`, `rk`, `ra`, `Govinc`, and source intermediates;
7. composite wage, Taylor `rb`, and national `GovSurplus`;
8. every manual-update iteration's gaps, boundary counts, adaptive action, `tKNratio`, iteration number, and termination;
9. final 31-province stationary objects and national aggregates.

The proposed first comparison budget remains one controlled MATLAB stationary run and one Python stationary run on manifests proven identical before either solve, with no shocks, transitions, IRFs, Results, or 2010--2023 batch. This is a proposal only, not execution authority. Exact/source-local equality, pre-frozen binary64/solver-propagated diagnostics, material mismatch, and qualitative diagnostics must remain separate. A mismatch may only be localized to the first divergent stage and classified as `PYTHON_IMPLEMENTATION_ERROR`, `MATLAB_SOURCE_OR_LEGACY_NUMERICAL_BEHAVIOR`, `DATA_OR_CALIBRATION_PROVENANCE_MISMATCH`, `SHARED_SOURCE_NUMERICAL_PROPAGATION_DIFFERENCE`, or `SCIENTIFIC_SPECIFICATION_OR_PROVENANCE_AMBIGUITY`; no automatic repair, tolerance relaxation, or rerun follows.

## 10. Scientific/model call ledger

| Operation | Calls |
|---|---:|
| MATLAB model/solver | 0 |
| modular HJB / KFE | 0 / 0 |
| standalone HA/HJB/KFE/aggregate | 0 |
| MP2 one-turn scientific execution | 0 |
| MP3 fixed point | 0 |
| legacy one-asset R5 | 0 |
| empirical GE / annual 31-province model | 0 |
| shocks / AR1 / transition / dynamics / IRF | 0 |
| Results | 0 |

Only static source reads, workbook/XML reads, HDF5 cache reads, hashing, schema inspection, and read-only arithmetic compatibility checks were performed.

## 11. Tests and static checks

- Live-authority equality and required ancestry: PASS.
- Clean-start and accepted-source immutability: PASS.
- Workbook year-cell/header inspection: PASS; 2009 maps to physical row 11 / zero-based data index 9 / MATLAB row 10.
- Province order/count inspection: PASS; 31 columns.
- Source-line mapping audit: PASS as evidence; terminal result is conflict.
- Read-only cache schema and primary-field compatibility comparison: PASS for inspected fields.
- Search for pre-existing annual MAT artifacts: none found.
- Scientific/model calls: exactly zero.
- Repository diff and whitespace checks are recorded at closeout.

The malformed drawing relationship in the regression workbook prevented a high-level workbook library from opening it as a complete presentation package. Read-only XLSX XML inspection recovered the numeric sheet evidence without modifying or repairing the workbook. This is a tooling/presentation defect, not a license to change the primary evidence.

## 12. Unresolved provenance requiring Owner/L3 adjudication

1. Decouple and specify the canonical calendar/output year (2009) independently of the current `ii+2008` filename convention.
2. Specify the canonical workbook `data_year` (source evidence says 10 for calendar 2009).
3. Specify which `data_MAT` cell / regression suffix is the calibration object for calendar 2009, rather than inheriting the same `ii` by assumption.
4. Confirm whether every annual calibration intentionally uses Zt constructed from calendar 2020, or provide the source-faithful alternative.
5. State how the corrected/decoupled route should be represented without modifying protected MATLAB source, or explicitly authorize a controlled adapter contract.

## 13. Forbidden-operation check and repository scope

- MATLAB, HJB, KFE, household solver, MP2 empirical one-turn, MP3 fixed point, empirical GE, annual 31-province execution, legacy R5, shocks, transition, dynamics, IRF, and Results: not run.
- Protected MATLAB, source workbooks, MAT cache, legacy R5, accepted household/oracle, MP1 contracts, MP2 arithmetic, and MP3 controller: not modified.
- `annual.py`, validators/tests, canonical data artifact, raw data, and model outputs: not created.
- CURRENT roadmap: not updated, because the task authorizes that PASS-route update and this invocation did not resolve the prerequisite mapping.
- Repository write scope: this report only.

## 14. Recommended next gate

Exactly one next gate is recommended: **Owner/L3 year-and-calibration identity adjudication**, explicitly decoupling (a) calendar/output year, (b) workbook `data_year`, (c) `data_MAT`/regression vintage, and (d) the fixed-2020 Zt role, followed by a new live GitHub task for annual-input binding.

MP4B, the 2010--2023 batch, and shocks are not authorized next while this mapping conflict remains unresolved.
