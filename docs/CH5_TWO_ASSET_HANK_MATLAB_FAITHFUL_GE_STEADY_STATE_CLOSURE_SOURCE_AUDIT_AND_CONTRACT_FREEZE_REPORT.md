# MATLAB-faithful GE steady-state closure source audit and contract freeze

## Terminal classification

`MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_OWNER_PROVENANCE_REQUIRED`

The designated MATLAB closure is auditable, but the source does not designate one unique Chapter 5 GE baseline year/trial point. `main.m` requests all fifteen annual closures for 2009–2023, and `multi_prov_HANK_12sts(ii,pp)` selects year-specific `data_MAT{ii}`. There is no explicit GE unknown vector, residual-map function, or root-solver input point. Choosing one year or converting the manual iteration state into a residual vector would be an Owner provenance/convention decision. Therefore the next residual-map parity contract cannot yet be frozen without guessing.

This is an audit-only result, not GE acceptance.

## Live authority and scope

- Fresh-fetched live start/final pre-publication authority: `cedff8f6b63dbc25f853de364f8db9f335c7280e`.
- Direct parent: accepted aggregate closeout `8cd3dc4eb6d0e3e6d5f5c8cb63036c1fd6042961`.
- Primary authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Protected root: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.
- Required `HANK_2ASSETS_HJB.m` SHA-256 verified: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.
- No MATLAB/Python source or test was modified.

## GE-relevant source inventory

| Relative path | SHA-256 | Signature/type | Relevant lines and role |
|---|---|---|---|
| `main.m` | `5C49CEAEDA9B43ED615E5DD376498D45F0E01D9A2F469C0FBB617C02110D5E12` | script | 84–94 invokes fifteen annual steady states; 151–183 persists Excel diagnostics |
| `multi_prov_HANK_12sts.m` | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` | `st = multi_prov_HANK_12sts(ii,pp)` | 13–114 numerical/grid/calibration initialization; 118–135 year/cache/data routing and persistence |
| `mpHANK_equilibrium_2000.m` | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` | `st = mpHANK_equilibrium_2000(param,grids,num,CHI,inits,data_MAT,st_ind,data_year)` | 17 distance data; 22–51 annual/province initialization; 57–79 outer call; 80–95 persisted steady-state struct |
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` | `[results,GDP_vec,finish] = HANK_mp_1eq(...)` | 7–45 manual convergence loop; 47–62 heuristic updates; 64–66 failure handling |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` | `[results,GDP_vec] = HANK_mp_1turn(...)` | 4–16 preferences and household call; 21–41 labor/capital/return propagation; 44–65 firm, wage, Taylor rule, fiscal diagnostic |
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | `results = HANK_2ASSETS_HJB(param,grid,num,CHIh,results,show_result)` | 26–36 price/state inputs; 333–369 KFE/aggregates; 397–418 household outputs |
| `HANK_firm.m` | `EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5` | `results = HANK_firm(param,grids,results,steadystate,show_result)` | 9–18 inputs; 29–75 production/prices/taxes; 80–98 outputs |
| `Lt_seperate.m` | `D30519AD81837E8EB5EBFE74BF25CC770E40B5C5AE5A254951AD97D436CACE26` | `Lt_mat = Lt_seperate(results,param,phi_mat,sigmau_MAT,N_prov)` | 3–16 province-to-province labor matrix |
| `wage_caculate.m` | `0FB84B51E2BE50CD3D065D33385882311A31E12596AEEB0CE2C808A8C36B6A63` | `wt_vec = wage_caculate(results,param,phi_l_mat,sigmau_MAT,N_prov)` | 3–17 household wage aggregator |
| `load_distdata.m` | `18F594DD7D1ED090CA2AF576DEBCD8DCAA73C012608A8921F8D5BD6CC24F478B` | `mydata = load_distdata(max_sigmau)` | 1–8 migration-cost data |
| `load_GDPdata.m` | `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5` | `mydata2 = load_GDPdata(...)` | 5–104 workbooks/transforms; 106–139 cached/R regression route; 239–246 persisted calibration cache |

No other `.m` file directly calls `HANK_2ASSETS_HJB`; the sole direct caller is `HANK_mp_1turn.m:15`.

## Exact call graph

`main.m:90–94`
→ `multi_prov_HANK_12sts(ii,0)`
→ either load `Multi_Province_12sts_<year>.mat:st` (`121–124`) or
→ `load_GDPdata(...)` (`128`)
→ `mpHANK_equilibrium_2000(...,data_MAT{ii},4,ii)` (`133`)
→ `load_distdata(max_sigmau)` (`17`)
→ `HANK_mp_1eq(...,steady_state=1)` (`72`)
→ up to `num.max3iter=500` calls of `HANK_mp_1turn` (`HANK_mp_1eq:7–8`)
→ 31 calls of `HANK_2ASSETS_HJB` (`HANK_mp_1turn:14–16`)
→ `Ct,Lt,At,Bt,AtTax` return
→ `Lt_seperate` produces `Lt_mat`; row sums produce destination `Lt_supply` (`23–26`)
→ cross-province `At*N` produces `Kt_supply`; province returns produce `rah` (`29–41`)
→ `HANK_firm` produces `Yt,Kt,Lt,ra,wjt,rk,Govinc` (`44–47`)
→ `wage_caculate` produces next household `w` (`49–53`)
→ Taylor formula produces next `rb`; `GovSurplus` is accumulated (`60–65`)
→ `HANK_mp_1eq` tests manual convergence and optionally updates `Zt/GovInv`
→ `mpHANK_equilibrium_2000` stores `st.results/grids/data_MAT/param/num/CHI`
→ `multi_prov_HANK_12sts` saves `Multi_Province_12sts_<year>.mat`.

There is no `fsolve`, `fzero`, or `lsqnonlin` GE call. The `fzero` inside `HANK_2ASSETS_HJB:106` is a household labor-FOC subsolve, not a GE root solver.

## Iterated/derived GE state table

The source has no joint root unknown vector. The following are sequential state objects per province (`i=1..31`), not a claimed residual-vector ordering.

| MATLAB object | Meaning/type | Initialization/source | Bounds/scaling | Household input? |
|---|---|---|---|---|
| `results{i}.Zt` | TFP; data primitive then heuristic update | `IND_Zt{4}(1,i)*Ztratio`, equilibrium lines 25–26; update `Yt0*Kt^(-alpha)*Lt^(alpha-1)` at `HANK_mp_1eq:49–51` | no explicit bound | no, firm input |
| `results{i}.GovInv` | government-owned/fixed capital component; iterated | `Kt0*GovInv_ratio`, lines 40; multiplied by `0.9/1.1` at `HANK_mp_1eq:52–56` | implicit through `ra` boundary trigger | no, firm capital input |
| `results{i}.w` | household wage; derived sequentially | init `20` (`multi...:93`); `wage_caculate` at `HANK_mp_1turn:50–53` | positivity check in wage helper | yes |
| `results{i}.rb` | liquid return; Taylor-derived sequentially | init `0.02`; `it-totalpit` at `HANK_mp_1turn:63–64` | none | yes |
| `results{i}.rah` | household illiquid return; derived cross-province | init `0.09`; formula at `HANK_mp_1turn:40` | none | yes |
| `results{i}.ra` | province firm illiquid return; derived | init `0.09`; firm lines 54–64 | clipped `[0.02,0.09]` | enters next `rah` |
| `results{i}.wjt` | province firm wage; derived | init `0.6`; firm lines 43,66–74 | clipped `[0.8,1.3]` | enters migration/wage aggregators |
| `results{i}.Kt` | firm capital, derived | data `Kt0`; then `Kt_supply+GovInv` | no direct scale | no |
| `results{i}.Lt` | firm labor, derived | data population; then `Lt_supply` | no direct bound | no; differs from household `Lt` after firm overwrite |
| `results{i}.Yt` | firm output, derived | data `Yt0`; Cobb–Douglas result | convergence ratio | feeds iteration |
| `results{i}.Tt` | transfer primitive | fixed init `0.1` | none | yes |
| `results{i}.tau` | labor-tax primitive | fixed init `0.05` | none | yes |
| `results{i}.rb_gap` | borrowing spread primitive | fixed init `0.07` | none | yes |
| `results{i}.pit,totalpit` | fixed initialized inflation objects in steady-state route | both `0.02` | none | indirect through `rb`/firm |

## Residual/equation and convergence table

| Source expression | Meaning/sign/scale | Inputs | Status/target |
|---|---|---|---|
| `NKrationgap(i)=abs(results{i}.KNratio/tKNratio(i)-1)` (`HANK_mp_1eq:31`) | absolute relative capital-labor fixed-point gap | firm `K/L`; smoothed prior ratio | root-like convergence diagnostic; max `<1e-9` |
| `Ytgap(i)=abs(results{i}.Yt/results{i}.Yt_1-1)` (`32`) | absolute relative output iteration gap | current/prior firm output | root-like convergence diagnostic; max `<1e-9` |
| `convergent_total=sum(results{i}.convergent)` (`33`) | household HJB convergence count | household flags | must equal `31` |
| `maxra==0 && minra==0` (`14–18,42`) | no province return at either clipping bound | `ra`, grid limits | mandatory convergence veto |
| `maxwjt/minwjt` (`19–23`) | wage-bound counts | `wjt`, grid limits | diagnostic only; not in line-42 acceptance |
| `Yt/Yt0-1` (`49`) | output/data discrepancy | firm output and observed GDP | if outside ±0.01, updates `Zt`; not final residual target |
| `ra` proximity to limits (`52–56`) | return-bound localization | firm `ra` | adjusts `GovInv` by ±10%; not a zero equation |
| `GovSurplus += Govinc-Bt*rb*N` (`HANK_mp_1turn:61–65`) | government surplus sign: income minus liquid-interest expense | `Govinc,Bt,rb,N` | diagnostic accumulator; not fed back or targeted to zero |

Convergence is joint across provinces but sequential/manual, not a simultaneous root solve. `tKNratio` is damped as `0.6*KNratio+0.4*tKNratio` (`60–62`). Failure at iteration 500 raises `"稳态没能成功收敛！"` (`64–66`). No warm-start value function is passed between household calls; each call constructs its own HJB initialization from current parameters.

## Firm, government, and market formulas

- Production: `Yt=Zt*Kt^alpha*Lt^(1-alpha)` (`HANK_firm:30`).
- Capital used by firms: `Kt=Kt_supply+GovInv` (`14`).
- Labor used by firms: `Lt=results.Lt_supply` (`9`), not household aggregate `results.Lt`; household `Lt` is overwritten at line 88.
- Marginal cost/NKPC steady-state update: exact expression at `HANK_firm:33–37`.
- Wage: `wt0=mt*(1-alpha)*Zt*(Kt/Lt)^alpha` (`43`), clipped at lines 66–74.
- Capital rental: `rk=mt*alpha/(Kt/Yt)` (`44–45`).
- Investment: `It=Kt-Kt_1+delta*Kt`, with `delta=0.025` (`47`; calibration line 69).
- Profit/dividend: `PIt=max((1-mt)*Yt-theta/2*pit^2*Yt,0)`; `divrate=PIt*(1-corptau)/Kt` (`46–54`).
- Firm asset return: `ra0=rk-delta+divrate`, clipped to `[ramin,ramax]` (`54–65`).
- Cross-province capital supply: `At*N` multiplied by `inter_prv_ratio`; destination supply excludes own contribution and divides by `N_prov-1` (`HANK_mp_1turn:29–37`).
- Household `rah`: `(1-inter_prv_ratio)*ra + inter_prv_ratio/(N_prov-1)*(tempra-inter_prv_ratio*ra)` exactly as line 40. This is a source-specific weighted return formula, not a market-clearing residual.
- Taylor block: `it=istar+rho_pi*totalpit+epsilon_pi`; `rb=it-totalpit` (`63–64`), with `istar=.015`, `rho_pi=1.25`.
- Province government income: `Corptax+Lt*tau+AtTax+GovInv*ra-Tt` (`HANK_firm:95`).
- National surplus diagnostic additionally subtracts `Bt*rb*N` (`HANK_mp_1turn:65`).
- No goods/resource constraint, consumption-resource equation, bond-supply target, numeraire equation, or government-budget zero condition exists in this route.

## Explicit closure answers

1. `rb` is endogenous only as a sequentially derived Taylor-rule value; it is not a root unknown. With fixed steady-state inflation inputs it is mechanically determined.
2. `rah` is endogenous/derived from province `ra` values and cross-province holding weights.
3. No residual equation closes `rah`; exact assignment is `HANK_mp_1turn:40`.
4. Household `w` is endogenous/derived by `wage_caculate`; firm `wjt` is marginal-product based and clipped.
5. Exact firm wage is `mt*(1-alpha)*Zt*(Kt/Lt)^alpha`; exact household wage aggregator is `wage_caculate:8–11`.
6. `Tt` is fixed at `0.1`; it is not budget-balanced/endogenous.
7. `tau` is fixed at `0.05`.
8. `rb_gap` is fixed at `0.07`.
9. Productive private capital uses `At*N` through the inter-province supply construction, plus `GovInv`; neither `Bt` nor `At+Bt` clears productive capital.
10. No liquid bond-supply/market-clearing target is specified. `Bt` only enters the surplus diagnostic as `Bt*rb*N`.
11. The firm uses migration-derived `Lt_supply`, not household `Lt` exactly.
12. `Ct` enters `Lt_seperate` and is reported as `Ct_total`; it does not enter a resource condition.
13. Government income/surplus is computed, but no budget/resource residual is targeted.
14. `AtTax` enters `Govinc`; it does not feed back into a closure equation. `AhTax` is computed by the household source and mapped to `AtTax`.

## Baseline grid/calibration and data provenance

The GE route requires the MATLAB production fixture, not the accepted `5x5x2` parity fixture:

- 31 provinces; annual `ii=1..15` representing 2009–2023;
- household grid `20x20x2`;
- `b∈[-2,5]`, `a∈[0,10]`, `z=[0.8,1.3]`;
- `ramin=.02`, `ramax=.09`, `wjtmin=.8`, `wjtmax=1.3`;
- `chi0=.1`, `chi1=2`, `a_bar=1e-6`;
- `ga=2`, `phi_l=5`, `frisch_l=.2`, `rho=.05`, `epsilon=10`, `theta=100`, `delta=.025`;
- `max_phi=.3`, `max_sigmau=.5`, `GDP_multiplier=1000`, `POP_multiplier=100`, `Ztratio=1`, `GovInv_ratio=1`.

Required data objects found and hashed:

| File | SHA-256 | Required variables/use | Status |
|---|---|---|---|
| `中国各省省会地理距离矩阵.xlsx` | `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566` | 31x31 distances → `sigmau_MAT` | present; source-local provenance only |
| `2000年后各省数据_填充NA.xlsx` | `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929` | GDP, capital, population, industry sheets | present; generated workbook |
| `2000年后各省数据.xlsx` | `09814A45D933B2685A35238A15C0C7BB501F00A63597796B3CADCE15C230ECB3` | raw fallback workbook | present |
| `R语言估计结果_plm估计.xlsx` | `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68` | regression alpha/intercepts | present |
| `数据估计结果_1000_100_0.mat` | `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A` | cached `mydata2`, including year-specific `IND_Zt/IND_alpha/GDP/CAP/POP` | present; selected by source |

No `Multi_Province_12sts_*.mat` cache was present during audit, so the live source would take the data/calculation branch. The data files have hashes but no Owner-issued baseline-year/provenance designation in the task.

## Dissertation cross-check

No dissertation Chapter 5 TeX/PDF/equation source was designated by the live task or located as a primary dissertation artifact in the repository. Therefore:

- Cobb–Douglas production, marginal-product wage/return, household aggregate meanings, and government-accounting interpretation: `MATLAB_NUMERICAL_CLOSURE_MORE_SPECIFIC` relative to the available project reports;
- no `MATLAB_DISSERTATION_CONFLICT_OWNER_DECISION_REQUIRED` claim is made without primary dissertation text;
- a formal dissertation alignment classification remains `OWNER_PROVENANCE_REQUIRED` for the exact dissertation artifact/path.

MATLAB remains the primary numerical authority.

## Unresolved Owner provenance list

1. Designate the exact Chapter 5 GE baseline year (`ii`/calendar year) for the next same-input residual-map gate, or explicitly authorize a multi-year contract.
2. Confirm whether `数据估计结果_1000_100_0.mat` with the hash above is the accepted calibration cache, rather than requiring regeneration from the Excel/R inputs.
3. Designate the dissertation Chapter 5 source artifact/path for the requested equation-level cross-check.
4. Define whether the next “residual map” should faithfully expose the source's manual diagnostics/state-update map, because MATLAB has no explicit unknown/residual vector or root function. This must not be invented by the executor.

## Deferred next-gate design

The recommended gate remains **MATLAB-faithful GE steady-state residual-map same-input parity at pre-frozen source-valid trial points**, but it is not executable until the four Owner provenance items above are resolved.

Once resolved, the smallest contract should freeze:

- province-major ordering for all 31-province sequential state inputs explicitly designated by Owner;
- source diagnostic ordering `[NKrationgap(1:31),Ytgap(1:31),convergent flags,ra-bound flags]`, or another Owner-approved faithful update-map representation;
- the exact year-specific initialized `results`, `grids`, `param`, `CHI`, `sigmau_MAT`, and `data_MAT` object hashes;
- source initial point plus at most one bounded perturbation that stays inside `ra/wjt` bounds;
- identical household value/policy warm-start identity across languages; source currently provides no cross-evaluation warm-start, so this must be specified explicitly;
- persisted per-province household inputs/outputs, `Lt_mat`, `Kt_supply`, `rah`, firm objects, wage vector, Taylor objects, diagnostic gaps, and every clipping/update flag;
- same-input source-local arithmetic rule `128*eps64*max(1,abs(x),abs(y))` plus a pre-frozen finite-reduction bound for 31-province sums;
- explicit call budget per trial point before execution. No full root solve should be authorized.

## Scientific call ledger, mutation, and acceptance level

| Scientific/model action | Calls |
|---|---:|
| MATLAB HJB/KFE/aggregate evaluator | 0/0/0 |
| Python HJB/KFE/aggregate evaluator | 0/0/0 |
| MATLAB/Python GE residual evaluation | 0/0 |
| GE root solve | 0 |
| D1-D3, asset-tail, transition, IRF, dynamics, calibration, Results | 0 |

Changed repository path: only this report. Pre-publication worktree otherwise clean. Acceptance level: complete source audit with unresolved Owner provenance; no GE contract acceptance and no next scientific execution authority.
