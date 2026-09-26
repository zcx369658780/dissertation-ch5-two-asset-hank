# Owner one-shot authorization — C8 same-frozen-input timing measurement

Date: 2026-09-26 (Asia/Shanghai). After reviewing `docs/CH5_K1B_C8_TIMING_ONE_SHOT_EXECUTION_DECISION_PACKAGE_20260926.md`, the Owner explicitly replied `授权一次 C8 测时`. This authorizes exactly one complete C8 same-frozen-input timing measurement attempt under the separately adopted budget and cooperative resource wall. It is not a C9/C10 execution authorization.

OWNER_ADOPTED__SEPARATE_SINGLE_C8_TIMING_BUDGET
Execution authorization ID: `CH5_C8_TIMING_MEASUREMENT_RUN001_20260926`
Authorized output root: `reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001`
Measurement contract SHA-256: `64E0A111E6C8FC186DB58F188CF55159ADCD3BBF213EF1457EF5EA7AEB569CB5`
Independent review SHA-256: `6217FC40E7EC992CB3302E43B8744B0C530F6696B48801BFC1AAD75D4EBB24C9`
Wrapper SHA-256: `8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A`

The complete separate attempted-call budget is the committed contract at the exact hash above: 39 per-category ceilings, five explicit per-province guards, at most one complete attempt, zero retries, and no borrowing from C9/C10. The process wall is cooperative 43,200 seconds from timed-action monotonic start: refuse the next scientific entry at/after the wall, permit an in-flight operation to reach a safe point, and do not force-stop at Asia/Shanghai 00:00. An in-flight operation can overrun 12 hours or midnight. Owner manual stop remains possible, but an interrupted or unresolved ledger is terminal for this task, never a free retry.

Before the single call, the assigned Codex task must independently verify local HEAD/source, the accepted wrapper and contract identities, clean tracked state, all three protected manifest hashes, sealed C7 entering-C8 input and absent exclusive output root. Any first identity, science, accounting or sealing defect stops this task. Preserve original numerical/failure terminal and attempted-call ledger. Only a complete sealed/read-back result is one observed timing sample; a failed or censored attempt is not. No science successor follows automatically.

C9/C10 prelaunch remains `BLOCKED__DURATION_BOUND_UNAVAILABLE`; this observation alone cannot establish an upper bound. Turn9 has not run. Results eligibility: `FALSE`.
