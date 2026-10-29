# TEMP31 MATLAB800家户7价格点R1：GPT独立A/B/C终审

REVIEW_DATE=2026-10-29
TASK_ID=CH5_TEMP31_MATLAB800_THREE_PRICE_INTERIOR_HA_PILOT_R1_20261029
REVIEW_KIND=INDEPENDENT_GITHUB_FIXED_REMOTE_BYTES_AND_SOURCE_NUMERIC_EVIDENCE
OVERALL=PASS_BOUNDED_EXECUTION_AND_73_OF_73_REMOTE_DELIVERY__FOUR_HJB_CONVERGED__ZERO_CERTIFIED_INTERIOR_HA__POST_KFE_STATIONARITY_BLOCKED
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_HEAD_BEFORE_REVIEW=3739e8e0f70a63f5f772d92b4d2cd207e8ec2ab2
TASK_CONTRACT_BLOB=519d700d5ed66daa32127e7f3a53f6c14aaa7ebb
OWNER_FREEZE_COMMIT=d3cc4ceb9d400f2aa00d26cbd577dcae8c5ef5d3
SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_PARENT=a51c2e7ff6548340a1ee86857b0ee55792fa69b4
SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
CANDIDATE_BRANCH=codex/ch5-temp31-matlab800-three-price-interior-ha-pilot-r1-20261029
PAYLOAD_COMMIT=82058048b14d5724cde3789ede801b781a202126
PAYLOAD_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
PAYLOAD_TREE=4db3d68548987c1939c807242e247402c5f0acc6
FINAL_COMMIT=c46a6e5e7220009450cceaf5d59e6e4db7c34f11
FINAL_PARENT=82058048b14d5724cde3789ede801b781a202126
FINAL_TREE=18a3305e62196a9d1f04534690c7149b201754d8

## A. 合同身份/交付独立验收

- GitHub直接读取治理branch HEAD=3739e8e0f70a63f5f772d92b4d2cd207e8ec2ab2，未漂移；候选branch HEAD严格等于FINAL_COMMIT；payload唯一parent=SOURCE_COMMIT，seal唯一parent=payload，两者tree与上列对应；SOURCE→FINAL diff正好两个提交、73个文件全部added且全在冻结task路径/新隔离validator路径白名单；payload→seal diff**仅**新增DELIVERY_FINAL_RECEIPT.json。任何历史src/exports/validators/docs/任务证据均没有被该候选修改/删除。
- 从FINAL固定commit重取71个manifest payload文件真实base64 bytes，使用自实现、经SHA256("abc")标准向量校验的独立散列计算，逐件对照manifest所列bytes、SHA256与GitHub返回Git Blob：71/71 PASS。manifest本身38669 bytes、SHA256=a83662071d4e9f85cdca06938d56188888438bf525b82e1a71cf6933e683009b、Git Blob=840899991de6c98656df0b027d03a937410fbef8，恰与seal的manifest_identity匹配。
- seal原始100662 bytes、SHA256=74577d3396a5ed9adf2f06c5e546f0e6d6e8425c0616eacbe14a84d832e59dc0、Git Blob=fd69e7f2c5c97ff8c25e10f1819b0aa2a9e53d6c；本身不得作自包含self SHA/最终commit，此身份由GitHub固定FINAL引用独立认证。最终71 payload+manifest+seal=**73/73**真实远端文件身份核对PASS。
- 源SOURCE_COMMIT真实获取九个Python HA依赖；全部九个Git Blob与candidate/source_identity.json的原source identity一致：bootstrap=b82eadea383a4d7546a11d4f19686440f8d71870；HJB=56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56；policy=d90eb4ba627d4c702062116c2a4ffadac0f43d86；economics=30528d55b884c62f3c9785dfe59197a61f125a3c；contracts=c746b616bec38531a7d96da81a54e2899d8aba53；pure operator=9a511e151c9bf449412dc5605dfa1a2076711277；MATLAB-faithful KFE=4ccb7cec8c4754e91bd8830a95dc533811784391；wage_debug=7df9c03fdd55d72beded7383866d683ca9356bc9；worksite_tax=90667ddc00c72b9290e91481af4835c808ecfccb。
- 公开证据的全部文件SHA得到独立验证；但本地 D:\ LOCAL_ONLY外置回执、原始Windows子进程、800状态最后G、未经脱敏raw stdout/stderr、KFE完整800格密度与矩阵不在GitHub发布内容，**不能声称已独立见证Windows执行现场或重新计算postG.T@g的800元残差**。审核能直接独立重算已公开的20格边缘聚合，并核对源代码残差计算方法、执行回执、逐轮轨迹。

A_ARTIFACT_INTEGRITY=PASS__73_OF_73_FIXED_REMOTE_BYTES_SHA256_BLOB
A_SOURCE_IDENTITY=PASS__9_OF_9_FROZEN_SCIENTIFIC_GIT_BLOBS
A_EXECUTION_HOST=BOUNDED_EVIDENCE__NOT_INDEPENDENTLY_WITNESSED_LOCAL_ONLY

## B. 数值、经济学和原MATLAB黑箱审阅

### B1 审计范围、价格、真实次数

唯一冻结shape=(b,a,z)=(20,20,2)=800；b=linspace(-2,5,20)，a=linspace(0,10,20)，z=[.8,1.3]，Q的转移系数1/3。固定偏好、调整成本、rb_gap=.07、Tt=.1和HJB(delta1000,max_iterations100,crit1e-7,drift1e-12)未被candidate变更。P0-P4的wt19来自既定numerical_bootstrap19；P5/P6由源合法的两个虚拟省份综合工资合成见证产生15.5/22，非真实厂商工资和实证数据。独立标量代数检查：wt/(.95*2^(5/6))对目标15.5、22回代原工资聚合公式均得到原wt。源代码的负例预检针对2格网格、工资再次扣税、来源错配、context错配、warm-start与提前KFE，记录在全局preflight；没有独立运行这些额外测试。
- 逐个读取7个P?_receipt.json和P?_iteration_trajectory.json，7条均exit0、timed_out false、retries0、单子进程、Windows Job进程提交1GiB回执，最大每点180s，所有7条耗时累计261.24900000018533s，每点均小于180s，无法直接独立见证真实native线程数或RSS硬限。
- 实际每点1 initializer、800 root/brentq，7个HJB driver、总421迭代与421个逐轮归档metric、336800个policy cell、428个assemble_source_operator、421个linear HJB solve。4个HJB converge点各KFE一次，其余三个KFE未执行：KFE=4。全部与预算/监督器真实code object profile计数及逐点回执对齐，未见额外科研求解。合同MAX 7/7/700/7，未用279轮及3次KFE配额在任务结束后关闭。
- 合约禁止的31省/真实经验Excel/firm/GE/IRF/外层固定点/Stage2/Stage3调用均公开记录为0；candidate diff无既有源码修改。进程真实现场不能被GitHub证明，故属于有界执行合规审核。

### B2 七点实测结论

| 点 | rah | rb | net wt | HJB轮次 | 末次maxabs(dV) | KFE | 原post G^T*g驻定残差 |
|---|---:|---:|---:|---:|---:|---|---:|
| P0 | .09 | .02 | 19 | 64，收敛 | 3.5073277615538245e-11 | NOT_CERTIFIED | 4.686593832556138 |
| P1 | .07 | .02 | 19 | 100，未收敛 | .032552545009447043 | NOT_RUN | — |
| P2 | .05 | .02 | 19 | 22，收敛 | 6.8680616749361434e-11 | NOT_CERTIFIED | .32557163336740258 |
| P3 | .07 | .01 | 19 | 100，未收敛 | .3137381136912758 | NOT_RUN | — |
| P4 | .07 | .03 | 19 | 12，收敛 | 5.9733238355619278e-8 | NOT_CERTIFIED | 3.7634433046985296 |
| P5 | .07 | .02 | 15.5 | 23，收敛 | 5.9108647754158028e-8 | NOT_CERTIFIED | 3.4077708099368875 |
| P6 | .07 | .02 | 22 | 100，未收敛 | .30284201302767055 | NOT_RUN | — |

HJB_CONVERGED=4/7，以原Python源value_change停止标准而言成立。KFE_CERTIFIED=0/4；INTERIOR_HA_CERTIFIED=0/7。没有任何已认证的At/Bt/Lt/Ct或31省可用资本/劳动供给。不能由7点样本判断完整三维价格可行域为空，也不能称HJB始终不收敛。

### B3 KFE矩阵/归一化/驻定性区别是首要科学阻塞

从所有4个完整P?_result.json读取：原密度均finite、sum(g)*db*da≈1、负质量≤1e-8、污染行改写系统残差约1e-17，故通过各自局部线性代数与质量数值指标；但未经污染的原始postG.T@g残差依次为4.68659、.32557、3.76344、3.40777，全部显著大于预注册1e-7门。
代码中该两种检验确实不同：
- Python MATLAB-faithful KFE沿用AT=postG.T、替换第floor(.37*800)-1=295行、rhs[295]=.007、求解后以sum(raw)*db*da归一；
- 单独认证计算原**未替换**的postG.T@normalized_density；
- Python监督器没有修改post算子、没有改污染行、没有clip负密度，也没有以已替换矩阵的小残差冒充原驻定方程。

GPT在本次审阅中**直接从Owner已上传原版MATLAB ZIP只读提取原字节**，ZIP SHA256=ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755、HANK_2ASSETS_HJB.m 12227 bytes SHA256=049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae，确认原MATLAB .m第333-344行是A=BB+AAH+Bswitch、AT=A'、替换iFix=floor(.37*M)对应AT的一行再AT\vec、归一化；该摘录未直接认证替换行前的A' g≈0。源Matlab的替换行求解法与Python有有界语义对应；GPT有原件但**Codex本地并未获取原MATLAB原件**，完整Matlab/Python全算子等价仍PARITY_UNCERTIFIED。

数学上，替换一行求解使**被改写**的线性方程残差很小，不保证**原始未改写**A'g=0，尤其当原post矩阵存在非零行和时。该区分解释“线性残差近0但驻定残差很大”可以同时成立，**但不能无完整800状态postG、g逐元素内容断言哪一特定矩阵行/经济机制为全部因果来源**。
额外只读证据：4个收敛HJB点的实际iteration operator最大绝对行和均≤.008682<原MATLAB homecrit=.01（不是原版阈值违规），但其**post-convergence operator**最大绝对行和分别为4.332347913709393、2.81989295896252、4.089693449132323、3.995721135191245。二者是不同矩阵且源Python由不同rate构造，不可偷换，尤其不能由post指标直接反判HJB隐式迭代非法。
本轮未修改HJB/KFE黑箱；新加入的站定性认证是**外部结果接受门**而非修改MATLAB算法。原版是否要求该额外科学门与完整Matlab/Python数值等价仍为独立研究问题。

### B4 20-bin内部资产分布的独立重算与限制

GPT从四个P?_result.json取得实际公开的a_mass20、b_mass20，并用冻结网格重新加权求At/Bt、a/b边缘总质量、内部格点质量及模态索引，独立重算均与远端报告一致，数值误差在约1e-15内。四点均通过R1预注册内部资产诊断阈值，但其密度未通过原post驻定门，不可宣称它们是真实/已认证的稳态分布。

| 点 | 未认证At | 未认证Bt | a内部mass | b内部mass | 驻定门 |
|---|---:|---:|---:|---:|---|
| P0 | 7.274097868486394 | 4.698277466946672 | 1 | .3211511586634552 | FAIL |
| P2 | 5.0722995536457365 | 1.8147088284647883 | .9461043278160232 | .7010464509905365 | FAIL |
| P4 | 7.2688448772635486 | 4.70974313001291 | 1 | .30704855218476157 | FAIL |
| P5 | 7.3037783353426775 | 4.688757796460507 | 1 | .32754863914089327 | FAIL |

上述数值为**未认证诊断数据**而非经济量化结果，不得用于Stage2各省资本/劳动力配置。原始800格密度与postG以及完整旧历史MATLAB/Pythonraw源比对尚未在公共GitHub归档，故GPT没有独立逐元素重算4个原postG驻定残差；当前归因只使用可追溯的冻结求解代码、逐点执行回执及公开原算子标量摘要。不得把残差计算的执行者报告误说成独立800x800重新求解。

B_NUMERIC_REVIEW=PASS_BOUNDED__SEVEN_FROZEN_POINTS__421_ITERATIONS__CONVERGED_4_OF_7
B_DISTRIBUTION_REVIEW=PASS_BOUNDED_RECOMPUTED_20_BIN_MARGINAL_MOMENTS__KFE_CERTIFIED_0_OF_4
B_SCIENTIFIC_SUCCESS=NOT_ACHIEVED__NO_CERTIFIED_INTERIOR_HA
B_MATLAB_FULL_PARITY=NOT_CERTIFIED
B_HJB_BLACK_BOX=UNCHANGED_BY_DIFF

## C. 分层裁决与明确STOP

artifact_integrity=PASS__73_OF_73_FIXED_GITHUB_REMOTE_BYTES_SHA256_BLOB
source_identity=PASS__9_OF_9_FIXED_PYTHON_SOURCE_BLOBS
numeric_review=PASS_BOUNDED_EXECUTION__4_HJB_CONVERGED__3_NOT_CONVERGED
implementation_review=PASS_BOUNDED__7_SUPERVISED_800_STATE_POINTS__NO_BLACKBOX_CODE_CHANGE
scientific_review=KFE_STATIONARITY_BLOCKED__ZERO_CERTIFIED_INTERIOR_HA
privacy_review=PASS_BOUNDED_PUBLIC_PATHS_AND_PRIVACY_REPORT__LOCAL_ONLY_NOT_INDEPENDENTLY_WITNESSED
actual_terminal=EXECUTOR_REPORTED_STOP__FINAL_REMOTE_BRANCH_AND_SEALED_DATA_INDEPENDENTLY_CONFIRMED
delivery=PASS__PAYLOAD_AND_SEAL__73_OF_73
cleanup=NONE_AUTHORIZED__NONE_PERFORMED_BY_GPT
not_completed=NONLINEAR_BELLMAN_OPTIMALITY_RESIDUAL__MATH_SOURCE_FULL_PARITY__CERTIFIED_KFE_STATIONARITY__CONTINUOUS_THREE_PRICE_DOMAIN__STAGE2_3__31_PROVINCE_GE_IRF_RESULTS
OVERALL=PASS_BOUNDED_EXECUTION_AND_REMOTE_DELIVERY__SCIENTIFIC_NO_PASS

SCIENCE_GAP_PRIORITY=READ_ONLY_ORIGINAL_POST_OPERATOR_STATIONARITY_CONTRAST_WITH_MATLAB_PROVENANCE__OWNER_DECISION_REQUIRED
OWNER_BOUNDARY=KEEP_MOLL_MATLAB_HJB_BLACK_BOX_IMMUTABLE
NEXT_ACTION=STOP_AWAIT_OWNER__NO_NEW_TASK_OR_MODEL_RUN_OR_OPERATOR_REPAIR

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

本报告是对已有有界科研运行及GitHub远端交付的独立审阅；发布本报告不会赋予未来任何调参、数值重跑、修改原版黑箱、签发子任务或生产激活授权。
