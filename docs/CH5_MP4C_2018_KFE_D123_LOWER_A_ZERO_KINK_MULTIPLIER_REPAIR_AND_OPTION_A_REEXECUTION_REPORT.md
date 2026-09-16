# CH5 MP4C 2018 KFE D1-D3 lower-a zero-kink multiplier repair and Option A reexecution

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_20260916`

## Verdict

`FAIL__OPTION_A_REEXECUTION_FIRST_CELL_NOT_ADMISSIBLE__STOPPED_WITHOUT_RETRY`

The authorized active lower-`a` zero-kink multiplier omission was repaired and verified. On fresh Option A reexecution, zero-based F-order cells 0–4 each returned one `SELECTED_ADMISSIBLE` policy using the repaired branch. The run then stopped at the first failing cell, flat index `5`, coordinate `(5,0,0)`, where the selector returned `NO_ADMISSIBLE_POLICY`.

The repaired active lower-`a` zero-kink candidates at cell 5 had nonempty multiplier/kink intersections and satisfied the repaired a-side law, but the two liquid derivative branches failed in opposite directions: the backward derivative produced `g_b>0`, while the forward derivative produced `g_b<0`. Both were rejected for `B_DERIVATIVE_DIRECTION_INCONSISTENT` under the unchanged selector contract.

Cells 6–799 were not executed. The full-map gate was not reached, so D2 assembly and the direct HJB solve remained zero. There was no repair, retry, alternate seed, tolerance change or continuation after the failure.

## Git identity and changed paths

- Fresh-fetched `origin/main`: `49af569233685ab082fff0e8a101c1129accc283`
- Branch: `codex/ch5-mp4c-2018-kfe-d123-lower-a-zero-kink-multiplier-repair-option-a-reexecution-20260916`
- Scientific-code Git HEAD before the first real selector call: `49af569233685ab082fff0e8a101c1129accc283`
- Candidate SHA convention: the final candidate SHA is returned after commit, non-force push and remote readback.

Exact changed paths:

- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py`
- `tests/test_mp4c_2018_kfe_d123_lower_a_zero_kink_multiplier.py`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/cell_0000.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/cell_0001.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/cell_0002.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/cell_0003.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/cell_0004.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/cell_0005.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/execution_ledger.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/execution_summary.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/manifest.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/post_execution_freeze_check.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/pre_execution_freeze.json`
- `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/preflight.json`
- `docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_REPORT.md`

No source-faithful/production code, cost law, generator, D2 tolerance, Option A seed, grid, calibration or Results material changed.

## Exact authorized repair

The selector now handles only `a_active`, lower-`a`, `regime=="zero_kink"` as follows:

1. form the raw D3 kink interval
   `[q_b*(1-chi_0), q_b*(1+chi_0)]`;
2. intersect it with the frozen lower-face multiplier domain `[p_a,+inf)`;
3. apply the prospectively fixed `_fp_bound(..., operations=16)` to the upper-endpoint comparison;
4. if nonempty, choose exactly `q_a=max(p_a,q_b*(1-chi_0))` and `lambda_a=q_a-p_a`;
5. persist `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN` plus the raw interval, deterministic minimum, arithmetic bound, chosen `q_a` and multiplier;
6. if empty, reject with `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERSECTION_EMPTY`.

The repair does not alter `c,l,d,cost,g_b,g_a,utility` or Hamiltonian for a fixed `q_b,d=0`. Slack lower-`a` retains `lambda_a=0`; upper-`a`, nonzero-transfer and liquid multiplier branches retain their previous behavior. Active-equality canonical-zero logic and D2 zero-tolerance semantics are unchanged.

## Focused preflight

Preflight was completed before the first real Option A selector call:

- 21 affected focused/synthetic tests: PASS;
- six new repair tests: PASS;
- `py_compile`: PASS;
- `git diff --check`: PASS;
- exact Option A file, field, scalar and grid hashes: PASS;
- exact 800-cell F-order enumeration and boundary adapter counts: PASS;
- slack lower-a, upper-a and nonzero-transfer unchanged tests: PASS;
- empty intersection fail-closed test: PASS;
- same-`q_b,d=0` consumed-policy identity test: PASS.

The pure arithmetic/source-bound Cell 0 preflight used no real selector and no root. It reproduced:

- `p_b^F=0.023046602641887657`
- `p_a^F=0`
- kink interval `[0.020741942377698892,0.025351262906076425]`
- chosen `q_a=0.020741942377698892`
- `lambda_a=0.020741942377698892`
- prospective upper-endpoint bound `3.5527136788005136e-15`
- nonempty intersection and exact canonical-min marker.

Synthetic preflight calls are tests of the isolated selector contract and are separate from the fresh real Option A execution ledger below.

## Frozen Option A identity

- Seed: `hjb100_initialization.mat:v0`
- Container: 13,362 bytes; SHA-256 `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`
- `v0`: shape `(20,20,2)`; F-order little-endian float64 SHA-256 `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665`
- Scalar binding: 2,732 bytes; SHA-256 `A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`
- Liquid grid field SHA-256: `A3FF663C18A2088A75B0E76C8ADA982EAF6D33ACFECB8DAA17C6D7DDE0533A76`
- Illiquid grid field SHA-256: `AE3A3A789FBC0DC9900B8153DEC717264C74AAB6FDA356C21C0EB22EEAC52567`
- Productivity grid field SHA-256: `A35F6FAB6E4564C6F4B1962A2ADE64E477F808432F747ABC7ACCF5E70B0B39B7`

No seed fallback or price/calibration recalculation occurred.

## Policy-map progress

| Flat F index | Coordinate | Outcome | Selected active set/regime | Cell roots |
|---:|---|---|---|---:|
| 0 | `(0,0,0)` | `SELECTED_ADMISSIBLE` | lower-a / zero-kink repaired canonical minimum | 4 |
| 1 | `(1,0,0)` | `SELECTED_ADMISSIBLE` | lower-a / zero-kink repaired canonical minimum | 0 |
| 2 | `(2,0,0)` | `SELECTED_ADMISSIBLE` | lower-a / zero-kink repaired canonical minimum | 0 |
| 3 | `(3,0,0)` | `SELECTED_ADMISSIBLE` | lower-a / zero-kink repaired canonical minimum | 0 |
| 4 | `(4,0,0)` | `SELECTED_ADMISSIBLE` | lower-a / zero-kink repaired canonical minimum | 0 |
| 5 | `(5,0,0)` | `NO_ADMISSIBLE_POLICY` | none | 0 |

The Cell 0 omission is therefore repaired in the real run: its active lower-a zero-kink candidate is admissible, has `q_a=lambda_a=0.020741942377698892`, and is the single selected consumed policy.

## First failing cell

- F-order flat index: `5`
- Coordinate: `(5,0,0)`
- State: `b=-0.1578947368421053`, `a=0`, `z=.8`
- `p_b^B=0.02256028269097067`
- `p_b^F=0.012481806039037598`
- valid lower-a derivative `p_a^F=-1.687538997430238e-15`
- candidates: 12
- admissible comparison count: 0
- roots: 0

The repaired active lower-a zero-kink comparison contains both legal liquid derivative branches:

| Liquid derivative branch | `q_b` | Chosen `q_a` | `lambda_a` | `g_b` | `g_a` | Rejection |
|---|---:|---:|---:|---:|---:|---|
| backward | `0.02256028269097067` | `0.020304254421873603` | `0.02030425442187529` | `3.3967923469887262` | `0` | `B_DERIVATIVE_DIRECTION_INCONSISTENT` because drift is forward |
| forward | `0.012481806039037598` | `0.011233625435133838` | `0.011233625435135525` | `-0.009203423814039269` | `0` | `B_DERIVATIVE_DIRECTION_INCONSISTENT` because drift is backward |

Both candidates persist the required canonical-min marker and nonempty raw intervals. Thus this terminal is not a recurrence of the repaired lower-a multiplier omission. It is a local liquid derivative-direction conflict for the frozen Option A derivative state at Cell 5. This report does not elevate that observation to HJB or equilibrium nonexistence.

## Gates not reached and call ledger

| Operation | Calls |
|---|---:|
| corrected policy maps started | 1 |
| real selector evaluations | 6 |
| scalar root invocations | 4 |
| passed cells | 5 |
| attempted cells | 6 |
| D2 generator assemblies | 0 |
| sparse direct HJB solves | 0 |
| selector evaluations on `V1` | 0 |
| nonlinear continuation | 0 |
| retries | 0 |
| KFE / MATLAB / outer / firm / wage-return | 0 |
| GE / annual / shock / IRF / Results | 0 |

Cells 6–799 are `NOT_EXECUTED_AFTER_FIRST_FAILURE`. No `V1` exists and the historical Cells 4/8/10 `V0/V1` diagnostics were not reached.

## Code freeze and evidence closure

Pre-execution hashes were written before real selector call 1. Post-execution readback reports `matches_pre_execution_freeze=true` for the entire corrected-diagnostic namespace and both focused Option A test files. No scientific code or test was modified after the first real selector call.

Frozen changed scientific identities:

- repaired selector SHA-256: `45C5B9156C2DCCC22AB2D85C068CBEE02F694F24BD2245720DE13BEE8AEC22AD`
- Option A execution driver SHA-256: `E827A68AA79814D249D78DCD500604EFE624E43225A6A911FC1BD5D0033A450E`
- repair focused test SHA-256: `1B88A5805E1489D3921851A12ADC4EA834C742C753E7E3B5748AC85144A4F374`

Evidence root:
`reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/`

The sealed manifest contains 11 entries totaling 145,700 bytes, covering preflight, freeze, six durable cell receipts, execution summary, ledger and post-freeze verification. Evidence was not overwritten or regenerated.

## Limitations and next gate

This candidate demonstrates that the authorized lower-a zero-kink multiplier repair works for Cell 0 and the next four cells, and preserves the first later fail-closed outcome. It does not authorize an additional derivative selection rule, root procedure, tolerance, seed, grid, calibration, D2 relaxation, retry or continuation.

Results eligibility remains `FALSE`; production is unchanged. This Builder does not merge `main` and does not publish a successor task. The next gate is independent Reviewer assessment of the candidate, the repaired Cell 0 receipt and the Cell 5 derivative-direction receipt.
