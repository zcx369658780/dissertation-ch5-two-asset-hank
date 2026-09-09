# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-10。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成：旧call725失败复现、rah=.07敏感性、KFE source/escape归因、b域压力测试、原始数据/插值审计、时间合同/Zt legacy审计、V2 pre-model实现、官方/付费数据审计、PIM资本链闭合、2018修订GDP闭合、canonical workbook构建，以及corrected-2018一轮/两轮/三轮传播和five-turn bounded prefix。Results=FALSE。

## 2018数据与输入合同
- rolling 10-year PLM；2018 window=2009–2018；same-year levels/Zt；
- 安徽GDP=`34010.9`亿元，POP=`6076`万人，PIM K2018=`1357314108.2013683`万元，alpha=`.772866243094144`；
- canonical workbook SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`；
- 资本为model-derived PIM object；2011投资定义断点保留。

## corrected-2018 propagation 已接受
turn1–3确认：当期firm raw return位于LOWER区，used `ra=.02`；turn3首次观测到 corrected `.02` 通过native capital-allocation timing进入household composite `rah`，安徽turn3 `rah=.0184420457528848`。该证据只证明传播，不证明稳态。

## five-turn bounded prefix
accepted candidate=`9864129dd2e97bae97238ab9cc588aea48682d29`。5 turns /155 province updates全部执行，scientific retries=0；turn4首次 native adaptation gate开启，turn4–5均执行31省Zt adjustment与`LOW_RA_DECREASE_0P9` GovInv action。

five-turn验收为：`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER_ACCEPTED__KFE_SOURCE_FREE_STATIONARITY_AND_UPPER_B_LEAKAGE_BLOCK_PREFIX_INTERPRETATION`。turn4/5 returned densities全31省均`DIAGNOSTIC_ONLY`；negative density mass只有机器精度量级，实质blocker为source-free stationarity residual和upper-b outward leakage。全国turn4/5每轮620 positive upper-b leak cells，max leak rate约2.2393；lower-b/lower-a/upper-a leakage为0。五轮C/L/A/B只可作为诊断值。

## 当前 active task
`tasks/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION.md`。
零科学调用地使用保存的operator/density/drift，做全国turn4/5 mass-balance、pin-row residual、boundary escape、implicit-source attribution，并与accepted call725 `rah=.07`机制比较。核心判定：是否确认相同的finite-box upper-b leakage + contaminated-row/row-replacement pinning algebra。

## 当前禁止
不允许turn6+、new KFE solve、steady state、GE、annual、MATLAB、IRF、Results；不允许production boundary/grid/source/pinning repair。D1–D3仍为deferred redesign proposals。

## 后续路线
当前KFE attribution验收 → 若same mechanism confirmed，则先进行Owner科学决策：是否进入finite-box boundary/KFE closure redesign specification；若partial/distinct，先定位additional residual source；若saved artifacts不足，则停在evidence gap。只有边界/KFE有效性问题得到新的明确科学裁决和任务授权后，才考虑重新进入corrected 2018科学运行。随后才可能进入有限省份、年度覆盖、MP5/MP6 dynamics。

2022–2023六个非正资本/无效Zt继续作为独立未来年份数据问题。生产网格当前仍冻结I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]。