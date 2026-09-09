# Chapter 5 MP4C 年度时间合同与 Zt legacy 审计报告

- Temporal-contract verdict: `CONFIRMED_LEVEL_INDEX_DEFECT__OWNER_EXPANDING_WINDOW_NOT_IMPLEMENTED_BY_SAVED_PLM_ARTIFACT`。
- PLM preservation verdict: `PRESERVE_PLM_ESTIMATOR__VINTAGE_END_YEAR_ALIGNED__COEFFICIENT_ARTIFACT_REBUILD_REQUIRED`。
- Zt legacy verdict: `LIKELY_LEGACY_FIXED_YEAR_ANCHOR`。
- Results eligibility: `FALSE`。
- MATLAB、HJB/KFE/household、firm/controller、GE/annual/stationary/IRF/Results及root/direct/iterative/eigen/model solve调用均为0。

## 结论

`steady_year = 2008 + ii` 同时得到年度文件名、源码2024-06-01注释和PLM sheet vintage支持。工作簿水平数据从2000开始，因此稳态同年水平量应使用矩阵一基行 `ii+9`。生产入口仍把 `data_year=ii` 传入初始化器；该初始化器据此读取GDP、CAP、POP及人均量。因此这是 `A_CONFIRMED_INDEX_DEFECT`。`data_MAT{ii}` 应继续保留，因为它选择以该稳态年为end-year的PLM/cache entry；最小修复是单独把水平量行改为 `ii+9`。

PLM estimator继续冻结保留。15个vintage（10–24）、4个行业的系数与截距sheet共120张全部存在，vintage end-year与2009–2023年度序列一致。可是全部60张系数sheet都只有 `time1` 至 `time9`，加上源码“前10年的数据估计本年alpha”注释，支持固定10期滚动窗。首个vintage10与Owner的2000–2009窗口一致；vintage19更像2009–2018，而不是2000–2018扩展窗。Owner已冻结2000起始扩展窗意图，因此现存PLM artifact不符合该合同。后续独立任务需找回/冻结R估计源，并在不切换PLM estimator的前提下重建版本化系数artifact。

`load_GDPdata.m` 将所有15个cache entry的Zt固定用矩阵row21/calendar2020构造。源码注释只说明“用2020年的pgdp和pcap”，没有给出base-year、normalization或经济锚定理由；搜索到的其他regression branches也没有为固定2020提供依据。因此分类为 `LIKELY_LEGACY_FIXED_YEAR_ANCHOR`，而非`PROVEN_BUG`。保存cache的465个industry4 Zt中384个与row21公式逐位相等，全部差异最大仅 `1.3877787807814457e-17`，说明其余只是binary64运算次序舍入。

另有cache身份问题：industry4的ii1–ii14 alpha与当前PLM sheet逐位一致，但ii15 cache alpha=`0.967775174774325`，当前vintage24 sheet B11=`1.0219847778591`；PLM workbook修改时间晚于cache。旧cache文件名没有数据/时间合同版本，不能证明2023 entry与当前workbook来自同一PLM artifact。

## ii=1与ii=10

- ii=1：steady/filename year=`2009`；PLM vintage10、sheet `总面板回归系数_10_行业4`；现有布局支持2000–2009十期窗；当前水平row1/year2000，候选row10/year2009；当前Zt row21/year2020，候选row10/year2009。
- ii=10：steady/filename year=`2018`；PLM vintage19、sheet `总面板回归系数_19_行业4`；现有布局支持2009–2018十期窗，不能证明2000–2018扩展窗；当前水平row10/year2009，候选row19/year2018；当前Zt row21/year2020，候选row19/year2018。对31个有效省份，候选Zt相对保存Zt的绝对相对变化中位数 `0.09022142928075905`、最大 `4.672582203960288`，仅作静态算术，不是模型结果。

## 全部支持年度映射

| ii | steady/filename year | PLM vintage | workbook支持的10期窗 | 当前level row/year | 候选level row/year | 当前Zt row/year | 候选Zt row/year | PLM窗口状态 |
|---:|---:|---:|---|---|---|---|---|---|
| 1 | 2009 | 10 | 2000–2009 | 1/2000 | 10/2009 | 21/2020 | 10/2009 | `ALIGNED_FIRST_2000_2009_WINDOW` |
| 2 | 2010 | 11 | 2001–2010 | 2/2001 | 11/2010 | 21/2020 | 11/2010 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 3 | 2011 | 12 | 2002–2011 | 3/2002 | 12/2011 | 21/2020 | 12/2011 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 4 | 2012 | 13 | 2003–2012 | 4/2003 | 13/2012 | 21/2020 | 13/2012 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 5 | 2013 | 14 | 2004–2013 | 5/2004 | 14/2013 | 21/2020 | 14/2013 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 6 | 2014 | 15 | 2005–2014 | 6/2005 | 15/2014 | 21/2020 | 15/2014 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 7 | 2015 | 16 | 2006–2015 | 7/2006 | 16/2015 | 21/2020 | 16/2015 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 8 | 2016 | 17 | 2007–2016 | 8/2007 | 17/2016 | 21/2020 | 17/2016 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 9 | 2017 | 18 | 2008–2017 | 9/2008 | 18/2017 | 21/2020 | 18/2017 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 10 | 2018 | 19 | 2009–2018 | 10/2009 | 19/2018 | 21/2020 | 19/2018 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 11 | 2019 | 20 | 2010–2019 | 11/2010 | 20/2019 | 21/2020 | 20/2019 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 12 | 2020 | 21 | 2011–2020 | 12/2011 | 21/2020 | 21/2020 | 21/2020 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 13 | 2021 | 22 | 2012–2021 | 13/2012 | 22/2021 | 21/2020 | 22/2021 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 14 | 2022 | 23 | 2013–2022 | 14/2013 | 23/2022 | 21/2020 | 23/2022 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |
| 15 | 2023 | 24 | 2014–2023 | 15/2014 | 24/2023 | 21/2020 | 24/2023 | `END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000` |

2020对应ii12，因此只有该年固定Zt row21恰好与候选同年。候选2022 Zt遇到非正资本省份 `上海市`；候选2023遇到 `吉林省, 上海市, 江西省, 湖南省, 新疆`。这些来自前序已接受的六个负资本单元，属于D类独立数据质量问题，必须先经官方/Owner数据处理，不能用时间索引修复掩盖。

## 最小source patch plan（未执行）

| 类别 | 文件/位置 | 当前表达式 | 候选表达式 | 保留的经济含义 |
|---|---|---|---|---|
| `A_CONFIRMED_INDEX_DEFECT` | `multi_prov_HANK_12sts.m` | `mpHANK_equilibrium_2000(..., data_MAT{ii}, 4, ii)` | `level_row = ii + 9; mpHANK_equilibrium_2000(..., data_MAT{ii}, 4, level_row)` | keep PLM-vintage cache entry ii; select GDP/CAP/POP levels for steady_year |
| `PLM_ARTIFACT_ALIGNMENT` | `R PLM generation source/workbook (future authorized task)` | `all coefficient vintages retain time1..time9, supporting fixed ten-period windows` | `retain PLM estimator; regenerate versioned coefficients on 2000:steady_year expanding samples` | implement the Owner-approved expanding-window contract without switching estimators |
| `B_LIKELY_LEGACY_ZT_ANCHOR` | `load_GDPdata.m` | `Zt_new = GDP{j}(21,col)*CAP{j}(21,col)^(-alpha)*POP{j}(21,col)^(alpha-1)` | `level_row = ii + 9; use GDP/CAP/POP at level_row in the unchanged formula` | align the level-implied technology index with the PLM vintage end year |
| `CACHE_IDENTITY` | `load_GDPdata.m` | `数据估计结果_{GDP multiplier}_{POP multiplier}_{reg_method}.mat` | `use a new explicit temporal-contract cache version and refuse old unversioned cache` | prevent corrected source from silently loading stale row21 Zt |
| `OUTPUT_IDENTITY` | `multi_prov_HANK_12sts.m` | `Multi_Province_12sts_{steady_year}.mat` | `retain calendar filename but add temporal-contract metadata and reject stale files without it` | filename is already calendar-consistent; metadata proves actual rows and vintages |
| `METADATA_CONTRACT` | `annual/cache serialization path` | `no authoritative row/vintage assertions; prior runtime metadata claimed row19 while bytes used row10` | `persist and assert steady_year, level_row/year, PLM vintage, sample start/end/window type, Zt row/year, contract version` | make labels and consumed arrays mechanically auditable |

稳定态输出文件名 `Multi_Province_12sts_{steady_year}.mat` 已按calendar year命名，可保留；但旧输出必须用contract metadata拒绝误读。cache名称必须增加明确版本或身份，否则生产代码会直接加载旧row21 Zt并绕过修正构造。metadata至少保存并断言 `steady_year`、level row/year、PLM vintage、sample start/end/window type、Zt row/year和temporal-contract version。

## 仍需Owner或官方数据决定

1. PLM窗口含义无需再次选择：Owner已定为2000起始扩展窗。当前缺口是R生成源和符合该合同的版本化PLM coefficient artifact；后续仍用PLM重建，不切换估计器。
2. Owner需接受或拒绝将Zt水平行从固定2020改为 `ii+9`。本报告推荐接受，但只给规格，不实施。
3. ii15/industry4需确定当前PLM workbook还是旧cache系数为权威；推荐新合同采用显式版本cache，禁止静默混用。
4. 安徽2018 GDP、常住人口、固定投资/资本链及alpha/Zt provenance仍按前序 `official_data_request.csv` 待核验。
5. 2022–2023六个负资本/复数log单元是独立问题；时间对齐会使其进入对应年度Zt候选，执行前必须关闭。

## 来源身份、检查和边界

- `load_GDPdata.m`: `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5`
- `multi_prov_HANK_12sts.m`: `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97`
- `mpHANK_equilibrium_2000.m`: `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5`
- `R语言估计结果_plm估计.xlsx`: `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68`
- `数据估计结果_1000_100_0.mat`: `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`
- `2000年后各省数据_填充NA.xlsx`: `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929`
- `CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT_REPORT.md`: `993F9A79BE58FE6ADBC3CF624C748FFD48DF3AD988BB13E58D764C60AC43A3E4`
- `CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT_ACCEPTANCE.md`: `3E69E7D29C25E88B6062F045F03A9B30115E216074F475A86589D38510AC0E75`
- `data_contract.json`: `AE6CAA4FF5565658D4952A561C7510F58596A9A9E09D0599236C8BED2D2A7DB1`
- `cache_audit.json`: `D3C88A5C056A6D0618838678270CA2FD4379A34C49CF830341F6192741755304`
- `anhui_2018_lineage.csv`: `B17AA92B56F52DB294740BC64BB1DA649DCA05D8EAD2E38748E83B348EFF5390`
- `official_data_request.csv`: `4DE660AD41AD379D3F5754AB1D7B2D5F82EC56AD4ABB9A77BB08A25A6FE09AA9`

6/6项synthetic tests通过，覆盖ii1/ii10映射、全部PLM sheet命名、固定10期layout分类、Zt静态算术和import-time零科学。完整静态证据根为 `D:\ProjectTemp\ch5-temporal-contract-audit-20260909-003`；`-001`因过强cache-alpha断言停止，`-002`在最终authority措辞收紧前完成，两者均保留不覆盖且科学调用为0。manifest/readback、测试原始日志与机器可读mapping/patch plan位于 `reports/mp4c_temporal_contract_audit_20260909/`。
