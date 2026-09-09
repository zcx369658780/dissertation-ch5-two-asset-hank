# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成原call725失败复现、rah=.07单户敏感性、KFE source/escape归因、b域压力测试、原始数据/插值审计、年度时间合同/Zt legacy审计、V2 pre-model静态实现、官方2018身份审计及付费数据缺口审计。Results=FALSE。

## 已冻结并实现的时间合同
`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；PLM estimator保持rolling 10-year；2018=2009–2018；Zt公式保持并使用同年水平量。生产网格继续I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]。

## 已闭合数据
- 2018安徽常住人口已闭合为`6076`万人：2023《中国人口和就业统计年鉴》表1-1明确2011–2019依据2020人口普查修订。
- 2018安徽GDP仍未闭合：provisional `34010.91`亿元与2018初步官方`30006.82`亿元之间缺少第四次经济普查后的修订精确表值。

## Owner资本方法裁决
资本存量继续采用现有永续盘存法（PIM），作为模型构造量而非官方发布量。冻结：
- `K0=I0/0.1`；
- `Kt=(1-.096)K(t-1)+I(t-1)`；
- depreciation=.096；
- 初始化规则保持；
- K2018使用I2000..I2017。

因此“不存在官方资本存量”不再是项目blocker。当前省级投资链作为模型校准来源使用，并显式保留CNKI整理来源和2011固定资产投资统计范围断点的限制；不得为了获得官方外观而重新拼接、插值或改PIM参数。

## 当前 active task
`tasks/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE.md`

零模型调用。任务静态重建安徽K2018，核对是否精确复现现有workbook-derived CAP=`1357314108.2013683`，并生成版本化PIM capital-input receipt、source/provenance和2011口径限制。`sj479`城市投资只能作方向性二次交叉核验，不得直接求和替换省级序列。

若复现PASS，资本/PIM data-method blocker关闭，下一主要数据blocker只剩修订后2018 GDP。

## 后续顺序
PIM资本链闭合 → 修订后2018 GDP闭合 → 最终2018 V2 candidate input → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE有效性 → 必要有限省份 → 年度覆盖 → MP5/MP6动态。

当前不运行household/HJB/KFE/firm/GE/annual，不调整GovInv/alpha，不扩大bmax，不切换PLM。2022–2023负资本问题继续独立处理。
