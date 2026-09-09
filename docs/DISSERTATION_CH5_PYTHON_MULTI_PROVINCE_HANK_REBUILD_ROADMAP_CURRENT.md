# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成原call725失败复现、rah=.07单户敏感性、KFE source/escape归因、一次b域压力测试、原始数据/插值审计、年度时间合同/Zt legacy审计，以及V2时间合同Python pre-model静态实现。Results=FALSE。

Owner已停止继续扩大`bmax`。生产网格冻结I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]，保持`amax>bmax`。

## 已冻结并实现的年度时间合同
- `steady_year = 2008 + ii`；
- 同年GDP/CAP/POP水平量一基row=`ii+9`；
- PLM estimator保持；
- PLM窗口=`steady_year-9 : steady_year`，rolling 10-year；
- 2009=2000–2009，2018=2009–2018，2023=2014–2023；
- 不采用expanding-from-2000；
- Zt保持原公式但使用稳态同年level row，不再固定2020。

Python annual/pre-model层已通过静态验收，合同版本`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`。2018绑定analysis/data_MAT 10/10、row19/year2018、PLM vintage19、window2009–2018、Zt2018。V2 payload对legacy/missing/inconsistent/hash-mismatch fail closed。

## 当前 blocker
2018 corrected输入仍来自provisional audited workbook，官方数据身份尚未闭合。优先核验：安徽2018 GDP、常住人口、2000–2018固定资产投资/资本存量链，以及与PLM/Zt provenance一致的来源记录。官方身份关闭前不启动新的2018科学稳态。

ii15 industry4旧cache alpha与当前PLM workbook不一致；旧无版本cache继续禁止作为纠正后输入权威。2022–2023六个负资本/复数log是独立blocker，但不进入下一次2018小规模验证。

## 后续顺序
2018官方数据身份/来源闭合 → 真正2018单年小规模科学验证 → 若修正输入后仍高收益/不收敛，再审计GovInv/外层适应速度 → household/KFE数值有效性 → 必要有限省份验证 → 年度覆盖 → MP5/MP6动态路线。

继续保持不变量：At*N而非At+Bt；household Lt与firm Lt_supply分开；保护原MATLAB/Excel/MAT；不以调容差、无限扩网格、无依据补source、更换估计器或调整GovInv来补偿错误数据合同制造PASS。
