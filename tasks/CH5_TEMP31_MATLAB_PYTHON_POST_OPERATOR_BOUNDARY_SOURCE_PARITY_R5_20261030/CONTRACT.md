# TEMP31 R5：原MATLAB与冻结Python后置算子、边界和概率守恒逐行只读来源对照

TASK_ID=CH5_TEMP31_MATLAB_PYTHON_POST_OPERATOR_BOUNDARY_SOURCE_PARITY_R5_20261030
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVAL=2026-10-30__MATLAB_PYTHON_POST_OPERATOR_BOUNDARY_SOURCE_LINE_BY_LINE_READONLY
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=1033b4a0531613093ce13789e3916fd228ae9b5b
TASK_PUBLICATION_COMMIT=GPT_SUPPLIES_EXACT_40_HEX_AFTER_PUBLICATION
EXPECTED_GOVERNANCE_HEAD=TASK_PUBLICATION_COMMIT_STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_MATLAB_PYTHON_POST_OPERATOR_BOUNDARY_SOURCE_PARITY_R5_20261030/CONTRACT.md
CANDIDATE_BRANCH=codex/ch5-temp31-matlab-python-post-boundary-source-audit-r5-20261030
FIXED_SCIENTIFIC_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_PARENT=a51c2e7ff6548340a1ee86857b0ee55792fa69b4
SOURCE_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
R4_FINAL_SEAL=5e1933e4c166fa40b95c82bed377538d843c7576
R4_FINAL_TREE=6bdc58c1129c00c9f9004b4e65e4fd9e3c29a7fc
R4_FINAL_REVIEW_COMMIT=1033b4a0531613093ce13789e3916fd228ae9b5b
R4_REVIEW_BLOB=2b079567bd03ade8ef9f2c37944be7bd9fdfc20a
OWNER_MATLAB_ZIP_SHA256=ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755
OWNER_MATLAB_HJB_FILENAME=HANK_2ASSETS_HJB.m
OWNER_MATLAB_HJB_BYTES=12227
OWNER_MATLAB_HJB_SHA256=049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae
MATLAB_HJB_BLOB_PYTHON=56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56
PYTHON_OPERATOR_BLOB=9a511e151c9bf449412dc5605dfa1a2076711277
PYTHON_KFE_CORE_BLOB=4ccb7cec8c4754e91bd8830a95dc533811784391
PYTHON_KFE_EXPORT_BLOB=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf
MAX_MODEL_HJB_KFE_POLICY_INITIALIZER_ROOT_GE_IRF_FIRM_31PROVINCE_CALLS=0
MAX_REAL_SCIENCE_SOLVER_CALLS=0
MAX_NEW_PRICE_POINTS=0
MAX_ORIGINAL_SCIENCE_SOURCE_WRITES=0
MAX_ORIGINAL_MATLAB_RUNTIME_CALLS=0
MAX_NO_HA_SYNTHETIC_STATIC_PROBES=1
MAX_SYNTHETIC_CHECK_ROUNDS=1
MAX_SYNTHETIC_CHECK_RETRIES=0
AUTO_ADAPTIVE_WORK=FALSE
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 科学目标与证据等级

Owner批准将R4发现的E03/E04后置KFE算子行和缺失问题，回溯至原MATLAB文件HANK_2ASSETS_HJB.m的真实源行和固定Python SOURCE_COMMIT的真实代码，逐行审核post资产漂移重算、BB/AAH/Bswitch稀疏对角线位置、b和a上下边界截断、post算子的守恒与KFE转置污染行。仅允许读源码、对照文本/AST与纯代数，必要时最多一个**不调用任何HA模型的微型矩阵索引/行和示意检查**。本轮没有新HJB/KFE模型实验、没有价格寻优、没有新800状态矩阵求解、没有正式修复授权。
R4执行者已认证原R3四个LOCAL_ONLY归档，但本任务优先复用已发布R4报告/统计及固定源文件，**无需再次开启四个NPZ或访问旧R3私有阵列**。不得读取P3/WASM/old locked、无关Project附件、私人文件、密钥；不得以新任务借口复跑E03/E04。
GPT在发布前从Owner上传原版ZIP真实字节直接计算ZIP SHA256=ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755、HANK_2ASSETS_HJB.m 12227 bytes SHA256=049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae，并检查所列MATLAB源码行。Codex本地若无已在当前安全隔离工作库授权存在的原MATLAB字节，**仅可引用本合同认证摘录，标MATLAB_RAW_LOCAL_VERIFICATION=NOT_AVAILABLE及SOURCE_EXCERPT_ONLY**。不要求也不允许去Owner私有目录、其他锁仓或网络补找ZIP/原件。引用受认证摘录可以支持有界静态语义讨论，但不可宣称本地实际MATLAB运行或逐元素数值等价。
保持证据分层：ORIGINAL_MATLAB_SOURCE_DIRECT_VERIFIED_BY_GPT，PYTHON_GIT_SOURCE_DIRECT_VERIFIED_BY_CODEX/GPT，STATIC_SEMANTIC_INFERENCE，SOURCE_EXCERPT_ONLY_IF_MISSING_RAW_LOCAL，PURE_NO_HA_TOY_ALGEBRA，NOT_TESTED_MATLAB_RUNTIME，EXECUTOR_ARCHIVED_R4_WITNESS。绝不把推测写成证明。

## 1. 原MATLAB关键行：经Owner ZIP原件认证的严格审计锚点

所有行号为HANK_2ASSETS_HJB.m的一基行号，不是其他MATLAB脚本行号。必须读取上一轮Owner冻结文档后，逐行引用源行、关键变量、网格flatten/对角偏移、原前置HJB/后置KFE差别；禁止把这组片段当作新的计算算法或更改原源。
A. HJB循环第114–119行定义原Vb向前/后差分及b边界导数，第135–154行计算l、u、dhBB/BF/FB/FF、边界dh_B/dh_F、Idh_B/Idh_F与b上界Idh_F(I,:,:)=0且Idh_B(I,:,:)=1的选择约束。第155–157行形成迭代阶段的X/Y/Z：X=-Ic_B*sc_B/db-Idh_B*sdh_B/db；Y=Ic_B*sc_B/db+Idh_B*sdh_B/db-Ic_F*sc_F/db-Idh_F*sdh_F/db；Z=Ic_F*sc_F/db+Idh_F*sdh_F/db。第185–188行拼BB，第190–198行形成MhB/MhF与a轴率，第226–233行拼AAH+Bswitch且第234–239行仅**HJB迭代A2max>homecrit**时BREAK。不得把这个内部guard转嫁给post KFE。
B. 原post阶段第262–264行不是重复调用HJB优化；先dh=Idh_B.*dh_B+Idh_F.*dh_F，再s=(1-tau)*w*zzz.*l+Rb.*bbb+Tt-Cmin-dh-HANK3_cost(...)-C，然后mh=dh+Rah.*aaah。特别注意这里使用原迭代末次保存的C,l,dh/Idh，不能静默当作新收敛值函数的重新优化政策。
C. 第265–267行post b率：X=-min(s,0)/db；Y=min(s,0)/db-max(s,0)/db；Z=max(s,0)/db。第268–296行原MATLAB按i+(j-1)*I压平、lowdiag行填X(i+1)、updiag行填Z(i-1)，BB每个z块 = spdiags(center,0)+spdiags([updiag;0],+1)+spdiags([lowdiag;0],-1)。特别在b第I格，不存在第I+1格，正向超界连接不在矩阵中，而中心Y仍保留-max(s,0)/db。如果这组语义和MATLAB spdiags具体shift规则经静态证明成立，则b上界源行对角与内向连线的剩余行和可有 -max(s,0)/db；对应Python边界需逐格对照。b下界在s<0时亦须检查反向超界：可能有min(s,0)/db的行损失。**这是待核的源推论，不是预先科研裁决，也不能忽略a轴、Bswitch或实际s符号。**
D. 第299–301行post a率：chih=-min(mh,0)/dah；yyh=min(mh,0)/dah-max(mh,0)/dah；zetah=max(mh,0)/dah。第302–332行对a方向分别用spdiags(...,0)、spdiags([updiagh;0],+I)、spdiags([lowdiagh;0],-I)装配AAH；在a上下边界也须核对outward rate是否仍在主对角，是否发生行和缺口。第333行A=BB+AAH+Bswitch。原MATLAB没有在该post A重构后执行同等A2max/homecrit断言。
E. 第334–344行KFE：M=I*J*Nz；AT=A'；iFix=floor(.37*M)（MATLAB一基，800→296）；vec(iFix)=.007；用单位行替换AT(iFix,:)；AT\vec；g_stacked按sum(g_stacked)*db*dah归一，然后每z块按MATLAB列优先reshape到(I,J)。**污染行求解成功与原post A' g=0并非同一数学命题**。
F. 第347–354行Lt/Bt/Aht/Ct以grid cell weight db*dah积分，只供静态语义对照，不能重新跑R4 KFE。
静态行证据与全原MATLAB文件认证hash必须一致。若Codex本地无MATLAB原始bytes，请仅把上文指定为GPT认证摘录，不能写LOCAL_MATLAB_BINARY_PARITY_PASS。

## 2. 固定Python逐段对照（只读SOURCE_COMMIT，非R4候选中的新增脚本）

固定源HJB：src/ch5_two_asset_hank/temp31_netwage_hjb.py，Git Blob=56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56
源operator：src/ch5_two_asset_hank/matlab_faithful_operator.py，Git Blob=9a511e151c9bf449412dc5605dfa1a2076711277
源KFE：src/ch5_two_asset_hank/matlab_faithful_kfe.py，Git Blob=4ccb7cec8c4754e91bd8830a95dc533811784391
导出KFE：exports/matlab_faithful_two_asset_ha.py，Git Blob=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf
其他必须查询的source由原R3、R4已发布清单核验，不允许为了报告而编辑任何源。
必须逐段检查：
- Python temp31_netwage_hjb.py的每轮固定value、select_temp31_netwage_local_policy、iteration G、隐式spsolve、停止逻辑和post G组装：post=assemble_source_operator(max(-mu_b,0)/db, max(mu_b,0)/db, max(-mu_a,0)/da, max(mu_a,0)/da, switch_matrix)。是否与原MATLAB 262–264后置源方程/最后政策变量语义等价，不能仅凭变量名推断。
- Python matlab_faithful_operator.py中row=i+j*I+nz*I*J，axis=0时±1、axis=1时±I，off-grid后向/前向offdiag按index保护**不进入矩阵**，但主对角无条件按-(rb+rf)保留。MATLAB spdiags对offset=±1,±I的上下条带、z块拼法、含边界贡献与Python COO/CSR须逐行比对。尤其检验 b upper row 的mu_b>0情形、b lower row的mu_b<0、a上下界可能的mh外流、Bswitch每行和，不能只看单点。
- Python KFE是postG.T，contaminated row index=int(floor(.37*M))-1，rhs=.007，稀疏解+db*da归一+order='F'。要求静态文本对照，不执行任何KFE或替代数值零空间算法。
- MATLAB phi/tau/w传值同Python输入的净综合wt、Rb(b<0)利差和Rah(a)功能等价性，仅可依据既有R3 source identity和最新Owner合同进行有界核对。若税/工资语义或后置s构造无法从已有证据逐项证明，则标PARITY_GAP，不声称全系统验证。

## 3. 重点数学鉴别：行和缺口“源语义可能性”与“实际R4原因”

必须产出source-row case table，固定各轴上下界/内部及positive/negative/zero drift三类，明示对角项、实际合法offdiagonal项、理论row_sum residual expression、对应MATLAB/Python源码位置、证据级别。至少考虑b_lower、b_upper、b_interior、a_lower、a_upper、a_interior及z切换项。不能把- outflow loss表达式先验用于所有状态，也不能把一条边界规则凌驾于实际post G当量之上。
MATLAB原post BB+AAH+Bswitch的总row sum是各轴贡献之和；Bswitch若每行守恒则为0，但实际row/column定向仍需查源la_mat和Python kron约定。不要推断G.T方向与row origin/destination相反。
R4既有只读归档审计公开证据：
- E03 postG max_abs_row_sum=2.840190710841881，非守恒source rows(tol1e-12)=20；postG原驻定残差最大=.32169695841610524，在destination equation row295，另799行约1.249e-16。质量亏损源集中b上边界、z1的a interior状态699/679/659等。
- E04 postG max_abs_row_sum=3.864670056858631，非守恒source rows=29；驻定残差最大=2.9445205842114848，同样destination row295，另799行约7.497e-16。源亏损集中b上边界、z0的299/279/259等。两个点row295这个**source行**本身row sum近0，而原KFE被替换的是**destination equation 295**，不得混淆。
- E03/E04 iteration G行和最大约.0026808411/.0026810554（低于.01），post G行和显著扩大；iteration负offdiag count=11/23，post G负offdiag=0，属于不同矩阵的单独数学风险，不能由post取代iteration判断原MATLAB homecrit。
- R4保存的source rate和row-loss summary不是原MATLAB runtime矩阵/向量，完全原MATLAB至Python逐元素矩阵等价仍未确认。
R5要评估：源MATLAB post spdiags 本身是否在边界超出时保留对角流出、Python是否静态忠实保留相同规则、现有E03/E04的R4非守恒指标是否在方向、边界索引、source row/destination row意义上与推断相容。要把SOURCE_STATIC_SUPPORTS_OUTWARD_DIAGONAL_LEAK 与 ACTUAL_SOURCE_RUNTIME_MATCHED 区分；只有后者才支持全面的原MATLAB行为与Python实际逐元素匹配，本任务无MATLAB运行权限因此不得自称后者通过。

## 4. 仅允许有界的无HA纯符号微校验

主路线为静态源码与代数对照，科学调用=0。允许最多一个no-HA synthetic check round，仅为验证**索引方向及边界行和**的公开小维度玩具（如I=3,J=3,Nz=2，固定人工signed drift），绝不读取R3 LOCAL_ONLY原始800状态数组，绝不导入/调用任何真实HJB/KFE/operator生产求解函数，绝不调用spsolve、稀疏特征求解、policy、root、MATLAB runtime或其他模型。微校验应分别输出手工预期率、有效offdiag与diag、行和以及边界toy例子的符号一致性；一旦需要真正MATLAB spdiags运行/非授权数据/改动既有源码才能判别，则标NOT_TESTED而非另建MATLAB实现。一次微校验失败后不重试/不扩大预算（独立代码检视不计science）。
静态工具只能读取批准的源码和R4公开报告，禁止新跑原经济模型、完整矩阵求解或归档重建。不能把no-HA toy当成原MATLAB 800x800算子逐元素真值，也不能借toy宣称KFE严格驻定通过。
至少交一份source_line_map与source_semantics_case_table，读者可以通过行号/原公式/Python函数位置复核，不得仅用一段自然语言摘要替代代码级证据。

## 5. 具体交付与状态判据

报告必须包含：
1. 原ZIP及.m原件经GPT验过的identity、Codex本地是否拥有合法原始bytes、SOURCE_EXCERPT_ONLY条件、冻结Python commit/tree/Git Blob。
2. MATLAB lines114–119,135–157,185–198,226–239,262–344逐段到Python的路径/行号/函数/表达式映射，逐项分类SOURCE_PARITY_STATIC_MATCH / SOURCE_PARITY_STATIC_DIFFERENCE / SOURCE_EXCERPT_ONLY / NOT_TESTED_RUNTIME，分别为b/a/z、最后policy变量、边界率、稀疏拼装、转置污染行/reshape。
3. b/a边界行和情况表、静态边界toy（若有则限一轮）及toy预算、任何已证明的不对称性。对MATLAB spdiags的偏移和边界逻辑须单独说明是已由源码明确推出、只有推断、还是须MATLAB runtime验证。
4. R4 E03/E04对应负source row sum和origin/destination方程各自的含义；重用R4已发表数值、不新跑HA/KFE；对原方法源内非守恒与Python移植差异至少给出**有界分层结论**。
5. 尚未支持的证据：未运行MATLAB runtime、未重建原MATLAB的真实post A和g、不可完整比较原MATLAB/Python二进制矩阵、未严驻定、原KFE line-replacement不等于所有原方程成立。下一步若需要原MATLAB运行应留OWNER_DECISION_REQUIRED，不能自动执行。
6. Provenance明确为R5静态来源审计，不能复制R2/R3 task标签；现有R1–R4 frozen evidence与黑箱无任何修改、保存历史STOP和隐私。

科研裁决定义：
STATIC_SOURCE_BOUNDARY_SEMANTIC_MATCH仅在逐项源证据充分时允许；FULL_MATLAB_PYTHON_RUNTIME_PARITY=NOT_TESTED；STRICT_STATIONARY_CERTIFICATION=FALSE_INHERITED_R3_R4；SOURCE_METHOD_KFE_COMPUTED_WITH_STATIONARITY_WARNING=UNCHANGED。数学证明某个边界对角缺口与完整经济机制证明必须分开。发现源式与Python静态映射有实质矛盾，报告CHANGES_REQUIRED_FOR_FUTURE_OWNER_DECISION而不是修改程序；证据不足标BLOCKED/NOT_TESTED，不盲判PASS。

## 6. 只允许的新增路径、隐私与交付

唯一可新增独立静态比较校验程序（不修改原科研源）：
validators/multi_province/temp31_matlab_python_post_boundary_r5_static_audit_isolated.py
唯一可新增报告证据目录：
tasks/CH5_TEMP31_MATLAB_PYTHON_POST_OPERATOR_BOUNDARY_SOURCE_PARITY_R5_20261030/ 下source_identity.json、source_line_map.md、post_drift_semantics.md、spdiags_axis_case_table.json、boundary_row_sum_analysis.md、toy_index_receipt.json(仅若获源静态安全许可并实际运行)、original_kfe_row_replacement_map.md、R4_archived_consistency_map.md、matlab_python_parity_gaps.md、result.md、model_budget_zero.json、gap_register.md、privacy_report.md、manifest.json、DELIVERY_FINAL_RECEIPT.json及最小实际静态证据。
所有源、exports、原MATLAB、现有validator/旧task/治理规则/论文Results均只读，不得编辑。不得新增新生产模块、HJB/KFE适配器、边界修复。授权独立安全repo内部从SOURCE_COMMIT建立唯一候选，不得从R4候选或治理branch派生；不建立新repo/worktree，不reset/clean/rebase/force-push或覆盖旧本地未提交证据；不进入受保护P3、locked store、其他私有资源。
预检查治理远端HEAD必须严格为GPT发布后提供的TASK_PUBLICATION_COMMIT，唯一parent=1033b4a0531613093ce13789e3916fd228ae9b5b且diff仅新增本CONTRACT；candidate远端初始不存在，源commit/tree及必要Blob与合同相符。
公开证据须有足够源码片段引用/函数行号/符号证明，不能用无内容的只有hash代替。含私有工作区路径或缓存身份只允许在**公开派生副本**用稳定角色标签，不改变原件；继承R4_DOUBLE_BACKSLASH_BYTES和此前原强制privacy gate，原扫描规则不能关闭、放宽或跳过。payload（含manifest）原隐私扫描真实PASS后才能创建唯一payload commit，正常授权SSH最多一次push并从固定远端读回文件路径、Blob、actual bytes、SHA256、commit/parent/tree；seal唯一新增本任务DELIVERY_FINAL_RECEIPT.json，经同一隐私门PASS后正常SSH最多一次push和全部远端回读。final seal的最终自身份用外置LOCAL_ONLY receipt绑定，无第三commit；SSH未知结果只读消歧，不二次push或改认证/协议。
真实模型数值执行=0，no-HA toy最多1次且不自动retry。若原始MATLAB无安全合法bytes，继续SOURCE_EXCERPT_ONLY有界报告；若源码blob身份或repo安全/隐私/交付无法验证，STOP并报告，有可能不推送。成功交付STOP__AWAITING_GPT_INDEPENDENT_ABC；GPT独立A/B/C后Owner决定是否另授权MATLAB runtime对照或者科研修复。无自动PR/Issue/merge/cleanup/next task。

## 7. 既有正式状态不变

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
