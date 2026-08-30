# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resume the immediately preceding MATLAB-faithful end-to-end stationary household aggregate parity gate using only the already persisted scientific artifacts, correct only the final comparator JSON-serialization boundary for the NumPy boolean scalar that prevented `comparison.json` persistence, execute exactly one replacement comparator, and close out the stationary distribution / household aggregate parity decision.

This task MUST NOT rerun any HJB, KFE, or aggregate evaluator.

This task MUST NOT infer PASS from the predecessor report's read-only aggregate table. PASS requires one valid persisted replacement comparator result under the unchanged scientific contract.

The target remains frozen-price stationary household quantities, not a general-equilibrium steady-state closure.

## 2. Controlling authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_REPORT.md`

Accepted authorities remain frozen:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`
- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_KFE_DENSITY_PARITY_ACCEPTED`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Predecessor terminal:

`MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_BLOCKED`

## 3. Live continuity

Task-authoring parent observed before publication:

`ac6aee8769f948b52fe4fa9488af6d7d3ed66f8c`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` as a direct child of the predecessor report commit;
3. verify clean worktree;
4. verify predecessor report identity;
5. verify accepted HJB/KFE source/report identities;
6. verify no unaccepted aggregate production/test path exists on `main`.

Do not begin from uncommitted scientific changes.

## 4. Frozen predecessor artifact root and scientific objects

Reuse only:

`D:\ProjectTemp\ch5-end-to-end-stationary-aggregate-20260830-001`

Frozen accepted/reused scientific identities:

- MATLAB HJB: `7351351B5D0F7012F03CB6A8CB79A6E31D8FC65FF5D7C26B4A241047F1B5DE94`
- Python HJB: `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`
- MATLAB KFE: `A53B304C134A909D99F1911983F8CB273AC295AEFF1A7DBBC9CFE621401F44E8`
- Python same-operator KFE: `DF97F38C48CB46B5BC871DCB036B0AD3336DB17BC897A4921B8DEEA148AA98A7`
- Python own-operator KFE: `FBFE4DF7BFD8FDFA848268F440E4CC6ADCF669EDF9C91067D87FCF3E4F324BE8`
- MATLAB aggregate output: `DB42C6338AB079D46DF95F2BA12BAE3326B624D3FBD5E430273966D88073F2F9`
- Python aggregate output: `212C424BEE00C5EBF9FA994FF3077F9F4786B9AA78DEDD1BBD2C36301431D6FA`
- density bridge NPZ: `7CE32408C6E91062F88F389160BC0EFC8561F4BEB93B8EB5CB2FFD437C0C8939`
- Python `A_P` serialization: `B07A2311FEA22D01ED4A26F59D8C79EEA5E82DFEC7AADBBD52C8D2BCE8A52035`

Predecessor source audit is frozen:

- `C^ss = sum(C .* g * dah * db, 'all')`
- `L^ss = sum(zzz .* l .* g * dah * db, 'all')`
- `A^ss = sum(aaah .* g * dah * db, 'all')`
- `B^ss = sum(bbb .* g * dah * db, 'all')`
- weight exactly `dah*db = 0.5*0.25 = 0.125`
- no `dz`, productivity probability, trapezoid, or endpoint weight
- `L^ss` is productivity-weighted effective household labor

Do not re-audit by modifying source; read-only confirmation is allowed.

## 5. Scientific execution budget

Exactly:

- MATLAB HJB: `0`
- Python HJB: `0`
- MATLAB KFE: `0`
- Python KFE: `0`
- MATLAB aggregate evaluator: `0`
- Python aggregate evaluator: `0`
- replacement comparator: at most `1`

No solver/evaluator rerun is authorized.

## 6. Mandatory comparator persistence audit

Inspect the frozen predecessor comparator and exact traceback before any correction.

Prove and record:

1. exact exception type;
2. exact traceback / failing `json.dumps` persistence line;
3. exact NumPy boolean scalar type (`numpy.bool_` or equivalent);
4. first sorted payload key/path containing the failing object;
5. all NumPy scalar types that can reach the payload;
6. whether any ndarray/non-scalar object can reach the payload;
7. whether all scientific comparison calculations completed before persistence;
8. whether material/unresolved aggregation completed before persistence;
9. whether the aggregate table and decomposition had been fully computed in memory before persistence;
10. that no field list, arithmetic bound, density-bridge rule, decomposition formula, mismatch logic, or PASS/MATERIAL logic needs modification.

Only if the failure is strictly serialization-only, freeze:

`END_TO_END_AGGREGATE_COMPARATOR_NUMPY_SCALAR_JSON_SERIALIZATION_ONLY`

Otherwise stop BLOCKED. Do not change scientific comparison logic.

The predecessor in-memory result, if recoverable, is not acceptance evidence.

## 7. Serialization-only comparator correction

Create a NEW comparator artifact. Do not overwrite the predecessor comparator.

The correction must be limited to JSON scalar normalization at the serialization boundary. Prefer:

```python
if isinstance(obj, np.generic):
    return obj.item()
raise TypeError(...)
```

only after static audit proves this exactly covers the frozen payload scalar types and no ndarray conversion is needed.

Every changed line must be classified:

`END_TO_END_AGGREGATE_COMPARATOR_JSON_SERIALIZATION_TYPE_NORMALIZATION_ONLY`

Do not change:

- HJB/KFE/aggregate inputs;
- aggregate formulas;
- density bridge formulas;
- policy/density decomposition formulas;
- finite-sum rounding bound;
- same-input `128*eps64*max(...)` rule;
- field ordering;
- material/unresolved logic;
- PASS/MATERIAL decision;
- any diagnostic/non-veto status.

## 8. No-science serializer preflight

Before the replacement comparator, freeze/hash:

- predecessor comparator;
- corrected comparator;
- exact comparator diff;
- serialization audit;
- serializer preflight;
- MATLAB/Python aggregate output identities;
- all three KFE density identities (`g_M`, `g_P_common`, `g_P_own`);
- density bridge NPZ identity;
- unchanged aggregate/decomposition contract;
- successor execution ledger.

Run exactly one no-science serializer preflight proving:

- native Python bool/int/float remain unchanged;
- `np.bool_` becomes identical native bool;
- every other NumPy scalar actually present becomes the identical native scalar;
- ndarray/non-scalar objects remain fail-closed unless an already-authorized frozen serialization path exists;
- payload scientific values, fields, ordering, classifications, material/unresolved lists, and PASS/MATERIAL logic are unchanged.

If preflight fails, stop BLOCKED without consuming comparator budget.

## 9. Replacement comparator contract

Run exactly one corrected comparator against the already persisted predecessor scientific artifacts.

It must re-establish and durably persist all predecessor-authorized comparisons, including:

### 9.1 Density bridge

Let:

- `g_M` = MATLAB density from MATLAB own accepted post-convergence operator;
- `g_P_common` = Python density on the common MATLAB operator from the accepted same-operator KFE gate;
- `g_P_own` = Python density on Python's own accepted post-convergence operator.

Persist:

`g_P_own - g_M = (g_P_own - g_P_common) + (g_P_common - g_M)`

with:

- same-operator solver leg;
- own-operator leg;
- total end-to-end difference;
- bridge residual;
- frozen bridge bound.

Use the existing frozen bounds unchanged.

### 9.2 Stationary aggregate table

Persist the qualified table:

| Stationary household quantity | MATLAB | Python | Abs. diff | Rel. diff | Classification |
|---|---:|---:|---:|---:|---|
| `C^ss` | ... | ... | ... | ... | ... |
| `L^ss` | ... | ... | ... | ... | ... |
| `A^ss` | ... | ... | ... | ... | ... |
| `B^ss` | ... | ... | ... | ... | ... |
| `A^ss+B^ss` | ... | ... | ... | ... | ... |

The predecessor read-only values are diagnostic expectations only; do not hard-code them into PASS logic.

### 9.3 Required contribution decomposition

For `C^ss` and `L^ss`, persist:

`aggregate_P - aggregate_M = policy_contribution + density_contribution + residual`

using the frozen decomposition convention from the predecessor task.

For `A^ss` and `B^ss`, because the state grids are common, persist:

- state-grid contribution = exact `0` if the source/common-grid identity is confirmed;
- density contribution;
- decomposition residual.

Persist the same for `A^ss+B^ss` either directly or as the sum of the accepted A/B decomposition, with an explicit identity residual.

### 9.4 Acceptance rules

Do not invent a broad aggregate tolerance.

Retain the predecessor pre-frozen finite-sum binary64 bound based on `gamma_n = n*eps64/(1-n*eps64)` and the same-input direct rule:

`128*eps64*max(1,abs(x),abs(y))`.

A PASS requires:

1. all reused accepted HJB/KFE identities match;
2. Python own-KFE backward-error certificate remains PASS from persisted evidence;
3. density bridge closes within the frozen bound;
4. same-operator and own-operator legs are fully accounted for;
5. aggregate formulas match designated MATLAB source;
6. `C^ss/L^ss/A^ss/B^ss/A^ss+B^ss` all pass the frozen finite-sum/decomposition contract;
7. all decomposition residuals pass;
8. material mismatch list is empty;
9. unresolved scientific residual list is empty;
10. source/environment failure list is empty.

## 10. Terminal acceptance and closeout

If replacement comparator persists PASS, freeze:

- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HOUSEHOLD_AGGREGATE_PARITY_ACCEPTED`

Terminal:

`MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_PASS`

If comparator persists a genuine scientific mismatch:

`MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_MATERIAL_MISMATCH`

If serialization/source/environment blocks persistence again:

`MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_BLOCKED`

Repository mutation is report-only unless an already-authorized unchanged aggregate helper/test path is proven to exist and is explicitly required for accepted production. Do not create production code merely to create a commit.

Required successor report:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`

On any terminal:

- preserve artifacts externally;
- stage only authorized report path(s);
- commit once;
- non-force push once;
- GitHub read-back;
- require `HEAD == origin/main`;
- require clean worktree.

## 11. Explicit prohibitions

Do not:

- rerun MATLAB/Python HJB;
- rerun MATLAB/Python KFE;
- rerun MATLAB/Python aggregate evaluators;
- change any accepted HJB/KFE source;
- change aggregate formulas;
- change density bridge/decomposition formulas;
- change tolerances/bounds after observing output;
- run general-equilibrium steady-state loops;
- solve `r*` or `w*`;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- run calibration extension or Results.

If and only if PASS, recommend only the smallest source-backed MATLAB-faithful general-equilibrium steady-state closure gate. Do not authorize it from this task itself.
