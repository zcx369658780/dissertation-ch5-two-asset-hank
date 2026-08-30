# CH5 Two-Asset HANK Owner MP4 Multi-Year / Cache / First-Year Parity Decision

Date: 2026-08-30
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Owner: final scientific authority

## Decision status

`OWNER_MP4_MULTI_YEAR_CACHE_AND_FIRST_YEAR_PARITY_DECISION_ACCEPTED`

The Owner freezes the following route after accepted MP3 manual update-map/controller semantics.

## 1. Active model and year contract

- `OWNER_MP4_FINAL_CONTRACT_MULTI_YEAR_2009_2023`
- `OWNER_MP4_INITIAL_CONTROLLED_ANCHOR_YEAR_2009`
- `OWNER_MP4_SINGLE_YEAR_PARITY_PRECEDES_MULTI_YEAR_BATCH`

The final Chapter 5 annual stationary contract is the fifteen-year 2009-2023 route. The first controlled production-validation anchor is 2009 only. No 2010-2023 batch execution is authorized until the 2009 route has passed its own provenance and MATLAB-Python stationary parity gates.

The exact mapping among source `ii`, workbook calendar-year row, and `Multi_Province_12sts_<year>` filename must be established from source/workbook evidence before any 2009 run. The label `2009` must never be assigned by assumption.

## 2. Calibration authority

- `OWNER_DERIVED_MAT_CALIBRATION_CACHE_NOT_PRIMARY_SCIENTIFIC_AUTHORITY`
- `OWNER_PRIMARY_CALIBRATION_AUTHORITY_SOURCE_WORKBOOKS_REGRESSION_INPUTS_AND_LOAD_GDPDATA_TRANSFORMATION`

`数据估计结果_1000_100_0.mat` is a derived cache, not primary scientific authority. It may be used only for provenance comparison, compatibility checking, or later acceleration after independent source-derived parity.

Primary calibration authority is the identified source workbooks / regression inputs plus the source-defined transformations in `load_GDPdata.m`. Python must reconstruct the annual calibration object from those primary sources rather than silently loading the derived MAT cache as truth.

If a source-reconstructed Python calibration object disagrees with the MAT cache, the discrepancy must be diagnosed; the cache must not automatically override source-derived inputs.

## 3. First-year MATLAB-Python stationary comparison

After provenance resolution, the first scientific production comparison shall use the source-backed 2009 input identity in both MATLAB and Python.

The comparison must include, at minimum, province-level and national diagnostics for the source-relevant stationary objects available from both implementations, including household aggregates, labor/capital allocations, firm quantities/prices/returns, controller convergence/adaptation history, and final steady-state objects.

Numerical differences are not automatically material if they are attributable to already accepted solver/floating propagation and remain within a pre-frozen comparison contract. However, directional/trend agreement is not a substitute for source/formula parity where exact same-input numerical parity is expected.

## 4. Shock/response comparison after stationary acceptance

- `OWNER_FIRST_YEAR_STATIONARY_PARITY_BEFORE_SHOCK_RESPONSE_PARITY`
- `OWNER_2009_MATLAB_NAMED_SHOCK_RESPONSE_COMPARISON_REQUIRED_BEFORE_MULTI_YEAR_RESULTS`

Only after the 2009 stationary route is accepted should the project compare the source-named MATLAB shock/IRF route with the Python reproduction for the same 2009 baseline.

The first response comparison should reproduce the MATLAB source-defined named shock path as a faithful diagnostic route. It must not be mislabeled as a genuine backward-HJB/forward-KFE transition if the source does not implement one.

In addition to numerical comparisons, the response review must explicitly compare qualitative behavior: sign, direction, peak/turning behavior, persistence/decay, province-level spillover direction, and any ranking used later in Chapter 5. Qualitative agreement is a diagnostic layer, not permission to ignore unexplained numerical or structural mismatches.

## 5. Mismatch diagnosis authority

- `OWNER_PARITY_MISMATCH_BOUNDED_ROOT_CAUSE_DIAGNOSIS_AUTHORIZED`

When a controlled MATLAB-Python stationary or named-response comparison produces a mismatch, Codex is authorized within the same parity task to perform a bounded read-only/root-cause diagnosis sufficient to classify the first differing object as one of:

- `PYTHON_IMPLEMENTATION_ERROR`
- `MATLAB_SOURCE_OR_LEGACY_NUMERICAL_BEHAVIOR`
- `DATA_OR_CALIBRATION_PROVENANCE_MISMATCH`
- `SHARED_SOURCE_NUMERICAL_PROPAGATION_DIFFERENCE`
- `SCIENTIFIC_SPECIFICATION_OR_PROVENANCE_AMBIGUITY`

Diagnosis must localize the first divergent stage/object and compare source formulas, inputs, ordering, and persisted intermediates. This authority does **not** authorize automatic scientific repair, formula redesign, tolerance loosening, or an unbounded rerun loop. Any repair/re-execution after diagnosis requires the task's explicit pre-authorized retry clause or a successor task.

## 6. Immediate route

1. MP4A: provenance resolution and 2009 annual-route preparation; zero model solve.
2. MP4B: controlled 2009 MATLAB-Python stationary parity, with bounded mismatch diagnosis if needed.
3. Only after MP4B acceptance: MP5A shock-law/source-role freeze and source-faithful 2009 named-response parity planning/execution in separately gated steps.
4. Only after 2009 stationary/response validation: consider 2009-2023 multi-year batch acceptance.

No full multi-year run, shock run, transition, genuine dynamics, IRF Results, or manuscript Results is authorized by this decision file itself.
