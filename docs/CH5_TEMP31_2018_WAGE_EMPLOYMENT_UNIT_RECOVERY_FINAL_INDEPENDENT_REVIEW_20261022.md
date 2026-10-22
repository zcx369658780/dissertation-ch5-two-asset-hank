# CH5 TEMP31 · 2018工资就业来源值单位归一化续审｜2026-10-22 Astra独立终审
TASK_ID=CH5_TEMP31_2018_WAGE_EMPLOYMENT_UNIT_NORMALIZED_RECOVERY_20261022
RUN_ID=1f540705a35e4212b5fe61951c74493b
CODEX_ACTUAL_TERMINAL=STOP_E1_EXHAUSTED_SOURCE_REQUEST_LEDGER_ASSERTION
TASK_OVERALL=NOT_PASS
ASTRA_REVIEW=PASS_BOUNDED_EVIDENCE_AND_UNIT_TEST_ORACLES__NOT_PASS_DATA_PIPELINE
ZIP_MEMBER_INTEGRITY=26_OF_26_PASS
UNIT_ORACLE_RECALCULATION=258_OF_258_EXPECTED_MATCH
COMPLETE_31_PROVINCE_PANEL=0_OF_31
RESULTS=FALSE
REVIEW_CANDIDATE=e9eb6a0d131bc8046af61d95892b2aa45e5740d8
REVIEW_BRANCH=review/ch5-temp31-wage-employed-unit-recovery-20261022
REVIEW_FIXED_PARENT=f3e2e1bb148c001c714db7ae42072d7f820e1aed
REVIEW_TREE=89915a69c4653ac0540826cf4d29eb33a554c03c
CLEANUP=ONLY_AFTER_FORMAL_ARCHIVE_REMOTE_READBACK

## 1. GitHub identity and original bytes
Candidate `e9eb6a0d131bc8046af61d95892b2aa45e5740d8`唯一parent`f3e2e1bb148c001c714db7ae42072d7f820e1aed`，tree`89915a69c4653ac0540826cf4d29eb33a554c03c`；同固定parent比较 ahead1/behind0，仅新增`_review_tmp/ch5/temp31-wage-employed-unit-recovery-20261022/result.md`、`manifest.json`、`evidence_sanitized.zip`三指定文件，review branch exact identical。
Owner上传的三原件真实 SHA256/Git Blob 经标准库独立复算，与GitHub候选provider Git Blob一致：
- result.md 15454B，SHA256 `7ef1ff28f7da316d648420952df368c0b34e8a453b6593f2098ed722beba3b88`，Git Blob `2fe57d4dc1528564d996716e94cf596b54062317`；
- manifest.json 10449B，SHA256 `a44176d202c098dbc3c3095d28526d7eb6a8b0bc9b7e0d0746e69a46638c4b2b`，Git Blob `86c443c067e41270554d9e557b65516934a336d4`；
- evidence_sanitized.zip 220081B，SHA256 `14746e539ce792189dc85d207ec148e97bad27f8101a4c598c475d49a05008fc`，Git Blob `87b3173fc12f4ec3bec34dbde785f27ad627e37f`。
ZIP 26/26 member CRC32+原字节长度+SHA256与manifest一致；展开1121717B，testzip无错误，不发生ZIP成员名重名/穿越；公开仅有限常见token/私钥头模式扫描，无命中（非穷尽性保证）。独立机器核验会话工件 `CH5_TEMP31_WAGE_UNIT_RECOVERY_INDEPENDENT_AUDIT_20261022.json`，SHA256 `e5647619e55d602dce9892be826feb9943d0c7e3ccc68aa55552bfab1f7f0698`；此工件存当前会话sandbox，不假称已入GitHub。

## 2. 258项数学测试真义及数据资格
`unit_validator_tests.json` 258条每条`expected==actual`、`passed=True`；Astra使用独立Python Decimal方法对已提交所有case的单位转换、年份/省份/统计范围/时间/地理类型和原值比较再次计算，258/258分类一致。其中63条预期`PASS_UNIT_AND_SCOPE_MATCH`，其余195条预期为拒绝/不可判定类，均符合预期。**这是对已封存的测试向量与源算法语义的独立计算，不是重新执行Codex Windows全工作流，也不能证明源站数值真实。**
吉林`2793233人/10000=279.3233万人`正例PASS；少1人负例VALUE_CONFLICT，统计标签仍2018年末`URBAN_NONPRIVATE_UNIT_EMPLOYED`；不可将其当2018年私营+非私营工资年度平均权重。
省级主表确有31个不同省，皆2018、31/31`panel_qualification=INCOMPLETE_NOT_ADOPTED`。较前次新天津2018年末就业：总896.56万人、城镇714.21万人，geographic_basis仍UNKNOWN，不授企业劳动工作地映射。数据`source_value_normalization_ledger.csv` 219行=31×7字段+2条新增，Astra独立统计：
- `PASS_UNIT_AND_SCOPE_MATCH`:20；
- `VALUE_UNIT_SCOPE_MATCH__EXTRACT_ONLY`:11；
- `INDETERMINATE_GEOGRAPHIC_BASIS`:15；
- `INDETERMINATE_TIME_TYPE`:12；
- `VALUE_UNIT_MATCH__SOURCE_CLASS_NOT_PRIMARY`:2；
- `MISSING_OFFICIAL_SOURCE`:159。
前述类型是局部来源检查等级，不等于31省真实数据通过。工资私营12/31观察、非私营16/31，总就业14/31、城镇8/31，私营工资调查同范围年度平均人数0/31，非私营单位覆盖人数6/31（多为年末框架或时点未知），不可使用不同总体人数机械合并两种工资，也不能将N_resident全局替换为N_employed。上海140270/140400、浙江/辽宁原来源轴与口径、新疆后年回溯摘录及甘肃转载等级仍有缺口，不得悄然填零。

## 3. 计账断言失败独立归因
失败`build_delivery.py`第71行 `assert request_count==58,(request_count,len(web),len(new))`，实际构建器返回`(50,47,5)`。审原始`build_delivery.py`第55/64行可见它依`args.get('system2_search_query',args.get('open',[]))`计入已保存网页调用，但2份批量检索入口在来源回执中以另一层`request`保存，造成批量查询各4条被计为0；其余45条单请求正确计为45，加5原站=50。Astra独立按47份public discovery receipts观察到2次×4条批查询+45次×1条=53条web查询/打开，另有5次原站请求，总数58。故这是**来源计账解析器与控制器语义不一致，漏记8次**，不是实际58/120超限、或发现真实不可修来源。
原E1恢复3/3全部已消耗，Codex正确记录STOP，禁止按Astra独立理解倒改实际运行终态；未修复重跑整条来源链。实际资源用户报告：官方来源请求58/120，Python14/22，direct44/100，Git API写6/8；包内prepublication快照为Python13/direct34/Git0，时点不同不可当不一致。用户本地完整最终JSON19073B/SHA256`dffa09b8f5ed95bc61d168760673911b09329e5dc819dfab8a74bd2df3226eab`仅报告，没有该本地原字节与控制器完成事件的独立复演。

## 4. 当前科研终局及后续Owner门
当前仅`PASS_BOUNDED_EVIDENCE_AND_258_UNIT_ORACLES`，**整体TASK=NOT_PASS、源值交付流水线=NOT_PASS、31省数据不获完整采用**。HA/HJB/KFE/roots/science driver/outer/GE/IRF均Codex报告0；正式V010、Results FALSE、V011 NOT_STARTED、production GLOBAL_STOP UNVERIFIED、家庭HU基准E3待决。
若Owner未来批准新SOURCE_ONLY任务，应先明确统一source_request事件口径并修builder计数（按每条实际query/open +每个原站请求，保留同query批记录、原始错误/对账ledger），只恢复已完成数据证据的交付/验证，再从官方源补未决省；不能重跑HA、篡改旧E1费用或自动用未完全验证的资料定HA网格。今次归档后只有Astra按旧Review HEAD及Git Blob严格精确清理**本轮**三件，三个历史PENDING ref `f8db0251fb98f2b157affc9bf7391895b86edba0`、`4e05976bbc8068b971ba5915133e9a6c3b73193d`、`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c`禁止改动。ACTIVE_TASK=NONE；未给新数值任务授权。
