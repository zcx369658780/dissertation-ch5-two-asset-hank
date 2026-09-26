# Current Builder Task — C9 timed-risk exception, inert static preparation

Task ID: `CH5_K1B_C9_TIMED_EXCEPTION_STATIC_RUNNER_PREPARATION_20260926`
Status: `ACTIVE__ZERO_SCIENCE_INERT_PREPARATION_ONLY`
Issued from local HEAD pending this dispatch commit; frozen `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. Sole Builder conversation: “第五章 K1B 跨天继续接续” (`01a0d867-be22-7d93-b2fb-0ddff659b686`). Sole worktree: `D:\ProjectTemp\c5k1bturn56`. Never access `deep-learning-hank` or another project path; Codex project membership is conversation context only.

## Authority and purpose

The Owner selected preparation of one **C9-only** timed-risk exception in `docs/CH5_K1B_C9_SINGLE_TURN_TIMED_RISK_EXCEPTION_OWNER_SELECTION_20260926.md`. This permits zero-science implementation and static tests, **not** C9 execution. The usual C9/C10 duration gate stays `BLOCKED__DURATION_BOUND_UNAVAILABLE`; the Owner has not selected C9 resource-wall seconds or separately authorized “run C9 now once”. Existing C9/C10 attempted-call ceilings were adopted in `docs/CH5_K1B_C9_C10_CALL_CEILINGS_OWNER_ADOPTION_20260925.md`; bind them as maxima, not as a call permit. Results eligibility remains `FALSE`.

At entry verify this task and `TASK_CURRENT.md` are byte-identical and committed; `HEAD:src` equals the frozen tree; tracked files are clean; only four protected untracked roots exist. Verify C6-prime/C7/C8/C8-timing manifest SHA-256 respectively `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`, `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`, `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`, `5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`. Verify the prospective output root `reports/ch5_k1b_turn9_timed_risk_exception_run001` does not exist, including broken links/reparse points. Stop at the first mismatch; do not clean or stage any protected root.

Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, `REVIEW_GATE.md`, the Owner selection, the C9/C10 adopted ceiling table and accepted C8-to-C9 transfer review. The C8 source runner `validators/multi_province/k1b_turn8_outer_r2/run.py` and accepted C8 timing wrapper `validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py` are read-only templates. Read only directly named C8 entering-C9 receipts/manifests and helper source needed to implement a mechanically equivalent C9 turn. Do not modify existing source or evidence.

## Exact allowed changes

Create only these seven paths:

1. `validators/multi_province/k1b_turn9_outer_r2/run.py`
2. `validators/multi_province/k1b_turn9_timed_risk_exception/run.py`
3. `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_INACTIVE_CONTRACT.json`
4. `tests/test_mp4c_k1b_turn9_outer_r2_preflight.py`
5. `tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py`
6. `docs/CH5_K1B_C9_TIMED_RISK_EXCEPTION_STATIC_PREPARATION_20260926.md`
7. `EVIDENCE/ch5_k1b_c9_timed_risk_exception_static_preparation_20260926/preparation_receipt.json`

No other path may change. The contract must be **inactive** with `resource_wall_seconds=null`, no one-shot execution authorization and exact hashes/identities wherever already available. The wrapper and runner must fail closed before scientific entry or output creation while the contract is inactive, including when `--execute` is supplied. Do not create the proposed C9 output root.

## Required static implementation

Implement a C9-specific guarded outer-turn delegate and C9-specific timing wrapper. Do not alter frozen equations, solver, grid, tolerances, payoff law, household integration or accepted C8/C7 files. Bind only the sealed C8 entering-C9 bundle (manifest SHA-256 `40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65`, readback SHA-256 `E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85`, input JSON SHA-256 `FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB`, NPZ SHA-256 `E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD`). C9 must use `turn=9`, produce a prospective turn10 entering bundle, and compare C8→C9 on the accepted nine components with strict `<1e-6`. It must stop after C9 seal/readback at `SAFE_PAUSE_AFTER_SEALED_C9`, never auto-start C10. Existing province/HJB partial artifacts are not resumable process state.

The attempted-call guard must implement all adopted category/alias, per-province, C9 per-turn and C9+C10 cumulative ceilings; initialize the new prospective C8-start window at zero without borrowing C6→C8 counts. Persist an attempt and decrement before each scientific entry; failures count, retries are zero, and uncertain or incomplete ledgers are terminal. Protect the sole new output root against preexistence, symlinks/reparse points and replacement. The timing wrapper must distinguish wall clock from monotonic elapsed time; finite C9-specific cooperative wall semantics become active only through a later separately adopted contract. At the wall deny the next science entry, allow an in-flight call to reach a safe point, preserve original terminal and ledger. An Owner manual stop cannot produce an automatic retry. The midnight exception may apply only to this single C9 attempt after later adoption; it cannot automatically clear C10's normal gate.

## Verification and handback

Run only bounded inert/static tests that cannot enter household, KFE, integration or write the proposed C9 root. Test default CLI and inactive `--execute` both fail closed with zero scientific calls; identity/hash/owner-contract/output-root mismatch; 39 categories and applicable per-province/cumulative guards; C8→C9 comparison and strict boundary; clock/resource semantics; first-failure/uncertain ledger; C9 complete-seal then no-C10 transition. Use mocks or pure functions, never real science. Model calls 0; scientific calls 0; retries 0; C9/C10 attempts 0. Stop on first task-authority or identity mismatch.

Report exact source hashes, altered-path inventory, test commands/outcomes, zero-call ledger and unresolved risks in the allowed report/receipt. Stage and commit **only** the seven allowed paths. Return commit/parent/tree and blob IDs for independent GPT Work review. Do not self-accept, activate the contract, edit `TASK_CURRENT.md`, send a successor, or run C9. This task ends at independent Work ACCEPT/REJECT; an active C9 resource contract and one-shot execution still require separate Owner action.
