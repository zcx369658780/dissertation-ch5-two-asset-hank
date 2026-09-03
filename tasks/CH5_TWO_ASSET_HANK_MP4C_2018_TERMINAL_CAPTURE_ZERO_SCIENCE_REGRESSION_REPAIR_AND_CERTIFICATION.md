# CH5_TWO_ASSET_HANK_MP4C_2018_TERMINAL_CAPTURE_ZERO_SCIENCE_REGRESSION_REPAIR_AND_CERTIFICATION

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / zero-science regression repairer / certification executor

Owner: final scientific authority

## 1. Authority basis

Immediate live predecessor authority:

`97f0ac6ff8d4fc5380602c115a5e609f4f632bf5`

The prior attempt stopped during mandatory zero-science preflight. No execution commit was published because a further local source review found that the newly added observability work had introduced a local diagnostic regression: inside `pre_frozen_household_output_batch`, `outputs.append(...)` had been moved outside the `for state, result in completed` loop, leaving only the last province row.

The live GitHub baseline at `97f0ac6f...` remains clean and contains the certified production-path-parity implementation in which `outputs.append(...)` is correctly inside the loop. The regression exists only in the uncommitted local observability worktree from the aborted terminal-capture task.

Accepted zero-science facts from the aborted attempt:

- `py_compile` passed;
- focused pytest reported `1 failed, 6 passed, 1 warning`;
- frozen 2018 input reads = 0;
- scientific PID = 0;
- stationary / household / production HJB / production KFE / MATLAB / R-PLM / shock / IRF calls = 0;
- no retry and no scientific execution occurred.

This task authorizes only bounded repair and certification of the local observability regression. It does **not** authorize any 2018 scientific execution.

## 2. Local-dirty-worktree continuity

The Builder is expected to begin from a local worktree based on `97f0ac6ff8d4fc5380602c115a5e609f4f632bf5` with uncommitted changes from the aborted task.

At start:

1. `git fetch origin`;
2. verify live `origin/main` is this task and is a direct child of `97f0ac6ff8d4fc5380602c115a5e609f4f632bf5`;
3. before changing anything, record local `HEAD`, `git status --short`, and full diffs of the authorized dirty paths into an external no-overwrite evidence root;
4. expected dirty paths are limited to:
   - `validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`;
   - `tests/test_mp4c_2018_first_singularity_diagnostic.py`;
   - `docs/CH5_TWO_ASSET_HANK_MP4C_2018_PRODUCTION_PATH_FAITHFUL_DURABLE_REEXECUTION_AND_TERMINAL_CAPTURE_REPORT.md`;
5. if any other tracked/untracked research path is dirty: STOP;
6. verify the new live task commit changes only this task file relative to `97f0ac6f...`;
7. fast-forward the local branch to live `origin/main` only if Git can preserve the authorized local modifications without overwrite/conflict. If not, STOP. Do not stash/reset/discard the local evidence silently.

After the safe fast-forward, the local tracked/untracked worktree may remain dirty only on the three authorized paths above.

## 3. Source-of-truth baseline for the repaired helper

The certified production-path-parity baseline is commit:

`c225f3ce3eff4a95236f7b7f9f0f6c814119c222`

Diagnostic Git blob at that baseline:

`96f93a42c3ffdd85991c3331df5d934a6890918a`

For `pre_frozen_household_output_batch`, the required baseline structure is:

- initialize `outputs=[]`;
- iterate over every `(state, result)` in `completed`;
- inside that loop, compute `aggregate=result.aggregates`;
- inside that same loop, append one output tuple;
- after the loop, construct one `PreFrozenHouseholdOutputBatch` from all accumulated rows.

The repair must restore this N-input → N-output semantics exactly while retaining the new terminal-result observability additions from the aborted task where they are otherwise correct.

## 4. Allowed edits

Only these paths may be edited:

- `validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`;
- `tests/test_mp4c_2018_first_singularity_diagnostic.py`;
- `docs/CH5_TWO_ASSET_HANK_MP4C_2018_PRODUCTION_PATH_FAITHFUL_DURABLE_REEXECUTION_AND_TERMINAL_CAPTURE_REPORT.md`.

No production/model file may be modified.

The report must be corrected so it no longer states or implies that the failure was merely a one-row synthetic fixture problem. It must accurately state that the local observability edit regressed `pre_frozen_household_output_batch` by moving `outputs.append(...)` outside the loop, causing an N→1 batch materialization defect. It must also preserve the zero-science facts: no frozen 2018 input and no scientific/model calls occurred.

## 5. Mandatory regression repair

Repair the local diagnostic so that:

1. `pre_frozen_household_output_batch(grid, completed, iteration)` returns exactly one materialized row per `completed` item;
2. ordering is preserved exactly;
3. every row uses its own `state` and `result`;
4. production-literal `AtTax` remains computed independently for each row;
5. convergence/iteration/statistic diagnostics remain per-row;
6. the previously certified production-path `phi[:]` recomputation remains unchanged;
7. durable pre-call/HJB ledgers remain unchanged;
8. raw singularity capture-before-postmortem remains unchanged;
9. no scientific/model call is added.

## 6. Mandatory zero-science tests

The focused tests must explicitly prevent recurrence of the N→1 regression.

At minimum verify:

- a two-province synthetic `completed` sequence yields batch length 2 for every vector field;
- a three-province synthetic `completed` sequence yields batch length 3 for every vector field;
- row order and province-specific aggregate values are preserved;
- province-specific nonzero `AtTax` values match the production literal expression independently;
- no value from the last province is duplicated across earlier rows;
- the terminal-result persistence helper can be tested with a valid >=2-province synthetic object and does not mutate batch semantics;
- prior production-path parity tests for `phi`, `AtTax`, complete batch fields and pure one-turn sensitivity remain passing;
- prior instrumentation tests for durable HJB ledger, raw capture-first persistence, and separate read-only postmortem remain passing.

Run at minimum:

`python -m py_compile validators/multi_province/mp4c_2018_first_singularity_diagnostic.py tests/test_mp4c_2018_first_singularity_diagnostic.py`

`python -m pytest -q tests/test_mp4c_2018_first_singularity_diagnostic.py`

Expected, if no tests are added/removed beyond the current aborted work, is `7 passed, 1 warning`; a different pass count is acceptable only if explained and all required assertions above are present. The only expected warning is the intentional dummy `MatrixRankWarning`.

## 7. Hard zero-science boundary

Forbidden in this task:

- reading the frozen 2018 input;
- creating any scientific PID;
- running stationary;
- running production household/HJB/KFE;
- MATLAB;
- R/PLM;
- shock/IRF;
- numerical experiment reruns.

Scientific/model call counters must remain exactly zero.

## 8. Evidence

Use a fresh no-overwrite root, preferred:

`D:\ProjectTemp\ch5-mp4c-2018-terminal-capture-zero-science-regression-repair-20260903-001`

Persist at minimum:

- pre-repair local status and diff snapshot;
- live authority identity;
- repaired helper diff;
- N→N regression-test receipts for 2 and 3 provinces;
- terminal-persistence zero-science receipt;
- compiler stdout/stderr;
- pytest stdout/stderr;
- zero-science execution ledger;
- report consistency receipt;
- SHA-256 audit manifest.

## 9. Publication authority

If and only if all mandatory zero-science checks PASS, this task explicitly authorizes one normal execution commit and push to `origin/main` containing exactly:

- `validators/multi_province/mp4c_2018_first_singularity_diagnostic.py`;
- `tests/test_mp4c_2018_first_singularity_diagnostic.py`;
- corrected `docs/CH5_TWO_ASSET_HANK_MP4C_2018_PRODUCTION_PATH_FAITHFUL_DURABLE_REEXECUTION_AND_TERMINAL_CAPTURE_REPORT.md`.

Suggested commit message:

`Repair MP4C 2018 terminal-capture zero-science regression`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean;
- report the final live SHA and exact changed paths.

If certification FAILS, do not publish inconsistent source. Preserve evidence, update the report locally to the strongest accurate fail-closed classification, and STOP for new authority.

## 10. Terminal markers

PASS:

`MP4C_2018_TERMINAL_CAPTURE_ZERO_SCIENCE_REGRESSION_REPAIRED_AND_CERTIFIED__N_TO_N_BATCH_SEMANTICS_RESTORED__READY_FOR_FINAL_DURABLE_2018_EXECUTION_TASK`

FAIL:

`MP4C_2018_TERMINAL_CAPTURE_ZERO_SCIENCE_REGRESSION_REPAIR_FAILED__NO_2018_EXECUTION`

## 11. Required report

Update the existing aborted-task report in place:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_PRODUCTION_PATH_FAITHFUL_DURABLE_REEXECUTION_AND_TERMINAL_CAPTURE_REPORT.md`

The updated report must distinguish:

- aborted preflight evidence from the prior task;
- the newly identified local N→1 source regression;
- the bounded zero-science repair/certification performed under this task;
- explicit statement that no 2018 scientific execution was authorized or performed by this repair task.
