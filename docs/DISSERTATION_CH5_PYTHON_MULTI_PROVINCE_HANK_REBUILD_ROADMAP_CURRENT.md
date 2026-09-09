# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成原call725失败复现、rah=.07单户敏感性、KFE source/escape归因、b域压力测试、原始数据/插值审计、年度时间合同/Zt legacy审计、V2 pre-model静态实现，以及首轮官方2018身份审计。Results=FALSE。

## 冻结年度合同
`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；PLM estimator保持rolling 10-year；2018=2009–2018；Zt公式保持并使用同年水平量。生产网格继续I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]。

## 当前数据状态
首轮官方审计未闭合最终修订身份：2018安徽初步官方GDP/人口与当前workbook不一致；第四次经济普查后的精确修订GDP和人口后续谱系未取得。K2018只依赖I2000..I2017，且固定资产投资在2011存在统计范围断点，因此未按官方链重算CAP。

Owner指出原CNKI面板有缺失/潜在偏误，并提供`D:\BaiduNetdiskDownload`中的付费人工整理数据作为高质量第二来源。当前active task：`tasks/CH5_MP4C_PURCHASED_DATASET_GAP_CLOSURE_AUDIT.md`。

任务优先审计：
- 地级市全要素生产率1978–2022；
- `sj479`地级市固定资产投资2000–2024；
- `NJ73`人口与就业统计年鉴1949–2023；
- 其他直接相关的省/市级人口、投资、GDP或生产率文件。

只读判断这些数据的schema、来源、缺失、口径和可比性；购买/人工校对不等于官方authority。城市投资只有在可加总、覆盖完整、地域边界和统计口径均证明成立时才允许生成描述性省级候选；TFP不替换当前PLM，只评估为独立验证基准或未来替代候选。

## 后续顺序
付费数据缺口闭合审计 → Reviewer判断candidate source/package与剩余官方缺口 → 数据身份足够闭合后才发布真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE数值有效性 → 必要有限省份 → 年度覆盖 → MP5/MP6动态。

当前不运行household/HJB/KFE/firm/GE/annual，不调整GovInv/alpha，不扩大bmax，不切换PLM。2022–2023负资本问题继续独立处理。
