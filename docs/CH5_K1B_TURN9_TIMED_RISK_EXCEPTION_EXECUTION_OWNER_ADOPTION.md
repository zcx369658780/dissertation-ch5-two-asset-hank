# Owner adoption — one C9 timed-risk exception execution

Owner decision, 2026-09-26 (Asia/Shanghai): **“现在运行 C9 一次”**.

Status: `OWNER_ADOPTED__SINGLE_C9_TIMED_RISK_EXCEPTION`
Execution authorization ID: `C9_TIMED_RISK_RUN001`
Authorized output root: `reports/ch5_k1b_turn9_timed_risk_exception_run001`
C9 contract SHA-256: `65992776BFBED510F5C59DBC14B8CBE0B65DCCBAD08C5E0559491303D5A5B466`
Independent review SHA-256: `EA21124F8E01470D2D03DE1FB6B496CCA7EDDC584EF7270796EB01DD08C94354`

This adopts exactly one C9 attempt under the already adopted active contract and the accepted static runner. The 39 category, five province and C9+C10 cumulative attempted-call ceilings remain binding. Failed attempts consume budget; retries are zero. C10, a second C9 attempt, economic or solver changes, and Results are not authorized.

The C9-only cooperative monotonic resource wall is 36,000 seconds from the wrapper attempt start. Expiry blocks the next scientific entry; an in-flight call may cross the wall or local midnight before the next safe point. Manual interruption may leave `CALL_LEDGER_UNRESOLVED` and does not authorize a free retry or partial restart. Only a fully sealed and read-back complete outer turn can be a safe pause.

This Owner decision becomes dispatchable only after the byte-identical one-shot task and this adoption are committed, all authority and input identities pass fresh independent final-chain review, and the C9 output root is still absent. Results eligibility remains `FALSE`.
