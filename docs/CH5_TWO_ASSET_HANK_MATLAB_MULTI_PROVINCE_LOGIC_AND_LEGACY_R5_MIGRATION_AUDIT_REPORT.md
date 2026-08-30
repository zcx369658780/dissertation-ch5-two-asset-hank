# Chapter 5 MATLAB multi-province logic and legacy R5 migration audit

## Terminal classification

`MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_ROADMAP_PASS`

This is a static source/migration audit. It accepts no GE, dynamic, calibration, transition, IRF, or Results object. Known Owner-provenance issues are carried to their earliest blocking stages without guessing.

## Live authority and call ledger

- Current repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Live task/start: `40274572ab46200cfd185e823c28fb4553b53284`, direct parent `14d474590df3575bd463ae69da8e481b4b2f27ea`.
- Historical R5 publication-time and fresh-fetched live `origin/main`: `9e73f7189865958fbe38a3cad4547b06b3d17aa3`.
- The historical checkout had a pre-existing untracked `AGENTS.md`; it was preserved. All R5 reads used `origin/main:<path>`.
- Primary numerical authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Accepted oracle: `exports/matlab_faithful_two_asset_ha.py`, SHA-256 `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.
- Designated MATLAB household source: `HANK_2ASSETS_HJB.m`, SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.

| Scientific/model action | Calls |
|---|---:|
| MATLAB | 0 |
| current modular Python HA | 0 |
| standalone oracle | 0 |
| legacy steady state / transition | 0 / 0 |
| AR1/model response | 0 |
| GE / dynamics / IRF | 0 / 0 / 0 |

## MATLAB source inventory

Protected root: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK` (read-only). The following files form the model route; remaining `.m` files are plotting, inequality summaries, data statistics, or isolated helpers and were searched but do not add a different solver route.

| File | SHA-256 | Signature/class | Source role and key lines |
|---|---|---|---|
| `main.m` | `5C49CEAEDA9B43ED615E5DD376498D45F0E01D9A2F469C0FBB617C02110D5E12` | script | annual steady states 84-94; shock/IRF caller 209-218; persistence/plots 151-183 and later |
| `multi_prov_HANK_12sts.m` | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` | `st=multi_prov_HANK_12sts(ii,pp)` | calibration/grid 13-114; year/cache/data route 118-135 |
| `mpHANK_equilibrium_2000.m` | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` | equilibrium function | data initialization 17-51; steady-state call 57-79; `st` persistence 80-95 |
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` | update-map iterator | manual loop/convergence 7-45; Zt/GovInv updates and damping 47-62; failure 64-66 |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` | one-turn function | household calls 4-16; labor/capital/returns 21-41; firm/wage/Taylor/fiscal 44-65 |
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | household function | prices/states 26-36; stationary HJB 240-260; stationary KFE 333-369; outputs 397-418 |
| `Lt_seperate.m` | `D30519AD81837E8EB5EBFE74BF25CC770E40B5C5AE5A254951AD97D436CACE26` | labor allocator | origin/destination migration matrix 3-16 |
| `HANK_firm.m` | `EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5` | firm function | inputs 9-24; production/prices 29-75; outputs 80-98 |
| `wage_caculate.m` | `0FB84B51E2BE50CD3D065D33385882311A31E12596AEEB0CE2C808A8C36B6A63` | wage aggregator | migration-weighted household wage 3-17 |
| `load_distdata.m` | `18F594DD7D1ED090CA2AF576DEBCD8DCAA73C012608A8921F8D5BD6CC24F478B` | data loader | distance/migration-cost input 1-8 |
| `load_GDPdata.m` | `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5` | data/calibration loader | workbooks/transforms 5-104; cache/R route 106-139; save 239-246 |
| `multi_prov_HANK.m` | `587FBA4ABA2DE88E2FD9B172379CEFA3E4AA144A32C8AD7FB26156618517E929` | shock wrapper | loads annual `st`, calls shock path, saves IRF 18-43 |
| `mpHANK_shock_2000.m` | `5909A972854B56E3E86F8EDA127A2A8AEAED236BFE1E7AA8C04A26DB750E9173` | forward shock loop | time loop 30-67; stationary one-turn call each date 46 |

Other searched helpers include `adjust_weight_matrix`, `init_weight_matrix`, `It_to_Kt`, `lab_solve2`, `HANK3_FOC`, `HANK3_cost`, `HANK_gini`, quantile/Gini and plotting functions. No alternative backward-HJB/forward-KFE transition solver was found.

## Source-backed call graphs

### Annual data/cache and stationary persistence

`main.m -> multi_prov_HANK_12sts(ii,0) -> [load Multi_Province_12sts_<year>.mat OR load_GDPdata] -> mpHANK_equilibrium_2000(data_MAT{ii}) -> load_distdata -> HANK_mp_1eq -> save st(results,grids,data_MAT,param,num,CHI) -> save annual cache -> main Excel/plot diagnostics`.

### One manual fixed-point turn

`HANK_mp_1eq -> HANK_mp_1turn -> 31 x HANK_2ASSETS_HJB -> Lt_seperate -> At*N capital allocation and rah -> HANK_firm -> wage_caculate -> Taylor rb and GovSurplus -> convergence tests -> optional Zt/GovInv/tKNratio updates`.

All 31 household calls consume the copied old-turn `results_temp`; no province observes a partially updated household state from an earlier province in the same turn. Cross-province allocations and firm/wage objects are then derived from the complete new household-output set.

### Named shock/IRF route

`main.m:209-218 -> multi_prov_HANK -> mpHANK_shock_2000 -> for t=1:T: reset shock levels from frozen st -> HANK_mp_1turn(steady_state=1) -> persist results -> carry results to t+1`.

This is a sequential comparative-statics path: each date solves a stationary HJB and `A' g=0` stationary density. It has no terminal condition, backward time-dependent HJB, forward time-dependent KFE, time-indexed distribution law, or transition convergence. Classification: `CONFIRMED_MULTI_PROVINCE_TWO_ASSET`, `AMBIGUOUS_CH5_PROVENANCE`, `NO_SOURCE_BACKED_GENUINE_DYNAMIC_ROUTE_FOUND`.

## State, flow, and orientation contracts

| Object | Exact source role / orientation |
|---|---|
| `N(i)` | province population; province order is workbook columns C:AG: 北京, 天津, 河北, 山西, 内蒙古, 辽宁, 吉林, 黑龙江, 上海, 江苏, 浙江, 安徽, 福建, 江西, 山东, 河南, 湖北, 湖南, 广东, 广西, 海南, 重庆, 四川, 贵州, 云南, 西藏, 陕西, 甘肃, 青海, 宁夏, 新疆 |
| `Ct,Lt,At,Bt,AtTax` | household aggregates from two-asset solver; household `Lt` is not final firm labor |
| `Lt_mat(j,i)` | labor from origin `i` assigned to destination `j`; columns origin, rows destination |
| `Lt_supply(j)` | row sum `sum_i Lt_mat(j,i)`, destination labor supplied to firm `j` |
| productive private capital | uses illiquid `At(i)*N(i)` only; `Bt` and `At+Bt` are excluded |
| `Kt_supply(j)` | destination/issuer capital supply from source-defined cross-province weights; `Kt=Kt_supply+GovInv` |
| `ra(j)` | firm/issuer illiquid return, clipped `[0.02,0.09]` |
| `rah(i)` | household illiquid portfolio return derived from all province `ra`; not a root residual |
| `rb` | Taylor-derived liquid return `it-totalpit`, with borrowing return shifted by `rb_gap` |
| `wjt(j)` | firm wage, clipped `[0.8,1.3]` |
| `w(i)` | migration-weighted household wage from `wage_caculate` |
| `Zt,Yt` | firm productivity and output; `Zt` is heuristically reset if output gap exceeds 1% |
| `KNratio,tKNratio` | current K/L and damped convergence reference; damping `0.6*new+0.4*old` |
| fiscal | `Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt`; national `GovSurplus` also subtracts `Bt*rb*N`; diagnostic, not balanced closure |

`inter_prv_ratio` and the distance/migration matrices are source-specific allocation objects. They are not equivalent to legacy R5's holder-row/issuer-column `W` absent an explicit proof.

The source stores the complete `Lt_mat` only into `results{31}` because the loop index remains 31 after allocation; the persistence callers explicitly retrieve `results{31}.Lt_mat`. This is a literal storage convention to preserve and test, not evidence that province 31 owns the matrix scientifically.

## Manual iteration contract

- Initialization is year-specific in `mpHANK_equilibrium_2000`, with household prices/returns and data-derived province states.
- Each turn uses 31 old-state household calls, then migration/labor, `At*N` capital, `rah`, firm, wage, Taylor `rb`, and fiscal diagnostics in that order.
- Maximum outer iterations: 500. Household controls in production source include maximum 100 iterations, criterion `1e-7`, pseudo-time step 1000.
- Acceptance requires max `abs(KNratio/tKNratio-1)<1e-9`, max `abs(Yt/Yt_1-1)<1e-9`, all 31 household convergence flags, and no `ra` at either clip. Wage-bound counts are diagnostic but not in the final acceptance predicate.
- `Zt` is directly recomputed when `|Yt/Yt0-1|>0.01`; `GovInv` is multiplied by `0.9` or `1.1` near return bounds; `tKNratio` alone is damped.
- Iteration exhaustion raises the source failure `稳态没能成功收敛！`.
- This is an ordered update map. It must not be silently replaced with Brent, Newton, `fsolve`, or another root solver.

## Data/cache provenance

| Input | SHA-256 / role | Classification |
|---|---|---|
| `中国各省省会地理距离矩阵.xlsx` | `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566`; distances/migration costs | `SOURCE_IDENTIFIED_EXTERNAL_DATA_PENDING_CAPTURE` |
| `2000年后各省数据_填充NA.xlsx` | `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929`; GDP/capital/population/industry | `SOURCE_IDENTIFIED_EXTERNAL_DATA_PENDING_CAPTURE` |
| `2000年后各省数据.xlsx` | `09814A45D933B2685A35238A15C0C7BB501F00A63597796B3CADCE15C230ECB3`; raw fallback | `SOURCE_IDENTIFIED_EXTERNAL_DATA_PENDING_CAPTURE` |
| `R语言估计结果_plm估计.xlsx` | `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68`; regression estimates | `SOURCE_IDENTIFIED_EXTERNAL_DATA_PENDING_CAPTURE` |
| `数据估计结果_1000_100_0.mat` | `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`; cached `mydata2` | `CACHE_DERIVED_NOT_PRIMARY_AUTHORITY`; acceptance requires Owner |
| `Multi_Province_12sts_<year>.mat` | derived annual `st`; none present in audited tree | `CACHE_DERIVED_NOT_PRIMARY_AUTHORITY` |

The source names cache year as `ii+2008` while `data_year=ii` indexes a dataset beginning in 2000. For `ii=1`, the filename says 2009 while the first data row may represent 2000. Source alone does not prove the intended mapping; baseline/multi-year semantics remain Owner-controlled.

## Dynamic/shock conclusion

`main.m` sets `T=20` and a deterministic decay `0.01*exp(-0.5*(t-1))`, then injects productivity, government-investment, tax, or monetary level shocks. No explicit AR(1) equation, innovation process, expectation law, response normalization contract, dynamic NK system, terminal condition, backward HJB, forward KFE, or transition convergence was found. The firm has an NKPC-like contemporaneous algebraic expression, not a complete dynamic NK route. The folder name mentions neural networks, but no `trainNetwork`, `fitnet`, `dlnetwork`, or neural-network implementation was found.

## Legacy R5 migration matrix

The old README/status/contracts explicitly define a synthetic two-region, 40-point, one-liquid-asset model. `docs/R5_1_MIGRATION_TRACEABILITY.csv` marks every old block `old_output_authority=FALSE`.

| File/family | Old role | Disposition | New authority / target | Validation gate | Risk |
|---|---|---|---|---|---|
| `household_hjb.py` | one-asset stationary/backward HJB | `REPLACE` | accepted two-asset oracle adapter | exact tiny-fixture values/policies/operators/labels | fatal boundary/order contamination |
| `distribution_kfe.py` | one-asset stationary/implicit KFE | `REPLACE` | accepted two-asset operator/KFE | sparse orientation, density, mass, aggregates | fatal flattening/orientation risk |
| `grids.py` | uniform 1D liquid grid | `ADAPT` validators; replace economics | source `(a,b,z)` contract | exact shape/order fixture | high |
| `parameters.py` | hard-frozen synthetic fixture | `REPLACE` economics; adapt parser/hash pattern | provenance/data/province contracts | schema/hash/Owner gates | high silent calibration |
| `steady_state.py` | symmetric scalar Brent, `W.T@assets` capital | `REPLACE` | MATLAB 31-province manual update map using `At` | one-turn then convergence parity | fatal |
| `regional_structure.py` | generic Cobb-Douglas shell | `ADAPT` | MATLAB firm with `Kt_supply+GovInv`, `Lt_supply` | province factor-price fixture | high semantic mismatch |
| `spatial_links.py` | synthetic `W` portfolio/capital | `REPLACE` | MATLAB migration/capital orientation | asymmetric hand fixture | fatal W inheritance |
| `aggregate_block.py` | balanced fiscal, goods/NFI/CA, nominal identities | `REPLACE` science; adapt containers only | MATLAB rah/wage/Taylor/fiscal diagnostic | equation-by-equation fixture | fatal closure laundering |
| `shocks.py` | generic quarterly AR(1) engine | `DEFER` | source/dissertation shock law first | frequency/law/loading parity | high |
| `transition.py` | disposable one-asset real-block transition | `DEFER`, likely `REPLACE` | future source-validated two-asset dynamic contract | timing/accounting/terminal parity | fatal |
| `diagnostics.py` | manifests and old-science metrics | `ADAPT` | new provenance plus source-specific diagnostics | serialization/hash/schema checks | medium |
| `io_contracts.py` | no-overwrite path discipline | `KEEP` after path review | successor evidence IO | collision/boundary tests | low |
| configs | old 2-region/AR1/transition fixtures | SS configs `REPLACE`; AR1/transition `DEFER` | source-derived contracts | schema/provenance gates | high |
| experiment runners | old SS/AR1/transition entry points | SS/transition `REPLACE`; AR1 `DEFER` | staged successor runners | task-budget and no-overwrite gates | high |
| tests | old scientific assertions plus utility checks | generic IO/import/hash `KEEP`; schema `ADAPT`; science `REPLACE`; AR1/transition `DEFER` | stage-specific fixture suites | false acceptance | high |
| docs/contracts | historical active contracts | `DEFER` as evidence | CURRENT roadmap | supersession check | medium |
| CI/package/lint/type shell | engineering scaffold | `KEEP/ADAPT` | chosen repository package | clean static checks | low |

Non-negotiable: old HJB/KFE cannot gain authority by adding a dimension; productive capital is `At`, never `At+Bt`; `Bt` is liquid; firm labor is migration-derived `Lt_supply`; old symmetric Brent, balanced budget, goods, NFI/CA, generic `W`, AR1, and transition timing have no MATLAB authority unless independently proven.

## Repository strategy

| Strategy | Governance/traceability | Cost/reuse | contamination risk | Disposition |
|---|---|---|---|---|
| A extend R5 | poor: stale one-asset contracts surround new work | superficially lowest | highest | reject |
| B extend current two-asset repo | best oracle lineage and task governance | moderate; migrate bounded engineering shells | lowest | **recommend** |
| C new successor repo | clean separation | highest bootstrap/provenance overhead | low after careful binding | Owner alternative only |

Recommendation: B. A dedicated C is warranted only if Owner requires organizational isolation; no repository was created.

## Owner provenance and earliest blockers

| Unresolved decision | Earliest blocking stage |
|---|---|
| exact `ii`/calendar-year and baseline vs multi-year contract | MP4 full annual acceptance; fixture row identity must be explicit at MP1 |
| authority of `数据估计结果_1000_100_0.mat` | MP4; capture lineage at MP1 |
| dissertation Chapter 5 primary path | MP5 shock-law adjudication and any equation-level publication claim |
| vectorized update-map ordering | only if MP3 exposes a vector API; source ordered object map remains usable |
| named shock/IRF route interpretation | MP5/MP6 |
| repository strategy | resolved to B by audit unless Owner overrides before MP1 |

These do not block completion of MP0.

## Reuse/redo estimate

Source evidence supports ranges, not point precision: roughly 20-30% of engineering mechanisms (IO/no-overwrite, hashing, manifests, CI/type/lint/test patterns) can be kept or adapted; roughly 70-80% of scientific implementation must be replaced or newly built. The latter includes two-asset integration, province contracts, migration/capital/wage/fiscal update map, annual orchestration, and any genuine dynamics.

## Outputs and next gate

- This report.
- CURRENT roadmap: `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`, SHA-256 `7995CE8814274158D3CE7F24EA84DD5FFD001BFD011B1B507E64A2D6B1655BD8`.
- Exactly one proposed successor is specified in the roadmap. It is design only and was neither created nor executed.

Authorized changed paths are exactly these two documentation files. This document records pre-closeout scope; final commit, push, read-back, `HEAD==origin/main`, and clean-worktree evidence is reported by the executor after the single commit.

## Appendix A — complete MATLAB `.m` inventory disposition

Core model files and hashes are in the main inventory. Every remaining `.m` file was statically classified below; `none in core graph` means no call from the steady-state or named shock chain was found.

| File | SHA-256 | Signature/call relation | Lines / classification |
|---|---|---|---|
| `main2.m` | `E4B8E5BF748FB38616E70B7B1F931B99E3B59468A7A27D3ABB00D0573B7F83FB` | script; alternate reporting caller | 1-290, output/diagnostic |
| `描述GDP数据统计特征.m` | `DCCB6E0FF3C8156C2CA2EB0C64B5B10BEF39C7E9634D8FEA286F5A6BD255C164` | script; none in core graph | 1-57, data diagnostic |
| `adjust_weight_matrix.m` | `E9742F8599DAB4E1EAA736DD3A352E4DB3E4B80A677F894547F69F7B64D5120C` | weight helper; not called by current route | 1-12, historical/ambiguous |
| `init_weight_matrix.m` | `4FAAF1208572E59E64EF8A831BDD3D4F07EBE02DE75E9569D0301FBB579530AA` | weight helper; not called, missing normalization dependency | 1-16, historical/ambiguous |
| `coefmat_save.m` | `2D6EB7E0585EE7322982CD7F5BBE4E133D93B97FE0A7D40EED7D1C18D930FB3D` | script; none in core graph | 1-29, persistence helper |
| `Ltmat_save.m` | `8D76192CBA2B5C11D4DBABA3E5E9AB61EEE298CBAA3D1AF863E10792D4D49491` | script; saves labor matrices | 1-13, persistence helper |
| `It_to_Kt.m` | `4A407DE29F2DCD370932DAE35436A1B9D3C0432A360D94ABC0F78E1F94FEBE50` | capital helper; none in current core graph | 1-11, historical/ambiguous |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | labor root helper called inside household path | 1-11, household dependency |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | FOC helper; household dependency | 1-22, household dependency |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | adjustment-cost helper; household dependency | 1-25, household dependency |
| `HANK_gini.m` | `CF8ABE1EC9495E5167CA1B5254BB6C36524CBC59F7E4FF6F196C9081317F706E` | distribution statistic | 1-21, diagnostics |
| `HANK_quantile5_multiprov.m` | `F4FFF22647A3ED7CBAB52EB71530FFC8D8ADC532FE929F6F11031507154F9F03` | quantile statistic | 1-21, diagnostics |
| `HANK_quantileg.m` | `D7E13A40FF57BFDF70BAC977C36ED573466AD06B36F41A5F86AA63A9DA6E5C6E` | quantile statistic | 1-35, diagnostics |
| `Gini_coef2.m` | `4DBF06B30713A1875199EE3422F1D27507440853B0837A15E292724077FA8A70` | generic Gini helper | 1-54, diagnostics |
| `Plot_multiprv_g.m` | `8F1489374930E3AF5F82EF35A4F70CE7F0C02CC36EB21196CED239D32E69C3E1` | plotting function | 1-36, output |
| `GetColors.m` | `DCE13B7BEDF6675DA8C3E60522789F8BD6E4CC3A97F1BEA5193A243C2762EB62` | color utility | 1-253, presentation |
| `Hex2RGB.m` | `9B107810D924FD4C471847BF4C153022C4BA7F05535BD900DA65F197BC622BE5` | color utility | 1-12, presentation |
| `RGB2MatlabColor.m` | `2861C4A806ABF3BFAE18FAF828E5FB954A822AF6888D943EF7631FBD948C3ED9` | color utility | 1-4, presentation |
| `max_abs_value.m` | `69690717049B62F8A0B9ABEB81E73234AD1FD8DAC7409E41995D90BCEB4E01EE` | numeric diagnostic helper | 1-16, diagnostics |

The 32-file count is the 13 core entries plus these 19 entries. No additional `.m` route is omitted.

## Appendix B — `data_MAT` and persistence object map

`load_GDPdata(GDP_multiplier,POP_multiplier,alpha_reg,fillNA_method,reg_method)` reads GDP, capital, population and industry sheets, applies the declared multipliers/fill route, reads or constructs regression objects, and returns `mydata2/data_MAT`. Its year-indexed cells supply `IND_Zt`, `IND_alpha`, `GDP`, `CAP`, `POP` and associated regression/calibration fields consumed by `mpHANK_equilibrium_2000`. `load_distdata(max_sigmau)` reads the 31x31 capital-city distance workbook and returns a scaled migration-cost matrix. The source has no manifest binding these values to a commit or year convention.

Persistence is complete as: calibration cache `数据估计结果_1000_100_0.mat:mydata2`; annual steady state `Multi_Province_12sts_<ii+2008>.mat:st` (`-v7.3`); `st={results,grids,sigmau_MAT,N_prov,data_MAT,param,num,CHI}`; summary workbooks `12年稳态值.xlsx` and `12年稳态Ltmat.xlsx`; named response cache `多省份IRF_<year>_<shockname>.mat`. Existing workbook/IRF outputs are derived evidence with no verified source manifest.

## Appendix C — legacy R5 per-file primary disposition

For compactness, common new authority is the accepted oracle plus MATLAB MP0 contracts; common target is the new `multi_province` namespace; every row nevertheless has one primary disposition.

| File | Old role | Primary | Proposed target / gate / risk |
|---|---|---|---|
| `AGENTS.md` | repo governance | `ADAPT` | current governance; live-task review; medium |
| `README.md` | old scope | `DEFER` | historical references; supersession scan; low |
| `docs/ARCHITECTURE.md` | old architecture | `DEFER` | historical references; no active imports; medium |
| `docs/IMPLEMENTATION_STATUS.md` | old status | `DEFER` | historical references; CURRENT precedence; medium |
| `docs/STEADY_STATE_EQUATION_CONTRACT.md` | synthetic equations | `REPLACE` | MP contracts; source-line audit; high |
| `docs/STEADY_STATE_DIAGNOSTIC_CONTRACT.md` | old diagnostics | `ADAPT` | new diagnostics contract; schema review; medium |
| `docs/AR1_ENGINE_CONTRACT.md` | old AR1 law | `DEFER` | MP5; source-law gate; high |
| `docs/TRANSITION_SOLVER_CONTRACT.md` | old transition law | `DEFER` | MP6; dynamic authority gate; fatal |
| `docs/CONFIGURATION_CONTRACT.md` | old fixture contract | `REPLACE` | MP1 contracts; no-default test; high |
| `docs/IO_AND_PROVENANCE_CONTRACT.md` | evidence IO | `ADAPT` | new IO contract; collision/hash gate; low |
| `docs/R5_1_MIGRATION_TRACEABILITY.csv` | history map | `DEFER` | reference manifest; authority-false check; low |
| `configs/scaffold_example.toml` | synthetic scaffold | `REPLACE` | MP1 synthetic fixture; schema gate; medium |
| `configs/steady_state_small_grid.toml` | one-asset SS | `REPLACE` | MP contracts; no stale fields; fatal |
| `configs/ar1_engine_baseline.toml` | AR1 config | `DEFER` | MP5; source-law gate; high |
| `configs/transition_small_grid_conditional.toml` | old transition | `DEFER` | MP6; timing/terminal gate; fatal |
| `experiments/README.md` | old runner guide | `DEFER` | historical references; low |
| `experiments/run_small_grid_steady_state.py` | Brent runner | `REPLACE` | future MP runner; task-budget gate; fatal |
| `experiments/run_ar1_engine_diagnostic.py` | AR1 runner | `DEFER` | MP5; law/provenance gate; high |
| `experiments/run_small_transition_diagnostic.py` | old transition runner | `DEFER` | MP6+; dynamic authority gate; fatal |
| `tests/test_aggregate_and_fiscal_block.py` | old fiscal/accounts | `REPLACE` | MP2 fiscal diagnostics; source fixture; high |
| `tests/test_ar1_and_transition_remain_not_started.py` | old status guard | `DEFER` | historical status; supersession check; low |
| `tests/test_ar1_engine.py` | old AR1 | `DEFER` | MP5; source-law gate; high |
| `tests/test_configuration_contract.py` | old config | `ADAPT` | MP1 schema tests; no defaults; medium |
| `tests/test_contracts.py` | generic contracts | `ADAPT` | MP1 invariants; source fixture; medium |
| `tests/test_distribution_kfe.py` | one-asset KFE | `REPLACE` | accepted two-asset KFE; exact operator gate; fatal |
| `tests/test_grids.py` | one-asset grid | `REPLACE` | `(a,b,z)` order tests; exact fixture; high |
| `tests/test_household_hjb.py` | one-asset HJB | `REPLACE` | oracle adapter tests; exact fixture; fatal |
| `tests/test_imports.py` | import smoke | `KEEP` | package smoke; static gate; low |
| `tests/test_io_no_overwrite_contract.py` | collision contract | `KEEP` | successor IO; path review; low |
| `tests/test_no_model_implementation.py` | historical negative guard | `DEFER` | old-stage evidence; low |
| `tests/test_spatial_contract.py` | synthetic W | `REPLACE` | asymmetric MATLAB orientation; hand fixture; fatal |
| `tests/test_steady_state_reproducibility.py` | old run identity | `ADAPT` | MP provenance; hash/no-overwrite; medium |
| `tests/test_steady_state_small_grid.py` | symmetric Brent SS | `REPLACE` | MP3 update map; source fixture; fatal |
| `tests/test_transition_configuration.py` | old transition config | `DEFER` | MP6; authority gate; high |
| `tests/test_transition_distribution_step.py` | one-asset forward step | `DEFER` | MP7; two-asset dynamic gate; fatal |
| `tests/test_transition_household_step.py` | one-asset backward step | `DEFER` | MP7; two-asset dynamic gate; fatal |
| `tests/test_transition_provenance_and_boundaries.py` | transition provenance | `ADAPT` | MP8/9 provenance shell; source timing gate; high |
| `tests/test_transition_runner_contract.py` | runner boundaries | `ADAPT` | future runner shell; budget/no-overwrite; medium |
| `tests/test_transition_solver_conditional.py` | old conditional response | `DEFER` | MP8/9; accepted transition required; fatal |
| `tests/test_transition_solver_zero_shock.py` | old zero-shock | `DEFER` | MP9; response definition gate; high |
| `tests/test_transition_terminal_diagnostics.py` | old terminal checks | `DEFER` | MP6/7; terminal authority gate; fatal |
| `tests/test_transition_timing_bridge_algebra.py` | old timing bridge | `DEFER` | MP6/8; source accounting gate; fatal |
| `src/chapter5_model/__init__.py` | package exports | `ADAPT` | new namespace exports; import gate; low |
