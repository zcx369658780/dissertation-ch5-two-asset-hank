# CH5 MP4C K1 — HJB payoff-scale authority zero-science audit

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: zero-science source/authority audit.
Issuer: ChatGPT Reviewer under Owner-approved payoff-scale decision.

## 1. Goal

Determine whether the firm-side raw return object `ra0` and the household continuous-time HJB use the same model-time scale, period convention and numeraire, and whether a source-backed mapping from firm return to household `r_a` can be frozen.

This task is not a runtime experiment. It must not change or execute the numerical model.

The Owner retains raw `ra0` as the economic payoff source object, but the direct numerical identity mapping `r_a = ra0` is no longer assumed scientifically valid until this audit closes the time/scale authority.

## 2. Mandatory reads

Fresh-fetch live `origin/main`; record actual SHA and verify this task remains active.

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_PAYOFF_SCALE_MAPPING_AND_DIAGNOSTIC_BOUND_POLICY_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC_ACCEPTANCE.md`
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC_REPORT.md`
- directly relevant accepted HJB/equation/KKT/boundary authority documents
- active Python firm/HJB/household/export sources that define `rho`, `delta`, `r_a`, `r_b`, productivity-state transitions, wage inputs, transfer law and time stepping/continuous-time equations
- relevant legacy MATLAB multi-province/two-asset sources and their accepted provenance manifests/reports
- relevant dissertation/source documentation already available under protected project authority.

Do not restart unrelated parity, K1 distance, KFE or data-rebuild gates.

## 3. Scientific-call budget

All new scientific/model calls are zero:

- trajectory `0`
- HJB `0`
- KFE `0`
- household runtime `0`
- firm runtime `0`
- MATLAB runtime `0`
- K1B `0`
- K2 `0`
- GE `0`
- annual `0`
- IRF/shock `0`
- Results `0`.

Allowed: static source inspection, hashing, parsing accepted persisted receipts, symbolic/unit algebra, static arithmetic on already-persisted values, compact tables, zero-science script/tests.

## 4. Time-unit inventory

Build a source-backed inventory for every object that can identify model time:

- household discount rate `rho`;
- liquid return `r_b` / `rb`;
- illiquid payoff `r_a` / `rah`;
- firm depreciation `delta`;
- firm raw return `ra0` and used/clipped `ra`;
- productivity-state transition generator/rates (`z`, `h_z`, transition intensity or equivalent);
- any wage/`wjt` law or bounds entering household income;
- adjustment-cost/transfer law coefficients if their units depend on time;
- HJB equation and any explicit/implicit continuous-time convention;
- steady-state outer iteration timing, clearly separated from economic calendar time;
- any annual/quarterly/monthly labels in MATLAB, dissertation text, comments, parameter tables or data construction.

For each object classify period authority as one of:

- `SOURCE_CONFIRMED_ANNUAL`
- `SOURCE_CONFIRMED_QUARTERLY`
- `SOURCE_CONFIRMED_OTHER`
- `MODEL_TIME_ONLY`
- `CONFLICTING_SOURCE_AUTHORITY`
- `UNRESOLVED`.

Do not infer a calendar period merely from a familiar parameter magnitude.

## 5. HJB dimensional consistency

Trace the exact source HJB equation/implementation and document the dimensional role of:

- `rho V`;
- flow utility;
- `V_b * mu_b` / liquid drift term;
- `V_a * mu_a` / illiquid drift term;
- productivity generator term;
- `r_b b` and `r_a a` income/return components;
- transfer `d` and adjustment cost.

Determine what common time unit these rates/drifts must share for the continuous-time HJB to be dimensionally coherent.

This is an authority audit, not permission to rewrite equations.

## 6. Firm-return scale audit

Trace exact source formulas and units for:

`rk = mt * alpha / (K/Y)`

and

`ra0 = rk + after_tax_profit_over_K - delta`.

For corrected-2018 data, determine from frozen data contracts and source construction whether:

- `Y` is an annual flow, another-period flow, or unresolved;
- `K` is an end-of-period/stock level and its price/base-year convention;
- `K/Y` therefore has an implicit time dimension;
- `delta=.025` has explicit calendar authority or is only a model-period parameter;
- `rk` and `profit/K` are directly comparable to the HJB rate unit.

If annual GDP is used to construct `Y/K`, say so only when source/data authority proves it. Distinguish data frequency from HJB model-time convention.

## 7. Legacy MATLAB and dissertation authority

Search accepted/protected legacy sources for explicit statements or equations identifying:

- period length;
- annualization or de-annualization;
- depreciation frequency;
- discount-rate frequency;
- productivity transition calibration frequency;
- return bounds `ramin/ramax` interpretation;
- wage/`wjt` bounds interpretation;
- whether firm `ra0` was intended to be passed directly to household HJB or transformed.

Record exact path/line/page provenance where available.

If sources conflict, do not reconcile silently; classify the conflict.

## 8. Current hard-bound inventory

Statically inventory all active or legacy hard bounds relevant to the current route, including at least:

- `ra` / `ra0` / `rah` related bounds;
- wage / `wjt` bounds;
- consumption floors/caps;
- derivative floors;
- labor bounds;
- transfer/control bounds if any;
- any price/return clipping in firm or household adapters.

For each bound record:

- exact source path/line;
- value;
- object bounded;
- current active vs legacy/reference status;
- source-stated purpose, if any;
- authority classification: structural / empirical calibration / numerical safeguard / unresolved.

Do not activate, change or recommend exact new values in this audit.

## 9. Candidate mapping table

Evaluate only mappings supported by actual source authority. Candidate rows should include, where applicable:

A. identity mapping: `r_a = ra0`;

B. calendar-to-model-time rate conversion if and only if both calendar period and HJB model period are source identified;

C. continuous-time rate conversion if source objects are proven to be discrete/gross returns and a mathematically appropriate transformation is source-compatible;

D. a source/dissertation-documented alternative payoff mapping if one exists;

E. temporary diagnostic bounds as numerical scaffolding — explicitly **not** a final economic mapping.

For each candidate report:

- source fidelity;
- dimensional consistency;
- cross-province ranking preservation;
- whether absolute scale changes;
- calibration assumptions required;
- whether Owner choice is needed;
- whether a bounded runtime test would be required afterward.

Do not invent arbitrary shrinkage factors, z-score payoff, ad-hoc normalization, smoothing, risk adjustment or new caps.

## 10. Static scale implications

Using only already-persisted accepted evidence, if useful, show what any **source-backed** candidate mapping would imply for observed Raw `ra0`/`rah` distributions.

No model feedback. Label all such calculations `STATIC_NO_FEEDBACK`.

If no source-backed non-identity mapping can be established, do not manufacture one merely to produce a table.

## 11. Diagnostic-bound policy

The Owner has authorized temporary hard return/wage bounds as future debugging scaffolding, but only under a fresh exact runtime task.

This audit must therefore recommend a governance protocol, not values:

- exact bounds preregistered before execution;
- saturation/hit counts persisted;
- bounds classified as diagnostic guards rather than structural economics;
- no post-result tuning to force PASS;
- any relaxation follows a preregistered ladder;
- bound-dependent steady state remains provisional;
- final route should widen/remove guards where scientifically feasible.

Do not activate bounds in this task.

## 12. Required end classification

Choose one truthful evidence-based outcome, for example:

- `IDENTITY_RA0_TO_HJB_RA_TIME_SCALE_SOURCE_CONFIRMED__DIRECT_MAPPING_REMAINS_AUTHORIZED`
- `SOURCE_BACKED_PERIOD_SCALE_MAPPING_IDENTIFIED__OWNER_FREEZE_REQUIRED_BEFORE_RUNTIME`
- `FIRM_RETURN_AND_HJB_TIME_UNITS_CONFLICT__DIRECT_RA0_MAPPING_NOT_AUTHORIZED`
- `PAYOFF_SCALE_AUTHORITY_REMAINS_UNRESOLVED__ADDITIONAL_SOURCE_EVIDENCE_REQUIRED`.

A more precise variant is allowed.

The classification itself does not authorize runtime.

## 13. Next gate

Recommend exactly one next gate:

- Owner freeze of a source-backed payoff mapping followed by a bounded runtime diagnostic;
- additional zero-science source/provenance closure;
- or, if identity mapping is genuinely source-confirmed, a bounded diagnostic-bound runtime design before longer trajectory work.

Do not enter 25-turn Raw, K1B, K2 or Results.

## 14. Allowed tracked changes

Allowed:

- one zero-science audit script if useful;
- focused zero-science tests;
- `docs/CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT_REPORT.md`;
- compact receipts under `docs/evidence/ch5_mp4c_k1_hjb_payoff_scale_authority_audit/`;
- truthful CURRENT closeout docs only at task completion.

Forbidden:

- `src/` scientific changes;
- payoff formula changes;
- bound changes;
- firm/HJB/KFE/C1/labor/capital-network science changes;
- calibration/grid/tolerance/solver changes;
- any scientific runtime.

## 15. Git/local safety and publication

Use a fresh isolated worktree from live main. Protect original MATLAB/source evidence. No reset/clean/stash/force-push/overwrite.

Stage explicit allowed paths only; no `git add .` or `git add -A`.

Publish one coherent candidate commit to a task branch, non-force. Perform one remote commit/report readback. Do not merge main and do not publish a successor task.

## 16. Final Builder response

Return:

- final classification;
- actual live-main baseline;
- branch/worktree/candidate SHA;
- changed paths;
- zero scientific-call ledger;
- time-unit authority table;
- HJB dimensional-consistency finding;
- firm-return scale finding;
- legacy MATLAB/dissertation evidence;
- hard-bound inventory;
- candidate mapping table;
- any `STATIC_NO_FEEDBACK` implications;
- diagnostic-bound governance finding;
- exactly one recommended next gate;
- KFE caveat;
- Results eligibility=`FALSE`.

Then stop. Do not run the model.
