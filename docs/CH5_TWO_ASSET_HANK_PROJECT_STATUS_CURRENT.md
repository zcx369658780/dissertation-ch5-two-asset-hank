# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION_ACTIVE__ROLLING_10Y_PLM_FROZEN`。
最新接受候选：`deb2d56560ce85590b9e19d34b4d28ea6b084e27`。时间合同审计报告：`docs/CH5_MP4C_TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT_REPORT.md`；Reviewer验收/Owner口径修正：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结年度时间合同
Owner最终选择PLM滚动10年窗（rolling 10-year window），理由是过旧数据会干扰不断发展的生产力估计；该选择与现有PLM artifact固定10期布局和源码“前10年的数据估计本年alpha”注释一致。

正式合同：
- `steady_year = 2008 + ii`；
- 稳态同年GDP/CAP/POP水平量使用MATLAB一基`level_row = ii + 9`；
- PLM估计器保持不变；
- PLM样本窗=`steady_year-9 : steady_year`，固定10年滚动；
- 2009使用2000–2009；2018使用2009–2018；2023使用2014–2023；
- 不采用从2000开始持续扩张窗口，不重建expanding-window PLM。

## 已确认缺陷与legacy
1. 旧MATLAB入口把`data_year=ii`传给初始化器，导致ii10/2018实际读取row10/2009水平量；这是confirmed level-index defect。
2. `load_GDPdata.m`固定用row21/calendar2020构造全部年度`Zt`；现有审计没有发现base-year/normalization经济依据，分类`LIKELY_LEGACY_FIXED_YEAR_ANCHOR`。当前Owner批准的实现方向是保持Zt公式不变，但用稳态同年的`level_row=ii+9`水平量。
3. 旧cache缺乏时间合同与PLM source版本身份；ii15 industry4旧cache alpha与较新workbook不一致。纠正后的输入不得静默继承旧无版本cache。
4. 2022–2023六个负资本/复数`log_pcap`仍是独立数据质量问题；本次实现不修改这些数据，也不把它们带入新的科学运行。

## 当前实现任务
任务只实现Python annual/pre-model输入层的时间合同，不运行模型：
- 机械断言2009–2023的calendar/index/level-row/PLM-vintage/rolling-window关系；
- GDP/CAP/POP与log量使用稳态同年数据；
- `Zt`使用同年GDP/CAP/POP和该年PLM alpha，不再固定2020；
- 增加显式temporal-contract version与cache/payload metadata；
- 对缺失、旧版、内部不一致或source-hash不匹配的corrected cache metadata fail closed；
- 只读生成2009和2018 corrected pre-model input摘要，用于后续Reviewer验证；
- 原始MATLAB源只读，仅输出未来最小MATLAB patch spec。

所有MATLAB model、household/HJB/KFE、root/direct/eigen、firm/one-turn/controller、GE/annual稳态、IRF/Results调用严格为0。

## 数据与数值边界
前序安徽2018官方数据人工核验清单仍未关闭；本次只使用当前已审计工作簿作为provisional primary source并记录hash，不将其升级为官方统计确认。此前rah=.09失败、.07敏感性、KFE source/escape、Qh负率、P32/sigma和b域压力测试仍只作为旧混合年份输入下的诊断证据。

生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]，保持`amax>bmax`。不继续扩大bmax，不调整GovInv/alpha收敛速度，不切换PLM估计器。

## 下一步顺序
完成并验收本次时间合同实现 → 关闭2018数据身份/官方核验 → 发布真正2018的单年小规模科学验证 → 若修正时间输入后仍高收益/不收敛，再审计GovInv/外层适应速度 → household/KFE数值有效性 → 必要有限省份验证 → 年度覆盖 → MP5/MP6动态路线。
