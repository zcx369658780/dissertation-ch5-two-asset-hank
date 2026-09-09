# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`OFFICIAL_2018_DATA_IDENTITY_CLOSURE_ACTIVE__NO_SCIENCE_RUN`。
最新接受候选：`6746565506eb953ea599536d3f745764d225ffef`。时间合同实现报告：`docs/CH5_MP4C_TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_OFFICIAL_DATA_IDENTITY_CLOSURE.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结并实现的年度合同
Owner冻结PLM滚动10年窗：`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；PLM窗口=`steady_year-9:steady_year`；2009=2000–2009、2018=2009–2018、2023=2014–2023；PLM estimator/workbook保持。

Python annual/pre-model层已实现`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`。2018绑定analysis/data_MAT 10/10、row19、vintage19、rolling window 2009–2018、same-year Zt 2018。当前安徽静态provisional输入：GDP=34010910.0，POP=607600.0，CAP=1357314108201.3684，alpha=.772866243094144，IND_Zt=.0006934646534806338。

## 当前 active task：官方数据身份闭合
本任务只做数据/证据工作，不运行模型。优先核验安徽2018 GDP、常住人口、固定资产投资序列及由冻结递推得到的2018模型资本存量。官方来源优先级：国家统计局 → 安徽省统计局/安徽统计年鉴 → 其他明确官方统计出版物。

必须区分官方观测量与模型派生资本存量；资本存量只有在官方投资序列完整可比时才按冻结递推静态计算，并标记`MODEL_DERIVED_FROM_OFFICIAL_INVESTMENT`。若投资口径断裂、官方值缺失或来源不可访问，停止并给Owner精确人工下载清单，不得自行插补或拼接不兼容序列。

如官方值与当前workbook一致，形成identity-closure receipt；如不一致，只生成versioned candidate correction package和差异/来源证据，不覆盖原Excel、filled workbook、PLM workbook、MAT cache或生产代码。

所有MATLAB、household/HJB/KFE、roots/solves、firm/one-turn/controller、stationary/GE/annual、IRF/Results调用均为0。

## 仍未关闭
2022–2023六个负资本/复数`log_pcap`为独立数据质量问题，不进入本次2018身份闭合。旧rah=.09/.07、KFE边界source/escape、Qh负率、P32/sigma和b域压力测试只代表旧混合年份输入。

生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。不继续扩大bmax，不调整GovInv/alpha速度，不切换PLM估计器。

## 下一步顺序
完成并验收2018官方数据身份闭合 → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv/外层适应速度 → household/KFE数值有效性 → 必要有限省份验证 → 年度覆盖 → MP5/MP6动态路线。
