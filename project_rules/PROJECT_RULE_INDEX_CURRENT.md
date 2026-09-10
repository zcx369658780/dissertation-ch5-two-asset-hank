# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`STEADY_STATE_REDESIGN_SPEC_ACCEPTED_PARTIAL__UNIT_AND_INITIALIZATION_PROBE_AUTHORIZED__PRODUCTION_RUNTIME_STILL_BLOCKED`。
当前 active Builder task：`tasks/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_AND_PRICE_RECEIPT.md`。
最新接受候选：`abfeec3bd7443cd5a95ef3a62aedae16be81b702`。
Reviewer acceptance：`docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

已接受的设计结论：legacy GDP亿元与资本万元被同样`×1000`导致资本相对共同货币单位放大`10,000`倍；household→macro productive-capital桥位于`At*N`，但当前隐含bridge系数1没有经济单位依据。Owner/Reviewer同意采用统一宏观单位作为下一bounded probe：`MU=10万元`、`NU=100 persons`，GDP亿元`×1000`、capital亿元`×1000`（或万元`÷10`）、POP万人`×100`。该共同单位合同已获准用于probe，但household asset-grid货币归一化仍未正式冻结。

下一probe使用Owner提供raw-NBS GFCF Track-A PIM作为诊断资本路线，`delta_pim=.096`；firm内现有`.025`折旧暂保持独立角色并必须显式记录，不静默统一。raw-NBS Track A在本probe中的选择不自动升级为Results authority。

alpha successor contract已冻结：保存`alpha_raw`，按Owner范围`[.2,.8]`取`alpha_used`并保留clip flag/reason；当前`alpha_raw=alpha_used=0.7380939146868483`。原active `reg_method=0`源码没有实际alpha clipping，旧`.3/.8`只是注释逻辑。

初始化设计已接受：不再把legacy `.09/.09/.6/20`视为合理数据初值；先绑定2018 Y/K/N、alpha与same-year Z，再按现有firm方程生成raw/clipped `ra0/wjt0`。下一task只执行initialization-only deterministic probe，不调用household HJB/KFE或steady-state loop。`rah`时序下一probe保持source-lagged baseline；after-firm timing仍为未来单独candidate。GovInv不新增damping，`w/rah` lambda与hysteresis阈值仍未冻结。

原single-loop思路继续保留：Stage A stabilization、Stage B near-steady online calibration、Stage C calibration freeze/final confirmation；不采用完整nested steady-state/calibration双循环，也不换Newton/Broyden/fsolve/Brent/Anderson等solver。

当前task严格禁止household HJB/KFE、outer turn、steady state、GE/annual/IRF/Results；只允许31省数据一致firm-side初始化方程及无需household solve的静态聚合/单位诊断。household asset bridge系数1仅允许作为`SOURCE_FAITHFUL_BASELINE_ONLY`诊断，不得从收敛表现反推新bridge。

此前MATLAB mixed-year数据审计、raw-NBS重估、five-turn KFE attribution继续作为有效历史证据；当前优先建立正确数据、单位和初始化价格尺度，再决定是否进入first bounded outer-turn validation。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新的科学执行必须先发布exact task。以后每次发布exact task，同一回复自动附Codex启动prompt。