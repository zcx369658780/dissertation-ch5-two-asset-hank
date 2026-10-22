# TEMP31 2018工资与就业人口来源审计｜正式冻结合同
TASK_ID=CH5_TEMP31_2018_NBS_WAGE_EMPLOYMENT_PROVENANCE_GATE_20261022
REVISION=ISSUED_20261022_R1
OWNER_APPROVED=2026-10-22__2018_OFFICIAL_WAGES_AND_EMPLOYMENT
STATUS=SOURCE_ONLY_NO_HA
FIXED_GOVERNANCE_BASELINE=7d0b6b43604b70bbaccd64dca9549836dee6234b
REVIEW_BRANCH=review/ch5-temp31-wage-employed-2018-20261022
REVIEW_FIXED_PARENT=7d0b6b43604b70bbaccd64dca9549836dee6234b
REVIEW_TEMP_PATH=_review_tmp/ch5/temp31-wage-employed-2018-20261022/

## A. 研究范围
Owner批准优先收集国家统计局、2019版《中国统计年鉴》及省级统计局的2018年31省私营/非私营单位税前年平均工资与对应就业人数。企业劳动投入未来优先按实际就业人口×效率构造，不能把原家庭N全局直接替换成就业人数。单列常住人口N_resident、全社会就业N_employed、城镇就业N_urban、工资统计覆盖N_wage_covered，以及来源/目的地与年末/年度平均口径。不得将同年非私营单位就业人员冒充全社会就业人员，且2018省级总就业数据应明确旧口径可比限制。
本轮不修改任何正式V010模型源、HA网格、工资上限或HU数值。HA/HJB/KFE/roots/science_driver/outer/GE/IRF全部0次，Results=FALSE、V011=NOT_STARTED。前次无HA结构32/32与符号32/32仅是Codex报告，因无公开原件不授独立PASS。

## B. 2018官方数据真实性
31省顺序严格为北京、天津、河北、山西、内蒙古、辽宁、吉林、黑龙江、上海、江苏、浙江、安徽、福建、江西、山东、河南、湖北、湖南、广东、广西、海南、重庆、四川、贵州、云南、西藏、陕西、甘肃、青海、宁夏、新疆。两套单位年均税前工资分别记录，不能未经同口径就业权重合并。必须优先找国家统计局/地方统计局官方原表、页码、表号、机构、URL、2018取值、年末或年平均、统计范围；西藏不得遗漏、陕西/西藏错位严拒，无法逐项证明写MISSING_OFFICIAL_SOURCE，不能用论坛转载/区域均值/别年工资填空。
全国校验点2018非私营年均工资82461元、私营49575元、年末全国就业77586万人、城镇就业43419万人，均是独立口径，不替代31省数值。官方来源：
https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900311.html
https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900312.html
https://www.stats.gov.cn/xxgk/sjfb/tjgb2020/201902/t20190228_1768642.html
2018地区就业资料不要机械和2020之后统一测算序列混用：
https://www.stats.gov.cn/hd/lyzx/zxgk/202508/t20250807_1960621.html
https://www.stats.gov.cn/hd/lyzx/zxgk/202408/t20240829_1956132.html
https://www.stats.gov.cn/hd/lyzx/zxgk/202407/t20240719_1955719.html

## C. 量纲与劳动人口映射
来源货币MU=10万元、人口NU=100人，工资yuan/person/year换到MU/NU/year时除以1000。家庭HU工资数参考仅可写w_HU=(w_yuan/1000)/s_H，其中先前s_H_GDPpc=64.8906755511是未经Owner采纳的Codex候选。工资统计均值不等于单位有效劳动工资、不等于税后家庭收入；需要明确效率、劳动时间、就业地/居住地迁移和工资覆盖范围后才能建立模型桥。不得随意把resident乘数全部改为employed乘数，不设asset_bridge或a_max、b_min，不能用工资来直接反推企业wjt上下界。
家庭/企业备选路径作为E3讨论列账：保留家户总人口和家庭资产归属，企业用就业人口和劳动效率；或让家户代表就业者并另处理无工作者、家庭成员、转移支付/资产持有。均须Owner之后单独授权。

## D. 交付
至少输出wage_employment_2018_31.csv、wage_source_ledger.csv、employment_scope_matrix.csv、wage_coverage_summary.md、source_urls_verified.md、first_error_and_budget.json；31行数据加来源表，不许未查页面编造成PASS。公开证据含实际来源和逐项条目，私人原2018规范工作簿只可精确验证必要字段且不上传。
wall<=7200秒，official_source_page_fetch<=150，Python starts<=16，direct starts<=60，E1<=2批，文件总<=64MiB，公开ZIP展开<=8MiB/成员<=32；旧科学/工程预算均不继承。新隔离scratch必须先有合法可信父目录和写前源身份门，禁止污染原dirty工作树、Git common-dir及C盘备份。
Codex自动GitHub独立Review分支只发布result.md、manifest.json、evidence_sanitized.zip，Review唯一parent为本合同FIXED_PARENT，非force；原字节、Blob、长度SHA256及ZIP每成员CRC/SHA/隐私完整回读，正式发行后才允许执行。遇平台/账号/工具安全拒绝立即STOP，不换账号、授权或传输渠道绕过。已有三个历史PENDING候选必须保留，不自动删除。
最终到WAIT_ASTRA_AND_OWNER_WAGE_EMPLOYMENT_DISCUSSION，不能自动继续HA或调参。