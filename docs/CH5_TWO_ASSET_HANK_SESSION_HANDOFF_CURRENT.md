# Chapter 5 当前交接 — complete checkpoint 2 accepted / bounded nonlinear continuation active

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
状态：`CHECKPOINT2_COMPLETE_NONCONVERGED__BOUNDED_NONLINEAR_CONTINUATION_TO_CHECKPOINT6_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Governance

Owner is final scientific authority; ChatGPT is L3 Reviewer/scientific-route authority; Codex is bounded Builder. GitHub live `main` is repository-state authority. `deep-learning-hank` remains separate and must never be used for this route.

## Major accepted milestone

The corrected V2 policy map now completes all 800 cells under the adopted multidimensional switching laws.

Accepted checkpoint 2:

- V2 SHA `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`
- P2 identity `EBCBABC0593EF163D2E7FA300F6FFEB6E3C187D232D4CCEA5D59AB7180CD1D95`
- u2 SHA `C222F4B147F48EA177A28AAF289F3ED5EA76F531BC08201070DD63698BF98D73`
- Q2 SHA `346DBCDA13392DAF6897DC185767B0E7C5961AA76A9AAA686053AEDA33C02F9F`
- checkpoint identity `71DC6975E814060A4F63961A736E6E9DDF766C51CE4672C3EF777E5E15B80C2C`
- D2 PASS.

Primary convergence fails at checkpoint 2:

- `B2=0.006582827785543588`
- `D2=0.05439336697877817`.

Thus the project has moved past local selector-closure work at V2 and back into the frozen nonlinear HJB trajectory.

## Active task

`tasks/CH5_MP4C_2018_KFE_D123_CHECKPOINT2_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919.md`.

The task binds accepted checkpoint 2 and may perform at most four updates through V6.

It does not remap V2 before the first update.

For checkpoints 3-6:

- one fresh policy map each;
- one D2/Q each only after map completion;
- B/D and policy/operator diagnostics;
- primary convergence first;
- exact cycle next;
- approximate period-2/3 only when full windows exist;
- direct solve to next checkpoint only if all gates remain nonterminal.

Earliest complete approximate period-2 window: checkpoint 4.
Earliest complete approximate period-3 window: checkpoint 6.

If any new selector/scientific issue appears, stop without repair.

Even if HJB convergence is reached, terminal topology/KFE is deferred to a separate Reviewer gate.

## Downstream

Household HJB convergence, terminal household KFE, market clearing, production replacement, GE, annual dynamics, IRFs, welfare and Results remain open/closed according to their later gates. Results eligibility is still FALSE.
