# Independent Work review: fifth turn6 repeat-runner repair

Date: 2026-09-25 (Asia/Shanghai)

Verdict: `ACCEPT__TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR5__ZERO_SCIENCE__EXECUTION_NOT_AUTHORIZED_BY_THIS_REVIEW`

## Candidate and scope

Reviewed local candidate `81866d8f23cbb36e16281c41add27539c6ce7c6f`, parent `f8f730cef0e43329c72974e2d9eafecf664a7c21`. The candidate changed exactly the four paths allowed by `TASK_CURRENT.md`: the future repeat runner, its focused test, preparation report, and receipt. The worktree is clean, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, and the planned repeat output root is absent. No production source or accepted science changed.

## Review of the three repair4 blockers

1. The future runner now installs bounded `Path.mkdir` and `Path.unlink` mutation guards during reused-code execution, with ownership and path-component checks before the operation. It also checks ownership before province and integration entry. The reviewed reused source uses these `Path` mutations for province, checkpoint, terminal and integration directory creation and compact-checkpoint deletion; its JSON writer and NumPy compressed writer remain routed to the prior root-bound exclusive writers. Inert tests exercise root loss and foreign replacement before the representative mutation paths. This closes the previously unguarded code path at the tested check-before-operation level.
2. When the output root is lost and no safe receipt can be written, the raised failure detail now retains the earliest original terminal, available guard-attempted and source-ledger counts, and a resolved/unresolved flag. Inert post-entry tests cover both resolved and `CALL_LEDGER_UNRESOLVED` outcomes.
3. Root identity now uses `lstat` and rejects symlink/reparse components before comparing the recorded identity. The same-inode reparse-attribute stub passes. A real directory-symlink test was skipped because this Windows host cannot create that symlink. The code fails closed if Windows reparse attributes or a nonzero identity are unavailable.

## Independent readback

I re-ran the focused zero-science suite: **38 passed, 1 skipped**. The default static preflight returned `PASS__STATIC_PREFLIGHT_ONLY`. All 34 receipt source/reference identities and the report SHA-256 matched current files; its literal scientific-call ledger is zero. Candidate hashes match the receipt: runner `E362B921D4984669C3257A671684F55809702531522D253C26D80886786880B2`, test `0C9B704BF787767E9940C0E51305AFCA499D21995F890CE1A6D7FC2504490FB1`, report `C62CD876F20DFD88C01838301D64BAB821EDF38791A4292CD9595C0505C86F48`, receipt `2207553FD00357183591CDC4F5455E506E5430776E6BB2535C7A457A39F40379`. The candidate diff check passes.

## Limit and next gate

The guard checks and subsequent filesystem operations are not atomic against an adversarial operating-system rename. This acceptance establishes bounded engineering preparation under that explicit residual limit; it does not establish actual replay behavior, numerical repeatability, a stopping law, or Results eligibility. No replay, HJB/KFE, integration, firm, turn7 household, or other scientific call was made during this review. `Results eligibility = FALSE`; `1e-6` remains diagnostic precision only.

The repair5 Builder task is complete. Any C5-to-C6-prime repeat must be a **separate one-shot task** with an explicit call budget, sealed input/output bindings, first-failure stop, and independent Work review afterward. This review alone does not authorize starting that repeat.
