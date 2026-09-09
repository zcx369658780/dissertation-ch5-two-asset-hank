# CH5 MP4C 2018 MATLAB input-data and initial-state comparison audit

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Perform a **data/provenance comparison only** for the original MATLAB multi-province HANK route used around the problematic corrected-2018 trajectory.

The immediate question is whether the observed outer-loop instability / household aggregate collapse can plausibly originate from the **external province-level inputs and initial state magnitudes** rather than from the household HJB/KFE algorithm itself.

Collect and compare the actual MATLAB-side values used to initialize and update the 31-province model, with primary emphasis on:

- initial/source `Zt` / productivity objects;
- capital objects: source capital data, `Kt_supply`, `GovInv`, and total productive `Kt` where available without rerunning science;
- target/observed GDP (`Y0`/GDP target) and population `N`;
- capital-output elasticity `alpha`;
- initial/old-state `ra`, household composite `rah`, `rb`, `wjt` / household wage objects where persisted or directly initialized in source;
- household aggregate `At`, `Bt`, `Lt`, `Ct` only where already persisted in accepted artifacts/caches and useful to diagnose scale propagation;
- any clipping/range-control variables relevant to the initial magnitudes (`ra` bounds, wage bounds, GovInv adjustment thresholds), as source metadata rather than as a redesign target.

The core deliverable is a **31-province side-by-side comparison table** showing what the original MATLAB route actually used versus the current corrected/canonical 2018 inputs where a valid mapping exists.

Do not run the household model, KFE, firm block, outer iteration, steady state, GE, annual model, IRF, or any new scientific solve.

## 2. Required authorities and sources

Read live GitHub current documents first:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`;
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`;
- accepted corrected-2018 data/canonical-input reports and the accepted turn1–5 reports needed only to identify the corrected 2018 comparison objects.

Read the protected original MATLAB tree **read-only** at the verified physical root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

At minimum inspect:

- `main.m`;
- `multi_prov_HANK_12sts.m`;
- `mpHANK_equilibrium_2000.m`;
- `load_GDPdata.m`;
- `HANK_mp_1eq.m`;
- `HANK_mp_1turn.m`;
- `Lt_seperate.m`;
- `HANK_firm.m`;
- `wage_caculate.m`;
- directly referenced workbooks / MAT caches used by the 2018 route.

Do not modify the protected MATLAB tree or its data files.

Current canonical private workbook authority remains read-only:

`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`

Expected SHA-256:

`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`

If this identity does not match, stop comparison against the workbook and report the mismatch; do not substitute another file silently.

## 3. Scientific-call budget

All scientific/model calls are **zero**:

- MATLAB model calls: 0;
- Python household/HJB/KFE calls: 0;
- firm/wage/migration/capital-allocation model calls: 0;
- outer-turn / steady-state / GE / annual / IRF / Results calls: 0;
- root/direct/iterative/eigen scientific solves: 0.

Allowed actions:

- static source inspection;
- read-only workbook/MAT/cache inspection;
- hashes and file provenance;
- extraction of already-saved arrays/scalars;
- deterministic arithmetic needed to express units or compare already-existing values;
- table construction, serialization and static tests.

If a quantity can only be obtained by rerunning a model function, mark it `NOT_AVAILABLE_WITHOUT_SCIENTIFIC_RERUN` rather than running it.

## 4. First task: reconstruct the original MATLAB 2018 data route

Before comparing numbers, reconstruct the exact data path for the 2018 case:

1. identify the year/index used by the original MATLAB route for the object labelled 2018;
2. identify every workbook/MAT/cache field that supplies GDP, capital, population, `alpha`, `Zt`, `GovInv` or other initial state values;
3. distinguish raw workbook data, transformed data, regression-derived values, cached values and runtime-initialized values;
4. record units and scaling operations at every step;
5. record the province ordering and prove that the comparison uses the same ordering;
6. explicitly surface any unresolved year-label/index mismatch rather than guessing.

Produce a short source-to-variable lineage map with file + line references.

## 5. Required 31-province comparison table

Create one machine-readable and one human-readable table with one row per province.

Columns should include, where actually available:

### Identity
- province index;
- province name;
- MATLAB source year/index;
- canonical year.

### GDP / population / production parameters
- MATLAB GDP target / `Y0`;
- canonical corrected GDP;
- absolute and relative difference;
- MATLAB population `N`;
- canonical corrected population;
- difference;
- MATLAB `alpha`;
- canonical `alpha`;
- difference;
- MATLAB initial/source `Zt`;
- canonical corrected same-year `Zt`;
- ratio / log-ratio / relative difference as numerically appropriate.

### Capital side
- raw/source MATLAB capital-data object (with original units);
- transformed MATLAB capital object used for model initialization, if source-backed;
- canonical PIM capital object;
- ratio / relative difference;
- initial/source `GovInv`;
- persisted `At` where already available;
- `At*N` where it is an already-defined deterministic transformation of saved values;
- persisted/source `Kt_supply` where available;
- total productive `Kt = Kt_supply + GovInv` where both components are already available from saved evidence or initialization, without rerunning allocation.

### Price/control state, if already available
- initial `ra` or runtime initialized `ra`;
- initial/composite `rah`;
- `rb`;
- `wjt` / household wage;
- whether each hits or begins near a configured bound;
- source location / artifact provenance.

Do **not** manufacture missing values by executing model functions.

## 6. Special focus: provinces and magnitudes most likely to destabilize the outer loop

At minimum identify:

- largest MATLAB-vs-canonical `Zt` discrepancies;
- largest capital-level / capital-per-capita discrepancies;
- largest GDP-target discrepancies;
- provinces with unusually large/small initial `GovInv` relative to private/productive capital;
- provinces whose initialized or persisted `ra`, `rah` or wage are at/near configured bounds;
- provinces with extreme implied `K/L`, `K/Y`, or `Y/N` ratios where these can be computed from already-existing data without model execution.

Highlight Anhui because the accepted corrected-2018 trajectory diagnostics are centered there, but do not restrict the audit to Anhui.

Also flag any province where unit scaling, interpolation, year indexing, regression-vintage selection, or cache provenance could explain an order-of-magnitude discrepancy.

## 7. Comparison against the accepted corrected-2018 setup

Use current accepted corrected-2018 evidence only as a comparison target; do not rerun it.

For each key object, classify the relationship as one of:

- `EXACT_MATCH`;
- `MATCH_AFTER_DOCUMENTED_UNIT_TRANSFORM`;
- `SMALL_REVISION_DIFFERENCE`;
- `MATERIAL_LEVEL_DIFFERENCE`;
- `MATERIAL_SCALE_OR_UNIT_DIFFERENCE`;
- `YEAR_OR_VINTAGE_MISMATCH`;
- `CACHE_OR_PROVENANCE_AMBIGUITY`;
- `NOT_COMPARABLE_BY_CONSTRUCTION`;
- `NOT_AVAILABLE_WITHOUT_SCIENTIFIC_RERUN`.

Do not infer that a discrepancy causes the turn3 asset collapse. The task is to identify candidate external-input scale problems and establish where they enter the outer loop.

## 8. Outer-loop interpretation map

Produce a concise static map showing how the audited variables feed the model:

`data / Zt / alpha / N / GovInv / initial prices`
→ household call inputs (`w`, `rb`, `rah`)
→ saved household aggregates (`At`, `Lt`, ...)
→ `Lt_seperate` / capital allocation
→ `Kt_supply + GovInv`
→ `HANK_firm`
→ next `wjt`, `ra`
→ next household `rah` / controller actions.

For every audited variable, state whether it is:

- exogenous data;
- calibration/regression derived;
- initialized state;
- household output;
- allocation output;
- firm output;
- controller-updated object.

This map is descriptive only; do not change equations or controller logic.

## 9. Evidence root and outputs

Use a fresh no-overwrite local evidence root, e.g.:

`D:\ProjectTemp\ch5-2018-matlab-input-data-initial-state-audit-20260910-001`

Use a fresh suffix if occupied.

Required repository-safe outputs:

- `docs/CH5_MP4C_2018_MATLAB_INPUT_DATA_AND_INITIAL_STATE_COMPARISON_AUDIT_REPORT.md`;
- a 31-province CSV/TSV comparison ledger under a suitable `reports/` subdirectory;
- source/data lineage map;
- unit/scaling audit;
- largest-discrepancy summary;
- outer-loop variable-role map;
- source/file hash receipt for the MATLAB workbooks/MAT caches actually read;
- call ledger certifying scientific/model calls = 0;
- manifest/readback receipt for repository-safe outputs.

Do not commit private/proprietary workbook or MAT contents beyond the minimum derived comparison values needed for this audit. Never commit the canonical workbook itself.

## 10. Allowed primary verdicts

- `MATLAB_2018_INPUT_DATA_AUDIT_PASS__MATERIAL_EXTERNAL_SCALE_DIFFERENCES_IDENTIFIED`;
- `MATLAB_2018_INPUT_DATA_AUDIT_PASS__NO_MATERIAL_EXTERNAL_SCALE_DIFFERENCE_FOUND`;
- `MATLAB_2018_INPUT_DATA_AUDIT_PARTIAL__YEAR_OR_CACHE_PROVENANCE_AMBIGUITY`;
- `MATLAB_2018_INPUT_DATA_AUDIT_BLOCKED__REQUIRED_SOURCE_DATA_UNAVAILABLE`.

A PASS here is only a data/provenance audit result. It does not establish household/KFE validity, outer-loop convergence, or Results eligibility.

## 11. Git / publication

Use an isolated branch/worktree if practical.

- preserve unrelated dirty/untracked files;
- no reset/clean/stash;
- explicit path staging only;
- no force push;
- commit and push the audit report and repository-safe ledgers on a dedicated branch;
- do not merge main;
- do not start a successor scientific task.

## 12. Stop conditions

Stop the affected comparison and report clearly if:

- the canonical workbook hash differs;
- the original MATLAB data source needed for 2018 cannot be located;
- the year/index mapping cannot be established without an Owner decision;
- extracting a requested quantity would require a scientific/model rerun;
- protected source/data would need to be modified.

Otherwise complete the full static/read-only data audit in one task.
