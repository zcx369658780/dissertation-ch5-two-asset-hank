# MP4B turn-1 source-layer numerical attribution report

## Terminal verdict

`MP4B_L3_READ_ONLY_TURN1_SOURCE_LAYER_NUMERICAL_ATTRIBUTION_AND_FIRST_ACTIONABLE_DIVERGENCE_PASS`

Strongest classification: `MP4B_SAME_INPUT_SOURCE_LAYER_PYTHON_IMPLEMENTATION_DEFECT_CONFIRMED`.

The protected MATLAB firm path consumes same-turn household `results.Lt` as carried `Lt_1`; Python `one_turn` fails to map `household_lt` and leaves old `Lt_prev` (`186000.0` for Beijing). Persisted scalar arithmetic gives MATLAB `mt=1.0121097874161467`, current Python `mt=1.0080400772138627`, and source-correct substitution `mt=1.0121097874161467`. No repair was authorized or made.

## Continuity and identities

Start task/HEAD `25f584ea948765186a62d1e7858aced4dbcf7106`, direct parent `6c3df05d627fee95d43bdf08577e5a87e41b2cff`, clean, `HEAD==origin/main`, ahead/behind `0/0`.

Immutable hashes matched: trace `6C4AEC5992A59C1C8D7859DEF082E5711864789CAE009FD1E5CC2B78B3F6A520`; final MAT `D2F4B225AC362A6805AAD1CD065AFA87DA32551833E5FC867BA3A37C9FD0B8F0`; baseline `68C9F396C57D385E72E6A46D94A53F4196F7E9BFBC84A6EAF66AB1FF64A0866B`; V5 `A64172CC32EC7295297CED6DFE27B52CE51B5EAD64AD82453C60EBE0152965C3`; overlay terminal/chronology/manifest `5C9675702D27FF03A3ADA8959166C757F152B8C9E91126533E557373CB7C74E0`, `09DC11C9BBB6E4CDF81C687A2F94FA1E460F2C608544825ADCAED88EC9A00F8F`, `DBA08ACDBC5E0E769FCA18C4E806B5B648703B839ED90469493835BEE146B6AB`; Beijing contract/MATLAB/standalone/comparison `FE833FAEB48521CD0C7594627AF6FB5012F9497A455E9B2C5E7490E0C40E6F22`, `024B097CEAC5872B5E83421B186C8424ECA92CD06A6D5D0FAF7B220BBFAB9DFE`, `9E9967F023C89F22550AEAC3C8CD53215B70E13C3C70E16C0CCC5C3D518A0F83`, `28966B73605BD82BA858C3B2A3CBC144C867377C71476B1003846C88AE6382BF`.

## Beijing household

Decimal / binary64 bits:

| Field | MATLAB | standalone | overlay |
|---|---|---|---|
| Ct | 11.400731651946101 / `4026CD2CB2F7293F` | 11.40073165194351 / `4026CD2CB2F7238C` | 11.400731651949162 / `4026CD2CB2F72FFA` |
| Lt | .6476235981139693 / `3FE4B9551FC08E18` | .6476235981138799 / `3FE4B9551FC08AF3` | .647623598114104 / `3FE4B9551FC092D5` |
| At | 7.274097868486163 / `401D18AD1C94349D` | 7.274097868485189 / `401D18AD1C943054` | 7.274097868486394 / `401D18AD1C9435A1` |
| Bt | 4.698277466946523 / `4012CB093F9046B2` | 4.698277466946337 / `4012CB093F9045E0` | 4.6982774669466725 / `4012CB093F90475A` |
| At+Bt | 11.972375335432687 / `4027F1DB2E123DA8` | 11.972375335431526 / `4027F1DB2E123B1A` | 11.972375335433068 / `4027F1DB2E123E7E` |

MATLAB-overlay absolute/relative/ULP/bound: Ct `3.0606628342866316e-12 / 2.6846196610226814e-13 / 1723 / 1.1400731651949161e-6`; Lt `1.346700528870315e-13 / 2.0794494406811925e-13 / 1213 / 1e-7`; At `2.3092638912203256e-13 / 3.174639567642827e-14 / 260 / 7.274097868486394e-7`; Bt `1.4921397450962104e-13 / 3.175929381765368e-14 / 168 / 4.6982774669466723e-7`; At+Bt `3.801403636316536e-13 / 3.1751457248972315e-14 / 214 / 1.1972375335433067e-6`. All three pairings for every field pass the unchanged frozen comparator.

MATLAB-standalone absolute/relative/ULP/bound: Ct `2.5917046286849654e-12 / 2.2732792138323528e-13 / 1459 / 1.1400731651946101e-6`; Lt `8.93729534823251e-14 / 1.3800138497516142e-13 / 805 / 1e-7`; At `9.743317264110374e-13 / 1.3394536945016507e-13 / 1097 / 7.274097868486163e-7`; Bt `1.865174681370263e-13 / 3.9699117272068356e-14 / 210 / 4.698277466946523e-7`; At+Bt `1.1617373729677638e-12 / 9.703482729359136e-14 / 654 / 1.1972375335432688e-6`.

Standalone-overlay absolute/relative/ULP/bound: Ct `5.652367462971597e-12 / 4.957898874854424e-13 / 3182 / 1.1400731651949161e-6`; Lt `2.240430063693566e-13 / 3.4594632904325197e-13 / 2018 / 1e-7`; At `1.20525811553307e-12 / 1.6569176512658908e-13 / 1357 / 7.274097868486394e-7`; Bt `3.3573144264664734e-13 / 7.145841108972078e-14 / 378 / 4.6982774669466723e-7`; At+Bt `1.5418777365994174e-12 / 1.287862845425606e-13 / 868 / 1.1972375335433067e-6`.

Persisted scalars are exact; grids/numerics and aggregation formulas/order are the same. Runtime raw incoming arrays were not serialized, so only representation-equivalent same-source construction, not byte identity, is claimed. Standalone/national HJB iterations are 73/64. Classification: `MP4B_TURN1_BEIJING_HOUSEHOLD_DIFFERENCE_ACCEPTED_NUMERICAL_NONIDENTITY_NO_ACTIONABLE_DEFECT`.

## Source chain and firm

MATLAB/overlay: `Lt_supply` 4209719.4410444815/4209719.44104403; `Kt_supply` 284250.6494603705/284250.6494603797; `rah` exact .06745076142659637; final firm Kt exact 225600114244.87213. Firm `Yt` 79417893.1140632/79417893.11405928; each side's `Zt*Kt^alpha*Lt^(1-alpha)` residual is zero, so `MP4B_TURN1_FIRM_YT_DIVERGENCE_UPSTREAM_INPUT_DRIVEN`.

The independent `Lt_1` mapping defect explains `mt`, preclip prices/returns and downstream `Govinc` (-5564891063.61484/-5565214271.424694) and composite wage (17.740518629558398/17.729107634252784). Beijing clips still agree: `wjt=1.3`, `ra=.02`.

## 31 provinces and turn 8

Turn-1 entry `Zt` and 17 mapped fields are 31/31 bitwise exact. Earliest differing layer counts: household output 31; migration 0; capital 0; firm input 0; firm output 0; wage/policy/controller 0; no observed difference 0. Max normalized differences: Ct 2.68462e-13 Beijing; At 3.17464e-14 Beijing; Bt 3.17593e-14 Beijing; household Lt 1.34670e-13 Beijing; Lt_supply 1.07807e-13 Guizhou; Kt_supply 3.24103e-14 Hainan; Yt 4.97940e-14 Gansu; Govinc 1.11081e-4 Guangdong; wjt 1.47143e-2 Hebei; ra has zero differing provinces. This normalization reports scale only and is not a tolerance.

Shanghai/Qinghai differences persist and grow before turn 8, but no isolated counterfactual connects either the benign household nonidentity or the `Lt_1` defect to the MATLAB-only Qinghai/Python-only Shanghai reset. Chronology is not causation; turn 8 remains upstream-unattributed.

## Package and ledger

External root: `D:\ProjectTemp\ch5-mp4b-turn1-source-layer-numerical-attribution-20260901-001`; required artifacts and their sizes/hashes are in `diagnostic_manifest.json`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `turn1_beijing_three_way_household_binary64.json` | 202 | `76D05272751371E33612B68D97EA066570E5F41A6F23D532BBBE0A41143D23F7` |
| `turn1_beijing_household_input_path_matrix.json` | 355 | `E2D3427D7FA9EE774D38B6D319C597F0EEABD86BA956655206751F597B433580` |
| `turn1_beijing_source_layer_chain.json` | 502 | `E512221E1D716D7A5DED8EE457D896184C6E5CE23EC4BAF0DBDE8E785F675089` |
| `turn1_firm_source_arithmetic_audit.json` | 2024 | `E5892C5665F6601EECD8977419961ED70E95902366E0422711B5619DC267B7E4` |
| `turn1_allprovince_earliest_difference_census.json` | 804 | `6781C74EFB6E784CD29B8B1C23816591DA3557DE43BEFB0C7B9542E4C8A41B4E` |
| `turn1_to_turn8_relevance.json` | 222 | `A76D9AE70F45BD3E740E6B3804C430D579AF02D4242CA65464391CEE1F26339A` |
| `source_expression_map.md` | 1253 | `D95C37D31992C33802F5E2CB6E35AD45BDCFD0B8C6789723CB19835F5F2BC9C0` |
| `diagnostic_manifest.json` | 1929 | `EFF74CF8917D212C9A8687A30EB0E6EEBFAF82125189F8FBD707D24A2A0CC2B4` |

The package also records the orchestrator intake checkpoint: 349 bytes, `790B5D3AD5E8A0257405DC8CA9D6532DB8F421372A9787D44CC658AEE8851484`.

Zero-model ledger: MATLAB/checkcode/stationary/HJB/KFE/household/firm/controller 0; Python stationary/HJB/KFE/household/MP2/MP3 0; comparator/replay 0; province replay 0; other years/batch 0; shocks/AR1/transition/dynamics/IRF 0; R5/Results 0. Only read-only parsing, hashing and persisted scalar arithmetic ran. Repository mutation is this report only.

## Exactly one recommended next gate

Publish a zero-model implementation task to correct and statically/test the Python `one_turn` mapping of same-turn `household_lt` into firm-source `Lt_1`/`Lt_prev`, followed by independent L3 review; authorize no stationary, MATLAB, comparator/replay, threshold work or Results.
