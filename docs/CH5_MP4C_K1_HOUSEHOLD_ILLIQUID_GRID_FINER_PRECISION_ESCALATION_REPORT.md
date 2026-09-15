# CH5 MP4C K1 — household illiquid-grid finer precision escalation report

Date: 2026-09-15

Terminal classification:

`ILLIQUID_GRID_FINER_PRECISION_NUMERICAL_FAILURE__NO_SCIENTIFIC_RETRY_AUTHORIZED`

Results eligibility=`FALSE`.

## Repository and authority

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Fresh-fetched actual baseline: `3f4a87af4927643f2f80f407ed8b207d41fb8718`
- Branch: `codex/ch5-mp4c-k1-illiquid-grid-finer-precision-escalation-20260915`
- Worktree: `D:\ProjectTemp\ch5-mp4c-k1-illiquid-grid-finer-precision-escalation-20260915-001`
- Accepted precision candidate reused: `de4994c22303e30be9cd4c22c0a5c7f7a00db88a`
- Accepted J160 science was reused without runtime.

The live oracle, protected MATLAB source, accepted grid-generic runner/finalizer, and accepted J160 evidence hashes all matched the frozen preflight identities. Only the new task-owned runner, finalizer, focused tests, report, and compact evidence were changed. Accepted household science, HJB/KFE numerics, parameters, bounds, mappings, guards, tolerances, and maximum iterations were not changed.

## Frozen inputs

The execution held `rb=.02`, `ra=.0675`, `w=15.5`, `a=[0,100]`, `b=[-2,20]`, `h=1`, `I=20`, and `Nz=2` fixed. The three new initial-value and baseline-labor objects were independently constructed before science; only `grid.a` varied. No warm start was used.

## Point results

| Point | HJB | Iterations | Final max abs dV | max A2max | KFE | At | Bt | modal a | modal b |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| accepted J160 | converged | 16 | 2.26131e-10 | 0.00151288 | valid | 89.29782531 | 5.81025383 | 94.33962264 | 2.63157895 |
| J320 | converged | 44 | 3.58192e-08 | 0.00151288 | valid | 89.16979926 | 5.81764933 | 95.29780564 | 2.63157895 |
| J640 | not converged | 100 | 0.0012277767 | 0.00151288 | not authorized | unavailable | unavailable | unavailable | unavailable |
| J1280 | not started after invalid-point hard stop | — | — | — | not authorized | unavailable | unavailable | unavailable | unavailable |

J640 had no illegal iteration, no hard error, and finite shape-valid HJB scientific arrays, but it did not meet the frozen convergence tolerance by frozen maxit=100. Therefore KFE was not legal for J640. The task's invalid-point stop then prohibited starting J1280. This is numerical nonconvergence evidence, not an economic or domain-pathology finding.

For J320, KFE total mass was 1, raw residual infinity norm was `5.13478e-15`, raw density minimum was `-6.27533e-19`, and 380 density entries were negative at numerical scale. The raw signed density was persisted before receipt construction and was not clipped, smoothed, or science-changing renormalized. J320 aggregates were `Ct=14.26116231`, `Lt=0.62798566`, `At=89.16979926`, and `Bt=5.81764933` (`Bt_pos=5.81764933`, `Bt_neg=2.54620e-18`).

## Precision comparison

J160→J320 is the only new complete pair:

- `Delta Ct=+0.00236260`
- `Delta Lt=-0.00007391`
- `Delta At=-0.12802605`
- `Delta Bt=+0.00739550`
- modal `a`: `94.33962264 -> 95.29780564` (`+0.95818300`)
- modal `b`: unchanged at `2.63157895`
- signed a-marginal CDF distance: `0.0021292541`
- signed b-marginal CDF distance: `0.0007585373`
- a upper-node quantiles: p90 `-0.61315826`, p95 `-0.92860945`, p99 `-0.93058102`
- `amax` mass: `0 -> 0`
- `bmax` mass: `0.0009774012 -> 0.0010587541`

The J160→J320 aggregate and marginal distances are descriptively smaller than the preceding J80→J160 changes. That single comparison is insufficient to establish a stabilization sequence: modal `a` still moves upward, upper quantile locations still move, and neither J320→J640 nor J640→J1280 has KFE evidence.

## Answers to the scientific questions

1. **At stabilization:** unresolved. J160→J320 changes only `-0.12803`, but the required two later comparisons are unavailable.
2. **Modal a:** it continues moving toward the upper domain at J320, from `94.33962` to `95.29781`; stabilization is not established.
3. **Full a marginal:** the J160→J320 signed-CDF distance falls to `0.00212925`, but no multi-step finer sequence exists, so full-marginal stabilization is unresolved.
4. **amax=100:** at J320 the endpoint mass remains exactly zero and is descriptively nonbinding for that completed point. A general finer-J conclusion is unavailable.
5. **bmax=20 at fixed I20:** J320 bmax mass remains small (`0.00105875`) and modal b remains interior. This supports only descriptive nonbinding at the completed fixed-I20 point, not liquid-grid precision.
6. **Old-domain jump decomposition:** the dominant old-domain→expanded-domain response remains supported because completed expanded-domain levels stay near the high-80s. A converged discretization component is not established because the finer ladder terminated at J640 HJB nonconvergence.
7. **Smallest defensible tested J:** none for bounded confirmation; J320 is a valid completed diagnostic point but is not a defensible stabilized-grid minimum.
8. **Interpretation:** precision remains unresolved because the frozen J640 HJB did not converge. The evidence does not establish stabilization by J1280 and does not, by itself, convert the numerical failure into domain/scale evidence.

Exactly one next Reviewer gate:

`REVIEWER_NUMERICAL_FAILURE_ROUTE_DECISION`

No J beyond 1280, liquid-I ladder, cross-state confirmation, domain change, recalibration, global model, GE, shock, IRF, downstream, or Results execution occurred.

## Call ledger and evidence

- New HJB calls: 2 started / 2 completed (J320 and J640)
- New KFE calls: 1 started / 1 completed (J320 only)
- J1280 HJB/KFE: 0/0 due to the task's invalid-point hard stop
- Scientific retries: 0
- Engineering retries: 0
- Global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results: all 0

Compact evidence is under `docs/evidence/ch5_mp4c_k1_household_illiquid_grid_finer_precision_escalation/`. Its sealed manifest contains 9 entries totaling 217,579 bytes excluding the manifest. Raw arrays and density are sealed in the external execution evidence rooted at `D:\ProjectTemp\ch5-mp4c-k1-illiquid-grid-finer-precision-evidence-20260915-001`.

KFE caveat: this remains the accepted standalone contaminated-row KFE diagnostic route. It does not resolve corrected-2018 multi-province finite-box upper-b leakage or MATLAB-style pinning and does not make Results eligible.
