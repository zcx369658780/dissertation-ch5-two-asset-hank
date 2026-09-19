# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`CHECKPOINT2_COMPLETE_NONCONVERGED__BOUNDED_NONLINEAR_CONTINUATION_TO_CHECKPOINT6_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted complete checkpoint 2

Reviewer accepted Builder candidate `62d01dac0eb1e516386cf6336837b5a2ef4463e5`.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_ACCEPTANCE_20260919.md`.

The Owner-adopted joint two-axis switching law is implemented and accepted. The accepted V2 policy map completes `800/800` cells.

Key checkpoint-2 identities:

- V2: `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`
- P2: `EBCBABC0593EF163D2E7FA300F6FFEB6E3C187D232D4CCEA5D59AB7180CD1D95`
- u2: `C222F4B147F48EA177A28AAF289F3ED5EA76F531BC08201070DD63698BF98D73`
- Q2: `346DBCDA13392DAF6897DC185767B0E7C5961AA76A9AAA686053AEDA33C02F9F`
- full checkpoint identity: `71DC6975E814060A4F63961A736E6E9DDF766C51CE4672C3EF777E5E15B80C2C`.

D2 passes.

Checkpoint 2 is nonconverged:

- `B2=0.006582827785543588 > 1e-8`
- `D2=0.05439336697877817 > 1e-7`.

No cycle is established at checkpoint 2.

## Active task

`tasks/CH5_MP4C_2018_KFE_D123_CHECKPOINT2_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919.md`.

The task reuses accepted V2/P2/u2/Q2 and may execute up to four new direct HJB updates, ending no later than checkpoint 6.

At every new checkpoint it must freshly map policies, assemble D2/Q, compute B/D and stability diagnostics, then apply primary convergence, exact-cycle and applicable approximate period-2/3 rules before any next update.

It must stop immediately on any failure, convergence or cycle condition.

Terminal KFE/topology/SVD, production, GE and Results remain forbidden.

## Update accounting

- V0->V1: accepted update 1
- V1->V2: accepted update 2
- active task may consume updates 3-6
- global ceiling: 100.

No damping, relaxation, adaptive Delta, solver substitution, retry or tolerance retuning is authorized.
