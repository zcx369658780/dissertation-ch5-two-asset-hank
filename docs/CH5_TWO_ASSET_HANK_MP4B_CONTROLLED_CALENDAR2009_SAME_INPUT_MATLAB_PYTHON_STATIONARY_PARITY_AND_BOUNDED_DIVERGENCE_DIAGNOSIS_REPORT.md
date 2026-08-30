# Chapter 5 Two-Asset HANK MP4B Controlled Calendar-2009 Stationary Parity Report

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Live task authority: `c2c7c430eab5456f74673b93646baaf47f93c2aa`

## 1. Terminal verdict

`MP4B_CONTROLLED_CALENDAR2009_STATIONARY_PARITY_BLOCKED`

Blocking condition:

`REQUIRED_CONTROLLING_RULE_FILES_MISSING_FROM_LIVE_MAIN`

The live MP4B task requires two repository rules to be read and obeyed before execution, but neither exists in the worktree, `HEAD`, or live `origin/main`:

- `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
- `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`

The task also requires every preflight to pass before scientific execution. Execution therefore stopped at the controlling-authority gate. No source-prepared state was constructed, `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS` was not claimed, and neither scientific run was invoked.

## 2. Live continuity

- Fresh fetch observed local accepted MP4A2 commit `85772bc6920db58cd6ec38bf8e1d7a5d593e12fc` one commit behind live `origin/main`.
- Fast-forward-only synchronization reached `HEAD == origin/main == c2c7c430eab5456f74673b93646baaf47f93c2aa`.
- The live task commit is a direct child of accepted MP4A2: `HEAD^ == 85772bc6920db58cd6ec38bf8e1d7a5d593e12fc`.
- Worktree was clean at start.
- The live task and `project_rules/PROJECT_RULE_INDEX_CURRENT.md` were read successfully.
- `AGENTS.md` and the available GitHub capability rule were read successfully.

## 3. Missing-rule proof

For each missing path:

| Check | Local safety rule | MATLAB diagnostic rule |
|---|---:|---:|
| worktree `Test-Path` | false | false |
| `git cat-file -e HEAD:<path>` | exit 128 | exit 128 |
| `git cat-file -e origin/main:<path>` | exit 128 | exit 128 |

The complete live `project_rules/` directory contains only:

- `PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `PROJECT_RULE_INDEX_CURRENT.md`

No similarly named file was substituted and no rule content was inferred from memory, prior repositories, or general practice.

## 4. Pre-solver same-input gate

Required gate: `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

Status: **NOT REACHED / NOT ESTABLISHED**.

Because controlling authority was incomplete, the following were deliberately not performed:

- MATLAB/Python prepared-state construction;
- canonical/runtime manifest comparison;
- cache/runtime comparison rerun;
- household grid/switching-generator comparison;
- controller/numerics equality comparison;
- output-root creation;
- MATLAB checkcode or executable invocation;
- Python empirical runtime integration or model invocation.

This report does not downgrade or alter the accepted MP4A2 canonical input identity. It only records that MP4B could not lawfully advance to its own prepared-state equality gate.

## 5. Scientific call ledger

| Scientific/model operation | Calls |
|---|---:|
| corrected calendar-2009 MATLAB stationary route | 0 |
| corrected calendar-2009 Python stationary route | 0 |
| MATLAB household/HJB/KFE internal calls | 0 |
| Python household/HJB/KFE internal calls | 0 |
| legacy wrong-year MATLAB route | 0 |
| 2010--2023 batch | 0 |
| shocks/AR1 | 0 |
| transition/dynamics/IRF | 0 |
| legacy one-asset R5 | 0 |
| Results | 0 |

No scientific run budget was consumed. This does not authorize execution or reuse of the same MP4B task after its blocked terminal; a live successor must re-establish authority.

## 6. Run roots, convergence, and iterations

| Item | Status |
|---|---|
| MATLAB run root | NOT CREATED |
| Python run root | NOT CREATED |
| MATLAB output manifest | NOT CREATED |
| Python output manifest | NOT CREATED |
| MATLAB convergence status | NOT RUN |
| Python convergence status | NOT RUN |
| MATLAB outer iterations | 0 |
| Python outer iterations | 0 |

No local scientific output, partial trace, stationary object, or model warning/error artifact exists from this invocation.

## 7. Layer-by-layer parity and first divergence

| Comparison layer | Status |
|---|---|
| controlling authority | **FIRST BLOCKING STAGE** |
| prepared-state equality | NOT REACHED |
| pre-solver annual identity | NOT REACHED |
| first-turn household inputs | NOT RUN |
| first-turn household outputs | NOT RUN |
| migration labor | NOT RUN |
| capital / `Kt_supply` / `rah` | NOT RUN |
| firm block | NOT RUN |
| wage / monetary / fiscal | NOT RUN |
| controller history | NOT RUN |
| final 31-province stationary state | NOT RUN |

First divergence: **not a numerical/model divergence**. The first terminal difference is between the live task's mandatory authority set and the rule files actually present on live `main`.

Root-cause status: infrastructure/governance publication failure. The five scientific mismatch classifications are inapplicable because neither same-input preparation nor either scientific route ran.

## 8. Qualitative diagnostics

Sign agreement, province ranking, cross-province direction/correlation, and Chapter 5 interpretation effects are all **NOT AVAILABLE**. Reporting them without scientific outputs would be fabrication. No qualitative diagnostic can be inferred from MP4A2 input preparation alone.

## 9. Mismatch and residual lists

- Material scientific mismatch list: not evaluated; no scientific comparison ran.
- Unresolved scientific residual list: not evaluated; no stationary objects exist.
- Source/environment failure list:
  1. missing `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md` on live `main`;
  2. missing `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md` on live `main`.

## 10. Files read and written

Read successfully:

- live MP4B task;
- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`;
- named roadmap, Owner decisions, and MP4A2 report until the mandatory-rule absence was confirmed.

Repository write: this report only.

No production source, validator, MATLAB helper, test, roadmap, protected MATLAB source, primary workbook, cache, canonical artifact, or historical repository was modified.

## 11. Tests and checks

- Fresh fetch / direct-parent continuity: PASS.
- Clean-start worktree: PASS.
- Live task existence and SHA: PASS.
- Required rule-path existence: **FAIL (terminal preflight)**.
- Git object read-back for missing paths: confirms absence.
- Prepared-state equality tests: NOT RUN.
- MP1--MP4A2 focused regression: NOT RUN after terminal authority failure.
- MATLAB static/checkcode preflight: NOT RUN.
- Disk/output-root preflight: NOT RUN.
- Scientific/model tests: NOT RUN.
- `git diff --check`: performed for this text-only report at closeout.

## 12. Forbidden-operation check

PASS. No MATLAB or Python model was run. The legacy wrong-year route, 2010--2023 batch, shocks, transition, dynamics, IRF, legacy R5, and Results were not accessed or executed. No run root was created, no primary/cache/canonical bytes were changed, and no accepted MP1--MP4A2 implementation was modified.

## 13. Acceptance level

No MP4B acceptance or parity marker is frozen. In particular:

- `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_ACCEPTED`: not established;
- household/outer/controller/final stationary parity: not evaluated;
- stationary route acceptance: not granted.

The accepted MP4A2 preparation remains unchanged and does not itself satisfy MP4B.

## 14. Exactly one recommended next gate

**Publish and independently read back the two missing controlling rule files on live GitHub `main`, then issue one new MP4B execution authority that names their exact accepted identities and re-establishes the full pre-solver gate before either scientific call.**

No scientific run, repair, shock gate, or multi-year gate should precede that governance-authority repair.
