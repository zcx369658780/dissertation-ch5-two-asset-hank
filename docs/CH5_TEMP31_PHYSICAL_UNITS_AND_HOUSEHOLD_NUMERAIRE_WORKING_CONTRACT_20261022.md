# CH5 TEMP31 — 2018统一量纲与家庭计价基准的研究工作合同
DATE=2026-10-22
STATUS=PHYSICAL_DIMENSIONS_WORKING_CONVENTION__NUMERAIRE_OWNER_E3_PENDING
OWNER_DIRECTION=UNIFY_UNITS_BEFORE_31PROV_PARAMETER_TUNING
FORMAL_V010=FROZEN_UNCHANGED
SCIENCE_RUN_AUTHORIZED=FALSE

## 1. 已知来源和命名
2018 canonical workbook SHA256 AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67，文件路径只在精确授权的本地只读任务中核。已接受静态报告 docs/CH5_MP4C_2018_REVISED_GDP_AND_CANONICAL_DATA_WORKBOOK_REPORT.md：GDP输入亿元、PIM K输入万元、人口万人。历史MATLAB把GDP亿元及K万元一律×1000造成资本货币量纲扩大10000倍；2018混年缓存亦禁止。docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md此前提议MU_10WAN_YUAN/NU_100_PERSONS，但SPEC=PARTIAL，不能假装其所有经济设定被Owner采纳。
本次Owner同意**优先统一数值系统**。在TEMP31 SOURCE_ONLY结构/单位测试中采用以下物理基准；它是规划器对已建议数据标准的工作选项，不更改冻结正式V010、也不构成最终资产网格货币numeraire选择。

## 2. 宏观物理量纲（在SOURCE_ONLY和未调用HA的结构模块中统一）
- MU = 100,000人民币元（10万元）。真实当年名义GDP Y[M U] = GDP_raw[亿元]×1000；资本K[MU] = PIM_K_raw[万元]÷10，等于K_raw[亿元]×1000。GovInv/Corptax/WageTax/省级财政总量必须同MU。禁止对资本万元直接×1000。
- NU = 100人。N[NU] = POP_raw[万人]×100。此N是人口量纲，不是户数，绝不恢复P/3；跨省真实目的地企业劳动以NU×人均效率劳动单位E表示。
- MU/NU = 1000元/人。人均消费/财富/工资/转移与AtTax在进入聚合前须区分MU/NU和家庭内部HU单位。年GDP与PIM年末stock的金额都可用MU表示，但**存量和年流量时间维度仍不同**。
- 企业K[MU]、L[NU·效率单位]，Y[MU/模型期]；原始工资w_raw量纲MU/(NU·效率单位·模型期)，无量纲alpha,mt,税率。资本收益r,rb,rah单位1/模型期；元/万人不等于元/人。Z单位应由Y/(K^alpha L^(1-alpha))导出，转换Y/K/N时Z数值必须根据单位重新计算，不能直接保留旧混年Z。
- MATLAB 原`ramax=.09/ramin=.02`是“每模型期收益率”候选界，非货币单位；需要确认年度与连续时间口径，不能按货币换算倍数缩放收益率。原wjtmin=.8/wjtmax=1.3是源数值界，其**现实元/人解释取决于下述HU基准及劳动效率/期间**，不能未经选择直接用物理MU/NU比较。
- 源2018安徽静态示例：GDP=34010900 MU，N=607600 NU，PIM K=135731410.82013685 MU，故GDP/N≈55.97515 MU/NU，K/N≈223.38942 MU/NU、K/Y≈3.99082；这里仅演示转换，不能用安徽替代全国31省固定基准或确定GovInv/家庭资产占比。

## 3. 家庭HA货币计价基准：一个共享numeraire，不是单调资本补偿参数
定义HU为HA内部统一的货币数值单位，s_H>0量纲为(MU/NU)/HU。A_HU和B_HU均为每人HU，C_HU/工资_HU/T_HU/AtTax_HU均为HU/每模型期，所有真正同一货币单位的原变量须统一转换；资产网格a∈[0,10]、b∈[-2,5]是HU数值范围。家庭私人财富流入宏观量为W_i[MU]=A_i[HU]*s_H[(MU/NU)/HU]*N_i[NU]；B同理。资本分配同一S且每列和1，Kprivate_j=sum_i S[j,i]W_i。
进入HA的物理单位工资或转移要除以同一s_H，firm有效劳动用NU×效率，企业工资原值若在物理系统计算则w_HU=w_phys/s_H。2018企业Y/K/GovInv若与家户回报直接进入一个HA-HU求解/企业HU数值系统，则都按同一s_H除法转成HU·NU或持物理单位明确桥接，不能仅放大At而不调整其他货币流量。收益率r及无量纲税率不能按s_H缩放。
**s_H不可随省、外层轮次、试错、价格触界或HA是否收敛自动改变；也不可把1当成获得Owner支持的宏观资产桥。** 一次选定必须覆盖31省同一个s_H，作为经济归一化而非幕后拟合因子。
对源效用u(c)与劳动厌恶权重、d(a,b)调整成本、固定调整成本/截距、a_bar及预算T/w/C, HJB连续时间单位逐一做符号量纲oracle。若源参数带HU幂次，单纯改变s_H会改变模型经济含义，必须把需要重新校准的系数列为E3，不可宣称统一货币缩放对模型严格等价。

## 4. 本轮允许比较的预注册HU基准（只算数，不做HA或选择）
候选GDP-ANCHORED：全国2018加总一致的s_H_GDPpc=SUM_j Y_j[MU]/SUM_j N_j[NU]，量纲MU/NU每HU。这个全国统一数来自可审计GDP/POP，非某省单独取值；若2018原数据缺省或多省顺序不符合授权则STOP。用s_H_GDPpc，原wjt[.8,1.3]在HU中的带映射为[0.8 s_H_GDPpc,1.3 s_H_GDPpc] MU/NU每效率单位；原a_max=10对应10 s_H_GDPpc MU/NU人均名义非流动资产。只作为可解释尺度候选，**不是已核真实工资统计范围或已采纳原MATLAB numeraire**。
候选LABOR-ANCHOR（可选诊断对照）：用同年Y、N、Owner已接受alpha及冻结mstar通过事前固定参考L_ref=N得到一个共同的产出加权预期劳动报酬参照。例如s_H_LABOR = SUM_j mstar*(1-alpha_j)*Y_j / SUM_j N_j；必须标为模型派生、取决于L_ref=N的初始假设，而非官方工资数据。此候选只在来源和L_ref确切受权时计算，不能擅采为生产工资单位。
若两个候选推导不支持同一记账口径或出现异常边界，记录证据和敏感性但不调s_H使工资/ra触界最少。最终Owner手动选择并冻结唯一s_H公式、输入SHA、2018年份、模型期、工资界语义、家庭效用成本单位之后才能在下一独立任务将其用于真实31省HA。

## 5. Source-only数值检查与科学停止
必须用单位指纹记录GDP亿元→MU、K万元→MU、N万人→NU、Y/N与K/N以及Y=ZK^alpha L^(1-alpha)的物理量纲。货币缩放任何两种等价单位写法在转回物理MU时应严格同值；反例：旧CAP×1000、人口重复×100、At仅资产一侧乘系数、wjt误按元/人未换算、跨省来源/目的地乱轴，必须拒绝。
不得在本轮启动HA/HJB/KFE、one-turn原生产经济求解、31省外层/GE/IRF、自动调N/Zt/GovInv/工资边界，也不得更改正式V010方案。必须输出31省SOURCE_ONLY数据矩阵和来源SHA、两个HU基准的解释与未决参数清单，供Owner下一次单位E3裁决。没有资格的指标保留NA/UNRESOLVED，不从原MATLAB历史跑通推导新经济合法性。
OWNER_NEXT=DISCUSS_AND_APPROVE_ONE_HOUSEHOLD_NUMERAIRE_OR_REQUEST_EXTRA_EVIDENCE__NO_AUTO_RUN
