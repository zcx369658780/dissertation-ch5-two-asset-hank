# Current Builder Task - repair new C9 non-authority contract proposal

Task ID: `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT_PROPOSAL_REPAIR1_ZERO_SCIENCE_20260926`
Status: `ACTIVE__PROPOSAL_REPAIR_ONLY__NO_LIVE_AUTHORITY__NO_SCIENCE`
Assignee: Codex project `Zotero-Analytical-Workflow`, conversation `第五章 K1B 静态 runner 审查后接续` (`01a0dcd7-2acc-7571-b292-5807a0be0b1d`) only.
Worktree: `D:\ProjectTemp\c5k1bturn56` only. Never access `deep-learning-hank` or Zotero repository files.

## Start gate

Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, `AGENTS.md`, `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_INDEPENDENT_REVIEW_20260926.md`, the three rejected proposal files, the adopted budget and the timed runner's contract checks at `validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py:352-403`. Verify this task-issuance HEAD directly descends from rejected candidate `c91c3030efb3d303fa50c7bb1aba66bc075d9d3a`, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, tracked files/index clean, only five protected untracked roots and their review-recorded manifest hashes. Verify the new C9 output root, live contract, runner-recognized ACCEPT review, Owner execution adoption and one-shot task remain absent. Stop on mismatch.

## Only allowed changes

Edit only these existing three paths:

- `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_20260926.json`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_ZERO_SCIENCE_20260926.md`
- `EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_active_contract_proposal_zero_science_20260926/proposal_receipt.json`

Keep the top-level proposal schema distinct from the runner schema, `active=false`, `execution_authorized=false`, and all unknown future authority hashes `PENDING/ABSENT`. Add an explicitly non-authoritative `prospective_live_contract_fields` map that uses the runner's exact live field names and known values. It must distinguish new `execution_id=C9_POST_FAILURE_NEW_ATTEMPT_001` from `old_execution_id=C9_TIMED_RISK_RUN001`, bind `output_root`, `attempts=1`, `retries=0`, exact `resource_policy=COOPERATIVE_PROCESS_WALL_CAP` and `resource_wall_seconds=36000`, adopted budget proposal/adoption raw hashes, wrapper/delegate raw hashes, unchanged `src_tree`, and the runner's exact four-key `sealed_input_sha256` map (`manifest`, `readback`, `json`, `npz`). Include the runner-required budget and old-governance maps and no automatic C10 or Results eligibility. The existing descriptive cooperative-wall meaning may remain separately labeled; do not present its longer phrase as the live `resource_policy` value. Do not copy the retired ID as the new execution identity or reuse the old output root.

Update report and receipt with the rejected baseline candidate identity, `HEAD:src`, proposal/report raw hashes, source bindings, protected manifest hashes, absent live/new-root facts, and an explicit account of this repair. Put the new candidate commit/parent/tree and all three final post-commit raw hashes in the terminal handoff, not self-referential fields inside the committed files. Preserve every earlier REJECT, limited ACCEPT scope and the original two prohibited `--execute` probes without reclassifying them. The report must state that known field mapping is not a finalizable live contract and that runner-recognized review, exact live adoption, Owner one-shot execution adoption/task and final dispatch review remain separate absent gates.

Use structured JSON parsing for comparisons. After finalizing the three files, run at most **one** no-model, read-only proposal check covering the corrected prospective field names/values and non-executable status; record exact command, exit code and result. On failure stop without another run or further edit. Stage only these three paths, make one local candidate commit, and report commit, parent, tree, `HEAD:src`, post-commit three raw SHA-256 values, clean tracked/index state, protected manifest hashes and absent live/new-root paths. Stop for independent GPT Work ACCEPT/REJECT; no push or successor.

## Hard stop

Do not edit either runner, source, tests, `CURRENT.md`, this task, review/Owner authority files or protected outputs. Do not create the actual live contract, runner-recognized ACCEPT review, Owner execution adoption/task or `reports/ch5_k1b_turn9_post_failure_new_attempt_001`. Do not call runner static preflight, `--execute`, `execute_once`, `load_delegate`, `run_timed_action`, model or science. No C9/C10 call, retry or partial resume. The old attempt is consumed and actual calls remain `CALL_LEDGER_UNRESOLVED`; the full-old-turn charge is governance accounting only. Results eligibility is `FALSE`. A later new C9 attempt still requires separate explicit Owner one-shot authorization and final independent dispatch review.
