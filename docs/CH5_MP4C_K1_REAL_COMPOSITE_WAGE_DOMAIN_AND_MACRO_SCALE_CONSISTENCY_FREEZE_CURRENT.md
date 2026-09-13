# CH5 MP4C K1 — real composite-wage-domain standalone health scan and macro-scale consistency freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_REAL_COMPOSITE_WAGE_DOMAIN_SCAN_WITH_MACRO_SCALE_AUDIT`.

## 1. Owner decision

The accepted standalone household health map uses the correct household-wage object but the wrong numerical wage domain for current provincial states. Accepted provincial household composite wages are approximately 12.84–18.52, while the old standalone scans observed only 0.8/1.05/1.3.

The next task therefore extends standalone HJB/KFE coverage to the real provincial household composite-wage scale without changing the HJB/KFE algorithm.

Do not modify the provincial `wjt` range in this task. Do not recalibrate firm wages, return mapping, GDP scaling, investment scaling, productivity, or any other economic parameter after observing results. This task is diagnostic and dimensional-consistency oriented.

If the real-wage-domain scan fails or becomes pathological, the correct response is not ad-hoc tuning. The task must stop scientific expansion and prepare a joint recalibration diagnosis for the later Owner gate.

## 2. Exact standalone scan

Fix `rb=.02` and run exactly 9 standalone MATLAB-faithful household points:

- `ra ∈ {.06,.0675,.07}`;
- household composite wage `w ∈ {13.0,15.5,18.0}`;
- Cartesian product only.

These wage values are representative of the accepted provincial composite-wage envelope and are household HJB inputs, not `wjt`.

All non-scanned household economics, grids and numerics remain identical to the accepted standalone oracle.

## 3. HJB/KFE algorithm freeze

No HJB/KFE redesign is authorized. Preserve the accepted MATLAB-faithful HJB/KFE algorithm, including initialization, upwind logic, transition matrix, derivative floor, transfer FOC, boundary law, pseudo-time/direct solve, convergence tolerance, iteration ceiling, transition-matrix legality check and contaminated-row stationary KFE.

No damping, relaxation, solver replacement, clipping, guard changes, grid changes, or post-result parameter tuning.

## 4. Classification and outputs

Per point first classify HJB as:

- `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`;
- `HJB_NOT_CONVERGED`;
- `HJB_CONVERGED`.

For converged HJB points only, run the accepted standalone KFE and publish raw diagnostics including `Ct,Lt,At,Bt`, marginals, endpoint masses, interior-a mass, modes, KFE residual, minimum density and negative-density count.

Distribution labels remain descriptive only:

- `LOWER_A_BOUNDARY_DOMINATED`;
- `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `UPPER_A_BOUNDARY_PILEUP`;
- `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`;
- `KFE_NUMERICALLY_PATHOLOGICAL` where signed KFE evidence is materially non-probabilistic.

Do not fit new thresholds after results.

## 5. Macro dimensional / quantity-scale audit

Because future modification of `wjt` or upstream mappings could silently change the scale of the model, this task must also perform a source/evidence audit of the model's macro quantity scale.

At minimum trace and report, using accepted repository sources/evidence where available:

1. province-level GDP/output object used by the model;
2. province-level per-capita GDP/output object, or a reproducible ratio from accepted output and population if the model defines the necessary objects;
3. household average/composite wage object actually consumed by HJB, and where possible the corresponding upstream provincial firm wage `wjt` scale;
4. any explicit multipliers/divisors/normalizations applied to GDP, capital, investment, population, labor, wage or productivity;
5. the source formula/chain connecting production quantities and wages where available.

The audit must distinguish:

- physical/statistical units from source data;
- model-normalized units;
- dimensionless/calibrated objects;
- quantities whose units cannot be proven from repository authority.

Do not infer RMB/yuan units merely from labels. Do not declare dimensional consistency unless the source chain supports it.

If accepted evidence contains province-level GDP, population and household wage for the same state/turn, report their numerical orders of magnitude side-by-side. If a full consistent triple is unavailable without running the global model, report that limitation rather than synthesizing values.

## 6. Recalibration trigger

If the real-composite-wage standalone scan shows widespread HJB nonconvergence, invalid transition matrices, severe KFE signed pathology, or universal artificial-boundary pile-up, do not adaptively tune the nine points.

Instead the final report must recommend a joint recalibration gate covering the upstream relationships among `wjt`, household composite `w`, `ra/rah`, and macro quantity scaling. The later recalibration must check province GDP, per-capita GDP and household wage magnitudes before any new `wjt` range is frozen.

## 7. Runtime limits

- HJB calls: exactly 9 unless a shared provenance blocker prevents execution;
- KFE calls: at most 9, one only after each HJB-converged point;
- scientific retries: 0;
- one pre-HJB engineering retry only for path/import/serialization/shape defects with unchanged science;
- global multi-province outer turns: 0;
- firm runtime: 0;
- MATLAB runtime: 0;
- K1B/K2/GE/downstream/shock/IRF/Results: 0.

The macro-scale audit is read-only and may use accepted source/evidence only.

## 8. Interpretation boundary

This task maps isolated household behavior at a realistic composite-wage scale. It is not a full steady-state calibration and cannot authorize `wjt`, return, GDP, investment or productivity changes by itself.

Standalone contaminated-row KFE remains distinct from the unresolved corrected-2018 multi-province finite-box upper-b leakage and MATLAB-style pinning blocker.

Results eligibility=`FALSE`.
