# CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC

## Task

Diagnose, without scientific repair, why the frozen R4 25-point primary HJB solve and 29-point upper-buffer HJB solve select different candidate identities on their shared common core.

This is a bounded, non-mutating scientific diagnostic gate. It is not a steady-state rerun, repair gate, fixture-change gate, acceptance gate, or MATLAB-Python parity gate.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Frozen implementation provenance

The consumed-run implementation/evidence baseline is:

`546b88be6316526682c5a02ef4671021d0f387c3`

Commit subject:

`Bind consumed R4 implementation and evidence baseline`

This baseline is provenance evidence only and is not scientific acceptance.

The exact source blobs used for diagnosis MUST be identical to the corresponding source blobs at that baseline. If live main contains changed model-source blobs, stop and report source drift instead of diagnosing.

## Required live authority read-back

Before work, fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_CONSUMED_RUN_IMPLEMENTATION_EVIDENCE_BASELINE_PUBLICATION.md`
- this task file
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125_REPORT.md`

Read the frozen implementation needed for diagnosis, including at minimum:

- `src/ch5_two_asset_hank/steady_state.py`
- `src/ch5_two_asset_hank/hjb.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/derivatives.py`
- `src/ch5_two_asset_hank/boundaries.py`
- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/contracts.py`

## Workspace requirement

Use a fresh isolated clone/worktree rooted at live `origin/main`.

Do not use the stale historical source checkout as the diagnostic execution workspace.

Before diagnostic execution record:

- live `origin/main`;
- diagnostic workspace root;
- branch/ref;
- `git status --short --untracked-files=all`;
- source blob identities for the model files above.

The workspace must be clean before diagnostic execution.

## Source immutability gate

Before execution, compare the following live-main source blobs with the consumed-run baseline commit `546b88be6316526682c5a02ef4671021d0f387c3`:

- `src/ch5_two_asset_hank/steady_state.py`
- `src/ch5_two_asset_hank/hjb.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/derivatives.py`
- `src/ch5_two_asset_hank/boundaries.py`
- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/generator.py`
- `src/ch5_two_asset_hank/productivity.py`
- `src/ch5_two_asset_hank/indexing.py`
- `src/ch5_two_asset_hank/kfe.py`
- `src/ch5_two_asset_hank/kfe_contract.py`

If any source blob differs, stop with:

`BLOCKED_R4_DIAGNOSTIC_SOURCE_DRIFT_FROM_CONSUMED_BASELINE`

Do not repair or choose a newer implementation.

## Diagnostic execution authority

Authorize exactly one bounded diagnostic reproduction consisting of:

1. one call to the existing internal HJB solve path for the frozen 25-point productivity grid `z=0.5:0.0625:2.0`;
2. one call to the existing internal HJB solve path for the frozen 29-point upper-buffer grid `z=0.5:0.0625:2.25`;
3. comparison only on the common core `z in [0.5,1.5]`.

Use the exact frozen R4 configuration embedded in the accepted implementation.

Do NOT call `run_frozen_r4_steady_state()`.

Do NOT continue to connectivity, recurrent-class, left-nullity, KFE, mass/density, or aggregate calculations.

Do NOT run `tests/test_r4_steady_state.py` or any pytest suite.

This two-HJB diagnostic pair is a separate diagnostic authorization and does not create or replenish any steady-state fixture rerun budget.

Set execution so repository bytecode/cache artifacts are not written where feasible, e.g. `PYTHONDONTWRITEBYTECODE=1`, and do not create persistent scientific outputs besides the authorized Markdown report.

## Required mismatch localization

On the common core, report:

- total number of compared states;
- total number of candidate-identity mismatches;
- every mismatching state as both tensor index `(i_a,i_b,i_z_core)` and economic coordinates `(a,b,z)`;
- 25-point selected `candidate_id`;
- 29-point selected `candidate_id`;
- whether each mismatch is interior/lower/upper in `a` and `b`;
- whether mismatches form a contiguous productivity region or isolated states.

No mismatch may be summarized away. If the count is large, write the complete table in the report.

## Required state-level comparison

For every mismatching state, compare the 25-point and 29-point solutions for at least:

### Value and directional derivatives

- value function;
- `V_a^F`, `V_a^B` and validity flags;
- `V_b^F`, `V_b^B` and validity flags;
- any zero-drift shadow derivative actually used by the selected branch, if reconstructible without source mutation.

### Selected controls and drifts

- consumption `c`;
- labor vector and aggregate labor if applicable;
- transfer `d`;
- adjustment cost;
- `mu_a`;
- `mu_b`;
- selected candidate identifier;
- implied upwind directions.

### Boundary/KKT state

- active lower/upper boundary status for both assets;
- `lambda_a` and `lambda_b`;
- stored KKT state residual;
- available KKT component residuals/slackness diagnostics;
- boundary feasibility/violation.

## Required candidate-selection diagnosis

Using existing source logic and, where possible without modifying repository source, an external ephemeral diagnostic calculation, determine for each mismatch whether the identity difference is attributable to one of the following classes:

1. `MATERIAL_POLICY_DIFFERENCE`
   - materially different controls/drifts/Hamiltonian choice;

2. `NEAR_TIE_SELECTION_INSTABILITY`
   - competing admissible candidates have Hamiltonians sufficiently close that the deterministic sort/tie logic changes identity under the small truncation-induced derivative difference;

3. `IDENTIFIER_ONLY_EQUIVALENCE`
   - candidate identifiers differ but resulting controls, drifts, KKT and Hamiltonian are equivalent within diagnostic tolerance;

4. `BOUNDARY_REGIME_SWITCH`
   - active/slack or directional boundary classification changes between 25 and 29 solutions;

5. `CANDIDATE_CONSTRUCTION_AVAILABILITY_SWITCH`
   - one candidate exists/is admissible in one solve but not the other because derivative interval, root certification, direction, boundary or KKT admissibility crosses a threshold;

6. `UNRESOLVED_WITH_EXISTING_NONMUTATING_EVIDENCE`.

For competing candidates that can be reconstructed without changing source behavior, report:

- candidate identifiers;
- Hamiltonian values;
- Hamiltonian gap to selected candidate;
- controls/drifts;
- KKT/boundary admissibility;
- exact reason a candidate is excluded if determinable;
- relevance of the deterministic sort key in `select_policy`.

Do not monkeypatch production functions to alter behavior. Do not edit source to expose candidate lists. A temporary diagnostic script outside tracked repository paths may call existing pure/internal helpers to reconstruct candidate information, but it must not change the model state or production source.

## Quantitative comparison tolerances

This gate is diagnostic, not acceptance. Do not tune tolerances.

Report raw differences and additionally flag:

- absolute control/drift/KKT differences relative to `1e-7` and `1e-12` where those thresholds are already part of the frozen contracts;
- Hamiltonian gaps in raw units and relative scale;
- whether identifier differences survive when comparing controls/drifts at machine-scale precision.

Do not invent a new acceptance tolerance that converts failure into PASS.

## Required root-cause conclusion

Return exactly one primary scientific diagnosis:

- `TRUNCATION_SENSITIVITY_MATERIAL_POLICY_SELECTION`
- `TRUNCATION_SENSITIVITY_NEAR_TIE_OR_IDENTIFIER_ONLY`
- `BOUNDARY_OR_KKT_THRESHOLD_CROSSING`
- `CANDIDATE_CONSTRUCTION_GAP`
- `MIXED_MULTIPLE_MISMATCH_CLASSES`
- `DIAGNOSIS_INCONCLUSIVE_WITH_NONMUTATING_EVIDENCE`

Also state whether the existing hard requirement of exact `candidate_id` equality across 25/29 is scientifically justified, overly strict, or cannot yet be judged. This is a diagnosis only; do not change that requirement in this task.

## Report authorization

Write exactly one new report:

`docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`

The report must contain:

- authority/baseline identity;
- exact diagnostic commands or ephemeral-script identity;
- source blob verification;
- mismatch table;
- state-level derivative/control/KKT comparison;
- candidate-selection classification;
- root-cause conclusion;
- whether exact candidate-ID equality appears scientifically necessary;
- forbidden-operation check;
- recommended next gate.

Do not modify any existing file.

## Commit/push authorization for report only

If and only if the diagnostic completes without source mutation and the report is the only repository change:

- explicitly stage only the report path;
- create one commit containing only that report;
- fresh-fetch before push;
- fast-forward push to live `main` only if remote main has not moved;
- no force-push, merge or rebase.

Suggested commit subject:

`Diagnose R4 common-core candidate identity mismatch`

If live main moves before push, stop and preserve the local report without merging/rebasing.

## Forbidden operations

Do not:

- modify model source, tests, fixture, configuration, parameters, tolerance, equations or policy contracts;
- call `run_frozen_r4_steady_state()`;
- rerun the consumed steady-state fixture;
- run steady-state pytest;
- continue beyond the common-core candidate comparison into connectivity/KFE/aggregates;
- tune values after seeing results;
- add artificial transitions;
- select recurrent classes;
- create invariant mixtures;
- implement transition solver;
- implement AR(1);
- run IRFs;
- read or run MATLAB for parity;
- claim MATLAB-Python parity;
- write Results prose;
- modify the stale historical source checkout;
- stage any file except the single authorized diagnostic report;
- use `git add .` or `git add -A`;
- force-push.

## Acceptance meaning

A PASS means only:

`R4_COMMON_CORE_CANDIDATE_IDENTITY_ROOT_CAUSE_DIAGNOSED__NO_REPAIR_AUTHORITY`

It does not mean R4 steady-state acceptance.

## Final response requirements

Report:

- verdict;
- files read/written;
- live main and consumed baseline identities;
- source blob verification;
- exact diagnostic execution count;
- mismatch count and complete state list;
- derivative/control/drift/KKT comparison summary;
- candidate-selection root-cause classification;
- scientific assessment of exact candidate-ID equality requirement;
- report path and commit hash if published;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Recommended next-gate logic

If diagnosis is `TRUNCATION_SENSITIVITY_NEAR_TIE_OR_IDENTIFIER_ONLY` and controls/drifts/KKT are economically/numerically equivalent:

- recommend a planning-only acceptance-contract review gate before any code change.

If diagnosis identifies a material policy-selection, boundary/KKT, or candidate-construction defect:

- recommend a narrowly scoped repair-design gate, followed by a separate implementation gate.

If diagnosis is mixed or inconclusive:

- recommend a narrower state-specific diagnostic gate.

No repair is authorized by this task.
