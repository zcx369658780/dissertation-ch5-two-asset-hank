# MP4B first-Beijing HJB guard observability replay report

Date: 2026-08-31

## Verdict

`MP4B_FIRST_BEIJING_HJB_GUARD_OBSERVABILITY_REPLAY_LOCALIZATION_PASS`

Established:

- `MP4B_FIRST_BEIJING_HJB_REPLAY_INITIAL_ITERATE_IDENTITY_PASS`
- `MP4B_FIRST_BEIJING_HJB_OFFENDING_LIQUID_DERIVATIVE_EXACTLY_LOCALIZED`
- `MP4B_HJB_FIRST_DIVERGENCE_SOURCE_SEMANTICS_DIAGNOSIS_COMPLETE`

This is observability evidence only, not an accepted HJB or household result.

## Continuity and replay identity

- live authority: `6f867c82bd17084980d344f6421455b490cf9e30`
- direct parent: `71f363c550a56d7bdba605ac5e8c416f3707b582`
- accepted oracle SHA-256:
  `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`
- prior initial diagnostic SHA-256:
  `6D9BC65657087D5DF3C17963D906EAFA93F2F5208F91D2211283B627F6C49951`

Before any value update, replay iteration 1 reproduced shape `[20,20,2]`,
initial-value SHA
`0B181AAD81C87DD5C13E4AB71BAF2F6B708EEEB3B71BC85331FFD6677E8AB14F`,
raw non-positive counts `0/0/0`, both-positive count `800`, nonfinite count 0,
and minimum cell `(18,19,1)` with
`VbF=0.001609918920837204`, `VbB=0.001610998339912406`.

The replay then used the accepted local-policy function for every cell strictly
before the stop, accepted `assemble_source_operator`, delta `1000`, rho `.05`,
the accepted switching matrix, and exact Fortran flatten/reshape ordering.

## Artifact

Root:
`D:\ProjectTemp\ch5-mp4b-first-beijing-hjb-guard-replay-20260831-001`

Artifact:
`first_beijing_hjb_guard_replay.json`

SHA-256:
`5DF297B56B62FD624C0A5BAAE6BAD63DDB2ECD308AFF2A80DC3B41A81BF57A02`.

## Completed iteration summaries

| iteration | min VbF | max VbF | min VbB | max VbB | nonpositive | statistic | new-value SHA prefix |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | .001609918920837204 | .01710327766593922 | .001609918920837204 | .01710327766593922 | 0 | .39062620303452533 | `2A206A2710AC...` |
| 2 | .002626386625505247 | .01242062571753125 | .002626386625505247 | .01242062571753125 | 0 | .035354649797403326 | `178163F6CDB8...` |
| 3 | .003358002048405766 | .010513935516640592 | .003358002048405766 | .010513935516640592 | 0 | .09227485670660163 | `A4DFAC48F09F...` |
| 4 | .00043448090430756427 | .06482768830303057 | .00043448090430756427 | .06482768830303057 | 0 | .29832743504186854 | `3F6D860EDC72...` |

Iteration 5 was not completed or assembled.

## Exact offending cell

- HJB iteration: `5`
- completed previous value updates: `4`
- zero-based `(i,j,k)`: `(5,18,1)`
- MATLAB `(i,j,nz)`: `(6,19,2)`
- `(b,a,z)`: `(-0.1578947368421053, 9.473684210526315, 1.3)`
- boundary flags: all false
- baseline labor: `0.6314022855913544`
- transfer income / rb / borrowing gap / effective rb:
  `0.1 / 0.02 / 0.07 / 0.09000000000000001`

Neighboring values:

| object | value |
|---|---:|
| current | `-1.5173653573108608` |
| liquid forward | `-1.522524631550784` |
| liquid backward | `-1.5187090007787158` |
| illiquid forward | `-1.501727004331531` |
| illiquid backward | `-1.5269976424702727` |

Derivatives:

| derivative | raw | MATLAB consumption/labor processed |
|---|---:|---:|
| `VbF` | `-0.014003744365506235` | `1e-6` |
| `VbB` | `0.0036470322698923963` | `0.0036470322698923963` |
| `VaF` | `0.029712870660726632` | unchanged |
| `VaB` | `0.0183013418028827` | unchanged |

The replay inspected these values immediately before local policy, did not call
local policy for this cell, did not finish iteration 5, and stopped.

## Transfer candidate evidence

Protected MATLAB raw `pa/pb` arithmetic is finite at this cell:

| candidate | pa | pb | pa/pb | source candidate |
|---|---:|---:|---:|---:|
| BB | .0183013418028827 | .0036470322698923963 | 5.01814638547815 | 18.55964077331755 |
| BF | .029712870660726632 | .0036470322698923963 | 8.147136757197735 | 33.3811741130419 |
| FB | .0183013418028827 | -.014003744365506235 | -1.3068891665833482 | -10.45368552592112 |
| FF | .029712870660726632 | -.014003744365506235 | -2.1217804242353084 | -14.313696746377776 |

No Inf or NaN ambiguity exists at the localized cell.

Floored liquid candidates:

| branch | consumption | labor | resources | drift |
|---|---:|---:|---:|---:|
| backward | 16.55885094926209 | .6179129710131375 | 15.348239857708705 | -1.2106110915533854 |
| forward | 1000 | .1198227797915766 | 3.0454121345361527 | -996.9545878654638 |

MATLAB source action is to floor `VbF` for consumption/labor and continue to
raw transfer ratios. Current Python action is to reject before the floor and
before transfer ratios.

Classification:
`PYTHON_IMPLEMENTATION_ERROR__NONSOURCE_PRE_FLOOR_LIQUID_DERIVATIVE_POSITIVITY_GUARD`.

## Call ledger and boundaries

| operation | count |
|---|---:|
| bounded replay invocation | exactly 1 |
| authorized province households | Beijing only: 1 |
| accepted local-policy calls before stop | 3200 |
| completed HJB value updates | 4 |
| offending-cell local-policy call | 0 |
| Python stationary / `solve_household_steady_state` | 0 / 0 |
| KFE / household aggregation / second province | 0 / 0 / 0 |
| MP2 / MP3 controller | 0 / 0 |
| MATLAB model / wrong-year / batch / shocks / dynamics / IRF / R5 / Results | 0 |

No repair or second replay occurred. Accepted oracle and protected sources were
not modified.

Focused tests covered synthetic traversal/stop-before-policy, prohibited-call
reachability and bounded horizon. Python compile and `git diff --check` passed.

## Exactly one recommended next gate

Authorize targeted accepted-oracle raw-Vb guard and transfer-candidate source-
order repair, followed by affected local-policy, HJB and standalone-household
parity revalidation; keep empirical stationary calls at zero.
