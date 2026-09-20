# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`RUN003_TRANSIENT_ONLY_NEGATIVITY_FORENSIC_ACCEPTED__UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_ACTIVE`

Results eligibility=`FALSE`。

## Accepted Beijing state

Corrected HJB:

- checkpoint 12 PASS;
- B `1.292732587643286e-11`;
- D `1.2743897048750341e-08`;
- final Q SHA-256 `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`.

Topology/rank:

- one unique closed communicating class;
- closed states: 400;
- transient states: 400;
- full-space GESVD rank/nullity: `799/1`.

## Current KFE failure

The accepted full-space normalized SVD candidate still FAILS the frozen entrywise nonnegativity gate:

- min p `-2.217909641958515e-12`;
- frozen floor `-1.9184653865526386e-13`.

No aggregate or integration result is accepted.

## Accepted support forensic

Candidate:

`633e93d3ab114df95ac5d127170ced7da67a2cb1`.

Acceptance:

`docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_ACCEPTANCE_20260920.md`.

Classification:

`RUN003_NEGATIVITY_BREACHES_TRANSIENT_ONLY__CLOSED_CLASS_MASS_PASSES_ENTRYWISE_FLOOR__KFE_METHOD_DECISION_REQUIRED`.

Exact facts:

- floor breaches: 14;
- closed-class breaches: 0;
- transient breaches: 14;
- closed entries: 400 positive / 0 negative;
- closed signed mass: `1.0000000000100855`;
- transient signed mass: `-1.0085295212390263e-11`;
- transient L1 mass: `1.0090064860097144e-11`.

This supports a support-aware KFE method diagnostic but does not itself alter KFE.

## Current active task

`tasks/CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_20260920.md`.

The task tests one unique-closed-class method candidate only:

- extract Q_CC from the accepted closed-class indices;
- one restricted dense GESVD;
- one sign orientation and one normalization on the closed class;
- embed exact zero mass on transient states by support construction;
- one full original `Q.T@p` stationarity validation.

No topology recomputation, full-space GESVD rerun, clipping, tolerance change, aggregate evaluation, or multi-province rerun is allowed.

If the method candidate is supported, the task must STOP for an explicit Owner/Reviewer method-adoption decision.

Turn 2, K1B, K2, GE and Results remain closed.
