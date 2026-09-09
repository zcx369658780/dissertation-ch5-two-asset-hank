# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成原call725失败复现、rah=.07单户敏感性、KFE source/escape归因、一次b域压力测试、原始数据/插值审计以及年度时间合同/Zt legacy审计。Results=FALSE。

Owner已停止继续扩大`bmax`的路线：历史上真正收敛稳态的`Bt`基本在0附近，且低收益流动资产不应通过不断抬高上界来解释异常；生产网格继续冻结I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]，保持`amax>bmax`。

## 已冻结年度时间合同
Owner最终选择PLM滚动10年窗，理由是过旧样本会干扰不断发展的生产力估计。该选择与现有PLM artifact固定10期布局及源码“前10年的数据估计本年alpha”一致。

冻结合同：
- `steady_year = 2008 + ii`；
- 同年GDP/CAP/POP水平量一基row=`ii+9`；
- PLM estimator保持；
- PLM窗口=`steady_year-9 : steady_year`；
- 2009使用2000–2009；2018使用2009–2018；2023使用2014–2023。

因此候选审计报告中“Owner expanding window”以及“必须为expanding window重建PLM artifact”的解释被Reviewer验收文件正式纠正，不作为当前路线。

## 已确认的时间/数据缺陷
1. 当前入口把`data_year=ii`传给初始化器，导致ii10/2018实际取row10/2009水平量；这是confirmed level-index defect。
2. `load_GDPdata.m`固定用row21/calendar2020构造所有年度Zt，当前无已发现经济/标准化依据；分类`LIKELY_LEGACY_FIXED_YEAR_ANCHOR`。候选方向是保持公式、将Zt水平量同步到`ii+9`同年行。
3. 旧cache缺少明确时间合同/PLM版本身份；ii15 industry4 cache alpha与较新workbook不一致。后续cache/output必须版本化并断言steady_year、level_row/year、PLM vintage/window、Zt row/year及source hash。
4. 2022–2023六个负资本/复数log单元是独立数据质量问题；不能被时间索引修复掩盖。

## 下一步顺序
年度合同最小实现（level row + 同年Zt + versioned metadata/cache） → 关闭2018官方数据/身份核验 → 真正2018的单年小规模验证 → 若高收益/不收敛仍存在，再审计GovInv/外层适应速度 → household/KFE数值有效性 → 必要有限省份验证 → 年度覆盖 → MP5/MP6动态路线。

当前尚未发布新的实现task；不运行31省，不调整alpha/GovInv，不继续扩大bmax，不切换PLM估计器。

继续保持不变量：At*N而非At+Bt；household Lt与firm Lt_supply分开；保护原MATLAB/Excel/MAT；不以调容差、无限扩网格、无依据补source或更换估计器制造PASS；D1–D3、a_bar/FOC和经济source均未自动批准。
