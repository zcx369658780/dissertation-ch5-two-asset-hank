# Chapter 5 当前规则入口

更新：2026-09-21；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：

`zcx369658780/dissertation-ch5-two-asset-hank`

开始任何工作先读取：

1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_OWNER_ADOPTION_20260921.md`
6. current active task.

Current status:

`OWNER_ADOPTED_MONOTONICITY_PRESERVING_HJB_RELAXATION__IMPLEMENTATION_AND_PERSISTED_REPLAY_ACTIVE`.

Results eligibility=`FALSE`.

Current active Builder task:

`tasks/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_20260921.md`.

Important current facts:

- Owner adopted deterministic global halving invariant-domain relaxation;
- exact alpha schedule is 1 then 2^-k, k=1..52;
- all represented raw b slopes must be finite and strictly >0;
- bitwise stagnation is rejected;
- one full solve plus arithmetic relaxation remains one HJB update;
- existing B/D thresholds, cycle rules, 100-update ceiling, D1/D2/D3, selector and terminal KFE laws remain unchanged;
- active task implements the law and replays accepted persisted updates only;
- fresh HJB/turn2 execution is still forbidden.
