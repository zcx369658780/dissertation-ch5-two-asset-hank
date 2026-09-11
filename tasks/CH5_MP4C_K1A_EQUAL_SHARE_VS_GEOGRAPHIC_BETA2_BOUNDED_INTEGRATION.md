# CH5 MP4C K1A — equal-share vs geographic beta=2 bounded integration

Date: 2026-09-11.
Task ID: `CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: bounded scientific integration / comparative trajectory diagnostic.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Goal

Integrate the accepted K1 bilateral capital-network successor into the corrected-2018 bounded multi-province route and compare exactly two preregistered K1A capital-allocation variants:

1. repaired equal-share baseline: `beta_distance=0`, `beta_return=0`;
2. pure-geographic benchmark: `beta_distance=2`, `beta_return=0`.

This task asks whether the repaired private-capital accounting and a moderate geography tilt can be propagated through the existing bounded corrected-2018 route while preserving capital accounting and C1 residual-public-asset logic, and how they change the raw-return pressure relative to each other.

This is **not** a steady-state acceptance, K1B run, K2 run, KFE closure, annual result, IRF, welfare or Results task.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`. Verify this task is present and has not been superseded.

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_ACCEPTANCE.md`
- `docs/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_REPORT.md`
- `docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`
- `src/ch5_two_asset_hank/multi_province/capital_network.py`
- current corrected-2018 one-turn/C1 integration code and the accepted C1 diagnostic report/acceptance directly relevant to `GovInv=max(Ktarget-Kprivate,0)`.

Do not restart historical parity or KFE gates that are not changed by this task.

## 3. Frozen scientific contract

### 3.1 Capital network

Keep:

`theta_i = inter_prv_ratio_i`

fixed for both paths.

Use the accepted destination-by-origin K1 matrix:

- `S[i,i]=1-theta_i`;
- `S[j,i]=theta_i*P[j,i]` for `j!=i`;
- `M_K[j,i]=S[j,i]*W_i`;
- `W_i=A_i*N_i`;
- `Kprivate_j=sum_i M_K[j,i]`;
- quantity and household return aggregation must use the same `S`.

### 3.2 Distance

Use the accepted mapped 2018 geographical-distance matrix and normalization receipt from:

`docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv`.

Do not reread or remap the protected workbook unless a concrete integrity mismatch requires verification. Do not change `D/D_max`.

### 3.3 Two and only two allocation variants

Path A — repaired equal-share:

`beta_distance=0`

`beta_return=0`.

Path B — pure geographic:

`beta_distance=2`

`beta_return=0`.

Do not run `.5`, `1`, `4` or any other beta-distance value. Do not choose a new coefficient after seeing results.

### 3.4 Household payoff bridge

For **K1A only**, freeze:

`portfolio_return_by_destination = current source-used/clipped ra`

Classification:

`K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`.

This keeps household payoff law source-faithful while the private-capital quantity/network block changes. It does not validate `[.02,.09]` as an economic return range.

Do not pass standardized raw-return scores into `rah`.

### 3.5 K1B remains off

Do not enable lagged-return attraction in this task. `beta_return=.5` is preregistered for future K1B but is not authorized to run here.

### 3.6 Labor and smoothing

Use source-faithful labor only.

Do not enable accepted normalized bilateral labor.

No portfolio smoothing or partial adjustment.

### 3.7 C1 public assets

Keep the accepted C1 rule exactly:

`GovInv = max(Ktarget - Kprivate, 0)`.

If `Kprivate>=Ktarget`, GovInv must be zero. Preserve any private-only overshoot. Do not introduce negative GovInv or a return-controller interpretation.

## 4. Implementation scope

Connect the separately accepted K1 capital-network module to the corrected-2018 bounded one-turn route using the minimum explicit successor wiring needed for this task.

Preserve the MATLAB-faithful legacy capital route unchanged and separately selectable for historical parity. Do not overwrite or reinterpret `capital_allocation.py`.

The K1 runtime integration must expose enough diagnostics to persist, for every completed outer turn and province as applicable:

- `theta`;
- home retained private capital;
- foreign outflow/inflow;
- destination `Kprivate`;
- full share-column sums / conservation residuals;
- `GovInv`;
- total K and Ktarget relation;
- raw `ra0`;
- used/clipped `ra`;
- `rk` component;
- profit/K component;
- clipping indicator;
- household `rah`;
- source-faithful labor identity needed to prove labor route was not switched.

Do not redesign unrelated interfaces. A small explicit adapter/config selector is preferred over duplicating one-turn code.

## 5. Bounded scientific execution

After implementation and focused zero-science/unit checks pass, run exactly two corrected-2018 bounded trajectories with identical initial state/data and all non-capital settings identical:

- Path A: equal-share beta distance 0;
- Path B: geographic beta distance 2.

Maximum outer turns per path: `25`.

Do not continue beyond 25 turns even if not converged. A path may stop earlier only because the existing scientific solver/household route fails under its frozen acceptance rules or a task stop condition below is hit.

These are bounded diagnostic trajectories, not steady-state claims.

## 6. Scientific/model call budget

Maximum authorized new runtime work:

- two corrected-2018 multi-province bounded trajectory invocations total: `2`;
- maximum outer turns: `25` per invocation;
- maximum province household/HJB solves implied by the two paths: `31 * 25 * 2 = 1550`, plus no extra science replay;
- MATLAB model calls: `0` unless the existing active corrected-2018 Python route itself requires none; this task is Python-successor integration;
- K1B runs: `0`;
- standalone KFE experiments: `0`;
- annual/GE/shock/IRF/Results calls: `0`.

The two trajectory invocations may each consume fewer than 25 turns if they stop naturally. Failed runtime invocations still count.

One additional runtime retry is authorized **only** if a clearly documented engineering failure occurs after invocation and before any scientific state update, such as serialization/path/output-shape failure. It must use byte-identical scientific inputs/configuration and cannot follow a scientific nonconvergence/failure. If the failure occurs after scientific state has advanced, preserve the output and do not rerun unless the existing task budget still contains an unconsumed original path invocation.

Ordinary pure tests, hashing, persisted-array comparisons, report generation and readback do not consume model calls.

## 7. Required comparisons

For both paths, report turn-by-turn and final bounded summaries sufficient to answer:

### 7.1 Capital accounting

- Does each origin column conserve `W_i=A_i*N_i`?
- Does national private capital equal national household illiquid wealth under the active bridge?
- Is home retained capital exactly `(1-theta_i)W_i`?
- Are quantity and household payoff weights generated from the same `S`?
- Are there any destination-`theta_j` double weights?

Any material accounting violation is a task failure and must not be hidden by tolerance changes.

### 7.2 C1 joint validation

For every province-turn:

- verify `GovInv=max(Ktarget-Kprivate,0)`;
- count `Kprivate>=Ktarget` cases;
- confirm GovInv is zero in those cases;
- report private-only overshoot explicitly;
- report total `K/Ktarget` distribution and any overshoot source.

Compare these quantities against the earlier legacy-private-K C1 evidence only as historical context; do not assume the old scale should remain.

### 7.3 Raw return re-audit

For each path and turn, persist and summarize:

`ra0 = rk + profit_component - delta`

using the actual active source decomposition.

Report:

- min/median/max raw `ra0`;
- count below `.02` and above `.09`;
- clipping count at lower/upper bounds;
- min/median/max `rk`;
- min/median/max profit/K contribution;
- relation of raw-return pressure to changed Kprivate and `Y/K`;
- whether geography beta 2 materially changes the cross-sectional raw-return dispersion relative to equal share.

Do not modify return bounds under this task.

### 7.4 Bounded path behavior

Report the existing outer convergence statistics for each turn/path without changing them. State whether each path is converged by turn 25 under existing rules, but do not label nonconvergence as a failure of K1 accounting if accounting remains valid.

Compare equal-share vs geography on:

- destination Kprivate distribution;
- GovInv distribution;
- total K/Ktarget;
- raw/used returns;
- `rah`;
- output/wage/convergence statistics already produced by the active route.

Keep interpretation diagnostic and mechanistic, not paper Results prose.

### 7.5 Labor and KFE boundaries

Prove the source-faithful labor path remained active in both runs.

Do not claim KFE is solved. Carry forward the corrected-2018 finite-box upper-b leakage / MATLAB-style pinning caveat exactly as an independent blocker.

## 8. Allowed changes

Authorized tracked changes are limited to the minimum files needed for K1A integration and evidence:

- an explicit K1 capital-network runtime adapter/config selector under `src/ch5_two_asset_hank/multi_province/`;
- focused tests directly covering that integration;
- the corrected-2018 bounded diagnostic runner only where needed to expose/select K1 without changing unrelated scientific behavior;
- one task report:
  `docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_REPORT.md`;
- compact machine-readable receipts under a task-specific `docs/evidence/` directory;
- CURRENT status/index/handoff updates at closeout only if truthful.

Do not modify:

- protected MATLAB source/data;
- legacy `capital_allocation.py`;
- accepted standalone K1 formulas unless a pure implementation defect is demonstrated; any scientific formula change requires stop/review;
- HJB/KFE equations or boundary laws;
- firm equations;
- labor normalization route;
- C1 GovInv formula;
- return/wage bounds;
- calibration parameters, solver semantics, tolerances, grids or iteration limits;
- annual/shock/IRF/Results code.

## 9. Pre-run checks

Before consuming either scientific trajectory invocation:

1. static/focused tests for K1 adapter selection and same-matrix accounting must pass;
2. prove legacy route remains unchanged/available;
3. prove both path configs differ only in `beta_distance` and resulting portfolio shares;
4. prove both use the accepted mapped distance receipt;
5. prove source-faithful labor and C1 formula remain active;
6. prove no K1B return-score feedback is enabled;
7. allocate distinct no-overwrite evidence directories for Path A and Path B.

If these cannot be established, stop before runtime.

## 10. Stop conditions

Stop scientific execution and preserve evidence if:

- a capital conservation identity fails materially;
- province order/mapping differs from accepted 31-province receipts;
- K1B/same-turn return feedback appears;
- source-faithful labor is not active;
- C1 GovInv formula differs from the accepted rule;
- a required scientific formula/tolerance/solver change appears necessary;
- a protected source would need modification;
- runtime inputs differ between A and B beyond the preregistered beta-distance change and its induced state evolution.

Do not tune parameters to rescue a path.

## 11. Acceptance classification

A successful task may support only a bounded K1A scientific diagnostic classification such as:

`K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_PASS`

provided the accounting and scope gates pass.

It does not imply:

- steady-state acceptance;
- final return-bound or payoff-return authority;
- K1B acceptance;
- K2 acceptance;
- KFE production closure;
- annual/IRF/welfare/Results eligibility.

A scientifically nonconverged 25-turn path may still produce a truthful partial/diagnostic outcome if accounting is valid; classify it explicitly rather than tuning.

## 12. Deliverables and publication

Use a fresh isolated worktree/branch from live main. Preserve stale/dirty original checkouts.

Write the report with outcome first, exact baseline, changed files, pre-run checks, call ledger, both path manifests, accounting/C1/raw-return tables, convergence summaries, limitations and next Owner gate.

Stage explicit paths only. No `git add .` or `git add -A`.

Create one coherent Builder commit, non-force push the task branch, read back the remote report/commit once, and stop. Do not merge main and do not publish a successor task.

Results eligibility remains `FALSE`.
