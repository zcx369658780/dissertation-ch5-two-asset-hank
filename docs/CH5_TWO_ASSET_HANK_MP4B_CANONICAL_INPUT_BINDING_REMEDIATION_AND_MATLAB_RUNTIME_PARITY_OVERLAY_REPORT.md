# MP4B canonical-input binding remediation and MATLAB runtime-parity overlay

## Terminal verdict

`MP4B_CANONICAL_INPUT_BINDING_REMEDIATION_AND_MATLAB_RUNTIME_PARITY_OVERLAY_PASS`

Established markers:

- `MP4B_PRIMARY_SOURCE_CANONICAL_BINDING_PRESERVED`
- `MP4B_DUAL_INPUT_AUTHORITY_CONTRACT_FROZEN`
- `MP4B_MATLAB_CACHE_RUNTIME_PARITY_OVERLAY_PREPARED`
- `MP4B_CACHE_OVERLAY_VALIDATION_ONLY_NO_SCIENTIFIC_DEFAULT_CHANGE`

This is a zero-model-execution validation-input binding remediation. It does
not establish stationary parity, causal attribution, scientific superiority of
the cache representation, or any Results claim.

## Live continuity and immutable evidence

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Live task authority / execution-start `HEAD` / `origin/main`:
  `0df0c711f52d029110bc47833109e28dd719f341`.
- Required direct parent: `a7ee476dbe16e8dfc71cebc9216ad92fd28c5ab0`; verified.
- Fresh fetch followed by fast-forward-only synchronization, clean entry
  worktree, `HEAD == origin/main`, and ahead/behind `0/0`: PASS.

The immutable primary canonical JSON remains at
`D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json`, SHA-256
`507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.
The accepted derived MATLAB runtime cache remains SHA-256
`923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`.
The predecessor all-province census and its audit manifest re-hashed to
`6AF998BE7F5BFA996AD683FE2ACF162561A8DFC2007E333F9C00532CEE55655E`
and `D1F1579E00D15F9821E47F68C226FAABDA91FF81848293E5233A753AED2D9079`.

## Dual-binding contract

`PRIMARY_SOURCE_CANONICAL` remains the default scientific/provenance mode. It
requires the immutable canonical SHA and preserves the original canonical bytes
and object exactly.

`MATLAB_CACHE_RUNTIME_PARITY_OVERLAY` is validation-only. It requires an
explicit `BindingMode` enum and explicit accepted census evidence; missing mode,
wrong SHA, missing overlay evidence, or an attempt to provide overlay evidence
to primary mode fails closed. It begins with the canonical object and replaces
only `vectors.initialized_zt` with cache binary64 values. No implicit fallback
between modes exists, and no current stationary driver/default was changed.

The overlay's all-province invariant is exact: 24 equal rows, 7 replacement
rows, five 1-ULP rows, and two 2-ULP rows. Every overlay value is verified
bitwise against the accepted cache evidence; every non-`initialized_zt` path
and the 31-province order remain bitwise/structurally identical. The seven
actual changed paths are indices 1, 12, 13, 15, 18, 23, and 25 (zero-based).

## Validation implementation and focused tests

Changed validation-only paths:

- `validators/multi_province/mp4b_canonical_input_binding.py` — standard-
  library-only modes, SHA gates, cache-evidence loader, overlay constructor,
  binary64/ULP validator, and no-overwrite external-package writer.
- `tests/test_mp4b_canonical_input_binding.py` — focused non-scientific test
  matrix.
- this report.

No `src/` production/scientific module, canonical input, MAT cache, MATLAB,
household adapter, MP2, MP3, controller, comparator contract, or tolerance was
modified.

`python -m py_compile validators/multi_province/mp4b_canonical_input_binding.py tests/test_mp4b_canonical_input_binding.py`: PASS.

`python -m pytest -q tests/test_mp4b_canonical_input_binding.py`: `7 passed`.

The focused matrix covers exact canonical/cache SHA gates; primary byte/field
preservation; explicit-mode/default rules; Mode-B-only `initialized_zt` change;
the exact 24/7 and 5x1-ULP/2x2-ULP census; exact cache hex values; unchanged
rows; non-Zt mutation and province permutation failure; missing/wrong evidence;
external no-overwrite behavior; and static absence of scientific runtime imports
or calls.

## External no-overwrite package

Fresh root:
`D:\ProjectTemp\ch5-mp4b-canonical-binding-remediation-20260901-001`.

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `binding_contract.json` | 860 | `B29A0D403C8182ADEA6159EFA03337FBF9FF1BABE523290CAF1ED24AF741B820` |
| `matlab_cache_runtime_overlay.json` | 57,131 | `072E5E943FB6BFF6768CD40001B031C3AF1A6DD92FCC3A86E1B6D476E03E0137` |
| `initial_zt_31province_hex_ulp_table.json` | 12,817 | `8207AB733AE5C007E1A83A94A209D61C6F3C1CF9F6F379E82CD32471BECC155F` |
| `canonical_vs_overlay_field_identity.json` | 1,795 | `92033F470C833300D50CC3AD3BF401BE7807666FE8D3E51E64CD1B429C6BEEE7` |
| `focused_test_results.json` | 300 | `59113A5CC019DCC79C16402A47836526373AA0B26DB6DF6C86DA440FA12B6B82` |
| `remediation_manifest.json` | 1,710 | `3009D72CFDEF06CD2BEEB0A29FED6357E07A047F646481A9410B1FC860A4D877` |

The derived 31-value cache vector is external-only and was not committed as
project data.

## Zero-model and forbidden-operation audit

MATLAB processes/checkcode/stationary/HJB/KFE/household/firm/controller: `0`.
Python stationary/HJB/KFE/household/MP2/MP3: `0`. Comparator and standalone
household replay: `0`. Other years/batch, shocks/AR1, transition/dynamics/IRF,
historical R5, and Results: `0`.

No model call was imported or invoked by the helper or focused tests. The only
operations were immutable hashing/JSON reads, standard-library binary64
comparisons, validation construction, focused tests, and external artifact
serialization.

Before closeout, `git diff --check` is run on actual staged content. The task
authorizes exactly one explicit-path commit, non-force push, fresh GitHub
read-back, `HEAD == origin/main`, ahead/behind `0/0`, and a clean worktree.

## Exactly one recommended next gate

Separately authorize one Python-only corrected-calendar-2009 stationary one-shot
under `MATLAB_CACHE_RUNTIME_PARITY_OVERLAY`, compared read-only with the already
admissible instrumented MATLAB chronology. That task must not rerun MATLAB and
must retain a finite one-shot budget.
