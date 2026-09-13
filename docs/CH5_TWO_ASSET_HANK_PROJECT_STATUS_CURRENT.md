# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTED__OWNER_FIXED_POINT_INTERVENTION_DESIGN_FREEZE_REQUIRED`。

最新 accepted HJB mechanism candidate：`c6d89327933edef2b942f10f462b58cfa6b52954`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTANCE.md`。
Owner/Reviewer HJB route freeze：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_REVIEW_FREEZE_CURRENT.md`。
当前 active Builder task：NONE。
Results eligibility=`FALSE`。

Accepted exact-input diagnostic：turn1/turn2 accepted G2 control、D1 OFF，exact-input coverage=`62/62`；instrumentation parity=`PASS`；`64 HJB = 2 parity + 62 replay`；scientific retries=`0`；KFE/outer trajectory/MATLAB/firm/K1B/K2/GE/IRF/Results=`0`；`62/62` replay outputs 与 `62/62` final operators exact-equal accepted artifacts；重现 turn1 `20/31`、turn2 `2/31`。

Accepted descriptive classification：`POLICY_CHATTERING_WITH_VALUE_UPDATE_OSCILLATION_AND_LATER_DERIVATIVE_FLOOR_AMPLIFICATION__NOT_PURE_TWO_CYCLE__NOT_MONOTONE_SLOW`。这是基于预注册连续指标的 post-hoc descriptive classification，不是因果结论。

关键时序证据：40/40 failed calls 的 policy switching 早于首次 derivative-floor hit；38/40 的 value-stat non-decrease 也更早；20/20 turn1-converged provinces 在 turn2 失败，且 turn2 policy switching 均从 iteration 2 出现，而 derivative-floor 首次命中在 iteration 3/4/5。初始 linear-solve absolute residual 在全部62 calls约 `4.39e-14–9.25e-14`，不支持 direct solve 作为起始故障。accepted operator 的 signed off-diagonal / boundary row-sum特征在成功失败calls均出现，不能单独解释分裂。

Return/wage guard state不能分离turn2成功与失败；wage saturation在turn1同时伴随成功和失败。Derivative floor保留为后续 amplifier/co-traveller，而非当前共同 initiating event。现有证据不支持仅延长100-iteration ceiling。

当前继续冻结：annual continuous time；`rho=.05`、`rb=.02`、borrowing gap `.07`、`delta=.10`、`Q_z=1/3`、`chi0=.1`、`chi1=2`；transfer FOC/selector/boundary；derivative floor；HJB equation/pseudo-time/update law/solver/tolerance/100-iteration ceiling/grid；G2 return guard `[-.10,.35]`；wage safeguard `[.8,1.3]`；K1A fixed theta、`beta_distance=2`、`beta_return=0`、same-S、source-faithful labor、C1 unchanged；K1B/K2 OFF。

KFE仍=`DIAGNOSTIC_ONLY`；finite-box upper-b leakage与MATLAB-style pinning为独立blocker。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。长期仍要求 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

唯一 next gate：`OWNER_HJB_ITERATION_FIXED_POINT_MECHANISM_INTERVENTION_DESIGN_FREEZE`。在Owner/Reviewer冻结一个 isolated same-input HJB-map intervention前，不发布 successor runtime task。