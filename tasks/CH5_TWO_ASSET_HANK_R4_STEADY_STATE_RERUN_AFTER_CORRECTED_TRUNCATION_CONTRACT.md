# CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT

## Task

Execute exactly one full frozen R4 steady-state run after the corrected truncation contract was implemented and bounded 25/29 compatibility was validated.

This is a one-shot fail-closed steady-state execution gate. It does not authorize scientific repair, tuning, MATLAB parity, AR(1), transition dynamics, IRFs, calibration changes, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Scientific authority

Accepted implementation baseline for this rerun:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Commit subject:

`Correct R4 cross-truncation compatibility contract`

Accepted implementation status:

`R4_TRUNCATION_CONTRACT_CORRECTED_AND_BOUNDED_25_29_COMPATIBILITY_VALIDATED__FULL_STEADY_STATE_NOT_RERUN`

The prior consumed steady-state run remains a historical FAIL under the superseded exact raw-ID contract. This task creates a new, separate one-run authorization under the corrected accepted contract.

## Required live read-back

Before execution, fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_AFTER_CROSS_TRUNCATION_RECONCILIATION.md`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION_REPORT.md`
- this task file
- current `src/ch5_two_asset_hank/steady_state.py`
- current `src/ch5_two_asset_hank/policies.py`
- current `src/ch5_two_asset_hank/contracts.py`
- current `src/ch5_two_asset_hank/generator.py`
- current `src/ch5_two_asset_hank/kfe.py`
- current `tests/test_r4_steady_state.py`

## Fresh workspace and source-identity gate

Use a fresh isolated clone/worktree rooted at live `origin/main`.

Record:

- live `origin/main`;
- workspace root;
- branch/ref;
- clean pre-run `git status --short --untracked-files=all`.

Before any Python execution, verify that all model/test source relevant to the full R4 run is byte-identical to commit `7a2388a2ba89073e307f05a909570e8c40a4be13`, except for governance/task/report files added after that commit.

At minimum verify Git blob identity for:

- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/steady_state.py`
- `src/ch5_two_asset_hank/hjb.py`
- `src/ch5_two_asset_hank/boundaries.py`
- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/derivatives.py`
- `src/ch5_two_asset_hank/generator.py`
- `src/ch5_two_asset_hank/indexing.py`
- `src/ch5_two_asset_hank/productivity.py`
- `src/ch5_two_asset_hank/kfe.py`
- `src/ch5_two_asset_hank/kfe_contract.py`
- `tests/test_r4_steady_state.py`
- `tests/test_r4_truncation_acceptance_contract.py`

If any scientific/test source drift is detected, stop without consuming the one-run budget:

`BLOCKED_R4_STEADY_STATE_RERUN_SOURCE_DRIFT`

## Frozen fixture

Execute exactly:

`R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1`

Do not change:

- `a`, `b`, or `z` grids;
- productivity boundaries;
- initialization;
- fixture parameters;
- economic parameters;
- transfer mechanism;
- equations or FOCs;
- boundary/KKT economics;
- corrected truncation contract;
- `1e-12`, `1e-7`, `1e-3`, HJB, generator, or KFE tolerances.

## Pre-run engineering checks

Before consuming the one-run budget, allowed checks are:

1. static compilation of the relevant Python source;
2. the non-steady-state pytest suite with `tests/test_r4_steady_state.py` explicitly excluded;
3. `git diff --check`.

If any pre-run check fails, stop without calling the frozen runner and report the failure. Do not repair in this task.

## Exactly-one full steady-state execution

After all pre-run gates pass, call:

`run_frozen_r4_steady_state()`

**exactly once**.

Recommended execution is a small ephemeral script outside tracked repository paths that imports the current live source, calls the runner once, retains the returned result in memory, and prints/serializes all required diagnostics from that single returned object.

Do not execute `tests/test_r4_steady_state.py`, because that test itself calls `run_frozen_r4_steady_state()` and would consume a second invocation.

Do not call the runner indirectly through any other code path after the one authorized call.

The one-run budget is consumed once the function is entered, regardless of PASS or exception.

## Required full-run scientific checks

The run must proceed fail-closed through the existing implementation and report all reached checks.

### HJB / truncation

Verify/report:

- primary 25-point HJB completion and residual;
- upper-buffer 29-point HJB completion and residual;
- KKT residuals;
- generator row-sum/off-diagonal validity;
- common-core normalized changes for:
  - value;
  - consumption;
  - transfer;
  - labor;
  - adjustment cost;
  - `mu_a`;
- canonical candidate compatibility;
- bilateral alias evidence for any raw-ID mismatch;
- `mu_b` Z/F/B classification compatibility;
- boundary/KKT compatibility.

### Endogenous illiquid connectivity

Verify/report:

- positive upward `a` edges > 0;
- positive downward `a` edges > 0;
- every `G_a` transition rate matches directional `mu_a/h_a` construction;
- no cross-`a` edge originates from `G_b` or `G_z`.

### Recurrent-class uniqueness

Verify/report:

- exactly one closed recurrent class;
- its `a` support spans at least two `a` indices;
- it includes the interior `a=0.5` index;
- it is not solely the computational upper `a=1.0` layer;
- left nullity equals one.

### Stationary KFE

Verify/report:

- KFE uses the accepted operator transpose contract;
- `||G^T g||_infinity <= 1e-10`;
- `|sum(g)-1| <= 1e-10`;
- minimum mass `>= -1e-12`;
- negative-mass count zero below tolerance;
- mass finite;
- density finite;
- mass/density consistency error `<= 1e-10`.

### Synthetic household aggregates

Verify/report separately:

- `A_hh` finite;
- `B_hh` finite;
- exact reported values.

These remain synthetic fixture diagnostics only and are not dissertation Results or calibration claims.

## Failure rule

At the first terminal failure:

- stop immediately;
- do not rerun the frozen fixture;
- do not run `tests/test_r4_steady_state.py` afterward;
- do not diagnose by running additional HJB/KFE/generator calculations;
- do not repair, tune, change tolerances, change fixture values, or modify source/tests;
- report exactly which acceptance stage was reached and the terminal exception/evidence.

No same-task adjustment is authorized.

## Report authorization

Write exactly one new report regardless of PASS or FAIL_CLOSED:

`docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT_REPORT.md`

The report must include:

- verdict;
- live/base commit and source-identity verification;
- files read/written;
- pre-run checks and results;
- exact frozen-run invocation count;
- HJB/truncation diagnostics;
- connectivity diagnostics;
- recurrent-class/left-nullity diagnostics;
- KFE diagnostics;
- mass/density diagnostics;
- `A_hh` and `B_hh` if reached;
- exact terminal failure if any;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Report-only commit/push authorization

No model source, tests, fixture, rule, or existing report may be modified.

After the run, whether PASS or FAIL_CLOSED, if the new report is the only repository change:

- explicitly stage only that report;
- create exactly one report-only commit;
- fresh-fetch remote before push;
- fast-forward push to live `main` only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Record R4 steady-state rerun after corrected truncation contract`

If remote main moved, preserve the report locally and stop without merge/rebase.

## Forbidden operations

Do not:

- modify model source, tests, fixture, parameters, tolerances, equations, FOCs, transfer mechanism, boundary/KKT economics, generator or KFE logic;
- call the frozen runner more than once;
- execute `tests/test_r4_steady_state.py`;
- tune after observing results;
- select recurrent classes manually;
- construct invariant mixtures;
- pin KFE rows as a scientific fix;
- add artificial transitions;
- implement AR(1), transition solver, or IRF;
- run MATLAB;
- claim MATLAB-Python parity;
- write dissertation Results prose;
- merge, rebase, reset, or force-push.

## Acceptance meaning

A task PASS means only:

`R4_FROZEN_STEADY_STATE_FULL_RUN_PASSED_UNDER_CORRECTED_TRUNCATION_CONTRACT__INDEPENDENT_ACCEPTANCE_PENDING`

It still requires independent reviewer acceptance before MATLAB-Python HA parity or any transition/AR(1) work.

A FAIL means:

`R4_FROZEN_STEADY_STATE_FULL_RUN_FAIL_CLOSED__NO_SAME_TASK_REPAIR`

## Recommended next gate

If PASS and independently accepted:

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP`

The next reviewer gate should first accept the Python steady-state evidence, then prepare the owner-facing MATLAB-Python HA structural/numerical parity checklist. It must not enter AR(1), transition dynamics, or IRFs before owner parity review.
