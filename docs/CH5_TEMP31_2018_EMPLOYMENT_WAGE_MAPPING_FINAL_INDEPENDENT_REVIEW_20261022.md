# CH5 TEMP31 | 2018工资就业O/I/S及家庭—企业劳动映射限域独立终审（2026-10-22）
TASK_ID=CH5_TEMP31_2018_EMPLOYMENT_WAGE_IMPUTATION_AND_LABOR_MAPPING_20261022
RUN_ID=b23569dcfb6a4c89a1a366e51bcadc6f
CODEX_ACTUAL_TERMINAL=PASS_SOURCE_ONLY_MAPPING_DESIGN_WITH_PENDING_DATA
ASTRA_REVIEW=PASS__BOUNDED_SOURCE_ONLY_MAPPING_DESIGN__PENDING_DATA_AND_OWNER_E3
ARTIFACT_INTEGRITY=PASS__32_OF_32_CRC_LENGTH_SHA256
UNIT_REGRESSION=258_OF_258_MATCH
STRUCTURAL_AND_IMPUTATION=349_OF_349_MATCHED_CASE_VECTORS
INDEPENDENT_31X31_EXACT_FRACTION_ORACLES=TWO_FIXTURES_PASS
SMALL_ORACLE=6_OF_6_PASS
O_SOURCE_CANDIDATE_CELLS=10_IN_7_PROVINCES
I_ACTUAL_FILL=0
S_ACTUAL_FILL=0
COMPLETE_31_PROVINCE_PANEL=FALSE
MODEL_ACTIVATION=FALSE
RESULTS=FALSE
V011=NOT_STARTED
REVIEW_CLEANUP=ONLY_AFTER_ARCHIVE_REMOTE_READBACK

## 1. GitHub与独立原始字节
Review candidate `d469ebd1dcb8f3b1aede9811e9904d6bbb17e812`，tree `0d0dafb423f16188e673a359987af03778a39234`，sole parent `4500347a525c39a8d7c5c2a483fac19bebaa18a3`。Review branch `review/ch5-temp31-wage-employment-mapping-20181022`在本次审查时指向同一候选，compare ahead1/behind0且仅新增固定路径的result.md、manifest.json、evidence_sanitized.zip；正式治理发行HEAD `bd7d88379b1e0eea028f7880d1eb68a9979d0a7d`审前不变。三个历史PENDING review refs分别为`f8db0251fb98f2b157affc9bf7391895b86edba0`、`4e05976bbc8068b971ba5915133e9a6c3b73193d`、`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c`，审前只读compare identical。
- result.md：4772 bytes、SHA256 72b9b80891a8c390d2c33bd1264ca3f8e93960eb72faed4f8d67281d1d2c9c5c、Git Blob 28b9b7100e21dfdf1f9c711790214cbe7255a13d；
- manifest.json：11922 bytes、SHA256 532ada911ed58bf1b4e68537fb99575d9aa08efe40d05b3c248b66d1143aa919、Git Blob 4673b11409cab6520ce24a79c6eb190075f217b3；
- evidence_sanitized.zip：79846 bytes、SHA256 0b676c59c69ba4f610b0d7bc95fe1751076d58fa8e33344664cb75cd37ea6697、Git Blob 42f3b8a6e658e6faf58fc02a339ab5c5d7d43e17。
Python标准库独立复算32/32成员SHA256/CRC32/解压原长度全部等于已固定manifest，expanded 688876B；成员路径无绝对、上级穿越、重复或符号链接，ZIP CRC全局PASS。公开限定模式的私钥头、Bearer、OpenAI key、Windows Users/ProjectTemp绝对路径扫描无命中。针对性审查并不等于穷尽所有隐私风险。独立机器验收工件（不作为GitHub已发布文件）：CH5_TEMP31_MAPPING_INDEPENDENT_AUDIT_20261022.json，SHA256 a830bd78fad5a125b75f19b56e907caa8dd68512338ffe9dc3b4d98673655125。

## 2. 请求账与数值算法限域
`source_request_canonical_events.jsonl`完整69个不同event_id：历史58个，CURRENT 11个；当前每条new_budget_charge=1，历史=0，来源EVENT身份/发生新旧边界正确。历史58保留源账53网页+5原站，旧builder50的漏计8源为批量请求解析；10个canonical schema cases expected/actual一致。此处验收的是固定公开事件账与规范算法，而非真实第三方计费金额。
`unit_regression_replay.json`258/258 expected/actual及pass标记匹配（其中63 PASS类，其余拒绝/不可判定反例）；`mapping_31_synthetic_oracles.json`349/349预期分类匹配。Astra额外不用Codex接口、用Python fractions.Fraction独立逐项重算两个非对称31×31 fixture：31来源列和=1；每一目的地实际head flow=sum_i M[j,i]*E_i；每一目的地有效劳动=sum_i M[j,i]*E_i*hours[j,i]*efficiency[j,i]，62个目的地头数+62个效率劳动值全部与归档一致；合成小例D=(45,55)、L=(45,110)、gross420、tax75、net345，6/6。未执行当前合同中的生产V010或HA运行时代码。SOURCE_ONLY经济映射建议不能据此转为已接受真实模型修复。

## 3. 2018数据分层的真实数量
三份表每份31省、2018同年且province order一致：O官方原始证据/统计口径经初门筛选后，仅10个非NA候选分布在7省：天津居民1559.60万、吉林非私营年末279.3233万、福建私营52930/非私营74316、湖南40175/70221、海南居民934.32万、重庆52558/78928、云南非私营75701元。均仍待Owner后续数据方案采用，不等于完成31省面板；特别吉林是非私营单位年末人数，不是工资统计年度平均分母。
I插值表31省全部NA，S情景表31省全部NA。理由：没有通过同省同指标2017/2019两端严格可比的完整资格；福建2017私营48830和2019私营57141均有原字节，但definition_version无法认定一致，且2018已观察52930，故只可做holdout敏感性候选，不得覆写O。广东、江苏等官方数据有拒绝/摘录，不能作为任意插值实填。尤其不允许把I/S当国家统计局发布值、不能称2018所有指标31省完整。

## 4. 家庭—就业—工资—企业劳动结构
合成方案A（建议优先Owner讨论，但尚未Owner批准）：保持H居民人头用于家户资产/消费及财政总量，区分原籍居民就业E_i=p_i H_i、目的地工作人口D_j=sum_i M[j,i]E_i、目的地有效劳动L_j=sum_i M[j,i]E_i htilde[j,i] epsilon[j,i]。税前有效劳动工资omega_j→gross_j=omega_j L_j，按目的地一次tau_j分离net labor income与wage tax；工资统计平均值仍需同覆盖年度平均人数E_unit_avg,工时/效率和工资组成。生产已有Lt_mat不在本任务源码权限内验证，建议矩阵M不能自行取代源Lt_mat。
方案B将就业者作为家户代表，必须另外定义非就业者U、资产/消费/财政转移份额和效用福利；单纯H→E替换会改变模型经济方程。当前12个E3经济学待决条目见包内unresolved_economic_E3.md，包括代表家户、工作地/居民地、就业率、迁移、工时/效率、工资范围、HU/资产桥、目的地税、非就业者福利、I是否可用、跨境残差、有效劳动单位对生产函数的影响。**A/B均未被Owner选择，s_H=64.8906755511也未采纳。**
本次数据任务没有重读私人2018规范workbook、未改已冻结V010/源HA；Codex报告HA/HJB/KFE/roots/driver/outer/GE/IRF均0，OS子进程详情UNKNOWN不冒称独立核实。Owner提供本机最终JSON20436B/SHA256 f30f7b1568b32be4ed8024b2df37ae015b4bfbceea716175ace7016043de29c9及完成事件仅为回执报告，Astra没有本机该两文件原字节独立复算；ZIP预算为PREPUBLICATION_SNAPSHOT（11 source,8 python,21 direct,E1=1），不冒称最终Git API调用审计。

## 5. Verdict与治理后续
本轮验收`PASS__BOUNDED_SOURCE_ONLY_MAPPING_DESIGN__PENDING_DATA_AND_OWNER_E3`；绝不升级为`COMPLETE_31_PROVINCE_PANEL`、`HA_CALIBRATED`或`FORMAL_V010_PASS`。无新的HA、调参或正式模型修改授权。先将本报告归档治理并固定Git远端Blob回读，之后只可在旧review ref无变化时普通nonforce删除本轮Review三件且逐件404，并另记录治理清理回执；三个更早PENDING候选不动。ACTIVE_TASK=NONE，等待Owner讨论A/B与下一经济学决策。
