# Current Builder Task - one-shot new C9 post-failure attempt

Task ID: `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION`
Status: `ACTIVE__ONE_SHOT_NEW_C9_POST_FAILURE`
Execution authorization ID: `C9_POST_FAILURE_NEW_ATTEMPT_001`
Authorized output root: `reports/ch5_k1b_turn9_post_failure_new_attempt_001`
Owner adoption SHA-256: `1B306192D895FE1746D47D8D1C9AAF383F9C02B3E4EEE33948C329C0822703F9`
C9 contract SHA-256: `7394216B2B43C8828F1778252F36AC75A259860B2C519758EE9C424CDD42C21F`
Wrapper SHA-256: `B1B2F54649B175F4E56C73135DECEED85C1AC966FE49A76431CF4B12B06633FD`
Delegate SHA-256: `AD592FCEEB6563D56BFEA6A9F35029B83712A6ACCED80A1BAF8F53C144F99D56`
Independent review SHA-256: `9C62625C648B9C33F4DFFF2CA8539C611EB96411E95D2858832C12A1527AF67E`

Only the Owner-designated Codex conversation “第五章 K1B 静态 runner 审查后接续” (`01a0dcd7-2acc-7571-b292-5807a0be0b1d`) may execute this task in `D:\ProjectTemp\c5k1bturn56`. Never access `deep-learning-hank` or Zotero repository files. The Owner explicitly authorized exactly one new C9 attempt in `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION_OWNER_ADOPTION.md`. This execution-version `TASK_CURRENT.md` and its `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION.md` copy must be byte-identical and committed. Their existence alone is **not dispatch**: do not invoke a runner or science until GPT Work has committed `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_FINAL_AUTHORITY_CHAIN_INDEPENDENT_REVIEW_20260926.md` with verdict `ACCEPT__C9_POST_FAILURE_NEW_ATTEMPT_FINAL_CHAIN_FOR_DISPATCH_ONLY` and sent a separate explicit dispatch message to this conversation.

## Entry gate before the one science invocation

Verify sole worktree, clean tracked/index, both committed task-file identities and their raw byte equality, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, committed raw R/C/O/wrapper/delegate hashes above, and the final independent dispatch review. Verify five pre-existing protected untracked roots and their C6-prime/C7/C8/C8-timing/C9-partial manifest SHA-256 values: `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`, `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`, `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`, `5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`, `80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3`. The new output root must be absent and safe. Do not infer actual old calls from the consumed `C9_TIMED_RISK_RUN001`: its actual ledger remains `CALL_LEDGER_UNRESOLVED`, while the full-old-turn charge is governance-only.

Run at most one zero-science active `static_preflight(..., require_inactive=False)` against the real committed chain. It must return `ACTIVE_AUTHORITY_STATIC_PREFLIGHT_ONLY__NO_SCIENCE`, with all checks true, before `--execute`. If any gate fails, stop without repair or science. No other test or dry-run may use `--execute`.

## Exactly one authorized execution

Only after the gates and explicit GPT Work dispatch message, invoke `validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py` exactly once with `--execute --execution-id C9_POST_FAILURE_NEW_ATTEMPT_001` and the sole repository path. Do not invoke the delegate directly. This is one new C9 attempt, not a retry of old C9. The runner enforces the separately adopted 39-key category, five-key province, C9-plus-prospective-C10 cumulative and lifetime governance ceilings; attempted calls are charged before entry, including failures. Maximum one outer turn, `attempts=1`, scientific/engineering retries `0`, no automatic C10 and no borrowing from the retired namespace.

The new-C9-only cooperative monotonic process wall is 36,000 seconds from wrapper attempt start. Expiry blocks the next science entry but does not interrupt an in-flight call, including across Beijing midnight. Do not impose a forced local-midnight stop. Manual interruption with uncertain accounting remains `CALL_LEDGER_UNRESOLVED`; no free retry or partial resume. Do not alter source, runner, solver, equations, grids, tolerance, calibration or budgets to recover a pass. Do not start C10, K2, GE, MATLAB, IRF, welfare or Results work.

At terminal, preserve the exclusive output root, journals and receipts unchanged. Report exact command, start/end clock evidence, terminal, attempted-call ledger and any unresolved layer, province/integration completion if available, output manifest/readback hashes, old protected hashes, and `HEAD:src`. Do not stage protected untracked roots or claim convergence/Results. Stop for GPT Work independent execution ACCEPT/REJECT. Results eligibility remains `FALSE`.
