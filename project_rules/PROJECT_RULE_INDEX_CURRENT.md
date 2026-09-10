# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`RAW_NBS_2018_REBUILD_ACCEPTED_PARTIAL__SAME_YEAR_GDP_POP_AND_LAGGED_FLOW_CAPITAL_REBUILT__SOURCE_ROUTE_DIFFERENCE_REMAINS`。
当前 active Builder task：无。
最新接受候选：`3bd6343011f17d1b2273386732f06e6da6bf84e9`。
Reviewer acceptance：`docs/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新raw-NBS rebuild确认：GDP 1992–2022、人口2000–2022完整；固定资本形成1996–2017完整，折旧1992–2017完整；投资与折旧在2018均无31省观测，因此不存在四源完全同年2018面板，未填补或伪造。根据冻结的lagged-flow PIM定义，完整2017流量仍可构造K2018。

Track A继续只作为primary comparable PIM rebuild：`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`，但raw gross fixed capital formation与当前accepted canonical investment route并非同一数据概念/来源，不能自动替换production capital authority。Track B使用观察折旧进行会计诊断，不是production authority。

重新估计2009–2018 pooled alpha=`0.7380939146868483`，SE=`0.03825774803543075`，R²=`0.6924937537873637`，N=310。安徽raw-NBS 2018 GDP=`34010.9`亿元、POP=`6076`万人；Track-A K2018=`70182.43335888097`亿元；Track-B K2018=`84616.8`亿元；Track-A Z2018=`0.0018759632501672073`。安徽相对legacy mixed-year object差异material，但不是唯一或最大异常；Track-A capital相对当前canonical capital约低48.3%，该差异需作为source/concept-route scientific choice处理。

此前MATLAB 2018 mixed-year audit和five-turn KFE attribution均继续作为有效历史证据；Owner当前要求先讨论生产校准应采用哪种投资/资本数据定义，不自动进入HANK/KFE production redesign，也不运行新稳态。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新的科学执行必须先发布exact task。以后每次发布exact task，同一回复自动附Codex启动prompt。