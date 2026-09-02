# CH5 TWO ASSET HANK MP4C L3 FORMAL 2009–2023 ANNUAL STATIONARY COVERAGE ACCEPTANCE REPORT

Date: 2026-09-02

## Terminal verdict

`MP4C_2009_2023_PYTHON_ANNUAL_STATIONARY_COVERAGE_FORMALLY_ACCEPTED`

Acceptance level:

`FULL_2009_2023_PYTHON_ANNUAL_STATIONARY_COVERAGE_ACCEPTED__CORRECTED2009_CROSS_LANGUAGE_PARITY_RETAINED__DYNAMICS_NOT_YET_ACCEPTED`

## Authority and continuity

- Formal L3 acceptance task authority: `7eeec9f159e78bffce62c407bb72d331f47bc90d`.
- Required predecessor execution: `9944ddb69e5b8b75122f8827dc6c440ead45e8ac`.
- Predecessor execution terminal: `MP4C_FULL_2009_2023_OWNER_RUN_PARALLEL_ANNUAL_STATIONARY_COVERAGE_PASS`.
- Runtime-cache Owner designation authority: `14c8061d0f1c7842c5da39f0e998302f4e7ca75a`.
- The predecessor execution is exactly one commit ahead of the runtime-cache authority and has that authority as its sole parent.
- The formal acceptance task is exactly one commit ahead of the predecessor execution and has the execution as its sole parent.

This L3 review is read-only. No MATLAB, Python stationary, household, HJB, KFE, comparator, AR(1), shock, dynamics, IRF, R5 or Results execution was performed.

## Changed-path review

The predecessor execution changed exactly eight repository paths, all additions:

1. `docs/CH5_TWO_ASSET_HANK_MP4C_FULL_2009_2023_OWNER_RUN_PARALLEL_BATCH_RUNNER_AND_EXECUTION_REPORT.md`;
2. `scripts/run_mp4c_full_annual_batch.ps1`;
3. `tests/test_mp4c_full_annual_batch_runner.py`;
4. `tests/test_mp4c_matlab_runtime_cache.py`;
5. `validators/multi_province/matlab_persistence_contract.json`;
6. `validators/multi_province/mp4c_matlab_runtime_cache.py`;
7. `validators/multi_province/mp4c_python_annual_production.py`;
8. `validators/multi_province/mp4c_run_full_annual_batch.py`.

No protected MATLAB source, primary workbook, runtime MAT cache, generated annual MAT/NPZ/XLSX/CSV result, historical accepted driver, household/HJB/KFE scientific source, `one_turn.py`, `firm.py`, controller, calibration, grid, threshold or tolerance was committed in the execution closeout.

## Accepted runtime representation

The production batch is explicitly bound to:

`MATLAB_PROTECTED_RUNTIME_DATA_CACHE`

with exact cache SHA-256:

`923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`.

The runtime-cache adapter is fail-closed on cache SHA, top-level schema, `mydata2` entry count, field schema, province order, calendar/index binding, field shapes, finiteness and admissible positive GDP/CAP/POP levels. It does not use `abs`, clipping, interpolation or manual replacement to repair the negative values observed in the current upstream workbook.

The accepted provenance interpretation remains:

`upstream workbook(s) -> load_GDPdata.m processing -> 数据估计结果_1000_100_0.mat -> protected MATLAB annual runtime -> Python MATLAB-faithful runtime binding`.

The cache is an accepted MATLAB protected runtime representation for this production route; it is not reclassified as raw/primary external data.

## Full annual coverage evidence

The Owner manually executed one coherent production batch over exactly 15 calendar years, 2009 through 2023 inclusive, using four year-level workers with BLAS/OpenMP thread counts pinned to one per worker.

The Phase-B audit establishes:

- annual coverage: `15/15`;
- batch status: `15 PASS`, `0 FAIL`;
- annual terminal status: `15/15 SOURCE_CONVERGED`;
- automatic reruns: `0` for every year;
- final household convergence: `31/31` provinces for every year;
- final province identity: complete, unique and in the accepted common order for every year;
- final continuous state: complete finite ordered `31 × 20` field map for every year;
- aggregate annual panel: exactly `465` rows = `15 years × 31 provinces`;
- all per-year success-marker output inventories re-hashed successfully;
- all required root-level batch summary artifacts listed by the artifact hash manifest re-hashed successfully.

The accepted 20 terminal fields are:

`Ct, At, Bt, Lt, Lt_supply, Kt_supply, rah, Kt, Yt, mt, KNratio, w, wjt, rk, ra, GovInv, rb, it, Zt, Govinc`.

## Persistence and restart evidence

Every accepted year contains the required final stationary-state outputs plus:

- exact final `Lt_mat` persistence with destination-row × origin-column orientation;
- compact final household restart NPZ;
- MATLAB-readable Python annual checkpoint MAT;
- checkpoint manifest binding annual input, source/runtime identities, scientific-code identities, terminal state and checkpoint hashes.

The Python checkpoint explicitly identifies itself as a source-backed Python restart representation and not as an unproven byte-compatible legacy MATLAB `st` drop-in. This is the correct interpretation boundary for later shock/IRF reconstruction.

## Timing evidence

Descriptive engineering timing for the accepted Owner run:

- workers: `4`;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `OPENBLAS_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- scientific batch wall clock: `32622.241112` seconds;
- launcher wall clock: `32623.063` seconds.

This timing is accepted as reproducibility/performance evidence for the Python production run only. It is not by itself a scientific acceptance criterion and does not establish a MATLAB/Python performance comparison.

## Relationship to corrected-2009 parity authority

The prior formal corrected-2009 marker remains unchanged:

`MP4B_CORRECTED_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_FORMALLY_ACCEPTED`.

This new acceptance does not replace or weaken that evidence. It extends accepted Python stationary production coverage to all 15 years under the Owner-designated protected MATLAB runtime cache.

It does **not** automatically promote 2010–2023 to MATLAB–Python stationary parity because no corresponding year-specific MATLAB comparator evidence was executed in this batch gate.

## Formal L3 acceptance decision

The evidence is sufficient to formally accept the complete 2009–2023 Python annual stationary production coverage.

Accepted marker:

`MP4C_2009_2023_PYTHON_ANNUAL_STATIONARY_COVERAGE_FORMALLY_ACCEPTED`

Acceptance level:

`FULL_2009_2023_PYTHON_ANNUAL_STATIONARY_COVERAGE_ACCEPTED__CORRECTED2009_CROSS_LANGUAGE_PARITY_RETAINED__DYNAMICS_NOT_YET_ACCEPTED`

This closes the MP4C annual stationary coverage gate.

## Scope not accepted

This decision does not establish or approve:

- blanket MATLAB–Python parity for 2010–2023;
- alternative controller-threshold robustness;
- AR(1) shock semantics;
- transition dynamics;
- IRFs or shock-response validity;
- historical R5 Results;
- dissertation/journal-paper final Results claims.

## Exactly one recommended next scientific gate

`MP4D_SHOCK_AND_IRF_SOURCE_SEMANTICS_AUDIT_AND_PYTHON_ROUTE_FREEZE`

The next gate should be zero-science/static first: audit the protected MATLAB shock caller, horizon/shock construction, annual steady-state checkpoint consumption, state carry-forward semantics and output persistence; distinguish the existing sequential comparative-statics route from any genuine transition-dynamics claim; then freeze the Python shock/IRF reconstruction contract before running representative-year or full-sample shock responses.
