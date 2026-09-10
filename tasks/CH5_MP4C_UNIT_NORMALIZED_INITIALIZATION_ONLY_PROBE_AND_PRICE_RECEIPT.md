# CH5 MP4C unit-normalized initialization-only probe and price receipt

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Implement and execute one **bounded initialization-only diagnostic probe** using the newly accepted unit/initialization redesign specification.

The purpose is to determine whether correcting the macro data units and replacing legacy arbitrary first prices with data-consistent firm-side initialization materially changes the initial price scale before any household HJB/KFE or steady-state iteration is attempted.

This task is not a steady-state run and does not authorize HJB/KFE or outer-loop iteration.

## 2. Required authorities

Read live:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`;
- `docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md`;
- `docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC_ACCEPTANCE.md`;
- raw-NBS 2018 rebuild report and ledgers.

Protected MATLAB root remains read-only:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

At minimum inspect source equations in:

- `HANK_firm.m`;
- `wage_caculate.m`;
- `HANK_mp_1turn.m`;
- `mpHANK_equilibrium_2000.m`;
- `load_GDPdata.m`.

## 3. Probe inputs frozen for this task

Use:

- actual 2018 GDP and population from the accepted raw-NBS rebuild;
- raw-NBS GFCF Track-A PIM capital with `delta_pim=.096`;
- current rebuilt `alpha_raw=0.7380939146868483` and owner range `[.2,.8]`, hence `alpha_used=alpha_raw`;
- common macro units: `MU=10万元`, `NU=100 persons`;
- GDP亿元 `×1000`;
- capital亿元 `×1000`;
- population万人 `×100`;
- same-year `Zt0=Y0/(K0^alpha L0^(1-alpha))` after conversion;
- firm depreciation remains `.025` if and where the source firm equation uses it; do not substitute `.096` into firm equations.

The PIM route is selected only for this diagnostic probe, not yet Results authority.

## 4. Scientific-call budget

Authorized scientific/model calls are strictly limited to initialization-only deterministic source-equation evaluation.

Allowed:

- deterministic evaluation of the existing firm initialization equations for all 31 provinces;
- deterministic cross-province return/wage aggregation if it can be evaluated from initialized firm prices and static allocation/distance weights without invoking household HJB/KFE;
- static capital/labor allocation algebra only if no household solve is required and every input is already explicit;
- unit conversions and receipt generation.

Forbidden:

- household HJB calls: 0;
- KFE calls: 0;
- household control solves: 0;
- outer turns: 0;
- steady-state iterations: 0;
- GE/annual/IRF/Results: 0;
- root/Newton/Broyden/fsolve/Brent/Anderson: 0;
- parameter tuning based on outcomes: 0.

If `rah0` or household `w0` cannot be formed without household-dependent allocation objects, mark them `NOT_AVAILABLE_WITHOUT_HOUSEHOLD_SOLVE` rather than broadening authority.

## 5. Required initialization equations and receipts

For each province construct a source-traceable initialization receipt with at least:

- `Y0_raw_亿元`, `Y0_MU`;
- `POP_raw_万人`, `N0_NU`;
- `K0_trackA_亿元`, `K0_MU`;
- `L0` and its exact proxy/source role;
- `alpha_raw`, `alpha_used`, clip flag/reason;
- `Zt0`;
- zero-change bookkeeping values required by the source firm equation (`Kt_1=K0`, `Lt_1=L0`, `Yt_1=Y0`, `Zt_1=Zt0`, price/inflation state as source-backed);
- `raw_wjt0`;
- `used_wjt0` after unchanged source bounds;
- `raw_ra0`;
- `used_ra0` after unchanged source bounds;
- lower/upper clip flags;
- any tax/compensation terms that the source price clipping logic changes;
- the exact source equation/line provenance.

Do not use legacy `.09/.09/.6/20` as the new data-consistent initialization except as an explicit comparison column.

## 6. Household-to-macro asset bridge diagnostic

The current source bridge is:

`At_macro = At_grid * N_model`

with implicit bridge coefficient 1.

This task must **not** promote coefficient 1 to an economically justified production normalization.

Instead:

- document it as `SOURCE_FAITHFUL_BASELINE_ONLY`;
- compute simple deterministic scale diagnostics using the legacy initialized `At=2` only as a historical-reference object, not as an accepted household equilibrium;
- compare `At*N` scale against 2018 K0/GovInv scale where meaningful;
- do not select a replacement bridge from these ratios;
- do not run household HJB to calibrate the bridge.

## 7. Initialization comparison

Produce a 31-province human-readable and machine-readable table comparing:

- legacy initial `wjt=.6`, `ra=.09`;
- data-consistent `raw_wjt0`, `used_wjt0`;
- data-consistent `raw_ra0`, `used_ra0`;
- whether each price is inside/below/above the unchanged source bounds;
- legacy mixed-year data versus corrected 2018 Y/K/N/Z where useful;
- K/Y, K/N, Y/N;
- source bridge scale diagnostic.

National summaries must include:

- count of raw ra below/inside/above bounds;
- count of raw wage below/inside/above bounds;
- min/median/max raw and used prices;
- provinces with largest raw-price discrepancies from legacy starts;
- top provinces by K/Y and K/N;
- whether the corrected-unit initialization still starts the model mostly on clipping boundaries.

## 8. Optional rah0/w0 receipt

If source-static information is sufficient, produce:

- source-lagged baseline `rah0` constructed from initialized clipped `ra0` under the existing cross-province return map;
- household `w0` constructed from initialized clipped `wjt0` under the existing static wage/migration map.

If either requires household outputs such as Ct/Lt or a household-dependent allocation, do not fake it. Mark the object unavailable and specify the minimum later probe needed.

No damping is applied in this task. The point is to observe the raw initialization scale first.

## 9. Implementation boundary

Implement only a diagnostic/helper path under validators/reports or another clearly non-production location.

Do not modify production household, firm, KFE, controller, steady-state or Results source.

No lambda/hysteresis/GovInv damping is selected here.

## 10. Evidence root and outputs

Use fresh local evidence root, e.g.:

`D:\ProjectTemp\ch5-unit-normalized-initialization-probe-20260910-001`

Use a fresh suffix if occupied.

Required repository-safe outputs:

- `docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_REPORT.md`;
- `reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv`;
- same table in Markdown;
- `national_initialization_summary.json`;
- `asset_bridge_scale_diagnostic.csv`;
- `source_equation_receipt.json`;
- `call_ledger.json`;
- focused tests/static checks;
- manifest/readback;
- reproducible diagnostic helper code.

## 11. Allowed primary verdicts

- `UNIT_NORMALIZED_INITIALIZATION_PROBE_PASS__DATA_CONSISTENT_PRICE_RECEIPT_COMPLETE`;
- `UNIT_NORMALIZED_INITIALIZATION_PROBE_PARTIAL__COMPOSITE_PRICE_OBJECTS_REQUIRE_HOUSEHOLD_INPUTS`;
- `UNIT_NORMALIZED_INITIALIZATION_PROBE_BLOCKED__SOURCE_EQUATION_OR_UNIT_CONTRACT_INCOMPLETE`.

## 12. Stop/authority after completion

Even on PASS:

- no household HJB/KFE;
- no first full outer turn;
- no steady state;
- no damping candidate execution;
- no hysteresis validation;
- no GovInv redesign;
- no production asset-bridge selection;
- no Results.

Commit and non-force push a dedicated branch. Do not merge main and do not start a successor task.
