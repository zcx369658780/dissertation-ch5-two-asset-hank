# Chapter 5 两资产 HANK 当前状态

更新：2026-09-17。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`NONLINEAR_CONTINUATION_FAIL_CLOSED_AT_V2_CELL100__ZERO_SCIENCE_ATTRIBUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted scientific checkpoint

Owner-adopted D1/D2/D3 corrected semantics、lower-a zero-kink multiplier handling、interior zero-liquid Z switching、Option-A V0 map/Q0、一次 direct HJB step V1、V1 remap Q1，以及 Q1 source-free unique invariant mass均已接受。Source-faithful/production paths remain frozen。

Accepted nonlinear design and Owner convergence law remain authoritative:

- Bellman residual `<=1e-8`;
- value change `<=1e-7`;
- both required at the same checkpoint;
- policy/operator stability diagnostic only;
- direct-solve normwise backward error `<=1e-12`;
- exact period `k>=2` recurrence and frozen approximate period-2/3 rules fail closed;
- at most 100 total HJB updates;
- fixed `Delta=1000`;
- no damping、relaxation、adaptive Delta、continuation、clipping、artificial diffusion、solver substitution、scientific retry or post-hoc tolerance tuning.

## Bounded nonlinear continuation result

Builder candidate `922cd9118d617c044209515762ccecc9ec3fd34d` is Reviewer-accepted as fail-closed evidence by:
`docs/CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_FAIL_CLOSED_ACCEPTANCE_20260917.md`.

Accepted facts:

- checkpoint 1: `B1=0.014710294187010184`, `D1=0.47118375690461445`; both fail the Owner convergence law;
- exactly one new direct update `V1->V2` passed the linear accuracy gate with residual `1.9012569296705806e-14` and backward error `2.5514110567283015e-16`;
- accepted V2 field SHA-256: `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`;
- fresh V2 policy remap passed cells 0-99 and failed first at flat F index `100`, `(i_b,i_a,i_z)=(0,5,0)`, physical `(-2.0,2.6315789473684212,0.8)`, with `NO_ADMISSIBLE_POLICY` and zero admissible comparisons;
- no complete P2/u2/Q2 exists; no D2/Q2, B2/D2/cycle or KFE gate was reached;
- no scientific retry or numerical-law modification occurred.

This does not prove nonlinear HJB nonexistence. It proves only that the frozen corrected selector, at the accepted V2 derivatives for the first failing cell, currently has no admissible selected branch.

## Active Builder task

`tasks/CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_20260917.md`

This is zero-science forensic attribution only. It must determine whether cell 100 is a genuine local KKT/input incompatibility, an omitted authority-backed legal branch, an authorized-root implementation omission, or a new Owner scientific-decision gate.

No selector/root/policy-map/D2/HJB/KFE/MATLAB/downstream scientific call is authorized in this attribution task. No runtime repair/reexecution is authorized until independent acceptance.

Production replacement、market clearing、GE、annual calibration、dynamics、IRF、welfare、causal interpretation and Results remain unauthorized.