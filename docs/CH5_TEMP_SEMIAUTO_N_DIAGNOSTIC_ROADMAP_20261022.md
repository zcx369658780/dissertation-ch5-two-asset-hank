# CH5 · TEMP人口量纲与宏观价格半自动调参路线（2026-10-22）
STATUS=OWNER_APPROVED_STRATEGY__FIRST_TASK_ISSUE_SEPARATE
FORMAL_V010_UNCHANGED=TRUE
MODEL_ACTIVATION=False
REAL_GE=False
Results=FALSE
V011=NOT_STARTED

## 0. 决策与执行制度（优先于历史“自动下一任务”）
Owner明确提出：宏观价格长期撞上界/下界，优先识别参数、量纲与生产要素比例，不默认求解器有错；先降低人口N，观察短轮次省级价格与资本劳动配置。直到探索出**可能存在稳态的参数区间**前，所有TEMP调参采用“GPT签发一次冻结实验→Codex执行10轮/条件至20轮→Astra独立验收→Owner与GPT对表讨论→Owner再授权下一参数”的半自动循环。**绝不在验收后自动签发/运行下一ARM、下一N或多省扩展**。每次只变一类可解释的自变量，不追求触界数量减少而静默调整数学方程。

## 1. 固定原MATLAB来源与变量边界
对Owner上传原MATLAB zip的`multi_prov_HANK_12sts.m`、`load_GDPdata.m`、`mpHANK_equilibrium_2000.m`、`HANK_mp_1turn.m`、`HANK_firm.m`进行只读确认：
- `POP_multiplier=100`、`GDP_multiplier=1000`，数据中GDP及资本同乘1000、POP同乘100；因而100不能未经单位检查直接判bug；且`load_GDPdata.m`的生产率`Zt_new=Y*K^(-alpha)*N^(alpha-1)`依赖人口标尺。
- 企业端`Kt=Kt_supply+GovInv`，劳动为`Lt_supply`；生产`Y=Zt*K^alpha*L^(1-alpha)`；企业原始工资`wt0=mt*(1-alpha)*Zt*(K/L)^alpha`，总资产回报`ra0=rk-delta+divrate`；实际clip边界`wjt=[0.8,1.3]`、`ra=[0.02,0.09]`，具体clip后值进入后续环节。
- 家庭`rah`来自资本组合及回报桥，家庭工资在不同MATLAB/Python运行层可能是`w`、`wt0`、`w_eff`；不可仅凭“wt”“rah”标签断言其各自是企业边界直接裁切字段。原MATLAB中没有确认到标准命名`Lst`；必须在当前已认证TEMP Python运行源中用代码字段/时点/单位证据寻找“家庭劳动供给”精确对应（如`Lt_HA`）。未找到则报MISSING，不假造Lst。
- `Zt`在首次人口缩放试验中保持原冻结基准**初值/来源**，不重新估计；`GovInv`亦保持原初值，允许原已冻结方程的轮内自主更新并记录，不可偷偷冻结其原有适应规则以制造只有N差异的假象。

## 2. 科学识别与唯一首轮ARM
首轮采用原100轮TEMP已归档的同一**匿名双省合成输入/黑箱来源**，优先确认当时`N_baseline`真实数值及单位，然后令`N_trial=0.5*N_baseline`（与原MATLAB POP_multiplier 100→50 **仅为概念性对照**，不宣称当前双省N恰为100）。其余初始参数、alpha、生产率、资本配置S/lagged raw、税楔、价格边界、GovInv/Zt适应律、HJB/KFE原黑箱、外层阻尼及数值容差保持冻结源一致；如无法确证来源/隔离/执行STOP，停止在NO_SCIENCE_RUN。历史基准100轮只引用已归档原证，同一轮对比需要一致起点/来源，如不可比明确标NOT_COMPARABLE而非重跑一组基准。
单ARM先最多10个完整外层轮，严守来源和预算。第10轮使用**事先记录的描述性工程早停门**：对每轮有效的两省聚合`max KN gap`与`max Y gap`，若第8-10轮均值相对第1-3轮各高出至少20%（分母需为正且数值可靠）并且第6-10轮有至少4轮两省均出现任一种firm原始工资或原始收益越界，标`EARLY_STOP_OBVIOUS_WORSENING`，到10停；如收敛已明确成立可提前停止但仅称TEMP观察；出现安全/E2/非有限/不可比较数据/真正HA硬失败随时立即STOP。其他属于`TREND_NOT_OBVIOUS`，在安全和剩余预算充足、全部HA资格满足的前提下由同一个受控进程追加第11—20轮；**绝对不超过20轮，不自动再试N、Z或边界**。20轮只能显示短期行为，不代表稳态存在/不存在定理；趋势门为实验管理规则，不擅加正式V010数值hard gate。

## 3. 强制两套逐省逐轮表
**价格触界表**：每省每完整轮记录`N`,`Zt`,`GovInv`,`Kt`,`Lt`,`K/L`,`mt`,`alpha`及`ra0`,`ra_used`,`rk`,`divrate`,`wt0`,`wjt_used`,`rah`,家庭实际`wt/w_eff/w`字段名与源；企业clip要以**raw在上下界外/上/下**计算，等于边界的used值不代表raw被裁切，`rah`/家庭`wt`仅以同单位参考带统计并显式`NOT_ACTUAL_CLIP`。全省数：上下界次数/有效轮分母/比例、首触界轮、由正常→上/下界的转折点、持续触界/反复跳出边界、趋势，未完成轮从分母剔除且另报异常。所有比例不可用缺省0顶替。
**量价与家企桥表**：每省逐轮企业`Zt,Kt,Kprivate,GovInv,Lt_firm`对家庭`At(per capita), N*At(total), Lt_HA或实际家庭劳动供给对应(每人和N放大总量)`、跨省`Lt_mat`目的地流入与来源省`Lst`候选，以及`K/L`和家—企差额。关键单位/时间/目的地×来源分离；企业Lt不必等于本地N*HA Lst（跨省迁移），资本需检`Kt=Kprivate+GovInv`与`S[j,i]`守恒。未找到“Lst”不能人工同一化为`Lt_supply`。
必须保留CSV逐轮和Markdown汇总：首轮、5、10、若有15、20及首次跨界等关键节点；两省都单独列。记录10轮决策阈值、用于判定的真实数、stop reason和HA/HJB/KFE资格，另提供说明哪些特征符合`K/L↑→工资↑/资本边际回报↓`等条件性诊断，不能从表格自动拟合新参数。

## 4. 科学与治理硬门
原正式V010 plan、真实31省、原2009历史、资本/税/HA黑箱方程、GovInv0.9/1.1及Zt原算法不改。暂不执行A0-A3、M2真实GE或任何冲击IRF；`Results=FALSE`。`ACTIVE_TASK`仅在独立新合同GitHub发行完成后才为已签发任务；Owner不得成为Codex常规人工传输message bus。
现有B-only候选`f8db0251fb98f2b157affc9bf7391895b86edba0`由Astra已完成独立12/12 ZIP限域PASS，但永久归档GitHub写入曾受平台安全检查阻断，**治理闭环未完成**；Review候选及其它两PENDING都必须保留、不假称清理。调参科学授权与旧审阅治理是不同账，不继承旧预算。
每张受权Codex任务自动发GitHub独立Review三文件（result.md、manifest.json、evidence_sanitized.zip），Astra独立终审、归档readback后精准清理；平台/账号拒绝hard STOP，不能绕过。Owner每次验收后与顾问讨论**下一参数方向**，无自动下一单。
