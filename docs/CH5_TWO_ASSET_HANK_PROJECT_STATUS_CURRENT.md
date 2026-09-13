# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_ACCEPTED__JOINT_RECALIBRATION_OWNER_REVIEW_REQUIRED`。

Accepted candidate：`41993260d87387235a2e58cc9a93a8aa06b98515`。
Reviewer acceptance：`docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_ACCEPTANCE.md`。
当前 active Builder task：NONE。Results eligibility=`FALSE`。

真实 household composite-wage standalone grid：`rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。HJB 9/9 legal/converged；KFE 9/9；9/9 的 illiquid-asset `a` distribution 均为 `INTERIOR_A_DISTRIBUTION_CANDIDATE`。三个 `ra` 均在三个真实 composite-wage 点上保持 interior。旧 `.8/1.05/1.3` narrow map 的分类结构不再保持，说明 observed household geometry 对 wage domain 有实质依赖；`1.3→13` 区间未观察，不能推断连续 frontier。

重要新增 caveat：虽然 `a` distribution 全部 interior，但 9/9 的 liquid-asset `b` marginal mode 都在 `bmax=5`，且上界质量为实质值。因此当前不能把这些点升级为 fully healthy/admissible household steady states；后续 joint recalibration 必须把 liquid-asset domain adequacy / `bmax` 纳入审查。Owner 已明确 `I/J` 属于计算精度参数，不应作为第一优先调参项；未来若需 grid recalibration，优先审查 `bmin/bmax`、`amin/amax` 等 domain bounds，`I/J` 默认保持原 MATLAB 级别，除非独立 precision sensitivity 证明需要调整。

Macro audit：GDP raw=`1548.4–99945.2` 亿元，`Y0_MU=1.5484e6–9.99452e7`；`Y0/N0=32.2231–151.0310`；initial household composite `w0=13.8375–18.5197`；raw firm `wt0=7.7643–36.3915`；guarded `wjt0=1.3`（31/31）。虽然 source chain 解释了 `wjt→composite w` 的 nonlinear aggregation，但 household wage 与 macro MU/NU / monetary unit / model period 的统一量纲映射仍未证明。结论：`DIMENSIONAL_RELATION_UNRESOLVED`。

不得直接修改 `wjt` guard，也不得通过放大 `I/J`、修改 HJB/KFE 算法或 clipping 来制造可行稳态。唯一下一 Owner gate：`OWNER_REVIEW_JOINT_WJT_RA_MACRO_SCALE_RECALIBRATION`。该 gate 必须共同审查 `wjt→w`、return/asset bridge→`ra/rah`、GDP/per-capita GDP、investment/capital、population、productivity/labor normalization，以及 asset-grid domain bounds，尤其 `bmax`。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning blocker。Results eligibility=`FALSE`。
