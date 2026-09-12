# CH5 MP4C K1 — quarterly-HJB vs annual-firm-flow source/calibration provenance closure

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: zero-science source/calibration authority closure.
Issuer: ChatGPT Reviewer.

## 1. Goal

Close the remaining time-unit/calibration provenance gap between annual corrected-2018 firm flow/stock objects and the continuous-time household HJB before any new runtime.

The previous accepted audit established that direct numerical identity `HJB r_a = current raw firm ra0` is not authorized because annual `Y/K` and profit/K are combined with a source-quarterly `delta=.025`, while the HJB primitives have no complete common calendar unit authority.

This task must determine whether existing dissertation/source/legacy calibration evidence can support one coherent time convention, or whether a precise Owner calibration decision remains necessary.

No model execution is authorized.

## 2. Mandatory reads

Fresh-fetch live `origin/main`, record actual SHA, and verify this task remains active.

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT_ACCEPTANCE.md`
- `docs/CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT_REPORT.md`
- `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_PAYOFF_SCALE_MAPPING_AND_DIAGNOSTIC_BOUND_POLICY_FREEZE_CURRENT.md`
- relevant accepted HJB/KKT/boundary authority docs
- dissertation `Main_Spine/c4.tex` and `Main_Spine/c5.tex`
- protected legacy MATLAB sources defining `rho`, `rb`, `delta`, `Q_z`, wage, firm returns, household HJB, transfers and adjustment costs
- active Python source defining the same objects.

Do not restart historical parity, K1A, KFE, distance or data audits except where a source identity is needed for this exact task.

## 3. Scientific-call budget

All new scientific/model runtime calls are zero:

- trajectory / outer turn: 0
- HJB: 0
- KFE: 0
- household runtime: 0
- firm runtime: 0
- MATLAB runtime: 0
- K1B: 0
- K2: 0
- GE: 0
- annual: 0
- shock/IRF: 0
- Results: 0.

Allowed operations are static source inspection, hashing, text extraction, symbolic/unit algebra, parsing accepted static receipts, and zero-science scripts/tests.

## 4. Depreciation conflict closure

Resolve or precisely classify all authoritative occurrences of firm/HJB depreciation:

- dissertation Chapter 4 `.025` quarterly statement;
- dissertation Chapter 5 `.0025` table entry;
- active Python `.025`;
- protected MATLAB `.025`;
- any dissertation equations or prose that imply annual depreciation near `.10`;
- any distinct PIM depreciation `.096`, which must remain separate from household/firm capital-return depreciation unless a source explicitly equates them.

For each occurrence record exact path/page/line, semantic role, calendar unit, and authority class.

End with one of:

- typographical conflict resolved by stronger source authority;
- genuine calibration conflict requiring Owner freeze;
- unresolved because evidence is insufficient.

Do not silently choose `.025`, `.0025`, `.10`, or `.096`.

## 5. Common time-base closure

Audit whether the inherited continuous-time HANK calibration is intended to use:

- quarter as one model-time unit;
- year as one model-time unit;
- another explicitly defined base unit;
- or only abstract model time.

Trace exact authority for:

- `rho=.05`;
- `rb=.02` and borrowing gap `.07`;
- `r_a/rah`;
- productivity generator off-diagonal intensity `1/3`;
- `delta`;
- wage and transfer flow units;
- `chi0`, `chi1`, and adjustment-cost timing;
- any labor-disutility/time normalization relevant to flow utility;
- shock/IRF quarter labeling only as supporting evidence, not automatic stationary-HJB authority.

Familiar parameter magnitudes are not proof.

## 6. Annual data-to-model-time bridge

Trace exactly how annual empirical objects enter firm/HJB quantities:

- annual GDP `Y`;
- capital stock `K`;
- population/labor units;
- firm wage `wjt`;
- profit flow;
- `Y/K` and profit/K;
- any per-capita/per-person scaling into household wage/asset grid.

Determine whether source documents ever state a conversion from annual firm flows to quarterly/model-time flows before HJB use.

If no conversion exists, classify it explicitly.

## 7. Calibration provenance tree

Construct a compact provenance graph/table for the active values and formulas:

`source statement -> legacy MATLAB literal/formula -> active Python literal/formula -> HJB/firm usage`.

At minimum include:

- `rho`
- `rb`
- borrowing spread/gap
- `delta`
- `Q_z=1/3`
- `chi0`
- `chi1`
- wage bounds
- return bounds
- `Tt`
- any consumption/derivative floors relevant to dimensional scale.

Mark each link as:

- `SOURCE_CONFIRMED`
- `LEGACY_INHERITED_ONLY`
- `CONFLICTING`
- `UNRESOLVED`
- `NUMERICAL_SAFEGUARD`.

## 8. Candidate coherent conventions

Evaluate only conventions supportable by evidence.

At minimum test conceptually:

### Convention Q — quarterly HJB/model-time

If source evidence supports quarter as the HJB base unit, determine the full set of conversions required for annual firm flows and all rate/flow primitives. Do not assume simple `/4` unless the flow object and conversion law are source-consistent.

### Convention A — annual HJB/model-time

If source evidence supports year as HJB base unit, determine the full set of parameter reinterpretations/conversions required, including quarterly `delta` and generator intensity.

### Convention M — unresolved/abstract model time

If no calendar base is source-authorized, state which calibrations must be newly frozen by Owner before runtime.

For each convention report:

- source support;
- dimensional consistency;
- required parameter conversions;
- whether cross-province ranking is preserved;
- whether it changes only units or changes economics/calibration;
- unresolved assumptions;
- whether Owner freeze is required.

Do not numerically calibrate by fit or convergence.

## 9. Discounting and depreciation conversion laws

If evidence supports a discrete-to-continuous or quarterly-to-annual conversion, distinguish explicitly among:

- linear flow scaling;
- simple rate multiplication/division;
- compounding;
- continuous log-rate conversion.

Do not treat these as interchangeable.

Only endorse a law if the source object is identified sufficiently to justify it.

If not, leave the mapping unresolved.

## 10. Wage / transfer / adjustment-cost consistency

This task must not focus on `ra0` alone.

Determine what happens to dimensional consistency of:

- firm wage `wjt`;
- household composite wage `w`;
- transfer `Tt`;
- endogenous transfer `d`;
- adjustment-cost term;
- consumption flow;
- labor-income flow

under each viable calendar convention.

A payoff conversion that leaves wage/transfer/cost flows on a contradictory time base is not a valid closure.

## 11. Diagnostic-bound policy interaction

Owner has authorized future temporary `ra/rah` and `wjt/wage` hard bounds for debugging.

This task must clarify which future guard objects should be applied:

- before calendar conversion;
- after calendar conversion;
- or only at the HJB interface,

for each viable convention.

Do not set any new numerical bounds.

Do not promote existing `[.02,.09]` or `[.8,1.3]` to structural calibration.

## 12. STATIC_NO_FEEDBACK calculations

If and only if a convention and conversion law are actually source-backed enough to evaluate, use persisted accepted raw `ra0`/firm components to produce static no-feedback distributions for the converted payoff components.

Label all such calculations:

`STATIC_NO_FEEDBACK__NO_MODEL_EXECUTION`.

Do not feed them to HJB, firm, KFE or outer iteration.

If authority remains unresolved, do not manufacture illustrative `/4` or annualized tables merely for convenience.

## 13. Required classification

End with one precise evidence-based classification. Examples:

- `QUARTERLY_HJB_TIME_BASE_SOURCE_CONFIRMED__ANNUAL_FIRM_FLOW_CONVERSION_LAW_IDENTIFIED__OWNER_FREEZE_REQUIRED`
- `ANNUAL_HJB_TIME_BASE_SOURCE_CONFIRMED__QUARTERLY_DEPRECIATION_CONVERSION_REQUIRED__OWNER_FREEZE_REQUIRED`
- `COMMON_CALENDAR_BASE_NOT_SOURCE_IDENTIFIABLE__OWNER_RECALIBRATION_CONTRACT_REQUIRED`
- `SOURCE_CONFLICT_RESOLVED__COMPLETE_TIME_BASE_CONTRACT_READY_FOR_OWNER_FREEZE`.

Do not use a classification that itself authorizes runtime.

## 14. Exactly one next gate

Recommend exactly one next gate:

- Owner freeze of a complete time-base/calibration contract, followed later by a bounded runtime diagnostic; or
- additional zero-science source closure if one identifiable source is still missing.

Do not publish or execute runtime, K1B, K2, 25-turn raw, steady state or Results.

## 15. Allowed tracked changes

Allowed:

- one zero-science provenance audit script if useful;
- focused zero-science tests;
- `docs/CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE_REPORT.md`;
- compact receipts under `docs/evidence/ch5_mp4c_k1_quarterly_hjb_annual_firm_provenance_closure/`;
- truthful CURRENT closeout docs at task completion.

Forbidden:

- any `src/` scientific change;
- parameter/calibration rewrite;
- payoff mapping implementation;
- hard-bound change;
- HJB/KFE/boundary/KKT equation change;
- firm/C1/labor/capital-network science change;
- grid/tolerance/solver change;
- runtime of any scientific model.

## 16. Git/local safety

Use a fresh isolated worktree/task branch from live main.

Protect original MATLAB/dissertation/evidence sources. No reset, clean, stash, force-push or user-file overwrite.

Stage only explicit allowed paths; do not use `git add .` or `git add -A`.

Publish one coherent non-force commit, verify remote commit/report readback once, do not merge main, and do not publish a successor task.

## 17. Final reply

Return:

- classification;
- actual live-main baseline;
- branch/worktree/candidate SHA;
- changed paths;
- zero scientific-call ledger;
- depreciation conflict result;
- common time-base authority result;
- annual-data bridge result;
- calibration provenance table/graph summary;
- candidate convention table;
- wage/transfer/adjustment-cost consistency result;
- STATIC_NO_FEEDBACK result if legitimately available;
- diagnostic-bound interaction finding;
- exactly one recommended next gate;
- KFE caveat;
- Results eligibility=`FALSE`.

Stop after publication. Do not run a model and do not enter K1B/K2.
