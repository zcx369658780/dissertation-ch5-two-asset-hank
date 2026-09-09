# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：zcx369658780/dissertation-ch5-two-asset-hank。

## 当前状态
状态：`B_DOMAIN_EXPANSION_ACCEPTED__TRUNCATION_MATERIAL__B12_STILL_INSUFFICIENT__NEXT_GRID_OR_BOUNDARY_DECISION_PENDING`。
最新接受候选：`daccda4698e87ee60a76fc4ff0196468b40198d3`。报告：`docs/CH5_MP4C_CALL725_RAH_0P07_B_DOMAIN_EXPANSION_REPORT.md`；验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：无。Builder 默认 `gpt-5.6-sol / medium`；实际 host 未暴露时不虚报已验证模型，不改 provider/global 配置。

Owner继续保留原 MATLAB-faithful 算法、`a_bar`、生产 `ramax` 与生产网格；不批准经济 source、D1–D3、边界实现或多省份新运行。Results eligibility=FALSE。

## 最新单户扩箱事实
唯一新科学对象仍是2018安徽call725、`rah/r_a=.07`。生产基线为 I20、b[-2,5]；诊断副本保持原 binary64 `db=0.368421052631579`，精确保留旧20个b节点并追加19点到12.0，得到I39、39x20x2=1560状态；a[0,10]、z[.8,1.3]、switch、价格、参数、`a_bar`、原生初始化、helper、solver、Delta1000、crit1e-7、maxit100均不变。共同旧子网格的 native V0/l0 800/800逐位一致。

扩箱HJB第17次更新满足原停止条件，statistic=`7.140894586754598e-08`。但最终迭代Qh仍有11个负非对角元，最小`-3.464832800963844`，所以停止条件通过不等于完整HJB数值有效。

post-loop Q仍有17个upper-b外向单元，最大rate=`3.469034770311481`，未加权总rate=`16.296417971077133`；其他三面0。`Q*1+ell`最大绝对值约`2.94e-15`，说明原有“越界offdiagonal省略但diagonal离开率保留”的有限箱机制仍在。

原KFE污染系统返回有限解，但原source-free稳态仍FAIL：`||Tg||inf=0.5206986084614471`，尺度比`0.11601750528081986`。正确的扩箱诊断分布质量为：总量`0.9999999999999999`；`b<=5`=`0.5327650526244969`；`b>5`=`0.46723494737550303`；新top face=`0.06835756005310577`。density-weighted upper-b escape=`0.10096648917534981`。这些是失败原稳态上的诊断密度事实，不是居民财富分布结果。

因此两个结论同时成立：旧`bmax=5`对这个保存单户状态是物质性截断，因为扩箱后约46.72%的诊断质量落在旧上界之外；但`bmax=12`仍未充分，因为新顶面仍约6.84%质量、仍有17个外向格且`Tg=0`明显失败。不能采用生产`bmax=12`，也不能声称网格收敛。

源pin随state_count机械改变为k=576，F-order(30,14,0)，坐标约(9.05263157894737,7.368421052631579,.8)。所以新旧KFE density与C/L/A/B比较是pin-dependent次级诊断，不是固定pin的纯bmax因果效应。row-replacement隐含source继续与escape闭合，但不采纳经济source法则。

## 预算与证据
本扩箱科学预算已消费：Python科学进程1；native init1；labor root/brentq各1560；HJB1、direct solve17；KFE/direct solve各1；aggregate1。重启/重试0；旧基线、其他利率/省份、firm/one-turn/GE/年度/MATLAB/IRF/Results调用0。
最终合成测试9/9；manifest SHA256=`B4299EB15F616AA1DE8D40FF5B655E4BB6AB6C694E673F99695B9822663BEA38`，Builder回执69引用全部匹配。Reviewer做L3提交/代码/报告和L4发布日志检查，未独立执行模型/测试、读取Windows大数组或重验69引用。

## 前置科学事实继续有效
- 原rah=.09 call725：原生HJB100不收敛、KFE非有限；上游raw `ra0≈.219`被clip到`.09`，原Zt/GovInv反馈实际执行。
- 单户仅改rah=.07：旧20x20x2箱中HJB26收敛/KFE返回，但原`Tg=0`失败；旧top-face质量约`.6758362`、density-weighted escape约`.6697587`。
- KFE质量账本已确认物质性残差集中在被替换行，隐含pin source平衡边界escape，仅限有限箱代数。
- 共同MAT初始化的MATLAB143/Python500、多轮P32、sigma丢失、Qh负率、旧边界规格等保持各自历史范围，未被扩箱实验解决。
- 旧runtime-cache 15/15 与 Owner-A 13/14 年口径继续分开，2018修正覆盖未接受。

## 下一科学选择
当前不运行31省。也不自动继续扫描bmax直到PASS。Owner下一步需在两条路中作出选择：
1. 预先冻结一个新的、仍为单户的更大b上界作为第二个截断稳健性点；或
2. 转入有限箱边界法则的明确科学选择。
任何新b点必须在结果前固定范围/分辨率/预算，继续保留原算法和生产设置；单纯多次扩箱不能取代边界经济含义。无Owner选择前不发布新科学task。

保护HJB SHA256=`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`；export blob=`9e7dc9556a2b76811e78f89999abecc045886106`。工作目录与全部历史证据继续只读保护。
