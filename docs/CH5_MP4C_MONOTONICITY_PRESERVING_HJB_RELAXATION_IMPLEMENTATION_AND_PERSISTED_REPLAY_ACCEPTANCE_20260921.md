# Chapter 5 monotonicity-preserving HJB relaxation implementation and persisted replay — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTED__EXACT_PERSISTED_REPLAY_PASS__FRESH_RUNTIME_AUTHORIZED_NEXT`

Accepted terminal:

`PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTED__EXACT_PERSISTED_REPLAY_PASS__FRESH_HJB_NOT_RUN`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `94e174ef2c500b246106a848713c1af232c1cd80`
- candidate: `5dbd04ad4aaf252381283501d762d633f504ba07`
- candidate tree: `1cf9cdcbb3caf4d3f31f172c963ccf4c93f6a497`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- changed paths: 17
- production scientific source changes: exactly 2 authorized paths
- CURRENT changes by Builder: 0
- successor published by Builder: no
- remote SHA/tree readback: exact.

## Production implementation acceptance

The Owner-adopted law is implemented in one shared helper:

`monotonicity_preserving_relaxation(V_old,Vhat,b_nodes)`

defined in:

`src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py`

and reused by:

`src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py`.

The helper implements the adopted contract:

1. require corrected shape and finite inputs;
2. require finite strictly increasing b nodes;
3. test represented full candidate at alpha=1;
4. if needed test exactly alpha=2^-k for k=1,...,52;
5. construct relaxed states exactly as
   `(1-alpha)*V_old+alpha*Vhat`;
6. require all 760 represented raw b-edge slopes finite and strictly >0;
7. reject bitwise stagnation against V_old;
8. accept the first passing candidate;
9. fail closed on exhaustion with:
   `FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED`.

The alpha=1 branch returns the full candidate directly, preserving bitwise identity when no relaxation is required.

No derivative magnitude floor, clipping, alternate alpha schedule, adaptive Delta, second solve or tolerance change was added.

## HJB integration ordering

Both corrected HJB update paths invoke relaxation only after the existing unique direct solve has passed its existing backward-error gate.

The direct-solve artifact and receipt continue to describe the exact full linear-system solution Vhat.

A separate `relaxation_receipt.json` records the invariant-domain search and accepted nonlinear next state.

Thus:

- one full solve remains one HJB update;
- alpha checks are arithmetic post-processing under the adopted law;
- no additional solve or scientific retry is introduced;
- the accepted next nonlinear state may differ from Vhat only when alpha<1.

## Protected source authority

Changed production paths are exactly:

- `src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py`.

Exact unchanged blobs were verified for:

- selector.py
- cost.py
- generator.py
- option_a_step.py
- q1_kfe_validation.py.

The `_terminal_kfe` function source in the changed nonlinear file is also byte-source-equivalent under the recorded source hash.

No D1/D2/D3, selector, switching, root, grid, calibration or KFE law changed.

## Exact persisted replay

Using only accepted 黑龙江 persisted V_old and full direct-solve Vhat pairs:

| Update | accepted alpha | halvings | outcome |
| --- | ---: | ---: | --- |
| 0->1 | 1.0 | 0 | exact full-candidate passthrough |
| 1->2 | 1.0 | 0 | exact full-candidate passthrough |
| 2->3 | 0.5 | 1 | exact adopted relaxed state |

For 2->3:

- accepted SHA-256:
  `987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF`
- minimum raw b slope:
  `0.005032838660371801`
- positive / zero / negative edges:
  `760 / 0 / 0`
- value-change infinity norm:
  `0.017682618173863407`.

Every replay identity/scalar matches the accepted design-gate evidence.

## Focused and negative tests

Focused tests: 10/10 PASS.

The evidence covers:

- alpha=1 exact passthrough;
- one-halving exact persisted replay;
- nonfinite old/full rejection;
- wrong-shape rejection;
- bitwise-stagnation rejection;
- signed-zero representation handling under the adopted bitwise contract;
- exact 53-attempt exhaustion;
- strict rejection of zero slopes;
- acceptance of an arbitrarily small represented positive slope, confirming no positive magnitude floor.

`py_compile` and `git diff --check` are reported PASS.

## Scientific-call boundary

Accepted ledger:

- production relaxation helper calls on persisted pairs: 3
- new direct solves: 0
- HJB update executions: 0
- selector maps: 0
- production root helpers: 0
- D2/Q rebuilds: 0
- KFE/SVD: 0
- aggregate/integration: 0
- turn2 replay/rerun: 0
- turn3: 0
- MATLAB: 0
- GE/Results: 0
- retry/tuning: 0
- fresh scientific runtime: 0.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_implementation_persisted_replay_20260921_run001/`

- manifest SHA-256:
  `A2C9310E7BA2EB284F2D14B5E270739CC2CCDC9DD39A8FFEC2B0F362D3A3C51F`
- entries: 10
- bytes: 20,147
- independent readback: PASS
- bad paths: none.

## Reviewer decision

The implementation is accepted.

The Owner-adopted relaxation law is now both authority and implemented corrected-diagnostic behavior.

A fresh turn-2 run may now be executed from the exact accepted entering state.

The fresh runtime must start from the canonical turn-2 entering receipt, run provinces in canonical order, stop at the first new scientific failure, and if all 31 household/KFE blocks pass perform exactly one integration and stop before turn3.
