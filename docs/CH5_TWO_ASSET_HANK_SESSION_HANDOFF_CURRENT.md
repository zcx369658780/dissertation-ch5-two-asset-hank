# Chapter 5 当前交接 — nonlinear continuation fail-closed at V2 cell100 / zero-science attribution active

更新：2026-09-17。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
状态：`NONLINEAR_CONTINUATION_FAIL_CLOSED_AT_V2_CELL100__ZERO_SCIENCE_ATTRIBUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Governance

Owner is final scientific authority; ChatGPT is L3 Reviewer/scientific-route authority; Codex is bounded Builder. GitHub live `main` is repository-state authority. `deep-learning-hank` is separate and must never be used for this route.

Protected/source-faithful MATLAB remains read-only. Corrected diagnostic work is separate from production replacement.

## Accepted route before the current failure

The corrected route has:

- accepted V0 policy map and Q0;
- accepted direct HJB step `V0->V1`;
- accepted V1 remap and Q1;
- Q1 one closed class `[5,6,405,406]`;
- accepted pin-free/source-free Q1 invariant mass, numerical rank/nullity `799/1`;
- accepted nonlinear design with state `V_n`, same-value derived `(P_n,u_n,Q_n)`, terminal-only KFE and fixed `Delta=1000`;
- Owner-adopted corrected-target convergence law.

Owner convergence law:

- Bellman residual `<=1e-8`;
- value change `<=1e-7`;
- both at the same checkpoint;
- policy/operator stability diagnostic only;
- direct-solve backward error `<=1e-12`;
- exact period `k>=2` and frozen approximate period-2/3 cycle rules fail closed;
- maximum 100 total HJB updates;
- no damping, relaxation, adaptive Delta, continuation, clipping, artificial diffusion, solver substitution, scientific retry or post-hoc tolerance tuning.

## Latest accepted fail-closed runtime

Builder candidate:
`922cd9118d617c044209515762ccecc9ec3fd34d`

Reviewer acceptance:
`docs/CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_FAIL_CLOSED_ACCEPTANCE_20260917.md`

Execution report:
`docs/CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_REPORT.md`

Key facts:

- checkpoint 1 raw metrics: `B1=0.014710294187010184`, `D1=0.47118375690461445`; not converged;
- exactly one new direct solve `V1->V2` passed the linear gate;
- residual infinity norm `1.9012569296705806e-14`;
- normwise backward error `2.5514110567283015e-16`;
- V2 SHA-256 `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`;
- checkpoint-2 policy map cells 0-99 passed;
- first failure flat F index `100`, zero-based `(0,5,0)`, physical `b=-2.0, a=2.6315789473684212, z=0.8`;
- derivatives at failure: `p_b^B=p_b^F=0.012333311206716577`, `p_a^B=0.00903315440190679`, `p_a^F=0.008957007194295222`;
- outcome `NO_ADMISSIBLE_POLICY`, zero admissible comparisons;
- no complete P2/u2/Q2; D2 assemblies 0; KFE calls 0; scientific retries 0.

The raw receipt includes rejection reasons such as lower-b primal infeasibility, derivative-direction inconsistency, transfer sign/KKT failure and one `ROOT_FAILURE_NO_UNIQUE_BRACKET`. These are evidence only, not permission to repair.

## Current active task

`tasks/CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_20260917.md`

This task must use only persisted evidence/static source/algebra. All selector/root/policy-map/D2/HJB/KFE/MATLAB/downstream scientific calls are exactly zero.

Required classification:

- `ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`
- `ATTRIBUTED__SELECTOR_OMITS_AUTHORITY_BACKED_LEGAL_BRANCH`
- `ATTRIBUTED__ROOT_IMPLEMENTATION_OMISSION_WITHIN_AUTHORIZED_BRANCH`
- `BLOCKED__OWNER_SCIENTIFIC_DECISION_REQUIRED`
- `BLOCKED__INSUFFICIENT_PERSISTED_EVIDENCE`

No repair/reexecution or successor task by Builder.

## Interpretation boundary

The current evidence does not establish nonlinear HJB convergence or nonexistence, a terminal KFE for V2, a household fixed point, GE, market clearing, production replacement or Results. The immediate scientific problem is strictly local attribution of the first V2 selector failure at lower-b boundary cell flat 100.