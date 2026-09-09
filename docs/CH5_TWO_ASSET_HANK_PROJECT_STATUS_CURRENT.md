# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`2018_RAW_DATA_AND_INTERPOLATION_AUDIT_ACTIVE__BMAX_ROUTE_DEFERRED`。
当前 active task：`tasks/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已接受事实
此前单户`bmax=12`压力测试已经接受：旧`bmax=5`对保存的2018安徽call725、rah=.07诊断状态具有物质性截断，但扩至12仍有upper-b压力、Qh负非对角元和source-free `Tg=0`失败，因此不能采用生产`bmax=12`或声称网格收敛。生产网格继续为I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。

Owner补充了重要历史事实与路线裁决：真正收敛的既有稳态里`Bt`基本在0附近；流动资产收益低于固定/非流动资产，因此不应通过不断扩大`bmax`追逐数值PASS，生产网格保持`amax>bmax`更符合当前模型设计。此前扩箱只保留为数值压力测试，不继续搜索更大b上界。

## 新优先级：数据先行
Owner指定原始数据路径：
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\2000年后各省数据.xlsx`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\2024年数据原始版.xlsx`
并要求核查当前使用的插值/平滑/缺失值处理数据。相关`2000年后各省数据_填充NA.xlsx`、`load_GDPdata.m`及`数据估计结果_1000_100_0.mat`等按实际存在与调用链只读审计。

本任务只做哈希、工作簿/MAT读取、源码数据链追踪、描述统计与2018安徽cell-to-model lineage；所有模型/HJB/KFE/firm/one-turn/GE/annual/IRF/Results/MATLAB调用均为0。不得修改原始工作簿、cache或生产loader。

重点解决：真实年份映射、31省/安徽列位置、原始与填充数据差异、缺失连续段/端点插补、单位/缩放、异常跳变，以及原始Excel→filled workbook→loader→mydata2/data_MAT/cache→2018安徽最终输入的逐字段来源。

若发现物质性数据质量/lineage问题，停止在报告阶段，并列出需要国家统计局/省统计年鉴人工核验的精确字段；不自动替换生产数据。若当前数据无明显物质问题，下一科学方向转为外层固定点/适应算法，尤其审计高收益/资本条件下各地区`GovInv`调整速度，不继续改`bmax`。

## 仍未解决
原rah=.09 call725不收敛/KFE非有限、`.07`局部敏感性、KFE边界source/escape、Qh负率、P32/sigma及2018年度覆盖等既有事实继续按各自范围有效。数据审计本身不修复这些问题，也不授权多省份重跑或生产参数改动。
