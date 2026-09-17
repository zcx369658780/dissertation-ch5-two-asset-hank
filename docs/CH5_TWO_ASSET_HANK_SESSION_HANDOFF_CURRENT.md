# Chapter 5 当前交接 — Owner convergence law adopted / bounded nonlinear continuation active

更新：2026-09-17。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
状态：`OWNER_CONVERGENCE_LAW_ADOPTED__BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Governance

Owner is final scientific authority; ChatGPT is L3 Reviewer/scientific-route authority; Codex is bounded Builder. GitHub live `main` is repository-state authority. `deep-learning-hank` is separate and must not be used.

## Accepted state

Corrected route has an accepted V0 policy map/Q0, one direct HJB step V1, one fresh V1 policy remap/Q1, and a unique pin-free/source-free Q1 invariant mass. Q1 has one closed class `[5,6,405,406]` and numerical rank/nullity `799/1`. These remain operator/one-step evidence until nonlinear convergence is established.

Accepted nonlinear design:
`docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`.

Owner convergence-law adoption:
`docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`.

## Frozen nonlinear convergence law

At the same checkpoint, require both:

- `||rho*V_n-u_n-Q_n*V_n||_inf <= 1e-8` in exact frozen F-order semantics;
- `||V_n-V_(n-1)||_inf <= 1e-7`.

Policy/operator stability must be recorded but is diagnostic only. Every direct HJB solve requires normwise backward error `<=1e-12`.

Exact full-checkpoint recurrence at period `k>=2` before convergence is fail-closed. Approximate periods 2 and 3 are recognized only after primary convergence fails: for `k in {2,3}`, the last `k` lag-`k` comparisons must all satisfy `||V_j-V_(j-k)||_inf <=1e-8`; period 2 therefore uses four recent checkpoints and period 3 uses six. No other approximate-cycle heuristic is authorized.

`Delta=1000` remains fixed. The call-725 path allows at most 100 HJB updates total; accepted `V0->V1` already used update 1, leaving at most 99 direct updates through V100. Damping, relaxation, adaptive Delta, parameter continuation, clipping, artificial diffusion, solver substitution, scientific retry and post-hoc tolerance tuning are prohibited.

## Active Builder task

`tasks/CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_20260917.md`

Builder must fresh-fetch live main, bind exact accepted V1/P1/u1/Q1 artifacts and scientific code, evaluate checkpoint V1 first, then continue only as required. Accepted `(P1,u1,Q1)` may be reused for the V1 gate and first V1->V2 update; no V1 remap is needed.

For each later checkpoint, enforce derivatives -> complete 800-cell policy map -> D2 Q_n -> Bellman/value/stability metrics -> convergence/cycle decision -> at most one fixed-Delta direct update. No KFE is run during ordinary rounds.

If HJB convergence passes, no further HJB update is allowed. The exact same-value Q* then proceeds to the accepted one-closed-class topology gate and exactly one pin-free/source-free terminal KFE validation. PASS means only a conditional household HJB-KFE fixed point at frozen prices/calibration.

Production replacement, market clearing, GE, annual calibration, dynamics, IRFs, MATLAB and Results remain unauthorized.