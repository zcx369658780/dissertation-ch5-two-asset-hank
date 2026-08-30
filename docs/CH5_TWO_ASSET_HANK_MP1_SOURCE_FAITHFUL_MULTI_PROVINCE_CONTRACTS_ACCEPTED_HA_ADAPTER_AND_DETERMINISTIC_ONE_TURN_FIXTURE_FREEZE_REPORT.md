# MP1 source-faithful multi-province contracts, accepted HA adapter, and fixture freeze

## Terminal classification and freezes

`MP1_SOURCE_FAITHFUL_CONTRACTS_ADAPTER_AND_ONE_TURN_FIXTURE_FREEZE_PASS`

Freeze:

- `MP1_SOURCE_FAITHFUL_CONTRACTS_ADAPTER_AND_ONE_TURN_FIXTURE_FREEZE_ACCEPTED`
- `MP1_PROVINCE_ORDER_AND_ORIENTATION_CONTRACT_ACCEPTED`
- `MP1_AT_ONLY_PRODUCTIVE_CAPITAL_CONTRACT_ACCEPTED`
- `MP1_ACCEPTED_TWO_ASSET_HA_STATIC_ADAPTER_CONTRACT_ACCEPTED`
- `MP1_NO_LEGACY_R5_RUNTIME_DEPENDENCY_ACCEPTED`
- `MP1_ASYMMETRIC_ONE_TURN_OUTER_FIXTURE_ACCEPTED`

MP1 freezes contracts and independent fixture arithmetic only. It implements no production one-turn/update-map code and accepts no GE, annual calibration, dynamic, IRF, or Results object.

## Authority and Owner route

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Live task/start: `c5a2060e08e5f237918bf9a7b6f820f8c6e35086`.
- Direct parent: Owner-route roadmap update `1158954fcb3d482a70c5ba45f4a3a311fbefdd91`.
- Owner markers verified: `OWNER_SINGLE_ACTIVE_CODEBASE_TWO_ASSET_HANK_ONLY`, `LEGACY_ONE_ASSET_R5_SUPERSEDED_NO_ACTIVE_PROGRAM_AUTHORITY`, `ACTIVE_MODEL_REPOSITORY_DISSERTATION_CH5_TWO_ASSET_HANK`.
- Primary numerical authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Historical one-asset R5 was neither opened as a runtime nor modified/imported/copied. It remains historical evidence only.

## Scientific/model call ledger

| Call | Count |
|---|---:|
| MATLAB | 0 |
| current modular Python HJB / KFE | 0 / 0 |
| standalone HA / KFE / aggregate | 0 / 0 / 0 |
| legacy R5 model | 0 |
| fixed point / GE | 0 / 0 |
| shock or AR1 response | 0 |
| transition / dynamics / IRF | 0 / 0 / 0 |

Executed Python was limited to imports, contract/fixture arithmetic, focused unit tests, compile checks, hashes, and static searches.

## Protected source continuity

Protected MATLAB root remained read-only.

| Source | SHA-256 | MP1 evidence |
|---|---|---|
| `multi_prov_HANK_12sts.m` | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` | annual/cache routing |
| `mpHANK_equilibrium_2000.m` | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` | province/data initialization 22-50 |
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` | later manual-loop boundary only |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` | household call 14-16; labor/capital/rah 21-40; firm/wage/Taylor/fiscal 44-65 |
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | input roles 26-36; household outputs 347-365 and 397-425 |
| `Lt_seperate.m` | `D30519AD81837E8EB5EBFE74BF25CC770E40B5C5AE5A254951AD97D436CACE26` | destination-row/origin-column formula 6-14 |
| `HANK_firm.m` | `EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5` | `Lt_supply`, `Kt_supply+GovInv`, firm/fiscal 5-98 |
| `wage_caculate.m` | `0FB84B51E2BE50CD3D065D33385882311A31E12596AEEB0CE2C808A8C36B6A63` | composite wage formula 4-16 |
| `load_distdata.m` | `18F594DD7D1ED090CA2AF576DEBCD8DCAA73C012608A8921F8D5BD6CC24F478B` | distance-to-migration-cost orientation 1-8 |
| `load_GDPdata.m` | `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5` | province columns 10/74; GDP/CAP/POP 93-104; cache 106-110/246 |

Accepted standalone oracle remained byte-identical at `exports/matlab_faithful_two_asset_ha.py`, SHA-256 `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`. No accepted household source changed.

No live task designated a dissertation artifact path. Dissertation alignment remains provenance-only and does not block MP1 because all implemented contracts are source-bound to MATLAB and the accepted oracle.

## Province and shape contract

The exact source order is frozen as:

`北京, 天津, 河北, 山西, 内蒙古, 辽宁, 吉林, 黑龙江, 上海, 江苏, 浙江, 安徽, 福建, 江西, 山东, 河南, 湖北, 湖南, 广东, 广西, 海南, 重庆, 四川, 贵州, 云南, 西藏, 陕西, 甘肃, 青海, 宁夏, 新疆`.

`ProvinceAxis`, `ProvinceVector`, and `ProvinceMatrix` reject wrong count, duplicates, unknown/reordered labels, non-finite values, and shapes other than `(31,)` or `(31,31)`. Arrays are copied and made read-only.

## Household static adapter contract

The adapter imports no solver and calls no callable. It records the accepted public symbols and constructs only an immutable argument description. Static boundary validation requires the accepted public grid, economic-parameter, and numerics fields and enforces `initial_value`/`baseline_labor` shape `(b,a,z)`.

| MATLAB outer role | Accepted HA role | Timing |
|---|---|---|
| `results.rah` | `HouseholdInputs.r_a` | pre-solve composite |
| `results.rb` | `HouseholdInputs.r_b` | pre-solve |
| `results.tau` | `HouseholdInputs.tau` | pre-solve |
| composite `results.w` | singleton `HouseholdInputs.wages` | pre-solve composite; no 31 illiquid states |
| composite migration wedge | singleton `migration_costs` | pre-solve composite |
| composite labor-disutility weight | singleton `labor_weights` | pre-solve composite |
| `results.Tt` | `transfer_income` | solver argument |
| `results.rb_gap` | `borrowing_rate_gap` | solver argument; not productive return |
| source grids `a,b,z` and `la_mat` | accepted `MatlabFaithfulHJBGrid.a,b,z,switch_matrix` | mandatory object; `la_mat` is the switching generator |
| `rho,ga,frisch_l,chi0,chi1,a_bar` | accepted economic parameter fields | explicit static map; no defaults |
| initial value / baseline labor / numerics | corresponding accepted solver arguments | mandatory, immutable arrays |

Accepted outputs map to `Ct`, household `Lt`, `At`, `Bt`, `AtTax`, convergence flag/statistic. Household `Lt` is not `Lt_supply`. `AtTax`, `Lt_mat`, and `Lt_supply` are marked as source-defined post-solve/reconstruction boundaries; `Lt_mat` and `Lt_supply` are outside the household HJB.

The accepted `EconomicParams` object also contains `mu_z` and `sigma_z` compatibility fields, but the standalone solver does not use them in place of `grid.switch_matrix`. MP1 therefore requires the accepted object shape without asserting a MATLAB `la_mat` diffusion/mean-reversion mapping.

## Flow/orientation invariants

- `Lt_mat[j,i]` is labor from origin `i` to destination `j`; rows are destinations, columns origins; `Lt_supply[j]=sum_i Lt_mat[j,i]`.
- Productive private capital contribution is `inter_prv_ratio[i]*At[i]*N[i]` only. `Bt` and `At+Bt` are forbidden; changing `Bt` alone leaves `Kt_supply` unchanged.
- `Kt_supply[i]=(sum(contributions)-contribution[i])/(N_prov-1)` and firm capital is `Kt_supply+GovInv`.
- Literal source return is `(1-q_i)*ra_i + q_i/(N-1)*(sum_j q_j*ra_j-q_i*ra_i)`, where `q_i=inter_prv_ratio[i]`; it is not generic `W@ra`.
- `wjt` is firm wage; `w` is the household composite wage; `Lt_supply` is the firm's labor input.
- `rb=istar+rho_pi*totalpit+epsilon_pi-totalpit`; `rb_gap` is a borrowing spread.
- `Govinc` and national `GovSurplus=sum_i(Govinc_i-Bt_i*rb_i*N_i)` are diagnostics, not an invented balanced-budget target.

## Data/cache provenance and unresolved annual authority

The manifest binds six source/cache identities without committing raw files: the distance workbook; filled and raw province workbooks; regression workbook; `数据估计结果_1000_100_0.mat`; and `Multi_Province_12sts_<year>.mat`. It records source/cache classification, verified MP0 hashes when available, raw/derived role, read-only/no-overwrite status, year semantics, and Owner-approval requirement.

`YearCacheBinding.require_annual_execution_authority()` fails closed until Owner verification. The unresolved relationship among `source_ii`, dataset row, and filename year `ii+2008` remains explicit. No baseline year or calibration-cache authority was selected.

## Asymmetric fixture

- Classification: `NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE`.
- Path: `tests/fixtures/multi_province/mp1_asymmetric_one_turn.json`.
- SHA-256: `7B8ACDB78F8BA92C9BAEA162A83F56CF4558DEE2802277281EDAF8B43D092219`.
- Dimension/order: `Synthetic-A`, `Synthetic-B`, `Synthetic-C`.
- Inputs are deliberately asymmetric in `N,Ct,Lt,At,Bt,AtTax,inter_prv_ratio,ra,wjt,tau,GovInv,alpha,Zt`, migration wedges and labor weights.
- Household outputs are pre-frozen; the accepted household solver is never called.
- Independent evaluator: `validators/multi_province/mp1_fixture_arithmetic.py`; it is not production code and exposes no `one_turn` API.

Expected objects frozen in the JSON include `Lt_mat`, `Lt_supply`, capital contributions, `Kt_supply`, `rah`, feasible firm `Kt/Lt/Yt/mt/KNratio/wjt/rk/tax/ra/Govinc`, household composite wage, Taylor `rb`, and national `GovSurplus`. Fixed-point/dynamic objects are exactly `DEFER_TO_MP2_SOURCE_FIXTURE`.

Negative tests prove that transposed labor orientation, `At+Bt` capital, generic return averaging, province reordering/shape errors, and legacy imports fail. A `Bt`-only perturbation preserves productive-capital objects.

## No-legacy dependency proof

- Active MP1 modules import only standard library, NumPy, and current-package modules.
- AST import scan found no `chapter5_model` import.
- `reject_legacy_runtime_references` rejects both the old package name and historical repository path.
- Fixture payload validation rejects legacy runtime references.
- Marker: `NO_LEGACY_R5_RUNTIME_DEPENDENCY=True`.

## Files written

- `src/ch5_two_asset_hank/multi_province/__init__.py`
- `src/ch5_two_asset_hank/multi_province/provenance.py`
- `src/ch5_two_asset_hank/multi_province/province_contracts.py`
- `src/ch5_two_asset_hank/multi_province/household_adapter.py`
- `validators/multi_province/__init__.py`
- `validators/multi_province/mp1_fixture_arithmetic.py`
- `tests/fixtures/multi_province/mp1_asymmetric_one_turn.json`
- `tests/test_mp1_multi_province_contracts.py`
- `tests/test_mp1_household_adapter.py`
- `tests/test_mp1_asymmetric_one_turn_fixture.py`
- this report.

No raw/binary data was added.

## Tests, checks, and forbidden operations

- Focused MP1 tests: `26 passed`.
- Compile/bytecode validation of changed Python paths: PASS.
- `git diff --check`: PASS.
- Static solver-call/import search: no scientific invocation and no legacy runtime import.
- Initial test integration found one false-positive string scan: the adapter's fail-closed rejection list intentionally names the forbidden historical repository. The test was corrected to inspect actual AST imports; no scientific or model retry was involved.

Forbidden-operation check: no MATLAB; no HJB/KFE/HA/GE/fixed-point/AR1/transition/dynamics/IRF; no production `one_turn`, `steady_state`, `annual`, firm/migration/capital/wage/monetary/fiscal module; no baseline/cache approval; no Results; no protected-source/oracle modification; no historical-R5 modification/import; no raw/binary data.

## Acceptance level and next gate

Acceptance is MP1 contract/static-adapter/asymmetric-fixture evidence only. It is not outer-model numerical parity.

Exactly one recommended successor: **MP2 source-faithful deterministic one-turn implementation on the frozen asymmetric fixture**, under a new live task with explicit allowed production paths and a separately frozen non-scientific/scientific call budget. MP3 and full 31-province execution remain unauthorized.

Git closeout evidence is reported after the single authorized commit, push, and GitHub read-back.
