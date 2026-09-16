# Chapter 5 MP4C 2018 KFE D1-D3 corrected diagnostic contract implementation and static validation

Date: 2026-09-16

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Verdict

`PASS__OWNER_ADOPTED_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTED_IN_ISOLATION__STATIC_AND_SAVED_CONTROL_VALIDATION_PASS__ZERO_SCIENCE`

This PASS is limited to isolated contract implementation, synthetic arithmetic, and hash-bound saved-control assembler checks. It is not a real-cell selector validation, HJB/KFE result, MATLAB parity claim, production replacement, or Results authority.

## Git and scope identity

- Fresh-fetched `origin/main`: `5360df95aae2bdb6a77032c35bf2276720803e8d`.
- Branch: `codex/ch5-mp4c-2018-kfe-d123-corrected-diagnostic-contract-static-validation-20260916`.
- Candidate SHA: assigned by the immutable Git commit and reported by the final non-force-push readback; a commit cannot embed its own SHA without changing that SHA.
- Corrected authority identifier: `CH5_MP4C_2018_KFE_D123_OWNER_ADOPTED_20260916`.
- State association: `(b,a,z)`, F-order, matching the accepted saved-control evidence.

Exact changed paths:

1. `src/ch5_two_asset_hank/corrected_diagnostic/__init__.py`
2. `src/ch5_two_asset_hank/corrected_diagnostic/contracts.py`
3. `src/ch5_two_asset_hank/corrected_diagnostic/boundary.py`
4. `src/ch5_two_asset_hank/corrected_diagnostic/cost.py`
5. `src/ch5_two_asset_hank/corrected_diagnostic/generator.py`
6. `src/ch5_two_asset_hank/corrected_diagnostic/saved_controls.py`
7. `tests/test_mp4c_2018_kfe_d123_corrected_diagnostic_contract.py`
8. `reports/ch5_mp4c_2018_kfe_d123_corrected_diagnostic_static_validation_20260916/static_validation_results.json`
9. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_REPORT.md`

No existing production or source-faithful file was edited.

## Isolation from the frozen reference

The implementation exists only under `src/ch5_two_asset_hank/corrected_diagnostic/`. It does not import a household selector, HJB loop, KFE solver, outer loop, firm block, wage/return block, or MATLAB bridge. The saved-control loader reads only grids, persisted total drifts and provenance hashes.

The following frozen-reference identities remain unchanged from fresh main:

| Path | SHA-256 | Git blob |
|---|---|---|
| `exports/matlab_faithful_two_asset_ha.py` | `F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8` | `e144c645d3f4dc842c2faa6b93b2ba0e24275dcf` |
| `src/ch5_two_asset_hank/matlab_faithful_hjb.py` | `6CF6292C71488601CFB8D6A8BFB8C85868A3C3FE281794DCF6B5398F363FFA61` | `e06f9871b361c8e1c8df7aab5c43c2dbd3b09b50` |
| `src/ch5_two_asset_hank/matlab_faithful_kfe.py` | `4A0C2734D5C5AF73448C0C3D18F34EB1786DECC7E32A20854FB862A401813ABD` | `4ccb7cec8c4754e91bd8830a95dc533811784391` |

This corrected target is not called MATLAB parity. The frozen reference and its accepted failure evidence remain intact.

## D1-D3 implementation map

| Contract | Code objects | Implemented meaning |
|---|---|---|
| D1 state constraints | `CorrectedDiagnosticGrid`; `assess_state_constraints`; `require_state_constraints`; `ClosedFaceOutwardDriftError` | All four asset faces are checked jointly. Lower faces remain labelled `economic_lower_bound`; artificial upper faces are labelled `artificial_upper_state_constraint`. Inward and tangent drifts pass. Every outward closed-face drift, including a dual-upper corner, is reported and rejected; no drift is clipped and no edge is silently deleted. |
| D2 conservative assembly | `assemble_consumed_drift_generator`; `CorrectedGenerator` | Uses only consumed total `mu_b/mu_a`, actual adjacent-node distances, and nonnegative retained rates. The diagonal is the negative retained outgoing-rate sum. An optional independently supplied conservative `z_generator` is validated and lifted without changing asset drifts. `(b,a,z)` F-order is explicit. |
| D3 regularized cost/KKT | `regularized_scale`; `regularized_adjustment_cost`; `regularized_adjustment_cost_subgradient`; `check_transfer_kkt` | Cost and derivative share `s(a)=max(a,a_bar)` for the whole domain. Positive, negative and zero-transfer kink branches implement `0 in q_a-q_b*(1+partial_d C)`. `q_b<=0` fails; there is no derivative floor, transfer cap, new coefficient or different technology. |
| Saved-control intake | `load_saved_control_set`; `SavedControlSnapshot`; `SavedControlProvenance` | Loads only the accepted 14 primary MAT/NPZ files after exact byte-count and SHA-256 verification against the accepted consumed-input receipt. It never calls a selector or solver. |

## Synthetic validation matrix

| Area | Cases | Outcome |
|---|---|---|
| D1 upper faces/corner | upper-`a`, upper-`b`, dual-upper corner | Both outward components at the corner are independently reported; all outward cases fail closed. |
| D1 active/slack/tangent | lower economic faces, upper numerical faces, inward and zero drift | Inward/slack and tangent/zero cases pass; boundary kinds remain distinct. |
| D2 rates and distances | nonuniform `b=[-2,-.5,1]`, `a=[0,.25,2]`; inward/forward/backward drifts | Rates use actual adjacent distances; minimum retained offdiagonal is `0.05714285714285715`; all offdiagonals are nonnegative. |
| D2 diagonal and closure | asset rates plus a conservative two-state productivity generator | Diagonal-construction error=`0.0`; `max(abs(Q@1))=1.1102230246251565e-16`, below prospective operation-count bound `4.973799150320706e-15`. |
| D2 coordinate action | same nonuniform fixture | Maximum liquid-coordinate error=`2.220446049250313e-16`; illiquid-coordinate error=`1.942890293094024e-16`. |
| D2 smallest outward sign | `nextafter(0,+1)` at upper `b` | Explicitly rejected before assembly; no tolerance silently admits an outward closed-face input. |
| D3 regularization locations | `a=0`, `.25<a_bar`, `a=a_bar=.5`, and `a=2>a_bar` | Cost, subgradient and KKT use scales `.5,.5,.5,2` respectively. |
| D3 transfer branches | positive, negative and exact zero kink | All on-target cases pass; an outside-kink target fails with the expected residual; nonpositive `q_b` is rejected without a floor. |

## Saved-control assembler-only validation

Provenance is exact and recovered, so `NOT_RECOVERED` does not apply:

- accepted snapshot manifest: `reports/call725_boundary_generator_repair_spec_20260907/snapshots.json`, SHA-256 `0F6E4BB3D852CF12880F9874BCE3BE1981341F0A6F6D337DC8B8885368932EC7`;
- accepted consumed-input receipt: `reports/call725_boundary_generator_repair_spec_20260907/consumed_inputs.json`, SHA-256 `D71F67CC840E98ECF109361A42ABC962844CFE18ABA86CAE77DB2CD08A40C526`;
- 14/14 primary files exist and individually match their accepted SHA-256 and byte counts.

| Snapshot group | Objects | Exact face violations per object | Corrected assembler outcome |
|---|---:|---|---|
| MATLAB/Python M24 | 2 | upper-`b` 12 + upper-`a` 18 = 30 | rejected before assembly, 2/2 |
| MATLAB/Python P24 | 2 | upper-`b` 12 + upper-`a` 18 = 30 | rejected before assembly, 2/2 |
| MATLAB/Python P32 | 2 | upper-`b` 17 + upper-`a` 15 = 32 | rejected before assembly, 2/2 |
| MATLAB/Python M143_FINAL | 2 | upper-`b` 2 + upper-`a` 18 = 20 | rejected before assembly, 2/2 |
| MATLAB trajectory 52 | 1 | upper-`b` 22 + upper-`a` 22 = 44 | rejected before assembly |
| MATLAB trajectory 57 | 1 | upper-`b` 23 + upper-`a` 19 = 42 | rejected before assembly |
| Python trajectory 146 | 1 | upper-`b` 2 + upper-`a` 12 = 14 | rejected before assembly |
| Python trajectory 401 | 1 | upper-`b` 2 + upper-`a` 11 = 13 | rejected before assembly |
| Python trajectory 424 | 1 | upper-`b` 2 + upper-`a` 12 = 14 | rejected before assembly |
| Python trajectory 500 | 1 | upper-`b` 2 + upper-`a` 12 = 14 | rejected before assembly |

Aggregate exact face violations are lower-`b`=`0`, upper-`b`=`139`, lower-`a`=`0`, upper-`a`=`226`, total=`365`. These are exact sign counts on persisted consumed drifts, not new scientific evaluations. All 14 saved controls are invalid inputs to the adopted closed-box assembler and are rejected as intended. No projection, clipping, selector call, repaired drift, or generator/KFE solve was attempted.

Full per-snapshot SHA-256, byte identity and outcome rows are in `reports/ch5_mp4c_2018_kfe_d123_corrected_diagnostic_static_validation_20260916/static_validation_results.json`.

## Checks and commands

Final focused command:

`python -m pytest -q tests/test_mp4c_2018_kfe_d123_corrected_diagnostic_contract.py tests/test_call725_boundary_generator_repair_spec.py tests/test_generators_and_kfe_contract.py`

Outcome: `24 passed in 1.12s`.

Static compilation command:

`python -m py_compile src/ch5_two_asset_hank/corrected_diagnostic/__init__.py src/ch5_two_asset_hank/corrected_diagnostic/contracts.py src/ch5_two_asset_hank/corrected_diagnostic/boundary.py src/ch5_two_asset_hank/corrected_diagnostic/cost.py src/ch5_two_asset_hank/corrected_diagnostic/generator.py src/ch5_two_asset_hank/corrected_diagnostic/saved_controls.py tests/test_mp4c_2018_kfe_d123_corrected_diagnostic_contract.py`

Outcome: `PASS`.

Two pure public-API diagnostics were also used: one loaded and hash-checked all 14 saved controls and emitted the compact rejection table; one emitted the nonuniform synthetic generator metrics sealed in the evidence JSON. TDD RED attempts were limited to expected missing-module/missing-interface failures. One standalone diagnostic initially failed only because `src` was not on the direct `python -c` import path and then passed after an explicit local `sys.path` insertion. None was a scientific or solver call.

## Exact zero-call ledger

| Category | Calls |
|---|---:|
| real selector/evaluator | 0 |
| HJB iterations/solves | 0 |
| KFE solves | 0 |
| outer loop | 0 |
| firm block | 0 |
| wage/return recalculation | 0 |
| MATLAB | 0 |
| GE | 0 |
| annual/downstream production | 0 |
| shock | 0 |
| IRF | 0 |
| Results | 0 |

No matrix solve, root solve, optimizer, real policy map, drift repair, or scientific retry occurred.

## Limitations and next permitted gate

This gate proves only that the adopted D1-D3 contracts exist separately and behave as specified on synthetic arithmetic and saved-control assembler inputs. It does not prove that a corrected selector can produce admissible real-cell controls, that the HJB converges, that a stationary KFE density exists or is nonnegative/unique, that a pin equation is redundant, or that production/GE/annual/IRF/Results are valid.

After independent Reviewer acceptance, the next permitted gate is the separately budgeted preregistered tiny real-cell corrected-target selector panel. This task does not publish that successor and does not authorize one target HJB step or any KFE solve.

Results eligibility=`FALSE`.
