# Chapter 5 two-asset HANK pre-P5 labor-curvature correction and MATLAB requalification report

## Terminal classification

`COMMON_FIXTURE_MATLAB_REQUALIFICATION_EXHAUSTED_NEEDS_REDESIGN__P5_BLOCKED`

All three pre-registered MATLAB qualification calls were consumed exactly once and none qualified. Each returned `convergent=false`, emitted `MATLAB:nearlySingularMatrix` from the stationary solve, and failed both non-collapse mass criteria. No Candidate 4 was created. Python and the companion rate were not run. P5 remains blocked.

## Live authority and continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Live start `origin/main`: `8c15a54a2cb242d72a5a5b3434e9a696f4a4fc0a`.
- Accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only <baseline> -- src tests`: empty (`PASS`).
- Final `origin/main`: the sole-report publication commit identified by the post-push read-back and final execution handoff; no scientific or test path is part of that commit.

## Protected identities

| object | SHA-256 | result |
|---|---|---|
| accepted `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS |
| accepted `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| production `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS |
| accepted `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | PASS |
| accepted external O1 helper | `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315` | PASS |

The O2 adapter was not loaded or executed. No third scientific adapter existed.

## Accepted labor-curvature correction

The accepted semantic mapping is:

`Python phi = 1 / MATLAB frisch_l`.

Python's labor policy has exponent `1/phi` and disutility exponent `1+phi`; MATLAB's labor policy has exponent `frisch_l` and disutility exponent `1+1/frisch_l`. Thus the corrected common native-curvature fields are:

- Python common-object metadata: `phi=5.0`;
- MATLAB scientific input: `frisch_l=0.2`.

Candidate 1 remains `phi=1`, `frisch_l=1`, for which the reciprocal mapping is exact.

## Corrected manifest and exact diff audit

- Predecessor manifest: 3479 bytes, SHA-256 `B06DDE32AD1FD7FADBB2DE41E7E5D5A3EC854908ED35F12CA91B0F161388353D`.
- Fresh corrected manifest: 3375 bytes, SHA-256 `90C2C5D02B9D19658254374F4A93AEA3F50E133827998B08039492CB2DBC91F6`.
- Machine-readable diff audit: SHA-256 `66A463558D2DA0CA7F08D3B54172BFF0EE1EB9AABD0645CA5083CBC5929D592D`.

The only scientific differences were:

```text
candidates[1].matlab_frisch_l: 5.0 -> 0.2
candidates[2].matlab_frisch_l: 5.0 -> 0.2
```

Here zero-based manifest indices 1 and 2 are Candidate 2 and Candidate 3. Python `phi=5` remained unchanged. Candidate 1 was exactly unchanged. Candidate 3 asset arrays, all other scientific fields, common productivity, qualification rules, run order, total/per-candidate budgets, and the `0.056` prohibition were unchanged. Metadata changes only replaced the obsolete failed labor-gate annotation with `LABOR_CURVATURE_MAPPING_CORRECTION_ACCEPTED`.

Candidate 3's exact 242-state grid passed static accepted MATLAB and Python `GridSpec` representability again without a model solve.

## Frozen candidates and execution counts

Common fields were `rho=0.05`, `ga=2`, `alphal=1`, `chi0=0.05`, `chi1=1`, `a_bar=0.5`, `rb=0.03`, `rah=0.055`, `w=1`, `tau=Tt=rb_gap=fixcost=fixcost2=0`, `z=[0.8,1.3]`, and `Q=[[-0.4,0.4],[0.3,-0.3]]`. The future companion `0.056` was recorded only.

| candidate | corrected labor fields | asset fixture | MATLAB calls |
|---|---|---|---:|
| C1 | `phi=1`, `frisch_l=1` | 5x5, `a=[0,2]`, non-borrowing `b=[0,5]` | 1 |
| C2 | `phi=5`, `frisch_l=0.2` | same as C1 | 1 |
| C3 | `phi=5`, `frisch_l=0.2` | 11x11, `a=[0,10]`, `b=[-2,5]` | 1 |

Python HJB/KFE/steady-state calls: 0. MATLAB `0.056` calls: 0. Final four-run parity calls: 0.

## Qualification diagnostics

| diagnostic | C1 | C2 | C3 |
|---|---:|---:|---:|
| `convergent` | false | false | false |
| exposed arrays finite | PASS | PASS | PASS |
| mass sum | 1.0 | 0.9999999999999999 | 1.0 |
| mass-sum tolerance `1e-10` | PASS | PASS | PASS |
| minimum mass | `-0` | `-6.77170298591294e-17` | `-0` |
| minimum-mass bound `-1e-12` | PASS | PASS | PASS |
| warning ID | `MATLAB:nearlySingularMatrix` | same | same |
| RCOND | `1.374549e-18` | `3.532290e-17` | `6.163991e-18` |
| no singular warning | FAIL | FAIL | FAIL |
| mass with `a>a_min` | `3.597150307933341e-18` | `-8.151150824989983e-17` | `2.435097097418892e-17` |
| `a` non-collapse bound `1e-4` | FAIL | FAIL | FAIL |
| mass with `b>b_min` | `8.654495811367200e-18` | `-3.350798277858479e-16` | `8.007831909394330e-17` |
| `b` non-collapse bound `1e-4` | FAIL | FAIL | FAIL |
| required aggregates finite | PASS | PASS | PASS |
| disposition | `NOT_QUALIFIED` | `NOT_QUALIFIED` | `NOT_QUALIFIED` |

Machine-scale negative derived masses in C2 reflect signed stationary-solve roundoff; they do not approach the required positive `1e-4` non-collapse threshold.

Qualification-only aggregates:

| candidate | C_hh | H_hh | L_hh | A_hh | B_hh |
|---|---:|---:|---:|---:|---:|
| C1 | 1.0479665172331991 | 0.9832761101143030 | 1.0479665172331991 | `2.942921525341106e-18` | `1.752093011129456e-17` |
| C2 | 1.0686290437333000 | 0.9920188642913241 | 1.0686290437333004 | `-6.669190884076708e-17` | `-7.119044331694946e-16` |
| C3 | 1.0260994320788104 | 1.0090738541012512 | 1.0860994320788104 | `7.205214289403434e-17` | -2.0 |

C3's `B_hh=-2` is the exact lower liquid bound and confirms complete lower-bound collapse despite restored borrowing support and wider resolution. These values are failure diagnostics, not parity evidence.

## Persistence and external artifacts

External root:

`D:\ProjectTemp\ch5-pre-p5-labor-mapping-requalification-artifacts-20260829-184433`

The final harness was statically clean and frozen before the first HJB call. An earlier JSON cell/struct container read failed before any attempt marker or HJB call; only that external container access was corrected, then the harness was rechecked and refrozen. No candidate or scientific field changed.

| artifact | bytes | SHA-256 |
|---|---:|---|
| final `run_candidate.m` | 6893 | `C4D6EEA69444369312C25D058AF400E8C10AE3B8FC78DD1C1F07E8645607D49E` |
| `verify_manifest_diff.py` | 2856 | `E25D5F8ECCC736AF3AB0F48396151867009EAC545BFFEB2CE423849F4EDD9151` |
| `initial_C1.mat` | 1811 | `9204A8201BB017507DB17F2C642471CAABD68EC2C08E7E2E9D55B342AD534553` |
| `raw_C1.mat` | 2888 | `216E7A122520D9C8DCBF26303A75C4BD5DEADBB504028FD909C53244699795E8` |
| `summary_C1.json` | 1137 | `B2309319CA90BE17037DDD478401CD659A244A61A3865B13423F00C860AE7FA1` |
| `initial_C2.mat` | 1785 | `7455435B3D6F098136DDCA76DC85F0B70195357F02232E28A0C847E8536B85F9` |
| `raw_C2.mat` | 3015 | `3D73750F8205BFA1861939C447D48280D07A26452D45A32FE67DC45233A8B69B` |
| `summary_C2.json` | 1182 | `BDFBDC5984EEF7346684D44C21265CA5AB119E92EACF7D507D190F54E69A8D73` |
| `initial_C3.mat` | 5079 | `DDB8D8CB5ECEEB5DA3488288C6661E2917837C8697E64225E4466C1871F54510` |
| `raw_C3.mat` | 6966 | `0F234F067B6BE20C107A4B941FD6532CE47C4952B30488668CE4C5A481AE6659` |
| `summary_C3.json` | 1122 | `DBECED7EB20B0AB473A8BC4CDD511451690B119E46E552B3EDB68CD0F294495D` |

Every returned raw output was saved immediately after its HJB call and read back before summary transformation and before starting the next candidate. Manifest, harness, O1 helper and accepted-source identities remained unchanged across all three scientific calls.

## Files read and written

Read: live task and governance files; predecessor task/report; current handoff; failed rate-matched execution report; structural authority and accepted P3/P4 reports; snapshot-authority report; accepted Python labor/grid source; accepted MATLAB HJB/cost/FOC/labor helper; predecessor external manifest.

Repository write: only this report.

External writes: fresh corrected/predecessor manifests, diff verifier/audit, exact O1 copy, final MATLAB harness, three attempt markers, three rate-matched initialization MAT files, three raw result MAT files, and three JSON summaries. No cache, source, test, repository binary, or Python bytecode was written.

## Forbidden-operation check

- accepted Python `src/tests` modified: no.
- MATLAB production source modified: no.
- diagnostic-patch tree/cache modified or executed as HJB source: no.
- third scientific adapter added: no.
- P1-P4 rerun: no.
- Python HJB/KFE/steady state run: no.
- MATLAB `0.056` run: no.
- final four-run parity entered: no.
- candidate edited after first scientific call: no.
- adjustment parameters, common productivity, other inputs, grids, solver or tolerances changed after results: no.
- Candidate 4 created: no.
- outer equilibrium/turn/shock/multi-province, AR(1), transition, IRF, calibration extension, dynamics or Results entered: no.
- MATLAB-Python parity or P5 acceptance inferred: no.

## Acceptance level and recommended next gate

Acceptance level: the corrected reciprocal labor mapping and bounded MATLAB requalification are complete, but **no common fixture qualified**. P5 remains explicitly **BLOCKED**. The final same-input four-run parity task is not recommended and was not consumed.

The native adjustment tuple `(chi0=0.1, chi1=2, a_bar=1e-6)` remains a plausible audited redesign dimension because it differs materially from the exhausted synthetic tuple `(0.05,1,0.5)`, but this task did not isolate it and does not authorize Candidate 4.

Recommended next gate:

`CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_ADJUSTMENT_TECHNOLOGY_AND_BOUNDARY_DEGENERACY_REDESIGN`

That Owner/reviewer gate must pre-register a new bounded candidate set and fresh call budget before any additional scientific run. It must not jump to final parity or P5.
