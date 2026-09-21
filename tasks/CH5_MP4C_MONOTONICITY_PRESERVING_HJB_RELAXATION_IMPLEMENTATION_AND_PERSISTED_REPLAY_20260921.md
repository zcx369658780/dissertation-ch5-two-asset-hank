# Task — monotonicity-preserving HJB relaxation implementation and exact persisted replay

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_20260921`

Status: `COMPLETED__ACCEPTED_PASS`

Results eligibility: `FALSE`

## Roles and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer / scientific-route authority. Codex is bounded Builder / scientific numerical analyst. GitHub live main is repository-state authority.

Absolutely do not enter, read, search, use or modify:

`zcx369658780/deep-learning-hank`.

## Owner-adopted authority

Read first:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_OWNER_ADOPTION_20260921.md`

Adopted marker:

`OWNER_ADOPTED__MONOTONICITY_PRESERVING_HJB_RELAXATION__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK`

This task implements that exact law only.

## Required reads

Fresh-fetch live main, then read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. Owner adoption above
6. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_SCIENTIFIC_DESIGN_GATE_ACCEPTANCE_20260921.md`
7. `docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_EMERGENCE_FORENSIC_ACCEPTANCE_20260921.md`
8. current nonlinear continuation and turn2 household integration source
9. this exact task.

## Scope

Implement the Owner-adopted global relaxation in the corrected-diagnostic HJB update path and validate it against the exact accepted persisted 黑龙江 update sequence.

This task includes:

- narrow production implementation;
- focused tests;
- exact persisted arithmetic replay through updates 0->1, 1->2 and 2->3;
- audit-receipt evidence;
- report and publication.

It does **not** include any fresh HJB solve or fresh turn2 execution.

## Production implementation contract

The implementation must expose one deterministic reusable relaxation helper whose inputs are:

- represented `V_old`;
- represented full direct-solve candidate `Vhat`;
- corrected grid / b nodes or equivalent exact spacing authority.

Required behavior:

1. verify both arrays finite and exact corrected shape;
2. reconstruct exactly the 760 raw b-edge finite differences from `Vhat`;
3. if all are finite and strictly >0:
   - accept alpha=1;
   - return Vhat unchanged/bitwise identical;
4. otherwise test `alpha=2^-k`, `k=1,...,52`, in exact order;
5. construct candidate exactly as:
   `(1-alpha)*V_old+alpha*Vhat`;
6. recompute all 760 represented raw b-edge slopes;
7. accept the first candidate satisfying:
   - every slope finite;
   - every slope >0;
   - candidate not bitwise identical to V_old;
8. on exhaustion, fail closed with:
   `FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED`.

Persist/return enough structured diagnostics for the required audit receipt.

No derivative magnitude floor.

No alternate alpha schedule.

No adaptive ceiling.

No outcome-specific exception.

## Integration into HJB update path

Integrate the helper **after** the one full implicit direct solve has passed the existing backward-error gate and **before** the returned next nonlinear state is accepted.

The direct-solve receipt must continue to describe Vhat, the actual full linear-system solution.

The HJB update ledger increments once for the full direct solve, exactly as before.

Arithmetic alpha checks are not scientific retries and do not cause additional direct solves.

The accepted next state may therefore differ from the direct-solve `next_value`; persist a distinct relaxation receipt and accepted-next-state identity when alpha<1.

Do not relabel the relaxed state as the exact frozen linear-system solution.

## Authorized production source paths

Production scientific changes are limited to the minimum necessary subset of:

- `src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py`

Prefer one shared implementation rather than duplicated scientific logic.

If a new helper module is strictly necessary to avoid duplication, STOP and report the proposed path before creating it; do not silently widen production scope.

No selector, cost, generator, D1/D2/D3 or KFE source may change.

## Exact persisted replay gate

Use accepted persisted 黑龙江 artifacts from:

`reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921/household/p07_黑龙江/`

Do not perform any new linear solve.

For each update 0->1, 1->2, 2->3:

- load exact V_old;
- load exact persisted direct-solve Vhat;
- call the new production relaxation helper only;
- persist the helper receipt;
- compare against the accepted design-gate arithmetic evidence.

Required exact outcomes:

### 0->1

- accepted alpha: `1.0`
- halvings: `0`
- accepted state bitwise equals persisted full candidate
- all 760 slopes strictly positive.

### 1->2

- accepted alpha: `1.0`
- halvings: `0`
- accepted state bitwise equals persisted full candidate
- all 760 slopes strictly positive.

### 2->3

- accepted alpha: `0.5`
- halvings: `1`
- accepted state SHA-256:
  `987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF`
- minimum raw b slope:
  `0.005032838660371801`
- positive edges: `760`
- negative edges: `0`
- zero edges: `0`
- value-change infinity norm:
  `0.017682618173863407`.

The replay is an implementation-parity gate, not a scientific HJB continuation.

## Required negative tests

At minimum prove:

- alpha=1 path returns Vhat bitwise unchanged;
- one-halving path returns exact accepted 2->3 replay identity;
- nonfinite V_old or Vhat rejects;
- wrong shape rejects;
- represented stagnation does not pass;
- exhaustive/no-pass condition raises the exact adopted terminal;
- a zero raw b slope fails strict positivity;
- no positive magnitude floor is present.

A synthetic exhaustion/stagnation fixture may be used; do not alter scientific data to manufacture a runtime result.

## Source-preservation gates

Require exact unchanged blobs for at least:

- selector.py
- cost.py
- generator.py
- option_a_step.py derivative law
- terminal KFE implementation
- D1/D2/D3 authority code.

Require:

- `py_compile` PASS for changed/new Python;
- focused tests PASS;
- `git diff --check` PASS;
- production changed-path set within the authorized source paths.

## Scientific-call boundary

Fresh scientific runtime is forbidden.

Counts must remain:

- new direct linear solves: 0
- HJB update executions: 0
- selector maps: 0
- production root-helper calls: 0
- D2/Q rebuild: 0
- KFE/SVD: 0
- aggregates/integration: 0
- turn2 replay/rerun: 0
- turn3: 0
- MATLAB: 0
- GE/Results: 0
- scientific retry/tuning: 0.

Calling the new arithmetic relaxation helper on accepted persisted V_old/Vhat pairs is authorized and is not a scientific model invocation.

## Allowed non-production paths

Focused tests:

`tests/test_mp4c_monotonicity_preserving_hjb_relaxation_implementation.py`

Validator:

`validators/multi_province/monotonicity_preserving_hjb_relaxation_implementation_persisted_replay/**`

Fresh evidence:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_implementation_persisted_replay_20260921_run001/`

Report:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_REPORT.md`

Do not modify CURRENT.

Do not publish a successor.

## Required terminal

Success:

`PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTED__EXACT_PERSISTED_REPLAY_PASS__FRESH_HJB_NOT_RUN`

Any mismatch or scope violation must fail closed with precise evidence.

## Required evidence

Persist:

- authority/source binding;
- production diff/source-freeze receipt;
- focused tests;
- exact helper contract;
- three-update persisted replay receipts;
- exact 2->3 accepted-state identity;
- negative-test receipt;
- scientific-call ledger;
- sealed manifest/readback;
- report.

Commit + ordinary non-force push, then STOP.
