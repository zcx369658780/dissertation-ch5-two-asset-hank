# Chapter 5 当前交接
更新：2026-09-09。唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Owner最终科学authority；ChatGPT Reviewer规划/验收/发布；Codex Builder默认`gpt-5.6-sol / medium`。

## 当前入口
fresh读取live main、AGENTS、规则索引、当前状态和active task。
当前状态：`PIM_CAPITAL_CHAIN_CLOSURE_ACTIVE__EXISTING_PIM_METHOD_FROZEN__GDP_STILL_OPEN`。
active task：`tasks/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE.md`。
Results eligibility=FALSE。

## 已冻结合同
PLM rolling 10-year；2018=2009–2018；`steady_year=2008+ii`；同年level row=`ii+9`；same-year Zt。2018人口已经由2023《中国人口和就业统计年鉴》修订值`6076`万人闭合。

## Owner最新资本方法裁决
不再要求“官方资本存量”。Chapter 5资本存量继续采用现有永续盘存法（PIM），作为模型构造量：
- `K0=I0/.1`；
- `Kt=(1-.096)K(t-1)+I(t-1)`；
- depreciation=.096；
- 初始化规则不变；
- K2018依赖I2000..I2017。

当前省级投资链继续作为模型校准来源，但必须保留其CNKI整理来源限制和2011固定资产投资统计范围断点；不得把整条链描述为官方同口径历史序列。不得为了收敛改PIM公式/折旧率/初值或用城市数据直接替换省级链。

## 当前task
零科学调用地静态重建安徽K2018并核对现有workbook-derived CAP=`1357314108.2013683`。若精确复现，生成`CH5_2018_PIM_CAPITAL_INPUT_V1`类版本化receipt，记录投资年份、source/hash、PIM公式、时序、参数、2011口径限制、derived CAP及V2 transformed CAP。资本必须标记model-derived。

`s​​j479`地级市投资只能作`SECONDARY_DIRECTIONAL_CROSSCHECK_ONLY`，六项省级加总条件未闭合时不得求和。

## 剩余blocker
修订后安徽2018现价GDP仍未闭合：当前provisional `34010.91`亿元，初步官方`30006.82`亿元，缺第四次经济普查后修订精确表值。

## 路线
PIM资本链闭合 → GDP闭合 → 最终2018 V2 candidate input → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv调整速度。

当前不运行household/HJB/KFE/firm/GE/annual，不调GovInv/alpha，不扩大bmax，不切换PLM。生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。
