# MP4B Python bootstrap repair and Python-only calendar-2009 report

Date: 2026-08-30

## Terminal verdict

`MP4B_PYTHON_ONLY_CALENDAR2009_STATIONARY_SCIENTIFIC_FAILURE`

The direct-script bootstrap defect is repaired and all four pre-science gates
passed. The sole authorized Python stationary invocation then failed during the
first household's source-initial-array construction. It produced no completed
household result and no final provincial or national state. No scientific repair
or rerun was attempted.

## Continuity and preserved authority

- live task/HEAD/origin-main at start: `4fbc4aa9362ca6b88931187919b28ed6d7d0318e`
- direct parent: `92379b704f74ecb13eaedc0f080a71132882efe8`
- canonical 2009 input SHA-256: `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`
- standalone oracle SHA-256: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`
- comparison contract SHA-256: `5F8CDA18F09325CC7A5821FADFB26AFB647DA50088B2055F8B5D4F5AF11A0969`

The immutable MATLAB root is
`D:\ProjectTemp\ch5-mp4b-fresh-calendar2009-matlab-20260830-001`.
Read-only rehashing passed:

- stationary output: `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B`
- profile: `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C`
- terminal JSON: `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270`
- status/turns/household calls: `COMPLETED / 184 / 5704`; final household flags `31/31` true.

## Bootstrap audit and exact repair

Root cause: direct-file invocation placed only the validator directory on
`sys.path`, while `exports.matlab_faithful_two_asset_ha` requires repository root
and `ch5_two_asset_hank` requires repository `src`.

| Import | Required root | Resolution |
|---|---|---|
| `exports.matlab_faithful_two_asset_ha` | current repository root | exact oracle path plus frozen SHA check |
| `ch5_two_asset_hank` | current repository `src` | package origin required beneath exact `src` |
| validator/test modules | none at runtime | not added |
| historical R5 / `chapter5_model` | forbidden | no path or import |

The entry now derives both roots only from `Path(__file__).resolve()`, validates
the repository layout and oracle identity before repository-local imports, adds
only those two finite roots, verifies resolved module origins, and fails closed.
`--bootstrap-check` writes one no-overwrite identity manifest and returns without
calling household, HJB/KFE, MP2, MP3, or stationary functions.

Markers established:

- `MP4B_PYTHON_DIRECT_SCRIPT_BOOTSTRAP_SCOPE_COMPLETE`
- `MP4B_PYTHON_DIRECT_SCRIPT_BOOTSTRAP_SMOKE_PASS`
- `MP4B_PYTHON_BOOTSTRAP_REPAIR_STATIC_AND_DIRECT_SMOKE_REVIEW_PASS`
- `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

Formal smoke command:

`python validators\multi_province\mp4b_python_empirical.py --bootstrap-check D:\ProjectTemp\ch5-mp4b-python-bootstrap-smoke-20260830-001\bootstrap_manifest.json`

Manifest SHA-256:
`DEC8775DFD403BACA8EA80B3CE39BA1E39EA495123619AA5BABF587236FEB3A5`.
It records the exact repository/oracle/package paths, accepted oracle SHA,
empty forbidden imports, and `scientific_model_calls: 0`.

Fresh Python reconstruction was compared recursively with the accepted fresh
MATLAB presolver manifest. Semantic mismatch count: `0`.

## Scientific invocation and preserved failure

Ledger for this task:

| Call | Count |
|---|---:|
| MATLAB stationary / HJB-KFE | 0 / 0 |
| Python stationary top-level | 1 |
| Python scientific rerun | 0 |
| completed Python household calls | 0 |

Python root:
`D:\ProjectTemp\ch5-mp4b-python-only-calendar2009-20260830-001`.

The run entered outer turn 1 and persisted its 31-province household-input
snapshot. While constructing the first household initial arrays,
`_source_initial_arrays` evaluated the labor equation at `l=0`; for a negative
liquid-asset state the consumption base was negative, so the fractional power
returned NaN and `scipy.optimize.brentq` raised:
`ValueError: The function value at x=0.0 is NaN; solver cannot continue.`

Terminal status is `ERROR`, converged is false, completed households are `0`,
household-call count is `0`, and no iteration result exists. Evidence hashes:

- run manifest: `030A4241D4FB7A8CFA5370811FC4502028A61E46521F9329D7768B45278F6774`
- terminal summary: `A7CAE3615A798E6430C9042F04F66BDE3C69835B40CF71AE7225BFF1AEAFDAD3`
- turn-1 failure: `2547B92C2BA585D87CDC650961F4BEDAD86DCA2E8DA2643AB0EC1F9B89FC358D`
- turn-1 inputs: `79B7A2805ECBAACDFCC70FA194E154263FA46EE313415A7060F90C65662DCE28`

## Comparison and diagnosis

Presolver equality and process/bootstrap identity are exact. The first supported
divergence is Python-only initial-labor construction before the first household
solver call. Classification: `PYTHON_IMPLEMENTATION_ERROR` in validation-entry
initialization/domain handling; this classification does not authorize a repair.

Because Python produced no household output or final state, MATLAB-versus-Python
provincial/national numerical differences, wage-bound categories, rankings, and
boundary comparisons are unavailable. The preserved MATLAB descriptive anchors
remain `sum Ct=283.3909431582526`, `sum At=47.95553248807161`,
`sum Bt=65.2831672243048`, `sum Yt=350556701.89460325`, and wage-bound
upper/lower counts `7/17`; they are not a two-route parity result. Preserved MATLAB
per-turn traces needed for deeper upstream localization are also unavailable and
MATLAB was not rerun.

Material mismatch list: Python initial-labor domain failure. Unresolved scientific
residual: source-faithful admissible-domain/root semantics for that initialization.
Environment/source failure list: empty.

## Checks, forbidden operations, and closeout

- Python compile: PASS
- focused bootstrap, MP3 seven-scenario, and online stationary tests: `27 passed`
- direct subprocess smoke from explicit direct-file entry: PASS
- no-overwrite behavior: PASS
- `git diff --check`: PASS
- forbidden operations: MATLAB rerun 0; wrong-year/batch/shocks/transition/
  dynamics/IRF/R5/Results 0; protected scientific source modifications 0;
  scientific repair/rerun after failure 0.

Changed repository paths are limited to the bootstrap entry, focused test, this
report, and the CURRENT roadmap. Final commit/push/read-back evidence is recorded
in the execution handoff after closeout.

## Exactly one recommended next gate

Publish one bounded Python initial-labor admissible-domain and MATLAB-source
semantics diagnosis/repair gate, with a separately authorized Python one-shot
budget and no MATLAB rerun.
