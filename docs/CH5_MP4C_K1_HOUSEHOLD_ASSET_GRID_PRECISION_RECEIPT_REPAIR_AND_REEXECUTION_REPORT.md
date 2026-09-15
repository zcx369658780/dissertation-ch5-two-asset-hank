# CH5 MP4C K1 — household asset-grid precision receipt repair and re-execution report

Date: 2026-09-15

Task ID: `CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION`

## Terminal classification

`ILLIQUID_GRID_PRECISION_NOT_STABILIZED`

R0 repaired only the task-owned fixed-grid receipt route. The identical frozen P1 ladder then completed with three legal/converged HJBs and three valid KFE receipts. The final `J80→J160` refinement remained clearly material without a stabilization trend, so P2 was not authorized and did not run. Results eligibility=`FALSE`.

## Repository and execution identity

- Actual fresh-fetched baseline: `03f30ada29ef7cea8dd0ab8f27b090df607c0909`.
- Branch: `codex/ch5-mp4c-k1-grid-repair-reexecution-20260915`.
- Fresh isolated worktree: `D:\ProjectTemp\ch5-mp4c-k1-grid-repair-reexecution-20260915-001`.
- R0 evidence: `D:\ProjectTemp\ch5-mp4c-k1-grid-repair-r0-evidence-20260915-001`.
- P1 raw evidence: `D:\ProjectTemp\ch5-mp4c-k1-grid-repair-p1-evidence-20260915-001`.
- P2 evidence root was not created.
- Compact evidence: `docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution/`.
- Frozen oracle SHA-256: `F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8`.
- Frozen MATLAB source SHA-256: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.

## R0 repair result

R0 changed only the precision task runner, finalizer and focused test. The accepted oracle, original MATLAB source, accepted coarse KFE wrapper, historical J20-only wrapper and Stage-A runner were unchanged.

The repaired runner invokes the same accepted `solve_matlab_faithful_stationary_kfe` numerical solve. Immediately after it returns, the runner persists HJB arrays, raw KFE density, actual `grid.a/grid.b`, and density shape. Only then does task-owned grid-generic extraction calculate aggregates, marginals, modes, endpoints and top bins. Raw signed density is not clipped, smoothed or renormalized.

Focused tests cover `J={20,40,80,160}` and `I={20,40,80}`, marginal/support alignment, mass dimensions, modes, endpoints, top bins, signed-density preservation, persistence-before-validation failure, and full J20 receipt regression. R0 result: `17 passed`; `py_compile` passed; HJB/KFE science calls=`0/0`.

## Frozen inputs

All points used `rb=.02`, `ra=.0675`, `w=15.5`, `a=[0,100]`, `b=[-2,20]`, `h=1`, `I=20`, and distinct fresh source initializations. Only authorized `J` varied. No warm start or accepted-science change occurred.

## P1 point results

| J | da | HJB iterations | final `max|ΔV|` | max A2max | KFE residual | At | Bt | modal a | modal b | amax mass | bmax mass |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20 accepted | 5.2631578947 | 10 | 4.3042e-09 | 0.0015128765 | 7.9526e-17 | 87.75417323 | 4.15547167 | 89.47368421 | 2.63157895 | 0.14305022 | 6.5110e-34 |
| 40 | 2.5641025641 | 11 | 2.3046e-10 | 0.0015128765 | 1.1156e-16 | 87.55005489 | 4.26409999 | 89.74358974 | 2.63157895 | 0.05189374 | 0 |
| 80 | 1.2658227848 | 10 | 3.3535e-08 | 0.0015128765 | 1.1854e-17 | 88.60703574 | 5.02227287 | 92.40506329 | 2.63157895 | 0.01530756 | -4.7600e-18 |
| 160 | 0.6289308176 | 16 | 2.2613e-10 | 0.0015128765 | 8.1879e-16 | 89.29782531 | 5.81025383 | 94.33962264 | 2.63157895 | 0 | 0.00097740 |

All four KFE receipts have total mass within floating-point scale of one. Raw density minima are between `-2.38e-18` and `-3.64e-19`; these signed values were preserved. Every point retains `INTERIOR_A_DISTRIBUTION_CANDIDATE` and `B_INTERIOR_DISTRIBUTION_CANDIDATE`, but interiority does not establish precision stability.

## Pairwise precision evidence

| refinement | ΔAt | ΔBt | ΔCt | ΔLt | modal a change | Δamax mass | a-CDF distance | b-CDF distance |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| J20→J40 | -0.20411834 | +0.10862832 | +0.34427100 | +0.00518004 | 89.4737→89.7436 | -0.09115648 | 0.01261160 | 0.02747203 |
| J40→J80 | +1.05698085 | +0.75817287 | +0.32424935 | +0.00233563 | 89.7436→92.4051 | -0.03658618 | 0.01759636 | 0.03446240 |
| J80→J160 | +0.69078957 | +0.78798096 | +0.19968037 | -0.00082064 | 92.4051→94.3396 | -0.01530756 | 0.01462234 | 0.03581732 |

The last refinement remains material in `At`, `Bt`, modal `a`, and both marginal-distance measures. The a-CDF sequence `0.01261→0.01760→0.01462` does not show monotone stabilization, while modal `a` continues moving upward. Therefore P1 is `ILLIQUID_GRID_PRECISION_NOT_STABILIZED` under the preregistered descriptive rule. No post-result numeric threshold was introduced.

## Final questions

1. Repair scope: PASS. Only the fixed-grid receipt/persistence route changed; accepted science and numerical solvers did not.
2. `At`: not stabilized by `J=160`.
3. Modal `a`: not stabilized; it moves from `89.47` at J20 to `94.34` at J160.
4. Full `a` marginal: not stabilized; final signed-CDF distance remains `0.01462` without a declining trend.
5. `amax` mass: it declines from `0.14305` to zero, but this alone does not offset the moving mode/aggregate/marginal evidence; the full illiquid distribution is not stabilized.
6. Old `a=[0,10]` to expanded `a=[0,100]` At jump: primarily a domain response. At comparable spacing, J160 gives `At=89.30`, while old-domain At was about `7.14–7.33`; the finer-J component within the expanded domain is much smaller (`J20→J160: +1.54365`) but is still unresolved for the final level.
7. P2 did not run, so `Bt` and the liquid marginal were not checked with respect to `I`.
8. At fixed `I=20`, `bmax=20` remains nonmodal on every finer-J point and bmax mass is at most `0.0009774`; this supports nonbinding at the tested P1 points, not liquid-grid precision across I.
9. No minimum defensible `I/J` is established for cross-state confirmation because P1 did not stabilize by J160.
10. Exactly one next Reviewer gate: `FINER_PRECISION_ESCALATION`.

## Runtime ledger and evidence

- R0: HJB/KFE=`0/0`.
- Accepted J20 reference: HJB/KFE=`0/0` new calls.
- P1: HJB started/completed=`3/3`; KFE started/numeric-returned/persisted/valid-receipt=`3/3/3/3`.
- P2: HJB/KFE=`0/0`.
- Scientific retries=`0`; engineering retries=`0`.
- Global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=`0`.
- Compact manifest: 12 entries, 127,874 bytes excluding itself.
- External P1 manifest: 15 entries, 587,692 bytes excluding itself; manifest SHA-256 `C77D85511AAD5C7B50E99144A9E84EB9E232EE77B3D67AF834C109608AECB495`.

This remains standalone contaminated-row KFE diagnostic evidence. It does not resolve corrected-2018 multi-province finite-box/pinning, constitute recalibration authority, or make Chapter 5 Results eligible.
