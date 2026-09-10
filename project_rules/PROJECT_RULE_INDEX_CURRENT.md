# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`GOVINV_LABOR_REDESIGN_SPEC_ACCEPTED__CAPITAL_AND_LABOR_CORRECTION_PATHS_SEPARATED__OWNER_IDENTIFICATION_DECISIONS_REQUIRED_BEFORE_IMPLEMENTATION`。
当前 active Builder task：无。
最新接受候选：`afb1cffeba207368b78c8ac4b93958285312eb53`。
Reviewer acceptance：`docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新zero-science redesign specification已接受。资本侧：`GovInv0=Ktarget`仅保留为historical/source-faithful数值起点，不再解释为已识别公共资本；residual候选`GovInv0=max(Ktarget-Kt_supply_initial,0)`在会计/量纲上成立，但`Kt_supply_initial`的观察时点与At-grid→MU bridge尚未识别。GovInv initialization与controller redesign必须拆分，不从收敛表现反推初始化或controller参数。

劳动侧：source chain已明确区分population N、household efficiency labor、`Lt_mat(destination,origin)`与destination `firm_Lt_supply`；`Lt_seperate`只乘人口一次，但origin-column destination levels未归一化，因此`firm_Lt_supply/N0`巨大不能解释为真实就业超额。`N0`仅为population proxy；literal `Lt_seperate`还依赖内生`Ct/wjt`，所以仅凭地理距离和人均GDP无法唯一恢复其static weights。

候选labor reference中：L0=`N`仅为透明proxy；L1允许在Owner明确kernel后构造归一化migration-adjusted population reference；L2需要另行接受省级就业/劳动力数据，目前`DATA_NOT_AVAILABLE`；L3用migration shares配合独立全国劳动总量在结构上可行，但全国总量、origin weights与kernel均属Owner/data科学决策。

最低风险后续顺序已接受：冻结Y/K/N/alpha → Owner选择labor reference与全国总量 → 重算same-year Z和初始价格receipt → 如有必要且另行授权，仅做一次labeled household initialization observation → 识别private K supply → 决定GovInv initialization → 独立controller task → 新bounded trajectory。当前不得自动实施任何候选。

corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。KFE/HJB独立blockers继续存在。

当前没有active Builder task。下一步需要Owner对labor reference/national labor total、private-K observation/asset bridge以及GovInv初始化路线作实质性科学选择后，Reviewer才能发布implementation exact task。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
