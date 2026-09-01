# MP4B Python runtime-overlay corrected-2009 one-shot and trajectory parity diagnostic

## Terminal verdict

`MP4B_RUNTIME_OVERLAY_CORRECTED2009_ONE_SHOT_AND_TRAJECTORY_PARITY_DIAGNOSTIC_PASS`

Strongest supported classification:

`MP4B_RUNTIME_OVERLAY_INITIAL_BINDING_EQUALIZED__LATER_DIVERGENCE_PERSISTS`

The validation-only overlay makes turn-1 entry `Zt` bitwise identical between
MATLAB and Python for all 31 provinces. It does not remove the already durable
turn-1 household/firm differences, turn-8 reset-category divergence, turn-154
Zhejiang controller-action divergence, or final wage-upper boundary mismatch.
Chronology alone is not used as a causal or fault attribution.

## Live authority and continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Live task authority / execution-start `HEAD` / `origin/main`:
  `aebe4e96260d86cc0f31053f92ac73881097b265`.
- Required direct parent:
  `61f400f3a8f32413ad9c68da1c5ad82ed7a0d0a1`; verified as the sole parent.
- Fresh fetch, fast-forward-only synchronization, clean entry worktree,
  `HEAD == origin/main`, and ahead/behind `0/0`: PASS.
- All named rules, predecessor task/report groups, current binding helper,
  immutable scientific driver, comparator, and exact external evidence roots
  were read before science.

## Validation-only overlay binding

`PRIMARY_SOURCE_CANONICAL` remains the scientific/default authority. The
immutable primary canonical input remains
`D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json`,
SHA-256
`507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.
The accepted derived MATLAB runtime cache remains SHA-256
`923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`.

Using only the accepted binding helper, explicit mode
`MATLAB_CACHE_RUNTIME_PARITY_OVERLAY` materialized a canonical-shaped
`binding.object` at
`D:\ProjectTemp\ch5-mp4b-python-runtime-overlay-input-20260901-001\runtime_overlay_input.json`.
The overlay changes only `vectors.initialized_zt`; every other field and the
31-province order remain identical to canonical.

The accepted invariant is exact: 24 equal rows, 7 replacements, five 1-ULP
replacements, and two 2-ULP replacements. Changed zero-based indices/names are
`1 天津`, `12 福建`, `13 江西`, `15 河南`, `18 广东`, `23 贵州`, and `25 西藏`.
The overlay remains validation-only and is not a new scientific canonical
artifact.

## Pre-science gate

- Binding helper blob:
  `20123513f232cb2d3cca1264565837e4882ea19f`.
- Immutable one-shot driver blob:
  `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`.
- Accepted comparator blob:
  `cbe7ce4e4855c139cc7bb3b20b56d124c4add266`.
- All Section 4 scientific/runtime SHA-256 identities: PASS.
- `python -m py_compile validators/multi_province/mp4b_canonical_input_binding.py tests/test_mp4b_canonical_input_binding.py`: PASS.
- `python -m pytest -q tests/test_mp4b_canonical_input_binding.py`:
  `7 passed in 0.09s`.
- Exact cache binary64 values, 24/7 census, 5x1-ULP/2x2-ULP pattern,
  province order, and non-`initialized_zt` identity: PASS.
- D-drive free space before science: `68.808 GiB`.
- Scientific run root absent before launch: PASS.
- `pre_science_gate.json` SHA-256:
  `FFBEABFAEBC8401DA7BE427DEA8211EAE1D5338ECB5E688369836BF237DD244C`.
- Scientific/model calls before launch: `0`.

## Exact one-shot scientific ledger

The immutable driver was invoked exactly once with the materialized overlay
input and fresh run root
`D:\ProjectTemp\ch5-mp4b-python-runtime-overlay-one-shot-20260901-001`.
It exited `0`, produced `SOURCE_CONVERGED`, completed 184 outer iterations and
5,704 household calls, and ended with household convergence `31/31`.

| Operation | Count |
| --- | ---: |
| Python corrected-2009 stationary top-level | 1 |
| Python stationary rerun | 0 |
| standalone household/HJB/KFE | 0 |
| standalone MP2/MP3 | 0 |
| qualified final-state comparator | 1 |
| comparator rerun | 0 |
| MATLAB process/checkcode/model call | 0 |
| other years/batch | 0 |
| shocks/AR1/transition/dynamics/IRF | 0 |
| R5/Results | 0 |

No repair-and-rerun lane was used.

## Overlay Python versus canonical Python

Both runs end at 184 outer iterations, 5,704 household calls, and final
household convergence `31/31`. Both have final wage upper/lower `5/17`, final
ra upper/lower `0/0`, 2,336 low actions, zero high actions, and 2,365 Zt
resets. Their low/high/reset coordinate sets are identical.

The first difference is turn 1, one-based province 2 Tianjin, entering `Zt`:
canonical `0.023633692874437028` versus overlay
`0.02363369287443703`. The seven initial representation replacements create
15,762 differing floating leaves across turns 1--14, including firm outputs;
the histories are identical thereafter. All 31 provinces and all 20 frozen
final-state fields are exactly equal between the two Python runs.

National values are also exactly unchanged:

| Field | Canonical Python | Overlay Python | Difference |
| --- | ---: | ---: | ---: |
| Ct | 276.52720698365306 | 276.52720698365306 | 0 |
| At | 47.11415467808319 | 47.11415467808319 | 0 |
| Bt | 65.21538414270965 | 65.21538414270965 | 0 |
| Yt | 350585612.6035657 | 350585612.6035657 | 0 |

## Overlay Python versus instrumented MATLAB chronology

The required binding gate passes: turn-1 entry `Zt` is bitwise exact for
`31/31` provinces.

The earliest remaining mapped differences are:

| Layer | Turn/province | MATLAB | Overlay Python | Difference M-P |
| --- | --- | ---: | ---: | ---: |
| household output `Ct` | turn 1, Beijing | 11.400731651946101 | 11.400731651949162 | -3.0606628342866316e-12 |
| firm output `Yt` | turn 1, Beijing | 79417893.1140632 | 79417893.11405928 | 3.919005393981934e-06 |
| next entry `Lt` | turn 2, Beijing | 4209719.4410444815 | 4209719.44104403 | 4.516914486885071e-07 |

The first categorical reset divergence remains at turn 8. MATLAB resets
Qinghai (one-based 29) but not Shanghai (9); overlay Python resets Shanghai
but not Qinghai. The unique MATLAB-only low-return action remains turn 154,
Zhejiang (one-based 11). MATLAB/Python low-action counts remain `2337/2336`;
Zt-reset counts remain `2366/2365`. MATLAB-only reset coordinates remain
turn 8 Qinghai and turn 156 Zhejiang; Python-only remains turn 8 Shanghai.

Final boundary categories remain: household `31/31`, ra upper/lower `0/0` on
both sides, wage lower `17/17`, and wage upper MATLAB `7` versus Python `5`.
Thus the turn-8, turn-154, and final wage-boundary dispositions are unchanged.

## Qualified final-state comparator

The complete 31-province terminal qualified for the accepted comparator. It
was invoked once, with reruns `0`, against only the preserved corrected-2009
MATLAB stationary output, the new overlay Python terminal, and the accepted
MATLAB terminal status. Output schema is
`MP4B_PRESERVED_MATLAB_PYTHON_FINAL_STATE_COMPARISON_V2`.

The output SHA-256 is
`77916C2376B96D7C94CBF15A2E5DED1BCF366C4430FACCE84746794B468986AB`.
Because the overlay and canonical Python final states are exact, this artifact
is byte-identical to the accepted canonical-run comparator artifact at
`D:\ProjectTemp\ch5-mp4b-final-state-comparator-replay-after-representation-remediation-20260831-001.json`,
which is also 106,389 bytes with SHA-256
`77916C2376B96D7C94CBF15A2E5DED1BCF366C4430FACCE84746794B468986AB`.
It confirms outer turns `184/184`, household `31/31`, ra upper/lower `0/0`,
wage lower `17/17`, and wage upper `7/5`; continuous national mismatches also
remain unchanged.

## External artifacts

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `runtime_overlay_input.json` | 57,131 | `072E5E943FB6BFF6768CD40001B031C3AF1A6DD92FCC3A86E1B6D476E03E0137` |
| `runtime_overlay_binding_manifest.json` | 5,090 | `1D059E59B27EC933D4F59526BBFB664D084E0F4C740221D4081579E1DF2CE90C` |
| `pre_science_gate.json` | 11,665 | `FFBEABFAEBC8401DA7BE427DEA8211EAE1D5338ECB5E688369836BF237DD244C` |
| `exact_scientific_launcher_command.txt` | 220 | `023AD0BDB14945429C3FD3C5DA0E343050ABFA24617CECF82784784950E9B6D9` |
| `python_run_manifest.json` | 606 | `030A4241D4FB7A8CFA5370811FC4502028A61E46521F9329D7768B45278F6774` |
| `python_terminal_summary.json` | 29,826,860 | `5C9675702D27FF03A3ADA8959166C757F152B8C9E91126533E557373CB7C74E0` |
| `overlay_vs_canonical_python_trajectory.json` | 119,651 | `2000380BB51CC505DE40EE3C5B5ED6691F9F9AA6253DCC0329123F7B375AB69C` |
| `overlay_python_vs_matlab_chronology.json` | 9,938 | `09DC11C9BBB6E4CDF81C687A2F94FA1E460F2C608544825ADCAED88EC9A00F8F` |
| `qualified_final_state_comparison.json` | 106,389 | `77916C2376B96D7C94CBF15A2E5DED1BCF366C4430FACCE84746794B468986AB` |
| `diagnostic_manifest.json` | 70,137 | `DBA08ACDBC5E0E769FCA18C4E806B5B648703B839ED90469493835BEE146B6AB` |

The diagnostic manifest inventories four binding-root files and 374 run-root
files with sizes and SHA-256. All runtime inputs, 184 turn input/output pairs,
terminal/history, parsers' JSON results, and comparator output remain external
under `D:\ProjectTemp`.

## Protected-boundary and closeout audit

No `src/` scientific module, existing driver, binding helper, comparator,
canonical input, MATLAB source/artifact, test, threshold, tolerance, prior
task/report, or project rule was modified. The only repository mutation is
this report. No MATLAB process was started.

Before the only execution commit, the report is explicitly staged and
`git diff --check --cached` is required to pass. Closeout uses exactly one
explicit-path commit, one non-force push, fresh GitHub read-back of this report,
`HEAD == origin/main`, ahead/behind `0/0`, and a clean worktree.

## Exactly one recommended next gate

L3 read-only review of this immutable overlay chronology package to decide
whether the remaining turn-1 same-input household/firm numerical divergence
warrants a separately authorized bounded source-layer diagnostic. It must not
rerun either stationary model or alter thresholds, tolerances, scientific
defaults, other years, shocks, transition/IRF, R5, or Results.
