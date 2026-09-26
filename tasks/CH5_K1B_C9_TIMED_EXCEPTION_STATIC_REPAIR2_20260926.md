# Current Builder Task — C9 timed-risk static Repair2

Task ID: `CH5_K1B_C9_TIMED_EXCEPTION_STATIC_REPAIR2_20260926`
Status: `ACTIVE__ZERO_SCIENCE_DELEGATE_IDENTITY_REPAIR`
Reviewer authority: `docs/CH5_K1B_C9_TIMED_RISK_EXCEPTION_STATIC_REPAIR1_INDEPENDENT_REVIEW_20260926.md`, verdict `REJECT__CALLER_SUPPLIED_DELEGATE_BYPASSES_BOUND_IDENTITY__ZERO_SCIENCE_REPAIR_ONLY`.

Only the existing Codex conversation “第五章 K1B 跨天继续接续” (`01a0d867-be22-7d93-b2fb-0ddff659b686`) may write `D:\ProjectTemp\c5k1bturn56`. It is already in the `Zotero-Analytical-Workflow` Codex project. Read/write only the Chapter 5 paths named in this task; do not open the Zotero project brief/index, user memory registry, `deep-learning-hank`, or another project. No other conversation may write this worktree.

## Entry and stop gates

Verify `TASK_CURRENT.md` is byte-identical to this archived task copy and both are committed; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`; tracked files clean. The only untracked roots must be the protected C6-prime/C7/C8/C8-timing outputs. Verify their manifest SHA-256 respectively `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`, `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`, `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`, `5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`. Verify the C9 timed-risk and outer output roots are absent, including broken links/reparse points. Stop on the first mismatch without repair.

Use Repair1 candidate `444117591f89394c1e768ba8f5943ecb527a3b5e` as the base. Read its report and independent REJECT. The inactive contract is read-only and remains `active=false`, `attempts=0`, `execution_id=null`, `resource_wall_seconds=null`. Its old delegate hash is intentionally stale until a later separately reviewed rebind. Do not activate it or create C9 output.

## Exact repair

Close the caller-supplied delegate bypass in `run_timed_action()` and `_instrumented_action()`. Every production route must load the exact committed delegate from `DELEGATE` under the contract hash before output creation or scientific entry, then use that loaded object for execution, budget and sealing. Remove the public `c9` production argument or make a caller-provided substitute fail closed. Retain any injected fake/action seam only in a private inert testing path that cannot be used to run science. Keep Repair1's four intended fixes and first-failure semantics intact.

Add focused inert tests that exercise the forged-delegate case: even when the authority gate is simulated as otherwise valid, a caller-supplied object cannot reach output creation or action. Also cover the fixed production object identity, default inactive CLI and `--execute` pre-science denial. Do not require a real active contract or create a real C9 output root.

## Allowed paths and verification

Modify only `validators/multi_province/k1b_turn9_timed_risk_exception/run.py` and `tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py`. Create only `docs/CH5_K1B_C9_TIMED_RISK_EXCEPTION_STATIC_REPAIR2_20260926.md` and `EVIDENCE/ch5_k1b_c9_timed_risk_exception_static_repair2_20260926/repair_receipt.json`. All other paths, including `TASK_CURRENT.md`, this archived copy, delegate, source, prior reports, tests, and inactive contract, are read-only to Builder.

Run only focused inert tests; no household, HJB, KFE, integration, benchmark, scientific call, retry, or real C9 output creation. Verify exact changed paths, source/report hashes, `git diff --check`, protected output hashes, and literal model/scientific/C9/C10/retry counts all zero. Stage and commit only the four allowed paths. Return commit/parent/tree, changed blobs, test results, failure behavior, and remaining risks for independent GPT Work ACCEPT/REJECT. Do not self-accept, rebind the contract, choose a wall, issue a successor, or run C9. Results eligibility remains `FALSE`.
