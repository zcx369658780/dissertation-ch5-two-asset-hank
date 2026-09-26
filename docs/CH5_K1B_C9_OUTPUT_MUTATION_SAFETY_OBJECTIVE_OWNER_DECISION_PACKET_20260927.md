# C9 output mutation safety objective: Owner decision packet

Status: decision request only. No option below is adopted by this document. Results eligibility remains `FALSE`.

## What is known

The new C9 attempt stopped with `CALL_LEDGER_UNRESOLVED` after the output guard raised `BLOCKED__OUTPUT_COMPONENT_REPARSE_POINT`; the terminal name did not prove a real reparse point. The bounded static `mkdir(parents=True)` repair and a check-between-checks regression have been independently accepted only for their narrow scope. The runner still checks paths before subsequent path-based creation/deletion, with an unresolved final-check-to-mutation race. Windows handle-relative operations have not been shown feasible or safe for this runner. See `docs/CH5_K1B_C9_OUTPUT_MUTATION_ATOMICITY_DESIGN_INDEPENDENT_REVIEW_20260927.md` and the accepted design it reviews.

## Choices

**A. Preserve a concurrent/hostile-replacement safety objective (recommended).** Keep execution blocked. Authorize only a separate zero-science platform feasibility and inert isolation study of handle-anchored create/delete or an equivalent verified containment mechanism. If the required semantics cannot be established on the target Windows environment, fail closed. This may delay or prevent a new C9 route; it does not spend a scientific call.

**B. Explicitly narrow the threat model.** Allow later engineering review under a trusted, exclusive single-process worktree with no concurrent writer or path replacement, acknowledging that current path-based checks do not protect against a concurrent/hostile replacement after the last check. This is acceptance of residual risk, not an atomic fix. Before any runner approval, Work must define enforceable exclusivity assumptions and test/monitor evidence; Owner must explicitly accept the remaining risk. This choice alone still does not authorize science.

**C. Do not pursue another C9 attempt.** Freeze this line of runner work and retain the failed attempts as partial failure evidence. Results eligibility stays `FALSE`; any different scientific route needs a separate design and Owner decision.

The recommended decision is **A** because the present safety contract already treats output-path substitution as a blocking condition, and a weaker threat model should not be inferred from a successful static regression. Owner may choose B or C explicitly. No option restores the old `C9_TIMED_RISK_RUN001` or new `C9_POST_FAILURE_NEW_ATTEMPT_001` budget; both actual ledgers remain `CALL_LEDGER_UNRESOLVED`. Any later scientific attempt requires a newly named budget, explicit one-shot Owner authorization, a fresh output root, and independently reviewed R/C/O/T identities. C10, retries, partial resume and Results remain closed now.
