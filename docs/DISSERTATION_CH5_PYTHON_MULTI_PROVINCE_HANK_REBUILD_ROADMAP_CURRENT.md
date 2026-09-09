# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-10。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已经完成：旧call725失败复现、rah=.07敏感性、KFE source/escape归因、b域压力测试、数据/插值审计、rolling-10y/same-year-Zt时间合同、2018官方/付费数据闭合、PIM资本链、canonical workbook、corrected-2018 turn1–5受控前缀，以及five-turn KFE全国leakage attribution。Results=`FALSE`。

## 2018数据层
数据层已闭合。canonical workbook SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。安徽2018 final-use：GDP `34010.9`亿元；POP `6076`万人；PIM `K2018=1357314108.2013683`万元；alpha=`.772866243094144`；PLM vintage19/window2009–2018；same-year Zt约`.0006934644495858679`。

## corrected-2018已接受轨迹
- turn1–3完整执行并接受；turn3首次直接观察corrected firm `ra=.02`进入下一household composite return。
- five-turn候选`9864129dd2e97bae97238ab9cc588aea48682d29`完整执行5 turns/155 updates；turn4首次native adaptation gate开启，turn4/5执行31省Zt adjustment与`LOW_RA_DECREASE_0P9` GovInv action。
- 但turn4/5 returned densities 31/31均`DIAGNOSTIC_ONLY`。material blocker是source-free stationarity residual + upper-b outward leakage；负density mass仅机器精度。

## 全国KFE归因已闭合
最新接受候选`ea4ac44fe3c65c506ff7fdfbdbf29d96078cc5c6`在zero-science-call下确认：

`SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`。

机制：upper-b finite-box assembler省略outside-grid offdiagonal但保留对应diagonal rate；post-loop KFE转置后替换`k=295`方程并设置`rhs[k]=.007`；被丢弃source-free equation在代数上等价于平衡upper-b escape的source。turn4/5 62/62对象residual几乎全部在pin row；off-pin residual仅浮点量级；mass-balance与implicit-source balance均在约`10^-16`闭合。该source equivalence不是经济entry/exit机制。

HJB-loop operator negative offdiagonals继续是独立问题，不能被post-loop KFE operator的非负offdiagonal状态掩盖。

## 当前路线节点
当前没有active Builder task。不得继续trajectory、turn6+、steady state或Results。

下一步是Owner scientific decision：选择finite-box/KFE closure redesign方向，再发布新的exact design/implementation task。需要明确区分：
- boundary state-constraint / no-outflow closure；
- generator total-drift consistency；
- pinning/source-free KFE formulation；
- grid/domain adequacy；
- HJB-loop operator admissibility。

D1–D3仍是此前deferred redesign proposals，不因本次机制确认自动升级为production contract。

## 后续大路线
Owner boundary/KFE closure裁决 → bounded design specification / static proof → 受控单household或极小前缀验证 → source-free KFE validity → corrected-2018短前缀 → bounded steady-state prefix → 有限省份/年份 → MP5/MP6 dynamics。任何一步均需自己的GitHub exact task和接受门。

2022–2023六个非正资本/无效Zt仍是独立未来年份数据质量问题。生产网格目前仍冻结I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]，除非Owner后续明确改变。