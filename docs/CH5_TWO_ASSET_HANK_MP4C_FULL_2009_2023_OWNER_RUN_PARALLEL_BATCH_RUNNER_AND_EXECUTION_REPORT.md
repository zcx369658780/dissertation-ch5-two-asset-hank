# MP4C full 2009--2023 Owner-run parallel annual batch: execution report

Date: 2026-09-02

## Verdict

`MP4C_FULL_2009_2023_OWNER_RUN_PARALLEL_ANNUAL_STATIONARY_COVERAGE_PASS`

The Owner manually completed one Python annual stationary production run for every
calendar year from 2009 through 2023, inclusive.  The Phase-B closeout audit was
read-only: it did not rerun a stationary worker or start MATLAB, the comparator,
shocks, AR(1), dynamics, IRFs, R5, or Results work.

This is Python annual stationary coverage against the Owner-designated
`MATLAB_PROTECTED_RUNTIME_DATA_CACHE`.  It is not a blanket MATLAB--Python parity
claim.

## Authority and immutable inputs

* Live task / authority commit: `CH5_TWO_ASSET_HANK_MP4C_MATLAB_RUNTIME_CACHE_OWNER_DESIGNATION_VERIFICATION_AND_BATCH_REAUTHORIZATION`, `14c8061d0f1c7842c5da39f0e998302f4e7ca75a`.
* At closeout, `HEAD == origin/main == 14c8061d0f1c7842c5da39f0e998302f4e7ca75a` before the authorized closeout commit.
* Owner batch root (external, no-overwrite): `D:\ProjectTemp\ch5-mp4c-full-annual-batch-runtime-cache-20260902-002`.
* Runtime representation: `MATLAB_PROTECTED_RUNTIME_DATA_CACHE`.
* Runtime cache identity: `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`.
* Phase-A implementation receipt: `D:\ProjectTemp\ch5-mp4c-runtime-cache-launcher-encoding-remediation-20260902-001\batch_runner_build_receipt_v3.json`, SHA-256 `59BF569F8BC77075DFE1F718AEE250DA494906E7DEA6549F76C5DBA8DEC2E20C`.

Before examining the batch output, all seven receipt-covered local implementation,
contract, test, and launcher files matched their recorded byte counts and
SHA-256 values exactly.  No source-model module, data, or accepted historical
driver was changed for this closeout.

## Owner execution record

The Owner used `Workers=4` with year-level subprocess parallelism and the thread
environment pinned to `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`,
`OPENBLAS_NUM_THREADS=1`, and `NUMEXPR_NUM_THREADS=1`.

| Item | Result |
| --- | --- |
| Calendar coverage | 2009--2023, 15 of 15 years |
| Batch statuses | 15 `PASS`, 0 `FAIL`, all exit code 0 |
| Year terminal status | 15 `SOURCE_CONVERGED` |
| Automatic reruns | 0 for every year |
| Household convergence | 31/31 provinces for every year |
| Scientific wall clock | 32,622.241112 seconds |
| Launcher wall clock | 32,623.063 seconds |
| Scheduler capacity | 4 workers |

The terminal progress display can list fewer than four `running` years after a
completion has already been collected; the persisted batch timing manifest is the
authoritative record and reports `workers: 4`.

## Read-only output audit

The audit checked the external batch root without modifying it.

1. `batch_manifest.json` covers exactly the ordered years 2009--2023 and records
   the designated runtime-cache representation and identity.
2. `batch_summary.json` and `batch_summary.csv` contain exactly 15 successful
   year entries.  `batch_timing.json` records the timing and one-thread BLAS
   environment above.
3. For each `year_2009` through `year_2023`, the `SUCCESS.json` output inventory
   was re-hashed: all nine listed output byte counts and SHA-256 values matched.
4. Every year has the required final steady state, `final_31x20.csv`, MATLAB
   persistence artifact, restart NPZ, Lt matrix, run manifest, checkpoint
   manifest, and timing file.  The final NPZ and MAT hashes bind exactly through
   the final household checkpoint manifest and success marker.
5. Every final CSV has exactly 31 unique provinces in the accepted common order
   and exactly these 20 finite terminal fields: `Ct`, `At`, `Bt`, `Lt`,
   `Lt_supply`, `Kt_supply`, `rah`, `Kt`, `Yt`, `mt`, `KNratio`, `w`, `wjt`,
   `rk`, `ra`, `GovInv`, `rb`, `it`, `Zt`, and `Govinc`.
6. `steady_state_panel_2009_2023.csv` contains exactly 465 rows (15 years x 31
   provinces), with each calendar year represented by 31 rows.
7. All eight root-level files listed in `artifact_hash_manifest.json` matched
   their recorded byte counts and SHA-256 values, including both aggregate XLSX
   workbooks.

## What was not executed

No Phase-B stationary rerun was performed.  The optional 2009 comparator-only
check was not invoked.  MATLAB, shocks, AR(1), dynamics, IRFs, R5, and Results
remain unexecuted by this task.

## Git boundary

Only the receipt-covered implementation/contract/tests/launcher and this report
are eligible for the one closeout commit.  The ignored runtime MAT cache, primary
inputs, external batch root, generated MAT/NPZ/XLSX/CSV artifacts, and logs are
not eligible for staging.
