# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / source auditor

Owner: final scientific authority

## 1. Purpose

Freeze the **smallest source-backed MATLAB-faithful general-equilibrium steady-state closure contract** after household HJB, stationary KFE, stationary distribution, and household aggregate parity have all been accepted.

This task is deliberately **audit/contract-only**. It must identify exactly how the designated MATLAB code closes the general-equilibrium steady state around the accepted household block, but it must **not run** the GE solver, HJB, KFE, aggregate evaluators, dynamics, or Results.

The output of this task is the authority needed for the next bounded GE residual-map parity task. It is not itself a GE steady-state acceptance.

## 2. Controlling accepted authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`

Accepted authorities:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`
- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_KFE_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HOUSEHOLD_AGGREGATE_PARITY_ACCEPTED`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Important scope boundary:

The accepted household aggregate values are frozen-price stationary household objects. They do **not** yet imply GE steady-state acceptance.

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`8cd3dc4eb6d0e3e6d5f5c8cb63036c1fd6042961`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` as a direct child of the accepted aggregate closeout commit;
3. verify clean worktree;
4. verify all controlling reports and accepted faithful HJB/KFE source paths exist;
5. record live start SHA;
6. do not begin from uncommitted scientific source changes.

## 4. Protected MATLAB source root and source identity

Designated protected root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Known required household source hash:

- `HANK_2ASSETS_HJB.m` — `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

First locate **every MATLAB file in the designated root that calls, wraps, parameterizes, iterates around, or consumes results from `HANK_2ASSETS_HJB`**.

For every GE-relevant file found:

- record full path relative to designated root;
- compute SHA-256;
- record function/script signature;
- record exact callers/callees;
- record relevant line ranges.

Do not modify protected MATLAB files.

If the GE driver/caller cannot be located from this root, stop BLOCKED and report the exact missing provenance needed.

## 5. Mandatory call-graph audit

Construct the exact steady-state call graph from the outermost GE driver down through the household solver and back to the residual/root solver.

At minimum identify:

1. outer steady-state script/function;
2. root finder / optimizer / manual iteration routine, if any;
3. unknown vector supplied to the closure;
4. any transforms from root variables into economic variables;
5. all inputs passed into `HANK_2ASSETS_HJB`;
6. all household outputs consumed by the outer closure;
7. firm block / production block;
8. government/tax/transfer block;
9. asset-market / bond-market conditions;
10. labor-market condition;
11. goods/resource condition, if present;
12. any normalization or numeraire;
13. convergence / acceptance rule;
14. final result fields persisted by the source.

Do not infer a standard HANK closure. Record only what the designated source actually implements.

## 6. Mandatory GE unknown/equation freeze

Produce one exact table with one row per GE unknown and one row per GE residual/equilibrium equation.

For each unknown record:

- MATLAB variable name;
- economic interpretation;
- whether primitive, transformed, or derived;
- source line where defined/transformed;
- initial guess;
- lower/upper bound if any;
- whether solved jointly or sequentially;
- units/scaling;
- whether it is passed directly into the household block.

For each residual/equation record:

- exact MATLAB expression;
- economic interpretation;
- source line range;
- household aggregate inputs used (`Ct`, `Lt`, `At`, `Bt`, etc.);
- firm/government variables used;
- sign convention;
- scaling/normalization;
- target value, normally zero unless source says otherwise;
- whether used by the root solver or diagnostic-only.

The report must explicitly answer, from source:

- Is `rb` exogenous or endogenous in steady state?
- Is `rah`/illiquid return endogenous? If so, what market/equation closes it?
- Is `w` endogenous? If so, exact wage condition.
- Is `Tt` fixed, exogenous, or budget-balanced/endogenous?
- Is `tau` fixed or endogenous?
- Is `rb_gap` fixed or endogenous?
- What asset concept enters the production/capital-market condition: `At`, `Bt`, `At+Bt`, or another source field?
- Is liquid asset supply zero, fixed, government debt, or another source-backed object?
- Is `Lt` the exact labor object used by the firm block, or is there another transformation?
- Is `Ct` used in a resource condition or only reported?
- Is there a government budget/resource condition?
- Are there any taxes on asset income (`AhTax` or related fields) entering closure?

If any of these cannot be resolved unambiguously from designated source, classify the unresolved item `OWNER_PROVENANCE_REQUIRED` rather than guessing.

## 7. Production/firms/government source map

Audit all GE-relevant equations outside the household block, including any source formulas for:

- production function;
- capital demand / return to illiquid asset;
- wage;
- depreciation;
- TFP/productivity normalization;
- government spending/transfers;
- taxes;
- bond/debt supply;
- profits/dividends;
- resource constraint;
- any fixed supply or normalization.

For every formula, record exact MATLAB variable names and line ranges.

If the MATLAB source uses precomputed constants or loads calibration/results from MAT files, record:

- file name;
- variable names loaded;
- whether the object is required for GE closure;
- whether its provenance/hash is available.

Do not open unrelated large/binary files unless required by the closure. Do not infer values from old outputs if the source loads them from an unavailable artifact; stop with provenance requirement instead.

## 8. Root-solver / numerical closure audit

Identify the exact numerical GE method:

- `fsolve`, `fzero`, `lsqnonlin`, manual bisection, fixed point, nested loop, interpolation, or other;
- dimensionality of solve;
- initial guess;
- solver options;
- tolerances;
- iteration limits;
- scaling;
- bounds/transforms;
- warm starts / continuation;
- whether HJB/KFE results are reused between root evaluations;
- failure handling;
- source criterion for declaring steady-state convergence.

If multiple steady-state routes exist, identify which one produces the Chapter 5 / two-asset baseline used by the designated model. Do not choose between routes by convenience.

## 9. Parameter/grid/calibration freeze for GE

Record the exact GE baseline parameter source and values required by the outer closure, including at minimum those that are not already household-local.

Explicitly determine whether the eventual GE parity should use:

- the small accepted `5 x 5 x 2` household parity fixture;
- the designated MATLAB production grid/calibration;
- or another source-defined GE fixture.

This task must **not decide by convenience**. The designated MATLAB source decides.

If the GE source requires the production grid/calibration, identify its exact dimensions, bounds, and parameter values, but do not execute it here.

## 10. Dissertation cross-check — evidence only

Cross-check the frozen MATLAB closure against the dissertation equations/Chapter 5 description available in project sources.

Classify each important relation as:

- `MATLAB_AND_DISSERTATION_ALIGNED`;
- `MATLAB_NUMERICAL_CLOSURE_MORE_SPECIFIC`;
- `MATLAB_DISSERTATION_CONFLICT_OWNER_DECISION_REQUIRED`.

The dissertation supplies economic interpretation. The designated working MATLAB implementation remains the primary numerical reconstruction authority.

Do not silently rewrite MATLAB closure to match textbook/general-knowledge equilibrium equations.

## 11. Next-gate residual-map contract design

If and only if the GE closure is fully source-resolved, design the **next** bounded task contract, but do not execute it.

The next task should be the smallest same-input GE residual-map parity test before any root solve.

Freeze recommendations for:

- exact unknown vector/order;
- exact residual vector/order;
- source-defined baseline/initial-guess point;
- at least one bounded source-valid perturbation point if needed to exercise sign/direction without solving;
- MATLAB/Python ordering;
- direct arithmetic acceptance rules;
- HJB/KFE call budget per trial point;
- whether household warm-start state must be identical across languages;
- which outputs must be persisted for root-cause localization.

Do not authorize the full GE root solve in this task.

## 12. Scientific execution budget

Exactly zero model/scientific solves:

- MATLAB HJB: `0`;
- Python HJB: `0`;
- MATLAB KFE: `0`;
- Python KFE: `0`;
- MATLAB aggregate evaluator: `0`;
- Python aggregate evaluator: `0`;
- MATLAB GE residual evaluations: `0`;
- Python GE residual evaluations: `0`;
- GE root solve: `0`.

Read-only source inspection, hashing, call-graph construction, and text/report generation are allowed.

## 13. Explicit prohibitions

Do not:

- modify MATLAB source;
- modify Python production source/tests;
- implement a GE solver;
- run a GE residual function;
- run any HJB/KFE/aggregate solver/evaluator;
- solve `r*`, `w*`, or any equilibrium unknown;
- change accepted household HJB/KFE routes;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- run calibration extension;
- generate Results claims.

## 14. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_REPORT.md`

Include at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. all GE-relevant MATLAB source paths and hashes;
4. exact call graph;
5. complete unknown table;
6. complete residual/equation table;
7. firm/production/government formulas;
8. household-output-to-GE mapping;
9. exact root-solver/numerical closure;
10. exact baseline parameters/grid/calibration source;
11. explicit answers to the `rb/rah/w/Tt/tau/rb_gap/At/Bt/Lt/Ct` closure questions;
12. loaded MAT/data dependency list and provenance status;
13. dissertation cross-check;
14. complete unresolved/provenance list;
15. recommended next residual-map parity contract;
16. zero scientific-call ledger;
17. changed-path list;
18. git status;
19. acceptance level.

## 15. Terminal classifications

Return exactly one:

### PASS

`MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_PASS`

Use only if the designated MATLAB GE closure is fully resolved and no Owner provenance decision is needed for the next residual-map gate.

### OWNER PROVENANCE REQUIRED

`MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_OWNER_PROVENANCE_REQUIRED`

Use if the source references an ambiguous/missing external steady-state artifact, calibration, driver, or closure convention that cannot be resolved from the designated source root and current project evidence.

### BLOCKED

`MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_BLOCKED`

Use if required source files are missing/corrupt or the call graph cannot be audited safely.

## 16. Repository closeout

Repository mutation is report-only.

Stage only the required report, commit once, non-force push once, GitHub read-back the report, require `HEAD == origin/main`, and require clean worktree.

If and only if PASS, recommend only:

**MATLAB-faithful GE steady-state residual-map same-input parity at pre-frozen source-valid trial points.**

Do not authorize the full GE root solve or dynamics from this task.