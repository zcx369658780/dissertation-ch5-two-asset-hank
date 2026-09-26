# Current Builder Task - complete two prospective live bindings

Task ID: `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT_PROPOSAL_REPAIR2_ZERO_SCIENCE_20260926`
Status: `ACTIVE__TWO_FIELD_PROPOSAL_REPAIR_ONLY__NO_LIVE_AUTHORITY__NO_SCIENCE`
Assignee: Codex project `Zotero-Analytical-Workflow`, conversation `第五章 K1B 静态 runner 审查后接续` (`01a0dcd7-2acc-7571-b292-5807a0be0b1d`) only.
Worktree: `D:\ProjectTemp\c5k1bturn56` only. Never access `deep-learning-hank` or Zotero repository files.

## Start gate

Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, `AGENTS.md`, `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_REPAIR1_INDEPENDENT_REVIEW_20260926.md`, the three Repair1 proposal files and the timed runner's contract checks at `validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py:352-444`. Verify this task-issuance HEAD is a direct child of rejected Repair1 candidate `81fcf96f6b35383e3f1b9e166069e8357b0b2621`, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, tracked files/index clean, only five protected untracked roots and their review-recorded manifest hashes. Verify the new C9 output root, live contract, runner-recognized ACCEPT review, Owner execution adoption and one-shot task remain absent. Stop on mismatch.

## Only allowed changes

Edit only these existing three paths:

- `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_20260926.json`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_ZERO_SCIENCE_20260926.md`
- `EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_active_contract_proposal_zero_science_20260926/proposal_receipt.json`

Keep the top-level proposal schema distinct from the runner schema, `active=false`, `execution_authorized=false`, and all unknown future authority hashes `PENDING/ABSENT`. In the existing explicitly non-authoritative `prospective_live_contract_fields` map, add only the two missing runner-required future values: `schema=CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT_V1` and `active=true`. These are descriptive future values inside the nested map, not an activated live contract. Do not change the other known prospective values, especially the separate new/old execution IDs, exact wall policy, budget maps and four-key sealed-input map.

Update the report and receipt to preserve the original and Repair1 REJECT identities, account for this two-field repair, and bind proposal/report raw hashes without self-reference. Put the new candidate commit/parent/tree and all three final post-commit raw hashes in the terminal handoff. Preserve every earlier REJECT, limited ACCEPT scope and the original two prohibited `--execute` probes without reclassifying them. State that prospective field completeness is not a finalizable live contract and runner-recognized review, exact live adoption, Owner one-shot execution adoption/task and final dispatch review remain separate absent gates.

Use structured JSON parsing for comparisons. Run at most **one** no-model, read-only proposal check covering the nested `schema` and `active=true`, the unchanged top-level non-executable state, the other runner-required prospective fields and absent live/new-root paths; record exact command, exit code and result. On failure stop without another run or further edit. Stage only these three paths, make one local candidate commit, and report commit, parent, tree, `HEAD:src`, post-commit three raw SHA-256 values, clean tracked/index state, protected manifest hashes and absent live/new-root paths. Stop for independent GPT Work ACCEPT/REJECT; no push or successor.

## Hard stop

Do not edit either runner, source, tests, `CURRENT.md`, this task, review/Owner authority files or protected outputs. Do not create the actual live contract, runner-recognized ACCEPT review, Owner execution adoption/task or `reports/ch5_k1b_turn9_post_failure_new_attempt_001`. Do not call runner static preflight, `--execute`, `execute_once`, `load_delegate`, `run_timed_action`, model or science. No C9/C10 call, retry or partial resume. The old attempt is consumed and actual calls remain `CALL_LEDGER_UNRESOLVED`; the full-old-turn charge is governance accounting only. Results eligibility is `FALSE`. A later new C9 attempt still requires separate explicit Owner one-shot authorization and final independent dispatch review.
