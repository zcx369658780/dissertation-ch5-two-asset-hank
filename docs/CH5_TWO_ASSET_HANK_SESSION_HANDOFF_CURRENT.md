# Chapter 5 当前交接 — household grid precision re-execution candidate

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ASSET_GRID_PRECISION_REEXECUTION_CANDIDATE_AWAITING_REVIEW`。

Baseline=`03f30ada29ef7cea8dd0ab8f27b090df607c0909`；branch=`codex/ch5-mp4c-k1-grid-repair-reexecution-20260915`；worktree=`D:\ProjectTemp\ch5-mp4c-k1-grid-repair-reexecution-20260915-001`。

R0 only changed task-owned precision runner/finalizer/test。Grid-generic tests cover `J=20/40/80/160` and `I=20/40/80`，J20 receipt regression unchanged，raw signed density 未 clip/smooth/renormalize；`17 passed`、`py_compile` PASS；受保护 solver/source diff=0；R0 science calls=0。

P1 fresh ladder：复用 accepted I20/J20，不 rerun；新运行 I20/J40、J80、J160。HJB=`3/3` legal/converged；KFE=`3/3` numeric-returned/persisted/valid；scientific retries=0。Scientific arrays 在 postprocessing 前落盘。

关键 final refinement：J80→J160 `ΔAt=+0.6907895741`、`ΔBt=+0.7879809617`、modal `a 92.40506329→94.33962264`、a-CDF distance=`0.0146223444`、b-CDF distance=`0.0358173164`。相较前两次 a-CDF `0.01261160,0.01759636`，未显示 stabilization trend。

Terminal=`ILLIQUID_GRID_PRECISION_NOT_STABILIZED`；P2 trigger=false；P2 HJB/KFE=`0/0`。At/modal a/a marginal/expanded-domain final level 未稳定；minimum defensible I/J 未建立。旧域→扩域巨大 At jump 主要为 domain response，但 finer-J component 仍未闭合。

固定 I20 的 finer-J 点上 modal b 均为 `2.63157895`，bmax mass 最大 `0.0009774012`；tested P1 points 上 nonbinding，I-grid stability 未检查。

Compact evidence=`docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution/`；external P1 manifest=`C77D85511AAD5C7B50E99144A9E84EB9E232EE77B3D67AF834C109608AECB495`。

唯一 next gate=`FINER_PRECISION_ESCALATION`。本 candidate 不授权 J320/J640、P2、full cross-state grid、recalibration、merge main、successor task 或 Results。
