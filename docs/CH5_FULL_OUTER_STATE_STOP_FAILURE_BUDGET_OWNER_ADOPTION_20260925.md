# Chapter 5 complete outer-state stopping, failure and budget contract — Owner adoption

Date: 2026-09-25 (Asia/Shanghai)

Owner decision: `OWNER_ADOPTED__BOUNDED_K1B_NINE_COMPONENT_STRICT_1E6_R2__CLIPPED_RA_REPORT_ONLY__TWO_TURN_CEILINGS__FIRST_FAILURE_ZERO_RETRY`

Owner confirmation: `好的我确认，请继续`, in response to Work's concrete recommendation after independent ACCEPT of `docs/CH5_OUTER_STOP_REPEATABILITY_OWNER_DECISION_PACKET_20260925.md`. The confirmed recommendation covered the nine-component carrier and formulas, strict `<1e-6`, two consecutive legal comparisons (R2), clipped-`ra` report-only treatment for the new criterion, up to two new turns with explicit ceilings, and first-failure/no-retry rules. This document records that choice. It is **scientific-contract authority**, not an execution task or a claim that any future turn has run.

Evidence anchors: accepted decision packet SHA-256 `D9AEB18FFEE8DA23B2430BEE7C5328F282E95B15354A019E26CBDD18E6D26495`; proposal `docs/CH5_OUTER_STOP_FAILURE_BUDGET_CONTRACT_PROPOSAL_20260923.md` SHA-256 `5D3BFE7B914DE3F6BE3B99E75E80680B18A4054FB186EBB715D865F4008DEAC6`; one-shot C5-to-C6-prime independent review `docs/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_INDEPENDENT_REVIEW_20260925.md`. The exact same-input pair supports empirical repeatability at that one input only. General outer-map numerical error bound remains `UNAVAILABLE`.

## Adopted carrier, timing and comparison

A legal same-stage checkpoint `C_n` requires 31/31 accepted household HJB/KFE results, exactly one completed source-faithful integration, completed raw `ra0_n`, and a sealed/read-back entering-`n+1` input/plan with destination-by-origin `S_(n+1)` and lagged `rah_(n+1)`. Same-turn raw-return feedback remains forbidden.

Compare the eight canonical 31-province vectors `Yt,Lt,wjt,rk,Kt_prev,w,raw_ra0_n,rah_(n+1)` and the 31×31 destination-by-origin matrix `S_(n+1)` at two complete legal adjacent checkpoints:

- `Yt,Lt,wjt,w`: `max abs(new/old-1)`, requiring every old denominator finite and nonzero.
- `Kt_prev`: `max abs(new-old)/Kt0`, with the exact frozen positive finite `Kt0` unchanged across checkpoints.
- `rk,raw_ra0,rah,S`: maximum absolute difference.

Bind source, input, province order, axes, shapes, finite status, matrix orientation and source/plan hashes before comparison. A missing or invalid denominator/identity is a failure, never a numeric zero.

Each of the nine component differences must be **strictly `<1e-6`**. This is an adopted numerical criterion for the **frozen bounded K1B outer map**. It is not a general model error tolerance, convergence theorem, mathematical fixed point, original MATLAB predicate, steady state, GE or Results permission. The `10^-12` class remains aspirational.

## R2 persistence and clipped-ra boundary

Require two **consecutive** complete legal adjacent comparisons, C6→C7 and C7→C8, each meeting all nine strict inequalities. R1 alone is insufficient. A legal comparison at or above the level is `VALID__NINE_COMPONENT_LEVEL_NOT_MET`, not divergence or scientific failure. Stop before turn9 household. A bounded two-turn run with zero, one or two passes receives the proposal's distinct terminal classes; even two passes end `CRITERION_MET_FOR_BOUNDED_K1B_MAP_ONLY__INDEPENDENT_REVIEW_PENDING` until independent Work review.

Record clipped `ra` upper-bound hits at every checkpoint but **do not use them as a disqualifier for this new nine-component criterion**. The original MATLAB zero-hit predicate is separate and remains unmet by the observed 31/31 hits at C4/C5/C6. Report-only treatment does not remove clipping from the economic object, establish validity of a broader equilibrium, or turn the original predicate into PASS.

## Adopted maximum calls and first-failure protocol

The exact per-turn and two-turn numerical ceiling table in the named proposal (under the SHA-256 above) is adopted for at most **two new complete turns from sealed C6**, except that its three previously unresolved categories are now explicitly resolved as follows:

| Attempted category | Per province | Per turn | Two-turn combined | Meaning |
|---|---:|---:|---:|---|
| `scalar_selector_root_invocations` | 20,000,000 | 620,000,000 | 1,240,000,000 | All root subtypes share this aggregate; no separate subtype allowance. |
| `terminal_kfe_attempts` | 1 | 31 | 62 | One accepted terminal KFE entry per province and turn. |
| `k1b_feedback_calls` | — | 1 | 2 | Ledger alias of the same frozen K1B allocation event, not another feedback pass. |

The other table rows include at most 50 direct HJB updates and 51 policy maps per province per turn; at most one household batch and one integration per completed turn; and zero full-space dense GESVD, retries, solver substitutions, K2, GE, MATLAB scientific calls and Results calls. Failed attempts count. No province borrows another's allowance. The task that later authorizes an execution must reproduce **every** adopted category ceiling, distinguish per-turn and combined caps, and verify source entry accounting before the first call. The algebraic ceilings are maxima, not targets or permission to spend them automatically.

Adopt the proposal's legality-first sequence: precall identity → 31/31 household HJB/KFE → one integration → seal/readback → comparison → budget terminal. Preserve the earliest original inner terminal, location and exact consumed ledger. If accounting is unresolved, mark `CALL_LEDGER_UNRESOLVED` rather than asserting zero. Stop at the first identity, legality, budget, seal or readback defect. No warm start, retry, rescue, second integration, alternate solver/alpha schedule, damping/tolerance/grid change, or repaired rerun within a consumed task. A legal level not met at the adopted budget is a valid bounded outcome, not a failure.

## Execution gate and claim boundary

No turn7 household or turn8 execution is authorized by this document alone. Work must issue a separate bounded task with sealed C6/turn7 input hashes, frozen source identity, explicit per-province/per-turn/combined call budget, output root, first-failure stop, and independent review after execution. If runner coverage, ledger resolution or output ownership cannot be established without changing accepted science, stop for a new design/review gate before calls. No scientific successor follows a failed or consumed task automatically.

`Results eligibility = FALSE`. K2, GE, annual dynamics, shocks, IRFs, welfare and dissertation Results remain closed.
