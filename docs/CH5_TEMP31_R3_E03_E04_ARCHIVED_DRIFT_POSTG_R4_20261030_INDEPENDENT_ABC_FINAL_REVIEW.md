# TEMP31 R4 E03/E04政策相关量、漂移与后置算子：GitHub固定提交独立A/B/C终审（2026-10-30）

REVIEW_DATE=2026-10-30
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
TASK_ID=CH5_TEMP31_R3_E03_E04_ARCHIVED_POLICY_DRIFT_POSTG_DIAGNOSTIC_R4_20261030
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_HEAD_BEFORE_REVIEW=3ba0903a6c9184ae7ff1033751693ad088f31d26
TASK_CONTRACT_COMMIT=3ba0903a6c9184ae7ff1033751693ad088f31d26
TASK_CONTRACT_BLOB=f52883ac2e821ead7d076b378eb84891b116ff66
FIXED_SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
FIXED_SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
CANDIDATE_BRANCH=codex/ch5-temp31-r3-e03-e04-readonly-mechanism-r4-20261030
PAYLOAD_COMMIT=0140ff9c404870107905f01fe856c77bf44408a4
PAYLOAD_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
PAYLOAD_ROOT_TREE=cdb3ca3ab5f3b2e65b1c89f562e038a55b26a04f
FINAL_SEAL_COMMIT=5e1933e4c166fa40b95c82bed377538d843c7576
FINAL_SEAL_PARENT=0140ff9c404870107905f01fe856c77bf44408a4
FINAL_ROOT_TREE=6bdc58c1129c00c9f9004b4e65e4fd9e3c29a7fc
R3_ORIGINAL_SEAL=e194e44be4287cc447fdc3d83adb0dbd01bcb9d0
OVERALL=PASS_BOUNDED_R4_REMOTE_DELIVERY_AND_ARCHIVED_DIAGNOSTIC__SCIENTIFIC_STATIONARITY_STILL_BLOCKED
MODEL_SOLVER_CALLS_DURING_GPT_REVIEW=0
SOURCE_SCIENCE_EDITS=0

## A. 交付、来源、归档与预算

1. GPT通过GitHub连接器直接读取治理HEAD=3ba0903a6c9184ae7ff1033751693ad088f31d26、R4候选HEAD=FINAL_SEAL_COMMIT。固定payload唯一parent=FIXED_SOURCE_COMMIT，tree=cdb3ca3ab5f3b2e65b1c89f562e038a55b26a04f；固定seal唯一parent=payload，tree=6bdc58c1129c00c9f9004b4e65e4fd9e3c29a7fc。SOURCE→SEAL两个commit、28个新增文件，均位于单一新R4任务目录和唯一新增isolated validator；PAYLOAD→SEAL仅增加本任务DELIVERY_FINAL_RECEIPT.json。旧src/exports/HJB/KFE/历史任务数据、R3原结果无Git diff修改。
2. GPT直接从固定SEAL GitHub fetch_file(base64)读取manifest登记的26份payload文件原始字节，以独立SHA-256算法逐件计算并核对Git Blob、bytes和manifest SHA256，26/26通过；SHA256("abc")标准向量自检正确。manifest自身13485 bytes、Git Blob=d56cc6b2bcd96489378ec7e5d16a60b1b3a64725、SHA256=a8c3a8fc6fbd9a9962ab759574292c8aa8673a83d69eb3605f41ffe8e6b7652c。独立Seal receipt 15352 bytes、Git Blob=e1c44568b859eaf566bd81c9b1bda39d270233d0、SHA256=702b368b3ad18ba72ae90fb96ccacea14aa3f5ea8e9ff5cf039545452da4d82c。共**28/28真实远端文件字节、Git Blob、SHA256通过**；不能拿GitHub读取等同于读取LOCAL_ONLY原文件。
3. R4的source_identity.json含4份关键冻结源：HJB=56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56；KFE core=4ccb7cec8c4754e91bd8830a95dc533811784391；post operator=9a511e151c9bf449412dc5605dfa1a2076711277；KFE export=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf。GPT从固定SOURCE_COMMIT逐项读取GitHub Blob核验4/4，无改动。其余原源继续沿原SOURCE_COMMIT冻结；不存在R4经济参数/算法的正式修改。
4. R3 E03/E04四份LOCAL_ONLY NPZ由Codex执行回执声称原位不跟随认证，SHA256/bytes分别为E03 HJB 265d9c8ea51b638d63376f91d357efadd3d8a85a48819443b2d0a49d2ffbc33c/107984，E03 KFE 0cf74725a77b2dcb85097950e81fbf0dbc9a32f7debe75adde13705a53e04ce6/12120，E04 HJB 84ec4cff5f89fe6b56cf695ec21fabfdd3c18198d4ec53c07f6b54fab353107c/106470，E04 KFE 9bddbc20afc0e6b09da27e491749ee062bfd8d4e7e299644d5f5ce72e5f45873/13137。四份实际字节和800维原矩阵/密度未发布GitHub、GPT无法直接读取Windows LOCAL_ONLY；因此归档内容本身属于执行者经SHA身份绑定的现场回执，不是GPT现场独立重新解析NPZ。
5. 执行者只读诊断receipt=exit0、timeout false、一次进程1/1、约1.609秒、硬1GiB committed-memory Job limit/1 active child，未发生重试；HJB/KFE/policy/initializer/root/线性求解/31省/GE/IRF调用均报告0。GPT审查新增脚本静态导入范围为NumPy、SciPy CSR、标准库且无调用冻结模型求解器，原npz只读、allow_pickle=False，审阅内容来自存档的矩阵乘法、向量和分组统计，不是新KFE求解。执行者现场调度、原隐私扫描器payload27/27与final28/28 PASS、实际本地四档案认证不能由远端独立重新执行；这些为PASS_BOUNDED_EXECUTOR_ATTESTED。原468?用户报告为467历史文件、12引用保全属于现场证据，不作为GPT独立哈希每一份旧文件结论。
A_REMOTE_IDENTITY=PASS__28_OF_28_ORIGINAL_BYTES_BLOB_SHA256
A_SOURCE_IDENTITY=PASS__4_OF_4_REVIEWED_SCIENCE_BLOBS
A_LOCAL_NPZ_IDENTITY=EXECUTOR_AUTHENTICATED__NOT_GPT_INDEPENDENTLY_WITNESSED
A_PRIVACY=PASS_BOUNDED__REMOTE_BYTES_VERIFIED__LOCAL_SCANNER_ATTESTED

## B. 漂移、后置算子和分布的独立有限数值与数学审阅

### B1. 原R3结果与20维公开边缘质量复算

固定源网格(b,a,z)=(20,20,2)、db=7/19、da=10/19。E03(rah=.05 rb=.02 wt19.75)和E04(rah=.05 rb=.02 wt19.90)均为R3历史已收敛HJB+原MATLAB风格KFE有限归一输出，但原postG.T@g残差分别.32169695841610524和2.9445205842114848，严格认证FALSE。
R4/numeric_crosschecks.json公开了两点20维a_mass20/b_mass20及两态z_mass2。GPT从固定R4公开数值直接按grid独立加权复算：
- E03 At=5.042931849870291，Bt=1.8181487115863018；
- E04 At=7.227004479580235，Bt=4.706049187240032；
- ΔAt=2.184072629709944，ΔBt=2.887900475653730，Δb上界质量=0.4393009995569363，a半L1=.5507289161806087，b半L1=.6423866234047643；两点a边缘质量和=1（E04浮点误差级）、z质量变化和约-1.1e-16。全部与R3旧点数值及R4独立摘要误差处于1e-15浮点精度量级。
R4原档案声称全800格SIGNED_SOURCE_OUTPUT_DISTANCE=.8572777486815678，GPT检查其不小于各a/b边缘半L1（必要条件）且公开的正负质量差和边缘变化代数相容；**但没有全800个g的公开数值，不能独立计算0.8572777486815678的真实值**。这个指标是执行者归档分析见证+公开代码，而非GPT直接独立重算。

### B2. 已保存政策相关量和漂移

R4/policy_drift_comparison.md、对应/evidence/policy_drift_metrics.json显示：
- E04-E03逐状态mu_a平均有符号变化+.1001001899，最大绝对差1.0687022924；mu_b平均有符号变化+.9195335886，最大绝对差5.6419434870。
- 按1e-12阈值，mu_a由负变正168格、正变负57格；mu_b由负变正106格、正变负11格，且有5格非零变零。
- 消费逐状态平均有符号变化约-.6253138537，劳动约+.0152049727，value约+.03725273996；b上界mu_b平均变化约+1.3882986844、最高4个b网格平均变化约+2.0006602807。所有这些量为直接存储字段的比较及由存档计算的描述统计，**不能证明转移/调整政策标签变化**。旧R3未保存完整transfer、adjustment_cost、liquid_label和transfer_label，也无全部政策历史；必须维持POLICY_LABELS_NOT_ARCHIVED。

### B3. iteration G vs post G、非守恒和负非对角元

四个来自归档的800×800 CSR统计（执行者原档案及公开代码）：
- E03 iteration_G: nnz4031、max abs row sum .0026808411、负非对角元11；E03 post_G: nnz3139、max abs row sum2.8401907108、负非对角元0。
- E04 iteration_G: nnz3720、max abs row sum .0026810554、负非对角元23；E04 post_G: nnz3125、max abs row sum3.8646700569、负非对角元0。
- E04 post_G减E03 post_G共有2655个数值非零变化、max绝对元素差9.2246531665。
迭代算子row-sum均小于原MATLAB homecrit=.01，而KFE后置算子row-sum数值明显更大；这个差异不能静默省略。迭代算子出现负非对角元及post非守恒均是独立需要进一步解释的数学可信度风险；没有同原MATLAB逐元素对跑、未保存BB/AAH分解，不能直接从这些信息推断具体程序错误或为满足CTMC数学条件改原黑箱。

### B4. KFE原始残差行与源行质量亏损

R4/evidence/kfe_residual_metrics.json和只读代码给出：
- E03原postG.T@g最大驻定残差=.32169695841610524，发生在被原KFE替换的**目的地方程 index295**，其余799个方程max约1.249e-16。
- E04目的方程295残差=-2.9445205842114848，其余799个max约7.497e-16。
- 与此不同，原矩阵的**源状态第295行**row sum分别仅约5.55e-17和4.44e-16。非守恒行真正集中在b上边界：E03 20个超tol非守恒源行，主要为z1/a内部；E04 29个，主要z0/a内部及部分z1。
- 执行者归档算得源行损失总和sum_i[g_i sum_j G_ij]，E03=-.3216969584161056，E04=-2.944520584211485；与sum(G.T@g)分别相等，浮点恒等式误差5.55e-16与4.44e-16。乘均匀cell weight=(7/19)*(10/19)后得到质量率约-.062378911604231和-.570959670068709。源行亏损最主要索引E03=699/679/659（b上界z1），E04=299/279/259（b上界z0）；不得把目的方程295残差叫作源295本身全部流失。
- GPT独立使用公开分区统计和格点权重复核了代数总量关系与区别，但未拥有原CSR+完整g，不能宣称独立逐状态构造G.T@g。结论是SOURCE_ARCHIVE_ALGEBRA_BOUNDED，而不是证明MATLAB黑箱造成该行为的源码因果。

### B5. 800状态密度质量重新配置

R4/evidence/density_reallocation_metrics.json公开按b分区的互斥质量变化：b_lower -0.05242087098、b_interior -0.38688012858、b_upper +0.43930099956，三者求和约0；对ΔAt的对应分区贡献约-.15935117118、-1.49559391475、+3.83901771565，合为ΔAt=2.18407262971；对ΔBt贡献约+.10484174196、+.58655373591、+2.19650499778，合为ΔBt=2.88790047565。z0质量变化-.03668010443，z1变化+.03668010443，总质量基本相抵。上界贡献是描述性同位置质量重新分配，不代表已经有真实稳态中经济主体的因果转移路径。
全800格半L1 .85727774868只能标SIGNED_SOURCE_OUTPUT_DISTANCE。E04的微负质量约5.2064e-21，源未修改或clip，原完整驻定方程仍不成立。20-bin可以直接独立重算；完整800格只能通过执行者原档案及公开摘要作有限审阅。

B_PUBLIC_MARGINAL_RECALC=PASS__AT_BT_20BIN_TV_WITHIN_FLOAT_ROUNDING
B_ARCHIVED_ARRAY_DIAGNOSTIC=PASS_BOUNDED__CODE_RECEIPT_AND_ALGEBRA_CHECKS__RAW_LOCAL_NPZ_NOT_AVAILABLE_TO_GPT
B_SOURCE_PARITY=NOT_CERTIFIED
B_STRICT_STATIONARITY=FALSE_E03_AND_E04
B_CAUSAL_MECHANISM=HYPOTHESIS_ONLY
B_FULL_POLICY_LABELS=NOT_ARCHIVED

## C. 最终分层裁决与正式状态

artifact_integrity=PASS__28_OF_28_REMOTE_BLOB_BYTES_SHA256
source_identity=PASS__FIXED_SOURCE_TREE_AND_4_CRITICAL_BLOBS
numeric_review=PASS_BOUNDED__SINGLE_ARCHIVED_READONLY_DIAGNOSTIC__20_BIN_INDEPENDENT_CROSSCHECK
implementation_review=PASS_BOUNDED__NO_SOURCE_CHANGES__NO_NEW_MODEL_SOLVES
scientific_review=DRIFT_AND_POST_OPERATOR_ASSOCIATIONS_OBSERVED__STRICT_KFE_STATIONARITY_NOT_CERTIFIED__CAUSAL_SWITCH_NOT_PROVEN
privacy_review=PASS_BOUNDED__LOCAL_GATE_ATTESTED__REMOTE_BYTES_VERIFIED
actual_terminal=EXECUTOR_REPORTED_STOP__FINAL_CANDIDATE_HEAD_VERIFIED
delivery=PASS__PAYLOAD_PLUS_SEAL__28_OF_28
cleanup=NOT_AUTHORIZED__NOT_PERFORMED
not_completed=ORIGINAL_MATLAB_PYTHON_FULL_PARITY__COMPLETE_POLICY_TAGS__STRICT_KFE_STATIONARITY__CONTINUOUS_PRICE_THRESHOLD__STAGE2_STAGE3__REAL31_GE_IRF_THESIS_RESULTS
OVERALL=PASS_BOUNDED_R4_ARCHIVED_READONLY_AUDIT_AND_DELIVERY__IMPORTANT_STATIONARITY_RISK_PERSISTS
NEXT_ACTION=STOP_AWAIT_OWNER_DECISION__NO_NEW_RUN_OR_TASK_AUTOMATICALLY_AUTHORIZED
P3=BLOCKED
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

本报告不是实证/稳态/GE通过证明，不替换任何原MATLAB数学黑箱，不改R1–R4历史成果或审阅结果，不运行新HA/KFE/GE/IRF，不合并、不清理、不自动签发下一任务。
