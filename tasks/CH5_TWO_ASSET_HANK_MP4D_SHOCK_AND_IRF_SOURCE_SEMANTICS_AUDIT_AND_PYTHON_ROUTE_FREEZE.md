# CH5_TWO_ASSET_HANK_MP4D_SHOCK_AND_IRF_SOURCE_SEMANTICS_AUDIT_AND_PYTHON_ROUTE_FREEZE

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor: Codex bounded Builder / source-semantics auditor

Owner: final scientific authority

## 1. Authority basis

Formal predecessor acceptance:

`MP4C_2009_2023_PYTHON_ANNUAL_STATIONARY_COVERAGE_FORMALLY_ACCEPTED`

Acceptance commit:

`478e8d05d1e8a2729f2e05b12ee30dfcaf323730`

Acceptance level:

`FULL_2009_2023_PYTHON_ANNUAL_STATIONARY_COVERAGE_ACCEPTED__CORRECTED2009_CROSS_LANGUAGE_PARITY_RETAINED__DYNAMICS_NOT_YET_ACCEPTED`

This task begins MP4D. It is a **ZERO-SCIENCE source audit and route-freeze gate only**.

It does not authorize any shock, AR(1), transition, dynamic, IRF, MATLAB, or Python scientific execution.

## 2. Purpose

Before reconstructing or running shock responses, determine exactly what the protected MATLAB code currently means by its shock/IRF route.

The audit must distinguish source-backed behavior from labels such as “dynamic”, “AR(1)”, or “IRF”. Previous static audit evidence suggested the protected route may be a sequential comparative-statics path that repeatedly solves stationary household objects rather than a genuine backward-HJB / forward-KFE transition system. This task must independently verify and freeze that conclusion from live protected source.

The output must specify one exact Python reconstruction contract and the earliest next executable scientific gate.

## 3. Required live continuity

At execution start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as direct child of `478e8d05d1e8a2729f2e05b12ee30dfcaf323730`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read completely:
   - `AGENTS.md`;
   - all CURRENT project rules named by `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
   - formal MP4C annual stationary acceptance report;
   - formal corrected-2009 parity acceptance report;
   - MP4C full-batch execution report;
   - `validators/multi_province/matlab_persistence_contract.json`;
   - live annual production/checkpoint implementation;
   - all prior source audits that address the MATLAB shock route.

## 4. Protected MATLAB source audit

Use the accepted logical/physical Junction identity and keep protected MATLAB source read-only.

Read at minimum:

- `main.m`;
- `main2.m` if it contains a related route;
- `multi_prov_HANK.m`;
- `mpHANK_shock_2000.m`;
- `multi_prov_HANK_12sts.m`;
- `mpHANK_equilibrium_2000.m`;
- `HANK_mp_1turn.m`;
- `HANK_2ASSETS_HJB.m`;
- `HANK_firm.m`;
- monetary, tax, government-investment and productivity shock helpers if any;
- plotting/export helpers used by the shock/IRF section;
- any function that loads `Multi_Province_12sts_<year>.mat` or writes shock-response output.

Record SHA-256 for every protected source that materially enters the route.

## 5. Exact shock-call graph

Freeze the exact protected call graph from the top-level caller to persisted response output.

At minimum answer:

- which `main.m` lines invoke the shock route;
- how calendar year / steady-state checkpoint is selected;
- how `multi_prov_HANK` loads the annual `st` object;
- exact signature and arguments passed into `mpHANK_shock_2000`;
- whether each response date calls `HANK_mp_1turn` once, a steady-state iterator, or another solver;
- whether household HJB/KFE objects at response date `t` are stationary or time-dependent;
- which state from date `t` is carried into date `t+1`;
- which baseline objects are reset from frozen steady state each date;
- which objects accumulate over time;
- what is persisted for plotting.

## 6. Shock semantics matrix

Inventory every shock type actually reachable from the protected top-level code.

For each shock, record:

- source label / numeric selector;
- economic target variable;
- province scope if applicable;
- baseline value;
- shock size/sign;
- exact time path formula;
- horizon;
- whether the path is additive, multiplicative, level, log, percentage, or percentage-point;
- decay/persistence parameter;
- whether the code contains a literal AR(1) recursion or only a deterministic exponential path;
- whether innovations are stochastic or deterministic;
- exact point at which the shock enters household/firm/fiscal/monetary objects;
- whether the same shock is reset from baseline every date or evolves from prior shocked value.

Do not call a deterministic exponential path “AR(1)” unless source contains the corresponding recursion and innovation semantics.

## 7. Genuine-transition diagnostic

Produce an explicit yes/no source matrix for the following objects:

- finite-horizon terminal condition;
- backward time-dependent HJB;
- forward time-dependent KFE/distribution law;
- expectation law across response dates;
- time-indexed value function solved backward;
- time-indexed distribution propagated forward;
- transition-path convergence condition;
- sequence-space / perfect-foresight solve;
- contemporaneous stationary HJB at each response date;
- contemporaneous stationary KFE at each response date;
- carry-forward of aggregate/state variables only.

Classify the protected route with the strongest source-backed label, choosing one of:

`GENUINE_TRANSITION_DYNAMICS_SOURCE_CONFIRMED`

`SEQUENTIAL_STATIONARY_COMPARATIVE_STATICS_RESPONSE_PATH_CONFIRMED`

`HYBRID_RESPONSE_ROUTE_CONFIRMED`

`SHOCK_ROUTE_SOURCE_SEMANTICS_UNRESOLVED`

Do not force equivalence between these classes.

## 8. Checkpoint-consumption contract

Audit what the shock route requires from annual steady state and compare it against the new Python checkpoint artifacts.

For each required object classify:

- exact Python equivalent already preserved;
- reconstructable from preserved Python annual checkpoint;
- currently missing but derivable without changing science;
- missing and requiring new scientific design/Owner decision.

Cover at minimum:

- province final `results` scalars;
- household value function;
- final consumption/labor/transfer policies;
- final KFE density;
- grids `a,b,z` and switching matrix;
- population/province order;
- annual runtime data / `data_MAT` semantics;
- `sigmau` / distance-migration matrix;
- parameter/numerical objects;
- `CHI` / adjustment-cost representation;
- initial aggregate and firm states;
- any shock selector and horizon objects.

Do not claim the Python `Python_Multi_Province_12sts_<year>.mat` is a drop-in legacy MATLAB `st` unless exact schema parity is proven.

## 9. Response-output contract

Freeze the exact source output required for later paper figures and validation.

Identify:

- variables stored at each horizon date;
- dimensions/orientation;
- province order;
- aggregate/national summaries;
- normalization used by plotting code, e.g. level change, percent deviation, percentage point;
- which figures/tables source code constructs;
- any historical file naming convention;
- any response variable that is plotted but not persisted.

Produce a Python-side output schema proposal that preserves source semantics and supports later paper plotting without forcing MATLAB file-format identity.

## 10. Representative-year validation design

Do not execute it yet.

Design the smallest next scientific validation gate.

Prefer a representative-year strategy before full 15-year shocks.

The design must specify:

- candidate representative year(s) and why source/provenance makes them informative;
- exact shock type to validate first;
- exact horizon;
- exact steady-state checkpoint used;
- MATLAB reference availability/need;
- comparison fields and normalization;
- allowable numerical non-identity criterion if already governed by an accepted comparator contract;
- stop conditions;
- finite execution budget;
- no blanket full-sample run until representative-year semantics are accepted.

If a representative year requires Owner choice because multiple scientifically distinct options remain, explicitly mark the choice and stop before publishing a scientific execution gate.

## 11. Performance boundary

Record as engineering context only that the accepted Python 15-year stationary production batch used four year-level workers and took `32622.241112` seconds scientific wall clock. Do not optimize HJB/KFE/grid/tolerances/controllers in this audit.

Potential future shock-batch performance improvements may concern orchestration, caching, checkpoint reuse and year-level parallelism only unless separately authorized.

## 12. Zero-science execution budget

Exact task budget:

- MATLAB process/model calls: `0`;
- Python stationary calls: `0`;
- Python household/HJB/KFE calls: `0`;
- comparator calls: `0`;
- shock/AR(1)/transition/dynamics/IRF scientific runs: `0`;
- R5/Results: `0`.

Allowed operations:

- source reads;
- static AST/text inspection;
- hashing;
- reading existing manifests/contracts;
- serialization/schema inspection without solver execution;
- deterministic text/JSON/CSV/Markdown artifact generation;
- zero-science tests for parsers/contracts if narrowly necessary.

## 13. Required external evidence package

Use a fresh no-overwrite root, preferred:

`D:\ProjectTemp\ch5-mp4d-shock-irf-source-semantics-audit-20260902-001`

Persist at minimum:

- `matlab_shock_call_graph.json`;
- `shock_semantics_matrix.csv`;
- `genuine_transition_diagnostic.json`;
- `checkpoint_consumption_contract.json`;
- `response_output_contract.json`;
- `python_shock_route_freeze.json`;
- `representative_year_validation_design.md`;
- `zero_science_execution_ledger.json`;
- `audit_manifest.json`.

## 14. Required repository report

Create only:

`docs/CH5_TWO_ASSET_HANK_MP4D_SHOCK_AND_IRF_SOURCE_SEMANTICS_AUDIT_AND_PYTHON_ROUTE_FREEZE_REPORT.md`

No scientific production code mutation is authorized in this task.

A narrowly scoped validation parser/test may be added only if strictly necessary to prove source semantics; prefer report/artifacts only.

## 15. Terminal classifications

PASS requires one unambiguous source-backed route classification and one frozen Python reconstruction contract:

`MP4D_SHOCK_AND_IRF_SOURCE_SEMANTICS_AUDIT_AND_PYTHON_ROUTE_FREEZE_PASS`

If source semantics remain scientifically ambiguous:

`MP4D_SHOCK_AND_IRF_SOURCE_SEMANTICS_AUDIT_BLOCKED_OWNER_DECISION_REQUIRED`

If PASS, recommend exactly one next gate:

`MP4D_REPRESENTATIVE_YEAR_SHOCK_RESPONSE_IMPLEMENTATION_AND_VALIDATION`

Do not start that next gate inside this task.
