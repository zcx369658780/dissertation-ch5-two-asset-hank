# CH5 MP4C 2018 KFE D1-D3 nonlinear convergence law — Owner adoption

Date: 2026-09-17

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Owner decision status:

`PASS__OWNER_ADOPTED_CORRECTED_TARGET_NONLINEAR_CONVERGENCE_LAW__BOUNDED_RUNTIME_SUCCESSOR_AUTHORIZED`

## 1. Authority

The Owner explicitly adopts the following corrected-target nonlinear HJB convergence law prospectively, before any further scientific continuation call from accepted checkpoint `V1`.

This adoption resolves the blocker classified by:

- `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_REPORT.md`
- `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`

No rule below may be retuned after observing the future trajectory.

## 2. Primary convergence law

For checkpoint `n >= 1`, define the same-value stationary Bellman residual

`R_n = rho*vec_F(V_n) - vec_F(u_n) - Q_n*vec_F(V_n)`

where `(P_n,u_n,Q_n)` is freshly generated from exactly `V_n`, except that the already accepted and provenance-bound `(P1,u1,Q1)` may be reused for checkpoint 1.

Define:

- Bellman metric: `B_n = ||R_n||_inf`;
- value-change metric: `D_n = ||V_n - V_(n-1)||_inf`.

The corrected-target HJB convergence candidate is reached if and only if both conditions hold at the same checkpoint:

- `B_n <= 1e-8`;
- `D_n <= 1e-7`.

Both are inclusive thresholds. No rounding toward PASS is permitted.

## 3. Policy/operator stability role

Policy stability and operator stability are mandatory recorded diagnostics but are **not** additional terminal convergence conditions.

Every checkpoint must still persist, at minimum:

- selected branch / active-set / transfer / Z-marker identity changes relative to the prior checkpoint;
- continuous-control and consumed-drift change summaries;
- `Q_n` sparsity-structure identity/change evidence;
- `Q_n` numeric hash and a norm summary for `Q_n-Q_(n-1)` where available.

A policy or operator change therefore does not by itself reject a checkpoint that satisfies the two primary convergence inequalities. D2 legality, topology and terminal KFE remain separate mandatory gates.

## 4. Direct linear solve acceptance

Every implicit HJB update must persist the original 800-equation residual and normwise backward error.

A direct solve is accepted only when:

`normwise_backward_error <= 1e-12`.

Any finite solve result with backward error above `1e-12`, any nonfinite result, solver warning/failure, shape/order mismatch or inability to evaluate the metric is fail-closed. No solver substitution or retry is authorized.

## 5. Exact-cycle rule

Before declaring continuation to another update, compare the immutable checkpoint identities already observed on the same trajectory.

If a nonconverged checkpoint exactly repeats the full nonlinear checkpoint identity of an earlier checkpoint at period `k >= 2` — meaning the exact `V` hash together with the selected-policy identity and `Q` identity recur — classify `EXACT_CYCLE` and stop fail-closed.

A period-one exact identity is not automatically a cycle failure; it must still satisfy the Bellman and value-change convergence law. If it does not, continuation may proceed only if all other gates remain legal.

No tolerance is applied to exact-cycle detection.

## 6. Approximate period-2 / period-3 cycle rule

Only periods `k in {2,3}` are prospectively recognized as approximate-cycle stop rules.

At checkpoint `n`, after the primary convergence law has failed, define a complete recent period window by requiring the last `k` lag-`k` value comparisons all to satisfy:

`||V_j - V_(j-k)||_inf <= 1e-8`

for every

`j = n-k+1, ..., n`.

Therefore:

- period 2 requires two consecutive lag-2 comparisons and uses the most recent four value checkpoints;
- period 3 requires three consecutive lag-3 comparisons and uses the most recent six value checkpoints.

If this complete-window condition holds for `k=2` or `k=3` while the primary Bellman-plus-value convergence law is not satisfied at checkpoint `n`, classify `APPROXIMATE_PERIOD_k_CYCLE` and stop fail-closed.

No policy/operator tolerance is added to this approximate-cycle test. No longer-period approximate-cycle rule, spectral heuristic, trend heuristic or fitted tolerance is authorized.

## 7. Iteration ceiling and fixed numerical method

The call-725 corrected trajectory permits at most 100 total HJB updates.

Accepted `V0 -> V1` consumed update 1. Therefore continuation from accepted `V1` may perform at most 99 additional direct updates, ending no later than `V100`.

If convergence has not passed at `V100`, classify bounded nonconvergence and stop.

The following remain frozen:

- `Delta=1000` for every update;
- no damping;
- no relaxation or averaging;
- no adaptive `Delta`;
- no parameter continuation;
- no clipping;
- no artificial diffusion;
- no scientific retry or post-hoc tolerance tuning.

## 8. Terminal household HJB-KFE gate

Once the HJB convergence candidate is reached, no further HJB update is permitted.

The same-value final `(P*,u*,Q*)` must pass all accepted D1/D2 legality checks. Then terminal topology/KFE validation must use exactly the same `Q*`:

- exactly one closed communicating class;
- pin-free/source-free homogeneous KFE;
- `Q*.T @ p* = 0`;
- accepted F-order convention and normalization;
- accepted full dense `gesvd` rank/nullity and nonnegative-mass checks;
- no row replacement, pin, source injection, clipping, alternative eigensolver or retry.

A PASS at this gate establishes only a **conditional household HJB-KFE fixed point at frozen prices/calibration**. It does not establish market clearing, GE, production replacement, annual calibration, dynamics/IRFs or Results eligibility.

## 9. Authorized successor

Reviewer may publish one bounded runtime successor beginning from the exact accepted `V1/P1/u1/Q1` checkpoint, using the law above and the already accepted finite operation ceilings.

Results eligibility remains `FALSE`. Production/source-faithful paths remain unchanged.