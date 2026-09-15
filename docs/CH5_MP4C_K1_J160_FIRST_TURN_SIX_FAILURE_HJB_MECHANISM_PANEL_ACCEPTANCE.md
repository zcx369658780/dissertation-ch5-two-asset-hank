# CH5 MP4C K1 — J160 first-turn six-failure HJB mechanism panel acceptance

更新：2026-09-15。

Reviewer verdict：

`SIX_FAILURES_HETEROGENEOUS_MECHANISMS_ACCEPTED__NO_COMMON_NUMERICAL_FIX_AUTHORIZED__TRACE_SPATIAL_LOCALIZATION_REQUIRED`

Accepted candidate：`ad4cdc8bbdf924c2ed06477abc10d1010038a5f7`，parent=`3b193f536fe2ab70fd487e3a4cde899ee5ed0c34`，exactly one commit ahead。

## Reviewer findings

- Input authority PASS；accepted first-turn and J640 manifests、six exact household inputs、source identities and fresh initialization receipts are sealed and consistent.
- Instrumentation invariance PASS；accepted J640 observer was reused without changing HJB behavior or control flow.
- Exact runtime respected：HJB=6，KFE=0，successful-province HJB=0，scientific retries=0，engineering retries=0；no outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results runtime.
- Six provinces exactly reproduced legal nonconvergence at maxit=100 with finite/shape-valid arrays and legal operators.
- Province classes are accepted as descriptive numerical mechanism classes: 天津、山西、重庆、甘肃=`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`；江西=`DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING`；贵州=`REPEATING_OR_LOW_PERIOD_CYCLE` based on exact joint-selector recurrence 96→98, period 2, without exact value recurrence.
- Panel class `SIX_FAILURES_HETEROGENEOUS_MECHANISMS` is accepted. The evidence rejects a single common slow-convergence story and does not justify a single universal damping/maxit/tolerance/calibration fix.
- All six begin selector switching at iteration 2, but floor timing, oscillation intensity, and recurrence behavior differ. This temporal similarity remains descriptive, not causal.
- Nearest-successful-neighbor comparisons remain descriptive only and do not establish that `(ra,w)` distance causes failure.

## Route decision

Do **not** change HJB/KFE algorithm, maxit, tolerance, Delta, derivative floor, selectors, grid, wage mapping, return mapping, guards, or calibration at this gate.

Before any input-envelope or calibration experiment, use the already sealed six-province iteration traces to localize **where in state space** the instability is expressed: whether switching, value argmax, derivative-floor activation, and recurrence are concentrated at liquid/illiquid boundaries or interior regions, and whether the four chatter provinces share the same state-space signature.

This next step is trace-only/offline: no new HJB/KFE/model runtime is authorized.

Results eligibility=`FALSE`。The corrected-2018 finite-box upper-`b` leakage / MATLAB-style pinning KFE blocker remains separate and unresolved.

Exactly one next gate：

`REVIEWER_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_ROUTE_DECISION`
