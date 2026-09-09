# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT_ACTIVE__PLM_PRESERVED`。
最新接受候选：`f850937ccb7b11b835ce5e45b9819ee25412ad03`。数据审计报告：`docs/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT_REPORT.md`；验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## Owner 最新科学澄清
Owner确认原年度设计不是从2000直接做稳态，而是先用一段历史样本估计各省技术/生产率，再做后续年度稳态。首个意图是用2000–2009样本估计用于2009稳态的技术对象；后续年份应沿用同样的“截至该年”的估计逻辑。去年已在`load_GDPdata.m`等遗留代码中测试过其他估计方法，但PLM效果最好，因此当前继续保留PLM，不因数值收敛问题切换估计方法。

Owner同时表示：固定使用2020水平行构造`Zt`很可能是代码遗留，而非有意的基准年锚定。

## 已接受的数据审计事实
原MATLAB入口用`ii+2008`命名年度文件，但`mydata2{ii}`/`data_year=ii`直接选择从2000开始的数据矩阵，因此`ii=10`的“2018”标签实际消费2009水平量。安徽2018标签下实际消费GDP=`10864.68`亿元、常住人口=`6131`万人、资本存量=`228121755.48548827`，对应2009行；真正2018工作簿对应GDP=`34010.91`、人口=`6076`、派生资本存量=`1357314108.2013683`。

同一2018标签状态还使用regression vintage19 alpha与固定2020水平行构造的Zt。数据审计另发现投资endpoint填充风险及2022–2023六个负资本/复数log_pcap单元；这些是独立数据质量问题。

## 当前任务
当前任务不运行模型，只把Owner原设计意图与源码实际实现对齐。重点验证：
- 是否应冻结`steady_year = 2008 + ii`；
- 同年水平量是否应选`ii+9`数据行（2009对应row10、2018对应row19）；
- PLM的`ii+9` vintage命名/样本终点是否已经与稳态年度一致；
- 固定2020行Zt是否缺乏经济依据并应视为legacy anchor；
- 最小修复是否只需修正水平量与Zt的年份索引，而不改PLM估计方法。

本任务所有HJB/KFE/firm/GE/年度/MATLAB/root/direct/eigen等科学调用均为0，只允许静态source/workbook/cache审计、索引算术、patch plan和synthetic tests。

## 冻结不变项
不继续扩大`bmax`；生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]，保持`amax>bmax`设计。Owner历史经验：真正收敛稳态的Bt基本在0附近。当前不调整alpha/GovInv收敛速度，不重跑2018、多省份、GE或Results，也不修改生产loader/cache/原始Excel/MAT/PLM估计方法。

此前rah=.09失败、.07局部敏感性、KFE边界source/escape、Qh负率、P32/sigma和b域压力测试继续保留为当前保存输入下的数值诊断，但不能解释为真正2018校准状态。
