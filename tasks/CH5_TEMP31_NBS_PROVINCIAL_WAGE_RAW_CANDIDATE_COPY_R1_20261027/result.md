# TEMP31 国家统计局声称来源工资原始候选复制回执

固定任务提交：3cc5b64d35fa0be439afb37d12dee7d52550597f
候选分支：codex/ch5-temp31-nbs-wage-raw-candidate-copy-20261027-r1
实际日期：2026-10-27（Asia/Shanghai）

已将 Owner 下载原件按原字节复制到经核验的论文工作树内隔离目录。原件及项目内副本均为 12652 字节，SHA-256 均为 8bb799fc41da5728a52c4958b2da0641ccbc81470a8d6e377625d79b5816b176；独立重新读取目的文件，确认逐字节一致。复制状态：COPIED_NEW_EXCLUSIVE_CREATE。原件未修改，没有覆盖不同内容的已有文件。

本地候选相对路径：`data/external_sources/nbs_provincial_urban_unit_wage_20261027/分省年度数据_城镇单位就业人员平均工资(元).xlsx`。
同目录已生成 `SOURCE_RECEIPT_20261027.json` 并重新读取核验；它与原始 Excel 均保留本地。GitHub 仅包含脱敏报告和哈希登记，不包含原始 Excel、工资值表、用户绝对路径或凭据。

## 原始候选资格

来源角色：OWNER_DOWNLOADED_NBS_CLAIMED。Sheet1，A1:Z36；2018 对应 I5:I35，31个工资单元。结构、31省及异常年份事实沿用固定任务单中 GPT 已独立检查的字节相同副本；执行者只做文件身份和复制回读，没有再次解析、计算或独立认证工资值。

2018 状态：2018_31_CELLS_COMPLETE__SOURCE_AND_MODEL_ELIGIBILITY_PENDING。
sector=NONPRIVATE_LIKELY__DEFINITION_PENDING。
accepted_as_raw_candidate=true；model_adopted=false。

2025及2001—2005年全部31省为字面字符串30，已在旁置回执和缺口登记中隔离，excluded_reason=ALL_31_LITERAL_30。隔离通过元数据标记实现，原始 Excel 保留全部原字节，不删除、修正或替换单元格。没有接纳其他年份，2006—2024年的结构合理性不作为年度认证。

指标代码、完整统计定义、原始导出链接、导出时间及修订vintage均为UNKNOWN。任务引用的国家统计局和福建统计局说明是定义参考，不能替代本工作簿的原始导出链接；本轮不访问或下载外部数据：
- https://www.stats.gov.cn/hd/lyzx/zxgk/202407/t20240719_1955719.html
- https://www.stats.gov.cn/hd/cjwtjd/202302/t20230207_1902273.html
- https://tjj.fujian.gov.cn/xxgk/tjxx/gzqk/201905/t20190523_4882127.htm

没有定义税后/净工资、家庭到手工资、劳动效率或工时换算，也没有将数据写入w/wjt/tau/sigma/phi或模型。共同版本、模型单位桥、生产连接和科学接受继续UNKNOWN/BLOCKED。

## 保护与交付边界

复制前后HEAD、分支、index、refs、六份治理文件及排除两个准确授权路径后的全部dirty/untracked状态指纹一致。仅授权的Excel候选与同目录旁置回执允许成为本地新增；全部旧证据、历史STOP/PENDING及其他科研状态保留。没有在科研工作树暂存、提交或推送；报告通过外置隔离Git对象库和普通权限SSH发布。

固定任务提交实际parent=c8446ea76625f4bbe574b61fbb55a5f7d2ff5e7c；任务单声明GOVERNANCE_PARENT=e6cde7e95aa808cabc6623d0e754b60c096695e3。两者分别记录，未混同；本候选从Owner固定任务提交建立。旧离线条款按固定来源工作流覆盖规则及本次Owner明确授权处理，不改写本地治理。

artifact_integrity=LOCAL_SOURCE_DESTINATION_BYTE_IDENTITY_PASS__REMOTE_REPORT_VERIFICATION_IN_DELIVERY_RECEIPTS
source_identity=OWNER_DOWNLOADED_NBS_CLAIMED__OFFICIAL_DEFINITION_AND_EXPORT_PROVENANCE_PENDING
implementation_review=COPY_ONLY
numeric_review=NOT_RUN
scientific_review=NOT_RUN
privacy_review=RAW_EXCEL_AND_PRIVATE_LOCATORS_EXCLUDED_FROM_GITHUB
actual_terminal=COPY_COMPLETE__FINAL_REMOTE_READBACK_AND_STOP_RECORDED_EXTERNALLY
delivery=SEE_DELIVERY_FINAL_RECEIPT_AND_EXTERNAL_FINAL_REMOTE_READBACK
cleanup=NOT_AUTHORIZED_NOT_PERFORMED
not_completed=DEFINITIVE_INDICATOR;EXPORT_PROVENANCE;COMMON_VINTAGE;MODEL_ELIGIBILITY;INDEPENDENT_ACCEPTANCE

科研、测试、预检、模型、HA/HJB/KFE/GE/IRF、正式科研源码修改和外部数据下载预算使用均为0。
V010=UNCHANGED；V011=NOT_STARTED；Results=FALSE；FORMAL_SOURCE_FREEZE=FALSE。
候选交付和远端回读完成后STOP，不自动合并、清理或启动下一任务。执行者不自认独立验收。
