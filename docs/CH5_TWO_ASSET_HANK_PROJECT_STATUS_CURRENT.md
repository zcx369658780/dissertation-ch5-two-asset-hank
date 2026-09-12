# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_G1_VS_G2_INSTRUMENTED_HA_HJB_DIAGNOSTIC_ACCEPTED__OWNER_HA_NUMERICAL_CONTRACT_DECISION_REQUIRED`。

最新 accepted instrumented candidate：`5d28382f5914d161817642bab9f3c6d73b41c935`。
Reviewer acceptance：`docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`。
当前 active Builder task：NONE。
Results eligibility=`FALSE`。

## 已接受：turn2 common-state mechanism localization
Instrumentation ON/OFF scientific outputs exact-parity，G1/G2 均完成5 turns。Turn1 完全一致；turn2 的31省均从同一 completed turn1 scientific state 进入。

Turn2 iteration1 中，directional/value derivatives、derivative-floor activations、pre-selector transfer candidates、liquid/transfer policy labels 仍完全一致。最先产生差异的是 frozen G1/G2 return guard 导致的 `effective_illiquid_return` 与 `mu_a` / illiquid-drift assembly；随后 operator、`V_new`、HJB statistic 立即分叉。

Iteration2 开始 value derivatives 与 transfer candidates 全面分叉；transfer labels 同期分叉，liquid labels稍后分叉；derivative-floor activation differences 到 iteration3/4 才出现。因此 derivative floor、selector、boundary law 和 wage input 均不是 initiating mechanism。

湖北 turn2 interior checkpoint 进一步证明：后期 huge transfer/cost 并非 selector 将温和 candidate 放大，而是 raw pre-selector `d_bb` candidate 已经在 evolving value-derivative / transfer-FOC feedback 中爆炸，随后 B branch 选中该 extreme candidate。

## 当前 scientific interpretation
当前最小 scientific blocker 已定位到 HA transfer/adjustment-cost candidate admissibility contract：在较高但仍 frozen annual HJB return exposure 下，现行 liquid-value-derivative driven transfer FOC 是否允许极大的有限 transfer candidate，以及 quadratic adjustment cost 对该 candidate 的放大是否需要经济上可解释的 admissibility/regularization contract。

这不是 Builder 调参问题。现有 evidence 不授权自动改 `chi0/chi1`、derivative floor、return/wage guard、boundary law、grid、tolerance 或 solver。Owner 必须先冻结下一版 HA numerical/economic contract。

Turns3-5 继续只属于 `PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL`。

## Price guards / KFE / Results
`ra/rah` 与 `wjt/wage` hit monitoring继续强制执行；长期目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。当前不得 longer G2、G3/G4、wage relaxation、K1B/K2。

KFE仍为`DIAGNOSTIC_ONLY`，finite-box upper-b leakage与MATLAB-style pinning独立未解决。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

Results eligibility=`FALSE`。
