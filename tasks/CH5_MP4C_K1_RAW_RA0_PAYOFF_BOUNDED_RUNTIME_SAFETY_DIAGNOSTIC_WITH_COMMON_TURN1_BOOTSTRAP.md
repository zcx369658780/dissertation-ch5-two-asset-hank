# CH5 MP4C K1 — raw `ra0` payoff bounded runtime-safety diagnostic with common turn-1 bootstrap

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_WITH_COMMON_TURN1_BOOTSTRAP`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: bounded scientific runtime-safety diagnostic.
Issuer: ChatGPT Reviewer under Owner-approved payoff and bootstrap/timing freezes.

## 1. Goal

Execute the previously blocked raw-`ra0` payoff safety diagnostic using the Owner-approved common turn-1 clipped-`ra` bootstrap.

This task isolates exactly one treatment difference after bootstrap:

- Control C continues prior-completed clipped/source-used `ra` payoff;
- Raw R uses prior-completed raw pre-clip `ra0` payoff beginning at turn 2.

The bilateral capital network, geography benchmark, theta, labor, C1, firm/HJB/KFE equations, calibration, bounds, grids, tolerances and solver semantics otherwise remain unchanged.

This is a short-horizon safety gate, not a steady-state gate.

## 2. Mandatory authority reads

Fresh-fetch `origin/main`, record actual SHA, and verify this task remains active.

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_ACCEPTANCE.md`
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_REPORT.md`
- `docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_ACCEPTANCE.md`
- `src/ch5_two_asset_hank/multi_province/capital_network.py`
- `src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py`
- accepted K1A bounded runner/validator code required to reproduce the beta-distance-2 path.

Do not restart historical data, distance, parity, KFE or payoff audits.

## 3. Frozen scientific contract

Use only:

- `beta_distance=2.0`
- `beta_return=0`
- fixed `theta_i=inter_prv_ratio_i`
- accepted 31-province order and distance matrix
- source-faithful labor
- smoothing OFF
- partial adjustment OFF
- K1B OFF
- K2 OFF
- C1 `GovInv=max(Ktarget-Kprivate,0)` unchanged
- firm/HJB/KFE equations unchanged
- return/wage bounds unchanged as legacy/source diagnostics
- grids/tolerances/solver semantics unchanged.

Final raw payoff contract remains:

`rah_i = sum_j S[j,i] * ra0_j`.

Raw `ra0` must not be clipped, normalized, annualized, smoothed or risk-adjusted when used as the Raw payoff.

## 4. Owner-approved bootstrap/timing rule

Starting initialization lacks `ra0`, so both paths use the same accepted entering clipped/source-used `ra` for turn 1.

Turn 1 is the common bootstrap turn:

- Control C payoff source = entering clipped/source-used `ra`;
- Raw R payoff source = entering clipped/source-used `ra`;
- same K1 `S`, same quantities, same scientific inputs.

After turn 1 completes:

- Control C turn `n>=2` uses its own prior-completed used/clipped `ra^(n-1)`;
- Raw R turn `n>=2` uses its own prior-completed raw `ra0^(n-1)`;
- both use the same accepted same-`S` quantity/payoff rule within each path.

No cross-path borrowing after turn 1. No same-turn feedback.

Turn 2 is the first treatment turn.

## 5. Horizon and counting semantics

Run exactly two bounded paths from byte-identical accepted initialization:

### Control C
- beta-distance 2
- turn 1 common clipped bootstrap
- turns 2-5 clipped/source-used payoff

### Raw R
- beta-distance 2
- turn 1 common clipped bootstrap
- turns 2-5 raw `ra0` payoff

Each path may complete at most **5 total outer turns**.

Report turn 1 separately as bootstrap. Treatment comparisons are turns 2-5 only.

Do not describe any turn-1 C/R difference as a raw-payoff treatment effect.

## 6. Minimal implementation authority

The accepted K1 capital-network engine must remain unchanged.

Allowed changes are limited to task-bounded payoff-source plumbing/selector and runtime evidence needed to implement:

- `BOOTSTRAP_CLIPPED_RA` for turn 1 both paths;
- `CONTROL_CLIPPED_RA` for Control turns 2-5;
- `RAW_PRIOR_COMPLETED_RA0` for Raw turns 2-5.

If prior-completed raw `ra0` is unavailable at Raw turn 2 despite a completed turn 1, stop and report a provenance blocker.

Do not modify the scientific formula for `ra0`, `S`, theta, distance softmax, C1, firm, HJB, KFE or labor.

## 7. Pre-run gates

Before science, prove with focused tests/static checks:

1. live baseline/task authority and accepted evidence identities;
2. accepted initialization has no raw `ra0`, and bootstrap rule is the Owner-approved resolution;
3. C/R starting payloads are byte-identical apart from path labels/mode metadata;
4. both turn 1 allocations use the same entering used/clipped `ra`;
5. Raw turn 2 is wired to turn-1 completed raw `ra0` of the same Raw path;
6. Control turn 2 is wired to turn-1 completed used/clipped `ra` of the same Control path;
7. same `S` is used for quantity and payoff in each mode;
8. K1B is OFF;
9. source-faithful labor is active;
10. C1 is unchanged;
11. raw payoff is not clipped/scaled/normalized/annualized/smoothed.

Any failed gate blocks science.

## 8. Scientific call budget

Maximum:

- trajectory invocations: 2 total
- Control: <=5 completed turns
- Raw: <=5 completed turns
- HJB calls <=310
- KFE calls <=310
- MATLAB model calls = 0
- standalone KFE experiments = 0
- K1B/K2 = 0
- GE/annual/shock/IRF/Results = 0.

No scientific retry after state advancement.

One engineering retry is allowed only for a pre-state-update path/serialization/output-shape failure with byte-identical scientific inputs.

## 9. Mandatory evidence

For both paths persist enough province-turn evidence to verify:

- payoff mode and source provenance;
- entering `rah` and next network-produced `rah`;
- destination payoff source vector;
- `S` identity, share-column sums and same-`S` quantity/payoff identity;
- Kprivate and origin/national conservation;
- GovInv and total K/target;
- raw `ra0`, used/clipped `ra`, `rk`, after-tax profit/K;
- available household consumption/control summaries;
- available illiquid transfer/drift `d` and liquid/illiquid drift extrema;
- HJB convergence/statistics;
- existing KKT/boundary diagnostics;
- NaN/Inf counts in values, controls, policies and key aggregates;
- KFE classification/caveat;
- Y, wage and outer residual statistics.

Do not alter equations or solver internals to manufacture new diagnostics.

## 10. Required comparisons

Report:

### Bootstrap turn 1
- confirm C/R scientific state and payoff source are identical up to expected numerical reproducibility;
- confirm completed turn 1 produces provenance-safe raw `ra0` for both paths.

### Treatment turns 2-5
Answer:

1. Does Raw R complete each authorized treatment turn without NaN/Inf or hard scientific failure?
2. How much larger/different is entering and network-produced `rah` versus Control?
3. Does HJB convergence/statistic materially deteriorate when raw payoff first enters at turn 2?
4. Do consumption, controls or drifts show clear pathologies relative to Control?
5. Are accepted HJB/KKT/boundary invariants preserved?
6. Does K1 capital accounting remain closed?
7. Does C1 remain exact within accepted numerical tolerances?
8. Is lagged provenance exact and free of same-turn feedback?
9. Are any failures attributable to raw payoff level rather than engineering defects?

Use existing diagnostics and descriptive C/R differences/ratios. Do not invent post-hoc thresholds.

## 11. Stop conditions

Stop Raw immediately and preserve evidence if:

- NaN/Inf enters HJB values, controls, key states or firm outputs;
- accepted HJB/KKT/boundary invariant fails hard;
- scientific solver exception occurs;
- same-turn feedback is detected;
- Raw turn `n>=2` payoff source is not exactly its own prior-completed `ra0`;
- same-`S`, capital or C1 accounting fails beyond existing accepted numerical tolerance.

Do not tune parameters, reintroduce clipping, add caps, change grids/tolerances/solver or change payoff contract after a stop.

## 12. Acceptance classification

If Raw completes treatment turns 2-5 safely with accounting/provenance gates intact, the strongest permitted classification is:

`RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED_WITH_COMMON_TURN1_BOOTSTRAP`

This does not establish 25-turn convergence, steady state, KFE validity, K1B/K2 validity or Results eligibility.

If the Raw path stops, classify truthfully and preserve the failure.

## 13. KFE boundary

All corrected-2018 KFE observations remain `DIAGNOSTIC_ONLY`; finite-box upper-b leakage plus MATLAB-style pinning remains an independent blocker. Do not solve it here.

## 14. Allowed tracked changes

Allowed:

- one minimal task-bounded payoff selector/adapter change if required;
- runner/finalizer;
- focused tests;
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_COMMON_TURN1_BOOTSTRAP_SAFETY_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_raw_ra0_payoff_bootstrap_safety/`;
- truthful CURRENT closeout docs if task completes.

Prohibited:

- capital-network economic formula changes;
- firm/HJB/KFE science changes;
- C1/labor science changes;
- bounds/calibration/grid/tolerance/solver changes;
- K1B/K2 runtime;
- annual/IRF/Results.

## 15. Git/local safety

Use a fresh isolated worktree/branch from live `origin/main`. Preserve unrelated dirty work. No reset/clean/stash/force push. Use no-overwrite evidence roots.

Stage explicit paths only; do not use `git add .` or `git add -A`.

Commit coherently, non-force push, perform one remote report/commit readback, do not merge main, and do not publish a successor task.

## 16. Final Builder response

Return:

- verdict/classification
- actual live-main baseline
- worktree/branch/commit SHA
- changed paths
- bootstrap/provenance implementation
- pre-run gate result
- Control and Raw call ledgers
- completed turns
- turn-1 bootstrap equivalence evidence
- turns-2-5 `rah` comparison
- HJB convergence comparison
- control/drift safety comparison
- NaN/Inf and hard-invariant status
- K1/C1 accounting
- source-faithful labor confirmation
- KFE caveat
- total scientific/model call ledger
- whether `RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED_WITH_COMMON_TURN1_BOOTSTRAP` is supported
- next Owner/Reviewer gate recommendation
- Results eligibility.

Then stop. Do not enter K1B or K2.
