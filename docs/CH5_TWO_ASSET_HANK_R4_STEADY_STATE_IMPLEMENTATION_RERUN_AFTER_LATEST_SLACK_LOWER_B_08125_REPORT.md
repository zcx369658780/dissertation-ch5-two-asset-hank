# CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125 — Evidence Report

## Verdict

`FAIL_CLOSED`

The frozen fixture `R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1` was invoked exactly once under the live task authority. Both the 25-point primary HJB solve and the 29-point upper-buffer HJB solve returned far enough for the common-core truncation checks to run. The scalar common-core normalized-change guard passed, but the next required check terminated the run:

```text
ch5_two_asset_hank.steady_state.SteadyStateValidationError: 25-vs-29 common-core candidate identities differ
```

The exception arose at `src/ch5_two_asset_hank/steady_state.py:206`. Per the task failure rule, execution stopped immediately. The fixture was not rerun, and no diagnosis, adjustment, or repair was attempted.

## Authority and files read

Live authority was read from `origin/main` after a fresh fetch because the local checkout is intentionally behind live GitHub `main`:

- `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- the routing rule linked by the current rule index
- `AGENTS.md`

Execution inputs and prior accepted evidence read:

- `src/ch5_two_asset_hank/steady_state.py`
- `tests/test_r4_steady_state.py`
- the R4 steady-state authorization report
- the immediately preceding steady-state rerun failure report
- `docs/CH5_TWO_ASSET_HANK_R4_UPPER_A_LOWER_B_POLICY_SELECTION_FAILURE_LATEST_RESOLUTION_08125_REPORT.md`

## Files written

- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125_REPORT.md` (this evidence report)

No model source, test source, fixture, rule, or task file was modified. Python may refresh ignored bytecode/cache artifacts during compilation and testing; these are not tracked implementation changes.

## Tests executed

1. Static compilation:

   ```text
   python.exe -m py_compile src/ch5_two_asset_hank/steady_state.py src/ch5_two_asset_hank/hjb.py src/ch5_two_asset_hank/policies.py src/ch5_two_asset_hank/boundaries.py src/ch5_two_asset_hank/generator.py src/ch5_two_asset_hank/kfe.py tests/test_r4_steady_state.py
   ```

   Result: `PASS` (exit code 0, no output).

2. Full test set excluding the frozen steady-state target:

   ```text
   python.exe -m pytest -q -p no:cacheprovider --ignore=tests/test_r4_steady_state.py
   ```

   Result: `29 passed in 3.57s`.

3. Frozen fixture invocation:

   `R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1` was invoked exactly once through `run_frozen_r4_steady_state()`.

   Result: exit code 1 with the terminal `SteadyStateValidationError` quoted above.

No steady-state pytest target and no second fixture invocation were run.

## Steady-state diagnostics

- Primary 25-point HJB: completed sufficiently for the truncation comparison; iteration count and terminal residual were not emitted before the fail-closed exception.
- Upper-buffer 29-point HJB: completed sufficiently for the truncation comparison; iteration count and terminal residual were not emitted before the fail-closed exception.
- Common-core normalized changes for value, consumption, transfer, and labor: all passed the hard `1e-3` guard; exact values were not emitted because the function raised before returning diagnostics.
- Common-core candidate identities: `FAIL`; the 25-point and 29-point candidate-id arrays were not exactly equal.
- Endogenous upward/downward illiquid-asset edges: not reached.
- Unique closed recurrent class: not reached.
- Left nullity: not reached.
- Stationary KFE residual, normalization, and minimum mass: not reached.
- Mass/density consistency: not reached.
- Synthetic `A_hh` and `B_hh`: not reached.

No inference is made about the location, count, economic cause, or admissibility impact of the candidate-identity differences. Obtaining those facts requires a separately authorized read-only diagnostic gate.

## Forbidden-operation check

- Frozen fixture invocation count: exactly one.
- Same-task retry, parameter tuning, diagnosis, or repair: none.
- Fixture, grids, productivity boundary, calibration, transfer mechanism, or economic equations changed: no.
- Generator changes, recurrent-class selection, invariant mixtures, or artificial transitions: none.
- Transition solver, AR(1) engine, IRFs, Results prose, or MATLAB-Python parity claim: none.
- Git pull, checkout, merge, reset, clean, commit, or push: none.
- Existing untracked research files: preserved.

## Git status at evidence capture

- `HEAD`: `46d98d140cebcefb795c14f3ba8f61a515d5f6ac`
- `origin/main`: `fd551da2a2c94c37c79dd78b9074c48360fdfa36`
- ahead/behind: `0 ahead / 56 behind`
- tracked staged changes: none
- tracked unstaged changes: none before this report was written
- existing untracked paths before this report: 69; preserved

This report is an additional untracked evidence file unless and until a later task explicitly authorizes Git staging or publication.

## Acceptance level

`R4_STEADY_STATE_IMPLEMENTATION_RERUN_FAIL_CLOSED`

This is not R4 steady-state acceptance. `CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE` must not be entered from this result.

## Recommended next gate

A new, precisely authorized, read-only diagnostic gate for the `25-vs-29 common-core candidate identities differ` failure. It should identify the differing common-core states and compare their selected candidate identities, boundary regimes, directional derivatives, controls, KKT/slackness status, and tie/selection logic without rerunning the frozen steady-state fixture and without modifying accepted implementation.
