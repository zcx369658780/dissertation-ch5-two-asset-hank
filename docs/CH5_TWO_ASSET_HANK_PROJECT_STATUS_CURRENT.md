# Chapter 5 两资产 HANK 当前状态

更新：2026-09-19。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`CHECKPOINT3_COMPLETE_NONCONVERGED__BOUNDED_NONLINEAR_CONTINUATION_TO_CHECKPOINT6_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoint 3

Reviewer accepted Builder candidate `ea97d03d065bae1c9fd7cbb98043d0e673d1e4a1`.

Acceptance:
`docs/CH5_MP4C_2018_KFE_D123_V3_CELL100_LOWER_B_NEGATIVE_FORWARD_A_PRE_SCREEN_REPAIR_AND_CHECKPOINT3_REEXECUTION_ACCEPTANCE_20260919.md`.

The lower-b negative pre-screen false negative is repaired under existing authority.

Checkpoint 3 is complete:

- V3 `4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF`
- P3 `06062946687922E1FAC83E8D4B1B19101469CC284339522595A19F4DECB6B07B`
- u3 `9BB321A63A92154D4B733B28126AF29DC1441B95D44517D884F4C858AECFE6F4`
- Q3 `4085E0D1B166E72650CA1E74E5CF9462F6677EEAFA8CDEF1FBD153F14088C255`
- checkpoint identity `0DEEF7E54C4972BFF7BB67AE6B67BA5E54B588F3EEF5ACDE85048F3E02FE715D`.

D2 passes.

Checkpoint 3 remains nonconverged:

- `B3=0.1291770476282596`
- `D3=0.05315900863346279`.

No exact cycle and no complete approximate cycle window at checkpoint 3.

## Active task

`tasks/CH5_MP4C_2018_KFE_D123_CHECKPOINT3_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919.md`.

The task reuses accepted V3/P3/u3/Q3 exactly and may consume updates 4-6 only.

No trend-based stop is authorized solely because B3 increased relative to B2.

Terminal KFE/topology/SVD, production, GE and Results remain closed.
