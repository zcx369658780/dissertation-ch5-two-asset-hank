# CH5 MP4C 2018 KFE Owner-decision recovery and option matrix — zero science

Date: 2026-09-15.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Status: ACTIVE.

## Objective

Create an Owner-ready, source-backed decision package for the unresolved corrected-2018 finite-box upper-`b` leakage / MATLAB-style pinning KFE blocker **without running any scientific model code and without choosing the scientific closure**.

The package must recover the exact repository definitions and provenance of deferred KFE redesign proposals D1-D3 (or explicitly certify that an exact definition is absent), then map each recoverable option to its scientific and integration consequences.

## Required startup authority

Fresh-fetch `origin/main`, then read at minimum:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_CLOSURE_ROUTE_FREEZE_20260915.md`
6. `docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_ACCEPTANCE.md`
7. `docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_REPORT.md`
8. the exact predecessor tasks/reports/acceptances and Git history needed to locate D1-D3.

Do not use `zcx369658780/deep-learning-hank` as authority and do not modify it.

## Allowed work

Zero-science only:

- Git/GitHub history and repository text reads;
- static source reads of the already designated protected MATLAB/Python KFE/HJB code paths when needed to map an option to source semantics;
- hashes, textual diffs, source-line mapping, equation/contract comparison;
- creation of one decision report;
- ordinary markdown/link/readback checks.

Protected MATLAB remains read-only.

## Forbidden work

Scientific/model/solver calls are all zero:

- HJB = 0
- KFE = 0
- outer/firm/wage-return recalculation = 0
- MATLAB = 0
- GE/annual/downstream = 0
- shock/IRF/Results = 0

Do not modify production Python/MATLAB, grids, boundaries, equations, selectors, floor logic, pin row, RHS source, tolerances, maxit, calibration, guards, or asset domain.

Do not adopt D1, D2, D3, or any newly invented alternative. Do not infer an economic household entry/exit process from the algebraic balancing source.

## Required decision package

Write:

`docs/CH5_MP4C_2018_KFE_OWNER_DECISION_RECOVERY_AND_OPTION_MATRIX_REPORT.md`

The report must contain:

1. **Authority recovery** — exact file/commit/history location defining each of D1, D2, D3. Quote only enough text to identify the option; prefer paraphrase plus exact path/commit/source lines.
2. **Missing-definition fail-closed rule** — if any D-item cannot be recovered exactly, mark it `NOT_RECOVERED_FROM_REPOSITORY_AUTHORITY`; do not reconstruct it from chat memory or model knowledge.
3. **Current accepted mechanism** — concise restatement of the accepted five-turn leakage/pinning evidence, clearly separating source-free residual, upper-`b` escape, dropped pin equation, and the non-economic algebraic balancing source.
4. **Option matrix** — for every recovered D-item, identify:
   - what finite-domain/KFE object changes;
   - whether HJB boundary semantics also change;
   - whether it is source-faithful, corrected-successor redesign, diagnostic-only, or another classification explicitly supported by authority;
   - expected mass-conservation implication as an algebraic consequence only;
   - parity implications versus protected MATLAB;
   - whether asset-domain/grid meaning changes;
   - whether a new economic assumption is introduced;
   - smallest future implementation/validation experiment that would be required *after Owner selection*.
5. **Non-options** — list changes already ruled out by accepted authority (for example automatic bmax expansion or pin/source changes merely to force PASS) only where supported by live documents.
6. **Owner decision form** — a compact final section presenting the exact choices that still require Owner selection. Do not recommend an option unless repository authority already contains an explicit Reviewer recommendation; otherwise present consequences neutrally.
7. **Call ledger** — certify all scientific/model/solver calls are zero.

## Acceptance conditions

PASS only if:

- every D1-D3 definition is either traced to repository authority or explicitly marked unrecovered;
- no option is silently adopted or scientifically reinterpreted;
- current accepted KFE mechanism is represented consistently with the five-turn acceptance;
- source-faithful versus redesigned-successor consequences are kept distinct;
- report is sufficient for Owner to make the next scientific choice without any new model run;
- changed paths are exactly the report (plus task-owned non-scientific evidence only if strictly necessary and explicitly listed in the report);
- no production science file changes;
- all scientific/model/solver call counts remain zero.

## Stop conditions

Stop and report rather than improvise if:

- D1-D3 cannot be uniquely recovered;
- live authority materially changed the KFE mechanism or task premise;
- a requested conclusion would require a new model call or a substantive scientific choice.

## Git / publication

Use an isolated worktree if useful. Preserve unrelated user state. No reset/clean/stash/force-push. Stage explicit paths only. Commit and push the report on a task branch; return branch name, commit SHA, exact changed paths, call ledger, and readback evidence. Do not merge to `main` unless a later Reviewer action explicitly accepts it.
