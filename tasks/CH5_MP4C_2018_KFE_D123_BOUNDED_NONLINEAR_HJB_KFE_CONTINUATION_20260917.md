# Task — CH5 MP4C 2018 KFE D1-D3 bounded nonlinear HJB-KFE continuation

Date: 2026-09-17

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID: `CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_20260917`

## 0. Governance and scope

This is an authorized scientific runtime task for the corrected diagnostic target only.

Before doing anything:

1. fresh-fetch live `origin/main`;
2. verify zero ahead/behind against the chosen clean worktree baseline;
3. read `AGENTS.md`, `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, current status/handoff, the Owner convergence-law adoption, the accepted nonlinear fixed-point design/acceptance, the accepted Q1 KFE validation, and the exact corrected selector/D2/HJB authorities;
4. report the exact baseline SHA used.

Never enter, read, use or modify `zcx369658780/deep-learning-hank`.

Protected/source-faithful MATLAB remains read-only. Do not execute MATLAB in this task.

Do not modify production/source-faithful scientific behavior. Any implementation required for orchestration/checkpointing must remain within the corrected diagnostic route and must not change frozen selector/D1/D2/D3/Z/KKT equations.

Results eligibility remains `FALSE`.

## 1. Required starting checkpoint

Start from the exact accepted corrected checkpoint 1:

- `V1` field SHA-256 `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2`;
- V1 direct-step artifact SHA-256 `28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173`;
- accepted V1 policy receipts: 800/800 `SELECTED_ADMISSIBLE`;
- `Q1` SHA-256 `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E`;
- Q1-remap manifest SHA-256 `573FCF61220E5982EB4A6E78FAFC5D82310BAC7F7638D2D83B576B1420DDCF37`;
- accepted `p1,g1` artifact SHA-256 `14E6EC29650A7F9F5D95B023E5B6E54AC1391DC836E2513AC9CACAFEEB7B4254`.

The already accepted `(P1,u1,Q1)` may be reused for checkpoint 1 and for the first `V1 -> V2` update. Do not rerun the V1 policy map merely to reproduce accepted evidence.

`p1` is operator evidence only. It must not be fed into the HJB update and must not be used as a later KFE warm start.

## 2. Frozen corrected-target convergence law

Authority:
`docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`.

For checkpoint `n >= 1`, using same-value `(P_n,u_n,Q_n)`, compute

`R_n = rho*vec_F(V_n) - vec_F(u_n) - Q_n*vec_F(V_n)`.

Define:

- `B_n = ||R_n||_inf`;
- `D_n = ||V_n - V_(n-1)||_inf`.

A corrected-target HJB convergence candidate is reached if and only if both:

- `B_n <= 1e-8`;
- `D_n <= 1e-7`.

The inequalities are inclusive and must be evaluated from unrounded stored values.

Policy/operator stability is mandatory diagnostic evidence only; it is not an additional convergence gate.

## 3. Checkpoint-1 evaluation before any new update

Before any V2 solve:

1. load exact accepted `V0`, `V1`, `P1`, `u1`, `Q1` evidence required to compute `B1` and `D1`;
2. hash-bind every input and verify exact accepted identities;
3. compute and persist `B1`, `D1`, policy/operator diagnostic identity for checkpoint 1;
4. apply the primary convergence law;
5. if checkpoint 1 already converges, do not execute a V2 solve and proceed directly to Section 9 using exact Q1;
6. otherwise continue under the rules below.

No KFE call is permitted merely because accepted `p1` exists.

## 4. Per-round order for n >= 2

For every newly created `V_n`, execute exactly this order:

1. hash-bind finite `V_n`, exact shape `(20,20,2)`, F-order, b-fastest, frozen grids/prices/calibration/productivity generator/scientific code;
2. construct frozen raw forward/backward one-sided derivatives from `V_n`, preserving the accepted unused-boundary-slot carrier rule;
3. traverse all 800 cells in F-order and execute the accepted corrected selector once per cell under the frozen D1/D3/lower-a-zero-kink/interior-Z rules;
4. persist each complete selector comparison receipt before advancing;
5. require 800/800 `SELECTED_ADMISSIBLE` before any D2 call;
6. assemble one D2 `Q_n` from consumed total drifts and enforce every accepted closed-face, nonnegative-offdiagonal, diagonal, row-sum, coordinate-action and evidence/hash check;
7. compute and persist `B_n`, `D_n`, policy-stability diagnostics and operator-stability diagnostics;
8. first evaluate the primary convergence law;
9. only if primary convergence fails, evaluate exact-cycle and approximate-cycle stop rules;
10. if no stop rule fires and update ceiling remains, perform at most one implicit HJB direct solve to create `V_(n+1)`.

No stale policy/operator may be carried into a later checkpoint.

## 5. Policy/operator diagnostics

Persist at every fresh checkpoint at least:

- selected branch/active-set/transfer/Z-marker identities and counts;
- exact number and locations of identity changes relative to prior checkpoint;
- max/summary changes in continuous controls and consumed drifts;
- Q sparsity pattern identity/change summary;
- Q numeric hash;
- a prospective norm summary of `Q_n-Q_(n-1)`;
- selector/root/D2 call ledgers.

These are diagnostics only. Do not invent a terminal stability threshold.

## 6. Direct HJB solve and backward-error gate

If continuation is still legal, use only the frozen method:

`Delta = 1000`

`M_n = (rho + 1/Delta)*I_800 - Q_n`

`rhs_n = vec_F(u_n) + vec_F(V_n)/Delta`

`vec_F(V_(n+1)) = solve(M_n,rhs_n)`.

Persist the original 800-equation residual and a normwise backward error computed prospectively and reproducibly.

The solve passes only if:

`normwise_backward_error <= 1e-12`.

Any result above the threshold, nonfinite metric/value, solver warning/failure, shape/order mismatch, or inability to evaluate the metric is immediate fail-closed.

No retry, alternative sparse/direct solver, iterative refinement, damping or substitution is authorized.

## 7. Cycle rules

### 7.1 Exact cycle

After primary convergence fails, compare immutable checkpoint identities already observed on this trajectory.

If the exact `V` hash together with selected-policy identity and `Q` identity repeats an earlier checkpoint at period `k >= 2`, stop as:

`EXACT_CYCLE`

Do not apply a tolerance.

A period-one exact identity is not itself a cycle failure; it still must pass the primary convergence law.

### 7.2 Approximate period 2 / 3

Only `k in {2,3}` is authorized.

At current checkpoint `n`, after primary convergence fails, require the full recent lag-k window:

`||V_j - V_(j-k)||_inf <= 1e-8`

for every

`j = n-k+1, ..., n`.

Thus:

- k=2 requires the last two lag-2 comparisons, using the most recent four V checkpoints;
- k=3 requires the last three lag-3 comparisons, using the most recent six V checkpoints.

If the full condition holds, stop as `APPROXIMATE_PERIOD_2_CYCLE` or `APPROXIMATE_PERIOD_3_CYCLE`.

Do not add longer-period heuristics, trend tests, spectral tests or fitted tolerances.

## 8. Hard ceilings

The complete corrected trajectory may contain at most 100 total HJB updates.

Accepted `V0 -> V1` consumed update 1. Therefore this task may execute at most 99 new direct HJB solves and may not create a value beyond `V100`.

Worst-case future ceilings from accepted V1:

- new corrected policy maps: 99;
- selector evaluations: 79,200;
- scalar-root invocations: 311,256;
- interior-Z root invocations: 285,120;
- D2 assemblies: 99;
- sparse direct HJB solves: 99;
- ordinary-round graph/SCC summaries: at most 99 if the existing implementation records them diagnostically;
- terminal dense GESVD KFE solves: at most 1;
- terminal normalized stationary candidates: at most 1;
- terminal `Q*.T @ p*`: at most 1;
- retries / solver substitutions / damping / adaptive-Delta / continuation / MATLAB / downstream calls: 0.

Unused calls from a failed round do not become retry budget.

If V100 fails the primary convergence law, stop as bounded nonconvergence. Do not alter the algorithm.

## 9. Terminal same-value topology/KFE gate

If and only if the primary HJB convergence law passes at checkpoint `n`:

1. freeze `V*=V_n`, `P*=P_n`, `u*=u_n`, `Q*=Q_n` and their hashes;
2. perform no further HJB update;
3. verify exact-positive graph/SCC topology for the same `Q*`;
4. require exactly one closed communicating class before numerical KFE;
5. perform exactly one accepted pin-free/source-free KFE validation on that same `Q*`:
   - solve homogeneous `Q*.T @ p*=0` by the accepted full dense `scipy.linalg.svd(..., lapack_driver="gesvd")` contract;
   - F-order, b fastest;
   - no row replacement, pin or balancing source;
   - one global sign orientation and one normalization;
   - enforce accepted rank/nullity, stationarity, normalization and nonnegative-mass bounds;
   - no clipping, alternative eigensolver, warm start or retry.

Special case: if checkpoint 1 is the convergence candidate, exact previously accepted Q1 topology/KFE evidence may be reused only after all artifact/code/hash identities are proven identical to the frozen terminal Q*. Do not rerun KFE solely for duplication if the accepted evidence is exact and complete. If identity cannot be proven, fail closed rather than silently reusing it.

A terminal PASS is classified only as a conditional household HJB-KFE fixed point at frozen prices/calibration.

## 10. Fail-closed conditions

Stop immediately, with no repair/retry, on the first occurrence of any of the following:

- provenance/hash/code drift;
- nonfinite V/derivative/control/utility/drift/Q/residual/metric;
- selector/root budget breach or first non-`SELECTED_ADMISSIBLE` cell;
- incomplete 800-cell map or missing durable receipt;
- any D2 legality failure;
- direct-solve failure or backward error `>1e-12`;
- `EXACT_CYCLE` before convergence;
- `APPROXIMATE_PERIOD_2_CYCLE` or `APPROXIMATE_PERIOD_3_CYCLE` before convergence;
- V100 without primary convergence;
- threshold ambiguity caused by rounding or missing raw metric;
- terminal Q* with other than one closed communicating class;
- terminal SVD/rank/nullity/stationarity/normalization/nonnegative-mass failure;
- any attempt to introduce damping, relaxation, adaptive Delta, continuation, clipping, artificial diffusion, solver substitution or fitted tolerance.

Do not treat any failure as permission to modify the frozen numerical law.

## 11. Required artifacts and report

Persist durable evidence sufficient for independent replay/audit:

- startup/baseline/provenance manifest;
- immutable per-checkpoint manifest with V hash, P/u/Q identity, Bellman/value metrics, policy/operator diagnostics, call ledger and status;
- per-update direct-solve residual/backward-error evidence;
- cycle-detection ledger containing exact compared checkpoint indices and raw norms;
- terminal topology/KFE evidence if terminal gate is reached;
- one final execution report under `docs/`.

The report must state:

- exact baseline and candidate SHAs;
- exact scientific code hashes before/after;
- number of newly executed maps/selectors/roots/Z-roots/D2/direct solves/KFE/SVD/Q.T@p calls;
- final checkpoint index and exact stop reason;
- full raw terminal metrics;
- whether a conditional household HJB-KFE fixed point was established;
- explicit statement that GE/production/Results remain unproven.

## 12. Allowed final classifications

Use exactly one clear final classification consistent with evidence, for example:

- `PASS__CORRECTED_HJB_CONVERGED__TERMINAL_SOURCE_FREE_KFE_PASS__CONDITIONAL_HOUSEHOLD_FIXED_POINT_ESTABLISHED`
- `FAIL__CORRECTED_HJB_EXACT_CYCLE`
- `FAIL__CORRECTED_HJB_APPROXIMATE_PERIOD_2_CYCLE`
- `FAIL__CORRECTED_HJB_APPROXIMATE_PERIOD_3_CYCLE`
- `FAIL__CORRECTED_HJB_UPDATE_CEILING_REACHED_WITHOUT_CONVERGENCE`
- `FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`
- `FAIL__CORRECTED_HJB_LINEAR_SOLVE_ACCURACY_GATE`
- `FAIL__HJB_CONVERGED__TERMINAL_TOPOLOGY_OR_KFE_GATE`
- `BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT`

If an unforeseen scientific choice would be required, stop as Owner-decision-required instead of inventing a rule.

## 13. Explicit prohibitions

No production replacement. No market clearing. No GE. No annual calibration. No dynamics. No IRF. No welfare. No causal interpretation. No paper Results. No MATLAB execution. No change to protected/source-faithful files. No post-hoc tolerance tuning.