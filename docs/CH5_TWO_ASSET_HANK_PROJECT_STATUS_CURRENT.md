# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTED_AND_ACCEPTED__FRESH_TURN2_RUN005_ACTIVE`

Results eligibility=`FALSE`。

## Accepted implementation

Accepted candidate:

`5dbd04ad4aaf252381283501d762d633f504ba07`

Acceptance:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_ACCEPTANCE_20260921.md`

The Owner-adopted deterministic global halving invariant-domain law is now implemented in both corrected HJB update paths.

Exact persisted replay:

- 0->1 alpha=1
- 1->2 alpha=1
- 2->3 alpha=0.5
- relaxed 2->3 state SHA-256:
  `987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF`.

No fresh HJB runtime was executed by the implementation task.

## Active task

`tasks/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_20260921.md`

The task executes one fresh canonical turn2 from the exact accepted entering state.

It must stop at the first new scientific failure.

If all 31 HJB/KFE blocks pass, it may perform exactly one integration and persist the raw turn3 candidate, but turn3 household execution remains forbidden.
