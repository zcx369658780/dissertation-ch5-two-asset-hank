# MP4B Python full-initialization preflight and one-shot report

Date: 2026-08-31

## Terminal verdict

`MP4B_PYTHON_ONLY_CALENDAR2009_STATIONARY_SCIENTIFIC_FAILURE_AFTER_FULL_INIT_PREFLIGHT`

All zero-science and pre-science gates passed. The sole authorized Python
stationary invocation then failed in the first province household HJB before
one household result was returned. No repair or rerun occurred.

## Continuity and accepted authority

- live task/HEAD/origin-main at start:
  `c729f89d08dcf9b83a8d9844860a619f6e25c3a6`
- direct parent / accepted scalar parity:
  `199261016e2a1b7382c28b112ec258eca07b029a`
- preserved marker:
  `MP4B_INITIAL_LABOR_PYTHON_MATLAB_FROZEN_CELL_ROOT_PARITY_PASS`
- canonical input SHA-256:
  `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`
- standalone oracle SHA-256:
  `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`
- comparison contract SHA-256:
  `5F8CDA18F09325CC7A5821FADFB26AFB647DA50088B2055F8B5D4F5AF11A0969`

## Bootstrap and presolver gates

Direct command:

`python validators\multi_province\mp4b_python_empirical.py --bootstrap-check D:\ProjectTemp\ch5-mp4b-full-init-bootstrap-smoke-20260831-001\bootstrap_manifest.json`

Bootstrap manifest SHA-256:
`DEC8775DFD403BACA8EA80B3CE39BA1E39EA495123619AA5BABF587236FEB3A5`.
It records exact current repository/module origins, accepted oracle identity,
no forbidden runtime, and scientific calls zero. Marker established:
`MP4B_PYTHON_DIRECT_SCRIPT_BOOTSTRAP_SMOKE_PASS`.

Fresh Python presolver reconstruction was recursively compared with the
accepted MATLAB presolver manifest. Semantic mismatch count: `0`. Marker:
`MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`.

## Full first-turn source initialization

A validation-only direct entry mode loops in the scientific entry's exact
`province,k,j,i` order across 31 provinces and the `20*20*2` grid. It calls only
the accepted `_source_labor_root` and source-identical `c0`/`v02` arithmetic.
It does not call household, HJB, KFE, MP2, MP3, or the stationary controller.

Root:
`D:\ProjectTemp\ch5-mp4b-full-init-preflight-20260831-001`.
Manifest SHA-256:
`36C1DA1F1BEABD857BA54417A168CB8CA17FC0F984FF50627F12652220980A8B`.

| check | result |
|---|---:|
| checked / expected cells | `24,800 / 24,800` |
| first failure | none |
| maximum source residual | `5.773159728050814e-15` |
| minimum `c0` | `10.24466389968385` |
| minimum root base | `10.251666835735994` |
| `v02` range | `[-2.2796313738283325,-1.4773664265733266]` |
| household/HJB/KFE/MP2/MP3/stationary calls | all `0` |

Every source `x0`, bracket endpoint and root was finite and strictly inside the
open real domain; every `c0` was strictly positive and every `v02` finite/real.
No clipping, epsilon substitution, NaN replacement, formula substitution or
alternate solver was used. Marker established:
`MP4B_PYTHON_FULL_FIRST_TURN_SOURCE_INITIALIZATION_PREFLIGHT_PASS`.

## Pre-science gate and preserved MATLAB evidence

Python compile, direct bootstrap/initial-labor tests, MP3 seven-scenario tests,
online runtime regression and diff checks passed: `40 passed`. Oracle, MP2,
MP3, stationary runtime and comparison-contract identities were unchanged; no
active R5 import existed; the fresh run root was absent and D drive had about
76.2 GB free. Marker established:
`MP4B_PYTHON_ONLY_CALENDAR2009_SCIENTIFIC_EXECUTION_PREFLIGHT_PASS`.

The immutable MATLAB root remained
`D:\ProjectTemp\ch5-mp4b-fresh-calendar2009-matlab-20260830-001`.
Read-only hashes passed:

- output: `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B`
- profile: `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C`
- terminal: `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270`
- status/outer turns/household calls: `COMPLETED / 184 / 5704`; final flags `31/31`.

## Sole Python scientific invocation

Run root:
`D:\ProjectTemp\ch5-mp4b-python-only-calendar2009-full-init-20260831-001`.

The run entered outer turn 1 and the first Beijing household. Initial-array
construction completed, but `select_matlab_faithful_local_policy` raised
`ValueError: designated transfer FOCs require positive liquid derivatives`
inside HJB policy selection. No household solve returned.

| artifact | SHA-256 |
|---|---|
| run manifest | `030A4241D4FB7A8CFA5370811FC4502028A61E46521F9329D7768B45278F6774` |
| turn-1 household inputs | `79B7A2805ECBAACDFCC70FA194E154263FA46EE313415A7060F90C65662DCE28` |
| turn-1 household failure | `D9E93BCFFC69221354E5819CD0BCEDFBC5A52F22C6D5DA63BB188C4C74A435F6` |
| terminal summary | `BBFFF4AA66E2B9D052FA0C300A760599E7D87A783A49AC67FAAFFE45FB93FE8B` |

Status is `ERROR`, converged is false, outer turn reached is 1, completed
households and recorded household calls are `0/0`, and scientific reruns are 0.

## Comparison and first divergence

Presolver, scalar root parity and the complete first-turn initialization layer
pass. The first supported divergence is the Python HJB local-policy layer's
positive-liquid-derivative admissibility guard for the first Beijing household.
Classification: `PYTHON_IMPLEMENTATION_ERROR` in the current Python scientific
route relative to the same-input preserved completed MATLAB route. Exact
derivative cell/value evidence is not exposed by the present failure artifact,
so deeper localization is observability-limited and this classification does
not authorize repair.

Python produced no household output or final state. Consequently province and
national final differences, household convergence comparisons, boundary/
clipping categories and ranking diagnostics are unavailable. Preserved MATLAB
per-cell/per-iteration derivative traces are also unavailable; MATLAB was not
rerun. Material mismatch list: HJB liquid-derivative admissibility failure.
Unresolved residual: exact first offending derivative/state/policy candidate.
Infrastructure and environment failure lists: empty.

## Call ledger and forbidden operations

| operation | count |
|---|---:|
| bootstrap/full-init validation scalar work | 24,800 cells, model calls `0` |
| Python stationary top-level | `1` |
| completed Python household calls | `0` |
| Python scientific rerun | `0` |
| MATLAB stationary/HJB/KFE/multi-province/scalar | `0` |
| wrong-year/batch/shocks/transition/dynamics/IRF/R5/Results | `0` |

No protected MATLAB, accepted oracle/HJB/KFE, MP2, MP3, runtime, canonical
input, comparison contract or preserved MATLAB artifact was modified.

## Exactly one recommended next gate

Authorize one observability-only, zero-scientific-rerun diagnostic that exposes
the exact first Beijing HJB liquid derivative and local-policy candidate inputs,
and compares their semantics with protected MATLAB source; keep all stationary
reruns closed.
