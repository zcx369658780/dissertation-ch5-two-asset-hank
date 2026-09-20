# Chapter 5 run004 31-province household/KFE pass and raw-next-payoff reduction-order guard acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_FAIL__31_PROVINCE_HOUSEHOLD_AND_ADOPTED_KFE_PASS__RAW_NEXT_PAYOFF_BITWISE_REDUCTION_ORDER_GUARD_FAIL__INTEGRATION_ONLY_REPLAY_AUTHORIZED`

## Accepted candidate

- live-main baseline: `3a78812434ba2783b08919b55a3fe93f4788f725`
- Builder candidate: `af770c1fb787098569df2a25471cdc8101eda3a3`
- candidate tree reported/read back by Builder: `84450e8649e19553a568fa60e7a7f706c6787546`
- ancestry independently verified: `1 ahead / 0 behind`, merge-base exactly the baseline
- GitHub compare interface returned a capped file list with no CURRENT paths; Builder remote readback reports the full task diff as the authorized implementation/test/report plus run004 evidence root
- Builder did not merge main and did not publish a successor.

The candidate has been fast-forwarded into live `main`.

## Adopted KFE implementation acceptance

The Owner-adopted unique-closed-class support KFE implementation is accepted.

Beijing implementation parity passed against the previously accepted method-candidate evidence.

Fresh run004 established:

- household HJB PASS: `31/31`
- adopted terminal KFE PASS: `31/31`
- corrected stationary aggregates produced: `31/31`
- one exact 31-province household batch constructed.

Accepted run004 household-batch identity:

`8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05`

Scientific summary:

- final HJB checkpoint distribution: 11 -> 6, 12 -> 16, 13 -> 7, 14 -> 2
- B range: `1.839361996047728e-13` to `1.0435691200072483e-10`
- D range: `1.8187873429553747e-10` to `9.787390053972445e-08`
- maximum direct-solve backward error: `3.8614220703856567e-16`
- unique closed-class sizes observed across provinces: 320, 360, 400, 480, 640
- minimum closed-support mass across provinces: `4.4726907762316044e-10 > 0`
- maximum full-Q stationarity infinity norm: `3.2439329000766293e-16`
- full-space 800x800 GESVD calls: `0`.

The run004 evidence root contains exactly 31 province terminal receipts and 31 stationary aggregate receipts under the adopted KFE authority.

These household/KFE results are accepted and do not need to be rerun for the immediate integration repair successor.

## Integration failure classification

The single authorized integration turn reached:

- household batch construction: 1
- source-faithful labor reconstruction: 1
- K1A allocation: 1
- C1 residual GovInv construction: 1
- firm evaluations: 31
- composite wage batch: 1
- monetary assignment: 1
- fiscal diagnostic batch: 1
- raw-next-payoff construction: 1.

The first failing guard was:

`FAIL__RAW_NEXT_PAYOFF_SAME_S_IDENTITY`.

The code compared:

`raw_ra0 @ S`

against:

`np.sum(raw_ra0[:, None] * S, axis=0)`

using `np.array_equal`.

These are the same adopted mathematical same-S payoff law with different floating-point reduction orders. Bitwise equality between the two reduction implementations is not an economic or accounting identity.

No evidence indicates an S-orientation mismatch, payoff transformation, K1B feedback, or altered raw-ra0 law.

The failure is therefore accepted as an engineering/numerical identity-guard defect, not a failure of the adopted payoff equation.

Because the guard fired before the remaining integration accounting block completed, the run004 integration turn is **not** accepted as closed. Raw-next-payoff and next-state candidate remain unaccepted outputs.

## Canonical numerical designation for successor

The adopted economic payoff law remains unchanged:

`rah_i = sum_j S[j,i] * raw_ra0_j`.

For the successor integration replay, the canonical numerical evaluation is designated as a deterministic per-origin `math.fsum` over the 31 destination terms in ascending destination index order:

`rah_i = math.fsum(float(raw_ra0[j]) * float(S[j,i]) for j in range(31))`.

This is a numerical implementation designation of the already adopted sum, not a payoff-law change.

The successor must prove same-S identity by provenance and deterministic term construction:

- exact raw-ra0 vector identity;
- exact S identity from the K1A quantity allocation;
- destination-by-origin orientation;
- canonical ordered product-term hash;
- canonical fsum result.

A BLAS `raw_ra0 @ S` replay may be recorded only as a non-gating diagnostic. Bitwise equality to BLAS is not required.

No ad-hoc tolerance, payoff clipping, rescaling, smoothing, annualization, z-score, or risk adjustment is authorized.

## Evidence

Run004 root:

`reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004/`

Sealed manifest:

`CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`

with 4,353 entries and 61,650,777 bytes. Independent readback PASS.

## Route consequence

The next task is integration-only.

It must bind the accepted run004 31-province household batch and per-province aggregates, reconstruct the exact batch without rerunning household science, implement the canonical same-S sum, and replay exactly one integration turn.

No HJB, policy, D2, SCC, KFE SVD, stationary-mass solve, or aggregate evaluation is authorized in that successor.

Turn 2, K1B, K2, GE and Results remain closed. Results eligibility remains `FALSE`.
