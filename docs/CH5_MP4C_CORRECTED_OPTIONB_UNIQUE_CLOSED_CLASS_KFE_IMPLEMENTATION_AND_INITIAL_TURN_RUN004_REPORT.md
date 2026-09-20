# Chapter 5 Owner-adopted unique-closed-class KFE implementation and run004

## Terminal verdict

`FAIL__RAW_NEXT_PAYOFF_SAME_S_IDENTITY`

The Owner-adopted unique-closed-class support KFE was implemented and passed exact Beijing parity. The fresh run004 then completed all 31 province household HJB and terminal KFE blocks. The single authorized integration turn stopped at its first failure: the bitwise same-S replay check compared BLAS `raw_ra0 @ S` with a separately ordered column sum and returned false. No tolerance was changed and no scientific retry was run.

## Authority and implementation

- Actual live-main baseline: `3a78812434ba2783b08919b55a3fe93f4788f725`.
- Implementation paths: `nonlinear_continuation.py`, `optionb_initial_turn_integration.py`, and the focused test file only.
- The KFE uses one exact-positive SCC analysis, the unique closed-class restriction `Q_CC`, one restricted dense `gesvd(Q_CC.T)`, both frozen threshold views, the smallest restricted right singular vector, one sign orientation, one normalization, strict-positive closed support, exact positive-zero transient embedding, and one original full-Q `Q.T @ p`.
- Full-space 800-state dense GESVD calls: `0`.
- Scientific code pre/post freeze: exact match.

## Beijing implementation parity

Parity status: `PASS`.

- Q12 SHA-256: `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`.
- Closed members: F-order flat indices `200..399` and `600..799`.
- `Q_CC`: `400 x 400`, nnz `1537`.
- Restricted spectrum SHA-256: `9981787A127FFCB774E0C6A312DF72A2D13C5385681927E2C0DBCDC9D0D082B6`.
- Local and inherited rank/nullity: `399/1` and `399/1`.
- Closed candidate SHA-256: `649481483AA0DD54081ACD9C3419B926EF94D0C3CC3637F2412D13F31F0D0C48`.
- Embedded full candidate SHA-256: `5D7DA01D02C8EA711CD43AE5CD3FBF14107CE8394B97BE2E7AE1C904EDC658E0`.
- Full-Q residual SHA-256: `B450EB9F97A3CDB66FDD24C7FE2DD9BB3997E834738572CFC1AA9BE69FFFDC71`.
- Separate parity ledger: topology `1`, restricted GESVD `1`, normalized candidate `1`, full-Q multiplication `1`, full-space GESVD `0`, HJB/policy/D2 `0`, retries `0`.

## Fresh run004 household result

All `31/31` province household blocks passed HJB convergence and terminal KFE.

- Final checkpoint distribution: checkpoint 11: `6`; 12: `16`; 13: `7`; 14: `2`.
- Same-checkpoint B range: `1.839361996047728e-13` to `1.0435691200072483e-10`.
- Same-checkpoint D range: `1.8187873429553747e-10` to `9.787390053972445e-08`.
- Maximum direct-solve normwise backward error: `3.8614220703856567e-16`.
- Unique closed-class sizes: 320: `5`; 360: `15`; 400: `8`; 480: `2`; 640: `1`.
- Minimum closed-support probability mass across provinces: `4.4726907762316044e-10`, strictly positive.
- Maximum full-Q stationarity infinity norm: `3.2439329000766293e-16`.
- Every province has exact per-checkpoint histories and a `province_terminal_receipt.json` under the run004 evidence root.

## Integration and exact first failure

The 31-row household batch was constructed once. The integration consumed source-faithful labor reconstruction `1`, K1A with `beta_distance=2` and `beta_return=0` `1`, C1 residual GovInv `1`, firm evaluations `31`, composite wage `1`, monetary assignment `1`, fiscal diagnostics `1`, and raw next-payoff same-S construction `1`.

The terminal failure occurred at the pre-persistence identity guard:

```python
rah_next = raw_ra0 @ shares
replay = np.sum(raw_ra0[:, None] * shares, axis=0)
np.array_equal(rah_next, replay)
```

The guard returned false because the two floating-point accumulation orders were required to be bitwise equal. The task forbids post-hoc tolerance changes and scientific retries, so no raw-next-payoff receipt or next-state candidate was accepted.

## Exact run004 scientific ledger

| Call | Count |
|---|---:|
| source-native initializations | 31 |
| labor roots attempted / returned | 24,800 / 24,800 |
| corrected policy maps / D2-Q assemblies | 408 / 408 |
| selector evaluations | 326,400 |
| scalar / interior-z / interior-a / joint roots | 130,333 / 24,265 / 392 / 49 |
| direct HJB updates / post-update checkpoint evaluations | 377 / 377 |
| SCC decompositions | 31 |
| restricted dense GESVD | 31 |
| full-space 800 dense GESVD | 0 |
| normalized candidates / full-Q `Q.T@p` | 31 / 31 |
| corrected aggregate evaluations | 31 |
| household batch | 1 |
| labor / K1A / C1 | 1 / 1 / 1 |
| firm evaluations | 31 |
| wage / monetary / fiscal | 1 / 1 / 1 |
| raw-next-payoff same-S construction | 1 |
| scientific retries / solver substitutions | 0 / 0 |
| turn 2 / second outer turn / K1B / K2 / adaptive controller | 0 / 0 / 0 / 0 / 0 |
| MATLAB science / GE-annual-shock-IRF-welfare-Results | 0 / 0 |

Historical run001/run002 consumption remains read-only in the lineage receipt and is not included in the run004 ledger.

## Evidence and checks

- Evidence root: `reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004/`.
- Sealed manifest SHA-256: `CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`.
- Manifest: `4,353` entries, `61,650,777` bytes.
- Independent readback: `PASS`, bad paths `0`.
- Focused tests: `15 passed`.
- `py_compile`: PASS.
- `git diff --check`: PASS.
- Turn 2 was not run. CURRENT files were not modified. No successor was published. Main was not merged.
