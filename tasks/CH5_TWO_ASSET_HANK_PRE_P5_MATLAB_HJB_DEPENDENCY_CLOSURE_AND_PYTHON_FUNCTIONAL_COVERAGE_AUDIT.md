# CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HJB_DEPENDENCY_CLOSURE_AND_PYTHON_FUNCTIONAL_COVERAGE_AUDIT

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / source auditor

Owner: final scientific authority

## 1. Task purpose

Before the already-published P5 acceptance-design review is executed, close the complete MATLAB household-HJB dependency graph and compare every scientifically active MATLAB helper/behavior against the accepted Python reconstruction.

This is a **read-only source/dependency/functional-coverage audit**.

It must answer whether the Python rewrite omitted any scientifically material function or behavior used by the designated MATLAB household solver, including inherited three-asset code paths that may or may not be active in the two-asset configuration.

Do not implement missing functionality in this task.
Do not run MATLAB or Python scientific models.
Do not alter P1-P4/R4 evidence.
P5 remains blocked.

## 2. Supersession / task order

The previously published task

`tasks/CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW.md`

is **DEFERRED_PENDING_THIS_DEPENDENCY_AUDIT**.

Do not execute that P5 review until this dependency audit has been completed, published, and independently accepted.

## 3. Live authority and source continuity

Task-authoring parent observed by reviewer:

`1b94e01f51c2da66dc1d855431dd129fae22b31c`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. record live start SHA;
4. read `AGENTS.md` and both required project rules;
5. verify accepted Python `src/tests` continuity from baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Required check:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

must be empty.

## 4. Designated MATLAB source root

Audit the actual local source tree read-only:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Re-verify the already accepted identities:

- `HANK_2ASSETS_HJB.m`
  - `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m`
  - `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `lab_solve2.m`
  - `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

The Owner-provided copies of these four files independently match these accepted identities, but the designated local root remains the source-tree authority for the dependency closure.

## 5. Required GitHub evidence reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_FULL_HJB_STRUCTURAL_DECOMPOSITION_AND_STATIONARY_OPERATOR_DIAGNOSTIC_REPORT.md`
- accepted Python source under `src/ch5_two_asset_hank/`, especially `economics.py`, `policies.py`, `boundaries.py`, `hjb.py`, `generator.py`, `kfe.py`, `steady_state.py`, `productivity.py`, `contracts.py`, plus relevant tests.

## 6. Phase A — complete MATLAB direct and transitive dependency closure

Starting from `HANK_2ASSETS_HJB.m`, statically enumerate every function call and classify each as:

- MATLAB built-in / toolbox;
- same-project custom function;
- external/path-resolved custom function;
- array/indexing expression misidentified by naive parsing.

For every custom function:

1. identify exact resolved file path under the designated tree if present;
2. record bytes, lines, SHA-256, function signature;
3. find duplicate same-name files anywhere under the designated tree and classify path ambiguity;
4. inspect that helper recursively and continue until the transitive custom dependency graph is closed;
5. classify whether it can affect:
   - initialization;
   - HJB policy equations;
   - HJB convergence;
   - generator construction;
   - stationary KFE/distribution;
   - aggregates;
   - post-processing only;
   - display only.

At minimum the direct graph must explicitly address:

- `lab_solve2`
- `HANK3_FOC`
- `HANK3_cost`
- `HANK_gini`

The current reviewer inspection found `HANK_gini` called five times near the end of `HANK_2ASSETS_HJB.m`; it was not among the four previously protected helper identities. Determine its exact source, all transitive dependencies, and whether its absence from Python is material to the HA scientific core or only to inequality-statistic post-processing.

If any required custom dependency source cannot be located, return a missing-source blocker rather than guessing.

## 7. Phase B — MATLAB-to-Python functional coverage matrix

Do **not** compare by function name alone. Compare by scientific object/behavior.

For every MATLAB dependency or scientifically active inline block, map it to one of:

- `EXACT_PYTHON_EQUIVALENT`
- `FUNCTIONALLY_INLINED_IN_PYTHON`
- `AUTHORIZED_REDESIGN_ALREADY_ACCEPTED`
- `MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT`
- `POSTPROCESSING_NOT_REQUIRED_FOR_HA_CORE`
- `UNUSED_OR_INACTIVE_THREE_ASSET_RESIDUE`
- `MATERIAL_PYTHON_OMISSION_CANDIDATE`
- `UNRESOLVED_EQUATION_AUTHORITY_REQUIRED`

For each row give:

- MATLAB source/file/line or block;
- exact mathematical behavior;
- whether active under the actual two-asset domestic calls;
- Python file/function or explicit absence;
- existing authority/report that already adjudicates the difference, if any;
- materiality to HJB/KFE/steady-state correctness;
- final classification.

## 8. Mandatory high-risk checks

### 8.1 `lab_solve2` and initialization

The MATLAB HJB calls `fzero(@lab_solve2,...)` over every state to construct `l0`, then constructs `c0` and `v02` before the HJB iteration.

Audit:

- exact equation solved by `lab_solve2`;
- whether it is only an initialization device or also defines an equilibrium condition later used by the HJB;
- Python's initialization construction(s);
- whether the lack of a literal `lab_solve2` port is scientifically harmless, already accepted as initialization redesign, or a material omission.

Do not require literal initialization equality if existing authority already rejects that requirement; document the authority.

### 8.2 `HANK3_FOC` / `HANK3_cost`

Reconfirm domestic `foreign=0` call coverage and whether any foreign/third-asset branches can become active in this two-asset HJB.

Explicitly classify:

- `fixcost`, `fixcost2`, price-conversion logic;
- whether those branches are dead/inactive for the two-asset model;
- O1 low-`a` accepted redesign.

### 8.3 `HANK_gini`

Trace it fully.

Determine whether it:

- only consumes the already-solved distribution/policies and returns inequality statistics;
- mutates any scientific state or feeds back into `results.convergent`, policies, generator, KFE, or subsequent household equations;
- is required for the current HA parity/P5 correctness scope;
- should instead be listed as a future Results/post-processing implementation gap.

Do not implement it in this task.

### 8.4 Three-asset inheritance residue

Audit all variables/branches that appear inherited from a three-asset implementation, including at minimum:

- `alphap`;
- `VafF`, `VafB`, `Raf`;
- foreign branches in `HANK3_FOC` / `HANK3_cost`;
- any fixed-cost/price fields used only by those branches.

For each, prove whether it is active or dead in the two-asset execution path.

Do not port dead code merely for line-by-line similarity.

### 8.5 State-dependent illiquid return schedule — mandatory equation-authority audit

This is a critical check discovered by reviewer inspection of the Owner-provided main source and must not be skipped.

The MATLAB main defines:

`raah = rah .* (1 - 0.1*(ahmax./ah).^(-9))`

then places this into `Rah`, and later uses `Rah.*aaah` in the illiquid drift/generator and `AhTax` calculation.

Accepted Python production currently uses:

`mu_a = r_a * a + d`

with scalar `r_a`.

Audit separately from the already accepted O12 line-90 initialization issue:

1. prove every scientifically active use of `raah`/`Rah` in MATLAB;
2. distinguish the odd initialization expression `Rah.*raah` from the later drift term `Rah.*aaah`;
3. quantify analytically how the effective return varies over the MATLAB `a` grid, including lower and upper bounds;
4. search the dissertation/equation-authority reports for an explicit adjudication of **state-dependent illiquid return versus constant `r_a`**;
5. determine whether existing O7/O12 decisions actually cover this issue or whether they only cover drift signs and initialization;
6. if no explicit authority exists, classify this as `UNRESOLVED_EQUATION_AUTHORITY_REQUIRED` / `MATERIAL_PYTHON_OMISSION_CANDIDATE` and block the P5 review.

Do not silently assume this MATLAB schedule is authoritative, and do not silently assume it is legacy residue. Owner/reviewer equation authority must decide if it was never previously adjudicated.

### 8.6 Output/statistics coverage

Inventory all post-solve outputs written to `results`, including but not limited to:

- `g`, `C`, `l`;
- `Lt`, `Bt`, `At`, `Ct`;
- borrowing statistics;
- adjustment-cost statistics;
- MPC/utility/marginal utility where exposed;
- Gini statistics.

Classify which are required for HA scientific correctness/P5 and which belong to later Results/reporting scope.

## 9. Phase C — contradiction audit against accepted O1-O12 / P1-P4

The audit must explicitly answer whether the newly closed dependency graph reveals any issue that was absent from, or incorrectly assumed away by, the accepted structural review.

Pay particular attention to the existing accepted statements that:

- O7 budget/drift signs are aligned;
- O12 covers legacy initialization behavior;
- P1/P2 primitives/local policies are complete;
- P3/P4 common operator/KFE evidence is complete.

For every newly discovered behavior, state whether it:

- is already tested by P1-P4;
- is outside P1-P4 but harmless/post-processing;
- is an accepted redesign/non-comparability;
- or is a new scientifically material gap requiring Owner decision.

Do not revoke accepted evidence unless there is a direct contradiction. If there is a direct contradiction, identify the smallest affected acceptance claim precisely.

## 10. No execution / no implementation

Scientific run budget:

- MATLAB HJB/KFE/model calls: `0`
- Python HJB/KFE/steady-state calls: `0`
- P1-P4 reruns: `0`

No source mutation is authorized.

Filesystem reads, hashes, grep/static parsing, Git reads, and non-scientific syntax/dependency inspection are allowed.

## 11. Terminal classifications

Return exactly one:

### A. No material omission

`MATLAB_HJB_DEPENDENCY_CLOSURE_COMPLETE_NO_MATERIAL_PYTHON_OMISSION__P5_REVIEW_MAY_RESUME`

Use only if every scientifically active MATLAB dependency/behavior is either represented in Python, functionally inlined, already accepted as redesign/legacy limitation, or proven irrelevant to HA core correctness.

### B. Material omission / unresolved authority

`MATLAB_HJB_DEPENDENCY_AUDIT_FINDS_MATERIAL_PYTHON_OMISSION_OR_AUTHORITY_GAP__P5_BLOCKED`

Use if any scientifically active MATLAB behavior lacks a Python counterpart **and** has not already been explicitly adjudicated as a redesign/legacy limitation.

Name the smallest exact gap. Do not implement it.

### C. Missing dependency source

`MATLAB_HJB_DEPENDENCY_CLOSURE_BLOCKED_MISSING_SOURCE__P5_BLOCKED`

Use if a custom dependency required to classify scientific behavior cannot be located/read.

## 12. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HJB_DEPENDENCY_CLOSURE_AND_PYTHON_FUNCTIONAL_COVERAGE_AUDIT_REPORT.md`

The report must contain:

1. terminal classification;
2. live start/final GitHub identity;
3. Python source continuity;
4. complete direct/transitive MATLAB custom dependency graph;
5. exact path/hash/signature table for every custom dependency;
6. duplicate/path-ambiguity audit;
7. complete MATLAB-to-Python functional coverage matrix;
8. `lab_solve2` initialization finding;
9. `HANK3_FOC` / `HANK3_cost` domestic-vs-foreign/three-asset finding;
10. `HANK_gini` finding and transitive closure;
11. three-asset residue table;
12. state-dependent `raah/Rah` equation-authority finding;
13. output/statistics coverage table;
14. contradiction audit against O1-O12 and P1-P4;
15. exact material gaps, if any;
16. forbidden-operation check;
17. acceptance level;
18. exact recommended next gate.

If classification A: recommend resuming the deferred P5 acceptance-design review.

If classification B: recommend the smallest Owner/reviewer equation-authority decision gate; do not recommend implementation until that decision is made.

If classification C: recommend only recovery/upload of the exact missing dependency source.

## 13. Explicit prohibitions

Do not:

- execute the deferred P5 review in the same task;
- run MATLAB models;
- run Python models;
- modify Python `src/tests`;
- modify any MATLAB file;
- copy MATLAB code into Python;
- implement Gini/statistics;
- implement any suspected missing function;
- add an adapter;
- change accepted equations;
- widen tolerances;
- resume parameter tuning;
- enter AR(1), transition, IRF, calibration extension, dynamics or Results;
- issue P5 acceptance.

The purpose is to establish **dependency completeness and scientific functional coverage before P5**, not to maximize line-by-line similarity.