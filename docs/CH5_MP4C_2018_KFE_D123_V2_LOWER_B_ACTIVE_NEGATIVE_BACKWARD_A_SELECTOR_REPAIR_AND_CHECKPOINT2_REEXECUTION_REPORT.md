# CH5 MP4C 2018 KFE D123 V2 lower-b selector repair and checkpoint-2 reexecution report

Date: 2026-09-19

Task: `CH5_MP4C_2018_KFE_D123_V2_LOWER_B_ACTIVE_NEGATIVE_BACKWARD_A_SELECTOR_REPAIR_AND_CHECKPOINT2_REEXECUTION_20260917`

## Terminal verdict

`FAIL__REPAIRED_SELECTOR_CHECKPOINT2_POLICY_MAP_OR_D2_GATE`

The authorized selector coverage defect was repaired and the focused engineering gate passed. The single fresh V2 policy-map attempt then failed closed at checkpoint 2, flat F index 100, because the repaired selector still produced `NO_ADMISSIBLE_POLICY`. The newly represented lower-b active negative-transfer/backward-`a` branch reached a genuine root, but its resulting positive illiquid drift was inconsistent with the frozen backward-`a` direction. No Q2 or checkpoint-2 Bellman/value/stability/cycle result exists.

Results eligibility: `FALSE`.

## Git and execution binding

- live `origin/main` baseline after fresh fetch: `5b2e7e159945a70a53fcc5920e2273ae54844be9`
- task branch: `codex/ch5-mp4c-2018-kfe-d123-v2-lower-b-active-negative-backward-a-selector-repair-checkpoint2-20260917`
- implementation freeze commit: `f66157a15447eac1f2061dc70f37fd8e690da6a2`
- final pre-science freeze commit: `52277adbedda043f2767cb60d6d89847ae331080`
- final pre-science tree: `97ab9813857e1283e8402025f07cdc3d382578e9`
- accepted V2 field SHA-256: `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`
- predecessor selector SHA-256: `C60C584A44A143CB584563ACDAA8F7E30EBC1CA45B90F8AF39728D40AC70E5E6`
- repaired selector SHA-256: `DBEB8EDCDA18B14579F36C2B68A50A47C9E717F49E84BC31A2E4E17180E9C327`

The run loaded the accepted V1 artifact, accepted V2 artifact, and accepted Q1 once each. The V2 binding gate passed. Neither the V1 policy map nor the V1-to-V2 HJB solve was rerun.

## Authorized repair

Only the corrected-diagnostic route was changed. The lower-b active negative-transfer derivative pre-screen now uses `q_b >= max(p_b, tiny)` and separately represents every frozen-law-legal interior-`a` direction. The upper-b screen retains its distinct `0 < q_b <= p_b` domain and one-root fail-closed behavior.

The repair did not change the root equation, root tolerance, KKT law, transfer law, zero-kink behavior, positive-transfer behavior, interior-Z law, D2 law, HJB update law, `Delta=1000`, convergence thresholds, solver, grid, calibration, data, source-faithful path, or production path.

An additive checkpoint-2-only execution helper enforced the task budget: one V2 map, Q2 only after a complete 800-cell map, and no HJB solve or KFE route.

Changed paths relative to the live-main baseline are exactly:

- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/checkpoint2_reexecution.py`
- `tests/test_mp4c_2018_kfe_d123_lower_b_active_negative_backward_a.py`
- the preserved pre-science blocked evidence root named below (5 files)
- the formal `run001` evidence root named below (109 manifest entries plus its sealed manifest)
- this execution report

## Engineering verification

The exact focused set comprised nine test files. Result:

- tests: 53
- passed: 53
- failures/errors/skips: 0/0/0
- JUnit SHA-256: `9EE766FC00FC5ABCFA64055D61F1396F971A51C07F9272E1FB73BEFC97F36F37`
- `py_compile`: PASS

Coverage included lower-b active negative/backward-`a`, lower-b active negative/forward-`a`, upper-b domain non-regression, the cell100 eighth-case census, positive active no-root rejection, boundary-node interior-Z unavailability, and affected D1/D3/KKT/selector behavior. No tolerance was weakened and no assertion was deleted.

## Pre-science launcher receipt

The first launcher invocation stopped before artifact loading or scientific entry with:

`BLOCKED__IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENTIFIC_RUN`

The preflight incorrectly compared worktree bytes against a Git-normalized selector identity and checked cleanliness after creating its own evidence root. This was corrected within the task's explicit launcher/preflight allowance by binding to the Git blob identity and capturing cleanliness before evidence creation. The blocked evidence root was preserved at:

`reports/ch5_mp4c_2018_kfe_d123_v2_lower_b_active_negative_backward_a_selector_repair_checkpoint2_reexecution_20260917/`

Its scientific ledger is entirely zero: artifact loads 0; maps 0; selector evaluations 0; scalar roots 0; interior-Z roots 0; D2/Q2 assemblies 0; checkpoint diagnostics 0; HJB/KFE and all downstream calls 0. It did not consume or reset the single scientific attempt.

## Single scientific execution

Fresh no-overwrite evidence root:

`reports/ch5_mp4c_2018_kfe_d123_v2_lower_b_active_negative_backward_a_selector_repair_checkpoint2_reexecution_20260917_run001/`

Cells 0 through 99 completed. Static receipt comparison against the predecessor checkpoint-2 attempt found zero selected-policy identity changes and maximum absolute change 0 for controls, drifts, and utility. The first failure was cell 100:

- flat F index: `100`
- zero-based index `(i_b,i_a,i_z)`: `(0,5,0)`
- state `(b,a,z)`: `(-2.0,2.6315789473684212,0.8)`
- outcome: `NO_ADMISSIBLE_POLICY`
- candidate count: 8, versus 7 before repair
- scalar roots at this cell: 4, versus 3 before repair
- interior-Z roots at this cell: 0
- admissible comparisons: 0

The added eighth case is:

- active set: `lower_b`
- transfer: `negative`
- `a` derivative: `backward`
- root status: `ROOT_CONVERGED`
- `q_b = 0.012457851515416401`
- `d = -0.23013514168909557`
- canonical `g_b = 0`
- `g_a = 0.00670682022114244`
- rejection: `A_DERIVATIVE_DIRECTION_INCONSISTENT`

The authority-backed active negative/forward-`a` case also reached a root:

- `q_b = 0.012447419227151839`
- `g_a = -0.0005429159000894801`
- rejection: `A_DERIVATIVE_DIRECTION_INCONSISTENT`

The active positive-transfer case remained the frozen legal rejection `ROOT_FAILURE_NO_UNIQUE_BRACKET`; no root was fabricated. Boundary-node interior-Z remained unavailable.

## Scientific ledger

| Call or route | Count |
|---|---:|
| accepted V1 artifact loads | 1 |
| accepted V2 artifact loads | 1 |
| accepted Q1 loads | 1 |
| fresh V2 policy maps | 1 |
| selector evaluations | 101 |
| scalar-root invocations | 56 |
| interior-Z root invocations | 20 |
| D2/Q2 assemblies | 0 |
| checkpoint-2 diagnostic evaluations | 0 |
| direct HJB solves | 0 |
| V2-to-V3 HJB updates | 0 |
| ordinary graph/SCC summaries | 0 |
| terminal topology gates | 0 |
| KFE/SVD/eigen/nullspace/normalized stationary candidates/`Q.T@p` | 0 |
| MATLAB/production/outer/firm/GE/annual/shock/IRF/Results | 0 |
| scientific retries | 0 |
| solver substitutions | 0 |
| damping/relaxation/adaptive Delta/continuation | 0 |

The scientific-code pre- and post-execution hash maps are identical.

## Durable evidence

- formal manifest entries verified: 109/109
- manifest total bytes: 1,619,867
- sealed manifest SHA-256: `55B689DCF4DD547CAE650A1353062390148050BC2EE95EA51E16571C2CB30947`
- cell100 receipt SHA-256: `3F46413C628B253ED7EA2E96799CA2B52DBB7E961C9D9934CAAC045BAC3FCD66`
- derivative receipt SHA-256: `8224728E2EC63D64184F8D02C02E3F41AE0CEE9582EC93F9050E250966B0148E`

Because the policy map did not complete, P2, u2, and Q2 are `NOT_COMPUTED`. Consequently B2, D2, policy/operator stability, Q2-Q1, exact-cycle, and approximate period-2/3 diagnostics are also `NOT_COMPUTED`. No terminal topology or KFE gate was entered.

## Scope closure

The task stops at the first checkpoint-2 selector failure. No second scientific repair or retry was attempted. Main was not merged, no successor task was published, and no production, GE, IRF, or Results claim is supported.
