# CH5 TEMP31 · 2018物理量纲统一与31x31无HA结构接线长任务
TASK_ID=CH5_TEMP31_UNIT_NUMERAIRE_AND_NONHA_MATRIX_GATE_20261022
REVISION=ISSUED_20261022_R1
OWNER_DIRECTION=2026-10-22 先统一数值量纲，之后才能再调31省参数
MODE=SOURCE_ONLY_UNIT_DECISION_SUPPORT_AND_SYNTHETIC_NOHA_MATRIX_INTEGRATION
BASELINE=ec91e9e5dcb32ca04a3f83c97a6795c176f55bcf
REVIEW_BRANCH=review/ch5-temp31-unit-numeraire-nonha-20261022
FIXED_PARENT=ec91e9e5dcb32ca04a3f83c97a6795c176f55bcf
TEMP_PATH=_review_tmp/ch5/temp31-unit-numeraire-nonha-20261022/
SCIENCE_BUDGET=0; HA_HJB_KFE_ROOTS_GE_IRF=0

## 1. 固定已归档来源
基于已发表、只读source ref：当前状态CURRENT/TASK_CURRENT/DOC_INDEX和正式V010 plan；docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md Git Blob d4c021aca1ac35549781ba725607ed20aeb0f8fb（仍PARTIAL）；docs/CH5_MP4C_2018_REVISED_GDP_AND_CANONICAL_DATA_WORKBOOK_REPORT.md Git Blob c1f6f0789535956dcfa760495d4a7f34f1e08637；本轮新工作合同 docs/CH5_TEMP31_PHYSICAL_UNITS_AND_HOUSEHOLD_NUMERAIRE_WORKING_CONTRACT_20261022.md（Git Blob将在发行manifest中冻结）。严格不把proposal改写成Owner已批准数值beta。
唯一2018数据原件只读路径 D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx，工作簿SHA256 AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67；如不存在/不匹配就只完成无需该文件的符号测试并SOURCE_UNAVAILABLE_STOP；不得搜本机旧混年份cache或替代来源。不上传私人原xlsx或31省逐项真实原数据。
模型源参考commit 94de4501dec051b969bee9d852eba2d4591f30ef，主要mainline_household_runtime/migration_labor/capital_network/one_turn/steady_state/firm/wage/fiscal_diagnostics及冻结正式matlab-faithful HA的SHA；使用旧接受身份和本任务已授权的精确单文件读取，绝不root recursive GitHub或宽tasks列表。

## 2. 先统一宏观物理量纲（NO-HA）
固定在SOURCE_ONLY层MU=10万元，NU=100人；来源GDP亿元×1000、PIM K万元÷10、人口万人×100；firm effective labor=NU×effort，Z按Y/K/L物理尺度重算，r税率和alpha等无量纲/每模型期。真实执行源不能把某省资本单位混成旧×1000，不使用混年2018；把所有代码/表字段标source_raw_unit, physical_unit, model_year/period, per_NU_or_total, transformation, used_in_equation, SOURCE_AUTHORITY_STATUS。
在现有2018唯一workbook源验证31省身份/年份和同年GDP/POP/CAP/alpha/Zt质量，SOURCE_ONLY全国Y/N共同标尺。如果官方数据/研究旧值不完整写NA，不以任意插值/新调参凑31省。

## 3. s_H家庭共同货币numeraire，只算候选、不选择
严格按工作合同计算s_H_GDPpc=total2018Y[MU]/total2018N[NU]，并在有已采纳alpha与mstar、参考L=N的明示源条件下计算s_H_LABOR作为对照；附两候选从2018原数据、算式、原字节身份到价格界元/人含义、a/b网格实际金额上限及2018 K/N的全31省尺度比表。
输出候选基准与raw上/下界实物含义，不把作为模型派生的LABOR基准说成官方工资，不为减少clip/调整结果选择。不得将β_A=1/100/10000自选为最终经济参数。若财政/效用成本元/模型期存在难换维度的参数须列E3，货币收益率绝不乘货币因子。须给定明确候选优缺点、推荐优先级，并把最终取值记OWNER_DECISION_PENDING。

## 4. 本任务允许的31×31无HA矩阵结构改写和测试
独立新scratch D:\ProjectTemp\ch5_temp31_unit_numeraire_nonha_20261022_01；先验证可信父目录、路径新建、身份、reparse/符号链接和旧受保护root/index；独占创建且首次写前身份二次核。不得写正式V010、历史private workbook/old journal/旧model tree或C盘备份，不能启动生产模型。
可在自有scratch对现有已接受源数学实施小范围无HA适配与oracle：S[j,i]含home retain1-theta_i、外省K1 foreign-only stable softmax、同轮同S的数量和raw收益，lagged raw return分账；phi[j,i]目的地×来源、tau[j]仅扣一次，Lt_mat[j,i]行和为firm Lt且不二次乘N；模拟At_HU、N_NU和符号s_H进行31省资本守恒；单位不定的财政只进行symbolic per_NU->aggregate桥，明确不能声明实体值通过。
至少构造两个非对称31省synthetic tests，负例覆盖旧CAP×1000、N二次乘、迁移矩阵轴交换、S列和不为1、same-S差错、只给At换单位却没换工资/消费、无权将未经采纳单位系数等于1。所有测试source+结果归档，在单位E3未决时只可获得STRUCTURAL_NOHA_PASS和NUMERAIRE_CANDIDATE_READY，绝不称UNIT_CALIBRATION_ADOPTED或31省STEADY_STATE_PASS。

## 5. 源字节、资源及自动交付
独立budget wall<=5400秒（source/unit900+engineering2400+delivery1500+final reserve600），engineering Python starts<=12、direct starts<=40、E1<=1批仅非模型格式/路径，scratch新增<=64MiB、源请求<=30个精确对象、Git Data writes<=8、Review三公开文件总<=2MiB、ZIP展开<=4MiB/成员<=28，成功发布<=1。HA/HJB/KFE科学roots、driver、outer、GE/IRF、正式V010修改和旧预算使用全部0。
Codex应自动发布脱敏result.md、manifest.json、evidence_sanitized.zip到独立Review分支 review/ch5-temp31-unit-numeraire-nonha-20261022 下 _review_tmp/ch5/temp31-unit-numeraire-nonha-20261022/，Review sole parent固定 ec91e9e5dcb32ca04a3f83c97a6795c176f55bcf（不是本任务issue/release）；仅白名单三件、普通nonforce、三Blob/SHA256与ZIP全成员CRC/length/SHA256远端原字节readback。源Workbook和省级真实值不公开；如果遇401/403/429/平台安全拒绝STOP，绝不切换账号、SSH、代理绕过。旧B-only、AB、HTTP三PENDING候选原SHA严格保留；Astra独立审查并治理归档远端readback后才清理本轮Review三件。
终态提供真实run_id、actual_terminal、全部资源/首错、SOURCE_ONLY 31省units sheet及两候选numeraire对照与32项目量纲/结构测试、原始最终JSON Base64/bytes/SHA、独立完成事件。首次许可可以完成所有既定无HA源码与测试，不拆额外工程微任务；结束立刻STOP、等待Astra和Owner选择家庭numeraire，绝不自动发新31省HA调参任务。Results FALSE、model_activation=False、REAL_GE=False、V011 NOT_STARTED。
