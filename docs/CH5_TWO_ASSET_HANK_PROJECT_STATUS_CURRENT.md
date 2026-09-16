# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`Q1_UNIQUE_SOURCE_FREE_INVARIANT_MASS_ACCEPTED__NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted scientific checkpoint

Owner-adopted D1/D2/D3 corrected semantics、lower-a zero-kink multiplier handling、interior zero-liquid Z switching、Option-A 800-cell V0 map、accepted Q0、一次 direct HJB step V1、Q0 two-sink attribution、V1 remap/Q1 topology以及 Q1 source-free KFE operator validation均继续有效。Source-faithful/production paths remain frozen。

## Q1 source-free invariant mass accepted

Builder candidate `580a48c2aa4d969f471293d6022c3cdf3bc1425e` is accepted by `docs/CH5_MP4C_2018_KFE_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_ACCEPTANCE_20260916.md`.

The exact accepted Q1 SHA-256 `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E` has exactly one closed communicating class `[5,6,405,406]`. One dense full GESVD produced numerical rank/nullity `799/1`; the second-smallest singular value `0.01704325702964291` is far above frozen `tau_rank=5.728066976324905e-12`.

The normalized probability mass satisfies `||Q1.T @ p||_inf=1.927355525830249e-15` below the frozen stationarity bound `3.076397750501459e-12`, `math.fsum(p)=0.9999999999999999`, and minimum stored mass `-7.838997498725127e-15` within the preregistered arithmetic nonnegativity allowance. No clipping, pin, source RHS, retry, tolerance tuning or solver substitution occurred.

This establishes a unique, normalized, source-free invariant mass for Q1 as a finite one-step V1-policy operator. It does not establish nonlinear HJB convergence, joint HJB-KFE fixed point, stationary economic equilibrium, production readiness or Results authority.

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ZERO_SCIENCE_20260916.md`。

This is a zero-science design/binding gate. It must define the exact nonlinear iteration state/update sequence, HJB convergence criteria, KFE timing, fixed-point consistency conditions, finite runtime budgets, fail-closed rules and evidence protocol before any V2 or further continuation is authorized.

All selector/root/policy-map/D2/HJB/KFE/MATLAB/downstream calls remain zero in this design gate. Production replacement and Results remain unauthorized.
