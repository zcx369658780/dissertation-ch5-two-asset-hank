# CH5 MP4C 2018 KFE D1-D3 corrected Q0 operator validation

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_20260916`

## Verdict

`FAIL__Q0_STRUCTURAL_OR_CONSERVATION_AUDIT__NO_SVD`

The bounded run stopped at the first post-load structural failure.  The exact
accepted Q0 was loaded once and audited once.  Its recomputed off-diagonal
aggregation did not reproduce the accepted exact-zero diagonal construction
identity: the maximum absolute value of
`diag(Q0) + sum(exact offdiagonals by row)` was
`3.552713678800501e-15`, not exact zero.  The already accepted source D2
receipt had recorded exact construction error `0.0` using the generator's
retained-outgoing construction array.  This run did not reinterpret the
difference as tolerance-admissible and did not change the frozen contract.

The separately frozen conservation check passed:
`max(abs(Q0 @ 1)) = 3.552713678800501e-15 <=
5.222144858126786e-14`.  Q0 was finite CSR `(800,800)`, had 3,118 nonzeros,
zero negative off-diagonals, minimum positive off-diagonal
`0.2642984748447064`, and exact-zero outward-face receipt coefficients on all
four asset faces.  These passing subchecks do not override the failed exact
diagonal identity.

Because the first structural failure is terminal under the task, SCC, dense
GESVD, rank/nullity, stationary mass, normalization, nonnegativity and
`Q0.T @ p` were not executed.  No retry, tolerance adjustment, clipping,
solver substitution or alternative construction check was used.

## Git identity and scope

- Fresh-fetched baseline: `bf7d0dc09220639dfa420ace4dfbedac93788202`.
- Branch:
  `codex/ch5-mp4c-2018-kfe-d123-corrected-q0-kfe-operator-validation-20260916`.
- Candidate SHA: the immutable task commit is reported by the post-push remote
  readback; a commit cannot embed its own SHA without changing that SHA.
- Main was not merged and no successor task was published.

Changed paths are exactly:

1. `src/ch5_two_asset_hank/corrected_diagnostic/q0_kfe_validation.py`;
2. `tests/test_mp4c_2018_kfe_d123_q0_kfe_operator_validation.py`;
3. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_REPORT.md`;
4. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916/preflight_binding_receipt.json`;
5. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916/pre_execution_code_freeze.json`;
6. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916/structural_conservation_receipt.json`;
7. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916/execution_ledger.json`;
8. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916/terminal_receipt.json`;
9. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916/post_execution_freeze_check.json`;
10. `reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916/sealed_manifest.json`.

## Binding and preflight

The startup authority was read from fresh `origin/main` in the required order
and the task remained the unique ACTIVE task.  The preflight completed before
any Q0 sparse load and established:

- Q0 path:
  `reports/ch5_mp4c_2018_kfe_d123_interior_z_switching_option_a_reexecution_20260916/d2_generator.npz`;
- bytes: `22474`;
- SHA-256:
  `093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`;
- accepted manifest bytes/hash: `125779` /
  `D628E24AD421EA5A38EF80230862FE7B3BBD9BFA368CA7BEB08820528ADB643E`;
- manifest entries/declared payload bytes: `810` / `13963843`;
- all 800 `cell_0000.json` through `cell_0799.json` were present,
  individually hash-bound to the accepted manifest, F-order index-consistent,
  and `SELECTED_ADMISSIBLE`;
- ordered receipt-name/hash digest:
  `DDC21060F327CE4642A898C8D9E71901C8FD125CAD35694A3A71A6EB8782272E`;
- state contract: `(b,a,z)=(20,20,2)`, F-order, b fastest,
  `omega=70/361`, forward equation `Q0.T @ p = 0`.

Each of lower/upper b and lower/upper a had 40 face receipts.  Every face's
outward drift sum, outward rate sum and outward mass-flux coefficient was
exactly `0.0`.

## Structural and conservation receipt

| Check | Result |
|---|---:|
| Q0 format / shape | CSR / `(800,800)` |
| finite matrix data | PASS |
| nonzeros | 3,118 |
| negative off-diagonal count | 0 |
| minimum positive off-diagonal | `0.2642984748447064` |
| recomputed diagonal construction error | `3.552713678800501e-15` |
| exact-zero diagonal identity | **FAIL** |
| `max(abs(Q0 @ 1))` | `3.552713678800501e-15` |
| prospective `Q0 @ 1` bound | `5.222144858126786e-14` |
| `Q0 @ 1` check | PASS |
| `Q0 @ 1` field SHA-256 | `B1C50ED52EF5A6CC2D6B4DE629ECC24F45A5DF727EE2C9C49CCF825F6123F4DE` |

The terminal classification is local to this validator's frozen exact
structural contract.  It is not evidence that a stationary distribution does
not exist, and it is not an HJB, KFE-in-general, equilibrium or Results claim.

## Call ledger

| Operation | Calls |
|---|---:|
| Q0 artifact load | 1 |
| structural/conservation audit | 1 |
| `Q0 @ 1` | 1 |
| SCC decomposition | 0 |
| dense `scipy.linalg.svd(..., lapack_driver="gesvd")` | 0 |
| normalized stationary candidate | 0 |
| `Q0.T @ p` | 0 |
| row-replaced/direct KFE solve | 0 |
| iterative eigensolver/nullspace solve | 0 |
| solver substitution | 0 |
| scientific retry | 0 |
| selector / root / policy map / D2 / HJB / V1 remap | 0 |
| MATLAB / outer / firm / wage-return / GE / annual / shock / IRF / Results | 0 |

Before this one scientific run, an initial launcher attempt stopped inside the
task-local Windows RSS probe before Q0 was loaded or any structural/SCC/SVD
operation occurred.  The ctypes API declaration was corrected, focused checks
and the zero-science binding preflight were repeated, and a fresh code freeze
was written.  This was not a scientific retry and consumed none of the frozen
scientific-call budget.

## Verification and durability

- Focused tests: `8 passed`.
- `py_compile`: PASS.
- `git diff --check`: PASS.
- Final scientific/test hashes exactly matched the pre-Q0-load freeze.
- Peak resident memory: `75,333,632` bytes, below `2,147,483,648`.
- Final scientific-run wall time: `0.6165504999225959` seconds, below 300.
- Sealed evidence manifest: 6 entries before the manifest itself, 6,523 bytes.
- No stationary-mass arrays artifact exists because the run stopped before
  SVD and candidate construction, as required.

## Interpretation boundary and next gate

This candidate preserves the first failure and supplies implementation plus
durable evidence only.  It does not validate uniqueness, rank/nullity,
stationarity, normalization or nonnegative mass.  Results eligibility remains
`FALSE` and production remains unchanged.

Any decision about whether the intended diagonal identity must use the accepted
retained-outgoing construction receipt, a recomputed sparse off-diagonal sum,
or an arithmetic allowance is a fresh Reviewer/Owner contract decision.  This
task does not repair or rerun that choice and does not publish a successor.
