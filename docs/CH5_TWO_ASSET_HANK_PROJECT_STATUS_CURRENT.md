# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`OWNER_ADOPTED_MONOTONICITY_PRESERVING_HJB_RELAXATION__IMPLEMENTATION_AND_PERSISTED_REPLAY_ACTIVE`

Results eligibility=`FALSE`。

## Owner-adopted HJB update extension

Owner adopted:

`OWNER_ADOPTED__MONOTONICITY_PRESERVING_HJB_RELAXATION__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK`

Authority:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_OWNER_ADOPTION_20260921.md`

The full implicit solve remains unique. After it passes the existing backward-error gate, the represented next state must remain inside the strict-positive raw liquid-slope domain.

Alpha search is exactly:

`1,1/2,1/4,...,2^-52`.

The first passing represented global convex candidate is accepted; otherwise fail closed.

## Active task

`tasks/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_20260921.md`

This task implements the adopted law and validates exact parity on already accepted persisted 黑龙江 updates.

Fresh HJB solves, selector maps, D2/KFE, turn2 continuation and integration remain forbidden.

After implementation acceptance, a separate fresh-runtime task may be published.
