# CH5 MP4C K1 raw `ra0` payoff bounded runtime-safety diagnostic report

Date: 2026-09-12  
Task: `CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC`

## Verdict

`BLOCKED_PRE_RUN__ACCEPTED_INITIALIZATION_HAS_NO_PRIOR_COMPLETED_RAW_RA0__ZERO_SCIENCE_CALLS`

The task's pre-run provenance gate failed before either trajectory invocation. The accepted initialization contains the 31-province `ra`, `rah`, and `rk` fields, but contains no `ra0` field for any province. Therefore Raw R cannot use an exactly prior-completed raw `ra0` vector for its first allocation without either inventing a return source or adding an Owner/Reviewer-authorized bootstrap rule. Both actions are outside Builder authority.

No scientific state was advanced. No payoff selector, runner, test, model, or economic-rule file was changed.

## Authority and repository identity

- live `origin/main`: `629cdb030f8b557f25d5c6c3ba5e9c42aab4038e`
- execution-start `HEAD`: `629cdb030f8b557f25d5c6c3ba5e9c42aab4038e`
- worktree: `D:\ProjectTemp\ch5-k1-raw-ra0-payoff-safety-20260912-001`
- branch: `codex/ch5-k1-raw-ra0-payoff-safety-20260912`
- active index state: `K1_PAYOFF_CONTRACT_FROZEN_RAW_RA0__BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_ACTIVE`
- Results eligibility: `FALSE`

The accepted initialization inspected was:

`D:\ProjectTemp\ch5-k1a-symmetric-rerun-evidence-20260911-001\path_b_geographic_beta2\runtime_input_payload.json`

Its SHA-256 was:

`EBB9FD91F3D3CE5D46476FE7BF1D0662E26EEA5C87357E4B13907CC76EBE9355`

## Pre-run gate result

The payload contains exactly 31 province states. Field inspection found:

| Field | Province states containing field |
|---|---:|
| `ra0` | 0 / 31 |
| `ra` | 31 / 31 |
| `rah` | 31 / 31 |
| `rk` | 31 / 31 |

The relevant runtime chain is otherwise clear:

- `one_turn.py` currently constructs `old_firm_return_ra` from entering `province["ra"]`.
- `k1a_runtime_adapter.py` passes that vector as `portfolio_return_by_destination`.
- `capital_network.py` forms the household payoff with the same destination-by-origin share matrix used by quantity allocation.
- a completed firm evaluation exposes both `ra0` and used/clipped `ra`, and `_post_turn_states` persists them into the next state.

Consequently, completed turn 1 could supply a provenance-safe raw `ra0` for turn 2. It cannot supply the prior-completed raw `ra0` required for Raw R's first allocation because that value does not exist in the accepted entering state.

The following tempting workaround was explicitly rejected:

1. run Raw R turn 1 with entering used/clipped `ra` as a common bootstrap;
2. switch to raw `ra0` only from turn 2.

That would add a new scientific timing/initialization convention not frozen by this task. It would also make the Raw first-allocation pre-run assertion false. The Builder therefore did not implement or execute it.

Pre-run gate status:

| Gate | Status |
|---|---|
| live baseline / task authority | PASS |
| accepted initialization identity | PASS |
| Control source can be entering used/clipped `ra` | PASS |
| Raw source can be entering prior-completed raw `ra0` | **FAIL** |
| C/R byte-identical except payoff designation | NOT REACHED |
| same `S` for quantity and payoff | static implementation path identified; runtime NOT RUN |
| K1B OFF / source-faithful labor / C1 unchanged | protected; runtime NOT RUN |
| raw payoff has no clipping/scaling/annualization/smoothing | NOT REACHED |

Under the exact task rule, any failed pre-run gate prohibits science.

## Scientific and model-call ledger

| Invocation/call | Count | Completed turns |
|---|---:|---:|
| Control C trajectory | 0 | 0 |
| Raw R trajectory | 0 | 0 |
| HJB | 0 | 0 |
| KFE | 0 | 0 |
| MATLAB model | 0 | 0 |
| standalone KFE experiment | 0 | 0 |
| K1B | 0 | 0 |
| K2 | 0 | 0 |
| GE | 0 | 0 |
| annual | 0 | 0 |
| shock/IRF | 0 | 0 |
| Results | 0 | 0 |
| engineering retry | 0 | n/a |

No no-overwrite external evidence root was created because no trajectory was authorized to start.

## Safety questions and accounting

Because both trajectories remained uninvoked, the requested C/R `rah`, HJB convergence, controls, drifts, NaN/Inf, hard-invariant, capital-accounting, C1-accounting, output, wage, and residual comparisons are `NOT RUN`, not PASS or FAIL.

Source-faithful labor, the accepted K1 capital formula, firm/HJB/KFE equations, C1, bounds, calibration, grid, tolerances, and solver semantics were not modified.

All corrected-2018 KFE observations remain `DIAGNOSTIC_ONLY`; finite-box upper-`b` leakage plus MATLAB-style pinning remains an independent unresolved blocker.

`RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED` is **not supported** by this execution because Raw R did not start.

## Required next authority gate

Owner/Reviewer must issue a fresh exact task that freezes one provenance-safe choice before any runtime attempt:

1. provide an accepted byte-identical initialization that already contains a provenance-bound prior-completed `ra0` for all 31 destinations; or
2. explicitly authorize and define a common turn-1 used-`ra` bootstrap, with Raw payoff first entering the household block on turn 2 and with the authorized turn-count/comparison semantics stated exactly.

No preference between those scientific choices is asserted here. Builder must not rerun, implement the bootstrap, enter K1B/K2, merge `main`, or publish a successor task without the fresh authority gate.
