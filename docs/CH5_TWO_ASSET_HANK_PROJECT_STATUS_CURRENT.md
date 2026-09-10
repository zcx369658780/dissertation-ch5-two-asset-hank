# Chapter 5 两资产 HANK 当前状态
更新：2026-09-10。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`RAW_NBS_2018_REBUILD_ACCEPTED_PARTIAL__SAME_YEAR_GDP_POP_AND_LAGGED_FLOW_CAPITAL_REBUILT__SOURCE_ROUTE_DIFFERENCE_REMAINS`。
最新接受候选：`3bd6343011f17d1b2273386732f06e6da6bf84e9`。
Reviewer acceptance：`docs/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_ACCEPTANCE.md`。
当前 active Builder task：无。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## raw-NBS 2018 rebuild
Owner提供国家统计局原始XLS：GDP、固定资本形成、固定资产折旧、年末常住人口。最新静态/校准任务未运行HANK/HJB/KFE/firm/outer-loop模型。

接受事实：
- GDP：1992–2022年31/31完整；人口：2000–2022年31/31完整；固定资本形成：1996–2017年31/31完整；折旧：1992–2017年31/31完整。
- 2018固定资本形成和折旧均无31省观测，因此四源完全同年2018面板不存在；未填补或伪造。
- 冻结lagged-flow PIM仍可由2017流量构造K2018：`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`。
- Track A仅作为raw-NBS gross fixed capital formation下的primary comparable PIM rebuild；不能自动替代当前canonical investment-route capital authority。
- Track B使用观察折旧：`Kt=K(t-1)+I(t-1)-D(t-1)`，只作为会计诊断。
- 2009–2018 pooled OLS重新估计`alpha=0.7380939146868483`，SE=`0.03825774803543075`，R²=`0.6924937537873637`，N=310；legacy alpha=`0.772866243094144`仅作比较。
- same-year 2018 Zt使用2018 GDP/POP和各自capital track计算，不再混入2020 level。

安徽：
- raw-NBS GDP2018=`34010.9`亿元；POP2018=`6076`万人；
- Track-A K2018=`70182.43335888097`亿元；Track-B K2018=`84616.8`亿元；
- Track-A Z2018=`0.0018759632501672073`；Track-B Z2018=`0.0016340686739896946`；
- 相对legacy mixed-year MATLAB：GDP约`+213.04%`、Track-A capital约`+207.65%`、Track-A Z约`+192.41%`，POP约`-0.90%`；安徽material但不是唯一或最大异常。
- 相对当前canonical PIM capital，安徽Track-A约低`48.29%`。该差异主要是raw gross fixed capital formation与canonical investment route的source/concept差异，尚未裁决production authority。

## 历史科学证据继续有效
此前原MATLAB“2018”mixed-year audit、corrected-2018 turn1–5诊断与five-turn KFE attribution继续有效，但目前不再把boundary/KFE redesign作为自动下一步。Owner当前优先讨论投资/资本数据定义及production calibration authority。

## 当前科学边界
当前没有active Builder task。不得自动运行新HANK/HJB/KFE/firm/outer-loop/steady-state/GE/annual/IRF/Results，也不得自动覆盖当前canonical capital series。

下一步由Owner与Reviewer比较：legacy MATLAB mixed-year input、current canonical investment-route PIM、raw-NBS GFCF Track A、observed-depreciation Track B之间的经济定义与量级，再决定production capital/data contract。
