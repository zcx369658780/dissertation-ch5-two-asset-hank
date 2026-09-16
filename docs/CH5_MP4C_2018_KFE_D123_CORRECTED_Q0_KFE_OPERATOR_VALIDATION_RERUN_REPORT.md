# CH5 MP4C 2018 KFE D1-D3 corrected Q0 operator-validation rerun

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_RERUN_WITH_BOUND_REAGGREGATION_20260916`

## Verdict

`FAIL__CLOSED_COMMUNICATING_CLASS_COUNT__NO_SVD`

The authorized secondary sparse-reaggregation repair passed, but the fresh run
stopped at the next mandatory structural gate.  The exact-positive off-diagonal
graph has **two**, not one, closed communicating classes.  The sole SCC
decomposition found 400 strongly connected components, each of size 2; closed
component labels 0 and 6 each have size 2, leaving 796 transient states.

The task requires exactly one closed communicating class.  The run therefore
terminated before dense GESVD.  Rank/nullity, stationary mass, normalization,
nonnegativity and `Q0.T @ p` were not evaluated.  There was no retry, solver
substitution, edge tolerance, graph repair or alternative decomposition.

## Git identity and scope

- Fresh-fetched baseline: `f003e2bd2e613ec8a2f365b2ee2905b3a2ae9ecf`.
- Branch:
  `codex/ch5-mp4c-2018-kfe-d123-q0-kfe-bound-reaggregation-rerun-20260916`.
- Candidate SHA: the immutable task commit is reported by the post-push remote
  readback; a commit cannot embed its own SHA without changing that SHA.
- Main was not merged and no successor task was published.

The only scientific-code change was the authorized Q0-validator secondary
audit; the only test-code change covers that audit and its accepted D2 receipt
binding.  No Q0, generator, policy, seed, grid or calibration path changed.

Changed paths are exactly:

1. `src/ch5_two_asset_hank/corrected_diagnostic/q0_kfe_validation.py`;
2. `tests/test_mp4c_2018_kfe_d123_q0_kfe_operator_validation.py`;
3. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_RERUN_REPORT.md`;
4. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_rerun_20260916/preflight_binding_receipt.json`;
5. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_rerun_20260916/pre_execution_code_freeze.json`;
6. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_rerun_20260916/structural_conservation_receipt.json`;
7. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_rerun_20260916/scc_receipt.json`;
8. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_rerun_20260916/execution_ledger.json`;
9. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_rerun_20260916/terminal_receipt.json`;
10. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_rerun_20260916/post_execution_freeze_check.json`;
11. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_rerun_20260916/sealed_manifest.json`.

## Exact binding and construction provenance

The preflight completed before Q0 load and established:

- accepted Q0 bytes/SHA-256: `22474` /
  `093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`;
- accepted D2 receipt bytes/SHA-256: `1526` /
  `60389B54953B69C05A4DB2693272E2A32A8FB3F962AD99A285F82B266BF2237B`;
- accepted D2 construction identity:
  `diagonal_construction_error == 0.0` exactly and its exact-zero check is
  `true`;
- accepted manifest bytes/SHA-256: `125779` /
  `D628E24AD421EA5A38EF80230862FE7B3BBD9BFA368CA7BEB08820528ADB643E`;
- all 800 policy receipts remained present, manifest-hash-bound,
  `SELECTED_ADMISSIBLE` and F-order index-consistent;
- ordered receipt-name/hash digest:
  `DDC21060F327CE4642A898C8D9E71901C8FD125CAD35694A3A71A6EB8782272E`;
- state contract remained `(20,20,2)`, F-order with b fastest,
  `omega=70/361`, and forward equation `Q0.T @ p = 0`.

## Repaired secondary diagonal audit

The accepted construction-provenance identity and independent CSR reduction
were persisted separately.

| Check | Result |
|---|---:|
| accepted D2 construction error | exact `0.0` |
| CSR reaggregation formula | `diag(Q0) + row_sum(stored CSR offdiagonals)` |
| raw maximum absolute discrepancy | `3.552713678800501e-15` |
| fixed bound | `5.222144858126786e-14` |
| finite and within bound | PASS |
| discrepancy vector SHA-256 | `43062E4AA466D6139D50B986EF8C62A5710EEE962C745A0C4078D4A1FACA7035` |
| discrepancy modified or zeroed | no |

No tolerance was selected after observing the discrepancy.

## Other reached structural checks

| Check | Result |
|---|---:|
| Q0 format / shape | CSR / `(800,800)` |
| finite matrix data | PASS |
| nonzeros | 3,118 |
| negative off-diagonal count | 0 |
| minimum positive off-diagonal | `0.2642984748447064` |
| `max(abs(Q0 @ 1))` | `3.552713678800501e-15` |
| frozen `Q0 @ 1` bound | `5.222144858126786e-14` |
| `Q0 @ 1` field SHA-256 | `B1C50ED52EF5A6CC2D6B4DE629ECC24F45A5DF727EE2C9C49CCF825F6123F4DE` |
| four outward-face drift/rate/flux ledgers | exact zero |

## Exact-positive graph result

- edge rule: every exact `Q0[i,j] > 0` off-diagonal, with no tolerance;
- positive directed edges: 2,318;
- SCC decomposition count: 1;
- strongly connected components: 400;
- component sizes: 400 components of size 2;
- closed component labels: 0 and 6;
- closed component sizes: 2 and 2;
- closed communicating class count: **2**;
- transient states: 796;
- SCC-label field SHA-256:
  `63717388651FFCCB336F6D0D324D6E3B063276E4F4D3ADE726FD639A63494A76`.

This result fails the frozen uniqueness prerequisite.  Because GESVD was not
run, this task makes no numerical-nullity claim and does not infer graph/SVD
agreement or disagreement.

## Call ledger

| Operation | Calls |
|---|---:|
| Q0 artifact load | 1 |
| structural/conservation audit | 1 |
| `Q0 @ 1` | 1 |
| SCC decomposition | 1 |
| dense `scipy.linalg.svd(..., lapack_driver="gesvd")` | 0 |
| normalized stationary candidate | 0 |
| `Q0.T @ p` | 0 |
| row-replaced/direct KFE solve | 0 |
| iterative eigensolver/nullspace solve | 0 |
| solver substitution | 0 |
| scientific retry | 0 |
| selector / root / policy map / D2 / HJB / V1 remap | 0 |
| MATLAB / outer / firm / wage-return / GE / annual / shock / IRF / Results | 0 |

## Verification and durability

- TDD red check: missing accepted-D2 construction binding failed as expected.
- Focused final tests: `11 passed`.
- `py_compile`: PASS.
- `git diff --check`: PASS.
- Scientific/test hashes after execution exactly matched the pre-Q0-load
  freeze.
- Peak resident memory: `75,395,072` bytes, below 2 GiB.
- Scientific-run wall time: `0.7002550999168307` seconds, below 300 seconds.
- Sealed evidence manifest: 7 entries before the manifest itself, 14,352
  bytes.
- No stationary-mass arrays artifact exists because the run stopped before
  GESVD and candidate construction.

## Interpretation boundary

This run establishes that the accepted Q0 passes the corrected construction,
secondary reaggregation, row-sum and closed-face checks, but fails the frozen
one-closed-class structural uniqueness condition.  It does not establish
rank/nullity, source-free invariant mass, nonlinear HJB convergence, a joint
HJB-KFE fixed point, stationary economic equilibrium, production readiness or
Results eligibility.

Results eligibility remains `FALSE`.  Any scientific response to the two
closed communicating classes requires a fresh Reviewer/Owner decision; this
task does not alter Q0 or publish a successor.
