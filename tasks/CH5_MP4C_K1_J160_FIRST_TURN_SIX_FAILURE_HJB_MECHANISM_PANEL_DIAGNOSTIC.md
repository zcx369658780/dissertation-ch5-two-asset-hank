# Exact task — CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_DIAGNOSTIC

## Objective

Classify the numerical nonconvergence mechanism for the six accepted first-turn provincial HJB failures at the accepted practical household grid, without changing science or recalibrating inputs.

## Read first

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_FREEZE_CURRENT.md`
7. accepted J640 mechanism diagnostic report/evidence
8. accepted first-turn provincial viability report/evidence
9. accepted MATLAB-faithful HJB authority

## Exact states

Replay only 天津、山西、江西、重庆、贵州、甘肃 using the exact accepted first-turn household-call inputs from the accepted input authority artifact. The exact `ra,w` coordinates are frozen in the companion freeze document. Do not reconstruct missing fields from chat memory and do not recompute firm/wage/return mappings.

## Runtime

If authority and instrumentation preflight pass:

- exactly one fresh-initialized HJB per failed province: total HJB=6;
- KFE=0;
- scientific retries=0;
- no successful province science reruns;
- no global outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results runtime.

## Required iteration trace

For every replay, persist a per-iteration trace containing at least:

- convergence statistic `max(abs(Vnew-Vold))`;
- signed dV and state coordinate at argmax;
- `A2max`, legality, finite/shape status;
- liquid-selector and transfer-selector change counts;
- derivative-floor hit counts and first activation;
- hashes for value and joint-selector state;
- recurrence/period-2/period-3 evidence;
- direct solve residual if available observationally.

The observation layer must not affect scientific control flow.

## Reproducibility gate

For each province compare the replay terminal result against the accepted viability receipt. If a previously failed province converges under identical inputs and science, classify that province `FAILURE_REPRODUCIBILITY_BLOCKER`; do not run KFE and do not treat the failure as repaired.

## Classification

For each province choose exactly one:

- `SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE`
- `POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`
- `DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING`
- `REPEATING_OR_LOW_PERIOD_CYCLE`
- `MIXED_OR_UNRESOLVED_NUMERICAL_MECHANISM`
- `FAILURE_REPRODUCIBILITY_BLOCKER`

Build event ordering for selector switching, first value-stat non-decrease/oscillation, and first derivative-floor activation.

Also produce a panel-level conclusion:

- `SIX_FAILURES_HOMOGENEOUS_CHATTER`
- `SIX_FAILURES_HOMOGENEOUS_SLOW_CONVERGENCE`
- `SIX_FAILURES_HETEROGENEOUS_MECHANISMS`
- `SIX_FAILURES_MECHANISM_UNRESOLVED`

Do not infer causality from temporal order alone.

## Offline comparison to successful provinces

Using accepted first-turn receipts only, identify nearest converged provincial neighbors in `(ra,w)` space for each failure and report their convergence iterations/final statistics. This is descriptive only and must use no new successful-province HJB calls.

## Prohibited

Do not change maxit, tolerance, solver, `Delta`, derivative floors, FOCs, selectors, boundaries, domain, grid, economic parameters, `wjt` guard, wage mapping, return mapping, or household inputs. Do not introduce damping/relaxation/line search/policy freezing. Do not run KFE or recalibration.

## Required outputs

Report:

`docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_DIAGNOSTIC_REPORT.md`

Evidence directory:

`docs/evidence/ch5_mp4c_k1_j160_first_turn_six_failure_hjb_mechanism_panel/`

At minimum:

- `source_identity.json`
- `input_authority_receipt.json`
- `instrumentation_invariance_receipt.json`
- `province_iteration_traces.json` or one CSV/JSON per province
- `province_mechanism_classification.json`
- `nearest_successful_neighbors.json`
- `panel_summary.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

## Git workflow

Fresh-fetch main, record actual baseline, use a fresh isolated worktree/branch, explicit stage only, one coherent Builder commit, non-force push, exactly one remote readback. No reset/clean/stash/force push, no `git add .` or `git add -A`, no merge to main, no successor task publication.

## Final response

Start with the panel terminal classification. Report actual baseline, branch, worktree, candidate SHA, changed paths, six exact input identities, six replay outcomes, six event-order/mechanism classes, nearest successful neighbors, panel conclusion, call ledger, KFE caveat, Results eligibility=`FALSE`, and exactly one next gate:

`REVIEWER_SIX_FAILURE_HJB_MECHANISM_ROUTE_DECISION`

Then STOP for independent Reviewer acceptance.
