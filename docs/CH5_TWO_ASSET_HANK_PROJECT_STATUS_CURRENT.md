# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`TURN2_BEIJING_CHECKPOINT2_SELECTOR_FAIL_ACCEPTED__F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_ACTIVE`

Results eligibility=`FALSE`。

## Accepted corrected initial turn

The first corrected multi-province turn remains fully accepted:

- 31/31 HJB PASS;
- 31/31 Owner-adopted unique-closed-class KFE PASS;
- stationary aggregates PASS;
- one K1A/C1/firm integration PASS;
- canonical raw turn-2 payoff and exact turn-2 entering state accepted.

## Accepted turn-2 failure

Candidate:

`37e563a87bf0dc1fb90224b03e0c4df9daea9d5f`.

Acceptance:

`docs/CH5_MP4C_TURN2_BEIJING_CHECKPOINT2_POLICY_SELECTOR_FAILURE_ACCEPTANCE_20260920.md`.

Turn 2 reached only Beijing.

Checkpoint 0:

- policy/D2 PASS;
- B `0.35948978452765235`;
- direct solve backward error `2.1754586146795478e-16`.

Checkpoint 1:

- policy/D2 PASS;
- B `0.019968227378343403`;
- D `0.5603661628256393`;
- convergence FAIL;
- no exact or approximate period-2/3 cycle;
- direct solve backward error `1.4650295837509506e-16`.

Checkpoint 2 first failure:

- flat F-order index 579;
- state index `(19,8,1)`;
- physical `(b,a,z)=(5,4.2105263157894735,1.3)`;
- selector outcome `NO_ADMISSIBLE_POLICY`;
- D2/Q not assembled.

The current selector therefore fails closed at this turn-2 state.

## Current scientific uncertainty

The failure does not yet establish that the underlying constrained household problem has no feasible policy.

The active upper-b negative-transfer regime is rejected before branch-specific root evaluation because multiple illiquid derivative branches survive the current pre-root viability screen.

The next task determines whether post-root evaluation would leave:

- exactly one admissible branch;
- no admissible branch;
- or a genuine multiple-policy ambiguity.

No selector repair is adopted yet.

## Active task

`tasks/CH5_MP4C_TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_20260920.md`.

No HJB, D2/Q, KFE, aggregate, integration or later-province execution is authorized in this forensic.

Turn 3, K1B, K2, GE and Results remain closed.
