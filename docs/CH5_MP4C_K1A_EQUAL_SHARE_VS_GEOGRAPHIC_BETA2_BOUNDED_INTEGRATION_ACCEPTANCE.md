# Chapter 5 MP4C K1A equal-share vs geographic beta=2 bounded integration acceptance

Date: 2026-09-11.

Reviewer verdict:

`K1A_BOUNDED_INTEGRATION_PARTIAL_ACCEPTED__ACCOUNTING_AND_PATH_B_EVIDENCE_VALID__PATH_A_RERUN_REQUIRED_AFTER_VALIDATOR_PROVENANCE_REPAIR`

Accepted candidate:

`f57fec4d66bb82d48dc02bed775761ec194e0084`

## Scope accepted

The K1A runtime integration implementation, zero-science provenance-validator repair, persisted evidence, and bounded Path B trajectory are accepted within their demonstrated scope. The candidate is one commit ahead of the prior live-main baseline `386594886bec9e42d3dc18791f7f1be212d3b5c9`, with only the task report/receipts, one K1A adapter, one focused test, and task-specific runner/finalizer files added. Protected MATLAB, legacy `capital_allocation.py`, accepted K1 formulas, HJB/KFE/firm/labor/C1 formulas, bounds, tolerances, grids, solver semantics and Results code are unchanged.

## Evidence accepted

- Pre-run focused suite: `50/50` PASS.
- Path A completed exactly one outer turn, then stopped at turn-2 entry because the reused task validator asserted the legacy `rah` formula rather than the accepted K1A same-`S` portfolio payoff identity.
- Because scientific state had advanced, Path A was correctly not retried under the original task.
- The subsequent repair was zero-science and limited to task-wrapper provenance validation: it validates `rah` against the prior completed K1A allocation and same portfolio matrix `S`. No economic equation, parameter, tolerance or solver object was changed.
- Path B then completed the authorized 25-turn bounded trajectory under the repaired validator.
- Across all 806 completed province-turn observations, K1 quantity/payoff same-matrix accounting, home retention, origin/national capital conservation and absence of destination-`theta_j` double weighting passed.
- C1 remained `GovInv=max(Ktarget-Kprivate,0)`; no private-only overshoot occurred in observed rows.
- Path B remained nonconverged at the 25-turn ceiling because `max_nk_gap=1.8619512598405663e-09 > 1e-9`; this is preserved as a numerical observation, not tuned away.
- All 775 Path B KFE uses remain `DIAGNOSTIC_ONLY`; empirical finite-box upper-b leakage / MATLAB-style pinning remains an independent blocker.
- Results eligibility remains `FALSE`.

## Scientific interpretation boundary

The first-turn A/B evidence shows C1 mechanically offsets the small Kprivate allocation difference at total-firm-K level, leaving turn-1 firm raw return, output and wage unchanged. The forward difference is instead carried through the K1A network-produced household `rah`, which would affect the next household pass. Because Path A stopped before that next pass, a full 25-turn A/B comparison is not yet available.

The completed Path B path also reconfirms that raw-return pressure remains severe under K1A: `755/775` province-turn raw `ra0` observations exceed `.09`. This supports continued re-audit of payoff/return authority after the clean A/B rerun; it does not authorize changing return bounds now.

## Next gate

A fresh exact task is authorized to rerun both preregistered K1A paths from identical accepted initialization under the already-repaired provenance validator, with no scientific design changes:

- Path A: `beta_distance=0`, `beta_return=0`;
- Path B: `beta_distance=2`, `beta_return=0`;
- fixed `theta_i`;
- source-faithful labor;
- no smoothing;
- K1A transitional payoff bridge = current source-used/clipped `ra`;
- C1 unchanged;
- maximum 25 outer turns per path.

The rerun exists solely to obtain symmetric bounded A/B evidence after the wrapper defect. It must not alter coefficients, payoff concept, solver settings or scientific formulas.
