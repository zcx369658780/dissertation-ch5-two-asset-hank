# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-17。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Results eligibility=`FALSE`。

## Accepted route

The frozen source-faithful reference and separately governed corrected successor remain distinct. Owner-adopted corrected semantics include D1 upper numerical state constraints, D2 consumed-total-drift conservative assembly, D3 regularized-cost-consistent KKT, active lower-a zero-kink multiplier handling, and interior zero-liquid Z switching.

## KFE-D2C/D/E — accepted corrected household checkpoints

The corrected route now has:
- accepted V0 800-cell policy map and Q0;
- one accepted direct HJB update `V0->V1`;
- accepted V1 remap and Q1;
- Q1 exact-positive single closed class `[5,6,405,406]`;
- accepted pin-free/source-free unique Q1 invariant mass with rank/nullity `799/1`.

These are household/operator diagnostics only until nonlinear HJB convergence is established.

## KFE-D2F-A — nonlinear HJB-KFE fixed-point design accepted

Zero-science candidate `ee83051d40c1389618288cef61d7d97711c1a861` is accepted. It freezes nonlinear state `V_n`, same-value derived `(P_n,u_n,Q_n)`, fixed `Delta=1000`, terminal-only KFE timing and a maximum 100 total HJB updates.

## KFE-D2F-B — Owner convergence law adopted

Owner adoption:
`docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`.

Frozen law:

1. stationary Bellman residual `||R_n||_inf <= 1e-8`;
2. value change `||V_n-V_(n-1)||_inf <= 1e-7`;
3. both conditions required at the same checkpoint;
4. policy/operator stability are mandatory diagnostics only;
5. direct-solve normwise backward error `<=1e-12`;
6. exact period `k>=2` full-checkpoint recurrence stops fail-closed before convergence;
7. approximate periods 2 and 3 use complete lag-k windows with `||V_j-V_(j-k)||_inf <=1e-8` after the primary convergence test fails;
8. total update ceiling 100, with `V0->V1` already consuming update 1;
9. no damping, relaxation, adaptive Delta, parameter continuation, clipping, artificial diffusion, solver substitution, scientific retry or post-hoc tolerance tuning.

## KFE-D2F-C — active bounded nonlinear continuation

Active task:
`tasks/CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_20260917.md`.

The task starts from the exact accepted V1/P1/u1/Q1 checkpoint. It evaluates V1 first and may then execute at most 99 additional fixed-Delta HJB updates, ending no later than V100. Every new value checkpoint requires a complete corrected policy remap, D2 operator assembly, same-value Bellman/value/stability evidence and fail-closed cycle/linear-solve checks before another update.

No KFE is executed during ordinary HJB rounds. If an HJB convergence candidate is reached, no further update is allowed; the final same-value Q* then proceeds directly to the accepted single-closed-class topology gate and exactly one pin-free/source-free KFE validation.

A full PASS establishes only a conditional household HJB-KFE fixed point under the frozen call-725 prices/calibration. It does not establish GE, market clearing, production replacement or paper Results.

## KFE-D3 — later production closure

Corrected multi-province production replacement, market clearing, GE/annual/dynamics/IRF and Results remain downstream gates with separate evidence and authority.

Capital/labor K1/C1/K1B/K2 routes remain deferred, not abandoned, behind the current household fixed-point route.