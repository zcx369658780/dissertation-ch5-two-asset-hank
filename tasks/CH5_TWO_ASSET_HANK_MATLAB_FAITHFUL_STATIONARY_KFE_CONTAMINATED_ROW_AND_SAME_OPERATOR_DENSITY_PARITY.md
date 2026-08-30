# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Implement the designated MATLAB **stationary KFE contaminated-row solve** as a distinct MATLAB-faithful Python route and establish MATLAB/Python density parity on the **same accepted post-convergence HJB operator**.

This task begins only because the full faithful HJB/operator route is now accepted under:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`

The target is the exact working MATLAB numerical algorithm, including its contaminated-row linear solve and `db*dah` density normalization. The clean/recurrent-class Python KFE remains reference/diagnostic only and must not replace or veto the faithful production route.

This task isolates the **KFE algorithm itself** by feeding MATLAB and Python the exact same frozen post-convergence operator. It does not yet accept own-language end-to-end stationary aggregates `C,L,A,B`, steady state, dynamics, or Results.

## 2. Controlling accepted authority

Read and obey at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_MATERIAL_MISMATCH_ROOT_CAUSE_DECOMPOSITION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_REPORT.md`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Required KFE authority:

`MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_SOLVE_IS_REQUIRED`

Historical clean/corrected evidence remains:

`CORRECTED_EQUATION_RECONSTRUCTION_TRACK_ACCEPTED_REFERENCE_EVIDENCE`

The clean KFE diagnostics (recurrent classes, nullity, unmodified stationary residual, nonnegativity, clean normalization) are diagnostic/reference evidence only in this faithful gate.

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`886503fb6c912f534fc5d5e0f492586eb45b1d7d`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` and is a direct child of the accepted HJB commit;
3. verify the accepted faithful source modules exist and have not drifted;
4. verify all designated MATLAB hashes;
5. verify a clean worktree;
6. do not begin from uncommitted scientific changes.

Accepted faithful source paths now on `main` include:

- `src/ch5_two_asset_hank/matlab_faithful_policy.py`
- `src/ch5_two_asset_hank/matlab_faithful_operator.py`
- `src/ch5_two_asset_hank/matlab_faithful_hjb.py`

Do not modify those modules in this task unless a source-proven interface defect makes KFE consumption impossible. If so, stop BLOCKED rather than broadening scope.

## 4. Designated MATLAB source identity and exact KFE authority

Designated MATLAB root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Required identity:

- `HANK_2ASSETS_HJB.m` SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

Also reverify the already-controlled helper hashes if read during execution.

The designated stationary solve to reproduce is:

```matlab
A = BB + AAH + Bswitch;
M = I*J*Nz;
AT = A';
vec = zeros(M,1);
iFix = floor(0.37*M);
vec(iFix) = 0.007;
AT(iFix,:) = [zeros(1,iFix-1),1,zeros(1,M-iFix)];
g_stacked = AT\vec;
g_sum = g_stacked'*ones(M,1)*db*dah;
g_stacked = g_stacked./g_sum;
```

Freeze the interpretation exactly:

- KFE consumes the **post-convergence** `A=BB+AAH+Bswitch`, not the HJB iteration operator;
- `AT=A'` is formed before row contamination;
- MATLAB one-based `iFix=floor(0.37*M)` maps to Python zero-based row `iFix-1`;
- RHS is exactly `0.007` at the contaminated row and zero elsewhere;
- the entire contaminated row is replaced by the corresponding unit row;
- solve the full `M x M` system directly;
- do not restrict to a recurrent class;
- do not use a nullspace/eigenvector method;
- normalize the **density** by `sum(g_stacked)*db*dah`;
- do not use trapezoidal endpoint weights;
- do not use a productivity quadrature weight;
- do not normalize a probability-mass vector by `sum(mass)=1` and then divide by cell weights as a substitute.

Do not alter `0.37`, `0.007`, `db*dah`, row choice, or solve form.

## 5. Mandatory MATLAB source/KFE audit before implementation

Before Python mutation, document exact source locations and verify:

- the `A` used at KFE entry is the post-convergence reconstruction, not the iteration `A`;
- `M=I*J*Nz` and the vector ordering are the accepted MATLAB `(b,a,z)` / Fortran ordering;
- `db` and `dah` are uniform grid spacings;
- no `dz`, z-probability, trapezoid half-weight, or other quadrature factor enters `g_sum`;
- `iFix=floor(0.37*M)` is valid for the frozen 50-state fixture (`M=50`, MATLAB `iFix=18`, Python row index `17`);
- post-convergence `A` is passed literally into `AT=A'` even if diagnostic row-sum or sign properties are not those of the clean Python KFE contract.

If designated source differs from the frozen formula above, stop BLOCKED and return the exact discrepancy.

## 6. Distinct faithful Python KFE architecture

Implement a distinct module, preferably:

`src/ch5_two_asset_hank/matlab_faithful_kfe.py`

Do not repurpose or modify:

- `src/ch5_two_asset_hank/kfe.py`
- `src/ch5_two_asset_hank/kfe_contract.py`
- corrected/reference steady-state code.

Suggested explicit API:

```python
solve_matlab_faithful_stationary_kfe(
    post_convergence_operator,
    *,
    shape,
    db,
    da,
)
```

The faithful result should expose enough auditable objects to compare MATLAB and Python, including at minimum:

- original post-convergence `A` identity/reference;
- `A.T` before contamination;
- contaminated row index in Python zero-based form;
- contaminated matrix;
- RHS vector;
- raw direct-solve vector before normalization;
- raw normalization factor;
- normalized density vector;
- normalized density reshaped in faithful `(b,a,z)` logical order;
- `db`, `da`, and `db*da`;
- solver residual for the **raw contaminated linear system** as diagnostic evidence.

No route flag, environment switch, or hidden mode selector.

## 7. Faithful diagnostics are non-vetoing unless source-required

The following may be computed and reported, but MUST NOT replace or automatically reject a source-faithful contaminated-row result merely because a clean mathematical KFE diagnostic is imperfect:

- SCC/recurrent-class count;
- left-nullity;
- unmodified `A.T @ g` residual;
- pin sensitivity;
- density minimum / negative-entry count;
- clean mass-conservation checks;
- clean `sum(mass)=1` comparison.

These are `DIAGNOSTIC_ONLY` in this route.

Finiteness of required source outputs and successful linear solve are still necessary for PASS.

## 8. Engineering tests before scientific KFE parity

Add narrowly scoped tests, preferably:

`tests/test_matlab_faithful_kfe.py`

Required engineering tests before any scientific KFE batch:

1. exact MATLAB/Python index mapping for representative `M`, including `M=50 -> MATLAB iFix=18 -> Python index=17`;
2. contaminated row is exactly a unit row and all other rows are unchanged from `A.T`;
3. RHS has exactly one nonzero equal to `0.007`;
4. a small synthetic full system reproduces an independently constructed contaminated solve;
5. normalization satisfies `sum(density)*db*da = 1` to machine precision;
6. no z weight or trapezoid factor is introduced;
7. shape/Fortran-order reshape roundtrip is exact;
8. clean `kfe.py` remains unchanged and separately importable;
9. predecessor faithful HJB primitive/local-policy imports remain valid.

Do not run a converged HJB in these tests.

## 9. Same-operator scientific parity object

This gate must isolate KFE by using **one exact common post-convergence operator** as input to both languages.

Use the accepted final HJB acceptance artifact root:

`D:\ProjectTemp\ch5-hjb-propagation-aware-final-20260830-001`

Required accepted HJB identities:

- accepted MATLAB HJB output SHA-256 `7351351B5D0F7012F03CB6A8CB79A6E31D8FC65FF5D7C26B4A241047F1B5DE94`;
- accepted Python HJB output SHA-256 `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`;
- fixture `5 b x 5 a x 2 z = 50 states`;
- same accepted ordering/initialization/parameter manifest from the HJB gate.

The **common KFE operator authority** for this task is the accepted MATLAB post-convergence `A` from that accepted HJB output, serialized losslessly as sparse coordinates/values plus shape and hash before any KFE execution.

Reason: same-operator comparison isolates contaminated-row KFE implementation and linear algebra from the already-understood HJB fixed-point solver propagation.

Do not regenerate either HJB.

Freeze marker:

`MATLAB_FAITHFUL_KFE_SAME_POST_CONVERGENCE_OPERATOR_INPUT_FROZEN`

Before KFE execution, verify that the common operator's ordering and state count match the faithful Python HJB ordering contract exactly.

## 10. External MATLAB KFE-only evaluator

Create a fresh external evaluator that:

- loads only the frozen common post-convergence `A`, `I`, `J`, `Nz`, `db`, and `dah`;
- performs exactly the designated contaminated-row KFE block;
- stops after normalized density and authorized diagnostics;
- does not rerun HJB;
- does not execute aggregates beyond normalization;
- does not execute dynamics.

Evidence label:

`MATLAB_SOURCE_EXTRACTED_CONTAMINATED_ROW_KFE_SAME_OPERATOR_PARITY`

Do not modify designated MATLAB source.

## 11. Pre-freeze artifacts and scientific call budget

Use a fresh no-overwrite artifact root.

Before either KFE scientific solve, freeze/hash/read back:

- common post-convergence operator sparse artifact;
- shape/order/grid-spacing manifest;
- MATLAB KFE-only evaluator;
- Python faithful KFE source;
- Python KFE runner;
- comparator;
- acceptance contract;
- engineering-test evidence;
- execution ledger.

Scientific call budget after freeze:

- MATLAB HJB: `0`;
- Python HJB: `0`;
- MATLAB KFE batch: at most `1`;
- Python faithful KFE batch: at most `1`;
- comparator: at most `1`.

No reruns or post-output repairs in the same task.

## 12. KFE parity acceptance contract

### 12.1 Direct construction objects

Require exact identity or the unchanged direct machine rule where floating representation requires it:

`128*eps64*max(1,abs(x),abs(y))`

for:

- common `A` sparse support and values;
- `A.T` support/values;
- contaminated row index;
- contaminated matrix support/values;
- RHS support/values;
- `db`, `da`, `db*da`;
- normalization formula inputs.

Exact stored-zero differences may be canonicalized only by dropping exact `0.0/-0.0` on copies, consistent with the accepted HJB mathematical-support contract. No threshold pruning.

### 12.2 Independent direct linear solve outputs

MATLAB backslash and SciPy sparse direct solve may differ at last bits despite solving the same frozen system.

Do not invent a broad raw-density tolerance.

Normalized density parity may PASS only if all are true:

1. common contaminated matrix and RHS pass the direct construction gate;
2. both raw solve vectors are finite;
3. each raw solution satisfies its own contaminated linear system with a machine-level backward-error certificate;
4. both use the exact same `db*da` normalization formula;
5. both normalized densities satisfy `sum(g)*db*da = 1` to a machine-level normalization certificate;
6. a same-input replay of normalization arithmetic passes the direct machine rule;
7. any remaining cross-language raw-solution/density difference is attributable solely to independent sparse direct-solver propagation;
8. no branch/index/row/RHS/normalization mismatch exists;
9. complete material mismatch list is empty;
10. complete unresolved scientific residual list is empty.

Recommended machine-level backward-error certificate for raw contaminated solve:

```text
residual_inf <= 256*eps64*max(1, ||M||_inf*||x||_inf, ||rhs||_inf)
```

where `M` here denotes the contaminated linear-system matrix, not state count. Freeze this exact certificate before execution; do not loosen it after observing output.

If all conditions hold, remaining raw cross-language density differences may be classified:

`KFE_DIRECT_SOLVER_PROPAGATED_DIAGNOSTIC_DIFFERENCE`

They are not a parity failure.

If either solver cannot meet the frozen backward-error certificate, return MATERIAL_MISMATCH or BLOCKED according to whether the issue is scientific mismatch versus source/environment failure. Do not tune the certificate.

## 13. Comparator objects

Compare and persist at minimum:

- state count and `(I,J,Nz)`;
- ordering identity;
- common `A` identity;
- transpose identity;
- MATLAB/Python contaminated row index;
- contaminated matrix mathematical support and values;
- RHS;
- raw solve vector;
- raw contaminated-system residual/backward-error metric;
- raw normalization factor;
- normalized density vector;
- normalized density reshaped `(b,a,z)`;
- density normalization error;
- minimum/maximum density and negative-entry count as diagnostics;
- unmodified `A.T @ normalized_density` residual as diagnostic only;
- all exact-zero representation differences separately from mathematical support.

Do not compare or accept `C,L,A,B` household aggregates in this gate.

## 14. Repository mutation scope

Authorized production mutation:

- new `src/ch5_two_asset_hank/matlab_faithful_kfe.py`

Authorized tests:

- new `tests/test_matlab_faithful_kfe.py`

Required report:

- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_REPORT.md`

Do not modify corrected/reference `kfe.py` or steady-state modules.

If parity is not PASS, preserve candidate artifacts externally, restore unaccepted production/test paths, and publish report-only unless an independently accepted source path exists.

## 15. Explicit prohibitions

Do not:

- rerun MATLAB HJB;
- rerun Python HJB;
- change the accepted HJB source;
- change the common post-convergence operator;
- change row `floor(0.37*M)`;
- change RHS `0.007`;
- change `db*dah` normalization;
- substitute clean recurrent-class/nullspace KFE;
- use trapezoid/productivity quadrature normalization;
- use diagnostic SCC/nullity/residual/nonnegativity as a production veto unless source-required;
- run own-language end-to-end stationary aggregates;
- compute/accept `C,L,A,B` as final steady-state parity yet;
- run steady-state equilibrium loops;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- run calibration extension;
- run Results.

## 16. Terminal classifications

Return exactly one:

### PASS

`MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_PASS`

Use only if the faithful contaminated-row construction and same-operator normalized density parity pass every frozen gate.

### MATERIAL MISMATCH

`MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_MATERIAL_MISMATCH`

Use if both KFE objects are valid but a frozen scientific construction/density parity condition fails.

### BLOCKED

`MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_BLOCKED`

Use for missing/corrupt accepted artifacts, source identity contradiction, failed engineering/pre-freeze requirements, or source/environment failure preventing valid comparison.

## 17. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_REPORT.md`

Include at minimum:

1. terminal classification;
2. live start/final GitHub SHA;
3. designated source identity and exact KFE lines/formulas;
4. accepted HJB source/output identities;
5. exact common post-convergence operator identity;
6. exact `M`, MATLAB `iFix`, Python row index, RHS, `db`, `da`, normalization measure;
7. faithful Python implementation/hash;
8. engineering tests;
9. MATLAB/Python KFE call ledger;
10. contaminated-system construction parity;
11. raw-solve residual/backward-error certificates;
12. raw density maximum difference and worst index;
13. normalized density maximum difference and worst index;
14. normalization factors/errors;
15. exact-zero representation diagnostics;
16. nonnegativity/unmodified-stationarity/SCC/nullity diagnostics clearly labeled non-vetoing;
17. complete material mismatch list;
18. complete unresolved list;
19. source/environment failure list;
20. changed paths;
21. git status;
22. acceptance level;
23. exact recommended next gate.

## 18. Next gate boundary

If and only if PASS, recommend only:

**MATLAB-faithful end-to-end stationary distribution and household aggregate parity using each language's accepted post-convergence operator, including the requested `C^ss`, `L^ss`, `A^ss`, and `B^ss` comparison table.**

Do not authorize dynamics from this KFE task alone.
