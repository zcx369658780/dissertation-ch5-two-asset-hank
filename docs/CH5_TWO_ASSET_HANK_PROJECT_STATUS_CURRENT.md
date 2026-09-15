# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_TASK_ACTIVE`。

最新 accepted finer-precision candidate：`e3db1ada75619a7db0139cef0da4aaabbb351690`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_ACCEPTANCE.md`。
Current freeze：`docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

代表状态继续冻结：`rb=.02, ra=.0675, w=15.5, a=[0,100], b=[-2,20], h=1, I=20`。Accepted HJB/KFE equations、FOC、selector、boundary、derivative floor、solver、tolerance、maxit=100、wage/return mappings、guards 与经济参数均不得改变。

Finer-precision escalation 已由 Reviewer 接受为 truthful numerical-blocked execution。J320 HJB 收敛44次迭代并得到有效 KFE：`At=89.16979926`、`Bt=5.81764933`、modal `a=95.29780564`、modal `b=2.63157895`；相对 J160，`Delta At=-0.12802605`，a-CDF distance=`0.0021292541`，amax mass=0，fixed-I20 bmax mass约`0.0010587541`。

J640 唯一 HJB 在 frozen maxit=100 后未收敛，final convergence statistic约`0.0012277767`；无 illegal iteration、hard error 或非有限/shape failure。KFE 正确未运行，J1280 按 hard stop 正确未启动。该事件当前仅可解释为 numerical nonconvergence，不能自动升级为 domain/scale pathology，也不能建立 illiquid-grid stabilization 或 smallest defensible stabilized J。

当前任务只允许在同一 J640 输入上进行 exactly one fresh-initialized HJB diagnostic replay，maxit仍100、tolerance不变，仅增加 task-owned observation/instrumentation，用于区分 slow convergence、policy/selector chatter、value oscillation、derivative-floor amplification 或低周期循环。KFE=0，J1280=0，scientific retries=0。

禁止：增加 maxit、damping/relaxation、改 tolerance、修改 HJB/KFE science、J1280、J>1280、liquid-I ladder、multi-state/finer 3x3、asset-domain change、recalibration、global/GE/Results runtime。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。
