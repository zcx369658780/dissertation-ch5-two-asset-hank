# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_AND_TRANSFER_VALIDATION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / export integrator

Owner: final scientific authority

## 1. Purpose

Package the already accepted MATLAB-faithful **two-asset heterogeneous-agent household block** into one self-contained Python file that can be transferred to a separate Deep Learning + HA research project and used as a numerical baseline/oracle.

The exported file must reproduce the accepted modular Python household implementation without changing economics, numerics, ordering, boundary behavior, sparse placement, KFE normalization, or stationary aggregate definitions.

This is an **export / transfer-validation task**, not a new scientific redesign and not a GE task.

The deliverable target is exactly one transferable implementation file:

`exports/matlab_faithful_two_asset_ha.py`

The file may depend only on Python standard library, `numpy`, and `scipy`. It must not import `ch5_two_asset_hank`, repository-local modules, project configuration, notebooks, cached artifacts, or external data files.

## 2. Controlling accepted authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_REPORT.md`

Accepted household authorities:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`
- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_KFE_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HOUSEHOLD_AGGREGATE_PARITY_ACCEPTED`

Primary numerical authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

The current GE source-audit terminal is deliberately non-blocking for this export:

`MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_OWNER_PROVENANCE_REQUIRED`

The standalone export stops at the accepted household block and MUST NOT embed or infer the unresolved 31-province GE fixed-point closure.

## 3. Live continuity

Task-authoring parent observed before publication:

`115c7b00c777e64a2e00ab79a67f9982f93a9e04`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` as a direct child of the GE source-audit report commit;
3. verify clean worktree;
4. verify all accepted faithful household source/report paths exist;
5. verify the designated MATLAB source hash remains unchanged;
6. record SHA-256 for every modular Python source consumed by the export before writing anything.

Required designated MATLAB source identity:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

## 4. Accepted modular Python source boundary

The export must be assembled only from the accepted household route and the minimum shared primitive contracts/equations it actually depends on.

At minimum inspect and source-map:

- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/matlab_faithful_policy.py`
- `src/ch5_two_asset_hank/matlab_faithful_operator.py`
- `src/ch5_two_asset_hank/matlab_faithful_hjb.py`
- `src/ch5_two_asset_hank/matlab_faithful_kfe.py`

Previously accepted faithful identities to verify from controlling reports:

- faithful policy SHA-256: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`
- faithful operator SHA-256: `0C9F6C1AE3E6428E49086DE900BE55D5038A10144EC061EDDFB9E7249A4A1AAC`
- faithful HJB SHA-256: `924831362C904A253D8AD6011FE9BB4C099C6DF4268D0C2AA30AB9139569F1DE`
- faithful KFE SHA-256: `27DA91779788E76C9F92697247FFF520D460CB9CCAFAC2DE39CDCFF7440A3E88`

If any accepted faithful source identity has drifted from the accepted report, STOP BLOCKED. Do not silently export a new implementation.

Do NOT copy corrected/reference-only machinery that is not needed by the accepted faithful route. In particular, the export must not include or invoke the historical corrected KKT/candidate-selection route as an alternative production solver.

## 5. Required standalone scientific content

The single file must contain all code necessary to evaluate the accepted household block, including the minimum validated dataclasses and helpers needed for:

### 5.1 Inputs/contracts

Provide standalone equivalents of the accepted types needed by the faithful solver, including at minimum:

- `EconomicParams`
- `HouseholdInputs`
- `MatlabFaithfulHJBGrid`
- `MatlabFaithfulHJBNumerics`

Do not include unused corrected/reference contract structures merely because they exist in the package.

### 5.2 Faithful household primitives

Include source-identical accepted logic for:

- adjustment cost with `max(a,a_bar)` denominator floor;
- bare-`a` transfer FOC;
- MATLAB illiquid-return taper `r_a*(1-0.1*(a/a_max)^9)`;
- consumption FOC;
- labor FOC;
- flow utility;
- MATLAB-faithful asset drifts.

Freeze these authority markers in the module-level provenance documentation:

- `MATLAB_FAITHFUL_TRANSFER_FOC_USES_BARE_A`
- `MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`

### 5.3 Faithful local policy/upwind block

Include the accepted local policy selector, including:

- derivative floor `1e-6`;
- drift tolerance `1e-12`;
- liquid B/F/0 selection;
- four bare-a transfer candidates;
- lower/upper `a` boundary behavior;
- lower/upper `b` behavior, including MATLAB upper-b forced backward transfer branch;
- iteration liquid coefficients;
- post-convergence `mu_a/mu_b` controls.

Do not simplify branches or rewrite them into a different candidate/KKT algorithm.

### 5.4 Faithful sparse HJB assembly

Include exact accepted MATLAB-spdiags-equivalent source placement:

- Fortran/MATLAB `(b,a,z)` flattening;
- signed iteration components;
- outward-boundary truncation without re-closing the diagonal;
- `Bswitch = kron(switch_matrix, I)`;
- full iteration operator `BB + AAH + Bswitch`;
- post-convergence operator built separately from final `mu_b/mu_a`.

Freeze:

- `MATLAB_FAITHFUL_HJB_ITERATION_OPERATOR_FOLLOWS_EXACT_SPDlAGS_BOUNDARY_TRUNCATION`
- `MATLAB_FAITHFUL_HJB_ITERATION_BB_MAY_HAVE_SIGNED_OFFDIAGONALS_AND_NONZERO_BOUNDARY_ROW_SUMS`

### 5.5 Faithful HJB driver

Include the accepted implicit HJB driver with unchanged:

- derivative construction and boundary derivatives;
- local-policy call ordering;
- `(1/Delta + rho)I - A` system;
- RHS `u + V/Delta`;
- sparse direct solve;
- convergence statistic `max(abs(V_new-V_old))`;
- separate post-convergence operator.

Do not add GE logic or change convergence behavior.

### 5.6 Faithful stationary KFE

Include the accepted contaminated-row KFE:

- input is post-convergence full `A`;
- `AT = A.T`;
- MATLAB one-based `iFix=floor(0.37*M)` mapped to Python zero-based `floor(0.37*M)-1`;
- RHS exactly `0.007` at the contaminated row;
- exact unit-row replacement;
- full direct solve;
- normalization exactly `sum(raw_g)*db*da`;
- Fortran reshape `(b,a,z)`.

Freeze:

- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_SOLVE_IS_REQUIRED`

Do not substitute clean/recurrent-class KFE logic.

### 5.7 Stationary household aggregates

Provide a standalone aggregate helper implementing the already source-audited MATLAB formulas exactly:

- `C_ss = sum(C * g * da * db)`;
- `L_ss = sum(z * l * g * da * db)`;
- `A_ss = sum(a_grid * g * da * db)`;
- `B_ss = sum(b_grid * g * da * db)`;
- `total_assets = A_ss + B_ss`.

Use faithful `(b,a,z)` broadcasting/order.

No `dz`, productivity-probability, trapezoid, or endpoint weights are allowed.

Make explicit in docstrings that `L_ss` is productivity-weighted effective household labor, not the 31-province migration/firm labor supply used by the unresolved GE outer block.

## 6. Required public transfer API

The single file must expose a small stable API suitable for a separate research repository.

At minimum expose:

- `solve_matlab_faithful_hjb(...)`
- `solve_matlab_faithful_stationary_kfe(...)`
- `aggregate_stationary_household(...)`
- one convenience wrapper named exactly:

`solve_household_steady_state(...)`

The convenience wrapper must:

1. run the faithful HJB;
2. require HJB convergence or fail explicitly;
3. run faithful KFE on the HJB post-convergence operator;
4. compute `C_ss`, `L_ss`, `A_ss`, `B_ss`, total assets;
5. return an auditable result object containing HJB, KFE, and aggregates.

Do not hide numerical settings or silently choose calibration values.

The wrapper must require the caller to provide all economic inputs, grids, initial value, baseline labor, transfer income, borrowing-rate gap, and HJB numerical settings required by the accepted solver.

## 7. Provenance header

The top of `exports/matlab_faithful_two_asset_ha.py` must contain a concise scientific provenance block stating:

- designated MATLAB source path and SHA-256;
- source repository name;
- export task authority commit;
- accepted HJB/KFE/end-to-end household parity markers;
- statement that the file is a faithful numerical baseline/oracle, not a redesigned solver;
- statement that GE closure and dynamics are intentionally excluded;
- dependency requirement: Python + NumPy + SciPy only.

Do not put credentials, local personal paths other than the scientific MATLAB provenance path, or transient ProjectTemp paths into the transferable file.

## 8. Static single-file dependency audit

Before numerical testing, prove:

1. the export contains no relative imports;
2. the export contains no `ch5_two_asset_hank` import;
3. the export contains no repository-path import or file read;
4. the export contains no MATLAB-engine dependency;
5. the export contains no pandas, matplotlib, torch, jax, tensorflow, numba, or project-specific dependency;
6. only standard-library, `numpy`, and `scipy` imports remain;
7. `python -m py_compile exports/matlab_faithful_two_asset_ha.py` passes.

Freeze:

`MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_DEPENDENCY_AUDIT_PASS`

If any hidden project dependency remains, do not proceed to acceptance testing.

## 9. Clean-room import validation

Create a fresh no-overwrite temporary directory outside the repository.

Copy ONLY:

`matlab_faithful_two_asset_ha.py`

into that directory.

From that directory, with repository root and `src` removed from `PYTHONPATH`, verify in a fresh Python process:

- import succeeds;
- public API symbols are present;
- no local package is imported as a side effect.

Freeze:

`MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_CLEAN_ROOM_IMPORT_PASS`

## 10. Numerical transfer validation

This task is allowed to execute the **standalone Python household solver only** for validation. Do not run MATLAB.

Reuse the already accepted 50-state final HJB fixture and frozen scientific inputs from the accepted artifact chain. Do not invent a new calibration.

Required accepted reference evidence includes:

- final Python faithful HJB accepted output SHA-256: `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`;
- final HJB convergence: `12` iterations;
- accepted stationary household aggregates:
  - `C_ss = 1.1296890749136979` (Python accepted end-to-end value);
  - `L_ss = 0.7341069339182127`;
  - `A_ss = 0.44059476682729026`;
  - `B_ss = 0.4601208223181049`;
  - `A_ss+B_ss = 0.9007155891453952`.

Important: the accepted aggregate values were generated using each language's own accepted post-convergence operator and faithful KFE. The standalone Python export must reproduce the accepted **Python** path.

### 10.1 Call budget

- MATLAB HJB/KFE/aggregate: `0`
- modular Python HJB/KFE/aggregate scientific rerun: `0` unless strictly needed for a packaging-only diagnostic preflight; prefer persisted accepted artifacts
- standalone Python end-to-end household solve: exactly `1` scientific validation run
- standalone validation comparator: exactly `1`

Do not rerun after observing output. Any correction after the scientific validation run requires a new exact task.

### 10.2 Same-runtime packaging parity

The standalone implementation is a packaging of the same accepted Python algorithm. Therefore require exact same-runtime parity against persisted accepted Python artifacts wherever representation allows.

Comparator must check at minimum:

- grid and ordering;
- initial value;
- HJB converged flag;
- iteration count exactly `12`;
- convergence statistic;
- `V`;
- consumption;
- labor;
- transfer;
- adjustment cost;
- effective illiquid return;
- `mu_a`, `mu_b`, utility;
- liquid/transfer labels;
- iteration `BB`, `AAH`, `Bswitch`, full `A`;
- post-convergence `BB`, `AAH`, full `A`;
- contaminated-row index/matrix/RHS;
- raw KFE solve;
- normalization factor;
- density;
- `C_ss`, `L_ss`, `A_ss`, `B_ss`, total assets.

For objects produced by the same Python arithmetic and solver path, require exact equality or byte-identical serialized representation where feasible. If exact equality fails solely because of sparse explicit `0.0/-0.0` storage, canonicalize only exact stored zero on copies and report the raw representation difference.

Do not introduce broad tolerances to make the export pass.

If a non-representation numerical difference appears between standalone and accepted modular Python, terminal is MATERIAL MISMATCH; do not repair/re-run within this task.

### 10.3 MATLAB evidence sanity check

Do not run MATLAB. Report that the standalone output remains covered transitively by the already accepted MATLAB/Python parity authorities only if standalone-to-accepted-Python parity passes.

Do not claim a new MATLAB call or new MATLAB parity experiment.

## 11. Required tests

Add one focused repository test file:

`tests/test_matlab_faithful_two_asset_ha_standalone_export.py`

It must test at minimum:

- static import boundary;
- public API presence;
- clean-room import helper or equivalent subprocess test;
- bare-a transfer FOC at `a=0` returns zero candidate;
- illiquid-return taper endpoints/interior;
- source-axis boundary truncation behavior;
- contaminated-row mapping for `M=50` gives zero-based `17`;
- KFE normalization identity;
- aggregate helper weighting/order on a small deterministic synthetic fixture;
- no GE/dynamics API is exported.

The test may import the export file by file path/module loader; it must not make the export depend on the package.

Run the focused tests and any accepted faithful household regression tests necessary to prove no existing household source was changed.

No source mutation is authorized in accepted modular HJB/KFE files.

## 12. Transfer artifact identity

After all tests pass, record:

- SHA-256 of `exports/matlab_faithful_two_asset_ha.py`;
- byte size;
- line count;
- public API list;
- Python/NumPy/SciPy versions used for validation;
- clean-room import command;
- scientific validation artifact SHA-256;
- comparator artifact SHA-256.

Freeze:

`MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_ACCEPTED`

The export should be suitable for direct copying into a separate Deep Learning HA repository as a reference/oracle module.

## 13. Explicit prohibitions

Do not:

- modify designated MATLAB source;
- modify accepted `matlab_faithful_policy.py`;
- modify accepted `matlab_faithful_operator.py`;
- modify accepted `matlab_faithful_hjb.py`;
- modify accepted `matlab_faithful_kfe.py`;
- modify corrected/reference production files merely to support export;
- include GE fixed-point logic;
- choose a Chapter 5 baseline year;
- resolve the GE provenance blocker;
- run GE residual-map parity;
- run GE steady-state iteration;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- add neural networks or Deep Learning code;
- optimize/vectorize/refactor in a way that changes accepted arithmetic order;
- make the standalone file import the source package;
- require local data files at runtime.

## 14. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_AND_TRANSFER_VALIDATION_REPORT.md`

The report must include:

1. terminal classification;
2. live start/final `origin/main`;
3. modular source identities and dependency map;
4. exact export source mapping;
5. provenance header audit;
6. static dependency audit;
7. clean-room import result;
8. focused test results;
9. exact scientific validation call ledger;
10. standalone-vs-accepted-Python parity summary;
11. HJB/KFE/aggregate regression values;
12. MATLAB parity transitivity statement and limitation;
13. standalone file SHA-256/size/line count/API;
14. changed paths;
15. git closeout evidence;
16. acceptance level;
17. explicit statement that GE provenance remains unresolved and is outside this export.

## 15. Terminal classifications

PASS:

`MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_AND_TRANSFER_VALIDATION_PASS`

On PASS freeze:

- `MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_DEPENDENCY_AUDIT_PASS`
- `MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_CLEAN_ROOM_IMPORT_PASS`
- `MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_ACCEPTED`

MATERIAL:

`MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_AND_TRANSFER_VALIDATION_MATERIAL_MISMATCH`

BLOCKED:

`MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_AND_TRANSFER_VALIDATION_BLOCKED`

## 16. Repository closeout

On PASS, publish only:

- `exports/matlab_faithful_two_asset_ha.py`
- `tests/test_matlab_faithful_two_asset_ha_standalone_export.py`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_AND_TRANSFER_VALIDATION_REPORT.md`

Commit once, non-force push once, GitHub read-back all three paths, require `HEAD == origin/main`, and require clean worktree.

On MATERIAL/BLOCKED, do not publish an unaccepted standalone export as transferable authority. Preserve artifacts externally and publish report-only, then require clean worktree.

No GE or dynamics task is authorized by this export task.
