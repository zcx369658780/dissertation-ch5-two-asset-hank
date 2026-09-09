# Chapter 5 MP4C 2018 原始数据与插值/缺失值来源审计报告

- Classification: `MATERIAL_DATA_QUALITY_OR_LINEAGE_ISSUE_FOUND`、`PARTIAL_EVIDENCE_NEEDS_OFFICIAL_DATA`。
- Results eligibility: `FALSE`。
- 模型、HJB、KFE、firm、one-turn、GE、年度、MATLAB、root/direct/eigen调用均为0。

## 核心结论

原MATLAB年度入口存在已证实的年份错位。`multi_prov_HANK_12sts(ii,pp)` 用 `ii+2008` 命名年度文件，却把 `data_MAT{ii}` 和 `data_year=ii` 直接传入初始化器。工作簿数据第1行是2000，所以 `ii=10` 的“2018”运行实际取第10行，即2009，而不是2018。HDF5 cache `mydata2{10}`、源码字段路径和已保存2018 runtime输入的31省向量逐位一致，全部对应2009行；该runtime JSON中的 `workbook_data_row_index=19` 元数据与实际向量矛盾。

安徽位于31省轴第12位（零基11），Excel列N。2018标签下实际消费：GDP原始/填充值 `10864.68` 亿元（GDP!N11，2009），变换后 `10864680.0`；常住人口 `6131` 万人（常住人口!N11），变换后 `613100.0`；资本存量 `228121755.48548827`（总资本存量!N11），变换后 `228121755485.48825`。对应真正2018单元格N20分别为GDP `34010.91`、常住人口 `6076`、派生资本存量 `1357314108.2013683`，变换后分别 `34010910.0`、`607600.0`、`1357314108201.3684`。

技术参数也混合年份：vintage19、行业4的alpha取R系数表最后数值B11=`0.772866243094144`并复制到31省；Zt固定使用数组第21行，即2020年GDP/CAP/POP构造。安徽保存Zt=`0.000641551386937363`。因此2018标签状态把2009水平量、vintage19共同alpha和2020水平锚定Zt组合在一起。

## 原始、填充与派生链

loader枚举14个原始sheet，范围B2:AG25；B列是全国，实际31省为C:AG。只有填充工作簿不存在时才对各矩阵执行 `fillmissing(...,'makima')` 并写出；当前文件已存在，运行时直接读取其保存值。总资本和三行业资本按 `K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)` 递推，四张资本sheet 744/744个单元与源码公式逐位一致。GDP/CAP/POP cache与填充变换744/744逐位一致；log数组仅有binary64舍入差。

总GDP 744个省年均原始未改。直接进入总量路径的常住人口有3个endpoint填充；总固定资产投资有129个原始缺失/非数值被填，其中128个属于尾端外推风险、1个内部填充。更广泛行业sheet存在大量连续缺失和endpoint填充，详见panel summary与外部10416行cell ledger。非缺失值没有被自动称为插值；机制不明的变化使用 `CHANGED_MECHANISM_UNRESOLVED`。

派生总资本出现6个负值并使MATLAB `log_pcap` 产生虚部π：上海市 2022 CAP=-1124219643872.7568; 吉林省 2023 CAP=-269548795292.80304; 上海市 2023 CAP=-5124015031628.114; 江西省 2023 CAP=-310147101039.39166; 湖南省 2023 CAP=-175916839211.5376; 新疆 2023 CAP=-119667485253.89499。这些集中在2022–2023，未直接进入本次2018标签的2009行，但证明endpoint填充与资本递推可生成经济上不可接受的派生量。

## 源文件身份与物质性异常表

- `2000年后各省数据.xlsx`: `09814A45D933B2685A35238A15C0C7BB501F00A63597796B3CADCE15C230ECB3`
- `2000年后各省数据_填充NA.xlsx`: `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929`
- `2024年数据原始版.xlsx`: `3EF3F80167AC630B0269601C88942AB6D8A7FEC769373828CD2AAC9C1C9F5C86`
- `数据估计结果_1000_100_0.mat`: `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`
- `load_GDPdata.m`: `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5`
- `It_to_Kt.m`: `4A407DE29F2DCD370932DAE35436A1B9D3C0432A360D94ABC0F78E1F94FEBE50`
- `mpHANK_equilibrium_2000.m`: `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5`
- `multi_prov_HANK_12sts.m`: `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97`
- `R语言估计结果_plm估计.xlsx`: `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68`

| 变量 | 年份/标签 | 分类 | 证据 |
|---|---:|---|---|
| GDP/CAP/POP/logs | 2018 label -> 2009 data | `YEAR_INDEX_MISALIGNMENT` | ii=10 makes filename2018 but data_year=10 selects workbook row10/calendar2009 |
| Zt/alpha | 2018 label mixes 2009 and 2020 | `MIXED_YEAR_CALIBRATION` | regression vintage19 alpha; Zt uses fixed workbook row21/calendar2020 |
| runtime input metadata | 2018 | `METADATA_VALUE_CONTRADICTION` | metadata workbook_data_row_index=19 but vectors and source paths exactly match row10 |

完整异常明细见 `reports/mp4c_2018_raw_data_audit_20260909/anomalies.csv`；该表只含定位审计所需的摘要值和源单元格引用，不含原始工作簿副本。

## 2024原始版与schema

`2024年数据原始版.xlsx` 的Sheet0按显式变量/单位/年份header与旧原始工作簿映射。13个可比变量的全部可比数值逐位一致；例如GDP 744/744一致。就业人数列为`--`，因此标记 `NOT_COMPARABLE`，没有强行合并。Sheet2是单独的年份×省份表，缺少可证明的逻辑变量header，只作schema线索，不纳入值合并。

## 质量判断与官方核验

年份错位直接改变2018标签下的GDP、人口、资本、人均量和GovInv初值，属于物质性lineage问题。元数据把实际row10写成row19，会掩盖该问题。负资本/复数log是独立的panel数据质量问题。当前证据足以停止在报告阶段，但不足以自行选择官方修正值。

`official_data_request.csv` 列出安徽2018 GDP、常住人口、2000–2018投资/资本存量链、alpha/Zt口径，以及6个负资本省年的精确人工核验请求。建议优先核对国家统计局分地区年度数据与相应省统计年鉴，并由Owner决定年份映射、资本存量构造和技术参数口径；本任务未修改任何数据或生产loader。

## 检查、证据与边界

6/6项synthetic tests通过，覆盖年份/省份映射、缺失分类、连续缺失段、单位/lineage bookkeeping和import-time零科学。MAT cache以v7.3/HDF5只读解析；旧R工作簿存在缺失drawing XML，审计器绕过无关系图形，直接从指定sheet OOXML读取缓存数值。2024 comparison摘要：8509个数值单元可比，差异0。

完整cell ledger仅存外部证据根 `D:\ProjectTemp\ch5-2018-raw-data-audit-20260909-007`，未提交原始Excel/MAT副本或可重建工作簿的大型全量值。仓库只保存源hash、契约、安徽lineage、异常摘要、官方请求、测试与manifest。由于已发现物质性问题，下一步必须等待Owner选择官方数据和修正语义；不得在本任务继续外层算法实验。
