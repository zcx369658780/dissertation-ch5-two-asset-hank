# CH5 · TEMP人口N×0.5两省价格边界20轮Astra独立终审（2026-10-22）

TASK_ID=CH5_TEMP_V010_SEMIAUTO_N050_PRICE_BOUNDARY_10_20_20261022
CODEX_RUN_ID=a6e047fe0b864ef899ce016e042b43cf
CODEX_REPORTED_TERMINAL=WAIT_ASTRA_AND_OWNER_PARAMETER_DISCUSSION
SCIENCE_TERMINAL=TEMP_MAX20_COMPLETED_NONCONVERGED
ASTRA_REVIEW=PASS__BOUNDED_20_ROUND_PARAMETER_DIAGNOSTIC_EVIDENCE__NO_STEADY_STATE
EVIDENCE_SCOPE=ORIGINAL_ZIP_BYTES_AND_40_CSV_ROWS_AND_FOCUSED_SOURCE_SEMANTICS
SCIENCE_STEADY_STATE=NOT_PASS
HA_STRICT_D_CONVERGENCE=2_OF_40
PRODUCTION_GLOBAL_STOP=UNVERIFIED
RESULTS=FALSE
REVIEW_COMMIT=ae4121b484aa9b0ed1b17be564e15ccbf9fa70ff
REVIEW_TREE=8729489be10469e6ff52a7a6b4cd69941cbb5d3c
REVIEW_SOLE_PARENT=cc8616038c595c302915b736e2f356cef46bc695
REVIEW_BRANCH=review/ch5-temp-n050-price-boundary-10-20-20261022
CLEANUP=ONLY_AFTER_THIS_REPORT_ARCHIVE_REMOTE_READBACK

## 1. 独立原字节身份与公开交付
- Owner上传的`evidence_sanitized(8).zip`实际105869 bytes；Astra本地Python标准库 SHA256=`030fd280abae200139086c93bdbe9b6fe2584a9391b32605bb1735c65f838752`；Git原生Blob SHA1=`edcff4db0bb398f09031d5faf73525e5a5f9663b`。GitHub固定ref下ZIP blob恰相同；ZipFile.testzip=None，31成员、540440 bytes展开、每件真实CRC32/length/SHA256与远端manifest逐项**31/31一致**。无重复/绝对路径/穿越/符号链接/加密，全部JSON解析/公开Python AST静态解析通过。
- GitHub候选 commit `ae4121b484aa9b0ed1b17be564e15ccbf9fa70ff`、tree`8729489be10469e6ff52a7a6b4cd69941cbb5d3c`、唯一parent`cc8616038c595c302915b736e2f356cef46bc695`；compare ahead1 behind0，仅新增`_review_tmp/ch5/temp-n050-price-boundary-10-20-20261022/{result.md,manifest.json,evidence_sanitized.zip}`。另两件Git Blob `eaebe5a385bcabd1b27158040762e7a1ac2b87c3`、`00f670d23d2a7d30efddb42533e6d34f70575613`。
- Owner另上传两CSV，原始字节精确等于ZIP内各文件（SHA256`ef46a974d3a81bb96d8afcf10f3277ee12418571231ea07f245c9f7bb9d24143`和`56ff7f6397a7895398fb9c44ae5d897c5eac423a471d7f907f65ddd23a2791c5`）。两CSV均40条省份×轮次；与ZIP内20行完整`trajectory.jsonl`多列精确同值。
- 公开31成员逐项机器查典型token、Bearer、私钥头、本机绝对路径，无命中；一处通用邮箱regex误命中系Python矩阵运算符`@`表达式，不是邮箱；原私人HA数组/旧私有archive不在公开包内。隐私审阅仅限公开材料。
- 本机最终JSON32777字节SHA256 `682ac4e07d38091443b1fe1411604aaec06c3becc53e453465e46c84a0478c96` 及外部exit0只见Owner报告，Astra并未获得该本地原字节独立复算；ZIP内`budget_audit.json`为**发布前快照**E1=1/direct31/Python6，Owner最终报告E1=2/direct48/Python9，时点不同不能当作矛盾也不能声称独立核对最终计费。

## 2. 试验识别与第10轮条件
冻结匿名两省N=100/160→50/80，同一fixture其余初始输入保持（Zt初值6/6.2，GovInv初值100/120），不重估初始Zt；黑箱源Git Blob`9e7dc9556a2b76811e78f89999abecc045886106`未修改。任务隔离`temp_bridge.py`基于模型`one_turn.py`提取并显式**两处有限调度修改**：允许使用有限但HJB不收敛的TEMP反馈、保留真实`batch.converged`标记；不能冒称生产one_turn原件原样执行或严格HA全部通过。
- 独立按20轮`trajectory.jsonl`复算第1—3轮max KN gap平均1.1846664、8—10轮0.1129538；max Y gap平均0.1256590→0.0467458；第6—10轮有5轮同时企业原始越界。冻结早停门要求两种gap均上升≥20% AND边界≥4，因此10轮**未触发联合恶化门**，允许同一ARM有界继续至20，未有参数自动搜索。
- 20轮完整、HA/HJB进入40、KFE进入40、HJB updates3986、scalar roots32000、science driver1，数据与公开`driver_terminal.json`/`events_summary.json`汇总一致。ZIP不包含约9.75MB原始全部细粒度事件journal，仅有摘要和选录；OS原始过程未由Astra独立复演，不将账本自报升格内核审计。

## 3. 每省上下界次数、量价与因果限度
- 逐省`ra0_raw>0.09`及`wt0_raw>1.30`均**20/20上界真越界**，下界0/20，首次第1轮，区间1—20持续、无进入INSIDE；来自raw比较而非used==边界推断。
- SYN_A: 首轮/末轮`ra0=2.204959→1.400483`、`wt0=4.027497→9.492677`、`Zt=6→5.052473`、`Kt=344.684→707.120`、`Lt_firm=96.892→70.791`、`K/L=3.557→9.989`、`GovInv=100→177.156`、`At(per capita)=2.580→8.691`、`N*HA_labor=46.567→27.861`。
- SYN_B: 首轮/末轮`ra0=1.763114→1.632426`、`wt0=6.563681→11.860346`、`Zt=6.2→5.828560`、`Kt=647.176→811.580`、`Lt_firm=101.956→75.610`、`K/L=6.348→10.734`、`GovInv=120→212.587`、`At(per capita)=8.036→8.680`、`N*HA_labor=69.364→58.009`。
- 每行独立公式检查`Y=Z*K^alpha*L^(1-alpha)`、`raw_wt0=mt*(1-alpha)*Y/L`、`rk=mt*alpha*Y/K`，`Kt-Kprivate-GovInv`最大残差5.7e-14、企业Lt与目的地`Lt_mat`行和残差0、same-S私人资本守恒最大2.3e-13，At×N和家户劳动×N精确。家庭`rah,w_eff`仅参考区间、没有本轮独立实际clip；`Lst=UNMAPPED`。目的地Lt不同于本省`N*Lt_HA`因跨省迁移和源劳动公式不同，不把差额误认为直接不出清证明。
- 第20轮SYN_A/B分别`rk=1.425483/1.657426`、分红`divrate=0/0`、`ra0=1.400483/1.632426`，可见原始高收益主要来自rk项；`mt=1.1806/1.2247`，`Zt=5.0525/5.8286`。K/L增加解释工资方向，但无法单独解释两种价格同时远超上界；应核Zt与mt单位和企业资本/劳动尺度，不自动确定唯一bug或批准新参数。
- HA原始收敛: SYN_A仅轮12、SYN_B仅轮6的source D收敛，2/40；其余38例`SOURCE_MAX100_FINITE_NONCONVERGED`并按原TEMP允许有限postloop KFE，质量受本轮合同审查，不等于严格HA通过。所有轮企业回报触界，末轮最大KN gap0.099982875/Y gap0.107845454，**正式V010共同稳态/目标校准均NOT_PASS**；`Results=FALSE`。

## 4. 禁区与Owner决策
验收为`PASS__BOUNDED_20_ROUND_PARAMETER_DIAGNOSTIC_EVIDENCE`，不是正式M2稳态、生产控制器GLOBAL_STOP、数学收敛定理或因果识别单项Zt效应。正式V010数学、HA黑箱、31省、GE/IRF/政策结果均冻结；科学旧预算不可结转。更早三个review candidates `f8db0251fb98f2b157affc9bf7391895b86edba0`、`4e05976bbc8068b971ba5915133e9a6c3b73193d`、`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c`只读保留。此轮终审永久归档和远端回读完成后，Astra才可精确非强制清理**本轮**review三件并404回读；其它分支绝不清理。
Owner已冻结**半自动参数讨论流程**：Astra必须先与Owner对比每省两份逐轮表与下一最小诊断提议；没有Owner新明确授权，不得自动调`N,Zt,GovInv,mt`、边界、HA方程或执行任何新数值工作。下一参数候选只是讨论：优先检查Zt尺度/mt和家庭raw价格传导，不建议继续盲目降低N。
