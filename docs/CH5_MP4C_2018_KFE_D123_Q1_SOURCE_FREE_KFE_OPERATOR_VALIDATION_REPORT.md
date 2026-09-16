# CH5 MP4C 2018 KFE D1-D3 Q1 source-free operator validation

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_20260916`

## Verdict

`PASS__ACCEPTED_Q1_UNIQUE_SOURCE_FREE_NORMALIZED_NONNEGATIVE_INVARIANT_MASS`

The exact accepted Q1 passed every frozen operator-level condition. Its exact-positive
off-diagonal graph has exactly one closed communicating class, with exact membership
`[5,6,405,406]`. The sole full dense GESVD found numerical rank 799 and nullity 1,
with the second-smallest singular value strictly above the prospectively frozen rank
threshold. The single sign/orientation and normalization produced a finite probability
mass whose source-free residual, normalization and nonnegativity checks all passed.

There was no clipping, tolerance tuning, retry, solver substitution, pin, row
replacement, RHS source or balancing source. This is an operator-level result only;
it is not nonlinear HJB convergence, a joint HJB-KFE fixed point, stationary economic
equilibrium, production readiness or Results evidence.

## Git identity and scope

- Fresh-fetched baseline: `a1f5d1888afd61572b56187910f78d7d9b1659d2`.
- Branch: `codex/ch5-mp4c-2018-kfe-d123-q1-source-free-kfe-validation-20260916`.
- Candidate SHA is established by the post-push remote readback; a commit cannot embed
  its own SHA without changing that SHA.
- Main was not merged and no successor task was published.

The task added only the bounded Q1 validator, focused tests, this report and the fresh
sealed evidence root. It did not modify Q1, selector, D2 law, V1, grid, calibration,
policy-map code or production/source-faithful model code.

## Exact input and provenance binding

The preflight completed before Q1 load and established:

- Q1 bytes/SHA-256: `23773` /
  `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E`;
- accepted D2 receipt bytes/SHA-256: `3560` /
  `EDE6EED10F4558BA4D902CC3AA9FDED7E23D961D997C12DE8E3654DC2990085A`;
- accepted topology bytes/SHA-256: `98454` /
  `4FDD25E33E2D1025849370391D43CE65F925859DAB4A4E97BDE28784D658E86D`;
- accepted manifest bytes/SHA-256: `125417` /
  `573FCF61220E5982EB4A6E78FAFC5D82310BAC7F7638D2D83B576B1420DDCF37`;
- accepted manifest: 808 entries and 14,117,850 total bytes;
- all 800 policy receipts were present, manifest-hash-bound,
  `SELECTED_ADMISSIBLE` and F-order index-consistent;
- ordered receipt-name/hash digest:
  `F63A3271AC73A583B825E0D1CD53F4B32D948A6D07EB6E33D41381545F285600`;
- state contract: `(20,20,2)`, F-order, b fastest, `omega=70/361`,
  `p` probability mass, `g=p/omega`, and `Q1.T @ p = 0`;
- the four asset faces each had 40 audited cells and exact-zero outward drift,
  outward rate and outward mass-flux coefficient.

The accepted D2 construction identity remained exact:
`diagonal_construction_error == 0.0`. The independently recomputed serialized-CSR
quantity `diag(Q1) + row_sum(stored CSR offdiagonals)` was persisted raw, with maximum
absolute discrepancy `1.7763568394002505e-15`, below the frozen
`2.976424297233587e-14` bound. Its vector SHA-256 is
`039AC0D63E1F3FD2AB14E3B50B23092DF9BA0205148145417BE06D36A1049B6A`.

## Structural and graph checks

| Check | Result |
|---|---:|
| Q1 format / shape | CSR / `(800,800)` |
| finite matrix data | PASS |
| nonzeros | 3,107 |
| negative off-diagonal count | 0 |
| minimum positive off-diagonal | `0.016508228132885275` |
| `max(abs(Q1 @ 1))` | `2.220446049250313e-15` |
| frozen `Q1 @ 1` bound | `2.976424297233587e-14` |
| exact-positive directed edges | 2,307 |
| strongly connected components | 155 |
| closed communicating classes | 1 |
| exact closed membership | `[5,6,405,406]` |
| transient states | 796 |

The SCC-label field SHA-256 is
`4127635E3C44D63DC6EC541F5C91F2550F5C08ACF842CA2ACB3CDAA486A579F0`.
No edge tolerance, graph repair or artificial diffusion was used.

## Rank, nullity and uniqueness

Exactly one full dense
`scipy.linalg.svd(Q1.T, full_matrices=True, lapack_driver="gesvd", check_finite=True)`
was performed.

| Quantity | Result |
|---|---:|
| largest singular value | `29.85754664366335` |
| frozen `tau_rank` | `5.728066976324905e-12` |
| second-smallest singular value | `0.01704325702964291` |
| second-smallest / `tau_rank` | `2975394160.0343795` |
| smallest singular value | `1.2835340137461252e-15` |
| numerical rank / nullity | `799 / 1` |
| GESVD warnings | 0 |

The numerical nullity agrees with the single closed communicating class. Singular-value
field SHA-256:
`24C1A6948C6E05D184EBBD1929543DE4A63454CEBAA71B5F5FD22B44322A7245`.

## Source-free mass checks

Only the right singular vector for the smallest singular value was used. It required
no sign reversal and exactly one scalar normalization.

| Check | Result |
|---|---:|
| `math.fsum(p)` | `0.9999999999999999` |
| `omega * math.fsum(g)` | `0.9999999999999999` |
| `||Q1.T @ p||_inf` | `1.927355525830249e-15` |
| stationarity bound | `3.076397750501459e-12` |
| normwise backward ratio | `1.2019137848100372e-16` |
| `fsum(Q1.T @ p)` | `-3.934635466146915e-17` |
| `(Q1 @ 1) dot p` | `7.902505491428859e-18` |
| global-source identity discrepancy | `4.7248860152898006e-17` |
| global-source bound | `2.461118200401167e-09` |
| minimum stored mass | `-7.838997498725127e-15` |
| nonnegative arithmetic allowance | `1.9184653865526386e-13` |
| total negative roundoff mass | `6.477016647039211e-14` |
| total-negative-mass bound | `1.5347723092421108e-10` |

All frozen checks passed without clipping the 406 negative-roundoff entries. The
persisted arrays artifact has SHA-256
`14E6EC29650A7F9F5D95B023E5B6E54AC1391DC836E2513AC9CACAFEEB7B4254`;
the `p`, `g` and residual field hashes are recorded in the sealed receipt.

## Call ledger

| Operation | Calls |
|---|---:|
| Q1 artifact load | 1 |
| structural/conservation audit | 1 |
| `Q1 @ 1` | 1 |
| SCC decomposition | 1 |
| dense full GESVD | 1 |
| normalized stationary candidate | 1 |
| `Q1.T @ p` | 1 |
| retry / solver substitution | 0 |
| row-replaced/direct KFE solve | 0 |
| iterative eigensolver/nullspace solve | 0 |
| selector / root / policy map / D2 reassembly | 0 |
| HJB / V2 / nonlinear continuation | 0 |
| MATLAB / outer / firm / wage-return / GE / annual / shock / IRF / Results | 0 |

## Verification and durability

- TDD red phase: the Q1 validator import failed before implementation existed.
- Focused Q1 tests: 5 passed.
- Focused Q0+Q1 validator regression: 16 passed.
- `py_compile`: PASS.
- `git diff --check`: PASS.
- Post-execution scientific-code hashes exactly matched the pre-Q1-load freeze.
- Wall time: `1.7273494999390095` seconds, below 300 seconds.
- Peak resident memory: `100605952` bytes, below 2 GiB.
- Fresh sealed evidence manifest: 11 entries before the manifest itself,
  38,807 total bytes.

## Interpretation boundary

This run establishes a unique, normalized, nonnegative within frozen arithmetic
allowance, source-free invariant mass for the exact accepted finite-state Q1 operator.
It does not establish nonlinear HJB convergence, a joint HJB-KFE fixed point,
stationary economic equilibrium, production readiness or Results eligibility.

Results eligibility remains `FALSE`. No successor task is published by this task.
