# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`HJB_PROPAGATION_REPAIR_AND_25TURN_KL_ACCEPTED__GOVINV_DOMINATES_CAPITAL_OVERSHOOT__LABOR_PROXY_SCALE_MISMATCH_REQUIRES_SEPARATE_REDESIGN`。
当前 active Builder task：`tasks/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md`。
最新接受候选：`0616c72b1f7f82185e6216149d06f035a071511c`。
Reviewer acceptance：`docs/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新25-turn corrected-2018 rerun已接受。successor harness允许有限且结构可用的`converged=false` HJB返回继续KFE/aggregate/downstream turn，同时保留`HJB_NONCONVERGED_DIAGNOSTIC_ONLY`和false flag，最终source steady-state predicate仍要求31/31 household HJB convergence。25/25 turns、775/775 household/HJB/KFE/aggregate/firm均完成，无scientific retry或第二trajectory；turn23-25 HJB为31/31 converged，但775/775 KFE仍为`DIAGNOSTIC_ONLY`，两类科学blocker继续独立存在。

K reconciliation已定量：turn20-25 pooled `firm_K_total/Ktarget` min/median/max=`1.3422659595802506/2.359983542526/2.866669200187509`；late-window median `private_K/Ktarget=0.00291675418808339`，median `GovInv/Ktarget=2.3579476910000015`。29/31省late-window mean严重高于target，2/31中度偏高。overshoot明确由GovInv主导而非household private K；source-faithful `GovInv0=Ktarget`在positive private supply加入后即机械性超过target，且当前controller在该25-turn prefix中没有消化，反而使median GovInv/target进一步上升。

Labor reconciliation也已定量：turn20-25 pooled destination `firm_Lt_supply/N0` min/median/max=`4.589147349109114/14.2307874070677/153.05180501585224`，31/31省late-window mean均严重高于population proxy。该结果不能解释为真实workplace employment超额，因为`N0`只是假设性population/labor initialization proxy；它证明household labor、population proxy、migration allocation和destination firm labor的量纲/参考对象尚未闭合。

当前active task因此改为zero-science redesign specification：分别审计GovInv初始化/控制器与labor object/normalization，比较`GovInv0=Ktarget`、residual-to-target、share/public-capital等候选；恢复`N`、household labor、`Lt_mat`、destination `Lt_supply`的完整维度链；分析Owner提出的“基于地理距离和人均GDP差距构造migration-adjusted labor reference”是否可作为可解释的校准/reference contract。不得运行HJB/KFE/firm/outer turn/steady state，也不得选择新GovInv、Lt、beta_a、bounds、damping或其他production参数。

此前corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。上一错误尺度100-turn candidate仍为rejected historical evidence。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
