# TEMP31 MATLAB原版KFE黑箱：逐项核对、必要最小替换与版本冻结 R1

TASK_ID=CH5_TEMP31_MATLAB_KFE_BLACKBOX_PARITY_FREEZE_R1_20261029
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVED=2026-10-29__REPLACE_PYTHON_KFE_WITH_MATLAB_SOURCE_AND_FREEZE__DIAGNOSTIC_SEPARATION
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=e6241bfa59317c93ef0eeb57d092e5ab3151ca10
TASK_PUBLICATION_COMMIT=EXACT_40_HEX_FILLED_BY_GPT_AFTER_PUBLISH
EXPECTED_GOVERNANCE_REMOTE_HEAD=TASK_PUBLICATION_COMMIT_STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_MATLAB_KFE_BLACKBOX_PARITY_FREEZE_R1_20261029/CONTRACT.md
OWNER_METHOD_FREEZE_PATH=docs/CH5_TEMP31_OWNER_MATLAB_KFE_BLACKBOX_METHOD_FREEZE_20261029.md
OWNER_METHOD_FREEZE_COMMIT=e6241bfa59317c93ef0eeb57d092e5ab3151ca10
CANDIDATE_BRANCH=codex/ch5-temp31-kfe-matlab-blackbox-freeze-r1-20261029
FIXED_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_PARENT=a51c2e7ff6548340a1ee86857b0ee55792fa69b4
SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
SOURCE_KFE_BLOB=4ccb7cec8c4754e91bd8830a95dc533811784391
SOURCE_EXPORT_BLOB=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf
HJB_ALGORITHM_SOURCE_WRITES=0
KFE_ALGORITHM_PATCH_ALLOWED=PROVEN_MATLAB_PARITY_ONLY
REAL_HJB_HA_POLICY_INITIALIZER_ROOT_GE_FIRM_IRF_RUNS=0
KFE_ONLY_ARCHIVED_REPLAYS_MAX=4
NEW_PRICE_POINTS=0
NEW_KFE_DIAGNOSTIC_ACCEPTANCE_DOES_NOT_CHANGE_SOURCE_ALGORITHM=TRUE
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 任务目的与Owner裁决

Owner已决定：整个HA的HJB和KFE内部数学算法必须严格采用原MATLAB HANK_2ASSETS_HJB.m，不允许为改善外部驻定残差、满足更强CTMC约束或制造漂亮结果而修改数学黑箱。KFE原始矩阵驻定残差应在黑箱产出后作为外部独立诊断。当前Python已有MATLAB-faithful KFE代码，因此**先逐行校验，有差异才最小替换；若数学步骤已忠实一致，则保留原字节并正式登记KFE方法/源码Blob冻结候选，禁止无意义的重写**。

本任务只为恢复TEMP31正常数值调试建立可信的KFE原版方法基线和独立诊断输出，**不执行任何新增rah/rb/wt搜索、不改变20x20x2网格/经济参数、不重新跑此前七点HJB、不运行31省、Stage2/Stage3、firm/GE/IRF、真实Excel**。旧七点R1及其GPT独立A/B/C回执必须逐字节保留，不能追溯重写“KFE_NOT_CERTIFIED”。允许另列源KFE方法计算得到的未认证数值结果，不得将其称为已经验证的严格概率稳态或正式论文结果。

## 1. 真实MATLAB与Python冻结身份

原ZIP多省份HANK_matlab原版程序.zip SHA256=ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755；原HANK_2ASSETS_HJB.m=12227 bytes、SHA256=049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae；原multi_prov_HANK_12sts.m SHA256=3c44449cfd4047b5c9e17e540afea2f50b4251150f8f74ab8cceed26e15dec97。GPT已直接从Owner ZIP读取如下原MATLAB行语义；Codex若既有安全隔离仓没有可核验授权MATLAB原字节，必须标MATLAB_RAW_LOCAL_VERIFICATION=NOT_AVAILABLE，仅按冻结逐行摘录对照，禁止访问P3/私有MATLAB/旧locked/shallow/reparse等保护路径、禁止网络额外获取私有MATLAB原件。

HANK_2ASSETS_HJB.m第262–264行：最后一轮真实policy给出dh；再得到
s=(1-tau)*w*zzz.*l + Rb.*bbb + Tt - Cmin - dh - HANK3_cost(...,dh,aaah,0) - C
mh=dh + Rah.*aaah。
第265–333行：用X=-min(s,0)/db、Y=min(s,0)/db-max(s,0)/db、Z=max(s,0)/db重建BB，用chih=-min(mh,0)/dah、yyh=min(mh,0)/dah-max(mh,0)/dah、zetah=max(mh,0)/dah重建AAH；沿MATLAB spdiags +-1、+-I及列优先索引并拼入Bswitch，得到post A=BB+AAH+Bswitch（不是最后HJB隐式迭代的A）。原版第334-344行随后原样：
M=I*J*Nz; AT=A'; iFix=floor(0.37*M); vec=zeros(M,1); vec(iFix)=0.007; AT(iFix,:)=[zeros(1,iFix-1),1,zeros(1,M-iFix)]; g_stacked=AT\vec; g_sum=g_stacked'*ones(M,1)*db*dah; g_stacked=g_stacked./g_sum; reshape前I*J/后I*J到(I,J,Nz)。
20×20×2时M=800，MATLAB一基iFix=296，Python零基=295。第345–354行根据g积分Ct/Lt/Bt/Aht。不得将替换行的求解等式等同于未被替换的原A'g=0。

现有Python冻结源关键原字节：
- src/ch5_two_asset_hank/matlab_faithful_kfe.py Git Blob 4ccb7cec8c4754e91bd8830a95dc533811784391
- exports/matlab_faithful_two_asset_ha.py Git Blob e144c645d3f4dc842c2faa6b93b2ba0e24275dcf
- src/ch5_two_asset_hank/temp31_netwage_hjb.py Git Blob 56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56（只读、不允许修改，line117返回post G）
- src/ch5_two_asset_hank/temp31_netwage_policy.py Git Blob d90eb4ba627d4c702062116c2a4ffadac0f43d86（只读）
- src/ch5_two_asset_hank/temp31_netwage_economics.py Git Blob 30528d55b884c62f3c9785dfe59197a61f125a3c（只读）
- src/ch5_two_asset_hank/matlab_faithful_operator.py Git Blob 9a511e151c9bf449412dc5605dfa1a2076711277（只读）
- src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py Git Blob b82eadea383a4d7546a11d4f19686440f8d71870（只读）。
所有引用源码必须从SOURCE_COMMIT核对Git Blob、必要bytes/SHA256，禁止隐式引用后续任务候选作为正式新科学源；算法快照若无差异就在证据中列为KFE_SOURCE_MATCH_NO_CODE_CHANGE，不能将注释/重排冒称重大算法替换。源数学算法的一致性未全部证实时，必须逐项标PROVEN/BOUNDED/BLOCKED。

## 2. 有界只读对照与必要最小代码授权

静态核对矩阵来自最终dh/s/mh（而不是HJB iteration bb/ab rates）；核对Python post_convergence_operator的生成时序、s与mh的模型数量/税一次应用、边界、post BB/AAH/Bswitch/spdiags的索引含义；特别严禁为了post row-sum问题更改HJB或generator。之后核对原MATLAB与两处Python KFE的transpose、替换行、rhs=.007、spsolve、normalize、Fortran reshape、db*da积分。Python标准库/NumPy/SciPy的布局差异如果存在要记录独立构造的矩阵元素对照与断言；若需要修改HJB/operator或政策经济公式才能匹配，必须STOP该源码修正并登记OWNER_DECISION_REQUIRED，不能越过黑箱。

**条件性唯一允许的既有科研文件写入**：src/ch5_two_asset_hank/matlab_faithful_kfe.py、exports/matlab_faithful_two_asset_ha.py，且只针对其KFE函数和结果类型的**已证明源不等价的最小更正**。禁止修改任一HJB/HA policy/operator/initializer/root/税率/经济与其他KFE实现，禁止创建平行KFE替代算法、改污染行/归一化、加入强制post驻定门到KFE求解函数、在KFE内部clip负密度。若两处核心本来等价，二者必须**保持原Git Blob不变**，仅冻结身份及外部接口策略，避免虚假代码改动。

新允许新增的唯一validator路径：
validators/multi_province/temp31_matlab_kfe_blackbox_parity_freeze_isolated.py
及本次任务证据目录 tasks/CH5_TEMP31_MATLAB_KFE_BLACKBOX_PARITY_FREEZE_R1_20261029/（下述完整交付）。新validator只能做固定源码和KFE回放的隔离对照、source-only KFE成功/严格诊断区分，不得调用HJB/policy/root/initializer或任何前序任务scientific runner，也不得改历史R1代码。不得写任何其他文件。

## 3. KFE-only有限回放与数据可得性

优先仅对上一轮七点R1中四个HJB收敛点P0、P2、P4、P5使用**已存在且可通过上轮任务evidence中LOCAL_ONLY归档SHA256认证**的source post G CSR矩阵及当轮KFE raw/density；只读归档，不能从已提交的标量摘要推测800×800矩阵或捏造原始密度。仅允许safe、非跟随路径内现有LOCAL_ONLY快照，不从旧P3/受保护库提取、不得用任何科学模型重跑重建缺失数据，也不得把LOCAL_ONLY二进制/绝对路径发布GitHub。
若全部4套存在且身份匹配：最多各1次调用冻结KFE函数，最多4个KFE-only scientific solves；不改变原post G，核验MATLAB求解法输出raw、density、normalization、AT污染行及预先归档的同源g/sha、20维a/b边缘与At/Bt。若缺失、疑似旧快照或无法验证则KFE_ONLY_REPLAY=BLOCKED_NOT_AVAILABLE，不假装执行，静态源码对照仍可交付。
如需KFE-only回放，每个点最多1条真实Python监督命令，硬超时30秒，1GiB进程提交内存限制、单活动子进程、六种BLAS等环境变量线程数1，失败后不重试；无法施加监督/资源限额即停止所有求解，报告阻塞。静态对照/纯数组测试可单独进行，但不得通过额外KFE求解绕过4次总预算。
如原MATLAB运行时不可用（预期），不能宣称“已运行MATLAB与Python逐元素差值0”；只能宣称MATLAB字节/公式对照与Python源回放，有界结论。

## 4. 冻结KFE与原始驻定残差的科学分层

从现在起KFE结果必须分成三个独立阶段：
1. MATLAB_KFE_METHOD_EXECUTED：原版定义的post A→转置→单行固定→rhs=.007→稀疏求解→db*da归一→reshape得到有限g。必要时明确报数值异常；此为**来源求解算法执行状态**。
2. ORIGINAL_STATIONARITY_DIAGNOSTIC：对未经污染的postA' g、post行和、概率质量、负质量、边界和内部概率分别记录，包含原封不动的科学风险。残差超过既有1e-7阈值时打STATIONARITY_WARNING，**不能当成第一层MATLAB源算法未执行的证据**。
3. STRICT_ECONOMIC_STATIONARITY_CERTIFIED：若单独要求完全驻定性、正概率等科学门，则按公开预先定义的严格门判断，不可以将仅完成第一层的At/Bt叫作已经认证的稳态经济结果。
以P0/P2/P4/P5原七点R1为固定回归案例：4个HJB达到源阈值，原KFE代码返回有限归一化密度，但post原始驻定残差大，不满足过去额外严格门。**不得篡改旧文件结论**。本任务应生成独立的兼容性状态映射和证据报告：SOURCE_METHOD_COMPUTED_WITH_STATIONARITY_WARNING，外部严格认证仍FALSE；当前项目Owner允许后续基于原MATLAB方法所产生的归档密度开展标有科学警告的**探索性**价格调试，但不得误用为已认证31省稳态或Results。
不要将数值诊断判据塞入Matlab faithful KFE原始求解函数，不允许静默改变调用者中任何先前已批准的严格科学验收；只可在新隔离validator/任务证据定义并展示新的分层结果，未来外层流程接线须另获Owner授权。

## 5. 预算/STOP与文件交付

HA/HJB/policy/initializer/root/GE/firm/IRF及31省调用上限严格为零；KFE_ONLY_SOURCE_REPLAYS≤4；新价格点、非价格结构参数修改、网格变化、来源替换、pip/conda联网安装均为零。当前方法冻结任务不能擅自进入下一轮价格调试，即使KFE核心静态等价或回放通过也STOP等独立验收。
保护原Git身份与各旧任务以及新旧八状态、MATLAB800七点的所有历史结论。旧R1里的KFE_NOT_CERTIFIED与GPT独立审阅报告永不改写，只能新增本任务解释。
必须交付（仅新task目录）result.md、matlab_kfe_exact_line_mapping.md、post_operator_handoff_map.md、matlab_kfe_algorithm_freeze_manifest.json、source_identity.json、original_stationarity_diagnostic_policy.md、four_point_legacy_result_classification.md、bounded_replay_evidence.md、gap_register.md、budget.json、privacy_report.md、manifest.json、DELIVERY_FINAL_RECEIPT.json、若执行则逐点真实脱敏回放logs/receipt，及必要最小隔离测试脚本。每文件列相对路径、Git Blob、真实bytes、SHA256、用途；原字节缺失时清楚给出阻塞，不以hash代替关键数学过程。对源已等价必须出示KFE原src/export源码最终Blob与固定原Blob严格相同的零修改证据。若必要源修正，列逐行diff、依赖影响与原MATLAB行号，科学评价仍待GPT审阅；不得自行宣布所有Python源已正式冻结。
授权候选严格从FIXED_PARENT创建唯一candidate（不能从治理分支或上轮七点candidate接续）；安全独立repo预检和GitHub治理HEAD必须精确等于发布任务的commit，且parent=e6241bfa59317c93ef0eeb57d092e5ab3151ca10、diff仅增本CONTRACT。未经授权不触碰P3、旧lock、历史不安全仓或生成新repo/worktree，禁clean/reset/rebase/force-push/自动merge、改变SSH身份。
仅正常SSH两阶段payload→seal各至多一次push，payload提交后的完整远端commit/parent/tree/文件Blob/bytes/SHA256核对后，再seal仅增DELIVERY_FINAL_RECEIPT.json；外置final readback LOCAL_ONLY。异常先只读消歧，无盲目重试/换协议/凭据。交付后STOP，回报candidate/payload/final SHA、parent/tree、是否修改KFE源及最终Blob、复核证据、真实KFE-only calls、未完成的MATLAB源等价和风险。等待GPT独立A/B/C；不得自动发后续价格任务或修复HJB。

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
