# CH5_TWO_ASSET_HANK_R4_EXECUTION_EVIDENCE_AND_LOCAL_IMPLEMENTATION_AUTHORITY_RECONCILIATION

## Task

Perform a read-only provenance and authority reconciliation for the consumed R4 frozen steady-state rerun before any candidate-identity diagnosis or scientific repair.

## Authority

This task is the sole authority for read-only reconciliation of the local implementation/evidence identity against live GitHub main.

It does not authorize any model rerun, diagnostic solver execution, source modification, Git synchronization, commit, push, or scientific repair.

## Why this gate exists

The previous one-run R4 task is consumed and reported `FAIL_CLOSED` at the 25-vs-29 common-core candidate-identity comparison.

Independent GitHub review found that live `main` contains the governance/task tree but does not expose the cited `src/ch5_two_asset_hank/steady_state.py` or the cited local execution report at their reported paths. The local checkout was also reported far behind `origin/main` with many untracked files.

Before diagnosing candidate identities, the exact implementation and evidence used by the consumed run must therefore be provenance-bound.

## Required read-back before work

Fresh-fetch and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125.md`
- this task file

## Required local preflight

Record without changing repository state:

- current branch;
- `HEAD`;
- `origin/main`;
- ahead/behind counts;
- `git status --short --untracked-files=all`;
- tracked staged count;
- tracked unstaged count;
- untracked count.

Do not pull, merge, rebase, reset, checkout, clean, stash, stage, commit, or push.

## Required source/evidence identity inventory

Identify every local file materially required to reconstruct the consumed R4 run, including at minimum where present:

- package configuration / environment files used by the run;
- `src/ch5_two_asset_hank/steady_state.py`;
- HJB / policy-selection implementation modules used by the run;
- generator / KFE implementation modules used by the run;
- frozen fixture/config/runner used for `R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1`;
- `tests/test_r4_steady_state.py`;
- any supporting tests explicitly relied on by the consumed run;
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125_REPORT.md`.

For each materially required file report:

- exact local path relative to repository root;
- file exists: yes/no;
- Git classification: tracked / untracked / ignored / absent;
- blob identity at local `HEAD`, if tracked;
- blob identity at `origin/main`, if present there;
- local SHA-256;
- size in bytes;
- whether live GitHub can reconstruct the exact consumed-run file content.

Do not print secrets, credentials, private data, or unrelated untracked-file contents.

## Required execution-evidence reconciliation

Read the existing local R4 rerun report only if it exists.

Confirm from existing evidence only:

- whether the one-run budget was consumed;
- reported command or runner identity;
- reported terminal exception and location;
- reported pre-failure checks;
- whether steady-state pytest was intentionally not run after the consumed failure;
- report SHA-256;
- whether the report itself is GitHub-bound.

Do not rerun anything to reproduce or expand the failure.

## Classification

Return exactly one primary classification:

1. `R4_CONSUMED_RUN_FULLY_GITHUB_RECONSTRUCTIBLE`
   - all material implementation/evidence files are bound to identifiable GitHub blobs/commits sufficient to reconstruct the consumed run;

2. `R4_CONSUMED_RUN_PARTIALLY_GITHUB_BOUND_LOCAL_IMPLEMENTATION_IDENTITY_REQUIRED`
   - governance authority is on GitHub but one or more material implementation/evidence files are local-only, untracked, or otherwise not reconstructible from GitHub;

3. `R4_CONSUMED_RUN_EVIDENCE_IDENTITY_CONTRADICTORY_BLOCKED`
   - hashes, file identities, task identity, or execution evidence are internally inconsistent.

## Forbidden operations

Do not:

- rerun the frozen fixture;
- run steady-state pytest;
- run HJB/KFE/generator solvers;
- perform candidate-identity diagnosis beyond reading existing evidence;
- modify source, tests, fixture, report, rules, or tasks;
- tune parameters or tolerances;
- modify economic equations or policy contracts;
- add artificial transitions;
- select recurrent classes;
- create invariant mixtures;
- implement transition solver;
- implement AR(1);
- run IRFs;
- claim MATLAB-Python parity;
- write Results prose;
- pull/merge/rebase/reset/checkout/clean/stash;
- stage/commit/push.

## Files written

None.

This is a read-only reconciliation task.

## Final response requirements

Report:

- verdict;
- files read;
- exact local/git identity table for material implementation/evidence files;
- consumed-run evidence summary;
- GitHub reconstructibility classification;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## Recommended next-gate logic

If classification is `R4_CONSUMED_RUN_FULLY_GITHUB_RECONSTRUCTIBLE`:

- recommend a new read-only candidate-identity diagnostic gate for the differing 25-vs-29 common-core states.

If classification is `R4_CONSUMED_RUN_PARTIALLY_GITHUB_BOUND_LOCAL_IMPLEMENTATION_IDENTITY_REQUIRED`:

- recommend an owner-authorized implementation/evidence baseline publication or equivalent GitHub binding gate before scientific candidate diagnosis.

If classification is `R4_CONSUMED_RUN_EVIDENCE_IDENTITY_CONTRADICTORY_BLOCKED`:

- stop and recommend evidence/provenance resolution only.
