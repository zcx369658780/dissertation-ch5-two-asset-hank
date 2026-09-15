# CH5 MP4C K1 — J640 HJB nonconvergence mechanism diagnostic freeze

Date: 2026-09-15

Status: `J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_FROZEN`.
Results eligibility=`FALSE`.

## Scientific scope

The accepted finer-precision candidate established a valid J320 point and a J640 HJB numerical nonconvergence event at the frozen representative household state. This task may diagnose that event only. It may not repair, retune, or extend the HJB algorithm.

Frozen state:
- `rb=.02`
- `ra=.0675`
- household composite `w=15.5`
- `a=[0,100]`
- `b=[-2,20]`
- `h=1`
- `I=20`
- `J=640`
- `Nz=2`
- accepted HJB/KFE equations, FOCs, selectors, boundaries, derivative floor, solver, tolerance, maxit=100, mappings, guards, and parameters unchanged.

## Authorized runtime

Exactly one fresh-initialized J640 HJB diagnostic replay. No KFE. No J1280. No warm start. Scientific retries=0. Global/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0.

The replay must reproduce the accepted J640 terminal classification within numerical reproducibility tolerance. If it unexpectedly converges, stop and report a reproducibility blocker; do not proceed to KFE.

## Required diagnostics

Persist per iteration at minimum:
- iteration number
- `max(abs(V_new-V_old))`
- argmax coordinate and signed value change
- operator legality / A2max
- policy/selector-label change counts versus prior iteration for liquid and illiquid choices when available
- consumption/policy change counts above deterministic machine-scale thresholds
- derivative-floor hit count and first-hit iteration
- any boundary-specific switch counts that can be obtained without changing science
- hashes of V and policy-label objects sufficient to detect repeated/cycling states

Classify the mechanism conservatively among:
- `SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE`
- `POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`
- `DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING`
- `REPEATING_OR_LOW_PERIOD_CYCLE`
- `MIXED_OR_UNRESOLVED_NUMERICAL_MECHANISM`

No classification may be inferred from final statistic alone.

## Decision boundary

This task does not authorize increasing maxit. It only determines whether the J640 failure is plausibly a grid-induced slower contraction or a recurrence of the previously observed policy/value chattering class. Successor route remains Reviewer-only.
