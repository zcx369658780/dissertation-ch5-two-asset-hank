# CH5 MP4C 2018 KFE D1-D3 corrected Q0 KFE operator validation rerun with bounded sparse reaggregation

Date: 2026-09-16

Status: ACTIVE

## Objective

Fresh-rerun the already designed source-free Q0 operator-level KFE validation after correcting exactly one validator semantic: the secondary sparse off-diagonal reaggregation audit is arithmetic-bound based rather than exact-zero. The accepted D2 construction receipt remains the exact-zero construction authority.

## Repository and baseline

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.

Builder must fresh-fetch `origin/main` and use the live main as baseline. Read `AGENTS.md`, rule index, current status/handoff, the Q0 KFE design report, the prior fail-closed report, and `docs/CH5_MP4C_2018_KFE_D123_Q0_KFE_STRUCTURAL_AUDIT_ARITHMETIC_REAGGREGATION_ACCEPTANCE_20260916.md` before work.

## Exact Q0 binding

Use only the accepted Q0 artifact:

`reports/ch5_mp4c_2018_kfe_d123_interior_z_switching_option_a_reexecution_20260916/d2_generator.npz`

SHA-256:
`093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`

No Q0 reconstruction or generator reassembly is permitted.

## Authorized validator repair

Only the Q0 validator/test may change as necessary to implement this distinction:

- accepted D2 receipt `diagonal_construction_error` must still equal exact `0.0` and remain the construction-provenance identity;
- independently recompute from loaded CSR:
  `diag(Q0) + row_sum(stored offdiagonals)`;
- persist the exact maximum absolute sparse-reaggregation discrepancy;
- require it finite and `<= 5.222144858126786e-14`;
- do not alter Q0, diagonal entries, offdiagonal entries or accepted receipts;
- no fitted tolerance, retry or alternate accumulation chosen after seeing outcome.

All other frozen Q0 KFE design semantics remain unchanged.

## Runtime contract

Forward stationarity: `Q0.T @ p = 0`.

State order `(b,a,z)=(20,20,2)`, F-order, b fastest. `omega=70/361`, `p` is probability mass, `g=p/omega`.

No row replacement, pin, RHS source, balancing source, clipping, absolute-value repair, iterative eigensolver, alternate LAPACK driver, solver substitution or retry.

Sole nullspace route after structural audit passes:
`scipy.linalg.svd(A, full_matrices=True, lapack_driver="gesvd", check_finite=True)`, `A=Q0.T`.

Use the frozen design report's exact prospective formulas for sign orientation, normalization, stationarity residual, nonnegative mass, rank threshold and uniqueness.

## Hard ceilings

- accepted Q0 artifact loads <=1
- structural/conservation audits <=1
- `Q0 @ 1` evaluations <=1
- SCC decompositions <=1
- full dense GESVD <=1
- normalized stationary candidates <=1
- `Q0.T @ p` evaluations <=1
- row-replaced/direct KFE solves =0
- iterative eigensolver/nullspace solves =0
- retries =0
- solver substitutions =0
- selector/root/policy-map/D2/HJB/V1 remap =0
- MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results =0
- wall time <=300 seconds
- resident memory <=2 GiB

## PASS requirements

All of the following must pass without retry:

1. Q0 artifact/hash/shape/order identity.
2. No negative offdiagonal; all entries finite.
3. Accepted D2 construction receipt still records exact construction error `0.0`.
4. Independent sparse reaggregation discrepancy `<=5.222144858126786e-14`.
5. `max(abs(Q0@1)) <=5.222144858126786e-14`.
6. Exact-zero outward asset-face drift/rate/flux ledger.
7. Exact-positive-edge graph has exactly one closed communicating class.
8. One GESVD gives numerical rank 799/nullity 1 at the frozen rank threshold; next-smallest singular value strictly exceeds threshold.
9. Null vector sign is orientable and total sum is strictly resolvable under frozen summation bound.
10. One normalization gives total probability mass 1 under the frozen bound.
11. Nonnegative mass passes the frozen componentwise and total-negative-mass arithmetic allowances with no clipping.
12. `Q0.T@p` source-free stationarity and global conservation ledgers pass the frozen prospective bounds.

Any first failure terminates immediately and no alternate solver/retry is allowed.

## Deliverables

Persist durable preflight, code-freeze, structural/SCC/SVD/stationary-mass receipts as reached, execution ledger, terminal receipt, post-freeze verification and sealed manifest. If PASS, persist `p` and `g` arrays plus their SHA-256 identities.

Create one report:
`docs/CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_RERUN_REPORT.md`.

Commit and non-force push the task branch. Do not merge main. Do not publish a successor task.

Results eligibility remains `FALSE` regardless of outcome.
