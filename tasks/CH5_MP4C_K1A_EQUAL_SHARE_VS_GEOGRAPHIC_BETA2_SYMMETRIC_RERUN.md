# CH5 MP4C K1A — equal-share vs geographic beta=2 symmetric rerun after validator repair

Date: 2026-09-11.
Task ID: `CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: bounded scientific re-execution with frozen science and repaired task provenance validator.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Goal

Produce a clean, symmetric bounded A/B comparison using the already accepted K1A implementation and the already repaired provenance validator. No scientific design changes are authorized.

Run exactly the same preregistered paths from identical accepted corrected-2018 initialization:

- Path A: repaired equal-share, `beta_distance=0`, `beta_return=0`;
- Path B: pure geographic, `beta_distance=2`, `beta_return=0`.

The predecessor task is accepted as partial evidence. This task exists only because Path A was stopped by a task-wrapper assertion that still checked the legacy `rah` formula. The repaired validator has already been exercised by the completed Path B run and is accepted as a zero-science provenance correction.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main` and verify this task remains active.

Read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_ACCEPTANCE.md`;
- `docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_REPORT.md`;
- `docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_ACCEPTANCE.md`;
- `src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py`;
- `validators/multi_province/k1a_equal_share_vs_beta2/run.py`;
- `validators/multi_province/k1a_equal_share_vs_beta2/finalize.py`;
- direct focused tests for this route.

Do not restart historical parity, KFE, or data-audit gates.

## 3. Frozen scientific contract

No scientific object may change relative to predecessor candidate `f57fec4d66bb82d48dc02bed775761ec194e0084`.

Keep exactly:

- `theta_i=inter_prv_ratio_i` fixed;
- accepted destination-by-origin K1 matrix;
- accepted mapped `D/D_max` distance receipt;
- Path A `beta_distance=0`, Path B `beta_distance=2`;
- `beta_return=0` in both paths;
- K1B off;
- source-faithful labor active;
- normalized bilateral labor off;
- smoothing/partial adjustment off;
- K1A household payoff bridge = current source-used/clipped `ra`;
- `GovInv=max(Ktarget-Kprivate,0)`;
- return/wage bounds unchanged;
- all HJB/KFE/firm equations, grids, tolerances, iteration limits and solver semantics unchanged.

The K1A payoff bridge remains classified:

`K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`.

## 4. Validator authority

The repaired task validator must validate household `rah` provenance against the prior completed K1A allocation using the same portfolio matrix `S`. It must not assert the legacy destination-theta-weighted `rah` formula.

Before runtime, prove by static/focused checks that:

1. the legacy validator assertion cannot trigger on a valid K1A same-`S` allocation;
2. the validator still fails if same-matrix provenance/accounting is genuinely violated;
3. no scientific equation or tolerance was changed by the repair.

Do not modify the validator further unless a purely representational/serialization defect is discovered. Any required scientific change is a stop condition.

## 5. Execution

Use a fresh no-overwrite evidence root. Do not reuse or overwrite the predecessor evidence root.

Run Path A and Path B from byte-identical accepted initialization and byte-identical non-capital configuration. The only preregistered exogenous difference is `beta_distance` and its induced subsequent state evolution.

Maximum outer turns per path: `25`.

Do not continue beyond 25 turns. Record whether each path satisfies the existing frozen final convergence predicate by or at turn 25.

## 6. Scientific/model call budget

Authorized new calls:

- bounded corrected-2018 trajectory invocations: exactly `2` maximum, one per path;
- outer turns: maximum `25` each;
- implied province HJB calls: maximum `31*25*2 = 1550`;
- implied KFE calls: maximum `1550`;
- MATLAB model calls: `0`;
- K1B runs: `0`;
- standalone KFE experiments: `0`;
- GE/annual/shock/IRF/Results: `0`.

No scientific replay beyond these two path invocations.

One retry is allowed only if an invocation fails before any scientific state update due to a documented engineering issue and uses byte-identical scientific inputs. No retry after state advance, nonconvergence, HJB/KFE scientific failure, or accounting failure.

## 7. Required evidence

For both paths, persist and compare the same fields as the predecessor task, including:

- share-column and origin/national capital conservation;
- home retained capital;
- foreign inflow/outflow;
- destination Kprivate;
- same-`S` quantity/payoff identity;
- `GovInv`, Ktarget, total K and private-only overshoot;
- raw `ra0`, used/clipped `ra`, `rk`, profit/K, clipping indicators;
- household entering `rah` and K1A network-produced payoff bridge `rah`;
- output, wage and frozen outer convergence metrics;
- source-faithful labor proof;
- HJB convergence flags;
- KFE classification/caveat.

Report full 25-turn A/B comparisons where both paths reach those turns. If one path stops scientifically before 25, report only the actual common completed prefix and classify honestly.

## 8. Questions to answer

1. Do both paths preserve all K1 capital accounting identities over the full completed bounded prefix?
2. Does C1 continue to satisfy `GovInv=max(Ktarget-Kprivate,0)` province-turn by province-turn?
3. How does `beta_distance=2` change Kprivate distribution relative to equal share once the change propagates through later household passes?
4. Does C1 continue to neutralize Kprivate differences at total-firm-K level, or do private-only overshoot cases emerge?
5. How do raw `ra0`, clipping counts, cross-sectional dispersion, `rah`, output, wage and convergence metrics differ over the common completed prefix?
6. Are both paths converged by turn 25 under the unchanged predicate?
7. Does the severe raw-return pressure (`ra0>.09`) persist under both paths?
8. Is the next scientifically useful gate payoff-return re-audit, K1B, or a convergence/KFE blocker instead?

Do not answer question 8 by silently changing science; make a recommendation based only on observed evidence.

## 9. Stop conditions

Stop and preserve evidence if:

- a material capital accounting identity fails;
- source/province mapping changes;
- K1B or same-turn return feedback appears;
- source-faithful labor is not active;
- C1 formula differs;
- a scientific formula/tolerance/solver change appears necessary;
- protected source modification would be needed;
- A/B inputs differ beyond the preregistered beta-distance choice and induced state evolution.

Do not tune to obtain convergence.

## 10. Allowed tracked changes

Prefer no production-science code changes. Authorized tracked changes are limited to:

- task-specific runner/finalizer or focused test changes only if required for non-scientific evidence plumbing;
- one report: `docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_REPORT.md`;
- compact task-specific receipts under `docs/evidence/ch5_mp4c_k1a_equal_share_vs_beta2_symmetric_rerun/`;
- CURRENT status/index/handoff closeout updates if truthful.

Do not modify `capital_network.py`, legacy `capital_allocation.py`, HJB/KFE/firm/labor/C1 science, calibration, bounds, solver semantics, grids, tolerances or Results code.

## 11. Publication

Use a fresh isolated worktree/branch from live main. Preserve stale/dirty original checkouts.

Stage explicit paths only; no `git add .` or `git add -A`.

Create one coherent Builder commit, non-force push the task branch, verify remote SHA/report once, and stop. Do not merge main and do not publish a successor task.

Results eligibility remains `FALSE`.

## 12. Final reply

Return concisely:

- verdict;
- actual live-main baseline;
- worktree/branch/commit;
- changed paths;
- pre-run validator and science-free checks;
- Path A and Path B call ledgers and completed turns;
- accounting/C1 summaries;
- full common-prefix A/B trajectory comparison;
- raw-return/clipping summary;
- convergence status;
- source-faithful labor confirmation;
- KFE caveat;
- total scientific/model call ledger;
- recommended next Owner/Reviewer gate;
- Results eligibility.
