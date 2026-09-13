# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`REAL_WAGE_SCAN_COMPLETE__MACRO_DIMENSIONAL_RELATION_UNRESOLVED__JOINT_RECALIBRATION_OWNER_REVIEW_REQUIRED`。

本轮 exact Builder task 已完成，active Builder task=`NONE`；未发布 successor task。Candidate 等待 ChatGPT Reviewer 独立 ACCEPT/REJECT。Results eligibility=`FALSE`。

真实 household composite-wage standalone grid 为 `rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。HJB 9/9 legal/converged；KFE 9/9；9/9 均为 `INTERIOR_A_DISTRIBUTION_CANDIDATE`。三个 `ra` 都在三个 wage 上保持 interior。旧 `.8/1.05/1.3` narrow map 的 2 interior/2 lower/4 ambiguous/1 upper 结构不再保持，因此 wage-domain 对 observed health labels 有实质影响，但 `1.3→13` 间连续 frontier 未观察。

Macro audit 使用 accepted corrected-2018 initialization-only 31-province receipt：GDP raw=`1548.4–99945.2` 亿元，`Y0_MU=1.5484e6–9.99452e7`；`Y0/N0=32.2231–151.0310` MU/NU；initial household composite `w0=13.8375–18.5197`；guarded `wjt0=1.3`（31/31），raw `wt0=7.7643–36.3915`。虽然同一 receipt 可并列这些对象，household wage 到 macro MU/NU 及 model-period 的映射仍未证明，结论=`DIMENSIONAL_RELATION_UNRESOLVED`。

不得直接修改 `wjt` guard。唯一建议但未执行的 Owner gate：`OWNER_REVIEW_JOINT_WJT_RA_MACRO_SCALE_RECALIBRATION`。它必须共同审查 `wjt→w`、return/asset bridge→`ra/rah`、GDP/per-capita GDP、investment/capital、population、productivity/labor normalization。

Runtime：HJB=9，KFE=9，retries=0；global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results 全部 0。Standalone contaminated-row KFE 不解决 multi-province finite-box upper-b leakage/MATLAB-style pinning blocker。
