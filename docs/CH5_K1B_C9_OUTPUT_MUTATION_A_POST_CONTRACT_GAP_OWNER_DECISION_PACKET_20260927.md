# C9 output mutation A after the native-contract gap: Owner decision packet

Status: `PROPOSED__NON_AUTHORITY__NO_TASK_OR_EXECUTION`. This packet does not revise the Owner's adopted objective A.

## Established boundary

The Owner adopted concurrent/hostile path-replacement containment in `docs/CH5_K1B_C9_OUTPUT_MUTATION_SAFETY_OBJECTIVE_A_OWNER_ADOPTION_20260927.md`. The accepted atomicity design shows a final-check-to-path-mutation window for root claim, recursive `mkdir`, JSON/NPZ creation and `unlink`. Candidate `ab554c7957fe182a7d4d4bdf00c69f7d66111579` was independently accepted only as official-documentation gap evidence: the target Windows/Python user-mode chain for all four operations remains `UNRESOLVED__FAIL_CLOSED`. No inert mutation experiment or runner change is ready to authorize. The accepted evidence does not establish that an ACL, separate account, sandbox, AppContainer or other isolation boundary is equivalent containment; none has been specified or tested for this project.

The existing threat description says a hostile process can replace the root, parents, symlink or reparse/junction components at arbitrary times. It does not specify the attacker's security principal, permissions, control of ancestor directories, or whether a privileged/same-token writer is in scope. An OS isolation proposal cannot be judged against objective A until those capabilities are fixed; silently excluding a capable writer would amount to a threat-model change, not a repair.

## Decision needed before another engineering route

**A1. Keep the presently stated hostile replacement capability in scope (default until changed).** Continue fail closed. A future zero-science task may seek an exact supported user-mode handle-relative contract for all four operations, but no further generic API-page survey or isolation mutation experiment should be mistaken for that proof. If no complete contract is found, C9 remains blocked. This preserves objective A without a new risk acceptance.

**A2. Consider an OS-enforced exclusion boundary as a proposed alternative, not yet an adopted equivalent.** First authorize only a zero-science security-boundary specification: exact attacker token/privileges, every mutable ancestor and root, who can change ownership/DACL or rename/delete, cross-volume and reparse behavior, and how a separate principal would retain necessary model input/output access. The specification must identify whether it actually preserves objective A or narrows it. If it narrows A, return for an explicit Owner risk decision; do not call it an implementation or run an isolation experiment at this stage.

**A3. Pause this C9 route.** Keep all candidate/failure evidence and consumed budgets intact while pursuing a separately designed dissertation route. This does not turn the partial C9 attempts into complete results.

Owner question: retain A1 as the research direction, authorize the A2 **specification only**, or select A3? Silence retains A1 fail closed. A2 would not authorize host/API probing, ACL changes, a temporary-root experiment, runner editing, preflight, `--execute`, a model call or a new output root. Any A2 specification candidate would require independent GPT Work ACCEPT/REJECT before a later experiment could even be considered.

`TASK_CURRENT.md` remains closed. Successor Codex conversation `01a0e046-973a-7bb1-b071-0305ebe541cf` has read-only intake but app-project membership is `UNVERIFIED`, so no writing task is dispatched. Both C9 attempts are consumed and actual ledgers remain `CALL_LEDGER_UNRESOLVED`; C10, retry, partial resume and Results remain closed, Results eligibility `FALSE`. Any future C9 science requires a fresh named budget, exclusive new output root, explicit Owner one-shot authorization and independent R/C/O/T review.
