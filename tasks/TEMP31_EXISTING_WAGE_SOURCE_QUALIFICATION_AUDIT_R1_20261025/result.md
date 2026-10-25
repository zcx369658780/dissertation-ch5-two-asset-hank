# TEMP31 既有工资来源资格与官方可用性审计

任务提交：f4ffac5c7c270ad79b00cadaf5091873daec1ca5
治理父提交：9fb8ed823e11234a531aee5b45be0504840cb2dc
候选分支：codex/temp31-wage-source-qualification-20261025-r1
实际检索日期：2026-10-26（Asia/Shanghai）
actual_terminal=SOURCE_QUALIFICATION_COMPLETE__SEE_FINAL_DELIVERY_RECEIPTS

## 结论

现有来源可以分级，但完整可比31省工资来源覆盖仍未建立。本轮未构造、填补、插值或交付工资值面板，也未定义净工资转换。

先审计既有台账的28个数值记录（私营12、非私营16）：7个记录有哈希匹配的统计局原始缓存；6个只引统计局来源、原件未定位；2个为后年年鉴历史行、版次和表待核；13个为政府/新闻/公共机构转载或非首发。后期严格O层仍只保留7个工资单元（私营3、非私营4）；单位通过或文件名“verified”不替代原件资格。本轮没有因新检索自动改写任何旧表或接受旧数值。S08/S09数值填补均为0。

31省×2类别的可用性矩阵是来源元数据，不含工资值。分类数量：
{
  "UNKNOWN": 5,
  "NOT_FOUND_IN_BOUNDED_SEARCH": 28,
  "OFFICIAL_CATALOG_ONLY": 7,
  "FOUND_OFFICIAL_ORIGINAL": 9,
  "OFFICIAL_PAGE_UNAVAILABLE": 13
}

这9个FOUND单元仅表示当前官方统计局/年鉴表或正文确实可读，不证明其数值、总体、版本已全部独立验收。7个目录单元的具体目标数据仍未读取；不可用、UNKNOWN和有界未找到也不是“官方数据不存在”。北京政府门户明确署统计局来源且正文可读，但首发原件路径未独立核实，因此保守列UNKNOWN，不混入直接局站FOUND。

## 国家来源与具体省级路线

- [国家统计局2018私营工资发布](https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900312.html)：表1实际只有东、中、西、东北四大区域，不是31省。附注明确单位就业人员及税前工资概念。非私营同年发布原页本轮超时，未把摘要当完整表读取。
- [中国统计年鉴2019目录](https://www.stats.gov.cn/sj/ndsj/2019/left.htm)：第4章列工资表，但本轮没有建立该目录提供31省两类别完整表的证据。另找到的旧“从业人员和职工工资”说明版次未定，不能冒充2018来源。
- [吉林2019年鉴表4-7](https://tjj.jl.gov.cn/tjsj/tjnj/2019/2019/B4_7.htm)和吉林2018私营发布均实际打开。表内就业人员与在岗职工列不能混用。
- [江苏2019年鉴表3-25](https://tj.jiangsu.gov.cn/2019/nj03/nj0325.htm)与[表3-29](https://tj.jiangsu.gov.cn/2019/nj03/nj0329.htm)均实际打开，分别为2018非私营及含2018列的私营工资。这比既有S04引用的2024年鉴历史列提供了更接近观测年的官方路线，但没有替换或复核成新数值面板。
- 上海2018发布、福建两类别2018发布、湖南非私营2018发布实际可读；具体URL、题名、表号/段落、单位及口径均见source_inventory.json。上海明确提示新旧工资指标不可比；福建就业人员、在岗职工和含劳务派遣工口径不得互换。
- 辽宁2019年鉴ZIP、黑龙江2019年鉴ZIP、湖北2019年鉴RAR目录/附件链接已核到，未下载。仅目录是目录，不是表数据可用证明。浙江2020目录的5-4历史系列包含2018年份，但未读取2018行；2019编辑说明只能证明版次存在。
- 湖南私营页不可读、重庆页超时、云南页405、新疆历史表404、海南页403、广东/广西/宁夏目录超时均保留，没有重试被拒页面、绕过控制或改用凭据。内蒙古等有界未找到项保留原状，不用其他省、市、年份或工资概念替代。

## 口径与版本风险

统计工资多为税前口径，包含代扣个人税费等，不能直接当家庭到手净工资或企业单位有效劳动工资。年平均就业人员工资不是年末人数分母、在岗职工工资、全口径社保基数、居民工资性收入或规模以上企业岗位工资。

观测年2018、发布年份、年鉴版次、URL迁移日期和修订版本分别记录，不按URL路径认定vintage。福建私营2018页附注明列GB/T4754-2011，国家同年私营发布注明GB/T4754-2017；差异保留，未擅自纠正或认定完全可比。共同价格基准、工时/效率/就业权重、生产wjt/tau/sigma/phi连接和callback/snapshot仍UNKNOWN/BLOCKED。

## Owner 决策材料

提供procurement_specification.md作为条件性后备，不采购、不接洽、不索样。本轮不能证明必须商业采购；应先由Owner决定是否允许读取/获取已定位的具体免费官方附件和补足表级证据。未找到目标表号的省份明确写UNKNOWN，未捏造版次、ISBN、页码、价格或数据可用性。

## 执行与接受边界

81个官方域限定查询及其检索词、日期、限制见search_coverage.json。网页工具年鉴链接定位曾失败；仅读取官方目录href元数据后确认江苏两表真实地址。没有保存新数据附件或原始网页数据文件。新网页原字节SHA保持UNKNOWN_NOT_DOWNLOADED；报告本身的大小/Blob/SHA在manifest及回读中核验，不混作新来源原字节证明。

artifact_integrity=REPORT_PAYLOAD_SEALED__REMOTE_READBACK_IN_DELIVERY_RECEIPTS
source_identity=BOUNDED_SOURCE_CLASSES_AND_AVAILABILITY_RECORDED__FULL_COMPARABILITY_NOT_ESTABLISHED
numeric_review=NOT_RUN
implementation_review=SOURCE_QUALIFICATION_ONLY
scientific_review=NOT_RUN
privacy_review=METADATA_AND_NECESSARY_PUBLIC_SOURCE_TITLES_ONLY
delivery=SEE_DELIVERY_FINAL_RECEIPT_AND_EXTERNAL_FINAL_READBACK
cleanup=NOT_AUTHORIZED_NOT_PERFORMED
not_completed=FULL_COMPARABLE_PANEL;UNREAD_TABLES_ARCHIVES;COMMON_VINTAGE;MODEL_WAGE_BRIDGE;PRODUCTION_JOIN_CALLBACK;INDEPENDENT_ACCEPTANCE
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

原科研工作树、dirty/untracked、index/refs及旧证据保持；本轮只向外置对象库生成和发布任务目录报告。完成候选交付与远端回读后STOP。
