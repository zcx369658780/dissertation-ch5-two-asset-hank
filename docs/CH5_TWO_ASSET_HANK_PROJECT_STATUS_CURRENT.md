# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`TEMPORAL_CONTRACT_IMPLEMENTATION_ACCEPTED__V2_ROLLING10Y_SAMEYEAR_ZT_STATIC_PASS__OFFICIAL_2018_DATA_STILL_BLOCKS_SCIENCE`。
最新接受候选：`6746565506eb953ea599536d3f745764d225ffef`。实现报告：`docs/CH5_MP4C_TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：无。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结并实现的年度合同
Owner冻结PLM滚动10年窗：`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；PLM窗口=`steady_year-9:steady_year`；2009=2000–2009、2018=2009–2018、2023=2014–2023；PLM estimator/workbook保持。

Python annual/pre-model层已实现合同版本`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`。2009绑定analysis/data_MAT 1/1、row10、vintage10、Zt2009；2018绑定10/10、row19、vintage19、Zt2018。2020使用row21仅因同年映射自然成立，不再存在fixed-2020特殊合同。

2018安徽静态corrected provisional输入：Python index11 / MATLAB index12 / Excel N；GDP=34010910.0，POP=607600.0，CAP=1357314108201.3684，alpha=0.772866243094144，same-year IND_Zt=0.0006934646534806338。

## provenance/cache合同
V2 payload显式保存contract/schema/output identity、steady/calendar year、analysis/data row、PLM vintage和rolling-window范围、Zt row/year以及primary/PLM source hashes。missing metadata、V1/legacy schema、内部年份不一致、source hash或PLM hash不匹配均fail closed。

ii15/industry4旧cache alpha=0.967775174774325，而当前hash-bound PLM workbook value=1.0219847778591；旧无版本cache不能覆盖当前workbook。原MATLAB源未修改，只发布未来最小patch spec。

## 验收证据
Scoped tests 22 passed；py_compile、git diff --check通过。Builder manifest 32项匹配，SHA256=`F529EF14096482734BC2FB98E90A739F2BBEF5D6AE23CE3D6B3AC8F1D8C10910`。一次historical annual-driver测试收集因受保护standalone household-oracle身份不匹配在执行前停止；日志保留、不绕过、不计入PASS，也未触发模型调用。

科学调用全部0：MATLAB、household/HJB/KFE、roots/solves、firm/one-turn/controller、stationary/GE/annual loop、IRF/dynamics/Results均未运行；仅构造2009和2018两个静态pre-model对象。

## 当前最高优先级blocker
2018 corrected输入仍使用`PROVISIONAL_AUDITED_SOURCE__OFFICIAL_VERIFICATION_OPEN`工作簿。安徽2018 GDP、常住人口、固定投资/资本存量链尚未完成官方来源身份闭合，因此在此之前不启动新的2018 household/firm/GE/annual科学运行，也不调整GovInv/alpha速度。

2022–2023六个负资本/复数`log_pcap`仍是独立数据质量问题，但不进入下一次2018小规模验证范围。

此前rah=.09/.07、KFE边界source/escape、Qh负率、P32/sigma和b域压力测试继续保留为旧混合年份输入下的诊断证据，不能解释为真正2018校准状态。

生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]，不继续扩大bmax。

## 下一步顺序
2018官方数据身份/来源闭合 → 真正2018单年小规模科学验证 → 若修正输入后仍高收益/不收敛，再审计GovInv/外层适应速度 → household/KFE数值有效性 → 必要有限省份验证 → 年度覆盖 → MP5/MP6动态路线。
