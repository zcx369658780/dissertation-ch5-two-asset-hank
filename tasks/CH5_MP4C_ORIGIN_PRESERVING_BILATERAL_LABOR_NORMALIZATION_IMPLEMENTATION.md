# Chapter 5 MP4C origin-preserving bilateral labor-normalization implementation

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Owner scientific decision now frozen for this task

Owner has approved preserving the full province-to-province labor matrix and normalizing migration **within each origin province**, not collapsing labor into national destination shares.

The intended successor logic is:

1. household block determines each origin province's labor supply per household/efficiency-labor object;
2. multiply by origin population once to obtain the origin aggregate labor mass;
3. use the existing `Lt_seperate` destination-attractiveness kernel to determine bilateral destination shares;
4. normalize those shares within each origin column;
5. allocate the entire origin labor mass across destinations;
6. destination firm labor is the row sum;
7. retain the complete destination-by-origin matrix so origin-specific migration and wage provenance remain traceable.

This task implements that bounded labor-normalization contract only. It does not claim labor is the primary cause of current steady-state failure and it does not modify GovInv.

## 2. Required authority

Fresh-read live `origin/main` and at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md`;
- `docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC_ACCEPTANCE.md`;
- accepted 25-turn K/L rerun report/acceptance;
- `src/ch5_two_asset_hank/multi_province/migration_labor.py`;
- `src/ch5_two_asset_hank/multi_province/one_turn.py`;
- `src/ch5_two_asset_hank/multi_province/wage.py`;
- protected/read-only `Lt_seperate.m` and `wage_caculate.m` if available through the already-authorized source path.

Protected MATLAB remains read-only.

## 3. Preserve legacy/source-faithful path

Do **not** delete, silently redefine, or relabel the existing literal source-faithful function:

`reconstruct_migration_labor`

Its current behavior remains historical/source-fidelity authority for MATLAB parity.

Implement the normalized successor as an explicitly different function/type/route, for example:

`reconstruct_origin_preserving_normalized_migration_labor`

or an equivalently explicit name.

Likewise, do not silently change `run_source_faithful_one_turn`. If one-turn integration support is added, create a separately named successor composition route rather than altering the meaning of the source-faithful route.

## 4. Frozen matrix orientation

Rows = destination province `j`.

Columns = origin household province `i`.

The complete bilateral labor-flow matrix is:

`M[j,i]`.

This orientation must remain explicit in code, tests, schemas, and reports.

## 5. Origin labor mass

For each origin `i`, define the aggregate origin labor mass as:

`L_origin_i = household_labor_per_capita_i * population_i`.

Here:

- `household_labor_per_capita_i` is the HJB/KFE returned efficiency-labor object already present in `PreFrozenHouseholdOutputBatch.household_lt`;
- `population_i` is the origin population object `N_i` in the accepted runtime;
- population is multiplied exactly once.

Do not replace `household_labor_per_capita` by population itself.
Do not impose an external national labor total in this task.
Do not normalize origin labor masses across provinces.

The implied national labor total is endogenous to the household outputs:

`sum_i L_origin_i`.

## 6. Destination-attractiveness kernel

Recover the same nonnegative destination-by-origin kernel used by the current literal `Lt_seperate` reconstruction before the final population multiplication.

For origin `i`, destination `j`, define raw attractiveness `q[j,i]` from the same source ingredients and powers as the current implementation:

`q[j,i] = C_i^(-gamma_c/phi_l) * [ wjt_j * (1 - tau_i - sigma[j,i]) / phi[j,i] ]^(1/phi_l)`

subject to the same finite/nonnegative power-domain checks.

Do not tune or alter:

- `gamma_c`;
- `phi_l`;
- `phi[j,i]`;
- migration wedges/distances;
- tax treatment;
- destination wage input;
- power exponents.

For a given origin, factors constant across destination may mathematically cancel under share normalization. Record this fact; do not remove source terms from the implementation merely to simplify unless tests prove algebraic identity and the report retains the original kernel definition.

## 7. Column normalization

For each origin `i`, compute:

`Q_i = sum_j q[j,i]`.

Require:

- `Q_i` finite;
- `Q_i > 0`.

Then define bilateral migration shares:

`s[j,i] = q[j,i] / Q_i`.

Required invariants:

- `s[j,i] >= 0`;
- for every origin `i`, `sum_j s[j,i] = 1` within tight deterministic floating tolerance;
- orientation remains destination rows, origin columns.

Zero/invalid origin columns must fail closed; do not invent equal shares as fallback.

## 8. Bilateral labor-flow matrix

Define:

`M[j,i] = s[j,i] * L_origin_i`.

Required origin-column conservation:

`sum_j M[j,i] = L_origin_i` for every origin `i`.

Destination firm labor is:

`L_firm_j = sum_i M[j,i]`.

Required national conservation:

`sum_j L_firm_j = sum_i L_origin_i = sum_{j,i} M[j,i]`.

This conservation is the key new normalization contract.

It does **not** require:

`L_origin_i = L_firm_i` province by province.

Net labor flow by province is therefore meaningful as:

`net_i = L_firm_i - L_origin_i`.

## 9. Traceability requirements

The normalized result object should expose, directly or through an auditable receipt:

- raw attractiveness matrix `q`;
- normalized share matrix `s`;
- origin aggregate labor mass vector;
- bilateral flow matrix `M`;
- destination firm labor vector;
- column sums of shares;
- column sums of flows;
- net destination-minus-origin labor vector;
- national conservation residual.

Do not reduce the output to destination row sums only.

The full matrix is required for province-to-province migration provenance and later household-wage attribution.

## 10. Henan-style provenance test

Add at least one small asymmetric synthetic fixture demonstrating the Owner's example logic.

For an origin province with aggregate labor mass `50`, construct deterministic shares such as or equivalent to:

- 60% remains in origin;
- 24% goes to destination A;
- 16% goes to destination B.

Verify the origin column sums exactly to `50` and the three bilateral flows are `30`, `12`, and `8` up to deterministic float tolerance.

Add other-origin inflows so the destination province can end with a firm labor total different from its resident/origin labor mass, e.g. `40` versus `50`, while the bilateral provenance remains fully reconstructible.

The precise synthetic numbers may differ if needed for direct kernel construction, but the test must prove the same traceability property.

## 11. Wage boundary in this task

Do **not** redesign `wage_caculate` / `composite_household_wages` in this task.

Reason: labor normalization and wage aggregation must remain separately attributable.

However, add documentation/tests proving that the normalized bilateral matrix retains the information needed for a later wage-provenance task:

for each origin `i`, the complete vector `M[:,i]` and/or `s[:,i]` identifies where that origin's workers are allocated.

Do not convert the current CES-like/composite wage formula into a simple weighted average here.

## 12. One-turn integration boundary

Preferred implementation:

- preserve the source-faithful one-turn route unchanged;
- add a separately named normalized-successor one-turn composition route or injection hook that consumes `household_outputs.household_lt` as origin labor supply and uses the new normalized migration result;
- keep capital allocation, firm equations, wage formula, monetary assignment, fiscal diagnostics, and update ordering otherwise unchanged.

If a clean separate integration route cannot be added without broad refactor, implement the normalized migration module and tests only, document the blocker, and return PARTIAL rather than mutating source-faithful semantics.

No scientific trajectory is authorized in this task.

## 13. GovInv boundary

Do not change:

- `GovInv0`;
- GovInv controller;
- capital target;
- asset bridge `beta_a`;
- private-capital allocation;
- firm-return controller thresholds.

The accepted evidence says current steady-state imbalance is more directly dominated by GovInv than by labor. This labor task must not be used to claim otherwise.

GovInv residual initialization will be handled in a separate successor task after this implementation is independently reviewed.

## 14. Zero-science execution budget

Scientific/model calls must remain zero:

- HJB = 0;
- KFE = 0;
- household solve = 0;
- `Lt_seperate` MATLAB runtime = 0;
- firm runtime trajectory = 0;
- outer turn trajectory = 0;
- steady state = 0;
- root/Brent scientific solve = 0;
- GE/annual/IRF/Results = 0.

Allowed:

- Python implementation edits;
- deterministic synthetic fixtures;
- direct pure-function calls to the new migration normalization routine;
- static source inspection;
- unit tests;
- compile/lint/static checks;
- serialization/hash/readback.

## 15. Mandatory tests

At minimum prove:

1. legacy `reconstruct_migration_labor` output remains unchanged for existing fixtures;
2. normalized route preserves destination-by-origin orientation;
3. every normalized share column sums to one;
4. every bilateral labor-flow column sums to that origin's aggregate household labor mass;
5. national destination labor equals national origin labor mass;
6. province destination labor may differ from its own origin labor mass without violating conservation;
7. asymmetric bilateral provenance is recoverable;
8. population is multiplied exactly once;
9. changing one origin household labor supply scales only that origin column's mass, not other origin masses;
10. changing one destination wage changes shares/directions as expected without changing total origin mass;
11. zero or invalid attractiveness column fails closed;
12. no negative/nonfinite output is accepted;
13. source-faithful route and normalized successor route are explicitly distinguishable in schema/API;
14. no GovInv/capital/wage/HJB/KFE economics changed.

## 16. Required outputs

At minimum commit:

- normalized successor production/module code;
- minimal separate one-turn integration support if safely implementable;
- regression tests;
- `docs/CH5_MP4C_ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_IMPLEMENTATION_REPORT.md`;
- `reports/mp4c_origin_preserving_bilateral_labor_normalization_20260910/normalization_contract.md`;
- `.../synthetic_bilateral_trace.csv`;
- `.../conservation_test_receipt.json`;
- `.../legacy_path_unchanged_receipt.json`;
- `.../api_schema_receipt.json`;
- `.../zero_scientific_call_ledger.json`;
- source/hash receipt;
- focused test receipt;
- manifest/readback.

## 17. Required report answers

Answer explicitly:

1. Does the new route retain the full 31x31 destination-by-origin provenance structure?
2. Is each origin labor mass preserved exactly across its destination column?
3. Is national labor conserved between origin household supply and destination firm use?
4. Can a province's resident/origin labor differ from its destination firm labor while flows remain attributable by province pair?
5. Does the implementation still permit later origin-specific household wage attribution?
6. Did any source-faithful MATLAB parity path change? It must be NO for PASS.
7. Did any GovInv/capital/controller/HJB/KFE/wage aggregation rule change? It must be NO for PASS.
8. What remains for the later GovInv task and later wage-provenance task?

## 18. Allowed verdicts

- `ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_PASS__FULL_MATRIX_TRACEABILITY_AND_CONSERVATION_ENFORCED`;
- `ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_PARTIAL__NORMALIZED_MODULE_VALID_BUT_ONE_TURN_INTEGRATION_DEFERRED`;
- `ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_BLOCKED__CURRENT_ARCHITECTURE_CANNOT_PRESERVE_PROVENANCE_WITHOUT_BROAD_REDESIGN`.

PASS is implementation evidence only. It does not authorize a scientific trajectory or Results.

## 19. Git boundary

Use a dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit and non-force push candidate;
- do not merge main;
- do not publish successor task;
- do not run a scientific trajectory.

Return to ChatGPT Reviewer with verdict, branch, candidate SHA, files changed, focused tests, conservation results, synthetic bilateral trace summary, legacy-path preservation result, zero-science call ledger, and report path.
