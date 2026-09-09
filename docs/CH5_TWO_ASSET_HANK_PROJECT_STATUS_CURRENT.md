# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`TEMPORAL_CONTRACT_AUDIT_ACCEPTED__ROLLING_10Y_PLM_FROZEN__LEVEL_INDEX_DEFECT_CONFIRMED__ZT_2020_ANCHOR_LIKELY_LEGACY`。
最新接受候选：`deb2d56560ce85590b9e19d34b4d28ea6b084e27`。报告：`docs/CH5_MP4C_TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT_REPORT.md`；Reviewer验收/Owner口径修正：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：无。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结年度时间合同
Owner最终选择PLM滚动10年窗（rolling 10-year window），理由是过旧数据会干扰不断发展的生产力估计；该选择与现有PLM artifact固定10期布局和源码“前10年的数据估计本年alpha”注释一致。

正式合同：
- `steady_year = 2008 + ii`；
- 稳态同年GDP/CAP/POP水平量使用MATLAB一基`level_row = ii + 9`；
- PLM估计器保持不变；
- PLM样本窗为`steady_year-9 : steady_year`；
- 2009稳态使用2000–2009；2018使用2009–2018；2023使用2014–2023；
- 不采用“从2000开始持续扩张窗口”，不要求因此重建PLM为expanding-window estimator。

## 已确认缺陷与legacy
1. 当前生产入口仍把`data_year=ii`传给初始化器，因此ii10/2018实际读取row10/2009水平量。该level-row错位是confirmed defect。
2. `load_GDPdata.m`固定使用row21/calendar2020构造所有年度`Zt`；源码审计未发现base-year/normalization经济依据，当前分类为`LIKELY_LEGACY_FIXED_YEAR_ANCHOR`，不是`PROVEN_BUG`。候选修复是保持原公式但使用同年`level_row=ii+9`。
3. ii1–ii14 industry4 cache alpha与当前PLM workbook一致，但ii15 cache alpha=`0.967775174774325`，当前vintage24 workbook=`1.0219847778591`。旧cache缺乏版本身份，后续必须版本化并记录PLM source/workbook hash和时间合同metadata。

## 数据质量仍未关闭
前序审计确认2018标签实际混用2009水平量、vintage19 alpha和2020 Zt；并发现固定资产投资endpoint填充风险，以及2022–2023六个负资本/复数`log_pcap`单元。年份合同修正不能掩盖这些问题。安徽2018 GDP、人口、固定投资/资本链等官方核验清单继续有效。

## 数值诊断的当前解释
此前rah=.09失败、.07单户敏感性、KFE source/escape、Qh负非对角元、P32/sigma与b域压力测试都继续作为“旧保存混合年份输入下”的数值诊断证据保留，但不能解释为真正2018校准状态。

生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]，保持`amax>bmax`。不继续扩大bmax；当前也不调整GovInv/alpha收敛速度。

## 下一步
先做有界实现：修正`level_row=ii+9`、将Zt水平行同步到稳态同年、版本化cache/output metadata并拒绝旧无版本cache；保持现有rolling-10y PLM estimator/artifact语义。第一次新的科学稳态运行前，仍需完成2018官方数据核验/身份确认，并把2022–2023负资本限制在本次2018验证范围之外。任何多省份、GE、年度批量或Results运行仍未授权。
