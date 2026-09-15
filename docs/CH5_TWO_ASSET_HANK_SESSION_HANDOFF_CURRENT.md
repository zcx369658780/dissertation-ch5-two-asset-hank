# Chapter 5 当前交接 — J160 post-science finalizer repair active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_CROSS_STATE_POST_SCIENCE_FINALIZER_REPAIR_TASK_ACTIVE`。

最新 accepted mechanism candidate：`b1c4897c72e3c11c1774ec59145865ae3f5fa6ca`。
Reviewer route decision：`docs/CH5_MP4C_K1_J160_CROSS_STATE_POST_SCIENCE_FINALIZATION_BLOCKER_ROUTE_DECISION.md`。
Freeze：`docs/CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_COMMON_SUPPORT_REPAIR_AND_CLOSEOUT.md`。
Results eligibility=`FALSE`。

J640 chatter diagnostic 已关闭继续追更细 J 的路线；J160 仅作为 provisional practical grid 候选。

上一 J160 cross-state Builder execution 没有 candidate commit，但报告已完成四个授权 fresh science points：HJB 4/4 legal/converged、KFE 4/4 completed、scientific retries=0；center J160 与 J20 references reuse-only。四点没有出现 J640 式 nonconvergence，reported amax mass均0，modal a/b均在内部，bmax mass最大约0.0163。

首次 offline finalizer 随后因 J20 与 J160 support 不同而失败：`ValueError: CDF comparison requires a common support`。J20 使用 `a=[0,10],b=[-2,5]`，J160 使用 `a=[0,100],b=[-2,20]`。原 task 不允许 post-science engineering retry，因此 Builder 正确停止，没有报告/compact evidence/candidate commit。

当前 exact task 是 zero-science closeout：先验证 raw evidence `D:\ProjectTemp\ch5-mp4c-k1-j160-cross-state-evidence-20260915-001` 的完整性和调用账，再只修 task-owned offline finalizer。different-support CDF comparison 必须采用 union interval，support 外 CDF 分别扩展为0和raw total mass，support 内保持既有 cumulative-node-mass + piecewise-linear convention；不得 clip/renormalize/smooth。

J20→J160 的新 metric 必须标记为 `DOMAIN_PLUS_GRID_CDF_DISTANCE`，因为 domain 与 discretization 同时变化，不能作为 pure precision distance。

本任务 HJB=0、KFE=0、scientific retries=0；禁止任何 science rerun、J320/J640/J1280、global/GE/Results runtime。若 raw evidence integrity 不通过，立即 STOP。

Owner 已授权 ChatGPT Reviewer 对此类 bounded numerical/engineering closeout 直接决策；结构模型、主要校准、accepted equations/guards 与 Results eligibility 仍保留 Owner authority。
