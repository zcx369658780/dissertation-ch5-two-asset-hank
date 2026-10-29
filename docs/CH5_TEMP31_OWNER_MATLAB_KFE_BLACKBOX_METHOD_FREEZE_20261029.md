# TEMP31 Owner新决策：KFE按照MATLAB原版算法纳入黑箱并冻结方法论（2026-10-29）

OWNER_DECISION_DATE=2026-10-29
STATUS=OWNER_MATLAB_KFE_METHOD_FROZEN__PYTHON_IMPLEMENTATION_VERSION_FREEZE_PENDING_INDEPENDENT_REVIEW
ROUTE=TEMP31
AUTHORITY=OWNER_DIRECT
HJB_BLACKBOX=IMMUTABLE
KFE_BLACKBOX_METHOD=MATLAB_SOURCE_AUTHORITATIVE
FORMAL_SOURCE_FREEZE=FALSE
GOVERNANCE_PARENT=bdfd325e9256831d9572fc9ad853fda1bebf0903
RESEARCH_SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
RESEARCH_SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
OWNER_ORIGINAL_MATLAB_ZIP_SHA256=ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755
OWNER_ORIGINAL_HANK_2ASSETS_HJB_M_SHA256=049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae
PYTHON_KFE_SOURCE=src/ch5_two_asset_hank/matlab_faithful_kfe.py
PYTHON_KFE_BLOB_AT_FIXED_SOURCE=4ccb7cec8c4754e91bd8830a95dc533811784391
PYTHON_EXPORT_SOURCE=exports/matlab_faithful_two_asset_ha.py
PYTHON_EXPORT_BLOB_AT_FIXED_SOURCE=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf

## Owner具体要求

1. 本项目HA模块中的HJB与KFE都属于**不可擅自修改的MATLAB原版黑箱算法**。Python适配只允许为实现忠实的MATLAB语义而做有源可追溯的最小改动，不能以更严格的数学生成元条件/驻定残差条件取代原MATLAB求解器，不能通过clip边界率、调整对角、重组概率流、替代线性求解算法去取得“科学通过”。
2. MATLAB原版HANK_2ASSETS_HJB.m第262-264行先使用最后政策的dh、s、mh重算资产漂移；第265-333行用上述**后置**漂移重新构造BB、AAH、Bswitch和A；第334-344行KFE使用A'、iFix=floor(0.37*M)（MATLAB一基下标）、将AT这一行替换为单位行，vec(iFix)=0.007，求AT\vec；然后以sum(g_stacked)*db*dah归一化并按MATLAB列优先顺序reshape至(I,J,Nz)。第345-354行据此积分出Ct、Lt、Bt、Aht等。必须保持完整原顺序、原算子来源和原参数。
3. 原版MATLAB有HJB迭代算子A2max>homecrit(.01) STOP检查，但没有发现**KFE后置post A**重新构造之后同样的行和阈值检查，也没有把未被替换的A'g残差作为求解成功的额外硬门。此前实验另加的maxabs(postA'.g)<=1e-7是本项目的**外部诊断/科学可信度观测**，不得无说明地覆盖原MATLAB KFE成功/返回定义；仍必须准确测量并公开，不能篡改或隐藏。
4. 必须分开状态：
   - HJB_SOURCE_CONVERGED：源值函数迭代收敛；
   - MATLAB_KFE_METHOD_EXECUTED：源KFE线性方程求解、归一化和密度输出得到有限值；
   - KFE_ORIGINAL_STATIONARITY_RESIDUAL_DIAGNOSTIC：未经改行的postA'.g残差与可能的非守恒、负密度等外部观察；
   - ECONOMIC_STATIONARY_CERTIFICATION：若需要严格稳态科学认证，另列结果，不等同于原版方法成功。不能将“源MATLAB KFE返回”和“全部数学稳态条件通过”混同。
5. 2026-10-29已审阅的TEMP31原800状态七点R1：P0/P2/P4/P5原HJB停止达标、MATLAB风格KFE曾返回有限归一密度，但额外原始post驻定门失败；旧报告中的KFE_NOT_CERTIFIED作为**旧外部严格认证结果**保留，不能追溯篡改。未来经源对照后可单列SOURCE_KFE_COMPUTED_WITH_STATIONARITY_WARNING，不等于“完全认证的KFE稳态”或正式31省实证结果。
6. 现有Python src/ch5_two_asset_hank/matlab_faithful_kfe.py以及exports/matlab_faithful_two_asset_ha.py从静态源码看已经包含原MATLAB的转置、替换第floor(.37*M)-1行、rhs=.007、稀疏线性求解、db*da归一及Fortran重排。**没有证实差异就不要重写**，尤其不要将等价算法改成另一种KFE。是否存在post算子生成、spdiags排列或入口接线差异须按原MATLAB真实行和固定Python Blob独立核验，未证部分标BLOCKED而非擅自修正HJB。
7. 本次是**Owner算法方法冻结**，不是已经完成Python代码更新、正式科学来源冻结或经济学结果认证。紧接的任务只能在合同限定的受保护范围中校核/必要最小移植修正KFE及其外部结果语义，完成候选、独立审阅以后才可宣布某一Python代码版本已冻结。
8. 以后回到TEMP31数值调试时维持原版20×20×2(800)网格和所有冻结非内生参数，仅调rah、rb、wt。旧8状态不收敛不能作为经济可行域证据。KFE额外驻定残差即使很大也必须原值公开、作为可信度风险标记，不得为了“通过”而修改黑箱结果。未经Owner批准不得自动续跑价格搜索、Stage2各省劳资映射、Stage3厂商或GE/IRF。
9. 原MATLAB原件位于Owner提供ZIP，Codex若无授权的原始字节，仅可据本冻结逐行摘录做SOURCE_EXCERPT_ONLY，不得访问保护P3/锁仓或另取私有MATLAB。遵守GitHub在线任务单→本地Codex候选→远端严格核验→GPT独立A/B/C→Owner决定的人工流程。

P3=BLOCKED
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
