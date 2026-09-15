# CH5 MP4C K1 — first-turn provincial input/outcome envelope audit

## Terminal class

`FAILURE_SUCCESS_INPUT_ENVELOPES_OVERLAP_SUBSTANTIALLY`

Results eligibility=`FALSE`.

## Authority and runtime

Actual baseline: `24ff3ca5a34530df661aa3f4a2adc7342e5fd8f7`. The accepted 31-province table and upstream mapping metadata were reconstructed solely from hash-verified repository evidence. HJB/KFE/firm/wage/return/outer/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results runtime and scientific retries are all zero.

`guarded_wjt` is retained only as a distinct upstream object and is never substituted for household composite `w`. Raw provincial `wjt` is unavailable in accepted compact evidence.

## Group envelopes

| group | n | ra min / median / max | composite-w min / median / max |
|---|---:|---:|---:|
| failures | 6 | 0.0649036548 / 0.0877776843 / 0.09 | 17.4716722 / 18.0684438 / 18.2030991 |
| successes | 25 | 0.0737060738 / 0.0840389907 / 0.0890622563 | 13.8374775 / 17.7173352 / 18.5196979 |
| all_31 | 31 | 0.0649036548 / 0.0848805905 / 0.09 | 13.8374775 / 17.8745822 / 18.5196979 |

## Failure ranks and nearest successes

| failure | ra rank | w rank | nearest success | standardized distance |
|---|---:|---:|---|---:|
| 天津 | 1/31 | 23/31 | 内蒙古 | 1.71427993 |
| 山西 | 22/31 | 24/31 | 河北 | 0.0692933142 |
| 江西 | 29/31 | 19/31 | 安徽 | 0.199056414 |
| 重庆 | 19/31 | 20/31 | 河北 | 0.0996549106 |
| 贵州 | 30/31 | 11/31 | 四川 | 0.249215875 |
| 甘肃 | 31/31 | 12/31 | 四川 | 0.255113276 |

## Guard, envelope and graph findings

- Guard result: `NO_DISCRIMINATING_GUARD_VARIATION`. Return guard is `NOT_APPLIED_BOOTSTRAP` for 31/31; corrected upstream wjt guard is `UPPER` for 31/31.
- Bounding boxes overlap: `TRUE`.
- Failure and success convex hulls overlap: `TRUE`; failures inside/on success hull: `2/6`.
- Single-ra threshold: `DOES_NOT_EXIST`.
- Single-composite-w threshold: `DOES_NOT_EXIST`.
- Fixed k=3 graph: `FAILURE_SUCCESS_NODES_INTERLEAVED`; failure-induced connected=`FALSE`, failure-to-success neighbor entries=`12`.

## Upstream mapping evidence

Raw pre-guard return is sealed for `31/31` and equals consumed ra for `31/31`. Raw provincial wjt is unavailable for `31/31`; guarded wjt is sealed but is not the household wage coordinate.

## Interpretation boundary

The six failures are descriptively interleaved with successes in the accepted consumed `(ra,w)` input space. This is not a causal result and does not authorize recalibration, guard/mapping changes, parameter changes, HJB/KFE changes, or Results use.

## Exactly one next gate

`REVIEWER_FIRST_TURN_INPUT_OUTCOME_ENVELOPE_ROUTE_DECISION`
