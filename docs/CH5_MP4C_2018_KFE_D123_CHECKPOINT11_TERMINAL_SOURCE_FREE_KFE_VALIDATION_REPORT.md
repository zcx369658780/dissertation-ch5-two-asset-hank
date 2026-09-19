# Chapter 5 MP4C-2018 D123 checkpoint-11 terminal source-free KFE validation report

Date: 2026-09-20

Task: `CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_20260920`

## Terminal verdict

`PASS__CHECKPOINT11_UNIQUE_SOURCE_FREE_INVARIANT_MASS__HOUSEHOLD_HJB_KFE_FIXED_POINT_CANDIDATE`

Exact accepted Q11 has exactly one closed communicating class and numerical nullity one. Its single full dense `gesvd` null vector passed the frozen source-free stationarity, normalization and nonnegativity-with-arithmetic-allowance checks without clipping, row replacement, pinning, source injection, solver substitution or retry.

This PASS is a conditional household HJB-KFE fixed-point candidate under frozen prices and calibration. Results eligibility remains `FALSE`.

## Repository and implementation binding

- fresh live `origin/main`: `bc10e8778dab6d8ba00feaa0b18fc5957d7b6435`;
- implementation-freeze execution HEAD: `cf265c874f13b4612643acea3c697109a35864fc`;
- task branch: `codex/ch5-mp4c-2018-kfe-d123-checkpoint11-terminal-source-free-kfe-validation-20260920`;
- isolated worktree: `D:\ProjectTemp\c11kfe`;
- worktree was clean before evidence creation;
- pre-execution and post-execution scientific-code hashes match.

## Exact checkpoint-11 and Q11 binding

The accepted 819-entry predecessor manifest was fully read back before terminal science. All recorded paths, sizes and SHA-256 values matched.

| Object | Exact identity |
|---|---|
| accepted predecessor candidate | `47ab268e788c856b2515ebadca0356dbecbcda81` |
| V11 | `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F` |
| P11 | `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3` |
| u11 | `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648` |
| Q11 artifact | `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD` |
| Q11 data | `9D489C6A5C8E4A1F705CEC228EDE380FF0A5F51D569CA31DE9BCF9B4BC56537A` |
| Q11 indices | `9A1E128BD9B13A6711B20FB992699DB405DEF5450543921ACAB69B57FA5474E6` |
| Q11 indptr | `63190CF1D9F4C98D89C81A9990736462F19170B45F97E03AD7B507D492D9C327` |
| checkpoint-11 identity | `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B` |
| checkpoint arrays | `F620823F15CEB71A168437880AC8655FCBC075D0B7894CBA013780759A8157B2` |

Accepted `B11=5.456747553811425e-11`, `D11=5.4012647243695255e-08`, D2 PASS and primary convergence PASS were bound exactly. The predecessor `identity_change_count=800` tuple/list representation false positive was ignored as directed; canonical P11 equals P10.

Q11 was sparse-loaded exactly once. The loaded CSR component identities matched the accepted identities above. No policy map, utility map, D2/Q assembly, HJB update or checkpoint-12 work occurred.

## Structural and conservation audit

| Diagnostic | Result |
|---|---:|
| shape / format | `800 x 800` / CSR |
| nnz | 3,118 |
| finite data | PASS |
| negative off-diagonal count | 0 |
| minimum exact-positive off-diagonal | `2.7404782515125115e-06` |
| exact-positive directed edges | 2,318 |
| `max(abs(Q11 @ 1))` | `1.7763568394002505e-15` |
| frozen conservation bound | `1.8450485966201867e-14` |
| serialized diagonal/off-diagonal reaggregation error | `1.7763568394002505e-15` |

`Q11 @ 1` was evaluated exactly once. The accepted D2 receipt was bound and Q11 was not reassembled.

## Exact-positive topology

Exactly one directed graph and one SCC decomposition were performed.

- SCC count: `13`;
- SCC sizes: one component of size `320` and twelve components of size `40`;
- closed communicating classes: `1`;
- closed-class size: `320`;
- closed-class membership: F-order flat indices `240..399` and `640..799`;
- transient states: `480`;
- exact-positive edge count: `2,318`;
- SCC labels SHA-256: `1C770FA23F2D8BC84AA86A79A4A0639E5522A91137D46358E205CF0C5A9512D0`.

The Q11 membership was discovered from exact-positive edges and was not imposed from historical Q1.

## Full dense SVD and rank/nullity

Exactly one call used:

`scipy.linalg.svd(A, full_matrices=True, lapack_driver="gesvd", check_finite=True)`

with `A=Q11.T` and no removed or replaced row.

| Diagnostic | Value |
|---|---:|
| numerical rank / nullity | `799 / 1` |
| singular values at or below `tau_rank` | 1 |
| `sigma_max` | `18.528640726738875` |
| second-smallest singular value | `3.400562953690602e-06` |
| smallest singular value | `1.2380844366549938e-16` |
| frozen `tau_rank` | `3.554655589411806e-12` |
| second-smallest / `tau_rank` | `956650.473767361` |
| smallest / `tau_rank` | `3.482994077802799e-05` |
| warnings | none |

Structural closed-class count and numerical nullity both equal one.

## Source-free invariant mass

The right singular vector associated with the smallest singular value required no sign reversal. Exactly one global orientation decision and one total-mass normalization were performed. Persisted arrays were not clipped, absolutized, truncated or renormalized.

| Diagnostic | Value | Frozen bound/status |
|---|---:|---:|
| `||Q11.T @ p||inf` | `1.9114484300919443e-16` | `tau_stationarity=6.317146315298578e-13`, PASS |
| normwise backward ratio | `5.804911693166085e-17` | `gamma_864=1.9184653865526386e-13`, PASS |
| `fsum(Q11.T @ p)` | `1.1943084172147506e-17` | source bound `5.053717052238863e-10`, PASS |
| `dot(Q11 @ 1,p)` | `3.2524065327241317e-18` | source bound, PASS |
| source identity discrepancy | `8.690677639423375e-18` | source bound, PASS |
| `math.fsum(p)` | `0.9999999999999999` | probability bound `1.7763568394005786e-13`, PASS |
| `omega*math.fsum(g)` | `0.9999999999999999` | density bound `1.7807977314990808e-13`, PASS |
| minimum p | `-1.4797178815899388e-16` | `-tau_nonnegative=-1.9184653865526386e-13`, PASS |
| negative stored entries | 191 | diagnostic only |
| total negative mass | `3.612331458450193e-15` | bound `1.5347723092421108e-10`, PASS |

Both p and `g=p/omega` are finite. Their ranges are:

- p: `[-1.4797178815899388e-16, 0.16083873102403526]`;
- g: `[-7.631116503628112e-16, 0.8294683128525246]`.

Persisted array identities:

- artifact: `1DD70201EAC5EED0AE768362D99A76736276BFB4D5E6AF0D8DBDB4E9D6FE7D16`;
- p: `E215FAE862DA81AD6DEB603859709EA0CF73B8F6F1897567DF942B186CD65ED7`;
- g: `D02592257722313B81C7A1DB40B799ADED8E8BDB5100A65C469E0997DA22E1CE`;
- stationarity residual: `8711794D28F3EEECC5F316B0AB69625E9CEFA72823556BA86F0EBEE75EDF6ED7`.

## Exact scientific ledger

| Operation | Count |
|---|---:|
| exact Q11 sparse loads | 1 |
| structural/conservation audits | 1 |
| `Q11 @ 1` | 1 |
| exact-positive graph constructions | 1 |
| SCC decompositions | 1 |
| full dense `gesvd` | 1 |
| normalized stationary candidates | 1 |
| global sign orientations | 1 |
| total-mass normalizations | 1 |
| `Q11.T @ p` | 1 |
| scientific retries / solver substitutions | `0 / 0` |
| iterative eigensolver/nullspace solves | 0 |
| row-replaced/direct KFE solves | 0 |
| policy maps / selectors / roots | `0 / 0 / 0` |
| D2/Q11 reassemblies | 0 |
| HJB solves or updates / checkpoint-12 work | `0 / 0` |
| damping, relaxation, adaptive Delta or continuation | 0 |
| clipping, artificial diffusion or parameter continuation | 0 |
| MATLAB / production / outer / firm / GE / annual / shock / IRF / Results | 0 |

Resource readback: wall time `1.525664599990705` seconds of 300 seconds; peak resident memory `100,478,976` bytes of 2 GiB.

## Engineering validation and evidence seal

- focused Q0/Q1/Q11 tests: `21 passed`;
- `py_compile`: PASS;
- `git diff --check`: PASS;
- scientific code freeze before/after: exact match.

Evidence root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint11_terminal_source_free_kfe_validation_20260920_run001`

Sealed manifest independent readback:

- SHA-256: `B7C06E3C369B6A5400DE76252DD70A539EFF1F2E4072C04639A1E93E512F5C1D`;
- entries: `12`;
- bytes: `41,890`;
- path/size/SHA-256 failures: `0`.

The twelfth entry is a post-execution protected-scope attestation that makes the zero counts for production, welfare, pin equations, row replacement, source RHS, balancing sources, clipping, absolute-value repair, second normalization and tolerance tuning explicit. Adding this serialization-only receipt and resealing the manifest performed no scientific calculation or retry.

## Interpretation boundary

This result establishes a terminal source-free invariant mass for the accepted finite Q11 and therefore a conditional household HJB-KFE fixed-point candidate at frozen prices/calibration. It does not establish production replacement, market clearing, GE, annual dynamics, shocks, IRFs, welfare or Results eligibility. No `CURRENT` file was modified, main was not merged and no successor was published.
