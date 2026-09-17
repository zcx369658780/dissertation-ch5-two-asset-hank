# Chapter 5 当前交接 — V2 lower-b selector omission accepted / minimal repair and checkpoint-2 reexecution active

更新：2026-09-17。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
状态：`V2_LOWER_B_SELECTOR_BRANCH_OMISSION_ACCEPTED__MINIMAL_REPAIR_AND_CHECKPOINT2_REEXECUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Governance

Owner is final scientific authority; ChatGPT is L3 Reviewer/scientific-route authority; Codex is bounded Builder. GitHub live `main` is repository-state authority. `deep-learning-hank` is separate and must never be used for this route.

## Accepted attribution

Builder candidate `582f7fca52e47ee5303164edbc62b98add363ec6` is Reviewer-accepted as:
`ATTRIBUTED__SELECTOR_OMITS_AUTHORITY_BACKED_LEGAL_BRANCH`.

The accepted defect is narrow:
- lower-b active KKT requires `q_b >= p_b`;
- the corrected selector's active lower-b negative-transfer derivative pre-screen incorrectly used `0 < q_b <= p_b`;
- this omitted the authority-backed negative/backward-`a` case;
- eight cases are required by the frozen lower-b/interior-a census, but the V2 cell100 receipt contains seven;
- static algebra shows the omitted case would still be inadmissible at cell100, so this is an implementation coverage defect rather than evidence for a different cell100 selected policy;
- positive active root failure is genuine no-root on the legal domain;
- interior-Z is not legal at the b-boundary.

Acceptance document:
`docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_ACCEPTANCE_20260917.md`.

## Frozen runtime checkpoint

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Checkpoint 1 remains the last complete same-value checkpoint until repaired checkpoint 2 completes:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`;
- V1->V2 direct residual `1.9012569296705806e-14`;
- backward error `2.5514110567283015e-16`.

Owner nonlinear law remains frozen: Bellman `<=1e-8` and value change `<=1e-7` simultaneously; fixed `Delta=1000`; backward error `<=1e-12`; frozen cycle rules; no damping/relaxation/adaptive Delta/continuation/clipping/artificial diffusion/solver substitution/scientific retry/post-hoc tolerance tuning.

## Current active task

`tasks/CH5_MP4C_2018_KFE_D123_V2_LOWER_B_ACTIVE_NEGATIVE_BACKWARD_A_SELECTOR_REPAIR_AND_CHECKPOINT2_REEXECUTION_20260917.md`

This task is deliberately narrow. It may repair only the corrected diagnostic selector's accepted lower-b branch-domain omission, run focused tests, then perform exactly one fresh V2 checkpoint-2 policy-map attempt. If the full map succeeds, it may assemble one Q2 and compute checkpoint-2 Bellman/value/policy/operator/cycle diagnostics. It must stop before any `V2->V3` HJB update and before any terminal KFE/topology/SVD work.

No production/source-faithful change, MATLAB, outer/firm/GE/annual/IRF/Results call or scientific retry is authorized.

## Next Reviewer action

When Builder returns the repair/reexecution candidate, independently inspect:
- exact code diff and whether only lower-face branch-domain coverage changed;
- focused tests, especially lower-b backward/forward negative cases and upper-b regression;
- scientific call ledger;
- fresh V2 checkpoint-2 receipt set;
- if reached, Q2 and B2/D2/stability/cycle evidence.

If the repaired checkpoint-2 map exposes a different first failure, treat that as the next scientific object rather than repairing it inside the same task. If checkpoint 2 completes, decide the next bounded continuation/terminal gate from the frozen law. Production, GE and Results remain closed.
