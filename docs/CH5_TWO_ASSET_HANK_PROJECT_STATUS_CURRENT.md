# Chapter 5 两资产 HANK 当前状态

更新：2026-09-17。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`OWNER_CONVERGENCE_LAW_ADOPTED__BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted scientific checkpoint

Owner-adopted D1/D2/D3 corrected semantics、lower-a zero-kink multiplier handling、interior zero-liquid Z switching、Option-A V0 map/Q0、一次 direct HJB step V1、V1 remap Q1，以及 Q1 source-free unique invariant mass均已接受。Source-faithful/production paths remain frozen。

## Nonlinear fixed-point design and convergence law

Zero-science design candidate `ee83051d40c1389618288cef61d7d97711c1a861` is accepted by `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`.

Owner convergence-law adoption is recorded in:
`docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`.

The frozen corrected-target law is:

- same-value stationary Bellman residual `||R_n||_inf <= 1e-8`;
- value change `||V_n-V_(n-1)||_inf <= 1e-7`;
- both conditions are required at the same checkpoint;
- policy/operator stability are mandatory diagnostics, not terminal convergence conditions;
- every direct implicit HJB solve requires normwise backward error `<=1e-12`;
- exact recurrence of full checkpoint identity at period `k>=2` before convergence is fail-closed;
- approximate period-2/3 cycles use complete lag-k windows with `||V_j-V_(j-k)||_inf <=1e-8` and stop only after the primary convergence test has failed;
- at most 100 total HJB updates, with `V0->V1` already consuming update 1;
- `Delta=1000` fixed; damping、relaxation、adaptive Delta、continuation、clipping、artificial diffusion、solver substitution、scientific retry and post-hoc tolerance tuning remain unauthorized.

## Active Builder task

`tasks/CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_20260917.md`

The Builder must fresh-fetch live `main`, bind exact accepted V1/P1/u1/Q1 provenance, evaluate checkpoint V1 under the adopted law, and if necessary continue no later than V100. Each new checkpoint must be fully derived and sealed before another update. The task is fail-closed on first selector/root/D2/linear-solve/evidence/cycle/ceiling failure.

If the HJB convergence candidate is reached, the same-value final Q* may proceed to the already accepted terminal topology and pin-free/source-free KFE gate. A PASS establishes only a conditional household HJB-KFE fixed point at frozen prices/calibration.

No production replacement、GE、market-clearing、annual calibration、dynamics、IRF、MATLAB or Results work is authorized. Results eligibility remains `FALSE`.