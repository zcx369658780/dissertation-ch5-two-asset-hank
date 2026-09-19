# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`CHECKPOINT10_COMPLETE_NONCONVERGED__BOUNDED_NONLINEAR_CONTINUATION_TO_CHECKPOINT12_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted trajectory through checkpoint 10

Reviewer accepted Builder candidate `537ed052a674d5f38f3586d6c94528af5e76b48b`.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT6_TO_CHECKPOINT10_BOUNDED_NONLINEAR_CONTINUATION_ACCEPTANCE_20260920.md`.

Checkpoints 7-10 are complete. Every policy map completes 800/800. Every D2 gate passes. Every direct solve passes the frozen backward-error gate. No exact or authorized approximate cycle is detected.

Recent metrics:

- checkpoint 7: `B7=9.83868092531745e-4`, `D7=2.7865782347942236e-3`
- checkpoint 8: `B8=1.6252618227152738e-4`, `D8=6.617669262674042e-4`
- checkpoint 9: `B9=8.986962138773924e-6`, `D9=1.1033293848816683e-4`
- checkpoint 10: `B10=3.874510913493001e-8`, `D10=5.8692895192891115e-6`.

Checkpoint 10 is close to, but does not satisfy, the frozen `1e-8 / 1e-7` primary thresholds.

## Exact checkpoint 10

- V10 `AE1610BA320F57AF73EE3C5411C298BF00610606B13B5185F2CD65BF1736FB24`
- P10 `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3`
- u10 `215BEC4AABBC337147D73A227751CD6A89CC483E3CA056470A2AEF161AA41F38`
- Q10 `917479763C4690FEAB358098D7F1CE2EBB4DD7C4939A7060156E7A4FCDEE59BD`
- checkpoint identity `4FC2855AB4102AEAE8B173D0EBBBF40FCD334583A039BE4AE65C8DE2B1145C8D`
- checkpoint arrays `BEA1D08A10C53E4EF3246A413A9446633DAAD6A4ACCAD4E34463BB74756C5512`
- D2 PASS
- exact/period-2/period-3 cycle: none.

## Active task

`tasks/CH5_MP4C_2018_KFE_D123_CHECKPOINT10_TO_CHECKPOINT12_BOUNDED_NONLINEAR_CONTINUATION_20260920.md`.

It may consume global updates 11-12 only and must stop immediately on convergence, cycle, selector/D2 failure, solve failure, or checkpoint 12.

Terminal topology/KFE/SVD, production, GE and Results remain closed.
