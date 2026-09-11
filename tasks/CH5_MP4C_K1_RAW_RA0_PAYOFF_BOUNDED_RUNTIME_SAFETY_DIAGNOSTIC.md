# CH5 MP4C K1 — raw ra0 payoff bounded runtime-safety diagnostic

Date: 2026-09-12.
Task ID: `CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: bounded scientific runtime-safety diagnostic.
Issuer: ChatGPT Reviewer under Owner-approved payoff-return freeze.

## 1. Goal

Test the Owner-frozen raw `ra0` household illiquid payoff contract under a very short bounded corrected-2018 K1A runtime before any K1B activation.

This task isolates exactly one scientific change:

`household portfolio payoff source: clipped/source-used ra -> raw pre-clip ra0`.

The bilateral capital network, geographic benchmark, theta, labor route, C1, firm equations, HJB equations, KFE implementation, calibration, bounds, grid, tolerances and solver semantics otherwise remain unchanged.

This is a runtime-safety gate, not a steady-state acceptance gate.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`, record actual SHA, and verify this task remains active.

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_ACCEPTANCE.md`
- `docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_REPORT.md`
- `docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_ACCEPTANCE.md`
- `src/ch5_two_asset_hank/multi_province/capital_network.py`
- `src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py`
- the accepted K1A bounded runner/validator source needed to reproduce the beta-distance-2 path.

Do not restart historical parity, distance, data, KFE or clipping audits.

## 3. Frozen scientific contract

Use only the accepted pure-geographic K1A benchmark:

- `beta_distance = 2.0`
- `beta_return = 0`
- fixed `theta_i = inter_prv_ratio_i`
- accepted destination-by-origin distance matrix and exact 31-province order
- source-faithful labor
- portfolio smoothing OFF
- partial adjustment OFF
- K1B OFF
- K2 OFF
- C1 `GovInv=max(Ktarget-Kprivate,0)` unchanged
- firm/HJB/KFE equations unchanged
- return/wage bounds unchanged as diagnostics/runtime legacy objects
- solver, grid, tolerances and iteration semantics unchanged.

The final payoff contract frozen by Owner is:

`portfolio_return_by_destination = raw ra0`

and

`rah_i = sum_j S[j,i] * ra0_j`.

Interpret raw `ra0` only as `MODEL_TIME_RETURN_RATE__CALENDAR_PERIOD_UNRESOLVED` and `INTERNAL_MODEL_PRODUCTIVE_CAPITAL_RETURN_NUMERAIRE__EXTERNAL_MARKET_MAPPING_UNRESOLVED`.

Do not annualize, normalize, smooth, risk-adjust or cap the raw household payoff.

## 4. Diagnostic design

Run exactly two short paths from byte-identical accepted initialization:

### Control C

- geography `beta_distance=2`
- payoff source = current clipped/source-used `ra`
- purpose: reproduce the known transitional bridge over the same short horizon.

### Raw R

- geography `beta_distance=2`
- payoff source = raw pre-clip `ra0`
- purpose: test the Owner-frozen payoff contract.

The two paths must be identical in every scientific input and runtime setting except the payoff-return source.

Each path is authorized for at most **5 completed outer turns**.

The design intentionally does not run 25 turns. The purpose is immediate safety and mechanism diagnosis.

## 5. Timing/provenance requirement

Preserve lagged outer-iteration timing.

Turn `n` firm raw return may affect household payoff only through the next completed K1 allocation/household state. No same-turn firm-return feedback is authorized.

For Raw R, the persisted provenance must demonstrate that the same accepted `S` used for capital quantity allocation is used for:

`rah = ra0_by_destination @ S_destination_origin`.

For Control C, preserve the corresponding clipped-used-`ra` same-`S` mapping.

Do not use the K1B z-score as payoff.

## 6. Minimal implementation authority

The accepted K1 bilateral capital-network engine is already implemented and must remain the capital-allocation engine for this task.

Allowed changes are limited to explicit task-bounded payoff-source plumbing needed to select either:

- entering clipped/source-used `ra`; or
- entering raw `ra0` from the prior completed firm state.

A small selector/adapter field is allowed if representation/plumbing only. Do not change the economic formula for `ra0`, `S`, theta, distance softmax, C1, HJB, KFE, firm production or labor.

Do not modify the legacy allocator except for zero-science assertions if strictly necessary; any scientific change there is prohibited.

If raw `ra0` is not available in a provenance-safe prior-completed state without changing scientific timing, stop and report the blocker instead of inventing a source.

## 7. Pre-run gates

Before either trajectory invocation, prove with focused tests/static checks that:

1. live baseline and accepted evidence identities are correct;
2. both paths use the same accepted K1 capital network and beta-distance-2 shares;
3. C/R payloads are byte-identical apart from payoff-mode designation;
4. Control uses clipped/source-used `ra`;
5. Raw uses prior-completed raw `ra0`;
6. both payoff modes use the same `S` as quantity allocation;
7. no K1B return-score feedback is active;
8. source-faithful labor is active;
9. C1 formula is unchanged;
10. raw payoff is not silently clipped, normalized, scaled, annualized or smoothed.

If any gate fails, do not run science.

## 8. Scientific call budget

Maximum runtime budget:

- trajectory invocations: 2 total
- Control C: at most 5 turns
- Raw R: at most 5 turns
- maximum HJB calls: `31*5*2 = 310`
- maximum KFE calls: `310`
- MATLAB model calls: 0
- standalone KFE experiments: 0
- K1B: 0
- K2: 0
- GE: 0
- annual: 0
- shock/IRF: 0
- Results: 0.

Scientific retries are not allowed after state advancement.

One engineering retry is allowed only if an invocation fails before any scientific state update because of a pure path/serialization/output-shape defect and the scientific inputs remain byte-identical.

## 9. Mandatory runtime safety diagnostics

For both C and R, persist province-turn evidence sufficient to compare:

- entering `rah`
- network-produced next `rah`
- payoff source by destination
- `S` identity and share-column sums
- Kprivate and national/origin capital conservation
- GovInv and total K/target
- raw `ra0`, clipped/used `ra`, `rk`, after-tax profit/K
- household consumption/control summaries already available from the accepted route
- illiquid transfer/drift `d` summaries if already exposed
- liquid and illiquid drift extrema if already exposed
- HJB convergence flag/statistic
- HJB/KKT/boundary failure counts already available from accepted diagnostics
- NaN/Inf counts in values, policies and key aggregates
- KFE classification and existing leakage/pinning caveat
- output, wage and existing outer residual statistics.

Do not create new scientific diagnostics that require changing equations or solver internals. If an important safety quantity is unavailable, report it as unavailable rather than redesigning the model.

## 10. Raw-payoff safety questions

The report must answer, over the common completed horizon:

1. Does Raw R complete each authorized turn without NaN/Inf or hard model failure?
2. Does raw payoff materially increase `rah` levels relative to Control C as predicted by the accepted static audit?
3. Do HJB convergence statistics deteriorate materially immediately after raw payoff first enters the household block?
4. Do controls or drifts hit clearly pathological magnitudes relative to the Control path?
5. Are accepted HJB/KKT/boundary invariants violated?
6. Does K1 capital accounting remain exact under the payoff switch?
7. Does C1 accounting remain exact?
8. Does raw payoff cause any same-turn feedback or provenance violation? It must not.
9. Are any failures economic/numerical consequences of the raw payoff level rather than engineering defects?

No threshold may be invented after seeing results. Use existing accepted diagnostics and direct C/R ratios/differences descriptively.

## 11. Stop conditions

Stop the Raw path immediately and preserve evidence if any of the following occurs:

- NaN/Inf enters HJB values, controls, state aggregates or firm outputs;
- an accepted HJB/KKT/boundary invariant fails hard;
- the solver raises a scientific exception;
- same-turn return feedback is detected;
- payoff source is not exactly prior-completed raw `ra0`;
- same-`S` quantity/payoff identity fails;
- capital or C1 accounting fails beyond existing accepted numerical tolerances.

Do not tune parameters or caps after a stop.

Control may continue only within its own five-turn ceiling and only if doing so does not violate the total call budget.

## 12. Interpretation boundary

A successful five-turn Raw path would establish only:

`RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED`

It would not establish:

- full 25-turn convergence;
- steady-state acceptance;
- final KFE validity;
- K1B validity;
- K2 validity;
- annual/IRF/welfare/Results eligibility.

A failed Raw path is scientifically informative and must not be repaired by reintroducing clipping unless a future Owner decision explicitly changes the payoff contract.

## 13. KFE boundary

All corrected-2018 empirical KFE observations remain `DIAGNOSTIC_ONLY`.

Finite-box upper-b leakage plus MATLAB-style pinning remains an independent blocker.

This task must not attempt to solve it.

## 14. Allowed tracked changes

Allowed:

- one task-bounded payoff selector/adapter change if required;
- task runner/finalizer;
- focused tests;
- `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_REPORT.md`;
- compact receipts under `docs/evidence/ch5_mp4c_k1_raw_ra0_payoff_safety/`;
- truthful CURRENT closeout docs only at task completion.

Prohibited:

- firm equation changes;
- HJB/KFE equation changes;
- capital-network formula changes;
- legacy scientific allocator changes;
- C1 changes;
- labor normalization changes;
- bounds/calibration/grid/tolerance/solver changes;
- K1B/K2 runtime changes;
- annual/IRF/Results changes.

## 15. Local safety / Git publication

Use a fresh isolated worktree from fresh `origin/main` if the existing checkout is stale or dirty.

Never reset, clean, stash, force-push or overwrite unrelated user files.

Use a new no-overwrite evidence root.

Stage explicit paths only; do not use `git add .` or `git add -A`.

After completion:

1. review diff;
2. create one coherent commit;
3. non-force push task branch;
4. perform one remote commit/report readback;
5. do not merge main;
6. do not publish a successor task.

## 16. Final Builder reply

Return:

- verdict;
- actual live-main baseline;
- worktree / branch / commit;
- changed paths;
- payoff selector/provenance implementation summary;
- pre-run gates;
- C/R call ledger and completed turns;
- `rah` level comparison;
- HJB convergence/control/drift safety comparison;
- NaN/Inf and hard-invariant status;
- K1 capital and C1 accounting status;
- source-faithful labor confirmation;
- KFE caveat;
- whether short-horizon raw-payoff safety is supported;
- scientific/model call ledger;
- next recommended Owner/Reviewer gate;
- Results eligibility.

Then stop. Do not enter K1B or K2.
