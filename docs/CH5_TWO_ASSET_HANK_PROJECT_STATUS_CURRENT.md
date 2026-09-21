# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`MONOTONICITY_PRESERVING_HJB_RELAXATION_PROPOSAL_ACCEPTED__OWNER_SCIENTIFIC_DECISION_REQUIRED`

Results eligibility=`FALSE`。

## Latest accepted design

Accepted candidate:

`9ad1c844b331ae4b131b57aeb70ade127b82000e`

Acceptance:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_SCIENTIFIC_DESIGN_GATE_ACCEPTANCE_20260921.md`

Accepted proposal:

- one full implicit solve remains mandatory;
- if its represented V candidate has all 760 raw b slopes finite and strictly positive, accept alpha=1;
- otherwise test global convex relaxation alpha=1/2,1/4,...,2^-52;
- accept the first represented candidate with all raw b slopes >0 and no bitwise stagnation;
- otherwise fail closed.

Persisted replay leaves updates 0->1 and 1->2 unchanged and accepts alpha=0.5 for 2->3.

## Owner decision gate

Decision brief:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_OWNER_DECISION_BRIEF_20260921.md`

No Builder task is active.

The current Owner-adopted full-update / no-relaxation law remains authoritative until Owner explicitly adopts or rejects the proposal.

No implementation, fresh HJB continuation, turn2 replay, turn3, K1B, K2, GE or Results is authorized.
