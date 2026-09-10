# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`UNIT_NORMALIZED_INITIALIZATION_PROBE_ACCEPTED__BROAD_FIRM_PRICE_BOUNDARY_HITS_PERSIST_AFTER_DATA_AND_MACRO_UNIT_CORRECTION__NEXT_DIAGNOSIS_MUST_TARGET_PRICE_NORMALIZATION_AND_BRIDGE_SEMANTICS`。
当前 active Builder task：`tasks/CH5_MP4C_FIRM_PRICE_NORMALIZATION_AND_HOUSEHOLD_MACRO_BRIDGE_FORENSIC.md`。
最新接受候选：`ff2a32e6c6eb799931b741c9a8557afdaa5c8bfa`。
Reviewer acceptance：`docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新初始化-only probe已经接受：使用正确2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、统一宏观单位`MU=10万元`与`NU=100 persons`后，protected-source firm初始化仍广泛撞价格边界。raw `ra`对`[.02,.09]`为below/inside/above=`0/1/30`；raw `wjt`对`[.8,1.3]`为`0/0/31`；31/31至少命中一个边界。安徽raw/used `ra0=.32587797015041736/.09`，raw/used `wjt0=13.487571992789512/1.3`，source-lagged `rah0=.08895777765800762`，静态wage composite `w0=18.29792118969518`。该证据不授权扩大bounds或从收敛表现反推household asset bridge。

protected `HANK_firm.m`在zero-change初始化下给出`mt0=.92`而不是早期redesign prose简化的`.9`；已按源码留痕，不修改production source。

当前新task继续保持zero-household/zero-steady-state，仅做firm price normalization与household↔macro bridge静态forensic。重点把raw wage分解为`mt*(1-alpha)*Y/L`等价形式，把raw `ra`分解为MPK、firm depreciation和profit/tax成分；做money/population单位缩放不变性分析；恢复HJB中`a/b/c/w/Tt/AtTax`的绝对/相对单位线索；明确`At_grid -> At*N -> Kt_supply -> Kt_supply+GovInv`桥接方程及未知货币conversion；核查legacy price bounds provenance。不得运行HJB/KFE、firm runtime、allocation、outer turn、steady state、GE/annual/IRF/Results，不得修改bounds或选择asset bridge。

此前的raw-NBS重估、mixed-year数据审计、steady-state redesign spec和five-turn KFE attribution继续作为有效历史证据；当前优先分离“wage单位不匹配”与“ra真实Y/K水平效应”，再决定下一步production contract。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新的科学执行必须先发布exact task。以后每次发布exact task，同一回复自动附Codex启动prompt。