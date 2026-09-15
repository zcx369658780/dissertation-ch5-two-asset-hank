# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_ACTIVE`。

最新 accepted spatial-audit candidate：`1e76a9222eb2ba6dff485b49f0c2c9ffa30af379`。
Reviewer acceptance：`docs/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACCEPTANCE.md`。
Current freeze：`docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Accepted practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. Finer-J and finer-I escalation routes remain closed; no maxit/tolerance/damping/relaxation/line-search changes are authorized.

Accepted first-turn HJB viability remains 25/31 converged and 6 legal nonconverged. Accepted six-failure mechanism panel is heterogeneous: 天津、山西、重庆、甘肃 chatter; 江西 derivative-floor amplification after earlier switching; 贵州 joint-selector period-2 recurrence without exact value recurrence.

The accepted trace-only spatial audit adds that value-update argmax localization is also heterogeneous: 江西 and 甘肃 are liquid-upper-bound concentrated under the preregistered argmax metric, while 天津、山西、重庆、贵州 are mixed. The four chatter provinces therefore do not share one value-argmax spatial signature.

However, the sealed traces do not contain selector changed-cell coordinates or derivative-floor coordinates. Therefore value-argmax localization cannot be treated as the full instability footprint, and no common boundary repair, grid expansion, HJB modification, or price recalibration is authorized from that audit alone.

The active task replays a preregistered seven-province matched panel with observational coordinate-resolved instrumentation only: failures 天津、江西、贵州、甘肃 and successful controls 湖南、上海、福建. Exactly one fresh HJB per province; KFE=0; scientific retries=0. The purpose is to compare selector-switch and derivative-floor spatial footprints between failures and converged controls without changing science.

The corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning KFE blocker remains separate and unresolved.
