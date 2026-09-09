# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`PURCHASED_DATASET_AUDIT_ACCEPTED__2018_POPULATION_IDENTITY_CLOSED__GDP_AND_INVESTMENT_REMAIN_OPEN`。
最新接受候选：`4db5c0691535e92d34a86c67ee96c2b8978c1de2`。报告：`docs/CH5_MP4C_PURCHASED_DATASET_GAP_CLOSURE_AUDIT_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：无。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结并实现的年度合同
PLM rolling 10-year；`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；2018使用2009–2018、PLM vintage19；Zt保持原公式并使用同年水平量。Python annual/pre-model层已实现`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`和V2 metadata/source-hash fail-closed合同。

## 本轮付费数据审计接受结论
1. 2018安徽常住人口身份已闭合为`6076`万人。证据来自付费本地包中的官方《中国人口和就业统计年鉴2023》表1-1；该表明确说明2011–2019年人口数据依据2020年人口普查修订。权威来源是官方年鉴，不是付费包本身。该证据解释了2018初步公报`6323.6`万人、2019年鉴约`6324`万人与后续修订`6076`万人之间的差异。
2. 2018安徽GDP仍未闭合。当前provisional workbook为`34010.91`亿元，2018初步官方公报为`30006.82`亿元；尚未取得第四次全国经济普查后修订口径下2018现价GDP精确值和修订表。
3. `sj479`地级市固定资产投资数据对安徽2000–2017每年覆盖16市，无重复、无缺失，但这不足以证明省级可加总。省级残余/省直管覆盖、行政区划衔接、统计口径一致性和城市到省份的加总授权未证明；2017值还包含依据增速推算的成分。因此未计算城市合计，也未运行资本递推。
4. 当前CAP=`1357314108.2013683`继续只是workbook派生provisional模型输入，不是官方资本存量，也没有被付费数据升级为候选资本存量。
5. 付费TFP数据在安徽2009–2018形成完整16市×10年×11方法、无缺失的高质量研究数据，但基年/尺度、具体deflator和省级聚合合同不足，生产用途分类为`NOT_COMPARABLE_WITH_CURRENT_PROVINCE_ZT`。PLM继续冻结；该TFP仅可在未来独立任务中作为验证基准或方法候选。

## 当前剩余数据blocker
2018科学运行前仍需关闭：
- 第四次全国经济普查后修订口径下安徽2018现价GDP；
- 2000–2017安徽省级可比固定资产投资链，或Owner另行批准资本存量重构方法。

人口不再是2018 blocker。

## 科学路线
当前不启动2018 household/HJB/KFE/firm/GE/annual科学运行，不调整GovInv/alpha，不扩大bmax，不切换PLM。下一步需要Owner在投资/资本链上作科学选择或提供更高权威省级投资数据；GDP继续寻找修订后官方表。

2022–2023六个负资本/复数`log_pcap`仍是独立数据质量问题，不进入下一次2018小规模验证范围。生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。
