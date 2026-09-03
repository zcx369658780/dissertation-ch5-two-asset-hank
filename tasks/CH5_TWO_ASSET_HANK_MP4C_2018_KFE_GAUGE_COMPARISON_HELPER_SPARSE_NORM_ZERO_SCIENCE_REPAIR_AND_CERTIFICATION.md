# CH5_TWO_ASSET_HANK_MP4C_2018_KFE_GAUGE_COMPARISON_HELPER_SPARSE_NORM_ZERO_SCIENCE_REPAIR_AND_CERTIFICATION

Date: 2026-09-04

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / zero-science helper-repair executor

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`27c77480516b126c800979e917366853fc5c42e8`

with terminal:

`MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_BLOCKED__NO_PRODUCTION_CHANGE_NO_2018_RERUN`

Accepted predecessor facts:

- the first and only O1/G0 `spsolve` invocation returned to the helper;
- before the solve result could be durably qualified, the helper called `numpy.linalg.norm(M, numpy.inf)` on a SciPy sparse contaminated matrix;
- NumPy raised `ValueError: Improper number of dimensions to norm.`;
- zero qualified density results were produced;
- remaining 7 predeclared gauge/operator pairs were not run;
- there was no retry, no production/model/source change, no 2018 rerun, no HJB/GE/stationary execution.

This is an engineering/helper-layer API defect. It is **not evidence of a model-parameter problem** and does not authorize changing any economic, numerical-model, HJB, KFE, grid, controller, calendar, or tolerance parameter.

## 2. Task type and hard boundary

Task type:

`ZERO_SCIENCE_HELPER_REPAIR__SPARSE_INFINITY_NORM_DIAGNOSTIC_ONLY__NO_KFE_SOLVE`

This task authorizes only repair and certification of the external comparison helper's sparse-matrix infinity-norm / backward-error diagnostic path.

Forbidden:

- any `spsolve` call;
- any KFE-style solve;
- any density solve;
- any HJB, household, stationary, GE, MATLAB, R/PLM, shock, or IRF execution;
- any new scientific PID;
- changing any model/economic/numerical-science parameter;
- modifying production/model/diagnostic/test source in the repository;
- changing G0/G1/G2 gauge definitions;
- changing accepted backward-error formula or multiplier;
- changing accepted density/aggregate tolerances;
- changing the frozen operator suite.

All helper edits and tests must remain in a fresh external evidence root. Only the certification report may be committed to GitHub.

## 3. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `27c77480516b126c800979e917366853fc5c42e8`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read:
   - `AGENTS.md`;
   - all CURRENT project rules;
   - predecessor diagnostic KFE gauge comparison task and blocked report;
   - accepted MATLAB-faithful KFE parity authority needed only to preserve the already-frozen backward-error formula.

## 4. Preserve the frozen scientific contract

The following must remain byte-for-byte / semantically unchanged in the repaired helper:

- G0/G1/G2 definitions;
- operator identities O1/O2/O3;
- cell weights;
- accepted KFE backward-error formula:

`residual_inf <= 256*eps64*max(1, ||M||_inf*||x||_inf, ||rhs||_inf)`;

- accepted density comparison rule;
- accepted aggregate formulas/tolerances;
- solve ordering and solve-budget accounting.

Do not alter any scientific parameter to make the diagnostic pass.

## 5. Root cause to repair

The invalid helper call is:

`numpy.linalg.norm(M, numpy.inf)`

where `M` is a SciPy sparse matrix.

Replace only the matrix-`inf` norm implementation with a sparse-safe deterministic definition equivalent to the dense induced infinity norm:

`||M||_inf = max_i sum_j |M_ij|`.

Preferred implementation pattern:

- ensure `M` is CSR/CSC sparse;
- compute absolute row sums without densifying the scientific matrix;
- convert the resulting row-sum vector to a 1-D finite NumPy array;
- take its maximum as a Python float.

A direct equivalent such as:

`float(np.asarray(abs(M).sum(axis=1)).reshape(-1).max())`

is acceptable if tested and version-compatible.

Do not use a method whose result depends on sparse-matrix object coercion quirks.

Vector norms remain ordinary NumPy vector norms.

## 6. Zero-science synthetic certification

Before touching any frozen scientific operator, create deterministic synthetic sparse matrices only.

At minimum test:

1. a 3x3 matrix with mixed signs;
2. a rectangular matrix if the helper is generic, otherwise a second square matrix;
3. a matrix with a zero row;
4. a matrix with very large and very small coefficients to exercise scale.

For each synthetic matrix compare the repaired sparse-safe infinity norm to:

`numpy.linalg.norm(M.toarray(), numpy.inf)`

Require equality within binary64 roundoff consistent with the exact row-sum arithmetic; record both values and absolute/relative difference.

Also test the full backward-error diagnostic formula on synthetic `M`, `x`, and `rhs`, comparing the sparse-safe helper result to a dense reference calculation.

## 7. No-solve enforcement test

Instrument / monkeypatch the helper environment so any call to:

- `scipy.sparse.linalg.spsolve`;
- any known density/KFE solve entry point;

raises immediately.

Run all zero-science tests under that guard and require solve count = 0.

## 8. Frozen O1 matrix dry diagnostic without solving

Only after synthetic certification passes, load the exact already-frozen O1 operator and construct the O1/G0 contaminated system matrix **without calling `spsolve`**.

Run only the repaired sparse-matrix infinity-norm calculation on that matrix.

Require:

- finite scalar result;
- no exception;
- no dense conversion of the full O1 matrix except, if desired, one bounded cross-check because O1 is only 50x50; if dense cross-check is performed, record it explicitly as zero-science diagnostic and do not solve;
- backward-error threshold scale can be computed symbolically/numerically once placeholder finite synthetic `x`/`rhs` vectors are supplied, but do not reuse or infer the consumed predecessor solve result.

This O1 dry check consumes **zero** gauge-comparison sparse-solve budget.

## 9. Helper integrity regression checks

Confirm the repair changes only helper observability/diagnostic arithmetic.

Specifically verify unchanged:

- matrix construction before solve;
- RHS construction;
- solver call site and arguments;
- post-solve normalization logic;
- negative-mass diagnostics;
- density-comparison formulas;
- aggregate formulas;
- solve-budget ledger semantics.

No new fallback, retry, regularization, or parameter tuning may be introduced.

## 10. Evidence root

Preferred fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-kfe-gauge-helper-sparse-norm-zero-science-repair-20260904-001`

Persist at minimum:

- `authority_identity.json`;
- predecessor helper copy / hash reference;
- repaired helper copy;
- helper diff;
- synthetic_sparse_norm_cases.csv;
- synthetic_backward_error_crosscheck.csv;
- no_solve_guard_receipt.json;
- o1_g0_matrix_norm_drycheck.json;
- helper_integrity_regression.json;
- zero_science_ledger.json;
- stdout/stderr;
- `audit_manifest.json`.

## 11. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_KFE_GAUGE_COMPARISON_HELPER_SPARSE_NORM_ZERO_SCIENCE_REPAIR_AND_CERTIFICATION_REPORT.md`

The report must state explicitly:

- predecessor failure was helper sparse-norm API misuse;
- it was **not** a model-parameter failure;
- no economic/model parameter was changed;
- repaired norm formula;
- synthetic dense-vs-sparse equality results;
- O1 matrix dry-check result;
- solve count = 0;
- no production/source modification;
- no 2018/HJB/GE/KFE solve execution;
- whether the helper is ready for a new gauge-comparison execution task.

## 12. PASS / FAIL

PASS terminal:

`MP4C_2018_KFE_GAUGE_HELPER_SPARSE_NORM_ZERO_SCIENCE_REPAIRED_AND_CERTIFIED__NO_PARAMETER_CHANGE__READY_FOR_FRESH_GAUGE_COMPARISON_EXECUTION_TASK`

On PASS, one report-only commit + push is authorized.

Suggested commit message:

`Certify MP4C KFE gauge helper sparse norm repair`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean.

FAIL terminal:

`MP4C_2018_KFE_GAUGE_HELPER_SPARSE_NORM_ZERO_SCIENCE_REPAIR_BLOCKED__NO_SCIENCE_NO_PARAMETER_CHANGE`

On FAIL, publish the strongest accurate report-only failure if possible and STOP.

## 13. No automatic scientific rerun inside this task

Even after PASS, do not execute O1/O2/O3 gauge solves in this task.

A fresh live GitHub task will separately authorize a new 8-solve diagnostic comparison after L3 review of this zero-science certification.
