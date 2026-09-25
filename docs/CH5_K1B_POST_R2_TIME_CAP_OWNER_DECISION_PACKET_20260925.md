# Owner decision packet — hard resource cap before prospective C9/C10

GPT Work independently **ACCEPTED** the zero-science timing audit at Builder candidate `17b61e8bed914bcf2b9cec50671968721c4617ad` in `docs/CH5_K1B_POST_R2_TIMING_BUDGET_ZERO_SCIENCE_EVIDENCE_INDEPENDENT_REVIEW_20260925.md`. No accepted sealed file provides scientific-process start/end or monotonic elapsed seconds for C7/C8. Result: **`MEASURED_SCIENCE_RUNTIME_UNAVAILABLE`**. Historical actual call counts and proposed per-category ceilings cannot be converted to hours. Old two-turn budget remains consumed; no turn9 has run; Results eligibility is `FALSE`.

## Owner choice

| Route | Decision needed | Consequence and limit |
|---|---|---|
| A. Set a resource cap independently | Specify the maximum **wall-clock time** you are willing to occupy the machine for a prospective C9/C10 attempt (`T_owner`, in hours or minutes), and whether you also require a CPU/GPU/energy or monetary cap. | This is a resource tolerance, not a measured runtime or completion forecast. A future runner would need a verified external watchdog to enforce a hard wall cap during an individual model operation. It must preserve attempted-call evidence and mark unflushed attempts `CALL_LEDGER_UNRESOLVED`. Setting a cap authorizes design and static runner work only; scientific execution still needs an explicit complete budget and separate approval. |
| B. Measure before setting the cap | Request a separately scoped, instrumented scientific attempt with explicit call ceiling, output root, process-bound monotonic timer, exact ledger, first-failure stop and independent review. | The measurement consumes a **new** scientific budget; C7/C8 cannot be rerun under old authority. One measured attempt may not predict later turns. An exact bounded task and explicit Owner authorization are required before any call. |

**GPT Work recommendation:** choose A if your practical concern is a maximum machine-occupation time and you can state that limit without a runtime forecast. It avoids an extra measurement call. Choose B if a timing estimate is necessary before you can set a limit; it costs a separately authorized scientific attempt. In either case, the proposed future two-turn per-category ceiling table remains a proposal, not a renewed budget, and the batch runner has not been implemented or independently reviewed. A 10/20-turn run remains outside the selected short-window design.

Please choose A with a finite wall time and any additional resource cap, or B for a separately budgeted measurement design. Neither choice by itself authorizes turn9, runner execution, K2, GE or Results.
