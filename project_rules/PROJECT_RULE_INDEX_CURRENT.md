# Chapter 5 当前规则入口

更新：2026-09-21；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：

`zcx369658780/dissertation-ch5-two-asset-hank`

开始任何工作先读取：

1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_UNIQUE_CLOSED_CLASS_SUPPORT_KFE_OWNER_ADOPTION_20260920.md`
6. `docs/CH5_MP4C_CORRECTED_INITIAL_TURN_FULL_CLOSURE_ACCEPTANCE_20260920.md`
7. `docs/CH5_MP4C_TURN2_F0579_PRE_ROOT_FALSE_NEGATIVE_FORENSIC_ACCEPTANCE_20260920.md`
8. `docs/CH5_MP4C_TURN2_RUN002_F0364_SELECTOR_FAILURE_ACCEPTANCE_20260920.md`
9. `docs/CH5_MP4C_TURN2_F0364_NEGATIVE_RATIO_SWITCHING_FALSE_NEGATIVE_ACCEPTANCE_20260921.md`
10. current active task.

Current status:

`F0364_NEGATIVE_RATIO_SWITCHING_FALSE_NEGATIVE_CONFIRMED__INTERIOR_B_REPAIR_TURN1_POLICY_PARITY_AND_TURN2_RUN003_ACTIVE`.

Current active Builder task:

`tasks/CH5_MP4C_INTERIOR_B_NEGATIVE_RATIO_SWITCHING_REPAIR_TURN1_PARITY_AND_TURN2_RUN003_20260921.md`.

Results eligibility=`FALSE`.

Important current facts:

- corrected initial turn remains fully accepted, but its compatibility with the new interior-b negative-ratio implementation must now be proven by exact policy-map replay before turn 2 continues;
- active-upper-b negative branch-enumeration repair remains accepted;
- F0364 forensic proves the current ratio<=0 interior-a switching guard is a false negative at an interior liquid node;
- Owner-adopted switching authority requires q_b>0, unchanged D3 KKT and q_a inside the closed sorted derivative interval, but does not require q_a>0 or ratio>0;
- authorized new repair is limited to interior liquid nodes with finite negative nonzero ratio and sign-aware endpoint mapping;
- active liquid-face negative-ratio behavior remains unchanged;
- ratio zero remains fail closed;
- fresh turn-2 run003 is gated on exact replay parity of all 408 accepted turn-1 policy maps;
- turn 3, K1B, K2, GE and Results remain closed.
