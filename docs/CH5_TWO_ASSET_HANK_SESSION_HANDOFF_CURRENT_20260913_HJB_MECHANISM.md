# Chapter 5 当前交接 — 2026-09-13 HJB mechanism candidate

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态

Baseline：`79ced4f7a2f5e05722a77d23d75e37ee4eada058`。

Builder branch：`codex/ch5-mp4c-k1-hjb-mechanism-t1-t2-20260913`。

状态：`HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_CANDIDATE_PUBLISHED__INDEPENDENT_REVIEW_REQUIRED`。

Active Builder task：NONE。

Results eligibility=`FALSE`。

报告：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_REPORT.md`。

Compact evidence：`docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2/`。

External evidence：`D:\ProjectTemp\ch5-mp4c-k1-hjb-mechanism-t1-t2-evidence-20260913-002`。

External sealed-manifest file SHA-256：`82A979E15DF22A651348F8C4E35FFE5688513E635877269DA98DF0755D03AF77`。

## Candidate facts

- exact-input coverage=`62/62`；accepted input/output/operator identities全部闭合；
- instrumentation parity=`PASS`；
- HJB calls=`64`（2 parity + 62 replay），HJB direct solves=`4,689`；scientific retries=`0`；
- KFE/outer advancement/MATLAB/household steady-state/firm/K1B/K2/GE/IRF/Results=`0`；
- accepted convergence exact reproduction：turn1=`20/31`，turn2=`2/31`；
- turn1 converged的20省在turn2全部失败；turn2仅重庆、贵州收敛，而两省turn1均失败；
- candidate classification=`POLICY_CHATTERING_WITH_VALUE_UPDATE_OSCILLATION_AND_LATER_DERIVATIVE_FLOOR_AMPLIFICATION__NOT_PURE_TWO_CYCLE__NOT_MONOTONE_SLOW`；
- 40/40 failed calls 的policy switching早于首次derivative-floor hit，38/40的value-stat non-decrease也更早；
- return/wage guard state在turn2均不能分离成功失败；
- accepted operator已知signed off-diagonal/boundary row-sum特征在所有calls早期都出现，initial absolute solve residual全部同在约`1e-14`尺度；
- 不支持仅延长100-iteration ceiling。

这些是direct replay、cross-group association和temporal ordering；没有same-state mechanism intervention，不建立因果结论。分类是`POST_HOC_DESCRIPTIVE_FROM_PREREGISTERED_CONTINUOUS_METRICS__NOT_A_GATE`。

## Frozen boundaries

Annual science、transfer FOC/selector/boundary/KKT、derivative floor、HJB equation/pseudo-time/update law/solver/tolerance/100-iteration ceiling/grid、G2 return guard、wage guard、K1/C1/same-S/source-faithful labor全部未改。D1保持OFF。不得自动启动D1/D2/D3、return/wage relaxation、derivative/solver/ceiling调整、KFE、trajectory、K1B/K2、GE/IRF/Results。

KFE仍为`DIAGNOSTIC_ONLY`，finite-box upper-b leakage与MATLAB-style pinning是独立blocker；standalone KKT residual仍 unavailable。

## 唯一当前 gate

ChatGPT Reviewer 对candidate SHA、报告、compact evidence、external sealed manifest与call ledger做独立 ACCEPT/REJECT。

Candidate只建议在独立验收之后由Owner考虑一个gate：`OWNER_HJB_ITERATION_FIXED_POINT_MECHANISM_INTERVENTION_DESIGN_FREEZE`。该建议不发布successor task，也不授权任何科学变更或运行。
