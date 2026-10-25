# TEMP31 既有工资数据发现报告

任务：CH5_TEMP31_EXISTING_WAGE_DATA_DISCOVERY_R1_20261025
固定任务提交：7349f9bc381b9d8cb7c24e175de101324dce259f
候选分支：codex/ch5-temp31-wage-data-discovery-20261025-r1

actual_terminal=DISCOVERY_COMPLETE__SEE_FINAL_DELIVERY_RECEIPT
本轮找回了有充分身份依据的历史输入、部分工资观测及映射；没有建立完整、当前、已采纳的 31 省净工资数据集。

## 最强候选与证据边界

1. 历史模型输入 S19：calendar_2009_primary_premodel_input.json，36,263 字节，SHA-256 507d1259a8a515e4224f40d434bd89645c02472650b51f5ada3181ba4bcdad48。与历史 MP4B 输入绑定任务的第 91–99 行明确记录完全一致。本轮只读核对现存原字节，没有重建或改写它。schema 为 CH5_MP4A2_CANONICAL_ANNUAL_INPUT_V1；binding.calendar_year=2009，另明确保留 fixed_zt_calendar_year=2020。三个工资/税字段 scalars.composite_wage、scalars.wjt、scalars.wage_tax 都是单个标量，并有 31 省显式顺序。当前 loader 第 101–121 行把这些共同标量赋给各省状态，见 loader_excerpt.md。找到这个历史输入不等于找到 31 个现实工资观测，也不证明它是当前 2018 TEMP31 的净工资来源、同快照输入或正式来源。标量生成链与经济单位仍 UNKNOWN。

2. 后期严格 O 层表 S03：wage_employment_2018_observed_31.csv，SHA-256 e51a4b38503df6701beea4456bedb0cde8bf97ecfdc36f08fc74c03d6ce3bf9d。year/layer/model_adopted 明确为 2018/O/False。31 行只有私营工资 3 省（福建、湖南、重庆）、非私营工资 4 省（再加云南），共 7 个工资单元。此前“10 个 O 单元”还含 2 个人口和 1 个年末就业单元，不能解读为 10 省工资或完整面板。匹配工资总体的年度平均就业权重及工作地/居民地就业字段均无数值。

3. 前期带资格标记的部分表 S04：wage_employment_2018_31_verified.csv，SHA-256 bda2d8b3a939f5d4c3f812c6a65dd0c31ef68693770bcbc48e5d47651c4cd1cb。保留私营 12、非私营 16 个数值，但混有原件、摘录与范围未决等资格，文件名 verified 不代表整体通过。S03 是后续更严格筛选，不能把两个表的数值数量直接视为同等来源覆盖。缺失标记和资格字符串不计为数值。S08/S09 的工资数值均为 0 个，model_adopted=False，不能宣称已完成插值或情景数据。

4. 六份既有官方原网页缓存：CQ_W、FJ_P、FJ_NP、HN_P、HN_NP、YN_NP。均实际定位到本地原文件，六件长度与 SHA-256 全部匹配此前 provenance 台账；2018 观测对应 2019 年 5–6 月发布。没有访问这些外网站点。原始网页不上传。FJ_P:601、FJ_NP:1431、HN_NP:188、YN_NP:1075 的短定义明确工资总额为税前工资，含代扣代缴个人所得税、社保、公积金等；不能把这些平均年工资当作模型净工资。来源 URL、单位/总体/时点元数据和必要短引文见 official_source_evidence.json。历史 containing-ZIP Blob 与当前 HTML 的 SHA-256 分开记录；本轮不冒称重新验收该历史 ZIP 或旧科学结论。

5. canonical 宏观工作簿 S01：CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx，224,020 字节，SHA-256 aea5a12b5e6474056c1c3ef84bf0156ba88442ef54b0a4fb9c4c6f33ca963f67。12 个 sheet 及已读表头是 GDP、人口、投资、资本、alpha、Zt 等；在这些表头未识别到工资观测字段。S02 canonical_data.json 是另一宏观导出，SHA-256 c5a3ca72939f7b46229b3be258d1b407c37dd07f8cd677e2d04ad67ce409adc5，不能与 507d 历史模型输入混同。旧原始/填充工作簿、2024 重排工作簿、稳态导出分别登记；有界表头和 sharedStrings 标签搜索不构成全盘“没有工资数据”的证明。

## 省份映射

S01 的 PROVINCE_ORDER!A1:D32 明确给出 31 省名称、MATLAB 1-based、Python 0-based 及源 Excel 列。S19 和四份 CSV 的显式名称列表均与该映射相同，31 个名称唯一。这里核对的是名称，未用行位置猜省份身份。该结果支持这些文件的名称连接；没有国家行政区代码字段，也不能据此证明真实生产 wjt/tau/sigma/phi 张量已正确接线。映射元数据见 province_mapping.json。

## 覆盖、保护与未完成项

31 件相关来源有身份记录。文件大小和 SHA-256 为本轮实际读取；tracked 项另列 HEAD/index 身份，未跟踪外部原件不伪造 Git commit/Blob。表头、schema、单元格/行号、范围、来源链与缺口均单列交付。真实工资数值行、原始工作簿、原 HTML、科学归档和私有绝对路径留在本地，仅上传脱敏元数据及短定义引文。

未解决：完整 31 省工资面板、历史标量的现实定义与单位、当前净工资生成链、共同 vintage、生产 ID/数组连接、匹配工时/效率和就业权重、共同税基/快照、生产 callback、独立科学验收。旧审计和 STOP/PENDING 不改写；本轮发现可以补充来源身份，不能追溯提升原审计覆盖。

artifact_integrity=REPORT_BYTES_SEALED__REMOTE_READBACK_IN_DELIVERY_RECEIPTS
source_identity=HISTORICAL_INPUT_AND_SELECTED_SOURCES_IDENTIFIED__CURRENT_NET_WAGE_BLOCKED
numeric_review=NOT_RUN
implementation_review=DISCOVERY_ONLY
scientific_review=NOT_RUN
privacy_review=METADATA_AND_SHORT_DEFINITION_QUOTES_ONLY__NO_RAW_SENSITIVE_DATA
delivery=SEE_DELIVERY_FINAL_RECEIPT_AND_EXTERNAL_FINAL_READBACK
cleanup=NOT_AUTHORIZED_NOT_PERFORMED
not_completed=FULL_31_NET_WAGE_PANEL; UNITS; COMMON_VINTAGE; PRODUCTION_JOIN; CALLBACK; SCIENTIFIC_ACCEPTANCE
INDEPENDENT_COMPLETION_EVENT=UNKNOWN

SCIENCE_BUDGET_USED=0
TEST_BUDGET_USED=0
PREFLIGHT_BUDGET_USED=0
MODEL_CALLS=0
FORMAL_SOURCE_WRITES=0
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
FORMAL_SOURCE_FREEZE=FALSE
AUTO_NEXT=FALSE

来源工作树的 branch/HEAD/index/refs、治理文件和全部 dirty/untracked 状态在读取前、发布前及最终回读后核对。没有暂存、提交或推送其工作树改动。候选仅发布外置隔离 Git 对象库中本轮生成的报告；回读完成后立即 STOP。

