# Chapter 5 MP4C Python runtime input-binding and unit-contract repair report

Date: 2026-09-10

Base `origin/main`: `e3558062a265a727e5da2f12ab7b737287db2129`

Branch: `codex/ch5-python-runtime-input-binding-repair-20260910`

Verdict: `PYTHON_RUNTIME_INPUT_BINDING_REPAIR_PASS__CORRECTED_2018_TRACK_A_UNIT_CONTRACT_ENFORCED`

## Result

The active corrected-2018 Python runtime no longer obtains GDP, population, capital, alpha, Zt, GovInv, or initialization prices from the private canonical workbook. A single frozen runtime object now binds the accepted repository-safe raw-NBS ledger and initialization receipt, with their exact SHA-256 identities, and carries year, route, unit, labor-role, GovInv-rule, and asset-bridge metadata into the serialized payload.

The former canonical builder remains only as the explicitly named `build_legacy_canonical_runtime_payload` historical replay API. It is not a fallback and is not called by the corrected single-, two-, three-, or five-turn prepare paths. The historical three-turn reexecution gate is now fail-closed because its accepted runner identity and predecessor values belong to the superseded canonical contract.

## Enforced contract

- year: actual 2018 GDP and population;
- capital: raw-NBS GFCF Track-A PIM, `delta_pim=.096`;
- `alpha_raw=alpha_used=.7380939146868483`;
- GDP and capital: `亿元 × 1000 → MU (10万元)`;
- population: `万人 × 100 → NU (100 persons)`;
- `L0=N0` with the explicit `population_proxy_NU` role;
- `Zt0=Y0/(K0^alpha*L0^(1-alpha))`;
- firm depreciation remains `.025`, separate from PIM depreciation;
- `GovInv0=Ktarget` is preserved using Track-A K in MU and labelled `SOURCE_FAITHFUL_INITIALIZATION_RULE__SCIENTIFIC_REDESIGN_PENDING`;
- the source-faithful diagnostic bridge remains `beta_a=1` and is labelled `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`;
- accepted static `rah0`, composite `w0`, clipped firm `ra0/wjt0`, firm `rk0`, and `mt0=.92` enter the repaired state;
- no Lt, GovInv controller, damping, hysteresis, price-bound, HJB/KFE, grid, or equation redesign was made.

The serialized runtime is checked again immediately after write and immediately before any future science. The validator binds the full 31-province input vector to an immutable canonical-content hash, verifies every active state against its corresponding typed input, and rejects missing sources, wrong order, wrong metadata, unit mismatch, any changed province input, and old-scale Anhui injection before a scientific launch marker can be written.

## Reconciliation

All 31/31 province assertions passed. The deterministic reconciliation ledger is `reports/mp4c_python_runtime_input_binding_repair_20260910/runtime_reconciliation_31province.csv`.

For Anhui:

| object | rejected historical canonical | repaired active corrected route |
|---|---:|---:|
| K / GovInv | `1357314108201.3684` | `70182433.35888097 MU` |
| Zt | `0.0006934644495858679` | `1.681124916844091` |
| Y0 | historical route not active | `34010900 MU` |
| N0=L0 | historical route not active | `607600 NU` |
| alpha | legacy value not active | `.7380939146868483` |

The dedicated before/after receipt is `reports/mp4c_python_runtime_input_binding_repair_20260910/anhui_before_after_receipt.json`.

## Verification

- focused corrected-runtime and single/two/three/five-turn static tests: latest run `35 passed in 1.16s`;
- cumulative focused tests in this task: 6 processes, 189 cases executed;
- Python compile checks: 5 processes, pass;
- actual prepare/readback against the protected distance workbook: pass, 31/31;
- repository evidence manifest readback: 7/7 entries, pass;
- runtime payload canonical-content SHA-256: `DE1D2CD803A53252835892A298A2DEA6CF2F937E949AF1E7DC401BF85EE2F73B`;
- final report-package manifest SHA-256: `713E8942BD5D22B413E961C435EF9CB6175A90857BAEA3DC9CDF1418D665FE7C`.

One whole-suite collection attempt stopped before test execution with 14 pre-existing test-isolation/source-identity collection errors: historical tests import different bare modules named `common`, `core`, and `contract` into one interpreter, while several MP4B tests enforce an older standalone-oracle identity. These failures do not touch the repaired paths, and this task did not broaden scope to alter that historical test architecture. All task-focused tests pass.

## Call ledger and boundary

Scientific/model calls were all zero: MATLAB, household/HJB/KFE/control, firm runtime, `Lt_seperate`, root/Brent, outer turn, steady state, GE, annual, IRF, Results, and parameter tuning. No trajectory was started and no successor science was published.

The evidence package is `reports/mp4c_python_runtime_input_binding_repair_20260910/`; its manifest readback passed. The final external deterministic prepare root is `D:\ProjectTemp\ch5-python-runtime-binding-repair-evidence-20260910-002` and contains no scientific launch marker. The earlier `-001` root is a preserved preliminary deterministic packaging run.

This PASS is an implementation candidate only. It does not authorize a trajectory, steady state, Results, merge to main, or successor scientific task. The next gate is independent ChatGPT Reviewer ACCEPT/REJECT of the pushed candidate commit.
