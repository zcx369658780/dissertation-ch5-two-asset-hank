# Chapter 5 当前交接 — coordinate-resolved selector/floor matched-control diagnostic active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_ACTIVE`。

最新 accepted spatial-audit candidate：`1e76a9222eb2ba6dff485b49f0c2c9ffa30af379`。
Acceptance：`docs/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACCEPTANCE.md`。
Freeze：`docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. Finer-J and finer-I routes remain closed.

Accepted six-failure temporal mechanism panel is heterogeneous. Accepted offline spatial audit is also heterogeneous at the value-update-argmax level: 江西 and 甘肃 are liquid-upper-bound concentrated; 天津、山西、重庆、贵州 are mixed. This does not establish selector/floor localization because the prior traces lack changed-cell coordinates and floor-hit coordinates.

Current exact task therefore performs coordinate-resolved observational replay for exactly seven preregistered provinces: failures 天津、江西、贵州、甘肃 and successful controls 湖南、上海、福建. Each gets exactly one fresh source-style HJB with accepted inputs, maxit100/tolerance unchanged. KFE=0, scientific retries=0. Instrumentation may observe selector changed-cell coordinates and derivative-floor hit coordinates but may not affect scientific control flow.

Matched-control comparison is essential: a boundary concentration that is equally present in successful controls is not failure-specific evidence. Conversely, a failure-specific concentration remains diagnostic evidence only and does not itself authorize boundary, grid, HJB, wage, return, or calibration changes.

No new synthetic `(ra,w)` point, firm/wage/return recalculation, KFE, outer model, MATLAB, K1B/K2, GE, downstream, shock, IRF or Results runtime is authorized.

Owner retains authority over structural equations, major economic calibration, causal interpretation and Results eligibility. ChatGPT Reviewer retains bounded local numerical/debug route authority.
