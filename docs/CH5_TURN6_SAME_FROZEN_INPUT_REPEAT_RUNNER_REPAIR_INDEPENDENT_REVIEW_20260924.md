# Independent Work review: turn6 same-input runner repair

Date: 2026-09-24 (Asia/Shanghai)

Verdict: `REJECT__TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR__PRE_EXECUTION_BLOCKERS__ZERO_SCIENCE`

## Candidate and accepted scope

Reviewed local candidate `c28340d4542e653cdf4e94ac4c11efe01e9c7c02`, parent `0713726f5044fe375e49e9daca794a30205a0549`. Its four changed paths match the repair allowlist, the worktree is clean, and `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. The preparation receipt's 34 file identity entries read back consistently. Thirteen focused static tests pass. The accepted sealed reference has 70/70 old-versus-old exact intermediate comparisons, including 31 KFE receipts and 31 mass-array NPZ files. No replay or other model/scientific call ran in this review. This validates preparation evidence only.

## Blocking findings

1. `run.py:345-354`: `compare_array()` leaves NumPy integer values in `max_index`. The real sealed C6 70-item self-comparison fails strict standard JSON serialization with `TypeError: Object of type int64 is not JSON serializable`. A successful future scientific run could therefore fail to persist its comparison receipt. Convert indices to Python `int` and test strict serialization of the complete result.
2. `run.py:275-303`: JSON comparison only checks numeric leaves. Changing the source labor `orientation` from `destination_by_origin` to `origin_by_destination` still yields `EXACT_BITWISE_MATCH`. Validate orientation, canonical province identity/order and required structural fields before a numeric match claim. Conflicts must be explicit `UNAVAILABLE` or legality defects; retain an exact scope label for what is compared.
3. `run.py:345-354`: finite but very large values can yield infinite subtraction. The comparator reports `LEGAL_DIFFERENCE_OBSERVED` with `inf`, then strict JSON persistence fails. Treat nonfinite differences as `UNAVAILABLE` and test this arithmetic case.
4. `run.py:409-490`: after the future gate passes and the output root is created, preflight writing, model import, hook setup and ledger creation occur outside the outer protected `try/finally`. A first exception can leave partial output without a terminal or exact zero/consumed ledger. Also, pre-call task/code hashes and grid/parameter setup at lines 491-496 do not produce the required zero-call `first_failure.json`. Cover every post-gate stage, preserve the earliest failure, restore monkeypatches, and keep an invalid future gate write-free.
5. `run.py:98-118`: the `completed_raw_ra0_vectors` trace marker is after the old integration function constructs `raw` and `used`, so this category is not guarded before its operation. Move its guard to an exact pre-construction entry and keep marker mismatch fail-closed. Verify all integration categories, aliases and exception reconciliation with static/stubbed tests, including actual task binding/restoration on success and failure. The current tests check only a source string and a single firm stub.

The corrected 31-province manifest binding and newly included intermediate receipts are useful, but the five findings prevent independent acceptance. A comparison scope limitation also remains: do not claim complete array equivalence for receipts that expose only totals or hashes, and explicitly classify any promised but unavailable intermediate.

## Next gate

Issue only a bounded, four-output-path, zero-science engineering repair. No one-shot repeat execution task, new budget, tolerance, stopping law, turn7 household, Results or model call is authorized. Work must independently ACCEPT/REJECT the next candidate before considering a separate one-shot execution task. Results eligibility remains `FALSE`.
