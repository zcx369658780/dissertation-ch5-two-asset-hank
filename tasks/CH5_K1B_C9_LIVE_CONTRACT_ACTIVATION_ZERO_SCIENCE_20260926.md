# Current Builder Task — C9 live contract activation, zero science

Task ID: `CH5_K1B_C9_LIVE_CONTRACT_ACTIVATION_ZERO_SCIENCE_20260926`
Status: `ACTIVE__ZERO_SCIENCE_IDENTITY_CHAIN_ONLY`
Owner authority: `docs/CH5_K1B_C9_EXACT_ACTIVE_CONTRACT_OWNER_ADOPTION_20260926.md`, classification `OWNER_ADOPTED__EXACT_C9_ACTIVE_CONTRACT__ZERO_SCIENCE_FINAL_CHAIN_ONLY`.

Only the latest Codex conversation “第五章 K1B 跨天继续接续” (`01a0d867-be22-7d93-b2fb-0ddff659b686`) may write `D:\ProjectTemp\c5k1bturn56`. It remains in the `Zotero-Analytical-Workflow` Codex project. Read only named Chapter 5 paths; never access Zotero brief/index, user memory, `deep-learning-hank` or another project. No other conversation may write this tree.

## Entry and stop

Verify this task and `TASK_CURRENT.md` are byte-identical and committed, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, tracked files clean, and only four protected C6-prime/C7/C8/C8-timing output roots untracked. Verify their manifest SHA-256 values respectively `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`, `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`, `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`, `5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`. Both C9 output roots must be absent including broken links/reparse points. Stop on mismatch without repair.

## Exact change

Copy **byte-for-byte** `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_ACTIVE_CONTRACT_PROPOSAL_20260926.json` (reviewed raw SHA-256 `65992776BFBED510F5C59DBC14B8CBE0B65DCCBAD08C5E0559491303D5A5B466`) over `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_INACTIVE_CONTRACT.json`. Verify both raw hashes and bytes match. Do not reserialize JSON. The fixed path name is historical; after copying, its content is active, but **no execution task or Owner execution adoption exists**.

Update only the two C9 inert test files as necessary to make the **active static proposal state** meaningful: use explicit `static_preflight(repo, require_inactive=False)` and expect `PASS__ACTIVE_PREFLIGHT_ONLY`; test direct `future_gate(repo, "C9_TIMED_RISK_RUN001", fixed committed delegate)` stops at `BLOCKED__FRESH_C9_TASK_GATE` before output/science. Adapt delegate direct-entry expectations to this first gate while retaining `BLOCKED__C9_WRAPPER_REQUIRED` for its CLI. Do not weaken budget/identity/failure tests or modify production code.

The runner-recognized execution Owner adoption path `docs/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_EXECUTION_OWNER_ADOPTION.md` and one-shot task path `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_EXECUTION.md` must remain absent. `TASK_CURRENT.md` must remain this **zero-science** task throughout. Do not invoke `--execute`, `execute_once`, `run_timed_action`, `_execute_after_gate`, or any model/scientific action. Do not create C9 output.

## Allowed paths and verification

Modify only the live contract JSON, `tests/test_mp4c_k1b_turn9_outer_r2_preflight.py`, and `tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py`. Create only `docs/CH5_K1B_C9_LIVE_CONTRACT_ACTIVATION_ZERO_SCIENCE_20260926.md` and `EVIDENCE/ch5_k1b_c9_live_contract_activation_zero_science_20260926/activation_receipt.json`. All other paths, including proposal, source, wrapper/delegate and this task, are read-only to Builder.

Commit the exact allowed changes first, then run only focused inert tests and read-only checks, because committed-file identity fails on an uncommitted live contract. After commit, explicitly call active `static_preflight()` and directly call `future_gate()` with the fixed committed delegate. Expected statuses are `PASS__ACTIVE_PREFLIGHT_ONLY` and `BLOCKED__FRESH_C9_TASK_GATE`; stop if future_gate unexpectedly passes or any output appears. Verify exact changed paths, hashes, `git diff --check`, four protected roots and literal model/scientific/C9/C10/retry counts zero. A post-commit evidence correction may amend only allowed paths; return final commit/parent/tree and evidence to GPT Work for independent ACCEPT/REJECT. Do not self-accept, create an execution adoption/task, issue a successor, or run C9. Results eligibility remains `FALSE`.
