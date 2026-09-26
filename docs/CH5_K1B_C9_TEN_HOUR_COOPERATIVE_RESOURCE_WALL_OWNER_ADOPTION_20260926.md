# Owner adoption — C9-only 10-hour cooperative process resource wall

Date: 2026-09-26 (Asia/Shanghai).

After GPT Work proposed a **C9-only 10-hour** cooperative process resource wall, the Owner replied: `好的我同意，请继续`.

The adopted numerical cap is `resource_wall_seconds=36000`, measured with a monotonic process clock from the start of the future C9 wrapper attempt. It applies only to the prospective **single C9 timed-risk exception**. On expiry, the guard denies the **next** scientific entry; it does not forcibly terminate an in-flight source call. Such a call may run past 36,000 seconds until its next safe point, including past local midnight or a planned shutdown. If the Owner manually interrupts it, attempted-call accounting may remain `CALL_LEDGER_UNRESOLVED`; that interruption is not a free retry or partial-turn resume. Only a complete outer turn with a sealed and read-back output can be a safe cross-day pause.

This cap is a resource ceiling, **not** a credible C9 completion-time upper bound. The single observed C8 duration of 3,382.203 seconds does not establish one. The C9/C10 attempted-call limits already adopted remain unchanged and failed attempts consume them. C10 receives no automatic resource wall or execution authorization.

This decision authorizes zero-science preparation and review of a precisely bound C9 active-contract candidate. It does **not** by itself adopt that final active contract, issue the separately required one-shot `run C9 now once` authorization, create a C9 output root, or permit any scientific call. The current contract remains inactive and `TASK_CURRENT.md` remains closed until a new scoped preparation task is issued. Results eligibility remains `FALSE`.
