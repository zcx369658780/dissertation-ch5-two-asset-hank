# Chapter 5 当前交接 — household asset-grid precision receipt repair active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_TASK_ACTIVE`。

最新 accepted Stage A candidate：`32763fac5a7c4a04dc8278a9069443f35c7c7e3c`。
Accepted blocked precision candidate：`e3b470f623232fcaf52ad50474178f79a2b0b9b9`。
Blocked-execution acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_BLOCKED_EXECUTION_ACCEPTANCE.md`。
Repair freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION.md`。
Results eligibility=`FALSE`。

Accepted Stage A facts：temporary diagnostic household bridge `h=1`；`a=[0,100]`、`b=[-2,20]`、`I=J=20`；`rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。9/9 HJB legal/converged，9/9 KFE-valid。Liquid marginal 9/9 modal `b=2.6315789473684212`，0/9 modal `b=20`；旧 `bmax=5` pile-up 已在 tested grid 上清除。

Blocked precision execution：representative state `rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20],h=1`；P1 `I=20,J={40,80,160}` HJB 3/3 legal/converged。三次 KFE numerical solve 返回后，旧 receipt/postprocessor 因固定 20-bin illiquid marginal 假设拒绝 finer-J results；无完整 finer-grid KFE receipts。Scientific retries=0，P2=0。Reviewer 已接受该 candidate 为 truthful blocked execution，而不是 grid-instability 或 recalibration evidence。

当前 exact task 先执行 R0 engineering repair：仅把 task-owned receipt/postprocessing 改为 grid-generic，必须保持 accepted HJB/KFE numerical solver、equations、parameters、asset bounds、mapping、guards 不变，并用 focused tests 证明 J20/40/80/160（以及相关 I20/40/80）均可提取 receipt，且 J20 行为不变。

R0 PASS 后 fresh rerun 原 P1：复用 accepted I20/J20 reference，只新跑 I20/J40、I20/J80、I20/J160；每点 exactly one HJB，合法收敛才 exactly one KFE；scientific retries=0。P1 稳定才进入 P2：J160 下新跑 I40、I80。禁止更细点和 full cross-state grid。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。完成后 STOP，等待 ChatGPT Reviewer 独立验收。
