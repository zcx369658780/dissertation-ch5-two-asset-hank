# Chapter 5 monotonicity-preserving HJB relaxation fresh turn-2 run005 — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__TURN2_RUN005_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION_PASS__RAW_TURN3_INPUT_READY`

Accepted terminal:

`PASS__MONOTONICITY_PRESERVING_RELAXATION_FRESH_TURN2_RUN005__31_PROVINCE_HJB_KFE_AND_INTEGRATION_PASS__RAW_TURN3_PAYOFF_READY__TURN3_NOT_RUN`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `8e9ad015aa01ff1c7a0ca42c6cf2150942aaeca3`
- candidate: `45e2e1f0f50c8e681d13e4e22fba4b50a90c8aad`
- candidate tree: `3e968037948124b23887ee4ae3fbd597e4738383`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- production source diff: empty
- CURRENT diff: empty
- successor published by Builder: no.

The candidate contains only the authorized fresh validator/test/report and fresh run005 evidence.

## Entering-state authority

Run005 binds exactly to:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json`

with:

- Git blob:
  `85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`
- file SHA-256:
  `E519E468B04D7EDC631F6A931FF367A7EDE5C3D510ED4E0979AB2FC8E13C5E11`
- entering raw payoff SHA-256:
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`
- 31 rows in exact canonical province order.

## Household HJB/KFE result

All 31 provinces pass the adopted corrected HJB and terminal unique-closed-class KFE authority.

Terminal checkpoints:

`[12,12,16,12,15,12,12,12,12,12,12,12,12,12,13,14,12,12,12,12,11,12,12,12,12,11,12,12,12,12,12]`

Across all 31 terminal states:

- maximum Bellman metric:
  `9.982478732517563e-11`
- maximum value-change metric:
  `9.97679068248658e-08`
- direct HJB updates:
  `380`
- SCC decompositions:
  `31`
- restricted GESVD:
  `31`
- normalized stationary candidates:
  `31`
- full-Q stationarity checks:
  `31`
- full-space 800x800 GESVD:
  `0`
- scientific retries:
  `0`
- solver substitutions:
  `0`.

No scientific failure occurred.

## Relaxation runtime evidence

The adopted relaxation helper is invoked 380 times.

- alpha candidates evaluated: 386
- accepted alpha=1: 374
- accepted alpha=0.5: 6
- exhaustion/failure: 0.

Exactly six updates require one halving:

- 黑龙江: 2
- 山东: 2
- 青海: 2.

No update requires more than one halving.

### 黑龙江 runtime parity

Normal runtime, without extra solve or selector calls, reproduces the accepted implementation replay:

- checkpoint0->1: alpha=1
- checkpoint1->2: alpha=1
- checkpoint2 full Vhat SHA-256:
  `1FA95217C9EEFDAA638F0CD07F00B59B053EB4A59E5670A0CED94852922DBFE7`
- checkpoint2->3: alpha=0.5
- accepted relaxed state:
  `987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF`
- minimum accepted raw b slope:
  `0.005032838660371801`.

The subsequent relaxed 黑龙江 trajectory converges and its terminal KFE passes.

## One-turn integration

Exactly one integration is performed after all 31 household/KFE blocks pass.

Accepted checks:

- source-update order
- share-column conservation
- home retained
- national private-capital conservation
- C1 residual
- finite firm outputs
- canonical same-S raw-next-payoff construction.

Key totals:

- origin private wealth:
  `140310000.0`
- destination private capital:
  `140310000.0`
- national private-capital residual:
  `0.0`
- labor destination total:
  `157407315.40224046`
- K1A beta_distance:
  `2.0`
- K1A beta_return:
  `0.0`.

Completed-turn-2 raw firm payoff SHA-256:

`B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951`

Canonical K1A raw turn-3 household payoff SHA-256:

`5996A20CEE227389A7975703452EA6DAF1A2F817C517FFE43BEF3A53FA4292E2`.

The persisted turn-3 state has 31 canonical rows and remains classified:

`TURN3_INPUT_CANDIDATE_ONLY__TURN3_NOT_RUN`.

No turn3 household, K1B, K2, GE or Results work occurred.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005_20260921/`

- manifest SHA-256:
  `C93BF19DB7C909A50C2753B0EA06FD4735F48A4C41C5A4C9CA6F8817B693B72F`
- entries: 4,752
- bytes: 64,191,647
- independent readback: PASS
- bad paths: 0
- readback scientific calls: 0.

Pre/post production-source freeze is exact.

Focused tests: 3/3 PASS.

## Scientific route consequence

The roadmap condition requiring a bounded corrected multi-turn prefix before reopening K1B is now satisfied by the accepted corrected turn-1 and turn-2 sequence.

K1B is therefore eligible to enter its preregistered lagged-return **safety/activation gate**.

This does not authorize K1B household runtime yet.

The next task is zero-science and must construct and validate the exact turn-3 K1B lagged-return share/payoff candidate before any turn-3 HJB execution.
