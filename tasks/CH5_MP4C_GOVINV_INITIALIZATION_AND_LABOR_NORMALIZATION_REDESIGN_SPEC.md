# Chapter 5 MP4C GovInv initialization and labor-normalization redesign specification

Date: 2026-09-10

## 1. Objective

Produce a zero-science redesign specification for two now-evidenced calibration problems in the corrected-2018 multi-province route:

1. `GovInv0=Ktarget` creates total firm capital overshoot once positive private household capital supply is added, and the current controller amplifies that gap over the accepted 25-turn diagnostic prefix.
2. destination firm labor from the existing migration/allocation mechanism is not commensurate with the initialization population proxy `N0`; late-window `firm_Lt_supply/N0` ratios are far above one in every province, so the labor normalization/reference contract must be reconstructed before further steady-state execution.

This task is design/static analysis only. It does not authorize a new trajectory, HJB/KFE run, parameter tuning, or production-source implementation.

## 2. Required authority

Fresh-read live `origin/main` and at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_REPORT.md`;
- its Reviewer acceptance;
- accepted corrected-2018 runtime input-binding repair report/acceptance;
- accepted raw-NBS 2018 rebuild report;
- accepted unit-normalized initialization probe and firm-price forensic;
- accepted MATLAB multi-province logic audit;
- protected/read-only MATLAB sources: `HANK_mp_1eq.m`, `HANK_mp_1turn.m`, `Lt_seperate.m`, `HANK_firm.m`, `wage_caculate.m`, `mpHANK_equilibrium_2000.m`, `load_GDPdata.m`.

## 3. Scientific facts already accepted

Do not re-litigate these facts:

- corrected-2018 runtime uses actual 2018 GDP/POP, raw-NBS GFCF Track-A PIM, `delta_pim=.096`, `alpha=.7380939146868483`, `MU=10万元`, `NU=100 persons`;
- `GovInv0=Ktarget` is currently only a source-faithful initialization rule pending redesign;
- `beta_a=1` is only source-faithful diagnostic baseline;
- productive private capital is household illiquid `At`, not `Bt` or `At+Bt`;
- firm total capital is `Kt_supply + GovInv`;
- late-window median total-K/target ≈ `2.35998`, private-K/target ≈ `0.00291675`, GovInv/target ≈ `2.35795`;
- late-window destination-firm-labor/population-proxy median ≈ `14.23079`, with all 31 province means severely above the proxy;
- `N0` is not observed workplace employment;
- no production GovInv or labor redesign is yet authorized;
- Results eligibility is FALSE.

## 4. Workstream A — GovInv initialization redesign

Recover exactly how `GovInv` is initialized, updated, and used in protected MATLAB.

Evaluate, without running science, at least these candidate initialization contracts:

### Candidate G0 — source baseline

`GovInv0 = Ktarget`

Retain only as benchmark; document why accepted 25-turn evidence shows systematic overshoot.

### Candidate G1 — residual-to-target initialization

`GovInv0 = max(Ktarget - Kt_supply_initial, 0)`

Define precisely what `Kt_supply_initial` would have to mean and at what point it can be observed without circularity.

Because household `At` itself depends on prices, explicitly analyze whether `Kt_supply_initial` should come from:

- generic initialized `At`;
- one household-pass output under data-consistent prices;
- a lagged/source-faithful prior state;
- or another source-backed object.

Do not choose among these without evidence.

### Candidate G2 — share initialization

`GovInv0 = g0 * Ktarget`, `0<=g0<=1`

Only analyze whether the source or dissertation provides any authority for a fixed share. Do not tune `g0` from convergence.

### Candidate G3 — decomposition-by-economic-role

If source/dissertation supports separate public-capital and private-capital concepts, define a contract using an externally justified public-capital share/series. Do not invent such a series.

For every candidate state:

- economic meaning;
- source support;
- circularity risk;
- dimensional consistency;
- interaction with `Kt_supply`;
- interaction with current `.9/1.1` GovInv controller;
- whether it preserves positivity;
- whether it can be identified without convergence-based tuning.

## 5. Workstream B — GovInv controller compatibility

Static-audit the existing controller:

- trigger on clipped `ra`;
- decrease/increase thresholds;
- multiplicative `.9/.1.1` update;
- relation to `Zt` update;
- relation to `KNratio/tKNratio` gate.

Use the accepted 25-turn ledger only as observed evidence to classify controller behavior; do not fit new parameters.

Design at most three controller-integration options for a later task:

- preserve current controller unchanged with a new initialization;
- preserve trigger but add under-relaxation/damping to GovInv path;
- separate initialization correction from controller redesign.

Do not freeze a new production controller in this task.

## 6. Workstream C — labor object/scale reconstruction

Recover all labor objects and their units/roles:

- population `N`;
- household labor returned by HJB/KFE;
- household labor before population aggregation;
- `Lt_mat(destination,origin)`;
- destination `Lt_supply`;
- firm `Lt`;
- any per-capita/efficiency-labor normalization;
- wage-calculate inputs;
- stored `results.Lt` before/after overwrite.

Construct an explicit dimensional chain.

The task must determine whether the huge `firm_Lt_supply/N0` ratios can be explained by one or more of:

- multiplying household per-capita labor by population after it already embeds a scale factor;
- comparing efficiency labor to raw population units;
- migration matrix normalization/aggregation;
- a source-intended nonlinear labor-supply level that is not meant to equal population;
- another source-backed normalization.

No empirical claim may be made beyond what source and accepted ledgers support.

## 7. Workstream D — migration-adjusted labor target/reference options

The Owner has proposed using geography and GDP-per-capita differences, via the existing `Lt_seperate.m` logic, to construct a migration-adjusted province labor reference because true interprovincial workplace employment is unavailable.

Analyze this idea as a calibration/reference design, not as a production implementation.

At minimum compare:

### L0 — population proxy baseline

`Ltarget_i = N_i`

### L1 — migration-adjusted population allocation

Apply the source migration weights/relative-income logic to exogenous province population totals to construct destination labor-reference shares, while preserving an explicit national total.

You must specify whether this is mathematically possible using static source weights without household endogenous labor quantities.

### L2 — employment-rate scaled population

Only if an authoritative employment-rate/labor-force source already exists in repository or protected data. Otherwise classify `DATA_NOT_AVAILABLE` and do not invent.

### L3 — model-consistent normalized migration shares

Use source migration mechanism only to produce destination shares, then normalize total labor to an independently fixed national aggregate. Analyze identification requirements and whether this preserves the intended migration assumption.

For each candidate describe:

- formula;
- source support;
- national conservation property;
- unit/scale contract;
- interpretation in paper;
- whether it changes economics or only calibration normalization;
- data requirements;
- risks.

## 8. Workstream E — joint K/L initialization contract

Design a staged initialization sequence that avoids simultaneous circularity.

At minimum consider:

1. bind corrected 2018 Y, Ktarget, population and alpha;
2. construct a labor reference/normalization candidate;
3. compute same-year Z under that candidate;
4. initialize firm prices from source equations;
5. perform at most one explicitly labelled initialization household pass if scientifically necessary in a future task;
6. construct initial private `Kt_supply`;
7. set GovInv according to the selected future rule;
8. only then begin the outer loop.

This is a specification only. Identify which steps would require a future scientific call budget.

## 9. No silent use of convergence to identify scale

Forbidden in this design:

- choosing GovInv scale because it converges;
- choosing labor normalization because it lowers boundary hits;
- choosing `beta_a` because it matches Ktarget;
- choosing wage/return bounds to obtain PASS;
- changing alpha, PIM delta, firm delta, HJB/KFE equations, grids or solver family.

Any candidate needing external identification must be labelled `OWNER_OR_DATA_DECISION_REQUIRED`.

## 10. Required outputs

At minimum:

- `docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md`;
- `reports/mp4c_govinv_labor_redesign_20260910/govinv_candidate_matrix.csv`;
- `.../govinv_controller_compatibility.md`;
- `.../labor_object_dimensional_chain.csv`;
- `.../labor_reference_candidate_matrix.csv`;
- `.../joint_initialization_sequence.md`;
- `.../owner_decision_matrix.csv`;
- `.../zero_scientific_call_ledger.json`;
- source/hash receipts, focused static tests, manifest/readback.

## 11. Required report conclusions

The report must answer:

1. Is `GovInv0=Ktarget` scientifically defensible as more than a historical numerical start?
2. Is residual initialization `max(Ktarget-Kt_supply_initial,0)` structurally coherent, and what exactly must identify `Kt_supply_initial`?
3. Should GovInv initialization and GovInv controller redesign be separated into different future tasks?
4. Why is `firm_Lt_supply/N0` so large under current scaling?
5. Which labor object should be compared to a population/employment target?
6. Is a migration-adjusted labor reference based on geography and GDP-per-capita source logic feasible without observed interprovincial workplace employment?
7. What is the lowest-risk next implementation order?
8. Which items still require Owner scientific choice?

## 12. Scientific-call budget

All model/scientific calls = 0.

Forbidden:

- HJB/KFE/household solve;
- `Lt_seperate` runtime execution on model states;
- firm runtime;
- outer turn/steady state;
- root/Brent scientific solve;
- GE/annual/IRF/Results.

Allowed:

- static source inspection;
- deterministic algebra;
- accepted-ledger analysis;
- source-safe helper calculations that do not advance model state;
- tests/hashes/serialization.

## 13. Allowed verdicts

- `GOVINV_LABOR_REDESIGN_SPEC_PASS__SEPARATE_CAPITAL_AND_LABOR_CORRECTION_PATHS_DEFINED`;
- `GOVINV_LABOR_REDESIGN_SPEC_PARTIAL__OWNER_OR_DATA_DECISIONS_REMAIN`;
- `GOVINV_LABOR_REDESIGN_SPEC_BLOCKED__SOURCE_SEMANTICS_INSUFFICIENT`.

A PASS/PARTIAL is design evidence only and does not authorize implementation or a trajectory.

## 14. Git boundary

Use dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit and non-force push candidate;
- do not merge main;
- do not publish successor scientific task;
- Results eligibility remains FALSE.

Return verdict, branch, candidate SHA, key GovInv conclusion, key labor-normalization conclusion, unresolved Owner choices, and report path.
