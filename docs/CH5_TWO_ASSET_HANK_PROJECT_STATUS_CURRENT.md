# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`LOCAL_BASIN_ROUTE_CLOSED_FOR_NOW__RETURNED_TO_MULTI_PROVINCE_INTEGRATION__KFE_OWNER_DECISION_PACKAGE_ACTIVE`。

Latest accepted local-basin Builder candidate：`c994cee14b5958e47078bd7281acffcbe56797e5`。
Latest local-basin Reviewer acceptance：`docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`。
KFE mechanism acceptance：`docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_ACCEPTANCE.md`。
Current route freeze：`docs/CH5_MP4C_2018_KFE_CLOSURE_ROUTE_FREEZE_20260915.md`。
Current active Builder task：`tasks/CH5_MP4C_2018_KFE_OWNER_DECISION_RECOVERY_AND_OPTION_MATRIX_ZERO_SCIENCE_20260915.md`。
Results eligibility=`FALSE`。

## HJB numerical authority remains frozen

Accepted practical household grid：`I=20,J=160,Nz=2,a=[0,100],b=[-2,20],h=1`，仅为 `PRACTICAL_BOUNDED_DIAGNOSTIC_GRID`。Finer-J / finer-I routes 已关闭；accepted FOC、selectors、boundary laws、derivative-floor logic、sparse solve、`tol=1e-7`、`maxit=100`、A2max legality gate `.01` 均不变。

31省 first-turn HJB：25/31 converged；天津、山西、江西、重庆、贵州、甘肃为 legal nonconverged；0 illegal operator、0 hard error、KFE=0。Temporal/spatial/matched-control evidence显示失败机制异质，successful controls也存在 substantial upper-b activity，因此 common failure-specific upper-b pathology 不成立。

Input/outcome envelope 与 guards 不提供可分离的 safe-price rule。Local-basin四对 topology 为山西→河北 `F→C→C→C→C`、重庆→河北 `F→C→C→C→C`、江西→安徽 `F→F→C→C→C`、贵州→四川 `F→C→F→C→C`；panel=`LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`。这些仅是 numerical HJB basin evidence。

Reviewer 已决定当前不再增加 synthetic `t`、matched pairs、adaptive bisection 或 basin mapping。若未来出现能够直接改变 integration decision 的新问题，可另行预注册最小诊断；当前 route B 优先。

## KFE integration blocker

Accepted corrected-2018 five-turn attribution 已确认：turn4/5 全部 62 province-turn objects 存在同一 finite-box upper-`b` escape + MATLAB-style dropped-equation/pinning algebra；material source-free residual 几乎全部落在被替换的 pin equation，off-pin residual 为 machine scale。Dropped equation 等价于一个平衡 upper-b escape 的 algebraic source，但该 source 不是已接受的 household entry/exit economics。

因此 KFE blocker 已从“机制未知”推进到“closure semantics 未决”。不能自动通过修改 upper-b boundary、扩大 bmax、加入 source、移植/删除 pinning 或改变 production KFE 来制造 closure。

Owner 保留 finite-domain/KFE closure scientific semantics 的最终选择权。当前 Builder 只执行 zero-science D1-D3 authority recovery + option matrix，不运行模型、不选择方案。

## Runtime state

Reviewer本次 route decision / GitHub publication scientific runtime=`0`。
在 Owner 选择 closure semantics 且 Reviewer 发布后续 scientific task 前：HJB=0、KFE=0、outer=0、firm=0、wage/return recalculation=0、MATLAB=0、GE=0、annual=0、shock=0、IRF=0、Results=0。
