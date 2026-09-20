# CH5 MP4C K1A raw-ra0 Path-B turn-1 31-province fixed-price one-step cross-section acceptance

Date: 2026-09-20

Reviewer verdict:

`PASS__TURN1_GENERATED_RAW_RA0_31_PROVINCE_FIXED_PRICE_CROSS_SECTION_ACCEPTED__CORRECTED_INITIAL_TURN_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_AUTHORIZED`

## Accepted candidate

- live main before Builder task: `a2c728582ca19718270c6b2c91ea9a0bac547072`
- implementation-freeze commit: `000bfd790cc5dadcb3723b7f4e1d47fcd8ed2475`
- Builder candidate: `d0e3cdc27f11d6d7bb0a0ec32299e0f00f90fcda`
- candidate tree: `17418b5db5e65da36df3bc085f27f5df89595a03`
- ancestry: exactly `2 ahead / 0 behind`
- independently tree-compared changed paths: `396`
  - driver: 1
  - focused test: 1
  - report: 1
  - evidence: 393
  - CURRENT files: 0
- Builder did not merge main and did not publish a successor.

## Exact source and compact-evidence acceptance

The accepted payoff CSV remains:

`docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/static_no_feedback_payoff_counterfactual.csv`

SHA-256:

`5496DA47A1F06E46088D4FA80B3803654FB6C47134EE0D32F2DF79028C0FE9F9`.

Exact selection:

- `path=B_GEOGRAPHIC_BETA2`
- `turn=1`
- province index `0..30`
- 31/31 active province labels
- 31/31 `STATIC_NO_FEEDBACK_COUNTERFACTUAL`
- 31/31 `VALIDATED_SAME_S_AND_NEXT_ALLOCATION_PAYOFF`.

The preregistered payoff vector is reproduced exactly. Its descriptive range is:

- minimum Jilin: `0.2826739400149174`
- median Hunan: `0.4775623850053351`
- maximum Beijing: `0.8951047990241244`.

Before science, the Builder fully read back the accepted three-point manifest

`6D0A210F3979B0E0499FA8CC4C21803EB59077D655286D7119E0F85741BB5ED4`

and zero-science recertified the compact evidence projection for LOW/MEDIAN/HIGH. Canonical policy identities, normalized change counts, constraints, transfer branches, switching indices/counts and selected field hashes all reproduced exactly with zero selector/Q/solve calls.

The compact representation is accepted for successor diagnostics.

## 31-province one-step acceptance

All 31 province-labelled payoff values completed in exact province-index order:

- 800/800 corrected selector cells;
- unchanged D2 legality/conservation gate;
- exactly one fixed-`Delta=1000` direct implicit HJB update;
- no warning;
- direct-solve normwise backward error below `1e-12`;
- no second update;
- no HJB convergence classification;
- no KFE;
- no scientific retry.

Cross-section diagnostics:

- `B_seed` min/median/max:
  `0.011596928157030645 / 0.02322999485492319 / 0.04815937276916729`
- `D_step` min/median/max:
  `0.07676771340507083 / 0.19075118997293417 / 0.20564400224507096`
- maximum backward error:
  `2.1698602585651234e-16`
- maximum `abs(Q@1)`:
  `3.552713678800501e-15`
- minimum off-diagonal:
  `2.7404782515125115e-06`.

All provinces have 80 serialization-normalized policy identity changes relative to accepted P11. Seven distinct canonical policy identities occur. Transfer branches are identical across the cross-section: negative 298, positive 323, zero-kink 179. No interior-a or joint root is selected; liquid-Z variants account for the observed compact policy families.

No trend, threshold or convergence-probability interpretation is accepted.

## Scientific ledger acceptance

Accepted scientific ledger:

- policy maps: 31
- selector evaluations: 24,800
- scalar roots: 8,405
- liquid-Z roots: 469
- interior-a roots: 0
- joint roots: 0
- D2/Q assemblies: 31
- direct HJB solves/updates: 31/31
- complete cross-section evaluations: 31
- retries/substitutions: 0/0
- KFE/SVD/eigen/nullspace/mass: 0
- aggregate/capital-network/firm/outer/K1B/MATLAB/GE/annual/shock/IRF/welfare/Results: 0
- payoff clipping/annualization/rescaling/smoothing/risk adjustment/z-score: 0.

Scientific wall time: `192.17272720002802s`.

Evidence root:

`reports/ch5_mp4c_k1a_raw_ra0_path_b_turn1_31_province_fixed_price_one_step_cross_section_20260920_run001/`

Final manifest:

`748765BF21DE1F2205CBFAF0E1C1CB8DC7FB136DCA7887159B81FD833E574DE5`

with 392 entries and 11,360,241 bytes. Persisted independent readback passed; final external readback recorded zero bad paths. Pre/post scientific-code freeze matches. Persisted focused suite: 8 PASS.

## Timing clarification

The accepted CSV object `static_raw_S_transpose_ra0` at row `turn=1` is a **completed-turn-1 raw firm-return portfolio payoff counterfactual**. Under the frozen lagged timing law, it is the payoff object that would enter the **next** household iteration, not the entering payoff of outer turn 1.

This does not invalidate the cross-section experiment: the experiment deliberately used these values only as fixed-price safety stresses.

It does mean the next integrated corrected route must **not** copy this historical turn-1 vector directly into the entering turn-1 household state.

The corrected route must start from the accepted outer-turn-1 initialization state. Turn 1 then produces its own corrected household outputs, K1A capital allocation, firms and raw firm `ra0`. The adopted next-period payoff must be generated from that same corrected turn:

`rah_next = raw_ra0_by_destination @ S_destination_origin`.

This avoids mixing historical diagnostic household outputs with the corrected household route.

## Successor

The next active task is:

`tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_KFE_AND_K1A_C1_ONE_TURN_INTEGRATION_20260920.md`.

It executes exactly one initial corrected multi-province turn. It includes a full 31-province corrected household HJB-KFE batch from accepted turn-1 initial states and then one K1A/C1/source-faithful-labor/firm integration turn.

It does not run turn 2.

Results eligibility remains `FALSE`.
