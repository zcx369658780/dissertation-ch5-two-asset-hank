# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`.

状态：

`K1B_TURN4_REPAIRED_ACCEPTED__TURN5_TURN6_BOUNDED_CONTINUATION_ACTIVE`

Results eligibility=`FALSE`.

## Accepted selector repair and historical compatibility

Candidate:

`2155d16ab04f705b1a0da1cc3b49d78e60592c2e`

Acceptance:

`docs/CH5_MP4C_K1B_TURN4_REPAIRED_REEXECUTION_ACCEPTANCE_20260921.md`

Accepted repair:

- production change only in corrected `selector.py`;
- repaired selector blob `51517dde0c829060b6e0c0d594ec60e7e6143883`;
- selector SHA-256 `DC8E0FBB751BA2A6DF58C88923E0A2E31D285D780E0EFE53CB90A580D59E99FE`;
- focused 安徽 and Beijing parity PASS;
- historical selected-policy identity parity `1227/1227`, mismatch 0.

## Accepted repaired K1B turn4

- 31/31 corrected HJB/KFE PASS;
- direct updates 378;
- 374 alpha=1, 4 alpha=.5, exhaustion 0;
- max B `3.5233607698081926e-11`;
- max D `3.523143110584215e-08`;
- exactly one frozen-share K1B/C1 integration PASS;
- completed-turn4 raw ra0 SHA `0312EBE6C2764DB3A834F1233712186ED1B6CE0C3E8BC01E58EFF6A0E8DCD267`;
- turn5 share SHA `2BDF7B8226C8404DB9C7FFEEE3F72F7AE9CA1305905460A4E2430AABEA4D3B06`;
- turn5 rah SHA `5CAF9166D85198E6923FFCD5A1F92D278C8A1C6CB924E8DD1B843F875E91D88E`;
- turn5 household not run.

Turn3->turn4 changes are modest but remain diagnostic only; no convergence is claimed.

## Active task

`tasks/CH5_MP4C_K1B_TURN5_TURN6_BOUNDED_CONTINUATION_DIAGNOSTIC_20260921.md`

The task executes exactly two more K1B-active turns, turn5 and turn6, under unchanged science. It prepares turn7 and stops before turn7 household.

The trajectory panel may report change-norm ratios but they are not pass criteria and cannot establish convergence.

K2, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
