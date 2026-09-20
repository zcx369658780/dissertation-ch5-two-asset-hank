# Chapter 5 corrected Option-B initial-turn 31-province integration report

Date: 2026-09-20

## Terminal verdict

`FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY`

The bounded run stopped at the first reached province, Beijing (`province_index=0`), after the source-native initialization and the initial corrected policy/D2 map. The first failing object was the checkpoint-0 policy-diagnostics composition. The accepted helper `_policy_diagnostics` requires iterable previous-policy rows and arrays, while the new initial-checkpoint caller supplied `None`. Python raised `TypeError: 'NoneType' object is not iterable`.

The failure occurred after scientific state advancement, so the task was not rerun and the driver was not patched after the code freeze. This report does not classify the Beijing HJB numerics, because no direct HJB update or post-update checkpoint evaluation was reached.

## Authority and provenance

- Fresh live-main baseline: `5e0eb950298351880f22b15edebc242f66e143b7`.
- Execution code-freeze commit: `ab3718c50b6877307a84251238dfd17e3f7b05de`.
- Initialization CSV Git blob: `5bb902183c8cb313d986ee5a9f8bd6b7c0624ae1`.
- Source-native initialization Git blob: `19ba32b0c5534f2726036ab8ba30fb204e359325`.
- K1A Git blob: `ac309b4dbe9f6b3ca1d3cfc691223600835d17b6`.
- C1 Git blob: `ba717dfdada1b47ee44af5562d3ffa01a9de8cfe`.
- All startup authority, clean-worktree, ancestry, focused-test and live-main checks passed.
- The pre/post scientific-code hash maps match exactly.

The initialization CSV contained exactly 31 rows in the accepted province order. All 31 `outer_turn_1_initial_state_json` objects parsed and bound before science. Only Beijing was reached scientifically.

## Reached scientific objects

### Beijing source-native initialization

- Initial value SHA-256: `92C09D3DB6976DE2093795AB2BEF1DF7164AB7F1F71136E30FF23B88275BDD56`.
- Baseline labor SHA-256: `69FF48AAB0414A4219E9F0174CB03C73EE0DEC33D48996B35B36FF8EDCB1EE81`.
- Scalar labor roots: `800/800` attempted/returned.
- Initialization retries: `0`.

### Beijing checkpoint 0 policy and D2/Q

- Selector outcomes: `800/800` admissible.
- Canonical policy identity: `E09671771A95DFAF5EF8D7AFC9F980DB72125AEBF9D2B1297FC3FA2BBBD1B7FA`.
- Selector roots: `483` total, including `206` interior-Z roots; interior-a and joint switching roots were `0`.
- D2 status: `PASS`.
- Q artifact SHA-256: `CFD13AD522809781A5DB46EF9BEC3565F79CDFBD2963BD3B7A6CB8CD742383C4`.
- Q CSR identity `(data, indices, indptr)`:
  - `00CBA4837671E13F78690AB99D97E83A2B1BED5A64D0AE95D325FF4EAAA9EF83`
  - `2A808A155EBBC90C839EF4B7335DD4A311D1B12FF1090D290B3A9F8BBDBD49EA`
  - `8EADEA08EACF738B98AA92E98F197D80C0B08819EA7ADDAC3DB0E495B831CB6D`
- Minimum off-diagonal: `0.26429466880683106`.
- Maximum `|Q @ 1|`: `3.552713678800501e-15`, within prospective bound `5.6259958580641315e-14`.
- All D2 boundary, coordinate-action, conservation and nonnegative-offdiagonal checks passed.

The 800 verbose cell receipts were projected after termination into deterministic policy arrays and hashes, then removed. This post-terminal evidence operation made zero selector, root, D2/Q or HJB calls.

## HJB/KFE and integration status

- Direct HJB updates: `0`; therefore no direct-solve backward error exists.
- Post-update checkpoint evaluations: `0`; therefore no `B/D`, primary convergence or cycle classification exists.
- Terminal SCC/GESVD/stationary-mass operations: `0`.
- Corrected aggregates: `0`.
- Province household PASS count: `0/31`; Beijing was not classified PASS or scientific FAIL because the engineering exception occurred before the first update.
- `PreFrozenHouseholdOutputBatch`: not constructed.
- Source-faithful labor, K1A, C1, firm, wage, monetary, fiscal and raw-next-payoff operations: all `0`.
- Integration accounting and `rah_next_raw = raw_ra0_turn1 @ S`: not reached and unavailable.

## Exact scientific ledger

| Object | Count |
|---|---:|
| Source-native initializations | 1 |
| Labor roots attempted / returned | 800 / 800 |
| Corrected policy maps | 1 |
| Selector evaluations | 800 |
| Selector scalar roots | 483 |
| Interior-Z roots | 206 |
| Interior-a / joint switching roots | 0 / 0 |
| D2/Q assemblies | 1 |
| Direct HJB updates | 0 |
| Post-update HJB checkpoint evaluations | 0 |
| SCC / dense GESVD / normalized mass / `Q.T@p` | 0 / 0 / 0 / 0 |
| Aggregate evaluations / household batches | 0 / 0 |
| Labor / K1A / C1 | 0 / 0 / 0 |
| Firm evaluations | 0 |
| Wage / monetary / fiscal batches | 0 / 0 / 0 |
| Raw-next-payoff constructions | 0 |
| Scientific retries / solver substitutions | 0 / 0 |
| Turn-2 household / second outer turn | 0 / 0 |
| K1B / K2 / adaptive controller | 0 / 0 / 0 |
| MATLAB / GE-annual-shock-IRF-welfare-Results | 0 / 0 |
| Payoff transformations or repair | 0 |

## Engineering verification and evidence

- Focused tests: `39 passed`.
- `py_compile`: PASS.
- `git diff --check`: PASS before the code-freeze commit.
- Evidence root: `reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_k1a_c1_one_turn_integration_20260920_run001`.
- Sealed manifest SHA-256: `F447D5DF30D302963D81EB09E68BEC72C1B89F8C1DE227936533045F9A16F315`.
- Manifest entries / bytes: `14` / `109,026`.
- Independent readback: `PASS`, bad paths `0`.

Turn 2 was not run. No CURRENT file was modified, no successor was published, and main was not merged.
