# Chapter 5 MP4C corrected-2018 25-turn K/L target reconciliation diagnostic — Reviewer rejection

Date: 2026-09-10

Candidate: `a0e117ade98f8197bb76cd2471f7932d545afbcc`

Reviewer verdict:

`REJECT_FOR_PREMATURE_HJB_NONCONVERGENCE_STOP__SOURCE_TURN_CONTRACT_ALLOWS_FLAGGED_HOUSEHOLD_OUTPUTS_TO_CONTINUE`

## Decision

The candidate package is internally careful and correctly binds the accepted corrected-2018 Track-A runtime, but it does not satisfy the source-faithful execution contract of the exact task because the harness raises immediately when one household HJB reaches the 100-iteration ceiling with `converged=false`.

The accepted MATLAB multi-province logic audit establishes that each outer turn consists of 31 household calls followed by migration/labor, `At*N` capital allocation, `rah`, firm, wage and controller logic. Household convergence is an explicit component of the *final outer steady-state acceptance predicate* together with K/N and output gaps and zero `ra` boundary hits. The source audit does not designate a single household `converged=false` flag as a mandatory immediate abort of the current turn.

Therefore the candidate's turn-1 Anhui result (`100` iterations, statistic `0.18862667495966345`) is valid diagnostic evidence, but the inference that this is a `hard scientific failure preventing continuation` is not source-backed. The current Python harness line `if not hjb.converged: raise RuntimeError("HJB did not converge")` is stricter than the accepted MATLAB ordered-update contract.

## Evidence retained

The following evidence remains valid and may be reused as historical diagnostic context:

- corrected-2018 pre-science runtime binding passed;
- Beijing through Zhejiang household/HJB/KFE evidence was produced under the corrected contract;
- Anhui HJB reached its frozen 100-iteration ceiling and returned `converged=false` with statistic `0.18862667495966345`;
- no migration, capital allocation, firm, wage or controller action occurred because the Python harness aborted before those stages;
- no second trajectory or scientific retry occurred;
- K/L turn-20-to-25 quantities are genuinely unavailable in this rejected execution.

The candidate is **not** accepted as the requested 25-turn K/L reconciliation because it terminated under a non-source-backed abort rule.

## Required correction

A successor implementation task must repair the corrected-2018 multi-turn harness so that household HJB nonconvergence is recorded per province and propagated as a convergence flag, but does not by itself abort the turn if finite model outputs exist and the source-style downstream computation can continue.

The run may still stop for true hard failures such as nonfinite state, failed numerical solve with no usable return object, malformed dimensions, unrecoverable exception, or another condition that actually prevents continuation.

Final source steady-state acceptance must continue to require 31/31 household convergence flags. A flagged household output used to continue a diagnostic trajectory must never be relabelled as scientifically accepted HJB evidence.

`Results eligibility=FALSE`.
