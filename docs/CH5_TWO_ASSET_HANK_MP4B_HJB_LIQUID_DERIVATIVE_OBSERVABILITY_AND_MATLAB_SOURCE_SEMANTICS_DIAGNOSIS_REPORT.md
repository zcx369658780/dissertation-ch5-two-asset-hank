# MP4B HJB liquid-derivative observability diagnosis

Date: 2026-08-31

## Terminal verdict

`MP4B_HJB_LIQUID_DERIVATIVE_OBSERVABILITY_DIAGNOSIS_BLOCKED`

MATLAB/Python operation ordering is uniquely resolved, but the exact offending
cell is not present in the initial Beijing HJB iterate. The preserved failure
must occur after at least one HJB value update, while this task expressly
forbids HJB iterations. No cell or derivative value was invented.

Established:
`MP4B_HJB_LIQUID_DERIVATIVE_MATLAB_SOURCE_ORDERING_FROZEN`.

Not established:
`MP4B_FIRST_BEIJING_HJB_OFFENDING_LIQUID_DERIVATIVE_EXACTLY_LOCALIZED` and
`MP4B_HJB_FIRST_DIVERGENCE_SOURCE_SEMANTICS_DIAGNOSIS_COMPLETE`.

## Continuity and source identities

- live authority: `61e26737739e46147e7c0b38ae6712fbced36e8e`
- direct parent: `1aeca1cfb2f083e151e881d92db8a81d53b6c918`
- protected `HANK_2ASSETS_HJB.m`:
  `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- protected `HANK3_FOC.m`:
  `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- protected `HANK3_cost.m`:
  `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- accepted standalone oracle:
  `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`

Protected sources and accepted scientific arithmetic were read-only.

## Exact MATLAB operation ordering

Protected HJB lines 114-140 uniquely establish:

1. lines 116/118 construct raw interior `VbF/VbB` differences;
2. lines 117/119 replace upper-forward and lower-backward liquid boundaries
   with source marginal utility;
3. lines 120-123 construct raw illiquid differences and zero boundary values;
4. lines 124-128 apply `max(Vb,1e-6)` only to consumption and labor FOCs;
5. lines 129-135 calculate liquid resources/drifts and liquid upwind labels;
6. lines 137-140 call `HANK3_FOC` with raw `Vah` and raw `Vb`;
7. `HANK3_FOC.m:19` evaluates `pa./pb` directly, without a raw-positive guard
   or derivative floor;
8. lines 141-154 construct transfer candidates and transfer upwind selection;
9. lines 155-198 assemble liquid/transfer and illiquid drift rates.

MATLAB therefore does not reject a cell solely because a raw pre-floor liquid
derivative is negative. It floors liquid derivatives for consumption/labor,
but uses the raw derivatives in transfer ratios.

## Exact accepted-oracle ordering

The standalone solver constructs interior differences and boundary marginal
utilities at lines 516-526, matching MATLAB's raw construction. During local
traversal it then calls `select_matlab_faithful_local_policy`.

That function:

1. rejects `min(v_b_forward,v_b_backward)<=0` at lines 247-248;
2. only afterward defines floored `vb_b/vb_f` at lines 259-260;
3. uses those floored values for consumption/labor at lines 261-273;
4. calls `transfer_candidate` with raw derivatives at lines 291-294;
5. `transfer_candidate` itself adds a second Python-only `v_b<=0` rejection at
   lines 85-91;
6. then performs transfer and local upwind selection.

Static source classification:
`PYTHON_IMPLEMENTATION_ERROR__NONSOURCE_PRE_FLOOR_LIQUID_DERIVATIVE_POSITIVITY_GUARD`.
This ordering defect is established independently of the unavailable later-
iteration cell, but exact first-divergence localization remains incomplete.

## Initial-iterate reconstruction and artifact

The validator reconstructed source initial value/labor arrays for the first
Beijing household, then directly formed the same `20*20*2` finite differences,
boundary values and floor arrays. It did not call a household solver, HJB
iteration, KFE, MP2, MP3, stationary controller or MATLAB function.

The first direct-script attempt used root suffix `-001` and failed before any
arithmetic because the new validator lacked repository bootstrap. It produced no
artifact and made zero model calls. The validator was given the same finite
`__file__`-derived repo/src bootstrap and rerun under:

`D:\ProjectTemp\ch5-mp4b-hjb-liquid-derivative-observability-20260831-002`

Artifact:
`beijing_initial_hjb_liquid_derivatives.json`

SHA-256:
`6D9BC65657087D5DF3C17963D906EAFA93F2F5208F91D2211283B627F6C49951`.

Initial-value shape is `[20,20,2]`, range
`[-2.2796313738283325,-1.4773664265733266]`, with byte SHA
`0B181AAD81C87DD5C13E4AB71BAF2F6B708EEEB3B71BC85331FFD6677E8AB14F`.

## Complete Beijing sign/floor counts

| category | raw | after MATLAB consumption/labor floor |
|---|---:|---:|
| `VbF <= 0` | 0 | 0 |
| `VbB <= 0` | 0 | 0 |
| either non-positive | 0 | 0 |
| both positive | 800 | 800 |
| either nonfinite | 0 | 0 |

Therefore there is no offending cell in the task-authorized initial iterate.

## Minimum raw-derivative witness, not an offending cell

The minimum raw derivative occurs at zero-based `(i,j,k)=(18,19,1)`, MATLAB
indices `(19,20,2)`, with `(b,a,z)=(4.63157894736842,10,1.3)`.

| object | value |
|---|---:|
| current / forward-b / backward-b value | `-1.477959554596793 / -1.4773664265733266 / -1.4785530803009712` |
| forward-a / backward-a neighbor | unavailable upper boundary / `-1.4779595659611804` |
| raw `VbF / VbB` | `0.001609918920837204 / 0.001610998339912406` |
| processed `VbF / VbB` | same / same |
| raw/processed `VaF` | `0 / 0` |
| raw/processed `VaB` | `2.1592336119091728e-08` |
| baseline labor | `0.6301812143154218` |
| transfer / borrowing gap / effective rb | `0.1 / 0.07 / 0.02` |
| boundaries | upper-a true; other three false |

Transfer ratios/candidates (`BB,BF,FB,FF`) are respectively:

| candidate | `pa/pb` | transfer candidate |
|---|---:|---:|
| BB | `1.3403077820841055e-05` | `-4.499932984610896` |
| BF | `0` | `-4.5` |
| FB | `1.3412064321762922e-05` | `-4.499932939678391` |
| FF | `0` | `-4.5` |

Liquid backward/forward candidates have consumption
`24.914515928568395 / 24.922866876266383`, resources
`13.154134512675288 / 13.152397124820164`, and drifts
`-11.760381415893107 / -11.77046975144622`. Both MATLAB and Python proceed at
this initial cell; it is included only as the minimum-positive witness.

## Blocker and minimal successor specifications

The preserved empirical error proves some later HJB local-policy call had a
non-positive raw liquid derivative. Because all initial derivatives are
positive, obtaining its exact iteration/cell requires observing at least one
HJB value update. Neither the failure artifact nor preserved MATLAB output
contains that trace, and HJB iterations were forbidden here.

Conditional repair specification, not implemented:

- target `exports/matlab_faithful_two_asset_ha.py` functions
  `select_matlab_faithful_local_policy` and `transfer_candidate`;
- remove the non-source pre-floor raw positivity rejection;
- retain `max(raw Vb,1e-6)` for consumption/labor FOCs exactly where MATLAB does;
- use raw boundary-treated `Vb` and raw `Va` for transfer ratios, matching
  `HANK3_FOC` operation order;
- retain current liquid/illiquid boundary and upwind order;
- explicitly test negative and zero raw derivatives against protected MATLAB
  scalar behavior before accepting division-edge semantics;
- rerun affected local-policy, HJB, standalone household and accepted export
  parity gates before any empirical stationary authorization.

Because this changes the accepted standalone oracle, all affected accepted
household/HJB authorities require targeted revalidation. This task does not
authorize that repair.

## Zero-call ledger and checks

| operation | calls |
|---|---:|
| Python stationary / household solver | 0 / 0 |
| Python HJB iterations / KFE | 0 / 0 |
| MP2 / MP3 empirical execution | 0 / 0 |
| MATLAB stationary/HJB/KFE/multi-province | 0 |
| wrong-year/batch/shocks/transition/dynamics/IRF/R5/Results | 0 |

Focused import/direct-script diagnostics passed. Source/oracle hashes and
forbidden-operation scans passed. `git diff --check` passed. No accepted
scientific arithmetic or protected artifact was modified.

## Exactly one recommended next gate

Authorize one instrumented first-Beijing HJB observability replay, stopping at
the first raw-derivative guard, with no KFE, household aggregate, MP2/MP3,
stationary controller or MATLAB model call; persist iteration/cell derivatives
only and do not repair in that gate.
