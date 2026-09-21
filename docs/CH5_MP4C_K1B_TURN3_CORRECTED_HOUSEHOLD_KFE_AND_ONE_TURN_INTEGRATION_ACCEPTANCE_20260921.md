# Chapter 5 K1B turn3 corrected household/KFE and one-turn integration — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__K1B_TURN3_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN4_INPUT_ACCEPTED`

Accepted Builder terminal:

`PASS__K1B_TURN3_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN4_K1B_INPUT_READY__TURN4_NOT_RUN`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `33e2177823fbdfd717c9a53b00c455047f91d86f`
- candidate: `1143cd8eb6e7722d7588107a0d69f68e8dd06df7`
- candidate tree: `9288af81b0c6f1abe53207fe695b7907eb48d046`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- production source changes: 0
- CURRENT changes by Builder: 0
- focused validator and test are task-specific and present
- pre/post production-source freeze is exact
- no successor was published by Builder.

The GitHub connector exposes the first paginated commit-file slice rather than all 4,760 paths, so the exact total-path count is supported by the Builder report and sealed evidence. Reviewer scope acceptance relies additionally on the accepted pre/post code-freeze receipts and the sealed evidence root, which show no production-source drift.

## Household HJB/KFE acceptance

All 31 provinces passed the corrected household HJB and unique-closed-class KFE authority.

Terminal checkpoint range:

`11..15`.

Maximum terminal metrics:

- Bellman B: `6.794251272701501e-11 <= 1e-8`
- value-change D: `6.750061443128175e-08 <= 1e-7`.

KFE ledger:

- SCC decompositions: 31
- restricted GESVD: 31
- normalized stationary candidates: 31
- full-Q stationarity checks: 31
- full-space 800x800 GESVD: 0.

No scientific retry or solver substitution occurred.

## Relaxation acceptance

- helper invocations: 377
- alpha candidates: 383
- alpha=1 accepted: 371
- alpha=0.5 accepted: 6
- other alpha: 0
- exhaustion: 0
- minimum accepted raw b slope: `7.672127670556508e-05` in 河南.

The six one-halving events are documented; no relaxation search caused another direct solve.

## Turn3 K1B integration acceptance

The integration reused the exact frozen turn3 K1B share plan:

`4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`.

Accepted accounting:

- source-faithful labor: exactly 1
- frozen K1B capital allocation: exactly 1
- C1 residual GovInv construction: exactly 1
- firm evaluations: 31
- wage / monetary / fiscal: 1 each
- origin private wealth: `140310000.0`
- destination private capital: `140310000.0`
- national private-capital residual: `0.0`
- home retained identity: PASS
- no same-turn share recomputation: PASS.

C1 GovInv total:

`2341682906.900551`.

Completed-turn3 raw `ra0` SHA-256:

`1C587932F4E8471209663D2262DB1BB308857EEEA1198D7868E4721CFB031E8F`.

The raw-return range is `[0.25385118409465646, 1.0844648167925854]`. Historical clipped/used return remains diagnostic only.

## Turn4 K1B candidate acceptance

Completed-turn3 raw returns were used only after the turn3 integration to prepare the next lagged K1B objects.

Population z-score:

- mean: `0.5185879356888632`
- std, ddof=0: `0.1907497808664968`
- z-score SHA: `67F06784094DAE4F6691AD79EA8107830FEF076CB1A2E28A96A34919E5122741`.

Frozen turn4 portfolio-share SHA:

`5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`.

Turn4 household payoff SHA:

`7DE65A71206F52AB3D2DA98D6D01C43A8A69D8B2C423BE49A15D5D287C434BE9`.

Classification:

`TURN4_K1B_INPUT_CANDIDATE_ONLY__TURN4_HOUSEHOLD_NOT_RUN`.

Turn4 household calls = 0. Same-turn feedback = 0.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001/`

- manifest entries: 4,724
- bytes: 63,722,204
- manifest SHA-256: `776F348F4BBF36587E2B484A10A00F96F6D01689322207A52A3770B93CDC03D9`
- independent readback: PASS
- bad paths: 0
- focused tests: 4/4 PASS
- production source pre/post freeze: exact.

## Route consequence

The first complete K1B-active corrected turn is accepted.

One successful K1B-active turn is not sufficient to claim outer numerical behavior. Because the K1B law, parameters, lag timing and next entering objects are already frozen and no new economic choice is required, Reviewer authorizes one further bounded K1B-active turn4 continuation before any longer outer path.

The next task must reuse the exact accepted turn4 input/share plan, execute at most one household/KFE batch plus one integration, prepare turn5, and stop before turn5 household.

K2, production-default replacement, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
