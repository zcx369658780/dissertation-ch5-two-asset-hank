# TEMP31 R6：原MATLAB–冻结Python后置算子逐元素同输入对照（独立科研验证合同）

TASK_ID=CH5_TEMP31_R6_MATLAB_PYTHON_POST_OPERATOR_ELEMENTWISE_PARITY_20261030
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVAL=2026-10-30__BOUNDED_MATLAB_PYTHON_POST_OPERATOR_ELEMENTWISE_RESEARCH
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=f17a5cb8b1bb151f340d2f10e92d6ea126c389ba
TASK_PUBLICATION_COMMIT=GPT_PROVIDES_EXACT_SHA_AFTER_PUBLICATION
EXPECTED_GOVERNANCE_HEAD=TASK_PUBLICATION_COMMIT_STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_R6_MATLAB_PYTHON_POST_OPERATOR_ELEMENTWISE_PARITY_20261030/CONTRACT.md
CANDIDATE_BRANCH=codex/ch5-temp31-r6-post-operator-elementwise-parity-20261030
FIXED_SCIENTIFIC_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
FIXED_SOURCE_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
FIXED_SOURCE_PARENT=a51c2e7ff6548340a1ee86857b0ee55792fa69b4
R5_FINAL_CANDIDATE_SEAL=cd6ef027dc0c7242e4f62ae648ca83641fc6f1c6
R5_FINAL_REVIEW_GOVERNANCE=f17a5cb8b1bb151f340d2f10e92d6ea126c389ba
R5_FINAL_REVIEW_PATH=docs/CH5_TEMP31_R5_FIXED_REF_SOURCE_RECOVERY_20261030_INDEPENDENT_ABC_FINAL_REVIEW.md
R5_FINAL_REVIEW_BLOB=e8e10a02ddedc3316bd44a4bf508b492bb0dc06c
R4_FINAL_REVIEW_COMMIT=1033b4a0531613093ce13789e3916fd228ae9b5b
R4_FINAL_SEAL_COMMIT=5e1933e4c166fa40b95c82bed377538d843c7576
OWNER_MATLAB_ZIP_SHA256=ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755
OWNER_MATLAB_HJB_NAME=HANK_2ASSETS_HJB.m
OWNER_MATLAB_HJB_SIZE_BYTES=12227
OWNER_MATLAB_HJB_SHA256=049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae
HJB_SOURCE_PATH=src/ch5_two_asset_hank/temp31_netwage_hjb.py
HJB_SOURCE_BLOB=56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56
OPERATOR_SOURCE_PATH=src/ch5_two_asset_hank/matlab_faithful_operator.py
OPERATOR_SOURCE_BLOB=9a511e151c9bf449412dc5605dfa1a2076711277
KFE_SOURCE_BLOB=4ccb7cec8c4754e91bd8830a95dc533811784391
EXPORT_SOURCE_BLOB=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf
MAX_HA_HJB_KFE_POLICY_FIRM_GE_IRF_REAL31_MODEL_CALLS=0
MAX_MODEL_SPSOLVE_OR_STATIONARY_DENSITY_SOLVES=0
MAX_PRICE_POINTS=0
MAX_PRODUCTION_SCIENTIFIC_SOURCE_WRITES=0
MAX_MATLAB_NATIVE_PROCESSES=1
MAX_PYTHON_PURE_ASSEMBLY_COMPARE_PROCESSES=1
MAX_SYNTHETIC_SOURCE_DRIFT_CASESETS=1
MAX_PREEXISTING_ARCHIVED_E03_E04_CASESETS=2
MAX_NEW_REPOS_WORKTREES=0
MAX_ISSUE_PR_MERGE_CLEANUP=0
AUTO_NEXT=FALSE

## 0. 目标、授权边界与上一轮区别

Owner批准进入与R5相区别的**一次有界数值研究**：不再仅对MATLAB源摘录/手工toy进行静态推理，而是在严格同输入条件下用原MATLAB的spdiags离散装配语句作为受控运行时oracle、与冻结Python COO/CSR后置算子进行逐元素比较，判断“原MATLAB离散规则自身的现象”和“Python移植差异”。本合同授权的运行严格限定为无HA、无HJB迭代、无KFE、无原模型求解器、无政策优化、无真实31省的**稀疏矩阵装配与比较**；这不是开放真实模型科学运行或修改算子的权限。

不要自动执行原始HANK_2ASSETS_HJB.m函数（其内部会调用lab_solve2/fzero和HJB/KFE线性求解）。允许仅将经原件认证的后置稀疏装配公式逐字对应地复制到新建隔离MATLAB验证脚本，提供**人工固定漂移数组**作为输入；不运行MATLAB实际经济求解器。运行时oracle的等级是MATLAB_POST_ASSEMBLY_RECIPE_ORACLE，不等于完整原HJB函数运行证据。不能把“相同外生漂移下矩阵相同”推导为“生成这些漂移的经济预算或政策选择相同”。

R5独立终审已PASS_BOUNDED，明确：Cmin在原MATLAB函数第7行为0；原MATLAB HJB iteration有homecrit BREAK，冻结Python driver无该相同分支；边界outward diagonal loss静态有条件解释R4的b-upper负行和；完整spdiags填充及运行时等价未认证；严格KFE驻定FALSE。所有历史判断及旧R5 STOP维持不变。

## 1. 前置固定来源与双平面原件门

先核验治理远端HEAD严格等于GPT交付的TASK_PUBLICATION_COMMIT、单parent=GOVERNANCE_PARENT，且治理新增diff仅本CONTRACT；不能以旧f17a5cb8作为任务发布后的HEAD。候选远端分支必须不存在；若已存在则STOP不可覆盖。科研candidate从FIXED_SCIENTIFIC_PARENT派生，不从R5候选或治理HEAD派生。固定源按FIXED_SOURCE_TREE、path、Git Blob逐个核验；R4/R5终审按各自review提交读取，绝不能从科学源旧提交读取后置审阅文件。上轮R5已证明9/9固定Ref读正常，不必重跑全部旧来源或497旧文件审计。

原MATLAB原件由本项目Owner上传，GPT已独立读取真实ZIP并复核上列ZIP/HJB sha256；本轮新任务可使用**Owner明确交给Codex的、已获准放在安全工作区内的原MATLAB文件**进行只读SHA256核验。不可去其他盘符/私人目录/锁仓猜路径，不下载未知镜像或改变账号、协议、凭据。若Codex没有原始.m字节，可依据本合同及R5经GPT认证的源码行进行**RECIPE_SOURCE_FROM_GPT_AUTHENTICATED_ORIGINAL**对照，但必须标记MATLAB_RAW_LOCAL_NOT_AVAILABLE；禁止写成MATLAB_ORIGINAL_RAW_LOCAL_PASS，也不能宣称完整MATLAB函数原件运行。不要把原MATLAB整个ZIP、非公开R3 NPZ、私人路径或凭据推送公开仓库。

本轮必须使用真正的授权MATLAB运行环境（若可用）来支持MATLAB_RUNTIME_RECIPE证据；不可用时只记录版本/availability并STOP__R6_MATLAB_RUNTIME_UNAVAILABLE，严禁自动安装MATLAB、切换远端机器或使用Octave结果冒称MATLAB。Octave亦不得未经本合同另设调用。对于运行脚本的外部依赖，只允许内置spdiags/sparse/reshape/基础索引与本合同明确的固定数据；不用optimization/statistics toolboxes、并行或网络。失败后不自动重试，不以无关的Python自制spdiags克隆冒充原MATLAB oracle。

## 2. 核心第一道科研门：完全相同的漂移数组再装配

固定状态顺序MATLAB: (i,j,nz) 一基，压平 i+(j-1)*I+(nz-1)*I*J；Python: (i,j,nz) 零基，压平 i+j*I+nz*I*J，Python ravel(order='F')。MATLAB两z块Bswitch=[eye(IJ)*la11,eye(IJ)*la12;eye(IJ)*la21,eye(IJ)*la22]；Python应为kron(switch_matrix,eye(IJ))。必须记录MATLAB行/列输出和Python CSR对应的(row,col,val)、CSR非对角位置与z块接缝。

原MATLAB原件HANK_2ASSETS_HJB.m的后置源码第262–264行：
- dh=Idh_B.*dh_B+Idh_F.*dh_F
- s=(1-tau)*w*zzz.*l+Rb.*bbb+Tt-Cmin-dh-HANK3_cost(results,CHIh,dh,aaah,0)-C
- mh=dh+Rah.*aaah
第265–296行b轴：X=-min(s,0)/db；Y=min(s,0)/db-max(s,0)/db；Z=max(s,0)/db；每z块BBi=spdiags(centdiag,0,IJ,IJ)+spdiags([updiag;0],+1,IJ,IJ)+spdiags([lowdiag;0],-1,IJ,IJ)，其中centdiag是按i+(j-1)*I写的Y，updiag第一i为0、i=2..I存Z(i-1)，lowdiag i=1..I-1存X(i+1)、i=I存0。
第299–333行a轴：chih=-min(mh,0)/dah；yyh=min(mh,0)/dah-max(mh,0)/dah；zetah=max(mh,0)/dah；每z块AAHi=spdiags(centdiagh,0,IJ,IJ)+spdiags([updiagh;0],+I,IJ,IJ)+spdiags([lowdiagh;0],-I,IJ,IJ)，其中updiagh j=1为0、j=2..J存zetah(j-1)，lowdiagh j=1..J-1存chih(j+1)、j=J存0；A=BB+AAH+Bswitch。**原[updiag;0] / [lowdiag;0]的长度、正负offset、spdiags具体对齐，不可先“修正为标准惯例”。** 记录MATLAB runtime actual输出，而不是以猜想替代原函数运行语义。

冻结Python operator核心assemble_source_axis/backward,forward,axis：b ±1、a ±I；只有合法相邻格才加入offdiag，主对角一律-(backward+forward)；assemble_source_operator=BB+AAH+kron(switch,identity)。冻结Python post在temp31_netwage_hjb.py：assemble_source_operator(max(-mu_b,0)/db,max(mu_b,0)/db,max(-mu_a,0)/da,max(mu_a,0)/da,switch_matrix)。**先令mu_b=s、mu_a=mh**，以同一符号值输入双方，隔离装配；不能先比较各自独立求解生成的不同政策漂移然后归咎spdiags。

## 3. 测试数据和有界预算

阶段A：一次固定小网格(I,J,Nz)=(3,3,2)，人工明确的s/mh（包含负、零、正；b下上界、a下上界、四角；确保b列接缝、a行接缝、z块边缘；至少一个非对称且行和为0的la_mat）。报告完整固定输入JSON或纯文本数值、每一坐标及行列次序；不得从真实经济模型中产生这些值。**使用真正MATLAB，启动最多一个进程、没有任何完整原HANK函数调用。**

阶段B（仅当阶段A已通过MATLAB原生运行时、且旧归档有明确安全路径）：可选只读旧R3 E03/E04最多两个已封存case，从其原NPZ读取已保存的mu_b/mu_a和网格/switch；做校验SHA256/bytes/原有字段、allow_pickle=False；仅以保存数组重装配800×800 post算子并做稀疏对比，**不重解HJB/KFE，不更新政策，不用价格搜索，不读取或发布完整g、私有个人信息**。源归档身份按R4终审固定表，不得私搜原路径。若旧NPZ仅在明确保护区或路径无法访问，阶段B=BLOCKED__ARCHIVE_INPUT_UNAVAILABLE，不能扩大权限、重构档案、改用新模拟点或用R4摘要当作实际逐元素数据。阶段B不对MATLAB原始HJB运行时全路径等价作认证。

允许用一个MATLAB进程在阶段A和（若合法取得）阶段B载入固定数值并依次只调用矩阵装配，另一个Python进程用冻结纯operator assembly函数/已认证同源隔离拷贝装配与比较，**不导入或调用真实HJB driver/policy selector/KFE求解器**。单过程内最多1人工小case+2旧case，无第二轮微调、无失败重试；MATLAB输入输出可使用中性无隐私标准数值文件（如 .mat / .csv，仅置于隔离目录LOCAL_ONLY）。只允许最小必要内存/时间；依原已批准安全资源控制，如无法继承Job limit则STOP且给出真实原因，不能放宽保护。

## 4. 逐元素验收、反例与必要归因

对每个case，分别核对MATLAB与Python实际BB、AAH、Bswitch、A：
1) 形状、行/列方向、非零坐标、z-block接缝、b±1和a±I对角位置、原MATLAB spdiags输入向量长度与MATLAB版本；
2) canonical sorted (row,col,value) 表（仅合成case全量可公开；旧归档只发布汇总、代表性前若干差异与哈希，不公开原800矩阵）；stored nnz 与structural nonzero区分；
3) 最大逐元素绝对误差及max-relative误差、差异个数（精确定义零阈值/数值容差），重点对角、非对角、边界、角点、b列接缝、a行接缝、z块接缝；
4) 每行row sum的MATLAB/Python独立向量，b_lower=min(s,0)/db、b_upper=-max(s,0)/db、a_lower=min(mh,0)/da、a_upper=-max(mh,0)/da、内部0的条件贡献；Bswitch若row-sum为0则额外贡献0。若不相等，必须记录具体(row,col)、原始两侧值和导致的真正MATLAB runtime索引规则。
5) 零及浮点比较同时提供绝对容差1e-12与相对容差1e-10，分别报告strict mismatch和tolerance mismatch，不得以sum、nnz、范数相似代替逐元素零差异。对一行是否守恒，应在各方向outflow-rate与其他轴/Bswitch贡献已确认后判读。
6) 如果发现Python与原MATLAB稀疏装配不一致，先定位最小反例并报告CHANGES_REQUIRED_REQUIRES_OWNER_DECISION；本任务禁止改Python或MATLAB源码。若完全一致，最多判定POST_ASSEMBLY_ELEMENTWISE_MATCH_ON_IDENTICAL_INPUTS，**不能推出HJB_POLICY_PARITY / ORIGINAL_FULL_MATLAB_RUNTIME_PARITY / STRICT_KFE_STATIONARITY**。

现有R4历史指标作为外部一致性检查而非本轮新求解目标：E03 postG非守恒源行20、max abs row sum2.8401907108、原post G.T@g最大残差.3216969584；E04对应29/3.8646700569/2.9445205842；最显著为b upper；被替换的是destination equation zero-based295，**不是source row295本身**。旧E03/E04源单位网格(b,a,z)=(20,20,2)。如阶段B可读取原档案，应检查旧postG与Python重装配逐元素一致及MATLAB recipe与之对照，但不可运行矩阵转置乘g或任何KFE求解来“验证”驻定。历史原KFE不严格驻定状态保持FALSE。

## 5. 第二道科研门：政策/现金流来源分离（仅静态不求解）

必须单独产出source_to_source_budget_map，逐项核对MATLAB s与Python mu_b、MATLAB mh与Python mu_a，至少包括：MATLAB第7行Cmin=0；现金资产正负两种Rb（负b附加借贷利差）；(1-tau)*w*z*l vs Python已校正净工资输入（避免重复征税）；Tt/transfer_income；dh与HANK3_cost中的max(a,a_bar)以及transfer符号；Rah/raah=a位置taper；保存的C/l/Idh/dh_B/dh_F与Python policy.last arrays；s/mh最终时序。HANK3_cost.m与HANK3_FOC.m只读原件源码为同一ZIP中权威辅助，但不得调用函数进行新policy solve。归类为 EXACT_STATIC_EQUIVALENT / CONDITIONALLY_EQUIVALENT / SOURCE_DIFFERENCE / UNRESOLVED_INPUT_OR_POLICY_GAP；缺少原始输入映射就明确阻塞，不填造数值。R5已确认homecrit原MATLAB第233–239行与Python driver存在差异，这一差异应继续登记，不能因第一道装配等价而宣告HJB整体等价。

## 6. 交付、白名单与STOP

唯一可新建的独立脚本路径：
- validators/multi_province/temp31_r6_matlab_post_operator_oracle_isolated.m （无模型调用，只含受认证原spdiags recipe、固定数组读写）
- validators/multi_province/temp31_r6_python_elementwise_comparator_isolated.py（只导入/复制经Blob认证的纯装配函数，不做求解）

唯一可新增报告/数据索引目录：
tasks/CH5_TEMP31_R6_MATLAB_PYTHON_POST_OPERATOR_ELEMENTWISE_PARITY_20261030/ 下 result.md、manifest.json、source_identity.json、native_matlab_runtime_receipt.json、synthetic_case_inputs.json、synthetic_elementwise_results.json、archived_case_gate.json、archived_elementwise_summary.json（仅真实读取时）、sparse_band_and_seam_table.md、matlab_python_first_mismatch.md、source_to_source_budget_map.md、R4_R5_evidence_relation.md、gap_register.md、model_budget_zero.json、privacy_report.md、DELIVERY_FINAL_RECEIPT.json、必要最小文本证据。旧NPZ、原MATLAB、MATLAB运行中间数组/完整旧矩阵只保留LOCAL_ONLY；严禁复制原始私有科研数组到公共GitHub，防止暴露个人路径/凭据，公开前执行已存在的隐私扫描门（不能放宽）。

完成来源硬门/真实MATLAB运行与报告后，在从FIXED_SCIENTIFIC_PARENT派生的单一全新candidate产生一个payload commit、普通权限SSH最多一次push；回读真实远端Blob、bytes、SHA256、commit/parent/tree与每个文件。最后一个seal commit仅加DELIVERY_FINAL_RECEIPT.json、独立隐私扫描PASS后普通权限SSH最多一次push，全量回读；最终回执外置LOCAL_ONLY，不追加第三commit。GitHub公开路径只留脱敏、必要且确有内容的证据。未经Owner下一次批准不允许修源码、合并、PR/Issue、清理、接下一任务。若发生权限拒绝/身份不符/源码不齐/真实MATLAB环境缺失/矩阵失败/隐私或推送门失败，记录真实停止点、已完成与未完成，不绕过限制，不谎称发布成功。

终态：
- 数值证据全部完成、正常交付：STOP__AWAITING_GPT_INDEPENDENT_ABC；
- 完整原MATLAB有界脚本不能在真实MATLAB运行：STOP__R6_MATLAB_RUNTIME_UNAVAILABLE；
- 逐元素差异：STOP__R6_POST_ASSEMBLY_DIFFERENCE_REQUIRES_OWNER_REVIEW（可在报告前提允许时交付失败证据；不可修补）；
- 其他来源/权限/隐私/交付阻断：STOP__R6_SOURCE_OR_SAFETY_OR_DELIVERY_BLOCKED。

GPT收到候选后独立A：固定来源/原件及证据完整性；B：真实MATLAB recipe与Python相同输入矩阵逐元素、边界及政策区别；C：artifact_integrity/source_identity/numeric_review/implementation_review/scientific_review/privacy_review/actual_terminal/delivery/cleanup/not_completed的分层裁决。任何PASS只能受已跑case与证据等级约束。

## 7. 继承科学状态（不可被本任务自动改变）

P3=BLOCKED
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
STRICT_KFE_STATIONARITY=FALSE_INHERITED_R3_R4_R5
ORIGINAL_R5_BATCH_FAILURE_ROOT_CAUSE=UNKNOWN
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE
