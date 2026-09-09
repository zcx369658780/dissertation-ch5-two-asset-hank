# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`RAW_DATA_LINEAGE_AUDIT_ACCEPTED__YEAR_INDEX_MISALIGNMENT_AND_MIXED_VINTAGE_BLOCK_PRODUCTION`。
最新接受候选：`f850937ccb7b11b835ce5e45b9819ee25412ad03`。报告：`docs/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT_REPORT.md`；验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：无。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 当前最高优先级阻塞：年度数据合同失配
已接受审计证明，原MATLAB年度入口存在物质性年份语义错位：`multi_prov_HANK_12sts(ii,pp)`用`ii+2008`命名年度文件，但实际把`mydata2{ii}`与`data_year=ii`直接传入初始化器。工作簿首行对应2000，因此`ii=10`的“2018”标签实际选择2009水平数据。

安徽位置为MATLAB第12位、Python零基11、Excel列N。2018标签下保存路径实际消费的安徽水平量支持2009来源：GDP=`10864.68`亿元、常住人口=`6131`万人、资本存量=`228121755.48548827`（最终loader缩放前）。真正2018工作簿对应值不同：GDP=`34010.91`亿元、常住人口=`6076`万人、派生资本存量=`1357314108.2013683`。

同一2018标签状态还混合不同技术参数时间口径：alpha来自regression vintage19；Zt固定使用工作簿第21行，即2020水平量。当前保存的“2018状态”因此不是一致的2018数据vintage。

## 数据质量问题
填充工作簿是当前实际持久化输入；存在后运行时不会重新生成。总路径中：常住人口有3个endpoint填充；总固定资产投资有129个填充，其中128个是endpoint/extrapolation风险、1个内部填充。更广行业sheet还有额外连续缺失与endpoint填充。

资本递推`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`在2022–2023产生6个负资本省年，并使`log_pcap`出现复数。它们不是call725当前2009来源的直接原因，但证明现有填充+资本递推链能生成经济上无效状态。

2024原始版与旧原始工作簿之间共有8509个明确可比较数值单元，差异0；未能证明schema映射的字段保持`NOT_COMPARABLE`。

## 官方数据与Owner选择
已生成10条官方人工核验请求。P0优先：安徽2018 GDP、常住人口、2000–2018固定资产投资/资本存量链、alpha/Zt时间口径。P1为6个负资本省年。

在Owner批准年度语义与官方数据口径前：
- 不继续扩大`bmax`；
- 不调整alpha/GovInv收敛速度；
- 不重跑2018年度、多省份、GE或Results；
- 不修改生产loader、cache、原始Excel/MAT、生产参数或边界法则。

## 先前数值诊断仍有效但降级为次级
此前接受的事实继续保留各自范围：原rah=.09 call725 HJB100不收敛/KFE非有限；单户仅改rah=.07时HJB可停止；KFE边界source/escape、Qh负非对角元、P32/sigma、单户b域扩箱等均未被数据审计否定。但这些诊断建立在当前保存输入上，不能再被解释为“真正2018校准状态”的证据。

生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。Owner历史经验：真正收敛稳态Bt基本在0附近，生产设计保留`amax>bmax`；bmax=12仅为压力测试。

## 证据
本数据审计模型科学调用全部0。Synthetic tests 6/6。Builder manifest/readback：32文件全部匹配，manifest SHA256=`A64F9B6B9CD244AA481F41BAD27C9A95BEF8A00C6CF3003781078552B8B5EDC3`；外部cell ledger 10416条，位于`D:\ProjectTemp\ch5-2018-raw-data-audit-20260909-007`。
