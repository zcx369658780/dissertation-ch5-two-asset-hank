# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT_20260913_HJB_MECHANISM.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_FREEZE_CURRENT.md`
8. active exact task：`tasks/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC.md`
9. accepted mechanism diagnostic report及compact evidence。

当前状态：`HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC.md`。
最新 accepted HJB mechanism candidate：`c6d89327933edef2b942f10f462b58cfa6b52954`。
Results eligibility=`FALSE`。

Accepted mechanism diagnostic：62/62 exact-input replay；instrumentation parity PASS；turn1 `20/31`、turn2 `2/31`；policy chattering与non-monotone value-update oscillation先于later derivative-floor amplification；现有证据不支持pure two-cycle、monotone-slow或仅延长100-iteration ceiling。

Owner已冻结第一isolated same-input intervention：`omega=0.5` value-update relaxation。保持accepted map到`V_solve`完全不变，之后仅令`V_next=0.5*V_old+0.5*V_solve`。accepted baseline为`omega=1`。

Treatment convergence必须使用raw fixed-point gap `||V_solve-V_old||_inf < 1e-7`，不能用机械缩小后的relaxed update；100-iteration ceiling保持不变。

Active task不重跑完整baseline；复用accepted 62个turn1/turn2 G2-control、D1-OFF exact inputs。先做2个`omega=1` exact-equivalence HJB calls（一个accepted converged、一个accepted failed），通过后最多62个`omega=0.5` treatment calls。总HJB budget<=64；scientific retry=0；KFE/outer trajectory/MATLAB/firm/K1B/K2/GE/IRF/Results均为0。

不得观察结果后调整`omega`；不授权damping ladder、adaptive damping、solver替换、tolerance/grid/price guard/derivative floor/FOC/selector/boundary/KKT/economic parameter变化。

KFE继续`DIAGNOSTIC_ONLY`；finite-box upper-b leakage / MATLAB-style pinning独立未解决。Standalone KKT residual unavailable。长期目标仍为`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

Builder完成active task后，唯一next gate为ChatGPT Reviewer独立ACCEPT/REJECT。GitHub live main是唯一repository authority；聊天不能替代exact task。
