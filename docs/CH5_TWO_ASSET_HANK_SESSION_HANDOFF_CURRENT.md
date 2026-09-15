# Chapter 5 当前交接 — J640 HJB nonconvergence mechanism diagnostic active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_TASK_ACTIVE`。

最新 accepted candidate：`e3db1ada75619a7db0139cef0da4aaabbb351690`。
Acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_ACCEPTANCE.md`。
Freeze：`docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Accepted finer-precision facts：J320 HJB converged in 44 iterations and KFE valid；`At=89.16979926`、`Bt=5.81764933`、modal `a=95.29780564`、modal `b=2.63157895`。相对 accepted J160，`Delta At=-0.12802605`、a-CDF distance=`0.0021292541`、b-CDF distance=`0.0007585373`；amax mass仍0，fixed-I20 bmax mass约`0.0010587541`。

J640 HJB 在 frozen maxit=100 后未收敛，final statistic约`0.0012277767`；没有 illegal iteration、hard error 或 finite/shape failure。KFE 未运行，J1280 未启动，scientific retries=0。这是 accepted numerical nonconvergence evidence，不是 domain/scale pathology 结论。

当前 exact task 只做一次 J640 fresh-initialized diagnostic replay，输入保持 `rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20],h=1,I=20,J=640,Nz=2`。HJB scientific behavior、tolerance、maxit=100 全部冻结；只允许 task-owned instrumentation 记录每次迭代的 value-change、A2max、selector/policy switching、derivative-floor hits 与循环/重复状态证据。

本任务 HJB exactly1；KFE0；J1280=0；scientific retries0；不得增加 maxit、damping、改 tolerance、改 HJB/KFE algorithm、改 domain/parameter/mapping/guard，也不得运行 global/GE/Results。

Reviewer 要求先判断失败机制，再决定是否仍值得追求 finer-grid precision。不得从 final statistic 单独推断 slow convergence。

Owner 已授权 ChatGPT Reviewer 对此类局部数值调试作 bounded、预注册决策并发布 exact task；结构模型、主要校准与 Results eligibility 仍保留 Owner authority。
