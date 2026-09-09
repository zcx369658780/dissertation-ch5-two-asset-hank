# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成原call725失败复现、rah=.07单户敏感性、KFE source/escape归因、一次b域压力测试、原始数据/插值审计以及年度时间合同/Zt legacy审计。Results=FALSE。

Owner已停止继续扩大`bmax`：历史上真正收敛稳态的`Bt`基本在0附近，且低收益流动资产不应通过不断抬高上界来解释异常。生产网格冻结I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]，保持`amax>bmax`。

## 冻结年度合同
- `steady_year = 2008 + ii`；
- 同年GDP/CAP/POP水平量一基row=`ii+9`；
- PLM estimator保持；
- PLM窗口=`steady_year-9 : steady_year`，固定rolling 10-year；
- 2009=2000–2009；2018=2009–2018；2023=2014–2023；
- 不采用expanding-from-2000窗口；
- 固定2020行Zt分类`LIKELY_LEGACY_FIXED_YEAR_ANCHOR`，当前实现方向为保持公式、改用稳态同年level row。

## 当前 active task
`tasks/CH5_MP4C_TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION.md`

任务只实现Python annual/pre-model输入层：calendar/index/level-row/PLM-window合同、same-year Zt、temporal-contract version、cache/payload metadata与stale-cache fail-closed；并只读生成2009/2018 corrected pre-model摘要。原MATLAB源不改，只输出patch spec。所有HJB/KFE/firm/one-turn/annual/GE/MATLAB model/root/eigen/IRF/Results调用均为0。

## 仍未关闭
- 安徽2018 GDP/人口/固定投资资本链等官方数据核验请求仍开放；
- ii15 industry4旧cache alpha与较新PLM workbook不一致，旧cache不得作为纠正后输入权威；
- 2022–2023六个负资本/复数log单元是独立数据质量blocker；
- 旧rah=.09、.07、KFE边界、Qh负率、P32/sigma和b域诊断仍仅代表旧混合年份输入。

## 后续顺序
时间合同实现验收 → 2018数据身份/官方核验闭合 → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv/外层适应速度 → household/KFE数值有效性 → 必要有限省份验证 → 年度覆盖 → MP5/MP6动态路线。

继续保持不变量：At*N而非At+Bt；household Lt与firm Lt_supply分开；保护原MATLAB/Excel/MAT；不以调容差、无限扩网格、无依据补source、更换估计器或调整GovInv来补偿错误数据合同制造PASS。
