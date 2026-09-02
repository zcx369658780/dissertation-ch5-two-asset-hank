# CH5 TWO ASSET HANK MP4D L3 FORMAL SHOCK/IRF SOURCE-SEMANTICS ACCEPTANCE REPORT

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Reviewer: ChatGPT L3 independent reviewer / scientific route authority

Owner: final scientific authority

## 1. Terminal verdict

`MP4D_SHOCK_AND_IRF_SOURCE_SEMANTICS_FORMALLY_ACCEPTED`

Accepted route classification:

`SEQUENTIAL_STATIONARY_COMPARATIVE_STATICS_RESPONSE_PATH_CONFIRMED`

Acceptance level:

`MP4D_SOURCE_SEMANTICS_ACCEPTED__NUMERICAL_SHOCK_RESPONSE_NOT_YET_AUTHORIZED`

## 2. Authority and continuity

Reviewed execution commit:

`1c3894ab84a76719b478da3ec06bea3d037ee808`

Required task authority:

`30f6274aefd1baab3fbb58df6b3060016125b93e`

Fresh GitHub verification established that the execution is the direct child of the task authority and that live `main` was the execution commit before this acceptance publication.

The execution changed exactly one repository path:

`docs/CH5_TWO_ASSET_HANK_MP4D_SHOCK_AND_IRF_SOURCE_SEMANTICS_AUDIT_AND_PYTHON_ROUTE_FREEZE_REPORT.md`

No scientific production code was modified.

## 3. Accepted source-backed semantics

The protected MATLAB shock/response route is accepted as follows:

1. `main.m` constructs a deterministic 1-percent exponential path `0.01*exp(-0.5*(t-1))` over `T=20` response dates.
2. The active source does not establish a stochastic AR(1) recursion or innovation process.
3. `multi_prov_HANK` selects an annual steady-state object and calls `mpHANK_shock_2000` for a chosen shock province.
4. At each response date, `mpHANK_shock_2000` resets named exogenous objects including `Zt`, `GovInv`, `tau`, and `corptau` from the frozen annual baseline and applies the date-specific shock.
5. Each response date calls one contemporaneous `HANK_mp_1turn` path.
6. That one-turn route invokes contemporaneous stationary household HJB/KFE logic together with migration, firm, wage, monetary and fiscal blocks.
7. Response `results` are carried from date `t` to `t+1`, while the named shocked exogenous objects are re-based on the frozen annual steady state each date.
8. There is no source-backed finite-horizon terminal condition, backward time-indexed HJB, forward time-indexed KFE, expectations recursion, sequence-space solve, perfect-foresight transition solve, or transition-path convergence condition.

Therefore the protected implementation must not be described as a genuine heterogeneous-agent transition-dynamics solver. The accepted scientific label is:

`SEQUENTIAL_STATIONARY_COMPARATIVE_STATICS_RESPONSE_PATH_CONFIRMED`

## 4. Frozen Python reconstruction boundary

A future Python response implementation must:

- materialize a source-semantic response state from an accepted annual checkpoint;
- preserve the frozen annual baseline separately from the carried response state;
- reconstruct the deterministic source shock path exactly;
- reset source-named exogenous objects from the frozen baseline each response date before applying the shock;
- carry only the source-backed response state across dates;
- call one source-faithful contemporaneous one-turn analogue per response date;
- preserve raw response fields;
- preserve source plotting normalization such as `response / baseline - 1` explicitly;
- avoid claiming that the Python checkpoint is a legacy MATLAB `st` drop-in unless exact schema parity is separately proven.

## 5. Zero-science ledger accepted

The MP4D audit performed zero:

- MATLAB model/process calls;
- Python stationary calls;
- household/HJB/KFE scientific calls;
- comparator calls;
- shock/AR(1)/transition/IRF scientific runs;
- R5/Results work.

The task is therefore accepted as a static source-semantics freeze only.

## 6. Important post-audit annual-data blocker

After MP4D execution was already underway, the Owner clarified a previously misunderstood annual-data construction:

- underlying processed annual data span calendar years 2000–2023;
- each steady-state year 2009–2023 uses a 10-year rolling PLM estimation window ending in that steady-state year;
- the R `plm` estimation outputs therefore correspond to 15 rolling windows: 2000–2009, 2001–2010, ..., 2014–2023;
- the rolling-window/result index and the calendar-year row inside the 24-row level-data arrays are distinct objects.

This clarification creates a material scientific blocker for the current Python annual runtime-cache adapter, which presently binds both the outer rolling-window entry and the inner 24-row level-data selection using the same `year-2008`-style index.

Therefore the previously published full-annual Python acceptance:

`MP4C_2009_2023_PYTHON_ANNUAL_STATIONARY_COVERAGE_FORMALLY_ACCEPTED`

is hereby **suspended as final annual scientific authority pending rolling-window/calendar-row revalidation**.

This suspension does not invalidate:

- the accepted household/HJB/KFE numerical reconstruction;
- the repaired source-faithful one-turn semantics;
- the batch runner engineering implementation;
- the fact that the previous 15-year batch converged under its then-bound inputs;
- the corrected-2009 MATLAB–Python parity evidence under its separately frozen same-input contract.

It means only that the 2009–2023 production batch cannot be used as final calendar-year paper evidence until the rolling-window versus annual-level row contract is corrected and re-executed if required.

## 7. Route decision

Do **not** proceed immediately to `MP4D_REPRESENTATIVE_YEAR_SHOCK_RESPONSE_IMPLEMENTATION_AND_VALIDATION`.

The required next gate is instead a return to MP4C data binding:

`MP4C_ROLLING_PLM_WINDOW_AND_CALENDAR_LEVEL_ROW_BINDING_CORRECTION_AND_OWNER_RERUN_PREPARATION`

Only after corrected annual steady states are accepted may the project return to the MP4D representative-year shock-response implementation gate.
