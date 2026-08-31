# CH5_TWO_ASSET_HANK_MP4B_ZERO_SCIENCE_COPY_BINDING_PATH_NORMALIZATION_REMEDIATION_AND_REAUTHORIZATION_READINESS

Date: 2026-08-31

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / zero-science copy-binding remediation auditor

Owner: final scientific authority

## 1. Purpose

The immediately preceding instrumented MATLAB corrected-calendar-2009 task was scientifically unconsumed because the single MATLAB launcher process stopped at the copied-source binding guard before `load_GDPdata` and before `mpHANK_equilibrium_2000`.

Accepted predecessor terminal:

`MP4B_INSTRUMENTED_MATLAB_CORRECTED_CALENDAR2009_SINGLE_RERUN_AND_CHRONOLOGICAL_PARITY_TRACE_BLOCKED`

Accepted predecessor execution commit:

`70492a69309a1af9caa07ae9f154858bf53033d3`

Accepted predecessor task authority:

`69444469b67897d46e3450e126cb2ec5e3cb7ffa`

Exact pre-model failure:

`MP4B:CopyBinding — required helper did not resolve from source_copy`

The predecessor report establishes that the guard compared `fileparts(which(helper))` and supplied `source_copy` using raw `strcmpi`, while the command supplied a forward-slash path. No stationary/HJB/KFE/household/firm/controller science was consumed.

This task is a **zero-science remediation and authorization-readiness gate only**. It does not authorize another MATLAB run.

## 2. Scientific budget

Hard budget for this task:

- MATLAB processes: `0`;
- MATLAB stationary calls: `0`;
- MATLAB HJB/KFE/household/firm/controller calls: `0`;
- Python stationary/HJB/KFE/household/MP2/MP3 calls: `0`;
- comparator replay: `0`;
- any other year/batch/shock/AR1/transition/dynamics/IRF/R5/Results call: `0`.

No scientific execution of any kind is authorized.

Permitted tools are static/read-only filesystem inspection, hashing, text comparison, PowerShell/Python string/path-representation checks that do not call model code, and creation of a fresh external remediation package under `D:\ProjectTemp`.

## 3. Live continuity

At task start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as direct child of `70492a69309a1af9caa07ae9f154858bf53033d3`;
3. require clean worktree, `HEAD == origin/main`, ahead/behind `0/0`;
4. read:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
   - `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`;
   - `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`;
   - `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`;
   - predecessor task `tasks/CH5_TWO_ASSET_HANK_MP4B_INSTRUMENTED_MATLAB_CORRECTED_CALENDAR2009_SINGLE_RERUN_AND_CHRONOLOGICAL_PARITY_TRACE.md`;
   - predecessor report `docs/CH5_TWO_ASSET_HANK_MP4B_INSTRUMENTED_MATLAB_CORRECTED_CALENDAR2009_SINGLE_RERUN_AND_CHRONOLOGICAL_PARITY_TRACE_REPORT.md`.

Any continuity or authority failure => stop with no local mutation beyond bounded notes and classify BLOCKED.

## 4. Immutable predecessor evidence

Treat the predecessor diagnostic root as read-only evidence:

`D:\ProjectTemp\ch5-mp4b-instrumented-matlab-calendar2009-20260831-001`

Do not edit, delete, rename, overwrite, or rerun anything inside it.

Require the predecessor artifact hashes recorded in the accepted report:

- `source_copy_manifest.json` = `1F40F2E207BEE74DCE49B5887CB581B39CA9CCA7C6EF7C8E18E13A685673FB59`
- `instrumentation_manifest.json` = `2E61A340D3908BE473FB72AAFC4D0076420974B202136E71FDE07FDA1A97684A`
- `instrumentation_manifest_revision_001.json` = `903EEFE050D65F9736820E3C0FFAC4E6496A0BFDF94726B14012158A0B38B5D9`
- `instrumentation_patch.diff` = `8320F93726ADE831DE4B530551E66A153B7795E3AA7C36315C758D1F2025FDFA`
- `instrumented_run_manifest.json` = `FF3417CA9D664807A424ED7D9A4EEAC279F2DCE506D301BD2EA1CF5052E0E50E`
- `pre_science_gate.json` = `59E56A2C34C6BDE0FB06394322B964709A4477A4C4BC54E5304AA31CEAD16701`
- `instrumented_terminal_status.json` = `AA88E352DF60D8366D40510544DC957B0E1B66DE4405880D0EAA5777B734C9A3`.

Also reverify, read-only, the protected original MATLAB identities and corrected-calendar-2009 canonical/baseline artifacts named in the predecessor task/report. Original MATLAB source remains strictly read-only.

## 5. Exact blocker reconstruction — static only

Without launching MATLAB, locate the exact failed wrapper/launcher text under the predecessor diagnostic root using only bounded direct-child/manifest-backed paths. Do not broad-search D:.

Extract and persist into the new remediation package:

- exact `source_copy` string supplied to the failed launcher/guard;
- exact helper list tested by the guard;
- exact guard expression and surrounding lines;
- exact static path form expected by each helper resolution from copied-tree membership evidence;
- whether the only observed representational difference is `/` versus `\`, trailing separator, case, or another syntactic path representation;
- whether any helper is actually absent from the copied source tree;
- whether duplicate helper names exist inside the exact copied tree;
- whether any helper resolves conceptually outside the copied tree based on static copied-tree membership and source manifests.

Do not claim the runtime value of `which(helper)` if it was not persisted. Clearly distinguish persisted runtime evidence from static reconstruction.

The objective is to classify the blocker as one of:

1. `PATH_REPRESENTATION_ONLY`;
2. `HELPER_ABSENT_FROM_COPY`;
3. `DUPLICATE_HELPER_OR_AMBIGUOUS_MEMBERSHIP`;
4. `WRAPPER_BINDING_LOGIC_DEFECT_OTHER`;
5. `INSUFFICIENT_EVIDENCE`.

## 6. Required normalization contract

If and only if the blocker is supported as `PATH_REPRESENTATION_ONLY`, design a deterministic MATLAB-side guard normalization contract for a future wrapper.

The normalization must be representation-only and must not change MATLAB search order or scientific code. It must:

- operate on strings only;
- convert `/` to `filesep` on Windows-equivalent path strings;
- remove only redundant trailing separators while preserving a drive root such as `D:\`;
- compare case-insensitively after separator normalization;
- reject relative paths;
- reject paths outside the exact fresh diagnostic `source_copy` root;
- retain the finite exact-root + exact-parent-membership discipline;
- not use Java canonical paths;
- not use broad `startsWith`, substring containment, or broad-D trust as the membership proof;
- not resolve or trust the protected logical/physical source root in place of the copied-tree root;
- not add any scientific/model call.

Preferred future guard shape is conceptually:

- normalize the supplied copied-root representation;
- normalize `fileparts(which(helper))` representation;
- require exact normalized equality for helpers expected at copied root, or exact normalized parent equality for helpers explicitly expected in a known copied subdirectory;
- fail closed on any mismatch.

Do not silently weaken the binding guard.

## 7. Static normalization test matrix

Create a zero-science representation test matrix under a fresh remediation root, recommended:

`D:\ProjectTemp\ch5-mp4b-copy-binding-remediation-20260831-001`

If it already exists, choose a fresh deterministic suffix; do not overwrite/delete.

Using a non-MATLAB static test harness, test at minimum:

- identical backslash path;
- same path using forward slashes;
- same path with one trailing separator;
- same path with repeated trailing separators;
- case-only variation;
- sibling directory;
- parent directory;
- child subdirectory not explicitly authorized;
- same textual prefix but different directory name;
- relative path;
- different drive;
- protected original MATLAB root instead of copied root.

The intended normalized guard must accept only representations of the exact authorized copied root/authorized exact parent and reject all escape/near-prefix cases.

Persist test inputs, normalized outputs, booleans, and a test-summary SHA-256. This is a string/path representation test only; do not invoke MATLAB.

## 8. Future-wrapper candidate — no execution

If the remediation is supported, construct one **candidate future wrapper** in the fresh remediation root only.

Requirements:

- start from the exact failed wrapper text;
- change only the copy-binding guard/path normalization and any diagnostics necessary to report exact helper/path mismatch;
- all code after the guard leading to corrected-calendar-2009 data loading and `mpHANK_equilibrium_2000` invocation must remain byte-for-byte or semantically/textually identical except unavoidable line-number shifts;
- do not alter equations, parameters, data indices, year mapping, regression vintage, calibration, model function arguments, working-directory semantics, path search order, instrumentation in the copied scientific files, convergence logic, controller logic, or observer schema;
- do not execute the candidate wrapper;
- do not run `checkcode` because this task permits zero MATLAB processes;
- persist the complete diff from failed wrapper to candidate wrapper and SHA-256 of both texts.

Also freeze the exact candidate future launcher command text, but do not execute it.

## 9. Reauthorization-readiness adjudication

A future one-shot instrumented MATLAB rerun may be recommended to the Owner **only if all** of the following are established without science:

- predecessor evidence identities match;
- copied helper files required by the guard are present at the intended copied locations;
- no ambiguous duplicate/membership condition is found;
- blocker is classified `PATH_REPRESENTATION_ONLY` or another equally narrow non-scientific wrapper defect with direct static proof;
- candidate fix changes only binding/diagnostic representation logic;
- static normalization escape tests all pass;
- candidate wrapper preserves the exact corrected-calendar-2009 scientific invocation body;
- original protected source remains unchanged;
- no MATLAB or Python science/model process was launched.

If all pass, terminal:

`MP4B_ZERO_SCIENCE_COPY_BINDING_PATH_NORMALIZATION_REMEDIATION_READY_FOR_OWNER_REAUTHORIZATION`

and recommendation:

`OWNER_REAUTHORIZATION_WARRANTED_FOR_ONE_FUTURE_INSTRUMENTED_MATLAB_CORRECTED2009_ONE_SHOT`

This is **not authorization**. Do not publish or execute the future science task automatically.

If any condition fails, terminal:

`MP4B_ZERO_SCIENCE_COPY_BINDING_PATH_NORMALIZATION_REMEDIATION_BLOCKED`

and identify the single narrow next diagnostic gate. Do not recommend a MATLAB rerun.

## 10. Required report

Create:

`docs/CH5_TWO_ASSET_HANK_MP4B_ZERO_SCIENCE_COPY_BINDING_PATH_NORMALIZATION_REMEDIATION_AND_REAUTHORIZATION_READINESS_REPORT.md`

The report must include:

- live authority and continuity;
- predecessor task/report/commit identities;
- predecessor artifact hash verification;
- protected-source and canonical-2009 identity verification;
- exact failed guard text and exact supplied `source_copy` representation;
- helper-list and copied-tree membership table;
- runtime-known vs statically reconstructed evidence distinction;
- blocker classification;
- normalization contract;
- complete static test matrix and result;
- failed-wrapper SHA, candidate-wrapper SHA, complete diff SHA;
- proof that scientific invocation body is unchanged;
- exact frozen future launcher text;
- scientific/model call ledger proving all zero;
- explicit reauthorization-readiness decision;
- forbidden-operation audit;
- Git closeout.

External remediation files stay under `D:\ProjectTemp` and must not be committed.

## 11. Repository mutation scope and closeout

Allowed repository change is only the required report, plus at most one bounded CURRENT roadmap/status line if strictly necessary. Do not modify code, tests, validators, scientific modules, project rules, calibration, contracts, task predecessor, or protected artifacts.

Closeout requirements:

- `git diff --check`;
- explicit-path staging;
- exactly one execution commit;
- non-force push;
- fresh GitHub read-back;
- report changed paths and blob SHA;
- `HEAD == origin/main`;
- ahead/behind `0/0`;
- clean worktree.

Do not start any future MATLAB task. Stop after the reauthorization-readiness verdict.