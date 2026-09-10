# Chapter 5 MP4C origin-preserving bilateral labor-normalization implementation report

## Verdict

`ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_PASS__FULL_MATRIX_TRACEABILITY_AND_CONSERVATION_ENFORCED`

Baseline: `3e8d26d1c5430d9734ec5ac3d4c3e74e68217ee9` on the dedicated branch `codex/ch5-origin-preserving-bilateral-labor-normalization-20260910`.

## Implemented contract

The legacy literal MATLAB-faithful migration and one-turn APIs remain intact. A separately named normalized successor evaluates the full source kernel `q[destination,origin]`, normalizes each origin column, multiplies household labor per capita by its origin population exactly once, and allocates that entire mass into the bilateral matrix `M[destination,origin]`. The result retains all raw, normalized, bilateral, aggregate, net-flow, and residual objects as read-only arrays.

A separate `run_origin_preserving_normalized_one_turn` consumes destination row sums for firms while reusing the unchanged capital, firm, wage, monetary, and fiscal component functions. It is not connected to steady-state, annual, or trajectory runtimes.

## Required answers

1. Full 31x31 provenance: **YES**. A direct deterministic test constructs and retains `q`, `s`, and `M` with shape 31x31 and destination-row/origin-column orientation.
2. Origin-column mass preservation: **YES**. Every `sum_j M[j,i]` equals `household_lt[i] * N[i]` within `1e-12` deterministic tolerance.
3. National conservation: **YES**. Synthetic origin and destination totals are both 100 and the residual is 0; the 31x31 test also passes.
4. Resident versus destination labor: **YES**. The asymmetric trace has origin masses `[50,20,30]` and destination firm labor `[49,26,25]`, with every bilateral flow retained.
5. Later wage attribution: **YES**. Each origin retains its complete `M[:,i]` and `s[:,i]`; the current CES-like wage rule was not changed.
6. Source-faithful parity path changed: **NO**. `reconstruct_migration_labor` was only followed by additive code, `run_source_faithful_one_turn` retains its body and return type, and the accepted fixture regression passes.
7. GovInv/capital/controller/HJB/KFE/wage rule changed: **NO**. Changed production paths are limited to migration, additive one-turn composition, and exports.
8. Remaining work: the later GovInv task must separately decide and implement its initialization/controller treatment; a later wage-provenance task may use the retained origin columns to define household wage attribution. Neither is authorized here.

## Synthetic provenance

For the Henan-style origin mass 50, shares `[0.60,0.24,0.16]` produce bilateral flows `[30,12,8]`. Other origins send 10 and 9 units into Henan, so Henan's destination firm labor is 49 rather than its origin labor 50. The full provenance is in `synthetic_bilateral_trace.csv`; the net value alone is not used as a substitute.

## Verification and boundaries

Focused suite: **27 passed in 1.31s**. It covers legacy fixture parity, 3x3 asymmetric traceability, 31x31 shape, column and national conservation, population-once behavior, household-labor and destination-wage perturbations, invalid-column fail-closed behavior, valid negative-tax/negative-wedge literal-kernel cases, distinct APIs, and separate one-turn integration. `py_compile` and `git diff --check` passed.

Scientific-call ledger is zero for HJB, KFE, household solve, MATLAB runtime, firm/outer trajectories, steady state, root/Brent, GE, annual, IRF, and Results. This PASS is implementation evidence only: steady state is not accepted, labor calibration and wage provenance are not complete, and Results eligibility remains false.
