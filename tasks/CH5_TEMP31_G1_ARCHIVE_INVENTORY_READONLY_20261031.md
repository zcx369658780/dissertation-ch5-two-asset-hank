# CH5-TEMP31-G1 · 归档前只读盘点任务单

TASK_ID=CH5_TEMP31_G1_ARCHIVE_INVENTORY_READONLY_20261031
TASK_TYPE=LOCAL_AND_REMOTE_ARCHIVE_INVENTORY_READ_ONLY
OWNER_AUTHORIZATION=EXPLICIT_2026-10-31
STATUS=ISSUED
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_HEAD_AT_ISSUANCE=d6048c89e33bcdfdd3bb50d4b65f4418fa888d46
GOVERNANCE_TREE_AT_ISSUANCE=4bb423fbe19deb293dd60fceb438a4de7adf4c68
FIXED_PARENT=d6048c89e33bcdfdd3bb50d4b65f4418fa888d46
CANDIDATE_BRANCH=NONE__READ_ONLY_TASK_NO_CANDIDATE_BRANCH
GITHUB_EXECUTOR=GPT_DIRECT_READ_ONLY_AUDIT
LOCAL_EXECUTOR=OWNER_LOCAL_CODEX_READ_ONLY_AUDIT
SCIENCE_BUDGET=0
MODEL_CALLS=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
GIT_MUTATION_BUDGET=0
FILE_MUTATION_BUDGET=0
DELETE_BUDGET=0
MOVE_RENAME_BUDGET=0
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 1. Owner decision and purpose

Owner has decided that TEMP31 will become the sole active Python multi-province HANK research mainline. Historical programs, experiments, results, logs, source snapshots and governance records must first be identified and safely archived. Only after independent archive verification and a separate Owner decision may redundant branches or local copies be deleted.

This task is inventory only. It does not authorize archive writes, tags, branches, bundles, file copies, source changes, branch deletion, local cleanup, model execution or scientific acceptance.

Two historical source assets are explicitly protected and must never be overwritten or discarded:

1. The Python program/source state associated with the first September 2026 reproduction of the corrected 2018 multi-province model behavior.
2. The latest TEMP31 Python source that corrects duplicate wage-tax application.

The exact local identities of both assets are not presumed. Codex must locate and report their exact original paths, source identities and hashes. Do not infer that a later isolated patch is the same as the current local TEMP31 program.

## 2. Fixed GitHub reference candidates

These are reference candidates, not final Owner-approved archive identities.

### 2.1 September first-reproduction candidate

- Branch: codex/ch5-corrected-2018-single-turn-20260909
- Result/evidence commit: 90ee5b29f3be070d9f8f28c9614e1b59fe798462
- Commit tree: 7cf2741803bde15c4eaee3cbcf46d53fabcfc32c
- Parent/source-state commit: 725cbcc86756eb92bd50f477875ca30d53e88c5e
- Parent/source-state tree: 5032974d251926d802267c7cc5bcb0a64cdad6d4
- Report: docs/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION_REPORT.md
- Evidence directory: reports/mp4c_2018_corrected_single_turn_20260909/

The report records one complete ordered turn across 31 provinces, 31 HJB returns and 31 KFE returns. It explicitly does not establish stationary convergence; results_eligible=false, steady-state execution was not authorized, and MATLAB calls were zero. Preserve the report and raw evidence as historical evidence, not as formal Results.

### 2.2 September corrected runtime input-binding candidate

- Branch: codex/ch5-python-runtime-input-binding-repair-20260910
- Commit: a7bd3b1a705ff42e2933b22a8c6563ec47248ce4
- Tree: 1490e63dda5da128306e4a1dbc9f071f94170837
- Parent: e3558062a265a727e5da2f12ab7b737287db2129
- Main source path: src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py
- Git Blob: a8df732ba88a8cb343b30ae2667edce1c0a04326
- Report: docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_REPORT.md
- Evidence directory: reports/mp4c_python_runtime_input_binding_repair_20260910/

This is a distinct corrected input-binding milestone. Preserve separately from the September single-turn source/evidence and from TEMP31.

### 2.3 TEMP31 isolated single-tax R4 candidate

- Branch: codex/ch5-temp31-worksite-tauj-single-tax-isolated-20261028-r4
- Sealed receipt commit: 92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27
- Payload commit: e99c622b41b255e5312589c61c57689a42a0b3e3
- Payload parent: 5e4ec0ae4c310b8071b6aef68642fd0ffd862478
- Payload tree: 17e5e57ca917d28b29171ec88fb69cbddd164143
- Source path: src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py
- Git Blob: 90667ddc00c72b9290e91481af4835c808ecfccb
- Bytes: 10435
- SHA-256: 7cd0ec0e6038468f1d14ea52b3746e8f80f1613a9c3bd0d754f89dab74bb7571
- Task result: tasks/CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R4_20261028/result.md
- Source identity: tasks/CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R4_20261028/source_identity.json

Important limitation: R4 introduced an isolated pure module and synthetic tests. Its own report states that production wiring, real initialization/HouseholdInputs/HJB consumer verification, empirical net-wage provenance, labor units and fiscal adoption were not completed. The source identity reports gpt_independent_pass=false. Do not call it the production TEMP31 source or claim scientific acceptance. It is a protected historical candidate pending comparison with the actual latest local TEMP31 snapshot.

### 2.4 Later TEMP31 references that must not be conflated

If present in the local asset locators, compare the local current TEMP31 candidate against:

- codex/ch5-temp31-ha-net-wage-no-tau-bootstrap19-20261029-r1 @ 10ee7973713c547faa581388aa97fbfd898809de
- codex/ch5-temp31-hjb-convergence-delta-ladder-20261029-r1 @ 56447829ce0e6c3c85552c53c351b26a2452a4bd
- codex/ch5-temp31-r3-e03-e04-readonly-mechanism-r4-20261030 @ 5e1933e4c166fa40b95c82bed377538d843c7576
- codex/ch5-temp31-r5-fixed-ref-source-recovery-r1-20261030 @ cd6ef027dc0c7242e4f62ae648ca83641fc6f1c6

Do not inspect or revive MATLAB R6/R12 work. Preserve all existing R12 privacy and STOP boundaries.

## 3. Local starting locators

Use only these already-known local locator documents as the starting point:

- D:/Zotero-Analytical-Workflow/docs/project_sources/dissertation_ch5_python_mainline_20261031/LOCAL_SYNC_AUDIT_20261031.md
- D:/Zotero-Analytical-Workflow/docs/project_sources/dissertation_ch5_python_mainline_20261031/LOCAL_ASSET_LOCATORS.md

The outer D:/Zotero-Analytical-Workflow repository is a Zotero Skills repository, not the model repository. TEMP31 was previously identified as a snapshot rather than an ordinary Git working tree. Do not treat the outer repository as the formal model worktree.

Use exact paths in the locator report to inspect the model repository, TEMP31 snapshot, September source copies and original evidence roots. Do not perform a broad recursive scan of the entire D: drive.

## 4. Codex local read-only scope

A. Record exact path, file inventory, byte size, SHA-256 and available Git identity for:
- September first-reproduction Python source state and associated validator/tests;
- September single-turn report and evidence package;
- September 10 corrected runtime input-binding source and evidence;
- latest local TEMP31 source snapshot containing the wage-tax duplicate-application correction;
- immediate predecessor and any R3/R4/R5 source candidates needed to establish exact change lineage.

B. For each source candidate, report:
- repository/worktree or snapshot identity;
- commit, parent, tree, branch/ref and path, if actually available;
- Git Blob and SHA-256, file size and last-write metadata;
- whether the source is a complete model source, isolated module, validator, test or evidence-only payload;
- whether the local copy exactly matches a GitHub object or is local-only;
- exact diff/semantic scope already documented by existing evidence; do not run code to infer behavior.

C. Inventory experiment and evidence assets by manifest/result/log/input-snapshot identity, including failed and incomplete experiments. Preserve unknown/missing evidence as UNKNOWN/MISSING; do not replace missing originals with summaries.

D. Inventory local Git refs and working-tree state without changing them:
- top-level path, HEAD and tree;
- current branch, local branches, already-present remote-tracking refs and tags;
- worktrees, staged/unstaged/untracked status;
- commits and objects referenced by the protected September and TEMP31 source paths;
- whether relevant source commits are reachable from local refs.

Do not fetch, checkout, switch, reset, clean, prune, repack, create branches/tags, update refs or modify the index.

E. Classify each located asset into exactly one preliminary category:
- PERMANENT_MILESTONE: the two Owner-protected source milestones and their essential identity/evidence;
- READ_ONLY_ARCHIVE: historical source versions, experiments, failures, logs, reports, task contracts, decisions and reviews with independent research/audit value;
- POSSIBLE_DUPLICATE__NOT_DELETE_AUTHORIZED: exact byte duplicates or regenerable caches, with both original and duplicate paths listed;
- UNKNOWN_OR_BLOCKED: uncertain provenance, missing inputs, inaccessible data or privacy-sensitive material.

No item may be classified as approved for deletion in G1.

## 5. Bounded inspection budget

- Starting locator documents: 2 exact files.
- Candidate model roots: maximum 15, only those named by locators or direct references.
- Child directories: maximum 40.
- Exact source/evidence files whose content is opened: maximum 40.
- Source/evidence files whose SHA-256 is computed: maximum 60.
- Primary Python source files hashed: maximum 30.
- Git refs: inspect already-present refs only; no network fetch.
- No recursive whole-drive scan.
- If a budget is insufficient, STOP and report the missing coverage; do not expand the budget.

## 6. Explicit prohibitions

- No MATLAB launch, execution or source work.
- No HJB, KFE, HA, GE, IRF, steady-state, calibration, parameter, grid or tolerance execution/change.
- No Python module import, model runner, compile, test, benchmark or numerical reproduction.
- Do not parse/load NPZ or MAT matrices. For non-R12 accessible files, byte size and optional SHA-256 metadata may be recorded without decoding numerical arrays.
- Do not read R12 LOCAL_ONLY source or matrices, repair/re-run its comparator, weaken privacy assertions or start R13.
- Do not modify scientific source, equations, parameters, boundaries, solver, grid or tolerances.
- Do not modify local files, move/rename/copy/delete files, modify Git state, create commits, tags, branches, bundles or worktrees.
- Do not push, create GitHub Issue/PR, merge or delete any remote ref.
- Do not inspect unrelated Zotero Skills content or broadly scan the whole D: drive.

## 7. Required report and STOP

Return one structured report to Owner (chat output is sufficient; do not create or modify files):

1. Two protected milestone identities, exact paths and identity evidence.
2. TEMP31 wage-tax correction source identity, exact local path, predecessor, diff lineage and whether it is production-wired or isolated.
3. September 9/10 source and evidence identity; distinguish source commits from result/receipt commits.
4. Local repository/worktree/snapshot map and Git state.
5. Experiment/evidence inventory, including failed or incomplete records and missing originals.
6. Four-category preliminary preservation matrix.
7. Duplicate candidates with exact hash matches, but no deletion recommendation treated as authorization.
8. UNKNOWN/MISSING/BLOCKED items and coverage limits.
9. Proposed G2 archive plan and proposed G4 cleanup candidates, clearly marked NOT EXECUTED / OWNER DECISION REQUIRED.

After report delivery, STOP. Do not continue to G2, G3, G4 or any scientific task without a new explicit Owner authorization.
