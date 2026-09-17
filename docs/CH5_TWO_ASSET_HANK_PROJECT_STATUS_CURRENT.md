# Chapter 5 两资产 HANK 当前状态

更新：2026-09-17。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`Q1_SOURCE_FREE_KFE_ACCEPTED__NONLINEAR_FIXED_POINT_DESIGN_BLOCKED_ON_OWNER_CONVERGENCE_LAW__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted scientific checkpoint

Owner-adopted D1/D2/D3 corrected semantics、lower-a zero-kink multiplier handling、interior zero-liquid Z switching、Option-A V0 map/Q0、一次 direct HJB step V1、V1 remap Q1，以及 Q1 source-free unique invariant mass均已接受。Source-faithful/production paths remain frozen。

## Nonlinear fixed-point design gate

Zero-science design candidate `ee83051d40c1389618288cef61d7d97711c1a861` is accepted by `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`.

Accepted design freezes the nonlinear state as `V_n`; each same-value checkpoint freshly derives `P_n,u_n,Q_n`, computes stationary Bellman residual and stability diagnostics, and only if the Owner-bound convergence law passes may it proceed to one terminal topology/KFE validation on the same `Q*`. KFE is not run every iteration. `Delta=1000` remains fixed. Damping、relaxation、adaptive Delta、continuation、clipping 和 artificial diffusion remain unauthorized.

The accepted resource ceiling is at most 100 total HJB updates for this call-725 corrected trajectory; the accepted `V0->V1` update has consumed update 1, leaving at most 99 future updates through `V100`.

## Owner decision gate

No active Builder scientific task exists.

Owner decision is required before any further selector/policy-map/D2/HJB continuation call. The repository does not yet freeze a corrected-target convergence law for:

- Bellman residual threshold;
- value-change threshold and conjunction rule;
- whether policy/operator stability is mandatory or diagnostic;
- prospective linear-solve backward-error rejection bound;
- non-exact cycling/oscillation criterion and window.

Historical `max|V_new-V_old|<1e-7` remains provenance only and cannot be silently promoted to corrected-target authority. Results eligibility remains `FALSE` and production replacement remains unauthorized.
