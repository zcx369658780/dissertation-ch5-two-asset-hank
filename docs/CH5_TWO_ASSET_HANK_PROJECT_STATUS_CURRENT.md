# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`KFE_D123_STATIC_IMPLEMENTATION_ACCEPTED__TINY_REAL_CELL_SELECTOR_PANEL_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoints

Accepted practical household grid remains `I=20,J=160,Nz=2,a=[0,100],b=[-2,20],h=1`, diagnostic only. Finer-I/J and geometry-only local-basin refinement remain closed. The accepted 31-province first-turn and local-basin evidence is unchanged.

The corrected-2018 five-turn KFE mechanism remains finite-box upper-`b` escape plus MATLAB-style dropped-equation/pinning algebra; the implied balancing source is algebraic, not an adopted household entry/exit process.

Owner adopted D1 state constraints + D2 consumed-total-drift conservative assembly + D3 regularized-cost-consistent KKT as a separate corrected diagnostic target. Production/source-faithful paths remain distinct.

## Newly accepted static implementation

Builder candidate `d8cc627d23172b17d3f4dafce0a5f41886c9815d` is accepted by `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_ACCEPTANCE_20260916.md`.

The implementation is isolated under `src/ch5_two_asset_hank/corrected_diagnostic/`; focused static tests pass; tested conservative generator arithmetic closes `Q @ 1` at machine scale; all 14 accepted legacy saved-control snapshots are hash-verified and correctly rejected before assembly because their persisted drifts violate artificial upper faces. This acceptance does not yet prove a corrected selector can generate admissible real-cell controls.

## Active gate

Current active Builder task: `tasks/CH5_MP4C_2018_KFE_D123_TINY_REAL_CELL_CORRECTED_SELECTOR_PANEL_20260916.md`.

The preregistered panel is exactly ten historical call725 cells: eight M143_FINAL asset-boundary corners plus MATLAB step52 row799 and step57 row379. Maximum runtime authority is one corrected selector evaluation per cell, <=10 selector evaluations total, with at most four face-active sets x three transfer-sign regimes x one scalar root each, <=120 root invocations total, no retry after adverse numerics.

HJB=0, KFE=0, MATLAB processes=0, outer/firm/wage-return recalculation=0, GE/annual/shock/IRF/Results=0. One target HJB step remains a separate future gate.
