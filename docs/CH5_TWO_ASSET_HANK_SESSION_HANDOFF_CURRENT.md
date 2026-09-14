# Chapter 5 当前交接 — household asset-grid precision candidate awaiting review

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC_CANDIDATE_AWAITING_REVIEW`。

最新 accepted Stage A candidate：`32763fac5a7c4a04dc8278a9069443f35c7c7e3c`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_ACCEPTANCE.md`。
Precision freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Accepted Stage A facts：temporary diagnostic household bridge `h=1`；`a=[0,100]`、`b=[-2,20]`、`I=J=20`；`rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。9/9 HJB legal/converged，9/9 KFE-valid。Liquid marginal 9/9 modal `b=2.6315789473684212`，0/9 modal `b=20`，`bmax` mass至多约 `6.13e-08`；旧 `bmax=5` pile-up 已清除，Stage B `bmax=50` 未触发。

Illiquid result 尚未获得 precision authority：`At≈84.02–88.86`、modal `a` 多在 `89.47`、`amax` bin mass约 `9.3%–17.4%`，`J=20` 的 `da≈5.26316`。旧域 `At≈7.14–7.33` 到扩域 `At≈84–89` 是重大 domain/discretization response，不得解释为 calibration improvement。

Candidate terminal：`P1_KFE_EVIDENCE_UNAVAILABLE__NO_SCIENTIFIC_RETRY_AUTHORIZED`。Fresh baseline `2f1c12fadbef438f8b3895f309730b2aca8fb45e`；branch `codex/ch5-mp4c-k1-household-asset-grid-precision-20260915`；worktree `D:\ProjectTemp\ch5-mp4c-k1-household-asset-grid-precision-20260915-001`。

P1 exact ladder 已运行：`I=20,J={40,80,160}` 的 HJB 3/3 legal/converged，iterations=`11,10,16`。三次 KFE numeric solve 均返回进入 accepted wrapper，但随后被其 frozen `a.size==20` postprocessor 以 `ValueError: expected the frozen 20-bin illiquid marginal` 拒绝；没有 persisted finer-grid density、aggregate 或 marginal receipt。禁止 scientific retry，故 P1 stability unresolved、P2 trigger=false、P2 HJB/KFE=0。

Runtime ledger：accepted reference HJB/KFE=0；P1 HJB started/completed=3/3；KFE started=3、完整 persisted receipt=0；P2 HJB/KFE=0；scientific/engineering retries=0；global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0。

Owner 已授权 ChatGPT Reviewer 对后续相似的小范围、本地数值校准/调试直接做 bounded、预注册决策并发布 exact task；结构性模型、accepted equations/guards、主要经济校准、因果解释或 Results eligibility 变更仍需 Owner authority。

`At/modal a/a marginal/amax mass` precision、finer-grid `Bt/b marginal`、`bmax=20` nonbinding 与 minimum defensible grid 均未建立。Compact evidence：`docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_sensitivity/`。唯一 next gate：`REVIEWER_ROUTE_REPAIR_DECISION`；Reviewer 决定是否通过 fresh exact task 授权 grid-generic receipt repair 与同一 frozen P1 ladder 重跑。Builder 不修复、不重跑、不 merge、不发布 successor task。Results eligibility=`FALSE`。
