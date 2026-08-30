# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resume the immediately preceding MATLAB-faithful stationary-KFE parity gate using the already persisted MATLAB/Python KFE outputs, correct only the comparator JSON-serialization boundary for the NumPy boolean scalar that prevented `comparison.json` persistence, execute exactly one replacement comparator, and close out KFE parity without rerunning HJB or KFE.

This task must not infer PASS from read-only diagnostics. KFE parity is accepted only if one valid persisted replacement comparison passes the unchanged scientific contract.

This task stops before end-to-end own-language stationary aggregates, steady-state equilibrium loops, dynamics, IRFs, calibration extension, or Results.

## 2. Controlling authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_REPORT.md`

Accepted HJB authorities remain frozen:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`

Primary scientific authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Predecessor terminal:

`MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_BLOCKED`

## 3. Live continuity

Task-authoring parent observed before publication:

`e238331588b5b60a7f803cc446b76c820de0cc85`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is on live `main` as a direct child of the predecessor report commit;
3. verify clean worktree;
4. verify predecessor report and accepted HJB source/report identities;
5. verify no KFE scientific source has drifted on `main` because the predecessor restored the unaccepted KFE candidate before reports-only closeout.

Do not begin from uncommitted scientific changes.

## 4. Frozen predecessor KFE evidence — reuse only

Predecessor artifact root:

`D:\ProjectTemp\ch5-kfe-same-operator-20260830-001`

Frozen common input:

- accepted MATLAB post-convergence `A_post` only;
- common operator NPZ/MAT hashes `7A2ADC63...2C0F` / `2D4B8795...C3C8`;
- grid/order manifest `A851FF804E080F3EE302185E4CACE4D6EA61F595EBFCDCCE7D1115E3FA37B235`;
- shape `(5,5,2)` in faithful MATLAB/Fortran `(b,a,z)` order;
- `db=0.25`;
- `da=0.5`;
- `db*da=0.125`;
- contaminated row: MATLAB one-based 18 / Python zero-based 17;
- RHS value: `0.007`.

Persisted scientific outputs:

- MATLAB KFE output SHA-256 `A53B304C134A909D99F1911983F8CB273AC295AEFF1A7DBBC9CFE621401F44E8`;
- Python KFE output SHA-256 `DF97F38C48CB46B5BC871DCB036B0AD3336DB17BC897A4921B8DEEA148AA98A7`.

Preserved predecessor candidate identities:

- faithful KFE source `27DA91779788E76C9F92697247FFF520D460CB9CCAFAC2DE39CDCFF7440A3E88`;
- test `578DC75064C52A312EE1220A0FEADAB450B13BA855A436924A04D7FC6163E728`;
- MATLAB evaluator `C24FC39D...F644`;
- Python runner `7C0A0B3D...4E3A`;
- predecessor comparator `516E6B4D...5F2`;
- final predecessor ledger `C623AAD0E807F790B3F86A9631C128887DC49C1EB417DFEDAEA1F0C5ACA09F8D`.

Read-only predecessor diagnostics:

- MATLAB normalization factor `0.019701654849757503`;
- Python normalization factor `0.019701654849757506`;
- MATLAB raw contaminated residual infinity norm `8.673617379884035e-19`;
- Python raw contaminated residual infinity norm `2.168404344971009e-18`;
- raw normalized-density maximum difference `4.440892098500626e-16`;
- MATLAB normalization error `0`;
- Python normalization error `2.220446049250313e-16`;
- negative-count diagnostic MATLAB `0`, Python `5`.

These values are diagnostics only until the replacement comparator persists a valid decision.

## 5. Scientific execution budget

Exactly:

- MATLAB HJB: `0`;
- Python HJB: `0`;
- MATLAB KFE: `0`;
- Python KFE: `0`;
- replacement comparator: at most `1`.

Do not rerun any solver.

## 6. Comparator failure audit

Inspect the frozen predecessor comparator and traceback before any correction.

Prove and record:

1. exact exception type and traceback location;
2. exact scalar type that failed JSON persistence, expected to be `numpy.bool_` or another NumPy boolean scalar;
3. exact key/path in the result payload containing it;
4. whether every scientific comparison and PASS/MATERIAL aggregation completed before persistence;
5. every NumPy scalar type that can reach the persisted payload;
6. whether any ndarray or non-scalar object can reach the payload;
7. that no field list, tolerance, direct-system check, solver-propagation check, density normalization rule, diagnostic/non-veto rule, or PASS/FAIL logic needs modification.

Only if the failure is strictly persistence-only, freeze:

`KFE_COMPARATOR_NUMPY_SCALAR_JSON_SERIALIZATION_ONLY`

Otherwise stop BLOCKED. Do not modify comparator logic.

The predecessor in-memory decision, if recoverable, is not acceptance evidence.

## 7. Serialization-only correction

Create a new comparator artifact. Do not overwrite the predecessor comparator.

The correction must be limited to JSON serialization type normalization. Prefer one narrow `default=` callback such as:

```python
if isinstance(obj, np.generic):
    return obj.item()
raise TypeError(...)
```

but use this form only after the static audit proves that all NumPy objects reaching the payload are scalar `np.generic` values and that no ndarray conversion is needed.

Every changed line must be classified:

`KFE_COMPARATOR_JSON_SERIALIZATION_TYPE_NORMALIZATION_ONLY`

Do not change:

- common operator;
- contaminated row or RHS;
- transpose;
- solve vectors;
- normalization formula;
- density values;
- comparison fields;
- tolerances;
- exact-zero sparse normalization;
- backward-error certificate;
- diagnostic/non-veto classification;
- mismatch aggregation;
- PASS/MATERIAL logic.

## 8. No-science serializer preflight

Before the one replacement comparator, freeze/hash:

- predecessor comparator;
- corrected comparator;
- exact comparator diff;
- serialization audit;
- serializer preflight;
- both persisted KFE output hashes;
- common operator identity;
- grid/order/spacing manifest;
- unchanged KFE parity contract;
- successor execution ledger.

Run exactly one no-science serializer preflight. It must prove:

- native Python `bool/int/float` remain unchanged;
- `np.bool_` becomes the identical native boolean;
- every other NumPy scalar type actually present in the frozen payload becomes the identical native scalar;
- unsupported ndarray/non-scalar objects remain fail-closed unless the frozen payload demonstrably requires an already-authorized non-scalar serialization path;
- the result payload before/after scalar conversion is scientifically identical;
- no comparison field/order/value/mismatch/PASS logic changes.

If the preflight fails, stop BLOCKED and do not consume comparator budget.

## 9. Replacement comparator

Run the corrected comparator exactly once against the already persisted MATLAB/Python KFE outputs.

Do not rerun MATLAB or Python KFE under any circumstance in this task.

The replacement comparator must preserve the predecessor KFE contract, including:

### Direct construction parity

Use the frozen direct rule:

`128*eps64*max(1,abs(x),abs(y))`

for source-local/direct objects, including:

- common `A` identity;
- `A.T`;
- contaminated row index;
- contaminated matrix;
- RHS;
- `db`, `da`, `db*da`;
- normalization formula inputs and same-input replay.

Exact stored zeros may be ignored only by dropping exact `0.0/-0.0` on copies. No threshold pruning.

### Independent contaminated solves

Retain the frozen backward-error certificate:

`residual_inf <= 256*eps64*max(1, ||M_system||_inf*||x||_inf, ||rhs||_inf)`

for each language's raw contaminated solve.

The cross-language raw solution/density does not require last-bit equality if and only if:

1. both solve the identical contaminated system and RHS;
2. both backward-error certificates pass;
3. both raw solutions are finite;
4. both use exactly `sum(raw_g)*db*da` normalization;
5. same-input normalization replay passes the direct machine bound;
6. normalized density satisfies its normalization identity;
7. every cross-language difference is attributable only to independent direct-solver floating propagation;
8. material mismatch list is empty;
9. unresolved scientific residual list is empty.

If these hold, residual density differences may be classified only:

`KFE_DIRECT_SOLVER_PROPAGATED_DIAGNOSTIC_DIFFERENCE`.

### Diagnostic-only quantities

The following remain non-vetoing unless the designated MATLAB production algorithm itself uses them as a veto:

- SCC/recurrent classes;
- nullity;
- unmodified `A.T @ g` residual;
- minimum density;
- negative-density count;
- pin sensitivity;
- clean-KFE mass-conservation diagnostics.

In particular, the predecessor read-only negative-count difference `0` versus `5` must be persisted and explained, but it is not by itself a faithful-production mismatch under this same-operator contaminated-row task.

## 10. Terminal decision and repository closeout

If replacement comparator completes and all faithful KFE gates pass, freeze:

- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_KFE_DENSITY_PARITY_ACCEPTED`

Terminal:

`MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_PASS`

On PASS:

1. restore the predecessor faithful KFE source and test **byte-identically** from preserved artifacts;
2. require their SHA-256 to equal exactly:
   - source `27DA91779788E76C9F92697247FFF520D460CB9CCAFAC2DE39CDCFF7440A3E88`;
   - test `578DC75064C52A312EE1220A0FEADAB450B13BA855A436924A04D7FC6163E728`;
3. do not modify accepted HJB files;
4. write successor report;
5. stage only faithful KFE source/test and successor report;
6. commit once;
7. non-force push once;
8. GitHub read-back all published paths;
9. require `HEAD == origin/main` and clean worktree.

If the comparator completes with a genuine scientific mismatch, terminal:

`MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_MATERIAL_MISMATCH`

If serialization/source/environment blocks persistence again, terminal:

`MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_BLOCKED`

On MATERIAL/BLOCKED:

- preserve artifacts externally;
- do not publish unaccepted KFE source/test;
- publish successor report only;
- require clean worktree.

## 11. Required successor report

Write:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`

Include at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. predecessor KFE report identity;
4. persisted MATLAB/Python KFE output hashes;
5. exact comparator failure audit;
6. corrected comparator hash/diff;
7. no-science preflight result;
8. exact `0/0/0/0/1` scientific/comparator call ledger;
9. complete KFE parity summary;
10. contaminated system/RHS identity;
11. backward-error certificates;
12. normalization factors/errors;
13. maximum raw/density difference;
14. diagnostic-only negative counts and unmodified stationarity diagnostics;
15. material mismatch list;
16. unresolved scientific residual list;
17. changed paths;
18. git closeout evidence;
19. acceptance level;
20. exact recommended next gate.

## 12. Prohibitions

Do not:

- rerun MATLAB/Python HJB;
- rerun MATLAB/Python KFE;
- change common `A`;
- change contaminated row/RHS;
- change normalization;
- change tolerances/backward-error contract;
- convert diagnostic-only quantities into a new veto;
- modify accepted HJB source;
- modify clean/reference `kfe.py`;
- run end-to-end stationary aggregates;
- compute/accept final `C^ss,L^ss,A^ss,B^ss`;
- run steady-state equilibrium loops;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- run calibration extension or Results.

If and only if PASS, recommend only:

**MATLAB-faithful end-to-end stationary distribution and household aggregate parity using each language's own accepted post-convergence operator, including the requested `C^ss`, `L^ss`, `A^ss`, `B^ss` comparison table.**
