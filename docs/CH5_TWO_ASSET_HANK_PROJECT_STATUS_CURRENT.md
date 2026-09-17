# Chapter 5 两资产 HANK 当前状态

更新：2026-09-17。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`V2_LOWER_B_SELECTOR_BRANCH_OMISSION_ACCEPTED__MINIMAL_REPAIR_AND_CHECKPOINT2_REEXECUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted attribution

Reviewer accepted Builder candidate `582f7fca52e47ee5303164edbc62b98add363ec6` as:
`ATTRIBUTED__SELECTOR_OMITS_AUTHORITY_BACKED_LEGAL_BRANCH`.

Accepted causal finding:
- lower-b active multiplier domain is `q_b >= p_b`;
- frozen corrected selector incorrectly used upper-face-style `0 < q_b <= p_b` in the active lower-b negative-transfer derivative pre-screen;
- this omitted the authority-backed active lower-b / negative-transfer / backward-`a` case, yielding seven persisted cases where the frozen census requires eight;
- static algebra shows the omitted cell100 case would still be rejected under the accepted V2 inputs, so the defect is branch coverage rather than evidence of a new admissible cell100 policy;
- positive active root failure is a genuine no-root condition on the legal lower-face domain;
- interior-Z remains inapplicable at the liquid lower boundary.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_ACCEPTANCE_20260917.md`.

## Frozen nonlinear facts

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Checkpoint 1 remains the last complete same-value checkpoint until a repaired complete V2 map exists:
- `B1=0.014710294187010184`;
- `D1=0.47118375690461445`;
- V1->V2 direct solve residual `1.9012569296705806e-14`;
- backward error `2.5514110567283015e-16`.

Owner convergence law remains unchanged: `B<=1e-8` and `D<=1e-7` at the same checkpoint, fixed `Delta=1000`, frozen cycle rules, no damping/continuation/tolerance retuning, and maximum 100 total HJB updates.

## Active Builder task

`tasks/CH5_MP4C_2018_KFE_D123_V2_LOWER_B_ACTIVE_NEGATIVE_BACKWARD_A_SELECTOR_REPAIR_AND_CHECKPOINT2_REEXECUTION_20260917.md`

The task authorizes only:
1. minimal corrected diagnostic selector repair for the accepted lower-b active negative/backward-`a` branch-domain omission;
2. focused branch-completeness/regression tests;
3. exactly one fresh V2 checkpoint-2 policy-map attempt;
4. only if the full map completes, at most one Q2 assembly and checkpoint-2 Bellman/value/stability/cycle diagnostic evaluation.

The task explicitly authorizes zero `V2->V3` HJB updates, zero terminal topology/KFE/SVD work, zero MATLAB/production/GE/annual/IRF/Results calls and zero scientific retries.

Production/source-faithful paths remain frozen. This stage does not establish nonlinear HJB convergence/nonexistence, terminal KFE, household fixed point, market clearing, GE or Results.
