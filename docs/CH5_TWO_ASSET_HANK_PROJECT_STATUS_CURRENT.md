# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`RUN003_BEIJING_HJB_TOPOLOGY_RANK_PASS__STATIONARY_MASS_ENTRYWISE_NONNEGATIVITY_FAIL__ZERO_SCIENCE_SUPPORT_FORENSIC_ACTIVE`

Results eligibility=`FALSE`。

## Accepted foundation

Still accepted:

- corrected D1/D2/D3 household law;
- same-checkpoint HJB convergence law `B<=1e-8 AND D<=1e-7`;
- source-free terminal KFE contract as the current scientific gate;
- corrected household aggregate semantics;
- Owner Option-B raw-ra0 payoff law;
- K1A/C1 one-turn integration design, not yet reached.

## Run003 accepted result

Candidate:

`e352acaa6003bf0ccec8e5ad56688a626ccf2146`.

Acceptance:

`docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NONNEGATIVITY_FAILURE_ACCEPTANCE_20260920.md`.

### Beijing HJB

PASS at checkpoint 12:

- B `1.292732587643286e-11`;
- D `1.2743897048750341e-08`;
- 12 direct solves;
- max backward error `3.0832786979441453e-16`;
- final Q SHA-256 `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`.

### Beijing topology and rank

PASS:

- exact-positive edges: 2316;
- one SCC call;
- 11 components;
- exactly one closed class of 400 states;
- 400 transient states;
- GESVD rank/nullity `799/1`;
- structural closed-class count equals numerical nullity.

### Stationary-mass gate

FAIL only at frozen per-entry nonnegativity:

- min p `-2.217909641958515e-12`;
- per-entry floor `-1.9184653865526386e-13`;
- negative entries: 278;
- total negative mass `1.0087680036243705e-11`;
- total-negative bound `1.5347723092421108e-10` PASS;
- stationarity and normalization checks PASS.

No aggregate or multi-province integration object was produced.

Run003 manifest:
`18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B`.
Independent readback passed; code freeze matched.

## Current active task

`tasks/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_20260920.md`.

This task is zero-science only. It decomposes the already persisted normalized p and residual over the accepted closed-class and transient masks.

It may diagnose whether the entrywise violations are transient-only or occur inside the closed class. It may not alter p, rerun SCC/SVD/KFE, project support, clip, renormalize, change tolerance, or accept KFE.

Any later change to KFE support handling, solver semantics or nonnegativity acceptance remains a substantive scientific decision.

Turn 2, K1B, K2, GE and Results remain closed.
