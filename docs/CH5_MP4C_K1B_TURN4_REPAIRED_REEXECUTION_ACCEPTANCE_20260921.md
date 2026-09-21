# Chapter 5 K1B turn4 repaired reexecution — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__ANHUI_F0364_REPAIR_HISTORICAL_PARITY_AND_K1B_TURN4_REEXECUTION__TURN5_INPUT_ACCEPTED`

Accepted Builder terminal:

`PASS__ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR__HISTORICAL_POLICY_PARITY_PASS__K1B_TURN4_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN5_K1B_INPUT_READY__TURN5_NOT_RUN`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `1843bd413ee019b04c6937abd1e89cf044e62241`
- candidate: `2155d16ab04f705b1a0da1cc3b49d78e60592c2e`
- candidate tree: `a9ec093b7d574a1a566d5451278555d437f5dcf2`
- ancestry: 1 ahead / 0 behind
- pre-repair selector blob: `e8a1d72e23661576f14ac42b7dff6e3001837206`
- repaired selector blob: `51517dde0c829060b6e0c0d594ec60e7e6143883`
- repaired selector SHA-256: `DC8E0FBB751BA2A6DF58C88923E0A2E31D285D780E0EFE53CB90A580D59E99FE`
- pre/post execution source freeze: exact
- CURRENT modified by Builder: no
- successor published by Builder: no.

The production semantic change is confined to the accepted interior-b/interior-a finite-negative-R branch-local positive-domain logic in `selector.py`. The accepted focused and historical compatibility gates provide the controlling scope evidence.

## Focused repair acceptance

安徽 F0364 is selected by the normal production selector with:

- q_b = `0.0015039676061569449`
- q_a = `-0.0005008835855672058`
- d = `-5.840722762648187`
- g_a = `0`
- g_b = `-17.978717494437753`
- Hamiltonian = `-0.06734914681687235`
- no interior-b switching root.

The production floating-point KKT residual is `1.0842021724855044e-19`, well below the unchanged arithmetic tolerance `1.1564470160853633e-12`. No KKT/cost arithmetic was altered to force an exact displayed zero.

The prior Beijing F0364 candidate remains exact, and the focused regression gates preserve positive-ratio, active-liquid-face negative-ratio and ratio-zero behavior.

## Historical compatibility acceptance

Mandatory selected-policy identity replay passed:

- turn1 run004: 408/408
- turn2 run005: 411/411
- turn3 accepted: 408/408
- combined: 1227/1227
- mismatches: 0
- selector evaluations: 981600
- accepted/replayed ordered digest:
  `31C7D784B2AB023E115DB40E1F74003D2FF91572877CD50F26B116BDBC37848B`.

Historical replay consumed zero HJB updates, D2/Q, KFE/SVD, aggregate/integration and retry/tuning calls.

This establishes compatibility of the narrow repair with all accepted predecessor household policy paths.

## Fresh turn4 acceptance

All 31 provinces passed corrected HJB/KFE.

- direct HJB updates: 378
- policy maps / D2-Q: 409 / 409
- selector evaluations: 327200
- SCC / restricted GESVD / normalized stationary / full-Q: 31 each
- full-space 800x800 GESVD: 0
- relaxation: 374 alpha=1 and 4 alpha=.5
- exhaustion: 0
- scientific retry / solver substitution: 0 / 0
- max terminal B: `3.5233607698081926e-11`
- max terminal D: `3.523143110584215e-08`.

The fresh path reached the same 安徽 checkpoint4/F0364 derivative state and selected the accepted repair candidate in-path with no additional selector call.

## Turn4 K1B integration acceptance

Exactly one integration ran after the 31/31 gate:

- household batch / source-faithful labor / frozen K1B / C1: 1 each
- firms: 31
- wage / monetary / fiscal: 1 each
- same-turn share recomputation: 0.

Frozen turn4 share SHA:

`5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`.

Origin private wealth total is `140310000.0`. Destination private capital is `140310000.00000003`; national residual is `2.9802322387695312e-08`, well inside the frozen scale-aware conservation tolerance.

Completed-turn4 raw ra0 SHA:

`0312EBE6C2764DB3A834F1233712186ED1B6CE0C3E8BC01E58EFF6A0E8DCD267`.

## Accepted turn5 entering objects

Turn5 candidate:

`reports/ch5_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair_reexecution_20260921_run001/turn5_k1b_input_candidate.json`

- Git blob: `7826691387916254ef55b149651d51f8438cab10`
- file SHA-256: `10CDFE998FBC95F09DA682F5389F268A1569A5FEB345D61470B3E8AA415D01D1`
- classification: `TURN5_K1B_INPUT_CANDIDATE_ONLY__TURN5_HOUSEHOLD_NOT_RUN`
- rah SHA: `5CAF9166D85198E6923FFCD5A1F92D278C8A1C6CB924E8DD1B843F875E91D88E`.

Frozen turn5 share/payoff plan:

`reports/ch5_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair_reexecution_20260921_run001/turn5_k1b_frozen_share_payoff_plan.npz`

- Git blob: `83cee2bafb63d5f608e9d1b76480621a14077cc3`
- file SHA-256: `57A31EAA59A9E6CCD74E1DD5C18C74496829BA181866E12300CA7EB202890A70`
- portfolio-share SHA: `2BDF7B8226C8404DB9C7FFEEE3F72F7AE9CA1305905460A4E2430AABEA4D3B06`.

Turn5 raw-return z-score input:

- mean `0.5190899802806576`
- population std `0.1915047411123845`
- z-score SHA `2B8B8543BF810BF92BF32EBE1CD43DD72FD4D686BFFAF27D9E3054C92ECE7D24`.

## Repeated-turn diagnostic

Turn3 -> turn4 changes are descriptive, not acceptance criteria:

- raw-ra0 max absolute change: `0.004025704005734321`
- raw-ra0 Euclidean norm change: `0.005510286646555688`
- portfolio-share max absolute change: `0.00017089672979736514`
- portfolio-share Frobenius change: `0.0002936100333500836`
- rah max absolute change: `0.0035652015398268677`
- direct updates: 377 -> 378.

These values do not establish convergence, but they support moving from one-turn-at-a-time activation tests to a bounded multi-turn diagnostic under unchanged science.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair_reexecution_20260921_run001/`

- entries: 4748
- bytes: 64640636
- manifest SHA-256: `1C4F6BB5423471F126B0670BBC48A486CAE2B25ECC8B79B944C8827D29D4F93B`
- independent readback: PASS
- bad paths: 0.

## Route consequence

The repaired selector and the complete K1B-active turn4 are accepted.

Reviewer authorizes a bounded two-turn continuation covering turn5 and turn6 under exactly the accepted K1B economics and numerical laws. This is a trajectory diagnostic, not a steady-state or convergence claim.

The continuation must stop before turn7 household and may not enter K2, GE or Results.
