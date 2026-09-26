# Independent final authority-chain review - one new C9 attempt

Reviewer: GPT Work
Verdict: ACCEPT__C9_POST_FAILURE_NEW_ATTEMPT_FINAL_CHAIN_FOR_DISPATCH_ONLY
Scope: committed R/C/O/T identity and permission for one bounded dispatch only; no scientific result is accepted here.

The Builder's two-path T candidate is `0377c534f51a268470d57e23b625938d629c9e25`, parent `e3ae3a73e3615c44c53490f17917f8867468d0fd`, tree `d4a467b5d8984937f406a2bfb1c687ea1b27f7dc`, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. It changed only `TASK_CURRENT.md` and `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION.md`. Both working bytes and their respective committed `HEAD:path` bytes equal the fixed draft, raw SHA-256 `EE1BDC60CAC5450FAB1C860FD292AA32ED65AD17E070856D8B5A9DDB64DAB67A`.

## Exact chain

| Node | Committed path | Raw SHA-256 |
| --- | --- | --- |
| R | `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_RUNNER_INDEPENDENT_REVIEW.md` | `9C62625C648B9C33F4DFFF2CA8539C611EB96411E95D2858832C12A1527AF67E` |
| C | `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT.json` | `7394216B2B43C8828F1778252F36AC75A259860B2C519758EE9C424CDD42C21F` |
| O | `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION_OWNER_ADOPTION.md` | `1B306192D895FE1746D47D8D1C9AAF383F9C02B3E4EEE33948C329C0822703F9` |
| T/current and T/copy | `TASK_CURRENT.md`; `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION.md` | `EE1BDC60CAC5450FAB1C860FD292AA32ED65AD17E070856D8B5A9DDB64DAB67A` each |
| wrapper | `validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py` | `B1B2F54649B175F4E56C73135DECEED85C1AC966FE49A76431CF4B12B06633FD` |
| delegate | `validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py` | `AD592FCEEB6563D56BFEA6A9F35029B83712A6ACCED80A1BAF8F53C144F99D56` |

Each listed file itself was regular and non-reparse, path-specific Git-clean, and its filtered worktree blob matched `HEAD:path`; the runner's active preflight must still check path components before dispatch. The R, O and T literal tokens required by the timed wrapper were present, and the active 27-field C bound the exact execution ID, exclusive output root, budget namespace, R/wrapper/delegate hashes, `attempts=1`, `retries=0`, 36,000-second cooperative wall, no automatic C10 and Results eligibility `FALSE`. The Owner's separate one-shot choice A is recorded in O; it does not change the old actual-call ledger.

The only untracked paths were the five pre-existing protected output roots. Their C6-prime/C7/C8/C8-timing/C9-partial manifest raw hashes all matched the accepted values; the old C9 failure terminal remained `CALL_LEDGER_UNRESOLVED`. The new output root was absent. The Builder's T-preparation turn made no runner, preflight, `--execute`, model or scientific call. Original static-runner REJECT verdicts and the first two prohibited `--execute` probes remain historical facts, not reclassified by this review.

The first `load_delegate` call in `run_timed_action` invokes `preimport_authority_gate` before the delegate source is read or executed; the outer `future_gate` rechecks before science. This review did **not** invoke either runner or active static preflight. The execution task fixes the sole local Python interpreter, an at-most-once zero-science active static preflight, and the exact one-shot `--execute` command. If that preflight fails, the Builder must stop without a science attempt or repair. After an explicit dispatch message to the designated conversation, at most one wrapper execution may begin; any failure or ambiguous accounting consumes the attempt, with no retry or partial resume. The 36,000-second wall blocks a *next entry* only and may not bound an in-flight call. C10, K2, GE, convergence and Results remain closed; Results eligibility is `FALSE`.
