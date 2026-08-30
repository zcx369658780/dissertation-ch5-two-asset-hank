# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Establish the first **end-to-end MATLAB-faithful stationary household comparison** using each language's own already accepted HJB post-convergence operator and the accepted contaminated-row KFE algorithm.

The task must produce and compare the Owner-requested stationary household table:

- `C^ss` — aggregate household consumption;
- `L^ss` — aggregate household labor;
- `A^ss` — aggregate illiquid assets;
- `B^ss` — aggregate liquid assets;
- `A^ss + B^ss` — total household financial assets.

This is a stationary household-distribution/aggregate gate at frozen prices/parameters. It is **not yet a general-equilibrium steady-state outer-loop acceptance** and must not be described as accepting equilibrium `r*`, `w*`, calibration closure, dynamics, IRFs, or Results.

The task must use the exact designated MATLAB aggregate formulas after source audit. Do not infer formulas from notation if the source differs.

## 2. Controlling accepted authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`

Accepted authorities:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`
- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_KFE_DENSITY_PARITY_ACCEPTED`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`d7a2357496f1c3cdfd676d52d7d60f782f3e7202`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` as the direct child of the accepted KFE closeout commit;
3. verify clean worktree;
4. verify accepted HJB and KFE source/report identities;
5. verify designated MATLAB source hash before aggregate-source interpretation;
6. record live start SHA.

Do not begin from uncommitted scientific changes.

## 4. Reuse-only accepted HJB/KFE scientific objects

Do not rerun accepted HJBs.

Accepted final HJB artifact root:

`D:\ProjectTemp\ch5-hjb-propagation-aware-final-20260830-001`

Accepted HJB outputs:

- MATLAB: `7351351B5D0F7012F03CB6A8CB79A6E31D8FC65FF5D7C26B4A241047F1B5DE94`
- Python: `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`

Reuse from those objects:

- common grid/parameter/initialization identities;
- MATLAB own post-convergence `A_M`;
- Python own post-convergence `A_P`;
- MATLAB policy arrays `C_M`, `L_M`, transfer, cost, etc.;
- Python policy arrays `C_P`, `L_P`, transfer, cost, etc.

Accepted same-operator KFE artifact root:

`D:\ProjectTemp\ch5-kfe-same-operator-20260830-001`

Accepted KFE outputs on MATLAB `A_M`:

- MATLAB faithful KFE: `A53B304C134A909D99F1911983F8CB273AC295AEFF1A7DBBC9CFE621401F44E8`
- Python faithful KFE on the same MATLAB operator: `DF97F38C48CB46B5BC871DCB036B0AD3336DB17BC897A4921B8DEEA148AA98A7`

These two accepted KFE objects form the **same-operator bridge** and must be reused read-only.

Accepted common-operator identity from that gate:

`7A2ADC63CE7A4BB5184036E4CFC07EC082185C90C5B818C572ED05756D222C0F`

Accepted shape/order/spacing:

- `(b,a,z)=(5,5,2)`;
- Fortran/MATLAB ordering;
- `db=0.25`;
- `da=0.5`;
- cell weight `db*da=0.125`.

Do not substitute corrected/reference HJB or clean KFE objects.

## 5. Designated MATLAB aggregate-source audit — mandatory before execution

Designated source:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

Required SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

Read the exact post-KFE aggregate block, including the region around the stationary solve and all lines that construct household aggregates/results.

Audit and record exactly:

- the density object used for aggregation;
- whether aggregates multiply by `db*dah` and whether any `dz`, productivity probability, endpoint/trapezoid weight, or other weight appears;
- exact consumption array used;
- exact labor array used;
- exact illiquid-asset grid object used;
- exact liquid-asset grid object used;
- exact formulas and result-field names for consumption, labor, illiquid assets, and liquid assets;
- whether any aggregate is computed before/after reshaping and the exact vectorization/order;
- whether the source also computes total assets, adjustment costs, transfers, or other household moments that should be reported as diagnostics;
- whether there is any distinction between household aggregate `L` and an equilibrium/production-side labor object.

Do not guess from expected notation.

If the source does not support one of the Owner-requested labels `C^ss/L^ss/A^ss/B^ss`, map the exact source field to the requested table and state the mapping explicitly.

If any aggregate formula is ambiguous, stop:

`MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_BLOCKED`

Do not proceed by inference.

## 6. Freeze aggregate authority after source audit

Only after the source audit closes, freeze an exact aggregate contract.

Expected canonical form if and only if confirmed by source is a density-weighted sum over all `(b,a,z)` states using the same MATLAB density normalization and `db*da` cell weight. The source, not this expectation, controls.

The production Python aggregate route must reproduce the source formula, weight, and object definitions exactly.

Do not use:

- equal-weight state averages;
- clean-KFE probability mass as a substitute for MATLAB density;
- `dz` or productivity weights unless the source explicitly uses them;
- trapezoid endpoint weights unless the source explicitly uses them;
- equilibrium identities as substitutes for source aggregation.

## 7. Own-language end-to-end stationary-distribution design

The end-to-end objects are:

### MATLAB side

- accepted MATLAB HJB policy arrays from the accepted final HJB output;
- accepted MATLAB post-convergence operator `A_M`;
- accepted MATLAB faithful KFE density on `A_M` from `A53B...F44E8`.

No MATLAB HJB or MATLAB KFE rerun is required or authorized.

### Python side

- accepted Python HJB policy arrays from `A33E...98A7`;
- accepted Python own post-convergence operator `A_P`;
- run the published faithful KFE solver exactly once on `A_P` to obtain Python own stationary density `g_P_own`.

The published faithful KFE implementation is:

`src/ch5_two_asset_hank/matlab_faithful_kfe.py`

Accepted source SHA-256 from the KFE gate:

`27DA91779788E76C9F92697247FFF520D460CB9CCAFAC2DE39CDCFF7440A3E88`

Do not change its contaminated row, RHS, normalization, or solver contract.

## 8. Required bridge decomposition for distribution differences

Reuse the accepted Python same-operator KFE density `g_P_common` from `DF97...98A7`, which was computed using MATLAB `A_M`.

Define:

- `g_M` = MATLAB faithful density on MATLAB `A_M`;
- `g_P_common` = Python faithful density on MATLAB `A_M`;
- `g_P_own` = Python faithful density on Python `A_P`.

The comparison must report separately:

1. `g_P_common - g_M`: already accepted direct-solver propagation on the same operator;
2. `g_P_own - g_P_common`: propagation caused by using Python's own already-accepted post-convergence HJB operator instead of MATLAB's;
3. `g_P_own - g_M`: total end-to-end density difference.

Verify the bridge identity on the persisted vectors:

`g_P_own - g_M = (g_P_own - g_P_common) + (g_P_common - g_M)`

within a pre-frozen floating arithmetic bound.

The task must not treat an accepted upstream HJB-operator propagated difference as a new formula mismatch.

However, the Python own KFE solve must independently pass the same contaminated-system backward-error certificate accepted in the KFE gate:

`residual_inf <= 256*eps64*max(1, ||M_system||_inf*||x||_inf, ||rhs||_inf)`.

Also require:

- finite raw solution;
- exact row/RHS contract;
- exact `sum(raw_g)*db*da` normalization;
- density normalization identity;
- no source/index/normalization discrepancy.

## 9. Faithful stationary aggregate implementation

After source audit, implement a distinct narrow production module only if needed, preferably:

`src/ch5_two_asset_hank/matlab_faithful_stationary.py`

It may contain only source-faithful stationary household aggregation over already solved HJB/KFE objects.

Do not modify:

- accepted faithful HJB modules;
- accepted faithful KFE module;
- corrected/reference `steady_state.py`;
- clean/reference KFE;
- calibration/equilibrium code.

Preferred auditable result fields, subject to exact MATLAB source mapping:

- `c_ss`;
- `l_ss`;
- `a_ss`;
- `b_ss`;
- `total_assets_ss`;
- density normalization diagnostic;
- optional source-backed adjustment-cost/transfer aggregate diagnostics.

Add a narrow test file only if implementation occurs, preferably:

`tests/test_matlab_faithful_stationary_aggregates.py`

## 10. Aggregate comparison and decomposition contract

For each requested aggregate `Q` in `C^ss`, `L^ss`, `A^ss`, `B^ss`, and for `A^ss+B^ss`, persist:

- MATLAB value;
- Python value;
- absolute difference;
- relative difference;
- classification;
- source formula/field mapping.

For `C` and `L`, decompose the aggregate difference using the same cell weight and a single fixed state ordering. A valid exact algebraic decomposition is:

`Q_P - Q_M = weight*sum((x_P-x_M)*g_M) + weight*sum(x_P*(g_P_own-g_M))`

where `x` is the relevant policy array.

Report:

- policy contribution;
- density contribution;
- decomposition residual.

For `A` and `B`, the state grids are common, so the policy/state-object contribution should be zero; report the density contribution explicitly.

For `A+B`, report both direct total and `A^ss+B^ss` identity residual.

Do not introduce a broad raw aggregate tolerance after observing output.

### 10.1 Direct/source-local arithmetic

Retain the existing machine rule for same-input source-local replay:

`128*eps64*max(1,abs(x),abs(y))`.

Use it for:

- grid values;
- cell weight;
- source-local aggregate formula replay on identical arrays/density;
- exact asset-grid mapping;
- contaminated row/RHS/normalization construction where rechecked.

### 10.2 Reduction/decomposition arithmetic

Before scientific aggregation, analytically freeze a finite-sum rounding bound for 50-state weighted sums and decomposition closure using standard binary64 `gamma_n = n*eps/(1-n*eps)` reasoning or a stricter justified equivalent. Record the exact derivation and formula before execution.

Do not choose this bound after observing aggregate differences.

This reduction bound is for arithmetic closure of the aggregation/decomposition itself; it is not a license to hide policy/density implementation differences.

### 10.3 Propagation-aware aggregate acceptance

A raw MATLAB/Python aggregate difference may be classified:

`ACCEPTED_HJB_KFE_PROPAGATED_AGGREGATE_DIAGNOSTIC_DIFFERENCE`

only if all are true:

1. HJB parity authorities remain accepted;
2. same-operator KFE parity remains accepted;
3. Python own KFE solve on `A_P` passes its backward-error and normalization contracts;
4. aggregate formulas/weights/field mappings are source-identical;
5. same-input aggregate replay passes the direct/reduction arithmetic contract;
6. distribution bridge identity closes;
7. `C/L` aggregate decomposition closes within the pre-frozen reduction bound;
8. `A/B` differences are fully attributable to the own-density difference on common state grids;
9. no categorical/index/grid/source discrepancy exists;
10. material mismatch list is empty;
11. unresolved scientific residual list is empty.

If these conditions do not hold, do not accept the aggregate merely because the scalar difference is small.

## 11. Required comparison table

The final report must contain this table populated with actual scientific values:

| Stationary household quantity | MATLAB | Python | Abs. diff | Rel. diff | Classification |
|---|---:|---:|---:|---:|---|
| `C^ss` | | | | | |
| `L^ss` | | | | | |
| `A^ss` | | | | | |
| `B^ss` | | | | | |
| `A^ss + B^ss` | | | | | |

Also include a second compact decomposition table:

| Quantity | Policy contribution | Density contribution | Decomposition residual |
|---|---:|---:|---:|
| `C^ss` | | | |
| `L^ss` | | | |
| `A^ss` | `0` expected if source/grid mapping confirms | | |
| `B^ss` | `0` expected if source/grid mapping confirms | | |

The report must clearly state that these are stationary household aggregates under the frozen parameter/price fixture, not yet an accepted general-equilibrium steady state.

## 12. External aggregate evaluators and freeze

Create a fresh no-overwrite artifact root.

Create an external MATLAB aggregate-only evaluator that:

- loads only persisted accepted MATLAB HJB policy arrays and accepted MATLAB KFE density;
- executes only the exact audited MATLAB aggregate formulas;
- does not rerun HJB or KFE;
- does not run equilibrium/calibration/dynamics code.

Create a Python aggregate runner that:

- loads persisted accepted Python HJB policy arrays;
- loads the newly persisted Python own KFE density;
- executes only the same accepted aggregate formulas.

Before any new scientific solve/aggregate evaluation, freeze/hash/read back:

- designated aggregate-source audit;
- accepted MATLAB/Python HJB object identities;
- accepted same-operator KFE object identities;
- Python own `A_P` serialized losslessly;
- faithful KFE source identity;
- aggregate implementation source if added;
- MATLAB aggregate evaluator;
- Python aggregate runner;
- comparator;
- reduction-bound derivation;
- manifest/order/weights;
- execution ledger.

## 13. Scientific call budget

Authorized calls in this task:

- MATLAB HJB: `0`;
- Python HJB: `0`;
- MATLAB KFE: `0`;
- Python own-operator KFE: at most `1`;
- MATLAB aggregate evaluator: at most `1`;
- Python aggregate evaluator: at most `1`;
- final comparator: at most `1`.

No rerun after observing scientific output.

If Python own KFE fails, stop immediately; do not repair/rerun in the same task.

If either aggregate evaluator fails, stop; do not repair/rerun after scientific execution.

## 14. Comparator requirements

The final comparator must persist:

- accepted HJB/KFE input identities;
- MATLAB/Python own post-convergence operator identities and their accepted HJB relationship;
- `g_M`, `g_P_common`, `g_P_own` identities;
- Python own KFE backward-error and normalization diagnostics;
- maximum/summary density differences for the two bridge legs and total end-to-end comparison;
- bridge-identity residual;
- exact source formula mapping;
- all five requested aggregate values and differences;
- `C/L` policy/density decomposition;
- `A/B` density contribution;
- `A+B` identity residual;
- reduction-bound checks;
- material mismatch list;
- unresolved scientific residual list;
- source/environment failure list.

JSON serialization must use the already learned scalar-normalization discipline and fail closed on unsupported non-scalar objects. Do not repeat the prior NumPy scalar persistence failure.

## 15. Terminal classifications

### PASS

`MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_PASS`

Use only if all own-language distribution and aggregate contracts pass and both material mismatch and unresolved lists are empty.

On PASS freeze:

- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HOUSEHOLD_AGGREGATE_PARITY_ACCEPTED`

### MATERIAL MISMATCH

`MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_MATERIAL_MISMATCH`

Use for a genuine source/formula/index/weight/distribution/aggregate mismatch.

### BLOCKED

`MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_BLOCKED`

Use for missing/corrupt accepted artifacts, source ambiguity, failed Python own KFE solve, evaluator failure, comparator persistence failure, or an environment blocker that prevents a qualified comparison.

## 16. Repository mutation and closeout

If PASS, authorized publication paths are limited to:

- `src/ch5_two_asset_hank/matlab_faithful_stationary.py` if created;
- `tests/test_matlab_faithful_stationary_aggregates.py` if created;
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_REPORT.md`.

Do not modify already accepted HJB/KFE source.

If no production module is needed because aggregation is purely external and source-trivial, publish report only; do not create code for the sake of mutation.

On MATERIAL/BLOCKED, preserve all artifacts externally, restore unaccepted source/test changes, and publish report only.

Commit once, non-force push once, GitHub read-back every published path, require `HEAD == origin/main`, and require clean worktree.

## 17. Prohibitions

Do not:

- rerun MATLAB/Python HJB;
- rerun MATLAB KFE;
- change accepted HJB/KFE sources;
- change contaminated-row or normalization authority;
- use clean/reference KFE as production;
- run general-equilibrium steady-state loops;
- solve for `r*` or `w*`;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- run calibration extension;
- run Results.

If and only if PASS, recommend only the smallest next source-backed gate required to move from frozen-price stationary household aggregates to MATLAB-faithful general-equilibrium steady-state closure. Do not authorize dynamics yet.
