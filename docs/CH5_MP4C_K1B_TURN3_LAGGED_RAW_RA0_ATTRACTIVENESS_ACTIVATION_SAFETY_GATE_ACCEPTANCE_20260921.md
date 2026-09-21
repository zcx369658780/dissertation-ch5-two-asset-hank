# Chapter 5 K1B turn-3 activation safety gate — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__K1B_TURN3_ACTIVATION_SAFETY_GATE__TURN3_K1B_RUNTIME_AUTHORIZED`

Accepted Builder terminal:

`PASS__K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE__SHARES_AND_HOUSEHOLD_PAYOFF_CANDIDATE_READY__NO_HJB_RUN`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `7b6c30a568e1c89ca6a553451abe382e48ee7e23`
- candidate: `1c2157c1ee381f1bbc21bcebaa0233784e41a5c5`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- changed paths: 19
- production source diff: empty
- CURRENT diff: empty
- changed paths are limited to the authorized validator, focused test, report and fresh evidence root
- successor published by Builder: no.

## Input and raw-ra0 authority

The accepted safety gate binds completed-turn2 raw firm `ra0` exactly:

`B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951`.

The 31-province canonical order is unchanged.

Reviewer independently recomputed the frozen population cross-sectional convention from the persisted 31-vector:

- ordered mean: `0.5151713619509639`
- population standard deviation, ddof=0: `0.18665369395010123`

These exactly match the candidate receipt.

The persisted z-score vector SHA-256 is:

`E152FE1C33634F2127D2B535638FA2725687650496140641F0FC6D6A4C02B564`.

The z-score is used only for destination attractiveness; raw `ra0` levels remain the household payoff object.

## K1B share plan

Frozen turn3 K1B share-plan SHA-256:

`4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`.

The accepted construction uses:

`score[j,i] = -2.0*distance_score[j,i] + 0.5*return_score[j]`

over foreign destinations only, with the existing stable softmax.

Independent matrix checks from the persisted receipt confirm:

- orientation = destination x origin
- all entries finite and nonnegative
- home shares exactly equal `1-theta_i`
- maximum full-column sum error from 1 is `2.220446049250313e-16`
- K1A and K1B home shares are bitwise identical
- 900 foreign cells change
- maximum foreign-share change is `0.044098231463694224`.

No direction or magnitude of reallocation is an acceptance target.

## Turn3 household payoff candidate

K1B turn3 household payoff SHA-256:

`CEEFE34C16BA0DFDE9FA0C5590DFBB89084475BD88A8496EC18FEEBA7CB674D2`.

Range / mean:

- min `0.30906980372526094`
- max `0.994711274812942`
- mean `0.5266585162077394`.

The candidate is classified:

`TURN3_K1B_INPUT_CANDIDATE_ONLY__HOUSEHOLD_NOT_RUN`.

Reviewer independently compared it to the accepted run005 turn3 candidate:

- 31 rows preserved in canonical order
- non-`rah` state mismatches: 0
- exactly one `rah` entry remains bitwise equal, corresponding to the origin with `theta=0`.

A separate direct payoff recomputation from persisted raw `ra0` and `S_K1B` agrees within binary64 roundoff; the candidate's canonical ordered check reports maximum difference `1.1102230246251565e-16`.

## Timing and conservation

Accepted timing:

- turn3 K1B attractiveness uses completed-turn2 raw `ra0`
- turn3 firm output is not used to construct turn3 shares
- `S_K1B` is predetermined before the turn3 household solve
- turn3 capital quantities may use turn3 household wealth, but must reuse this exact frozen share plan
- turn3 household payoff and turn3 capital quantity accounting must use the same `S_K1B`
- turn3 firm raw returns may only affect the next turn's K1B share plan.

Scale-only conservation panel:

- origin private wealth total: `140310000.0`
- destination private capital total: `140310000.0`
- national residual: `0.0`
- home retained identity: PASS.

This is algebraic safety evidence, not a turn3 capital prediction.

## Zero-science and evidence integrity

All model-science counts are zero, including household HJB/KFE, direct solves, selector/root, D2/Q, firms, integration, turn3 household, K1B runtime, K2, MATLAB and GE/Results.

Evidence root:

`reports/ch5_mp4c_k1b_turn3_lagged_raw_ra0_activation_safety_gate_20260921_run001/`

- manifest SHA-256: `55908ED2B1C99436CF25A564AEE0E36589081B8CB20087505F7F5AB4F7AFC396`
- entries / bytes: `14 / 150185`
- independent readback: PASS
- bad paths: 0
- focused tests: 4/4 PASS.

## Route consequence

The safety prerequisite for turn3 K1B execution is satisfied.

The next bounded scientific task may execute exactly one corrected turn3 household HJB/KFE batch and, only if all 31 provinces pass, exactly one K1B/C1/source-faithful-labor integration using the frozen turn3 share plan above.

That authorization does not establish outer fixed-point convergence, K2, GE, annual dynamics, IRFs, welfare or Results.
