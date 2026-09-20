# Chapter 5 corrected initial-turn full-closure acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_PASS__CORRECTED_INITIAL_TURN_FULLY_CLOSED__31_PROVINCE_HOUSEHOLD_KFE_AND_CANONICAL_K1A_C1_INTEGRATION__RAW_TURN2_PAYOFF_READY`

## Accepted candidate

- live-main baseline: `1257c15e6c91c3ae5d7f7184d381ff5289960dfa`
- Builder candidate: `3dfd610d94d0ef5dbf6874e33c6839a04c45d3fd`
- candidate tree reported/read back by Builder: `a8dd599222ed833754fa3c9fa216f87948760d20`
- ancestry independently verified: `1 ahead / 0 behind`, merge-base exactly baseline
- independently verified changed paths: 22
- CURRENT files: 0
- Builder did not merge main and did not publish a successor.

The candidate has been fast-forwarded into live `main`.

## Terminal acceptance

Accepted terminal:

`PASS__RUN004_ACCEPTED_31_PROVINCE_HOUSEHOLD_KFE__CANONICAL_SAME_S_INTEGRATION_REPLAY_PASS__RAW_NEXT_PAYOFF_READY__TURN2_NOT_RUN`

This closes exactly one corrected initial multi-province turn under the Owner-adopted unique-closed-class terminal KFE authority.

## Household binding

The successor integration replay bound the previously accepted run004 household evidence without rerunning household science.

Accepted facts:

- run004 sealed manifest:
  `CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`
- province terminal receipts: 31
- stationary aggregate receipts: 31
- accepted/reconstructed household batch identity:
  `8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05`
- household HJB/KFE/aggregate reruns in the integration replay: 0.

The 31/31 HJB, 31/31 adopted unique-closed-class KFE, and 31/31 aggregate results from run004 remain accepted.

## Canonical same-S payoff closure

The accepted economic law remains:

`rah_i = sum_j S[j,i] * raw_ra0_j`.

The canonical numerical evaluation is now frozen as ordered `math.fsum` over destination index `j=0..30` for each origin.

Accepted identities:

- raw firm ra0 SHA-256:
  `E8C85E4C29D44151C4D89D94F7F68136231917507ADECE30D5ACC7C322DF397A`
- exact K1A S SHA-256:
  `AC8DD36BB21E2B907D7521C98F8E65DCA3803291B54296AA7C2681E8CC6F226F`
- ordered product terms SHA-256:
  `19E65998D0A1F9BC65372B7C8364A9571FEA507642513C215C983A8E49358474`
- canonical payoff SHA-256:
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`
- orientation:
  `destination_by_origin`.

BLAS comparison differed by at most `2.220446049250313e-16`; only 15/31 entries were bitwise identical. This confirms why the prior bitwise cross-reduction guard was invalid. BLAS is diagnostic only.

## Integration accounting acceptance

All replay accounting gates passed:

- source update order;
- K1A share-column accounting;
- national private-capital conservation;
- home retained capital;
- C1 residual GovInv identity;
- firm-K accounting;
- all firm outputs finite;
- raw-ra0 finite;
- same exact S used for quantity and payoff;
- canonical raw-next-payoff finite;
- no payoff transformation.

Accepted national totals:

- origin private wealth: `127341904.64894083`
- destination private productive capital: `127341904.64894083`
- conservation residual: `0`
- total C1 GovInv: `2354651002.2516108`.

## Accepted turn-2 entering-state authority

The accepted turn-2 entering state is exactly:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json`

Git blob at acceptance:

`85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`.

Require:

- status `PASS`;
- rows: 31;
- exact active province order;
- classification on every row:
  `TURN2_INPUT_CANDIDATE_ONLY__TURN2_NOT_RUN`;
- raw-next-payoff SHA-256:
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`.

These rows are now accepted as the entering outer-turn-2 state authority for the next bounded task.

Turn 2 itself has not yet been executed.

## Scientific meaning

Accepted:

- one complete corrected initial multi-province turn;
- 31/31 corrected household HJB fixed points;
- 31/31 Owner-adopted unique-closed-class terminal KFE blocks;
- 31 stationary aggregate blocks;
- one K1A beta2 / beta_return0 + source-faithful labor + C1 + firm integration;
- one canonical raw-ra0 same-S payoff vector;
- exact 31-row turn-2 entering state.

Not established:

- outer fixed-point convergence;
- convergence of a multi-turn trajectory;
- K1B;
- K2;
- GE;
- Results.

## Evidence

Integration-replay evidence root:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/`

Sealed manifest:

`79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D`

with 17 entries and 126,733 bytes. Independent readback PASS.

## Route consequence

The next bounded scientific step is exactly one corrected turn-2 continuation.

It may use the accepted 31-row next-state receipt as entering turn 2, solve the 31 corrected household HJB/KFE blocks under the adopted terminal KFE authority, execute exactly one turn-2 integration, construct the canonical raw payoff for a possible future turn 3, and STOP.

No long trajectory, K1B, K2, GE or Results is authorized.
