# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成原call725失败复现、rah=.07单户敏感性、KFE source/escape归因和一次b域压力测试，但原source-free稳态与Qh数值有效性尚未通过。Results=FALSE。

Owner现已明确改变下一步路线：不再通过持续提高`bmax`寻求收敛。历史经验表明正常收敛稳态的`Bt`基本在0附近；当前模型中流动资产收益低于固定资产收益，生产网格保持`amax>bmax`。因此b=12只作为已完成压力测试保留，生产I20,b[-2,5]与J20,a[0,10]继续冻结。

## 当前 active task：原始数据/插值审计
`tasks/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT.md`。
零模型调用。只读检查原始Excel、filled/interpolated workbook、MAT cache及MATLAB数据loader，解决：
1. 原始值→缺失值填充/平滑→transform/cache→2018安徽模型输入的完整lineage；
2. `ii/data_year`与实际日历年份映射；
3. 31省/安徽方向与列位置；
4. missing runs、endpoint/extrapolation、异常跳变、非正值、单位/缩放和schema变化；
5. 需要国家统计局或省统计年鉴核验的精确变量-省份-年份清单。

数据异常若有明确路径影响2018/calibration，则先由Owner决定官方值和修正方案，不直接改生产数据或运行模型。若审计范围内未发现物质性数据问题，则下一阶段进入外层收敛算法审计：围绕source-faithful ordered update map，研究高收益/资本失衡时`GovInv`及相关适应速度是否过慢。任何算法改动先冻结具体规则和有界单年/小规模测试；不直接恢复31省年度批量运行。

## 后续顺序
数据/lineage审计 → （必要时）官方数据修正裁决 → 外层收敛/适应规则审计与有界诊断 → household/KFE数值有效性与2018单年闭合 → 必要有限省份验证 → 年度覆盖 → MP5/MP6真正动态路线。

继续保持不变量：At*N而非At+Bt；household Lt与firm Lt_supply分开；原MATLAB受保护；不以调容差/无限扩网格/无依据补source制造PASS；D1–D3、a_bar/FOC和经济source均未自动批准。
