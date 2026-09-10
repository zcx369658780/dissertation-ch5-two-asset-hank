# Chapter 5 MP4C Python runtime input-binding and unit-contract repair

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Repair the current Python multi-province runtime implementation so that the accepted corrected-2018 data and unit contract are the objects actually consumed by initialization and subsequent model turns.

This task responds to the Reviewer rejection of candidate `242e853708d3d0d4f891c7a043d7d4e3fba05c50`, which ran with a legacy/canonical capital-GovInv scale instead of the frozen raw-NBS Track-A/unit-normalized baseline.

The goal is an implementation correction plus tests and static/deterministic receipts. This task does **not** authorize a new 50/100-turn scientific trajectory.

## 2. Required authorities

Fresh-read live `origin/main` and at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_CORRECTED_2018_100_TURN_BOUNDARY_TRAJECTORY_DIAGNOSTIC_REJECTION.md`;
- `docs/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_REPORT.md`;
- `docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_REPORT.md`;
- `docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_ACCEPTANCE.md`;
- `docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md`;
- accepted firm-price forensic report/acceptance;
- current Python multi-province runtime/data-loader/harness source actually used by candidate `242e853...`.

Candidate `242e853...` may be inspected as rejected evidence but must not be merged.

Protected MATLAB remains read-only.

## 3. Frozen corrected-2018 runtime contract

The repaired Python runtime must bind, for all 31 provinces:

- actual 2018 GDP;
- actual 2018 population;
- raw-NBS GFCF Track-A PIM capital;
- `delta_pim=.096`;
- `alpha_raw=.7380939146868483`;
- `alpha_used=.7380939146868483`;
- common macro units `MU=10万元`, `NU=100 persons`;
- GDP conversion: `亿元 * 1000 -> MU`;
- capital conversion: `亿元 * 1000 -> MU`;
- population conversion: `万人 * 100 -> NU`;
- same-year `Zt0 = Y0/(K0^alpha * L0^(1-alpha))` under the accepted 2018 population-as-labor proxy for initialization;
- protected firm depreciation `.025` remains distinct from PIM depreciation `.096`;
- source `ra` bounds `[.02,.09]` and wage bounds `[.8,1.3]` unchanged;
- source-lagged `rah` timing unchanged in the source-faithful baseline;
- no new `w/rah` damping, no new hysteresis, no new GovInv damping in this repair.

This task does not promote raw-NBS Track-A or `beta_a=1` to Results authority. It only repairs the runtime to obey the previously authorized diagnostic baseline.

## 4. Proven bug to repair

The rejected candidate entered the trajectory with runtime values inconsistent with the frozen contract. In particular, the runtime inherited the earlier canonical corrected-three-turn payload / old capital scale instead of Track-A/unit-normalized objects.

For Anhui, the repaired pre-science initialization must reproduce the accepted receipt:

- `Y0 = 34,010,900 MU`;
- `N0 = 607,600 NU`;
- `K0_trackA = 70,182,433.35888097 MU`;
- `alpha_used = .7380939146868483`;
- `Zt0 = 1.681124916844091` within serialization/float tolerance.

It must **not** silently bind the old canonical objects such as:

- `K≈1.357314108e12` in the old transformed scale;
- `Zt≈0.00069346445` from the previous canonical contract.

## 5. Implementation requirements

Identify and repair every Python path by which a corrected-2018 run obtains:

- province order;
- GDP;
- population;
- PIM capital;
- alpha;
- Zt;
- `Kt0/Kt_1`;
- `GovInv0`;
- `Y0/Yt_1`;
- `Lt0/Lt_1`;
- initialization prices/returns;
- runtime payload hashes/receipts.

There must be one explicit corrected-2018 runtime data object / schema, not a mixture of legacy and corrected payloads assembled ad hoc across functions.

Avoid broad refactors unrelated to this bug.

## 6. Runtime authority and fallback rules

For the corrected-2018 route:

- legacy/canonical old-scale data may remain available only as explicitly named historical/diagnostic inputs;
- no implicit fallback from Track-A corrected data to canonical/legacy transformed capital is allowed;
- missing corrected inputs must raise a clear error before science starts;
- year, route, unit and source identities must travel with the runtime payload.

Recommended explicit metadata fields include:

- `data_year=2018`;
- `gdp_route`;
- `population_route`;
- `capital_route=RAW_NBS_GFCF_TRACK_A_PIM`;
- `capital_unit=MU_10WAN_YUAN`;
- `population_unit=NU_100_PERSONS`;
- `delta_pim=.096`;
- `alpha_raw`, `alpha_used`;
- `zt_contract=SAME_YEAR_Y_K_L_2018`;
- source file/hash identities.

## 7. GovInv initialization boundary

Do **not** invent a new economic GovInv initialization rule in this task.

Repair only these proven implementation requirements:

1. whatever `GovInv0` rule the current authorized baseline uses, its numeric value must be expressed in the same `MU` as `Kt_supply` and `Ktarget`;
2. `GovInv0` may not be inherited from an old capital object in a different unit/route;
3. store explicit fields:
   - `GovInv0_raw_source`;
   - `GovInv0_MU`;
   - `GovInv0_rule_id`;
   - `GovInv0_route_id`.

If the current source-faithful rule is `GovInv0=Ktarget`, preserve that rule for now but apply it to the **correct Track-A Ktarget in MU**, and label it `SOURCE_FAITHFUL_INITIALIZATION_RULE__SCIENTIFIC_REDESIGN_PENDING`.

Do not implement `GovInv=max(Ktarget-Kt_supply,0)` yet; that is a later Owner/Reviewer scientific decision.

## 8. Household asset bridge boundary

Do not choose a new `beta_a`.

For the repaired diagnostic runtime:

- keep source-faithful `beta_a=1` only when explicitly requested by the diagnostic baseline;
- label it `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`;
- store bridge metadata in the runtime object/receipt;
- prevent any code path from using convergence or target matching to alter the bridge.

## 9. Labor initialization boundary

Do not redesign `Lt_seperate` in this task.

Initialization may continue to use 2018 population proxy `N0` / `L0` exactly as in the accepted initialization receipt.

However, make names/metadata explicit so that:

- `household_labor_per_capita`;
- `population_proxy_NU`;
- `firm_Lt_supply`;

cannot be silently conflated.

Add assertions/tests for shapes and roles where practical.

## 10. Pre-science hard assertions

Before any future scientific run can advance state, the repaired route must validate all 31 provinces against an immutable expected initialization receipt.

At minimum assert:

- province order 31/31 exact;
- year 2018 31/31;
- GDP exact/within documented source precision;
- population exact/within documented source precision;
- Track-A K exact within deterministic float tolerance;
- alpha raw/used exact;
- Zt0 deterministic identity;
- unit metadata exact;
- capital route exact;
- no old canonical capital-scale object present in the active runtime state;
- GovInv and K operands have identical declared units;
- finite values and positive Y/K/N where required.

For Anhui include a dedicated assertion for the values listed in section 4.

Failure must stop before any household/HJB/KFE/firm/outer scientific call.

## 11. Compatibility tests

Add tests proving:

1. corrected-2018 builder returns the accepted 31-province initialization receipt;
2. legacy/canonical and corrected Track-A routes cannot be confused by identical field names without route metadata;
3. attempting to inject the rejected candidate's old-scale Anhui `K/GovInv/Zt` into the corrected route fails pre-science;
4. serialization/deserialization preserves unit and route metadata;
5. runtime payload hash changes if capital route/unit/value changes;
6. province order mismatch fails;
7. missing 2018 corrected input fails;
8. no scientific model call is needed for these tests.

## 12. Deterministic reconciliation outputs

Without running household/HJB/KFE/outer science, generate a 31-province pre-science reconciliation ledger containing at least:

- province;
- corrected GDP raw and MU;
- corrected POP raw and NU;
- Track-A K raw亿元 and MU;
- alpha;
- Zt0;
- current repaired GovInv0 MU under the preserved source-faithful rule;
- old rejected-candidate K/GovInv/Zt values when available, clearly labelled rejected/historical;
- ratios old/new;
- unit/route metadata;
- assertion status.

Also provide a dedicated Anhui before/after receipt.

## 13. Scientific-call budget

All model/scientific calls = 0 for this implementation task.

Forbidden:

- household HJB;
- KFE;
- household controls;
- firm runtime trajectory call;
- `Lt_seperate` runtime solve;
- outer turn;
- steady state;
- root/Brent scientific solves;
- GE/annual/IRF/Results.

Allowed:

- Python code edits;
- deterministic data loading/conversion;
- static/deterministic formula checks;
- tests;
- hashes/serialization;
- lint/compile/static checks.

## 14. Required repository outputs

At minimum:

- repaired Python production/runtime source files;
- focused regression tests;
- `docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_REPORT.md`;
- `reports/mp4c_python_runtime_input_binding_repair_20260910/runtime_reconciliation_31province.csv`;
- `.../anhui_before_after_receipt.json`;
- `.../runtime_schema_receipt.json`;
- `.../pre_science_assertion_receipt.json`;
- `.../call_ledger.json`;
- `.../source_hash_receipt.json`;
- manifest/readback and static test receipts.

Do not commit private raw XLS or protected MATLAB files.

## 15. Acceptance criteria

A candidate may be submitted for Reviewer acceptance only if:

- corrected-2018 runtime data binding is explicit and single-route;
- 31/31 pre-science assertions pass;
- Anhui matches the accepted unit-normalized receipt;
- rejected old-scale payload is demonstrably blocked;
- GovInv uses the corrected Track-A K scale/unit under the preserved source-faithful initialization rule;
- no unapproved Lt/GovInv/bridge/damping/controller scientific redesign is introduced;
- all focused tests pass;
- scientific/model calls remain zero;
- worktree clean and candidate branch pushed.

Allowed primary verdicts:

- `PYTHON_RUNTIME_INPUT_BINDING_REPAIR_PASS__CORRECTED_2018_TRACK_A_UNIT_CONTRACT_ENFORCED`;
- `PYTHON_RUNTIME_INPUT_BINDING_REPAIR_PARTIAL__ADDITIONAL_LEGACY_FALLBACK_PATH_REMAINS`;
- `PYTHON_RUNTIME_INPUT_BINDING_REPAIR_BLOCKED__CURRENT_RUNTIME_ARCHITECTURE_CANNOT_ENFORCE_CONTRACT_WITHOUT_OWNER_DECISION`.

## 16. Git boundary

Use a dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit and non-force push candidate;
- do not merge main;
- do not publish successor scientific task;
- do not run a new trajectory.

Return to ChatGPT Reviewer with verdict, branch, candidate SHA, files changed, test results, 31-province assertion result, Anhui before/after receipt, and report path.
