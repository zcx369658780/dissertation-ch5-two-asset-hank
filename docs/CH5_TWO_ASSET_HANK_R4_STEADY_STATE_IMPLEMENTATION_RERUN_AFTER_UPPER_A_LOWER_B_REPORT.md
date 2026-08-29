# Chapter 5 Two-Asset HANK R4 — Steady-State Rerun After Upper-A/Lower-B Resolution

Date: 2026-08-22

## Verdict

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_UPPER_A_LOWER_B_FAIL_CLOSED`

## Acceptance level

`R4_STEADY_STATE_RERUN_REJECTED_PRIMARY_HJB_POLICY_SELECTION_FAILURE`

The frozen fixture was invoked exactly once under the live task. Execution
stopped at a new primary-HJB policy-selection failure. No same-task diagnosis,
adjustment, tuning, repair, or rerun followed.

## Live authority and repository state

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Fresh-fetched `origin/main`:
  `7f92117d3505e863ef6fd271e627b672cf118fe2`.
- Local baseline: `46d98d140cebcefb795c14f3ba8f61a515d5f6ac`.
- Start relation: `0 ahead / 50 behind`.
- Live task:
  `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_UPPER_A_LOWER_B.md`.
- Live `AGENTS.md`, project rule index, and GitHub capability/authority-routing
  rule were read directly from `origin/main` without pull or checkout.

## Files read

- live repository governance, project rule index, capability-routing rule, and
  exact rerun task;
- R4 steady-state fixture authorization report;
- latest preceding steady-state rerun report;
- accepted upper-`a`/lower-`b` policy-fixture resolution report;
- current steady-state runner and target steady-state test.

## Files written

- added this report.

No source, test, fixture, solver, policy, boundary, generator, equation,
parameter, calibration, tolerance, or prior evidence file was modified.

## Tests executed

1. Static compilation of the steady-state runner, HJB, policy, boundary,
   generator, KFE, and target test: passed.
2. Non-steady-state regression suite with
   `tests/test_r4_steady_state.py` explicitly excluded:
   - `27 passed in 2.90s`.
3. The first formal launcher process exited during module import because the
   ordinary Python process did not include the repository `src` directory:
   - `ModuleNotFoundError: No module named 'ch5_two_asset_hank'`;
   - the frozen function was not imported, resolved, or invoked;
   - fixture invocation count remained zero.
4. Formal frozen runner after explicitly placing the existing repository
   `src` directory on that process's module path:
   - `run_frozen_r4_steady_state()` invoked exactly once;
   - terminated with `PolicySelectionError` before returning a result;
   - formal process exit: `1`.

The target pytest was not separately executed because that would have invoked
the fixture a second time.

## Steady-state diagnostics

- fixture: `R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1`;
- actual fixture invocation count: exactly `1`;
- terminal stage: primary 25-node HJB policy selection;
- terminal logical state: `(i_a,i_b,i_z)=(2,1,5)`;
- frozen coordinates: `(a,b,z)=(1.0,2.5,0.8125)`;
- state location: computational upper illiquid boundary and interior liquid
  state;
- exception:
  `PolicySelectionError: no admissible self-consistent candidate at state (2, 1, 5)`.

The primary HJB did not return. Therefore no accepted primary iteration count,
HJB residual, KKT residual, or generator residual is available. The
upper-buffer HJB, 25-vs-29 truncation comparison, endogenous illiquid-asset
connectivity, closed recurrent classes, left nullity, stationary KFE,
normalization, nonnegative mass, mass/density consistency, and synthetic
`A_hh`/`B_hh` were not reached.

This task does not authorize replaying or diagnosing the new blocker.

## Forbidden-operation check

- frozen fixture, grids, productivity boundary, test-only parameters,
  calibration, initialization, and tolerances: unchanged;
- economic equations, transfer mechanism, accepted policy contracts, HJB,
  generator, and KFE: unchanged;
- parameters were not tuned after the result;
- no same-task diagnosis, adjustment, repair, or second fixture invocation was
  performed;
- no candidate was forced and no constraint was relaxed;
- no artificial transition, recurrent-class selection, invariant mixture, or
  normalization trick was introduced;
- upper-buffer HJB, connectivity, uniqueness, KFE, and accounting gates were
  not reached;
- transition solver and AR(1) shock engine: not implemented or run;
- IRF/dissertation experiment: not run;
- Results prose and MATLAB-Python parity claim: not produced;
- MATLAB and protected scientific sources: not read, run, or modified;
- pull, checkout, merge, reset, clean, commit, and push: not performed;
- all pre-existing untracked research files and prior evidence: preserved.

## Git status

- final `HEAD=46d98d140cebcefb795c14f3ba8f61a515d5f6ac`;
- final `origin/main=7f92117d3505e863ef6fd271e627b672cf118fe2`;
- relation: `0 ahead / 50 behind`;
- tracked staged modifications: none;
- tracked unstaged modifications: none;
- retained research tree remains untracked relative to the old local baseline;
- this task adds only this new untracked evidence report.

## Recommended next gate

Do not proceed to `CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE`.

Recommend a new bounded, read-only policy-selection diagnostic task for the
primary-HJB upper-`a`/interior-`b` failure at
`(a,b,z)=(1.0,2.5,0.8125)`. It should classify candidate construction,
upper-`a` boundary direction, derivative availability, multipliers,
complementarity, and KKT rejections without invoking the frozen steady-state
runner. Any repair or later rerun requires separate exact live GitHub authority.
