# CH5 MP4C 2018 KFE D1-D3 bounded nonlinear HJB-KFE continuation

Date: 2026-09-17

Task: `CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_20260917`

## Terminal verdict

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

Checkpoint 1 did not satisfy the Owner-adopted primary convergence law. Its
single authorized `V1 -> V2` direct solve passed the frozen linear-solve
accuracy gate. The fresh checkpoint-2 corrected policy map then stopped at its
first failure: F-order flat index 100, `(b,a,z)` index `(0,5,0)`, returned
`NO_ADMISSIBLE_POLICY`. No later selector, D2 assembly, Bellman metric, cycle
gate, HJB solve, topology gate or KFE call was executed.

This failure was preserved without scientific repair or retry. No conditional
household HJB-KFE fixed point was established.

## Git and startup identity

- Fresh-fetched live-main baseline:
  `a0ccb9801abc5bda4357c59ae2ab51acb273a34b`.
- Baseline worktree gate: clean and `0/0` ahead/behind `origin/main`.
- Task branch:
  `codex/ch5-mp4c-2018-kfe-d123-bounded-nonlinear-hjb-kfe-continuation-20260917`.
- Candidate SHA is established after this report, evidence and implementation
  are committed, ordinarily non-force pushed, and remotely read back. An
  immutable commit cannot contain its own SHA without changing that SHA.
- The pre-existing registered `main` checkout was not modified; it contained
  unrelated deletions and was 306 commits behind after fetch, so execution used
  a new isolated worktree from exact live `origin/main`.

One preliminary launcher command lacked the repository `src` entry on
`PYTHONPATH` and stopped at module resolution with `ModuleNotFoundError`. It did
not import the continuation module, create the evidence root, load an artifact,
or enter any scientific gate. The unchanged frozen implementation was then
started with the repository-local `src` import path. This was a launcher-layer
correction, not a scientific retry; the scientific ledger records zero retries.

## Accepted checkpoint binding

Checkpoint 1 reused the accepted evidence and did not rerun its policy map:

| Object | Verified identity |
|---|---|
| `V0` field | `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665` |
| `V1` field | `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2` |
| V1 direct-step artifact | `28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173` |
| accepted P1/u1 receipts | 800/800 `SELECTED_ADMISSIBLE` |
| `Q1` artifact | `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E` |
| Q1-remap sealed manifest | `573FCF61220E5982EB4A6E78FAFC5D82310BAC7F7638D2D83B576B1420DDCF37` |
| accepted p1/g1 artifact | `14E6EC29650A7F9F5D95B023E5B6E54AC1391DC836E2513AC9CACAFEEB7B4254` |

The current Git blobs for the frozen selector, generator and Option-A adapter
matched their accepted authority blobs exactly. Input seed, scalar binding,
grid, F-order convention, productivity generator and `Delta=1000` also passed
the exact preflight identities recorded in
`accepted_checkpoint_1_binding.json`.

## Checkpoint 1 raw metrics

| Metric | Raw value | Gate |
|---|---:|---:|
| stationary Bellman residual `B1` | `0.014710294187010184` | `<=1e-8` — FAIL |
| value change `D1` | `0.47118375690461445` | `<=1e-7` — FAIL |
| V1 hash | `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2` | exact accepted |
| Bellman-residual field hash | `3F6715C726E6CF12245615E891EB13A09848B4347331F429EDA1326540146BA3` | persisted |
| value-change field hash | `003FA00B7FAAF935505C3DDF7E022C7EB89735D4CDD6714451C1FA226076C78E` | persisted |
| P1 identity hash | `8BA4BBE3F62863E4FDA4D0255FB2C70C19ED32686A94CE9FDE4EB828E258EB1D` | accepted receipts |
| full checkpoint identity | `9FDEB1724653BF5B71FD518F65CEFF68EF222ADEEEEE976322E2172ED41D1BD0` | persisted |

Primary convergence was evaluated before cycle detection. Neither exact nor
authorized approximate period-2/3 recurrence was available at checkpoint 1.

## Sole new direct HJB update

The accepted P1/u1/Q1 objects were used directly for the only new solve; no V1
selector map or Q1 D2 reassembly occurred.

| Quantity | Raw value |
|---|---:|
| update | `V1 -> V2` |
| solver | `scipy.sparse.linalg.spsolve` |
| `Delta` | `1000` |
| warnings | `0` |
| original-equation residual infinity norm | `1.9012569296705806e-14` |
| normwise denominator | `74.51786040735358` |
| normwise backward error | `2.5514110567283015e-16` |
| frozen backward-error bound | `<=1e-12` — PASS |
| V2 field hash | `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1` |
| direct-update arrays artifact | `FD8456D533A724BCD8099AF52A8AB7559EF3A99C6307E4ED85CB02A618CEFA16` |

## First checkpoint-2 gate failure

The new V2 map persisted every attempted cell receipt before advancing. Cells
0 through 99 passed. Cell 100 was the first terminal failure:

| Field | Raw value |
|---|---|
| flat F index | `100` |
| `(b,a,z)` zero-based index | `(0,5,0)` |
| physical `(b,a,z)` | `(-2.0, 2.63157894736842, 0.8)` |
| cell ID | `v002_f0100_b000_a005_z000` |
| `p_b_backward` | `0.0123333112067166` |
| `p_b_forward` | `0.0123333112067166` |
| `p_a_backward` | `0.00903315440190679` |
| `p_a_forward` | `0.00895700719429522` |
| selector outcome | `NO_ADMISSIBLE_POLICY` |
| admissible comparison count | `0` |
| cumulative selector evaluations | `101` |
| cumulative scalar-root invocations | `51` |
| cumulative interior-Z roots | `20` |

The persisted candidates contain rejection reasons including derivative-direction
inconsistency, lower-b primal infeasibility, transfer KKT/sign failures and one
`ROOT_FAILURE_NO_UNIQUE_BRACKET`. These are raw selector evidence, not authority
to alter the frozen equations or introduce a repair.

Because the failure occurred before completion of the 800-cell V2 policy map:

- no P2/u2 complete-map claim exists;
- no D2/Q2 assembly was attempted;
- `B2`, `D2`, policy/operator stability and cycle metrics are `NOT_COMPUTED` by
  the frozen order;
- the last complete same-value checkpoint is checkpoint 1;
- V2 exists only as the accepted output of the passing V1 direct solve and the
  input to the partial checkpoint-2 selector attempt.

## Complete scientific ledger

| Operation | Calls |
|---|---:|
| accepted V1 artifact loads | 1 |
| accepted Q1 loads | 1 |
| new corrected policy maps attempted | 1 |
| selector evaluations | 101 |
| scalar-root invocations | 51 |
| interior-Z root invocations | 20 |
| D2 assemblies | 0 |
| direct HJB solves | 1 |
| ordinary graph/SCC summaries | 0 |
| terminal topology gates | 0 |
| terminal dense GESVD | 0 |
| terminal normalized stationary candidates | 0 |
| terminal `Q.T @ p` | 0 |
| scientific retries | 0 |
| solver substitutions | 0 |
| damping/relaxation/adaptive-Delta/continuation calls | 0 |
| MATLAB/production/GE/IRF/Results calls | 0 |

Unused selector/root/D2/HJB/KFE budget was not reused.

## Durable evidence and verification

Evidence root:
`reports/ch5_mp4c_2018_kfe_d123_bounded_nonlinear_hjb_kfe_continuation_20260917/`

- root sealed manifest: 114 entries, 1,681,407 bytes before the manifest itself;
- root sealed-manifest SHA-256:
  `FC323B9691E28F20305CF5F71DD379C445CB80A506313A67DBC1954E88A5E041`;
- checkpoint-1 sealed-manifest SHA-256:
  `EEC3F27BC7C9684F43107860796C4B99E5D21B6E204F4D7001359DC40F3DA767`;
- pre/post scientific-code hash maps match exactly;
- focused D123 tests before the scientific run: 67 passed;
- `py_compile` / `compileall`: PASS;
- `git diff --check`: PASS;
- Ruff: `UNAVAILABLE` in the existing Python environment; it was not installed
  or used as a reason to alter the environment.

A broader `pytest tests -k ...` command was intentionally abandoned at collection
because unrelated historical tests produced 14 import/oracle-identity collection
errors before the focused D123 selection could run. The exact ten D123 test files
were then passed explicitly and all 67 tests passed. This did not execute or retry
the scientific continuation.

## Interpretation boundary

The run establishes only that checkpoint 1 fails the adopted nonlinear HJB
convergence law, its one V1-to-V2 direct solve meets the prospective linear
accuracy bound, and the frozen corrected selector has no admissible policy at
the first failing V2 cell identified above. It does not establish nonlinear HJB
convergence, terminal KFE validity for V2, a conditional household fixed point,
GE, market clearing, production replacement, calibration validity, dynamics,
IRFs, causal interpretation or paper Results.

Results eligibility remains `FALSE`. Main is not merged and no successor task
is published by this Builder task.
