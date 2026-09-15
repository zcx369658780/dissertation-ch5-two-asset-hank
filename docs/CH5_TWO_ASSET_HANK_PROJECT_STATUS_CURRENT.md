# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_ACTIVE`。

最新 accepted input-envelope candidate：`49ea4c12692c669701cdc7bcf8fd02267a068090`。
Reviewer acceptance：`docs/CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT_ACCEPTANCE.md`。
Current freeze：`docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Accepted practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. Finer-J and finer-I escalation routes remain closed; no maxit/tolerance/damping/relaxation/line-search changes are authorized.

Accepted first-turn HJB viability remains 25/31 converged and 6 legal nonconverged. Temporal mechanisms and coordinate-resolved selector/floor footprints are heterogeneous; successful controls also display substantial upper-b activity, so a common failure-specific boundary pathology is not supported.

The accepted 31-province input/outcome envelope audit further shows substantial failure-success overlap in consumed `ra` and household composite `w`: ranges and 2D bounding boxes overlap, convex hulls overlap, no single-ra or single-w threshold separates outcomes, and the fixed k=3 standardized graph is interleaved. Return and corrected upstream `wjt` guard states show no cross-sectional discriminating variation. Raw pre-guard return equals consumed `ra`; raw provincial `wjt` is unavailable in accepted compact evidence.

Therefore a simple provincial safe-price envelope or one-variable guard rule is not authorized. The active task now performs a bounded numerical local-basin interpolation diagnostic on four preregistered close failure/success pairs. It first proves all consumed household inputs other than `ra` and composite `w` are identical within each pair, then runs only `t=.25,.50,.75` line-segment probes. Expected HJB=12, KFE=0, scientific retries=0; endpoint reruns and adaptive bisection are forbidden.

The synthetic probes are numerical basin diagnostics only and must not be interpreted as feasible provincial equilibrium states or calibration targets. The corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning KFE blocker remains separate and unresolved.
