# Chapter 5 corrected Option-B initial-turn run001 engineering-exception acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_FAIL__CHECKPOINT0_DIAGNOSTIC_COMPOSITION_EXCEPTION__SCIENTIFIC_OBJECTS_PRESERVED__REPAIR_AND_FRESH_REEXECUTION_AUTHORIZED`

## Accepted failed candidate

- live-main baseline: `5e0eb950298351880f22b15edebc242f66e143b7`
- Builder candidate: `159786968d2bb47c12b0b7b88ed8aeaa6d0e8bdf`
- candidate tree reported/read back by Builder: `179fbaf365c525eeae6180e7bb831bc10ea8810f`
- ancestry independently verified: `2 ahead / 0 behind`, merge-base exactly the baseline
- independently verified changed paths: 19
  - opt-in driver: 1
  - focused test: 1
  - report: 1
  - compact evidence: 16
  - CURRENT files: 0
- main was not merged by Builder and no successor was published by Builder.

The candidate has been fast-forwarded into live `main` by the Reviewer as accepted failed-run evidence and as the repair baseline.

## Failure classification

Builder terminal:

`FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY`

The first failing object is:

`province_index=0 / 北京 / checkpoint=0 / INITIAL_CHECKPOINT_POLICY_DIAGNOSTICS`.

The exception is exactly:

`TypeError: 'NoneType' object is not iterable`.

This is accepted as an engineering composition defect in the new opt-in driver, not a scientific failure of the Beijing household problem.

The new driver initialized:

- `previous_rows=None`
- `previous_arrays=None`
- `previous_q=None`

and then called the accepted comparative helpers `_policy_diagnostics` and `_operator_diagnostics` unconditionally at checkpoint 0. Those helpers require an actual previous checkpoint.

The already accepted nonlinear-continuation route independently establishes the correct representational pattern: the initial checkpoint uses current-only policy/Q identities and marks previous-checkpoint comparison fields as unavailable; comparative diagnostics begin only after a prior checkpoint exists. Adopting that pattern introduces no new equation, economic law, boundary/KKT rule, solver, parameter, tolerance or calibration choice.

## Scientific ledger accepted for run001

Reached science before the engineering exception:

- source-native initializations: 1
- scalar labor roots: 800/800
- corrected policy maps: 1
- selector evaluations: 800
- selector scalar roots: 483
- interior-Z roots: 206
- interior-a/joint roots: 0/0
- D2/Q assemblies: 1
- direct HJB updates: 0
- post-update HJB checkpoints: 0
- SCC/GESVD/stationary mass/`Q.T@p`: 0/0/0/0
- aggregates/integration/firm: 0
- turn 2 / K1B / K2 / MATLAB / GE / Results: 0
- scientific retries: 0
- solver substitutions: 0.

Beijing checkpoint-0 policy map was 800/800 admissible and D2/Q passed its legality/conservation diagnostics. Because no direct HJB update occurred, no B/D convergence, cycle, backward-error or KFE conclusion is accepted for Beijing.

## Evidence acceptance

Accepted run001 evidence root:

`reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_k1a_c1_one_turn_integration_20260920_run001/`

Sealed manifest:

`F447D5DF30D302963D81EB09E68BEC72C1B89F8C1DE227936533045F9A16F315`

with 14 entries and 109,026 bytes. Independent readback is PASS. Pre/post code-freeze identities match.

Focused tests reported 39 PASS; `py_compile`, `git diff --check` and `git show --check` passed.

## Route consequence

Run001 closes as accepted failed evidence. It does not establish a household HJB failure and does not change any accepted scientific authority.

A successor may repair only the initial-checkpoint diagnostic representation in the new opt-in driver, add regression coverage, freeze code, and perform one fresh bounded reexecution of the same scientific task.

The predecessor scientific calls remain part of history and are not relabeled or erased. The successor has its own explicitly published budget and allows no in-task scientific retry.

Turn 2, K1B, K2, GE and Results remain closed. Results eligibility remains `FALSE`.
