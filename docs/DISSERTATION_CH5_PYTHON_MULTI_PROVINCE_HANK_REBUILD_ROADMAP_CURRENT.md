# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成原call725失败复现、rah=.07单户敏感性、KFE source/escape归因、一次b域压力测试和原始数据/插值审计。Results=FALSE。

Owner已停止继续扩大`bmax`的路线：历史上真正收敛稳态的`Bt`基本在0附近，且低收益流动资产不应通过不断抬高上界来解释异常；生产网格继续冻结I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]，保持`amax>bmax`。

## 已接受的数据问题
数据审计证明，原年度入口的标签和实际水平数据行错位：`ii+2008`作为输出年份，但`mydata2{ii}`直接从2000起始的数据矩阵取第ii行，因此`ii=10`标记2018却使用2009水平数据。该状态还混用regression vintage19 alpha与固定2020水平行构造Zt。该问题优先于边界压力和外层收敛调速。

Owner明确原设计意图：由于PLM需要历史样本，首个稳态应使用2000–2009样本估计用于2009稳态的技术对象；后续年份应沿用截至该年的估计。PLM是既有替代方法比较中效果最好的方法，当前不更换估计方法。Owner怀疑固定2020行构造Zt是遗留代码。

## 当前 active task：时间合同与Zt legacy审计
`tasks/CH5_MP4C_TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT.md`。

零模型调用。任务验证并冻结年度映射：
1. `steady_year = 2008 + ii`是否与文件名/回归vintage/历史设计一致；
2. 同年水平量是否应使用从2000起始数据矩阵的`ii+9`行；
3. PLM的`ii+9` vintage是否已经对应2000至steady_year的扩展样本；
4. 固定2020行Zt是否缺少经济依据，应视为legacy fixed-year anchor；
5. 最小修复是否只需校正水平量/Zt的年份索引，而保持PLM估计方法、经济方程和数值算法不变。

本task只输出temporal-contract表、legacy分类和source patch plan，不执行生产patch、不运行2009/2018稳态、不调整alpha/GovInv。

## 后续顺序
时间合同冻结 → Owner接受Zt年份语义/官方数据口径 → 最小数据索引修复 → 真正2009/2018的单年小规模验证 → 如仍存在高收益/不收敛，再审计GovInv/外层适应速度 → household/KFE数值有效性 → 必要有限省份验证 → 年度覆盖 → MP5/MP6动态路线。

继续保持不变量：At*N而非At+Bt；household Lt与firm Lt_supply分开；保护原MATLAB/Excel/MAT；不以调容差、无限扩网格、无依据补source或更换估计器制造PASS；D1–D3、a_bar/FOC和经济source均未自动批准。
