# 第五章路线图与版本登记

## 2026-10-15 当前：V0.0.9 合成两资产HANK已科研冻结并由Astra单独签发受限HJB/KFE实施授权

**`V009_FROZEN_AND_SEPARATELY_AUTHORIZED__SYNTHETIC_TWO_ASSET_HANK_ONE_PROVINCE_THEN_CONDITIONAL_TWO_PROVINCE__REAL_31_PROVINCE_AND_IRF_CLOSED`**。Owner完整批准E1–E3，[科研采纳](../versions/0.0.9/owner_scientific_adoption.md)与[数学数值冻结计划](../versions/0.0.9/plan.md)已在commit `f7caeb54b13ec977d1b503b124067ae522ca2433` tree `7c51c01cb81b5ca1dfe2124de4de1e3a154e71cf` / plan blob `cb76a840fdd9d1756728189bf29518679831aba6` 完成一次原子发表及远端独立回读；**冻结之后单独签发** [授权文书](../versions/0.0.9/authorization.md) `ASTRA_APPROVED_EXECUTION__CH5_V009__OWNER_ADOPTED_SYNTHETIC_TWO_ASSET_HJB_KFE_STATIONARY_ONLY`，只适用于新独立corrected-model人工1省、经全部门通过后非对称2省的内生HJB/KFE/资产债券/劳动/财政商品稳态数值。基线V008 `d41d229b681e09b913c21deff7a057085b9bc419` tree `88833acf90613380afa30ab8d6ee7e0297e98664`；仅13新增白名单路径、不合并main、不动原D盘dirty和B3。
人工参数/asset grid/init/Zgenerator在计划§3已经首跑前预注册，拒绝因不收敛事后调参。宏观根≤4、家庭新HJB/KFE≤176及8h、根/Scalar root、512MiB/256MiB硬界从实施与聚焦测试总账合并消费，重复失败与final-tree验证计入；动态IRF、24x24/31省正式求解、真实C8文件、历史已耗预算与Results仍0许可。即使软件oracle PASS，若HJB/KFE或市场条件不达标不能宣称合成HANK稳态取得；Codex必须报告失败和STOP。V0.0.10 NOT_STARTED，V1.2工作流/Owner连续委托不修改。

## 2026-10-15 历史：V0.0.9 Owner已批准E1–E3并冻结实施合同（尚未单独签发）

**`V009_FROZEN__OWNER_ADOPTED_SYNTHETIC_TWO_ASSET_HANK_PILOT__WAIT_SEPARATE_BOUNDED_SCIENTIFIC_IMPLEMENTATION_AUTHORIZATION__REAL_HANK_AND_IRF_CLOSED`**。Owner针对V009独立审议的E1–E3整体回复“没问题我批准”；[Owner科研采纳](../versions/0.0.9/owner_scientific_adoption.md)、[V009正式冻结计划](../versions/0.0.9/plan.md)在本次治理提交中封存，均只面向新的`SYNTHETIC_PILOT`，不更改原C8/Frozen historical math。E1: `a`私人基金权益、`b`全国债券均非负、固定S跨省回流R；E2:竞争性零利润firm/全国统一预算/公共资本gross-rental与维护净计价/允许signed财政T；E3:`MODEL_TIME_SYNTHETIC`、准确20×20×2 `(b,a,z)` b-fast及全部人工参数/资产域/初始化前冻结，1省先HJB/KFE/资产债券出清，合格后2省；24维/31省和动态IRF不在本实施里。

唯一新代码候选基线采用V008 `d41d229b681e09b913c21deff7a057085b9bc419` / tree `88833acf90613380afa30ab8d6ee7e0297e98664`，不合并main或修改原D盘8 dirty、untracked、ignored、外置common-dir/B3。正式冻结不是执行许可；待Astra核Git readback后另行签一次8小时受限Python新`reconciled_hank`实施授权，新增最多13白名单路径、最多176次新家庭HJB/KFE、4次宏观求解（1省2、2省2）、8个focused pytest/4个独立科学driver、800状态KFE restricted-gesvd和严格原B/D/Delta/单调/唯一closed-class规则，全面实测账+0真数据。任何算术/科研错误必须STOP而非调参救PASS。
V008原4条path额度与31省roots2/2继续历史已耗，不给新V009 science占用；原C8 A–D REQUEST_ONLY、A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER_UNRESOLVED、Results FALSE旧budget CLOSED保持。V0.0.10 NOT_STARTED；工作流V1.2及Owner连续版次权不变。

## 2026-10-15 历史：V009 SOURCE_ONLY提案已审、当时待Owner E1–E3采纳

**`V009_SOURCE_ONLY_SCIENTIFIC_PROPOSAL_REVIEWED__WAIT_OWNER_NEW_SYNTHETIC_HANK_ECONOMIC_AND_NUMERICAL_BASELINE__NO_SCIENCE_EXECUTION`**。Codex按V009原SOURCE_ONLY只读许可完成53份精确源/合同和隔离治理镜像，零Python/HJB/KFE、零真实受保护原件、零science/模型、零代码候选，回报本地文档blob一致和receipt `22BC74F8EC66C2D77483769DEA4A3512E5BC6DAAAD0C00354FE02F1C8150B75A`；网页仅从GitHub独立确认源blobs，镜像本地读回为Codex回执证据。Astra本轮独立GitHub核V008代码、旧HJB/KFE索引/accepted科学法则，并记录 [V009正式科研审议](../versions/0.0.9/scientific_proposal_review.md)。V009原DRAFT未冻结，V1.2含连续立版规则无需新工作流变更。

科学重点：真正内生`(b,a,z)` HJB、same-Q唯一闭类KFE、CES/单次税/全国财政与资本/债券市场出清，首个合成HANK稳态要与V008给定分布的条件稳态分级。**Astra发现Codex按`I^p=(r+δ)K^p+D`书写的资本基金式在目的省层面一般缺`R_j=Σ_iS_ji A_i(r_ai-r_j)`的固定S跨省再平衡现金流，虽全国ΣR=0，仍须在新模型精确记账/非对称Oracle。**此外原top-level KFE行置换与已采纳exact-positive restricted-gesvd法则不兼容，24×24推广不能沿用800/rank799硬编码。

E1资产产权(人工a权益、b国家债权/新收益无旧clip)、E2企业竞争性零利润/全国政府/signed转移/公共资本融资、E3人工时间与参数、20×20×2首次真正HJB/KFE数值及网格推广，是**新的高风险Owner经济/科学选择**；据持续授权须停Owner一次裁决，不能擅自实施。V008代码建议基线`d41d229b681e09b913c21deff7a057085b9bc419`仍PROPOSED，旧数据C8 A–D REQUEST_ONLY、A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER_UNRESOLVED/Results FALSE、旧science预算CLOSED不变。V0.0.10 NOT_STARTED。
## 2026-10-15 历史：Owner连续授权生效且V009初启版前DRAFT

**`OWNER_STARTED__V009_DRAFT__WAIT_CODEX_FULL_CORRECTED_HANK_STEADY_STATE_AND_DYNAMIC_CLOSURE_PROPOSAL__NO_SCIENCE_EXECUTION_OR_REAL_READ_AUTHORIZED`**。Owner于V0.0.8独立ACCEPT/CLOSED后授权继续下一科研长版，并授予**连续长版本的版前自动启动委托**：无新的工作流/重大科学/高风险权限决策时，Astra每轮验收和归档后直接开始下一DRAFT+SOURCE_ONLY一次任务，不再反复问Owner是否继续；若需**改工作流**则`STOP_AND_NOTIFY_OWNER__WORKFLOW_CHANGE_REQUIRED`并让Codex按Owner批准在隔离位置同步文件。权威决定见 [Owner 2026-10-15长期委托](CH5_OWNER_CONTINUOUS_VERSION_DIRECTIVE_20261015.md) 与 [V1.2限域工作规则](CH5_ASTRA_WORKFLOW_CURRENT.md)，没有授权后台、自动编程、真实protected读取或新高风险模型调用。

本版[正式启动但未冻结的 V009 DRAFT](../versions/0.0.9/plan.md)，唯一第一任务是Codex针对已接受V008代码候选`d41d229b681e09b913c21deff7a057085b9bc419` tree`88833acf90613380afa30ab8d6ee7e0297e98664`、旧HJB/KFE及历史科学决策开展SOURCE_ONLY集中理论/数值可行性核查，形成完整合成两资产HANK稳态（真正家户优化、KFE、资产/劳动力/全国财政与市场出清）与动态IRF的分级实施闭合方案。V009代码起点建议采用V008但须独立Git/dirty确认，NEXT_BASELINE_ADOPTION=PROPOSED/UNDECIDED；`main`和原D盘8 dirty不能自动覆盖。**实际代码、pytest、HJB/KFE、真数据、GE、IRF的新增执行授权0**；Codex仅获准对新版治理文档做安全隔离mirror同步，不得改原dirty。

V008终态仍`CLOSED__ACCEPT__CORRECTED_SYNTHETIC_ACCOUNTING_CONDITIONAL_STATIONARY_AND_SHOCK_DIAGNOSTIC_ONLY__REAL_HANK_IRF_BLOCKED__WITH_OBSERVATIONS`；旧V008路径4/4、31省roots2/2等全归旧封闭账，历史 C8 A–D真实文件REQUEST_ONLY、A16/window/C9/CALL_LEDGER与Results FALSE仍严格不变。V0.0.10 NOT_STARTED。

## 2026-10-15 历史：V0.0.8 首次新Python人工稳态/冲击数值闭环受限ACCEPT，正式CLOSED

**`CLOSED__ACCEPT__CORRECTED_SYNTHETIC_ACCOUNTING_CONDITIONAL_STATIONARY_AND_SHOCK_DIAGNOSTIC_ONLY__REAL_HANK_IRF_BLOCKED__WITH_OBSERVATIONS`**。已采纳新corrected CES工资/劳动对偶、全国单次工资税、统一财政人工会计，但未授权real参数/原C8或完整HANK/动态IRF。冻结commit `e222b302176f8ff627ced1442196299f804b9aa7` plan blob `891e8dae2eead0c5c39bf20a7542c68a004b5e94`；V008真实候选 `d41d229b681e09b913c21deff7a057085b9bc419` / tree `88833acf90613380afa30ab8d6ee7e0297e98664` / 唯一parent `d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`，GitHub独立确定恰13个新增白名单和branch readback，无main merge。正式[验收](../versions/0.0.8/acceptance.md)、[复盘](../versions/0.0.8/retrospective.md)。

人工Gate A数值/会计oracle受限通过；Gate B公开1/2/31省条件稳态由Astra独立复算最大经济残差1.18e-12/1.44e-14/9.95e-14；Gate C四条人工单省条件冲击路径140期公开数组独立复算，稳态和条件响应可核，但三坐标于t0/10/20先后注入，非三份独立真实政策IRF；Gate D因动态HJB/KFE、资产/债务/前瞻定价/终态未闭合保持`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE`。Codex本地最终`24 passed, 1 skipped`、pytest5/8、root10/12、31省2/2、paths4/4、原8 dirty/index SHA不变与资源账为CODEX_REPORTED_WITH_LOCAL_RECEIPTS，网页不声称复跑。路径额度已耗尽、最终树skip C是WITH_OBSERVATIONS，不自动豁免或重跑。

A16/window/C9/CALL_LEDGER和旧科学预算仍关；原C8 A–D真实文件REQUEST_ONLY、model_activation=False、Results FALSE。人工条件稳态不等于两资产HANK stationary GE，条件静态shock不等于动态HANK IRF。V0.0.9 NOT_STARTED、下一代码基线UNDECIDED；Owner如欲继续必须另行批准完整HANK/动态scientific gate及其预算，不启用B3/G0/old C9。
## 2026-10-15 历史：Owner正式采纳并冻结V0.0.8人工数值门（执行前）

**`V008_FROZEN__OWNER_ADOPTED_CORRECTED_MODEL__WAIT_SEPARATE_SYNTHETIC_IMPLEMENTATION_AUTHORIZATION__REAL_HANK_AND_IRF_CLOSED`**。Owner已明确同意把Astra提出的L1 CES劳动指数与严格工资对偶、全国一税一次计价、统一全国政府账户、AtTax暂不定归属和静态/稳态先行研究路线落实到Python，并希望实测稳态与IRF。正式版固定 [V008计划](../versions/0.0.8/plan.md)，只允许**新的隔离 corrected-model + 独立人工经济体 Gate A经济oracle、Gate B条件稳态、Gate C条件冲击路径、Gate D动态IRF准入诊断**；必须由Astra在冻结提交远端readback后另行签发受界实施授权。合成人工稳态不能标为2018真实31省双资产HANK GE，逐期条件冲击不得冒充前瞻性HANK IRF。

代码基线采用V007 candidate `d8bb49d86ea674ea4ff5e3fdf03929baa08a6514` tree `9b685397ad5bc76a4ac3bf4203776389742c5ec5`，不合并main/原本地dirty。迁移sigma、AtTax三种归属、国有资本clip等**尚未被Owner实际经济归属采纳**，仅允许明确人工枚举/零值测试，错误单位/重复分录默认拒绝。Old HJB/KFE/C8/C9/原数据/真实IRF预算仍0。历史IRF旧`mpHANK_shock_2000.m`逐期单次调用并不证明完整动态最优条件，结果等级分账。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE持续；V009 NOT_STARTED。

## 2026-10-15 历史：V0.0.8 理论方案独立审议完毕、当时待Owner科学方向选择

**`V008_SOURCE_ONLY_THEORY_PROPOSAL_REVIEWED__WAIT_OWNER_CORRECTED_MODEL_CHOICE__NO_IMPLEMENTATION_OR_REAL_READ`**。Owner启动V008后Codex交付一份跨博士论文/MATLAB/Python/历史接受/理论的SOURCE_ONLY集中提案；Astra已独立核当前PDF p94–97、原MATLAB关键成员、GitHub源/历史接受，并发表 [V008方案审议](../versions/0.0.8/scientific_proposal_review.md)。Codex对PDF/ZIP当轮未可读的局限仍是执行账真实事实；Astra已独立补读，六份MATLAB源码成员的SHA256与2026-08-30 GE source audit匹配，但不能宣称历史Python C8 execution来自这份ZIP。V008仍是DRAFT，没有冻结经济方程，没有实施授权或真实C8数据许可。

**研究优选而非Owner已采纳**：L1 CES劳动指数+严格双边劳动与工资对偶、全国统一单次工资税、全国统一财政/地区子账、AtTax收入/成本身份分账待证、静态/稳态会计优先；L2真实劳动+外生份额保留对照。历史Lt_prev source repair/2009 parity仅证数值源忠实；论文(5-2)统一税一次、(5-11)双边微观积分×N、(5-16)全国财政与Python不一致。私人raw/公共used/clip的潜在重复会计是条件命题，未与C8 lagged同期间封存。**等待Owner一次性科学方向选择后再冻结。**

V007 `CLOSED`、建议基线`d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`未自动采用或合并main；原D盘8 dirty与B3保护不变。A16/window/C9/CALL_LEDGER、Results及旧预算拒绝依旧，C8 A–D仅REQUEST_ONLY，V0.0.9 NOT_STARTED。
## 2026-10-15 历史：V0.0.8 Owner启动版前跨来源理论核查

**`OWNER_STARTED__V008_DRAFT__WAIT_CODEX_CROSS_SOURCE_ECONOMIC_THEORY_PROPOSAL__NO_MODEL_CHANGE_OR_REAL_READ_AUTHORIZED`**。Owner同意直接进入V008，准许需要时只读查历史科研记忆/接受原件、上传MATLAB ZIP的`.m`文本以及博士论文PDF第五章；指出老MATLAB存在错误，不能作为应当照抄的科学真值。现仅立版、发表 [V008 DRAFT](../versions/0.0.8/plan.md) 和一次Codex SOURCE_ONLY交叉核查任务，**不冻结新方程、不改模型、不给受保护C8真实原件/科学计算权限**。

V007的三个科学义务继续未经济认证：`Lt_prev` 被当前household均值覆盖，对比目的省按N聚合`Lt_supply`；`Govinc` 的`Lt*tau`与`AtTax/Tt`人口桥；不同来源的迭代/模型期与人均/宏观总体。Astra进一步确实查PDF p95(5-2)、p96(5-11)、p97(5-16)、p99表5-1、p101文本及用户MATLAB `HANK_firm.m/HANK_mp_1turn.m/Lt_seperate.m/multi_prov_HANK_12sts.m`，发现论文政府收支与Python财政不完全相同、论文书面预算未明示Tt、PDF delta .0025 vs MATLAB代码 .025、31 vs26文本矛盾，**来源矛盾不是自动接受的修正方案**。请Codex先从独立经济理论+历史采纳+源码给出可证伪修订选择，勿再次堆SOURCE_ONLY接口。

V007已正式 `CLOSED__ACCEPT__HISTORICAL_SOURCE_CROSSWALK_AND_ECONOMIC_UNIT_CRITICAL_OBLIGATIONS_ONLY__WITH_OBSERVATIONS`，候选 `d8bb49d86ea674ea4ff5e3fdf03929baa08a6514` / tree `9b685397ad5bc76a4ac3bf4203776389742c5ec5`；V008拟继承前版但BASELINE_PROPOSED/UNDECIDED，main及本地原dirty不自动合并。Owner Option1、人口/人均不N=P/3、K1/S/C1/HJB/KFE已采纳历史运行继续有效；真实C8 A–D仍REQUEST_ONLY，A16/window/C9/CALL_LEDGER阻断与Results FALSE持续，V0.0.9 NOT_STARTED。
## 2026-10-15 历史：V0.0.7 历史C8来源及经济量纲待证义务有限接受、正式CLOSED

**`CLOSED__ACCEPT__HISTORICAL_SOURCE_CROSSWALK_AND_ECONOMIC_UNIT_CRITICAL_OBLIGATIONS_ONLY__WITH_OBSERVATIONS`**。冻结 `635cea1c54afecc78d6678805a263a889985a291`，plan blob `940ac55265f5ee9bf9b82c3e955f900fbddf32ce`；真实候选 [`d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/d8bb49d86ea674ea4ff5e3fdf03929baa08a6514) / tree `9b685397ad5bc76a4ac3bf4203776389742c5ec5` / parent `198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`，单commit 1 ahead、仅3份新增V007白名单文档，Astra独立GitHub读取并核远端候选branch `codex/ch5-v007-source-unit-audit-20261015`，没有merge main。

Astra独立验收 [V0.0.7正式报告](../versions/0.0.7/acceptance.md)、[复盘](../versions/0.0.7/retrospective.md) 确认：Python在firm前覆写Lt_prev为household均值且当前Lt为migration总供给；household Tt被直接用在地区财政，AtTax为均值；Lt*tau劳动税在工资率解释下缺共同计价。Astra本轮额外只读Owner原MATLAB ZIP对应函数，发现它的`HANK_mp_1turn.m`在household→按N迁移→firm之间没有恢复old firm Lt；它只是辅助源码，不是C8历史执行字节。经济学实际结果/模型BUG、直接单位认证均未证实。Codex 10.5分钟/15,335,719B、保护原dirty/index与最终文档校核为CODEX_REPORTED_WITH_LOCAL_RECEIPTS，网页没有复跑本地命令。

原C8历史manifest SHA独立已接受，但今天原始成员/尺寸/字节未知；A–D累计申请上限1,048,576 / 3,538,944 / 4,046,848 / 4,112,384 B，全部**REQUEST_ONLY**，阶段A也没有新的Owner保护stat/read/hash/parse许可。C9、Objective A16/window、model_activation、Results仍严格停；V0.0.8 NOT_STARTED且NEXT_BASELINE_ADOPTION=UNDECIDED。后续优先是劳动和财政同量纲经济判定，真实保护来源读取仍需Owner新签门。CH5_WORKFLOW_V1.2不改，原V006/V005科学和行政终态不变。

## 2026-10-15 历史：V0.0.7 SOURCE_ONLY正式冻结/实施前

**`FROZEN__WAIT_CODEX_SOURCE_ONLY_UNIT_RECONCILIATION__REAL_READ_REQUEST_ONLY`**。Owner立版V007后，Codex仅SOURCE_ONLY交付集中原C8来源、经济单位、37文件分期许可建议，Astra独立核实历史独立接收及原MATLAB辅助源码，发现中间预算算术少计NPZ 64KiB并已纠正。正式冻结 [V0.0.7计划](../versions/0.0.7/plan.md)，代码文档候选基线采用上版 `198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`（tree `0c637893d92cafdf72a194b350b3bf7016894d5c`），但原D盘8 dirty/数千untracked和Git外部common-dir不得合并/清理。**冻结不等于实现授权**；此计划读回后才由Astra另行签发CODEX SOURCE_ONLY文档实施许可，真实protected stat/读取/哈希/解析或模型调用许可均0。

V007唯一长任务实质：以已接受历史C8独立SHA anchor和静态生产链为基础，完成MU/NU、At*N、Lt_prev/firm Lt、wage/tau、Govinc税/AtTax/Tt经济单位关键待证义务与Owner决策材料。原MATLAB ZIP用户上传只为辅助文本证据、不是C8历史执行字节。A/B/C/D申请请求最多37个，纠正的四级累计候选数为1,048,576 / 3,538,944 / 4,046,848 / 4,112,384 B，**依然只有REQUEST_ONLY，manifest自身大小未证**。拒绝重复V006 synthetic及G0/B3，正式原始科学/Results闭合未达。

旧A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE及旧science/data/consumer预算CLOSED继续有效。V0.0.8 NOT_STARTED，未经Owner新的经济学和保护访问决定不可启动真实原件/GE。

## 2026-10-14 历史：Owner启动V0.0.7版前DRAFT（已由2026-10-15冻结取代）

**`OWNER_STARTED__V007_DRAFT__WAIT_CODEX_CONSOLIDATED_SOURCE_ONLY_M1_EVIDENCE_PROPOSAL__NO_REAL_READ_OR_IMPLEMENTATION_AUTHORIZED`**。Owner复盘V0.0.6并决定工作流V1.2无必改项目，直接进入V0.0.7。本版本前草案为 [V0.0.7 M1计划](../versions/0.0.7/plan.md)，当前只许可Codex一次集中SOURCE_ONLY文档/代码审阅和科学单位/证据映射；**不是冻结计划，不是代码实施，也不是读取37项真实数据/受保护原件的新授权。**

上版V0.0.6 `CLOSED__ACCEPT__SOURCE_ONLY_IMPLEMENTATION_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`，accepted candidate `198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`、tree `0c637893d92cafdf72a194b350b3bf7016894d5c`，未合main。NEXT_BASELINE_ADOPTION对V0.0.7为PROPOSED/UNDECIDED，需实际Git/dirty审查后冻结。本版聚焦真实original C8 historical anchor、31省五字段/进入态/S/参数、人口与资本劳动工资量纲，和既有37文件（4,112,384B）REQUEST_ONLY的最小分期准入；可读历史公开代码/文档，不得实际打开、stat、哈希、解析真实JSON/NPZ/MAT/CSV、运行模型或恢复旧预算。

现仍A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE；V0.0.5有限关闭/B3非完整可信保护不变；不重启G0、B3/备份或删除。Owner仅授权立版；等Codex集中报告后由Astra科学审议、冻结，再分别处理实现与Owner真实读取许可。

## 2026-10-14 历史：V0.0.6 来源/三轴/双消费者合成工程有限接受并正式关闭

**CLOSED__ACCEPT__SOURCE_ONLY_IMPLEMENTATION_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS**。Owner已正式启动并由Astra独立冻结、授权V0.0.6。冻结commit `4857d9222580b491676cdf75951527eb06d16b49`，plan blob `5c96485f9b70c4c4033675134768b1ff4fe2d188`；实施候选 [`198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/198b70f8b1c7b802bc2e18cb4bb0825bdb495b00)，tree `0c637893d92cafdf72a194b350b3bf7016894d5c`，唯一parent为已接受V0.0.3候选 `cf74384f151427f0b7071ac0461cede6ad6cdf11`。GitHub独立证明8个白名单changed paths、candidate 分支与 remote HEAD、无main merge。正式 [acceptance](../versions/0.0.6/acceptance.md) 和 [retrospective](../versions/0.0.6/retrospective.md) 仅接受 SOURCE_ONLY_IMPLEMENTATION + SYNTHETIC_ENGINEERING（受限）；真实C8来源/经济单位/31省consumer及Results不接受。

Codex本地回报35/40/final40 passed（3/6进程），原工作树dirty/untracked/ignored保护、最终测试和存储/峰值回执皆为CODEX_REPORTED_WITH_LOCAL_RECEIPTS；GitHub代码身份与静态测试设计为INDEPENDENTLY_VERIFIED_GITHUB_CODE。瞬时Git pack内存/存储峰值不能补造为独立证实。未来37文件精确请求仍 REQUEST_ONLY。原 `A16 FAIL_CLOSED`、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、`model_activation=False`、Results FALSE、人口/人均、已采纳K1/C1/HJB/KFE和旧预算CLOSED均保持。V0.0.5终态继续有限行政关闭，B3/G0/清理不重启。

**V0.0.7 NOT_STARTED，NEXT_BASELINE_ADOPTION=UNDECIDED（对后续版本）；candidate接受≠merge main或下一版基线自动采用。** 按CH5_WORKFLOW_V1.2等待Owner下一轮明确立版，不自动签发新科研/真实来源访问授权。

## 2026-10-14 历史：V0.0.6 冻结及执行授权（候选交付前）

**FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_SYNTHETIC_IMPLEMENTATION**。Owner已正式启动 V0.0.6；Codex交付唯一 SOURCE_ONLY 集中静态方案，Astra独立阅读固定GitHub源码、原科学合同并审议，接受静态方案**仅作为受界合成工程基础**；真实C8历史字节、经济单位、运行消费者仍未证实。

**冻结计划：** [V0.0.6 正式计划](../versions/0.0.6/plan.md)，固定 freeze commit \`4857d9222580b491676cdf75951527eb06d16b49\`，plan blob \`5c96485f9b70c4c4033675134768b1ff4fe2d188\`；原DRAFT blob \`40f640a1d9533bfdb3f36241e96d2611c0fdf4dc\` 仅历史。**独立授权：** Astra本次独立聊天签发 \`ASTRA_APPROVED_EXECUTION__CH5_V0.0.6__SOURCE_ONLY_AND_SYNTHETIC_JOINT_BINDING_ONLY\`，生效范围只限上述冻结合同；尚未有Codex后续真正实现、测试或候选PASS证据。

**NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA：** \`cf74384f151427f0b7071ac0461cede6ad6cdf11\`；登记 tree \`372c693ca3dccea716ae8caef382f513e5a2316e\`，执行前Codex需readback。原本地模型 \`a1db8c114dec0ab69d69a5576e153a7f868cba0e\` 与 dirty tracked8（包含 \`government_assets.py\`、\`middle_stage.py\`）不覆盖、不自动合并。main 最近独立回读 \`dd90f41e0daa97cf55fcb2a7a233ee8cd64297ac\`，与候选不同；候选未合并main。未出现V0.0.6实施candidate。

允许仅隔离的完整五字段/三轴/2017→2018及两消费者的SOURCE_ONLY/纯合成接口，最多8小时、6个新 focused 进程、单进程10分钟和新增存储290MiB。受保护真实JSON/NPZ/receipts、旧C8/C9预算、actual consumer、科学HJB/KFE、GE、A16 hostile/旧目录清理均0许可；导入/依赖/输出边界不能证明则相关测试STOP。A16/window/C9/CALL_LEDGER、\`model_activation=False\`、\`Results FALSE\`保持；V0.0.5继续正式有限CLOSED，V0.0.7 NOT_STARTED。候选实现与集中回执返回后由Astra独立最终验收，不因当前冻结/授权宣称M1真实source闭环或科学Results。

## 2026-10-14 历史：V0.0.6 首轮DRAFT、随后已正式冻结并授权

**OWNER_STARTED__V006_DRAFT__WAIT_CODEX_CONSOLIDATED_SOURCE_ONLY_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED**。Owner明确确认回归多省份HANK科研主线、进入V0.0.6，以投稿成果优先战略M1作为本版方向。Astra发布 [V0.0.6 C8来源/31轴/量纲/消费者闭环版前草案](../versions/0.0.6/plan.md)，不是正式冻结/科学运行许可。Codex下一步一次性SOURCE_ONLY静态审阅实际代码HEAD与dirty，复用已接受C8 option1、SOURCE_ONLY axis binding及synthetic工程证据，集中提出 original-C8 receipt/result/batch、model0↔annual1 axis、source/calendar/unit、同annual master两个消费者及producer链具体实现与最小权限方案；无科学数据正文读取、无imports/tests或模型运行。Astra评审后才冻结/授权正式V0.0.6开发。

V0.0.5终态仍[CLOSED有限工程保全、主可信根G0未证](../versions/0.0.5/acceptance.md)，源dirty保护及备份延续而不复跑；原C8 real inputs/lifetime与Objective A未过、A16 FAIL_CLOSED、C9 PAUSED/账未知、Results FALSE/旧预算CLOSED不变。代码基线采用仍UNDECIDED、没有新candidate/main merge事实，不得从文档提交推断。Owner M1科学version开启**不等于**模型activation或真实科研D3/D4来源权限。

## 2026-10-14 会话交接归档（不更改V0.0.6当前权限）

本长会话Owner决定、V0.0.5最终验收/复盘、备份与清理证据等级、低频GitHub V1.2长任务要求、以及**随后已由其他最新治理提交记录的V0.0.6科研版前DRAFT**，集中保存于 [会话交接封存](CH5_CONVERSATION_HANDOFF_20261014_EVENING.md)。该交接为静态证据导航、不包含任何新增科学运行或备份/OS访问权限。最新执行权威仍为本登记最顶部的V0.0.6状态、对应最新冻结/草案和Owner未来明确授权。

## 2026-10-14 V0.0.5关闭、V0.0.6尚未启动时历史状态

**CLOSED__LIMITED_BACKUP_AND_ALIGNMENT_ACCEPTED__MAIN_G0_UNPROVEN__CLEANUP_DEFERRED__WITH_OBSERVATIONS**。Owner交付V0.0.5最终Codex本地对齐/清理分类报告，Astra已核B3冻结与有限验收、GitHub版本状态并审议。最终见[正式终验](../versions/0.0.5/acceptance.md)和[集中复盘](../versions/0.0.5/retrospective.md)。B3备份依Codex回报保全两个源根90,766普通文件/1,804,958,786B，各自SHA256匹配、C隔离Git fsck及5样本有限通过；**外部链接目标/活动链接、全树时间点、ADS/ACL/完整Windows敌对A16均未证明**，证据等级CODEX_REPORTED_WITH_LOCAL_RECEIPTS。

最终Codex汇报仅新增本地3,369B治理对齐说明，原dirty8/staged0保持、untracked 5,947→5,948、ignored4,553不变，**既有本地CURRENT仍是V0.0.2历史时态，不是全文同步**；新说明生成在B3副本之后，不属于旧90,766快照。对B3时点模型源互斥清理分类恰好76,625文件/1,150,549,423B，但缓存候选73文件2,112,602B仍缺依赖与删除名单、POTENTIAL_SAFE_CLEANUP=0；历史证据/active dirty/protected/UNKNOWN全部保留，实际删除/移动/重命名0。两次只读汇总错误已如实记录，后继写入未启动，修正后exit0。

**原V0.0.5主计划DRAFT，不追认为已正式冻结的G0 PASS，主可信可弃用敌对实验根仍BLOCKED/UNPROVEN**；V0.0.4 CLOSED/BLOCKED、D1/D2、科学D3-real/D4-real未授权、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE和旧CLOSED资源账不变。V0.0.6 **NOT_STARTED**；Owner采纳未来投稿成果优先战略，只待本人明确手动启动后续版本。本版后无需再发备份/清理微任务。

## 2026-10-14 B3受限备份通过、最终本地对齐报告尚未交付时历史状态

**V005_B3_CLOSED_LIMITED_ACCEPT__V005_FINAL_ALIGNMENT_AND_CLEANUP_INVENTORY_PENDING__G0_UNPROVEN**。B3 Codex回报已建立唯一C盘快照 C:\CH5_Research_Backup\CH5_B3_IDSAFE_PASSIVE_LINK_20261014_01：两个已批准源根共90,766普通文件/1,804,958,786B均已复制，目标独立SHA256全部90,766匹配、0失败；Windows句柄身份检查9项合成回归PASS及一次canary通过，隔离C盘Git fsck --full exit0/5样本通过；运行942.672秒、exit0、错误/重试0，资源报告未超冻结。Astra逐项核固定B3条件，**正式有限验收见 [B3验收](../versions/0.0.5/b3_acceptance.md)**，本机操作与原回执仅为CODEX_REPORTED_WITH_LOCAL_RECEIPTS、网页未独立校验C盘字节。

唯一reparse目录已保存332B被动描述、外部目标访问0、活动链接不恢复：EXTERNAL_DEPENDENCY_UNBACKED；源集合有限观察稳定、**POINT_IN_TIME_UNPROVEN**，ADS/ACL/完整NTFS恢复未证。不能称全自包含FULL_VERIFIED_BACKUP或A16/Results通过。B3关闭且不自动新增B4备份循环。Codex已做治理只读对齐，但本地CURRENT时态旧、模型树缺2026-10-14论文优先战略文档，旧战略正文还保留B2“进行中”历史时态；GitHub本次合并更新当前前缀，**不覆盖本地原dirty文件**。

V0.0.5主目标可信敌对实验G0仍DRAFT/UNPROVEN；Owner此前要求备份后清理旧版本目录，但目前只有宏观六类，**没有确切安全删除候选**，不授实际删除/移动。下一步仅一次本地治理/清理准确只读分类及对齐建议的集中长任务，然后Astra对V0.0.5作最后限制性关闭；未来V0.0.6须Owner手动启动，按已接受论文成果优先战略规划。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、Results FALSE和旧科学预算不变。

## 2026-10-14 B3结果未返回之前的历史状态

**V005_B2_CLOSED_SAFE_STOP__B3_FROZEN_AWAIT_CHAT_AUTHORIZATION**。Codex B2报告Win Python3.11 DirEntry.stat的st_ino/st_dev/st_nlink全零，与os.stat直接比导致SOURCE_CHANGED_BEFORE_OPEN误报；Python官方文档支持这项API区别，但Astra没有Windows本机源码与原始回执。B2约3.297s exit1，首次源正文打开0（读取额度预扣1），快照/复制/hash/恢复/FS写/Git写均报0，原普通文件汇总90,766/1,804,958,786B不代表源同一时点不变。旧B2的零重试权限已消费、不可原合同重跑。[B2安全停点审议](../versions/0.0.5/b2_acceptance.md)。

Owner要求优先结束**V0.0.5**、从V0.0.6起正式调整科研优先级，并请Codex集中对齐文档，因此Astra在同版内重新[冻结B3纠错+一次补充备份+文档对齐长任务](../versions/0.0.5/b3_identity_correction_backup_plan.md)。必须保留真实身份与句柄守卫，不准直接删除或弱化；先内存聚焦合成回归，后安全准入唯一新C快照，仅保存外链被动描述不接触外部目标，按B2规模上限给**一次独立B3新额度**。实施授权由Astra单独聊天签发，不另开GitHub微提交。若仍BLOCKED则集中收尾V0.0.5，避免自动B4循环。尚未备份任何普通源字节，本地清理删除未获准。原A16/window/C9/Results、科研D3-real/D4-real、V0.0.5 G0及V0.0.6 NOT_STARTED状态不变。

## 2026-10-14 B2回报前的论文成果优先战略历史状态

`OWNER_ADOPTED_PUBLICATION_FIRST__B2_UNCHANGED__NO_NEW_SCIENCE_AUTH`。Owner明确Python/MATLAB都有本地及GitHub程序备份（Owner提供信息、非网页独立全量验证），科研代码保全**无需另找物理隔离卷**；旧“可信可弃用根”属于Windows A16/D2敌对保护实验而非备份要求。Owner同意首篇优先完成科学可信GE/区域外溢及政策反事实，K2/年度动态/IRF/福利按首篇必要性排序。详见 [2026-10-14成果优先路线](CH5_PUBLICATION_FIRST_STRATEGIC_ROADMAP_20261014.md)。首稿估计再约5–8个长版本，非已冻结承诺。

现有B2依据原合同继续，Owner报告正在执行，网页没有独立本机进度；不追改B2或另派备份检查、物理磁盘实验。可规划不触碰protected的科研工作，所有真实科学读取、A16/C9/GE/Results门与旧消耗仍受原科学合同约束。V0.0.5核心G0未证，V0.0.6 NOT_STARTED。

## 2026-10-14 成果优先战略决定前的B2历史状态

`B1_CLOSED__SAFE_STOP__B2_FROZEN_AWAIT_SEPARATE_CHAT_AUTHORIZATION`。Codex B1报告唯一模型目录reparse目标指向两个许可源根以外，按B1 §3A**复制前安全停止**：exit1、2.671秒、目标访问0、快照0、复制/写入/hash/恢复0；Astra核固定B1合同并接受安全停点，运行数值仅Codex本地报告。[B1验收](../versions/0.0.5/b1_acceptance.md)。

Owner明确采纳**方案A**：仅保全项目内该reparse链接自身的类型/链接目标描述，不跟随也不复制外部内容，必须标记外部依赖恢复缺口；此为新B2许可，不追改B1。现已按相同两源根、D3/D4仅备份正文许可、C盘现有保护条件及B0容量实测**一次性固定 [B2长任务合同](../versions/0.0.5/b2_link_descriptor_backup_plan.md)**。B2 允许非覆盖快照内复制普通文件/逐文件hash/Git隔离恢复（文件<=100k、目录<=7k、普通逻辑<=4GiB、2小时、0重试），但不会随自动外链、VSS、提权、删除/清理或科学实验；尚无执行结果。Astra于同会话另行独立实施授权，不为授权增开GitHub微提交。项目外链未包含不能声称完整独立恢复；原科学A16/window/C9/Results与V0.0.5主G0未证保持，V0.0.6 NOT_STARTED。

## 2026-10-14 B1冻结待执行、尚未出现外链阻塞时历史状态

`B0_CLOSED_LIMITED_ACCEPT__B1_FROZEN_AWAIT_SEPARATE_CHAT_AUTHORIZATION`。Codex B0 回报两个固定来源非reparse普通文件90,766、目录6,325、逻辑字节1,804,958,786 B约1.681GiB，C空闲643,058,806,784 B约598.895GiB；10.382秒/exit0/0错误/0重试，**一个目录reparse未跟随、目标及ADS/hardlink/时间点一致性不明**。Astra根据固定B0合同有限验收，Windows实测只属 Codex 报告：[B0验收](../versions/0.0.5/b0_acceptance.md)。

Owner 新明确同意两固定源根内普通文件（含sealed/run004）**仅为保全目的的原字节读取/复制/哈希**，并接受 C盘现有安全配置下可能的明文本地副本；私有清单/日志 LOCAL_ONLY至后续处置，reparse只查自身不跟随，无科学解析、VSS、提权、删除、Windows攻击。Astra据B0实测将 [B1 正式冻结](../versions/0.0.5/b1_backup_copy_verify_plan.md)：100k files /7k dirs /4GiB /2小时、固定唯一 C 盘新快照、全员校验与隔离Git恢复、0自动重试。**单独会话实施授权将引用本次固定 SHA，不另开GitHub微提交**。暂未获B1本地执行结果，实际文件复制数 UNKNOWN/NOT_STARTED，不能宣布备份完成。

原 V0.0.5 核心可信独立实验根研究仍 DRAFT/UNPROVEN，原D2完整威胁模型、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、Results FALSE保持。B1失败、链接/ADS/源一致性不成立须 BLOCKED或PARTIAL，不得跳过后声称全备份。清理仅Owner批准后规划，不批准任何删除/移动；`NEXT_BASELINE_ADOPTION=UNDECIDED`，V0.0.6 NOT_STARTED。

## 2026-10-14 B0冻结待执行时状态（历史）

`B0_FROZEN__OWNER_D3_BACKUP_METADATA_D4_INVENTORY_APPROVED__AWAIT_SEPARATE_CHAT_AUTHORIZATION`。Owner批准在两个固定源根（linked worktree `D:\ProjectTemp\c5k1bturn56` 与外部 Git common-dir `D:\ResearchCode\dissertation-ch5-two-asset-hank\.git`）内受界、**不跟随链接**的元数据登记（含 protected/sealed 的目录项及逻辑大小），以及 `C:\CH5_Research_Backup` 自身状态和一次 C卷空闲查询。固定 [B0冻结合同](../versions/0.0.5/b0_metadata_gate.md)，具体 SHA 以本次 GitHub 固定提交为准；**单独 Astra 实施授权在 Owner/Codex 会话中签发，不再为授权、CURRENT、单个路径另发GitHub提交**。

Owner 明确纠正过去微任务/GitHub频繁提交：恢复 V1.2 的**版本长任务单**；本 B0 由 Codex 在批准范围内一次自主完成并一次集中交付，下一 GitHub 更新尽量与 B1下一实质里程碑合并。B0正文读取/复制/哈希/磁盘修改/真实清理/实验预算全部0；B1需按容量和保护情况再决定，不能自动开始。V0.0.5主G0仍UNPROVEN，D1/D2与A16 FAIL_CLOSED、C9 PAUSED、Results FALSE保持。

## 2026-10-14 B0尚未获Owner批准时状态（历史）

`REVIEWED__ACCEPT_BACKUP_DESIGN__OWNER_B0_METADATA_DECISION_REQUIRED__NO_COPY__NO_CLEANUP`。Astra已审议Codex的完整 SOURCE/CAPACITY/COPY/HASH/RESTORE 方案，确认现用 `D:\ProjectTemp\c5k1bturn56` 属于 linked worktree、外部 Git common-dir `D:\ResearchCode\dissertation-ch5-two-asset-hank\.git` 需纳入备份（两源路径来自 Codex Git 回报，网页无法盘核）。[完整技术审议](../versions/0.0.5/full_backup_review.md)已发布；下一阶段建议单独 B0 元数据登记，包含 protected/sealed 的**目录项与大小等 FS 元数据**，故必须先由 Owner 特别批准 D3-backup-metadata / D4-backup-inventory。当前**不允许实际全树递归探测、正文复制/散列或清理**。

B0之后按实测成员数/S及 C盘容量再讨论 B1 源正文字节权限、快照一致性、敏感副本生命周期、全文件校验和隔离Git恢复。128GiB、6h等纯建议非冻结配额。V0.0.5主 G0信任根仍 DRAFT/UNPROVEN，V0.0.4 CLOSED/BLOCKED；D1/D2和 A16 FAIL_CLOSED、C9 PAUSED、Results FALSE 全保持，V0.0.6 NOT_STARTED。

## 2026-10-14 Owner全量备份已选、Codex设计审议之前状态（历史）

**`OWNER_ADOPTED__FULL_LOCAL_PROJECT_BACKUP__POST_VERIFICATION_CLEANUP_INVENTORY_REQUIRED__NO_COPY_YET`**。Owner 明确希望**整个本地第五章项目**的全量快照，而非只保全 Git tracked，随后清理旧工作流每版创建的冗余子目录。详见 [Owner 全量备份及清理决定](../versions/0.0.5/owner_full_backup_cleanup_decision.md)与[全项目备份/清理新预检草案](../versions/0.0.5/full_project_backup_preflight.md)。备份必须计入 tracked current dirty、所有 untracked/ignored 和所需 Git history，以及受保护历史科研证据的覆盖资格；未获准或无法核验的对象必须作为 **PARTIAL** 披露，不能宣称完整。

**当前尚未实际复制任何本地文件，也未删除或移动任何原目录**。Codex 下一步应只提出源/容量/敏感对象 D3-backup、D4-backup、完整 copy/hash/restore 及清理候选分类方案；网页不能直接操作本地 C/D。完成备份验证之后，可以启动清理盘点，但**实际删除/移动须有精确路径与独立权限**，旧科学来源/dirty/untracked/ignored 默认不可删。备份/清理先行不改变 V0.0.5 可信根 G0 未证，不能把项目目录新子树视为完整 A16 敌对测试根。V0.0.5 主 plan仍 DRAFT，NEXT_BASELINE_ADOPTION=UNDECIDED；D1/D2、A16 FAIL_CLOSED、C9 PAUSED、Results FALSE保持，V0.0.6 NOT_STARTED。

## 2026-10-14 仅要求备份、全量覆盖尚未确定时历史状态

`WAIT_CODEX_BACKUP_SCOPE_PROPOSAL__NO_COPY_AUTHORIZED__V005_MAIN_G0_UNPROVEN`。Owner 明确要求备份到已空建 `C:\CH5_Research_Backup`，完成后直接续接 V0.0.5 可信实验根；并**建议**在当前项目目录新建可弃用测试子目录。当前项目树 `D:\ProjectTemp\c5k1bturn56` 包含 dirty8/数千 untracked/ignored/历史证据，**不能因新子目录而满足完整 D2 对共享祖先与敌对替换的威胁门**，项目内只能作未来普通非敌对 synthetic 测试候选，禁止 destructive fixture。Owner 新指示和风险界限见 [决策记录](../versions/0.0.5/owner_backup_then_fixture_decision.md)。

因备份原文件范围尚未指定，特别是 sealed run004 与本地 dirty/untracked/ignored 的历史访问门**仍关闭**，Astra 未授权全树递归复制。仅允许 Codex 提交[有界来源范围/备份方案 DRAFT](../versions/0.0.5/backup_scope_preflight.md)：优先既有**公开 Git 对象**安全基线、明确本地未备份差异及需独立 Owner 权限的范围。先定 source/bytes/校验/目的规则再单独冻结与执行；网页不可直接操作本地 C/D。此前空目录子门已有限接受，真实文件复制尚未启动。D1/D2保护、A16 FAIL_CLOSED、C9 PAUSED、Results FALSE原样，V0.0.5 主 plan 仍 DRAFT，V0.0.6 NOT_STARTED。

## 2026-10-14 空备份目录创建验收完成、Owner 尚未要求备份时历史状态

**`ACCEPT__SCOPED_EMPTY_BACKUP_DIRECTORY_CREATION__CODEX_REPORTED_ONLY`**。Codex 回报唯一 `C:\CH5_Research_Backup` 已创建：一次 `New-Item`、零重试/无Force，C根/目标/新目录/新目录非递归空检查各1次，普通非reparse目录且当时为空，退出0、错误无、约0.123秒。Astra 已对照冻结与独立授权文档审议；**这些 Windows 操作与零越权计数仅属 Codex 本地脱敏报告，网页不能独立盘核**。详见 [V0.0.5 空目录附属门验收](../versions/0.0.5/backup_directory_acceptance.md)。

本附属门现 `CLOSED__LIMITED_ACCEPT__EMPTY_BACKUP_DIRECTORY_REPORTED_CREATED`，该次 `C:\` 根/目标查询及单次 mkdir 授权均已消费；没有实际数据备份和恢复演练，不能自行开始复制。**V0.0.5 可信可弃用实验根主计划仍 DRAFT/NOT_FROZEN，G0 信任锚尚未证明**；C系统盘/备份目录是不可弃用保全用途，不得做 fixture 破坏性实验。D1/D2、A16 FAIL_CLOSED、C9 PAUSED、Results FALSE及旧资源门保持；`NEXT_BASELINE_ADOPTION=UNDECIDED`，V0.0.6 NOT_STARTED。

## 2026-10-14 子门仅冻结授权、尚未收到创建回报时历史状态

`SCOPED_BACKUP_GATE_FROZEN__ASTRA_APPROVED_EMPTY_DIRECTORY_ONLY__WAIT_CODEX_REPORT`。Owner 确认唯一目标 **`C:\CH5_Research_Backup`**，仅首次创建一个空目录，**不复制文件、不备份模型、不运行任何 fixture**。固定子门 [backup_directory_gate](../versions/0.0.5/backup_directory_gate.md) SHA `13dc04ca85b5a17692871862f5bf25e25a7799fa`，blob `d96af89ce774e39242bd68af11888afee7eb1b3d`；独立 [Astra 限定授权](../versions/0.0.5/backup_directory_authorization.md) SHA `463da12feda60a8efad8e42be0d35068f7a586f2`。仅允许 C卷根及准确目标的限定预检、一尝试 `New-Item`、新目录属性和非递归空状态读回；已存在/冲突/异常立即停止，不覆盖、不删除、不重试、不换目标，任何其它路径/资产操作均0。

**重要：本次仅冻结 V0.0.5 的“建立保全型备份空目录”附属操作门，原可信可弃用攻击实验根研究的 `versions/0.0.5/plan.md` 仍 DRAFT，V0.0.5 **整体未冻结、核心 G0 未解**。C系统盘和新备份目录不可当作可弃用实验卷；D1/D2及原 A16/window/C9/Results 科学保护继续。Codex 交付前目录是否创建 UNKNOWN；网页未直接操作 Windows。NEXT_BASELINE_ADOPTION=UNDECIDED；V0.0.6 NOT_STARTED。

## 2026-10-14 C/D OS拓扑审议完成、备份空目录尚未获准时历史状态

`DRAFT__STORAGE_TOPOLOGY_REVIEWED__BACKUP_AND_FIXTURE_SEPARATE__NOT_FROZEN`。Codex 报告 C/D 各自 Get-Partition、Get-Disk、Get-Volume 六次均退出0、无错误或重试，`C_D_OS_DISK_OBJECTS_DISTINCT=true`；C/D 均为 NVMe/NTFS，C `IsSystem/IsBoot=true`，D 两项=false。**该结果为 Codex 本地脱敏回报，非 Astra 独立 Windows 运行证据**。其 OS 磁盘对象判断支持但不能完全认证 Owner“两独立 SSD”的陈述；更不构成可信可弃用根。详见 [Astra C/D 限定回读审议](../versions/0.0.5/storage_topology_review.md)。

**C盘为系统/启动卷，仅可考虑保全型备份区，不能将 C:/公共祖先/备份区视为可弃用攻击根。** 推荐精确候选备份目录 `C:\CH5_Research_Backup`，尚未 Owner 确认其路径及首次创建范围，不可自行探测或写入；备份内容复制另批。独立 fixture 根仍为 `OWNER_SUPPLIED_ANCHOR_REQUIRED`，可选可信供应的隔离环境（路线 B）但不自动配置。V0.0.5 未冻结，无实现/创建/真实数据访问许可，`NEXT_BASELINE_ADOPTION=UNDECIDED`。D1/D2保持，A16 FAIL_CLOSED、C9 PAUSED、Results FALSE、旧预算均不变，V0.0.6 NOT_STARTED。

## 2026-10-13 C/D 存储映射只读许可、未回报时状态（历史）

`DRAFT__OWNER_APPROVED_C_D_READ_ONLY_TOPOLOGY__WAIT_CODEX_READBACK`。Owner 声明 C/D 位于两块不同物理 SSD（`OWNER_ASSERTED`），明确许可 Windows 内置 Storage 模块至多6次**限定 C/D 的只读磁盘/分区/卷映射**。固定边界：[Owner C/D 查询许可](../versions/0.0.5/owner_cd_topology_read_scope.md)。未核验前不得将盘符或磁盘对象等同独立可弃用实验卷；**C备份区仅用于保全，不能作攻击目标**。无真实数据/目录 ACL 探测、C盘目录首次创建、备份复制或 fixture 调用许可；V0.0.5 不冻结实施。`NEXT_BASELINE_ADOPTION=UNDECIDED`，A16/C9/Results 限制不变。

## 2026-10-13 C盘备份提议、OS拓扑许可发布前的历史状态

**`DRAFT__OWNER_C_BACKUP_NOMINATED__TRUSTED_FIXTURE_ROOT_UNPROVEN__NO_IMPLEMENTATION_AUTHORIZED`**。Owner 表示电脑具有 C/D 两个盘符并允许考虑 C 盘建立**备份区域**，偏好路线 A。已记入 [Owner C盘候选与分区/实验隔离边界](../versions/0.0.5/owner_c_backup_candidate.md)。C/D 盘符不证明物理盘分离；C 若包含 Windows/个人数据则不可把整个卷当作可弃用实验根。**备份区必须保全，绝不能用于攻击 fixture**；实际 C 目录不存在性、安全/卷身份、路径/ACL/重解析未核，不从这项批准推导创建或探测许可。

下一步只准备具体有限的 C 存储拓扑核验与备份区安全建立方案，必要查询/首次创建须另行在 V1.2 冻结并独立授权；旧 run004、模型祖先、V0.0.4 实验均不开。V0.0.5 仍无代码候选，`NEXT_BASELINE_ADOPTION=UNDECIDED`。D1/D2科学保护保持，D3-real/D4-real 未授权，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、Results FALSE、旧预算不变。V0.0.6 NOT_STARTED。

## 2026-10-13 V0.0.5 仅等待外部可信根时状态（历史）

**`REVIEWED__ACCEPT_EXECUTION_PROPOSAL__OWNER_SUPPLIED_ANCHOR_REQUIRED__NO_IMPLEMENTATION_AUTHORIZED`**。Astra 已审议 Codex `V0.0.5_TRUSTED_ROOT_EXECUTION_PROPOSAL_DRAFT`，将 **A（Owner/平台已有可弃用专用卷）+ C（根句柄受限相对创建）** 定为首选，**B（由可信供应方提供独立环境）** 定为备选。其核心前置是能够独立证明首次根身份与全部可变祖先的真实资产隔离，不能靠卷 GUID/目录名/创建后身份自证。完整[版前审议与 Owner 资源待决](../versions/0.0.5/review.md)。

**当前没有 Owner 提供的真实独立资源/供应锚，也没有 V0.0.5 正式冻结/独立实施许可。** 不允许磁盘/根/ACL探测、卷/VM创建、fixture或旧12场景、真实 run004 读取；Codex 无须继续重复只读调查。V0.0.4 `CLOSED/BLOCKED`，旧预算与授权不恢复。D1/D2保持，D3-real/D4-real未批准；`NEXT_BASELINE_ADOPTION=UNDECIDED`，A16 FAIL_CLOSED、C9 PAUSED、Results FALSE不变。V0.0.6 NOT_STARTED。

## 2026-10-13 V0.0.5 版前 DRAFT 等待 Codex（历史）

**状态 `DRAFT__WAIT_CODEX_TRUSTED_ROOT_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`。** Owner 明确要求开启 V0.0.5，解决上版 G0 **可信首次创建锚与可变祖先隔离证明**，而非重复12场景、继续旧 V0.0.4 fixture 执行或自动读取 run004。Astra 发布 [V0.0.5 版前草案](../versions/0.0.5/plan.md)，当前仅 Codex 在已有允许的 SOURCE_ONLY/非破坏性 Git 身份范围内提交**可信根来源路线、证明义务、Owner 最小独立环境选择与后续 bootstrap-only 验收门**；无实施/测试/根探测/隔离环境创建许可。

V0.0.4 `CLOSED__BLOCKED__G0_FIXTURE_ISOLATION_UNPROVEN__NO_EXPERIMENT__WITH_OBSERVATIONS` 且**无代码候选**，旧 D3-fixture/D4-fixture 不延续。候选基线建议追溯 V0.0.3 accepted `cf74384f151427f0b7071ac0461cede6ad6cdf11`、tree `372c693ca3dccea716ae8caef382f513e5a2316e`，但 `NEXT_BASELINE_ADOPTION=UNDECIDED`。D1 北京三文件仅拟核验对象、D2 完整 A16/window 威胁模型继续采纳；D3-real/D4-real 仍未获准，A16/C9/Results 保护不变。V0.0.6 NOT_STARTED。


## 2026-10-13 当前：V0.0.4 按 G0 安全阻塞关闭

**`CLOSED__BLOCKED__G0_FIXTURE_ISOLATION_UNPROVEN__NO_EXPERIMENT__WITH_OBSERVATIONS`**。Codex 报告首次可信创建锚与 fixture 隔离未证明，依冻结 G0 在创建前停下；12场景全部未运行，两项 oracle 未验证，无新代码候选。Astra 接受安全停点，**不接受工程/安全保护 PASS**；本地零操作和原工作树保全仅由 Codex 报告。

[正式验收](../versions/0.0.4/acceptance.md)与[版本复盘](../versions/0.0.4/retrospective.md)已归档。冻结计划 `1b825948e69fcdfd30c1826be023d6963d2e9b25`、blob `d5b6bbfd6b3b7146d2b9ab4a458ab75d666e1a91` 与独立授权 `7955fbbd1a5bc770124d3819a15f70638a4972a2` 不追改。流程偏差：PowerShell 首次 Git tree 表达式失败后仍继续只读检查，违反 V1.2，原样记录。

D1/D2 继续已采纳；D3-real/D4-real 未批准，真实资产 NO_READ；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、Results FALSE 保持。V0.0.5 NOT_STARTED。

## 2026-10-13 V0.0.4 冻结获授权时状态（历史）

**`FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_ISOLATED_FIXTURE`**。Owner D1（历史 run004 北京三元数据拟核验对象）及 D2（完整 Objective A16/window）已采纳；进一步明确批准**实验级 D3-fixture/D4-fixture**，即**仅可弃用人工 fixture 的 Windows 句柄保护试验**及其 LOCAL_ONLY/脱敏证据边界。与真实文件相关的 D3-real/D4-real **没有批准，仍 NO_READ**。

- **不可追改正式冻结计划**：[V0.0.4 plan](../versions/0.0.4/plan.md)，freeze commit **`1b825948e69fcdfd30c1826be023d6963d2e9b25`**、plan blob **`d5b6bbfd6b3b7146d2b9ab4a458ab75d666e1a91`**；原 DRAFT `f5abef37cf7aa5b22c0b918782cc9a28daf60e5a` 在 Git 历史保留。
- **独立执行授权**：[V0.0.4 authorization](../versions/0.0.4/authorization.md)，固定 SHA **`7955fbbd1a5bc770124d3819a15f70638a4972a2`**，裁决 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.4__ISOLATED_SYNTHETIC_FIXTURE_ONLY`。
- **候选代码基线** `NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA`（仅 V0.0.4）：V0.0.3 accepted doc/code candidate `cf74384f151427f0b7071ac0461cede6ad6cdf11`，tree `372c693ca3dccea716ae8caef382f513e5a2316e`；候选分支 `codex/ch5-v0.0.4-isolated-handle-fixture`，仅三份新增代码/测试/报告，**不合并 main/治理分支、不动原工作树 HEAD/index/dirty**。
- 实施前**G0 硬门**：全新的可弃用 fixture、所有可能攻击/改名/替换的祖先必须与真实第五章模型及任何不可弃用共享父目录隔离；**不得对 `D:\ProjectTemp` 公共祖先施加实验攻击**。隔离或合法 API/身份能力不足立即 `BLOCKED__NO_EXPERIMENT`，不能先创建/扫描保护路径/提权/安装工具再争取 PASS。
- **冻结预算**：最多12个场景、每场景60秒/1次启动、每场景最多3个攻击动作/5同步屏障、零自动重试，总实验窗口<=30分钟，最多4同时实验进程。新建 fixture<=4MiB、LOCAL_ONLY原回执<=4MiB、Git index/objects/工具/构建/限定 candidate_view合计<=24MiB、三份公开新文件<=128KiB，总新建<=32.125MiB。严格无真实数据/科学模型/旧 C9 output mutation 执行。
- **D4-fixture** 原始实验日志、安全主体/机器路径/ACL/token 细节保持 LOCAL_ONLY，保留至独立验收，**不自动清理或声称内存物理彻底擦除**；之后存废仍待 Owner 决定。公开仅脱敏场景、API返回分类/次数/覆盖缺口。
- **资格不升级**：最多获得 `ENVIRONMENT_AND_SCENARIO_BOUNDED_FIXTURE_PROTECTION_EVIDENCE`，不证明真正 run004 北京三文件安全可读、原 A16/C9 输出 mutation 四路径全安全或真实科学/Results。V0.0.1–V0.0.3 限定 ACCEPT/CLOSED 不变；`A16 UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、`model_activation=False`、`Results FALSE`、旧预算、人口/人均及不 `N=P/3` 全保持。V0.0.5 NOT_STARTED。

## 2026-10-13 V0.0.4 句柄设计接受、实验未授权时状态（历史）

**`FEASIBILITY_DESIGN_REVIEWED__FIXTURE_GATE_REQUIRES_OWNER_D3_D4__PROTECTION_BLOCKED__NO_READ__NOT_FROZEN`。** Owner D1=选择历史 run004 初始北京三元数据及 D2=保持全部 Objective A16/window 威胁范围仍 ADOPTED。Astra 依据 Microsoft 官方 Windows API 文档及[原 A16/窗口合同](CH5_K1B_C9_OUTPUT_MUTATION_SAFETY_OBJECTIVE_A_OWNER_ADOPTION_20260927.md)核对 Codex `V0.0.4_A16_WINDOW_PROTECTION_FEASIBILITY_DESIGN`，接受**可信根 + 句柄相对打开 + 全链持有**作为 `POTENTIALLY_FEASIBLE/NOT_PROVEN` 的候选。正式[独立可行性审议](../versions/0.0.4/a16_window_feasibility_review.md)记录了旧 Objective A **四种 output mutation** 与新历史元数据**只读窗口**的证据资格不同、不可相互关闭。

**当前仍没有实验 D3/D4 许可、V0.0.4 freeze SHA 或实施授权；真实北京文件 stat/open/read/hash/ACL/probe 与人工 fixture 实验调用均0**。未来若想验证，仅先由 Owner 批准独立、零真实资产、隔离的 fixture D3/D4，再冻结和独立授权；如果环境/祖先隔离不满足则 BLOCKED。D3/D4-real 仍待决，A16 `FAIL_CLOSED`、window `UNACCEPTED`、C9 `PAUSED`、CALL_LEDGER 与 Results FALSE 不变。`NEXT_BASELINE_ADOPTION=UNDECIDED`，V0.0.5 NOT_STARTED。

## 2026-10-13 V0.0.4 D1/D2 采纳后、句柄设计审议前状态（历史）

**`OWNER_D1_D2_ADOPTED__D3_D4_PENDING__PROTECTION_BLOCKED__NO_READ__V0.0.4_NOT_FROZEN`。** Owner 明确选择**历史 run004 初始北京三份元数据**作为拟核验对象（D1），并明确**不缩减完整 Objective A16/window 威胁模型**（D2）；对应正式[Owner D1/D2 采纳记录](../versions/0.0.4/owner_d1_d2_adoption.md)。旧 [Astra 版前审议](../versions/0.0.4/review.md)所写的 D1/D2 待决属于此前快照，现以本条为准。**D3 精确工具/principal/安全证明与保护探测/访问额度、D4 原字节/回执生命周期和公开规则仍待决**。V0.0.4 **没有冻结实施计划或独立执行授权**；不得对历史三目标进行 stat、ACL/reparse/祖先探测、open/read/hash/parse，不得编写读取器、运行测试、模型/科学任务。

Codex 下一步仅可交**有界无资产接触的 Windows A16/window 保护机制技术设计**，重点问是否存在在同用户并发、祖先目录替换与句柄寿命要求下可验证的实现路径；不能用 `resolve/stat/open` 冒充保护证明。未来3次/2.125MiB/零重试仍是**未获 D3 授权的候选预算**。`NEXT_BASELINE_ADOPTION=UNDECIDED`，V0.0.3 accepted code/doc 候选 `cf74384f151427f0b7071ac0461cede6ad6cdf11` 仅推荐。A16 `FAIL_CLOSED`、window `UNACCEPTED`、C9 `PAUSED`、CALL_LEDGER、Results FALSE 不变；V0.0.5 `NOT_STARTED`。

## 2026-10-13 V0.0.4 原审议：D1–D4 当时待决（历史）

**`REVIEWED__OWNER_DECISION_REQUIRED__PROTECTION_BLOCKED__NO_READ__NOT_FROZEN`。** Astra 已将 [V0.0.4 Owner 待决及保护审议](../versions/0.0.4/review.md)归档。Codex `V0.0.4_EXECUTION_PROPOSAL_DRAFT` 推荐历史 run004 初始北京三文件，但现有 A16/window 威胁下的 principal/SID、祖先重解析与句柄生命周期证明及明确访问许可未闭合。**D1选择研究对象、D2保护范围、D3精确访问/保护探测、D4原数据生命周期与对外摘要均待 Owner 决定**；当前不存在 V0.0.4 冻结计划或 `ASTRA_APPROVED_EXECUTION`，且真实数据 stat/open/read/hash、pytest/科学运行的本版许可全部0。

建议基线 `cf74384f151427f0b7071ac0461cede6ad6cdf11` 仍 `NEXT_BASELINE_ADOPTION=UNDECIDED`。未来拟议北京三文件3次/2.125MiB/零重试仅 `REQUEST_ONLY`；`C9 PAUSED`、A16 `FAIL_CLOSED`、window `UNACCEPTED`、`CALL_LEDGER_UNRESOLVED`、Results FALSE 不变。V0.0.5 NOT_STARTED。

## 2026-10-13 V0.0.4 DRAFT 等待 Codex 的历史状态

**`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`**。Owner 已同意启动 V0.0.4，Astra 经 V1.2/前版复盘核查判定：现行规则已包含依赖失败即停，**暂不升级工作流版本**；执行落实问题由下一版方案要求具体 fail-fast 手段。当前仅允许 Codex 有界只读源码/公开科学合同/Git 元数据审查并提交 [V0.0.4 北京历史元数据门草案](../versions/0.0.4/plan.md)所要求的执行方案。

本版目标是把 V0.0.3 的 corrected producer/source 联合合同推进到**可由 Owner 明确选择或拒绝的 run004 北京单省元数据限定读取门**，并判断 A16/window/权限硬门是否可闭合。V0.0.3 候选 `cf74384f151427f0b7071ac0461cede6ad6cdf11`，tree `372c693ca3dccea716ae8caef382f513e5a2316e` 只是新版本推荐基线，`NEXT_BASELINE_ADOPTION=UNDECIDED`。**用户启动 V0.0.4 并非已批准北京3文件读取，候选3次/2.125MiB/零重试仍 REQUEST_ONLY，实际读取0次。** V0.0.1–V0.0.3 已关闭且证据资格不升级；C9、A16/window、CALL_LEDGER、Results、科学预算和人口/人均原则均不变。V0.0.5 NOT_STARTED。


## 2026-10-13 当前：V0.0.3 文档来源合同有限接受并关闭

**终态：`CLOSED__ACCEPT__DOCUMENTARY_SOURCE_CONTRACT_ONLY__WITH_OBSERVATIONS`。** Astra 独立核验固定单父候选 `cf74384f151427f0b7071ac0461cede6ad6cdf11`，tree `372c693ca3dccea716ae8caef382f513e5a2316e`，父 `8f5457947492eef552f4261f8630c6c886af9fa5`，仅三份 `versions/0.0.3/` 新增文档，14/14个固定 GitHub path/blob 引用匹配，并按原冻结标准接受 G1–G4 `DOCUMENTARY_SOURCE_CONTRACT` 范围。文档候选不合并 main；未进行真实数据读取、科学模型或生产接线；网页未亲自重跑 LOCAL_ONLY 文档工具。

- **冻结计划（不追改）**：[plan](../versions/0.0.3/plan.md)，固定 `768a3181fcbc9d367ccce08b1d69458353a48229`、blob `1bf80332586a4e3beeeb355d90b5ec049c7e503c`；[独立授权](../versions/0.0.3/authorization.md) 固定 `2ec13ea41e7bb86eacb19f4601d243a1298bd4bd`。
- **最终归档**：[Astra 独立验收](../versions/0.0.3/acceptance.md)、[偏差复盘](../versions/0.0.3/retrospective.md)；Codex 三文档源码仅在候选 `cf74384f151427f0b7071ac0461cede6ad6cdf11`：[合同](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/producer_source_contract.md)、[Owner 请求](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/owner_read_request.md)、[执行记录](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/execution.md)。勿将这些候选文件相对链接误指向治理文档分支。
- **Codex 本地回执**：最终树文档校验 `exit0`、耗时1.859秒、墙钟 `1303.69/5400s`、总新增 `16,143,662B`，均在分层限额；原 HEAD/index/8 dirty/5915 untracked/4553 ignored 保全为执行端回执，网页无 Windows 原字节重算。最终文档回执 sha256 `5fd3f2abe2f71a9828022bde3403cd65e98aea8f56791b8551629a09dfe581eb`，manifest `c18231495f7eb4045313b36d99b59d2db9dcea66dbb20e5db1ec531662a33523`，仅报告身份，原件 LOCAL_ONLY。
- **保留真实偏差**：命令漏 `import sys` 且两文档误在失败后续写，确实违反 V1.2 的依赖失败即停；初次 checker 没处理 `docs/` 标题前缀。原失败与当时文本保存，后续14/14来源和最终冻结候选文档均通过。V1.2 不因此自动修改，也不将其认作全过程合规。详见正式复盘。
- **Owner 后续选择仍未发生**：run004 北京三文件只是 `REQUEST_ONLY`，建议 3次/2.125MiB/零重试，当前实际读额度仍为0；原资产存在性、子文件 hashes、联合真实认证 `UNKNOWN`。`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`window UNACCEPTED`、`model_activation=False`、`Results FALSE` 与旧 CLOSED 预算、人口/人均、不 `N=P/3` 均不变。V0.0.4 **NOT_STARTED**；不随本版结束自动立版或选下一代码基线。

## 2026-10-13 V0.0.3 已冻结并授权的历史状态

**现行状态 `FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_IMPLEMENTATION`。** Owner 已启动第三个版本；Codex 提交并停止于 `V0.0.3_EXECUTION_PROPOSAL_DRAFT`，Astra 核实 corrected producer/run004 历史接受及当前 GitHub 源码后采纳 `DOCUMENT_ONLY` 三文件方案、无科学/真实数据许可的决策包。该状态**只代表文档实施有权限，尚无 Codex 写入、通过测试或候选结果可接受**。

- 正式冻结计划：[V0.0.3 plan](../versions/0.0.3/plan.md)；**固定 freeze SHA `768a3181fcbc9d367ccce08b1d69458353a48229`**，plan blob `1bf80332586a4e3beeeb355d90b5ec049c7e503c`。旧 DRAFT `7c00b7d301550d712cecc5bc8ccdf00f69056818` 仅 Git 历史。
- Astra 独立实施授权：[V0.0.3 authorization](../versions/0.0.3/authorization.md)；固定提交 `2ec13ea41e7bb86eacb19f4601d243a1298bd4bd`；裁决 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.3__DOCUMENT_ONLY`。
- 本版固定 `NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA`：单父候选起点 **V0.0.2 accepted commit `8f5457947492eef552f4261f8630c6c886af9fa5`**，tree `af2a6a3d85f7525d480ad7da1916eaa25bf349b1`；独立候选分支 `codex/ch5-v0.0.3-corrected-producer-contract`。这不等于合并 main、修改本地原 checkout/dirty 或真实来源晋级。
- 仅新增三个文档：`versions/0.0.3/producer_source_contract.md`、`owner_read_request.md`、`execution.md`；Astra 负责后续最终验收与复盘。无代码、validators、test、真实 source-loader 或默认生产修改。
- **本版硬预算**：总墙钟<=90分钟；pytest/HJB/KFE/31省消费者/C8/C9/C10/旧任务/真实 protected 文件读取 **均0**。新增存储：Git操作32MiB、三文档 candidate_view 1MiB、LOCAL_ONLY回执2MiB、公开文档128KiB、总35.125MiB；失败后 fail-fast、UTF-8/LF、精确候选树/单父远端回读。
- **run004 北京未来拟议读取包只是 Owner 待决 `REQUEST_ONLY`**：三个特定文件、候选3次/2.125MiB/零重试是未来申请条件，**不是 V0.0.3 的实际读取许可或当前盘存在/哈希验证**。历史 run004 31/31 HJB/KFE/aggregate 接受只在原实验范围成立。
- V0.0.1 与 V0.0.2 继续原限定 ACCEPT/CLOSED；`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`window UNACCEPTED`、`model_activation=False`、`Results FALSE`、全部旧 CLOSED 科学/数据预算和人口/人均不 `N=P/3` 不变。V0.0.4 NOT_STARTED。真实认证、劳动人口经济量纲、外部年份价格仍 UNKNOWN。

## 2026-10-13 V0.0.3 版前 DRAFT 状态（历史，未授权实施）

`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`。Owner 已明确启动 V0.0.3；Astra 已发布 [V0.0.3 corrected producer 联合身份与安全读取草案](../versions/0.0.3/plan.md)。Codex **仅只读**编制执行方案；暂无冻结计划、独立实施许可、模型/tests 或真实 protected 文件读取权。V0.0.1 与 V0.0.2 均按原限定资格 ACCEPT/CLOSED；V0.0.2 固定候选 `8f5457947492eef552f4261f8630c6c886af9fa5` 仅为建议下一版代码/文档来源基线，`NEXT_BASELINE_ADOPTION=UNDECIDED`，原工作树与 main 不作自动合并。

本版针对真实 corrected producer 的 policy/mass/Q/checkpoint/收益/省份联合身份合同与 Owner 最小受保护读取申请包，**不再叠加模拟 seal**。旧 `C9 PAUSED`、A16 `FAIL_CLOSED`、`CALL_LEDGER_UNRESOLVED`、`Results FALSE`、人口/人均决策及所有旧数据/科学 0 新许可均保持。V0.0.4 NOT_STARTED。


## V1.2 后续交付与证据登记补充（2026-10-13，规范性说明）

本节为 V0.0.2 复盘后的**长期治理规则**，补充 V1.1 登记要求，不改变 V0.0.1 / V0.0.2 冻结计划、实施授权、已有执行报告、验收和复盘原件。**V0.0.3 是否启动仍以最近状态与 Owner 指令为准**，本段不构成派单。

后续版本的原登记字段继续有效；执行交付另外分开记录：①前置依赖命令是否 fail-fast，以及发生失败后实际继续/停止的路径；②新文本记录的 UTF-8/LF 与最终 Git 差异检查情况，编码/显示错误单独分账；③ `PRE_FINAL` 公开摘要与**终端候选 tree/commit** 的身份、最终运行进程/退出码、私有或可发布交付回执 SHA 的区别（不得自引用候选哈希）；④首次及其后每次 focused 测试的可测资源记录与不可测 `UNKNOWN`，禁止追填缺失历史值；⑤候选基线是否已经包含前版被接受的代码，与 `main` 是否合并仍单独证实。

以上是**每版本依实际复杂程度提交的简明证据项**，不新增固定测试次数、额外审批角色、额外候选推送或强制第三方验收。实际独立阅读 GitHub 源码/commit/测试设计与本地执行方报告的 raw receipts 必须区别；存在无法获取的原始终端回执时，按证据限制验收，不把测试摘要哈希冒充独立重跑。具体流程详见 [V1.2工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)。


## 2026-10-13 当前：V0.0.2 最终有限接受并关闭

**终态 `CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`。** Astra 依据不可追改冻结计划 `4b11c46823e7cdabc12de8b8036cc5efc2380c52` / blob `43171bc6b841695845e7576d7feaa3135b88c588` 与实施授权 `3ed139aee7563a7033fa02fb933c3b49f24bd6b1` 对 Codex 候选作了 GitHub 独立静态审查。候选 commit `8f5457947492eef552f4261f8630c6c886af9fa5`、tree `af2a6a3d85f7525d480ad7da1916eaa25bf349b1`、唯一 parent `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`，分支 `codex/ch5-v0.0.2-household-source-contract`，只新增五个已授权源码/测试/证据路径；候选不合并 main。

- 正式冻结：[V0.0.2 计划](../versions/0.0.2/plan.md)；[独立授权](../versions/0.0.2/authorization.md)；[Astra 验收](../versions/0.0.2/acceptance.md)；[版本复盘](../versions/0.0.2/retrospective.md)。执行文件仅存在候选代码提交： [crosswalk](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/source_crosswalk.md) / [execution](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/execution.md) / [public JSON summary](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/acceptance_summary.json)。
- Codex 集中报告精确树测试 `62 passed, exit0`、总 focused 进程 `6/12`、含保守起始计费时间 `2810.44/10800s`、本版存储 `26,887,236/176,422,912B`；这些运行/原 checkout 完整保全为 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，网页独立只核 GitHub 代码、测试和公开报告，不冒称亲自重跑/读取本机原始 JUnit。
- 公开摘要在最终准确树测试前封存，未内含最终测试/提交身份；第六次运行及两项最终私有 receipt SHA 由 Codex/Owner 额外交付。run01/02 RSS UNKNOWN、CRLF/GBK/UTF-8 与第5次中间树误续测等真实偏差见验收和复盘。
- 本版只是内部 simulated digest/seal 与合成 typed contract，通过不证明外部 REAL 源身份、protected asset 联合真实性、真正家户运行或经济单位；`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE`、旧 CLOSED 预算、人口/人均与不 `N=P/3` 均保持。
- `NEXT_BASELINE_ADOPTION` 对 **V0.0.2** 已固定从 `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4` 采用；**V0.0.3** 尚未启动且尚未选定代码基线。接受候选不等于已合并 main 或未来一定采用该候选；Owner 以后明确启动新版本后才另行决定。

## 2026-10-13 V0.0.2 冻结及授权状态（历史，非现行）

- **状态**：`FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_IMPLEMENTATION`。Owner 已启动 V0.0.2 版前规划，Codex 提交完整 `V0.0.2_EXECUTION_PROPOSAL_DRAFT`，Astra 审议后选择窄合成 source-boundary，完成冻结和独立实施授权。此状态仅说明可以启动受限工程，**尚无实施、测试或候选的通过证据**。
- **正式不可追改计划**：[V0.0.2 plan](../versions/0.0.2/plan.md)，固定 freeze SHA `4b11c46823e7cdabc12de8b8036cc5efc2380c52`，plan blob `43171bc6b841695845e7576d7feaa3135b88c588`。版前草稿存于历史固定提交 `5cfe41fd0a66877565accca3c8e7dc9a71fa35ee`，不是现行执行合同。
- **独立实施许可**：[V0.0.2 authorization](../versions/0.0.2/authorization.md)，固定提交 `3ed139aee7563a7033fa02fb933c3b49f24bd6b1`；裁决 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.2__SYNTHETIC_SOURCE_CONTRACT_ONLY`。
- **代码基线** `NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA`：前一版合成工程已接受的 commit `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`，tree `39e7a91ca473ba770bd65518607c3f78f4b9fe24`。仅作为本版本精确新候选树起点，**不合并 main、不移动原本地分支/HEAD/index**；远端目前不得假称 main 已包含。
- **文件/分层预算**：仅新增来源 metadata 工程模块与 focused 测试，以及 `versions/0.0.2/source_crosswalk.md`、`execution.md`、`acceptance_summary.json`；候选分支 `codex/ch5-v0.0.2-household-source-contract`。工程上限3小时、最多12次 focused pytest/次<=120秒、目标单进程1GiB。新增存储128MiB Git 操作 +32MiB isolated candidate_view/fixture +8MiB LOCAL_ONLY回执 +256KiB公开脱敏报告，合计<=168.25MiB。**真实科学/受保护数据/旧任务预算 0**。
- **科学资格上限**：仅 `SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING`；真实 producer、真实数据/31省、HJB/KFE、C8/C9/C10、GE、Results、生产均非本版目标且不授权。只有明示 `SYNTHETIC/NOT_REAL_SOURCE` 准入，模拟 seal/hash 不能证明真实性。人口/人均保留、户均封存、不 `N=P/3`。旧 `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE` 与 CLOSED 预算不变。
- **候选执行与终态**：Codex 版本内无实时监督自主管理合成工程，在冻结标准内修复与集中交付；仅正常 non-force push 受限候选一次并准确 readback。执行报告/最终候选 SHA/tree、Astra acceptance/retrospective 均 **NOT_YET_AVAILABLE**；收到候选后独立审议，不预先接受、不自动启 V0.0.3。

## 2026-10-13 V0.0.2 版前 DRAFT 记录（历史，不能用作执行授权）

Owner 已确认 V0.0.1 的收尾完成，并于本轮**手动要求开始下一版本规划**。Astra 草案：[V0.0.2 来源契约与输入准入计划](../versions/0.0.2/plan.md)。当前 `DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`；Codex 仅可对已授权源码做有限只读核查并交一份执行方案草稿。版本尚未冻结、未颁布独立实施许可、没有新模型运行或新测试授权。

V0.0.1 `CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`；其 accepted candidate SHA `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4` 与原代码基线、`main` 均须分开记录。`NEXT_BASELINE_ADOPTION=UNDECIDED`，候选默认不合并、不切换、不等于正式下一版代码基线。Owner 未采纳新的真实科学/数据执行许可，C9/Results/A16/ledger/未知经济单位照旧。


## V1.1 后续版本登记约定（2026-10-13，规范性说明）

本规则在 V0.0.1 `CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS` 后生效，**不重写该版的冻结计划、验收、复盘或历史版本登记**；新版本未启动。与旧记录中“待创建”的时态冲突时，优先按上方最近状态判读。

每个新版本由 Owner 明确启动；至少登记：版本 ID/状态及 Owner 启动出处、Astra 草案与 Codex 执行方案、**正式冻结计划的不可变 SHA/blob**、授权 SHA/边界、模型代码基线 commit/tree、真实模型 worktree/remote、候选 commit/tree 与分支、允许的变更路径、明确独立的工程/科学/数据/操作性存储/脱敏证据预算、测试与证据资格、执行报告和原始本地回执身份、Astra 独立验收、复盘及终态。没有必要的资源上限可写 NOT_APPLICABLE，不为形式主义机械复制旧预算。

**增加独立字段 `NEXT_BASELINE_ADOPTION`**：`UNDECIDED` / `ADOPTED_FROM_EXACT_SHA` / `NOT_ADOPTED`，含依据和固定 commit；候选接受不自动意味着进入 `main` 或下一版代码基线。可分开登记 `MERGED_TO_MAIN` 的实际 Git 证明，缺失则 `NOT_MERGED/UNKNOWN`。文档分支与代码分支分离时，执行报告必须链接其**真实存在的固定候选 commit**，不能使用指向文档分支而不存在文件的相对路径。

集中交付至少含实际代码与 Git 可核身份、简短脱敏测试/资源/保护摘要及私有原始回执的哈希和访问界限；Astra 在验收中显式区分 `INDEPENDENTLY_VERIFIED_GITHUB_CODE`、`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`、`UNKNOWN`。失败、Owner 限定例外及预算使用如实累积记录，冻结计划不事后重写。详见 [V1.1工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)。


## 2026-10-13 现行：V0.0.1 最终接受并关闭

- **状态：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`**。Astra 已独立核对 Github 固定候选身份、三文件增量、源码/测试与执行报告，接受合成工程范围，保留本地原始回执未直接复核的局限。
- 正式冻结计划（绝不追改）：[V0.0.1 plan](../versions/0.0.1/plan.md)，冻结提交 `6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8`，blob `065cfaf699db99f36d0fb05f037986ba22479298`。
- 独立实施授权：[authorization](../versions/0.0.1/authorization.md)，提交 `837b99dff12f1b263fd7f4b80c43e19cf4efaa48`。
- Codex 代码候选：[3260ec393dd4d53d6aab6c34d7c0442f09aa79f4](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4)，tree `39e7a91ca473ba770bd65518607c3f78f4b9fe24`，分支 `codex/ch5-v0.0.1-synthetic-household-bridge`，与原代码基线 `a1db8c114dec0ab69d69a5576e153a7f868cba0e` 直接相邻；仅新增合成源码、测试与脱敏 execution。
- Astra 最终结果：[独立验收](../versions/0.0.1/acceptance.md)；[偏差复盘](../versions/0.0.1/retrospective.md)；[执行报告](../versions/0.0.1/execution.md) **仅存在于独立候选分支**，此处应读固定候选链接：https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4/versions/0.0.1/execution.md 。勿将相对路径误认文档分支中已拥有该文件。
- Codex 报告 candidate_view 42/42 通过、4/8 focused 进程、最终新 EVIDENCE≈1.87MiB、墙钟≈21分钟；网页独立核查源码/42例静态设计及 Git SHA，但未直接复跑 Windows 私有 raw receipts。初始临时 Git index 超10MiB证据配额真实失败，后获 Owner 受限运维修正后恢复，未追改冻结科学/工程标准；记录于验收/复盘。
- 本版**不支持** HJB/KFE/31省来源真实性、经济劳动单位、真实生产 callback、K1B/GE/收敛、Results、发布。旧 `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE`、旧预算和人口/人均决定保持；生产未接受。
- **下一版 NOT_STARTED、没有 ISSUED、没有自动派单。** 后续路线由 Owner 新指令另行启动版前协商。候选 branch 不自动 merge main。当前本地脏工作区及未跟踪资产不由本网页验收追认其字节完整性。

## 2026-10-13 V0.0.1 立版与实施记录（历史）

- **版本 `0.0.1`：`FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_IMPLEMENTATION`。** Owner 启动第三阶段；Codex 已提交 `V0.0.1_EXECUTION_PROPOSAL_DRAFT`，Astra 审议后批准其纯合成工程方案。
- **不可修改的正式冻结计划**：[V0.0.1 plan](../versions/0.0.1/plan.md)；冻结提交 `6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8`，plan blob `065cfaf699db99f36d0fb05f037986ba22479298`。
- **独立实施许可**：[authorization](../versions/0.0.1/authorization.md)；发布提交 `837b99dff12f1b263fd7f4b80c43e19cf4efaa48`，其中含 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.1__SYNTHETIC_HOUSEHOLD_BRIDGE_ONLY`。
- 代码基线截点 `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，本地既有 dirty/untracked/ignored 不包含在该 SHA，Codex 启动前须 fresh-readback 与保护。
- 本版本仅准新的显式合成模块/测试、受控 isolated candidate_view、专属本地 EVIDENCE、脱敏执行报告；focused 工程预算 <=4小时、<=8个测试进程/每个<=120秒、目标<=2GiB、证据<=10MiB；真实科学/模型与受保护数据运行预算 0。
- Codex 在冻结边界内自主实施、调试和聚焦验证，集中发布一次候选供 Astra 最终独立验收。当前**仅为授权就绪**，尚无实际实施或通过证据；`execution.md`、`acceptance.md`、`retrospective.md` 仍待产生。
- 不更改旧 C9 PAUSED、CALL_LEDGER_UNRESOLVED、A16 FAIL_CLOSED、Results FALSE、劳动单位 UNKNOWN、既有经济法则、已关闭预算。**本登记不覆盖 plan 冻结原件。**

## 2026-10-12 第二阶段迁移记录（历史截点）
迁移后首版：**尚未制定，等待第三阶段**。Owner手动启动；本轮没有新版本号、批准、执行或通过记录。

## 路线图入口
历史[两资产路线图](CH5_TWO_ASSET_HANK_ROADMAP_CURRENT.md)及[Python重建路线图](DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md)保留现有内容和证据级别，不能由旧“下一步”直接启动。未来路线更新不能改原冻结版本。
当前优先未闭问题：真实solver来源绑定、聚合/frozen实际调用、frozen→batch构造、callback装配、量纲/人口分母/时点及科学运行与环境/保护。它们是问题清单，不是第三阶段执行计划。

## 后续登记约定
Owner确立版本后，在此登记：版本标识及阶段、正式计划路径和冻结依据（批准来源及固定提交）、代码基线与候选SHA、实际执行报告、独立验收、复盘位置和终态。
可采用`versions/<Owner确立的版本标识>/plan.md`、`execution.md`、`acceptance.md`、`retrospective.md`；这些是命名约定，目前全部待创建，不是现存链接。草稿仅版前协商。冻结计划不可事后改目标；修复批次针对原目标内缺陷，新增需求入未来版。

## 历史登记与固定证据
- 历史K1B等冻结版本：原件/原状态不重写。已有[科学合同账固定快照](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/a1db8c114dec0ab69d69a5576e153a7f868cba0e/SCIENTIFIC_DECISIONS.md)与[双边资本网络冻结稿固定快照](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/a1db8c114dec0ab69d69a5576e153a7f868cba0e/docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md)。
- 上述SHA是本地提交已存在于远端备份分支的文件快照，不是各合同首次冻结提交或全部验收基线的追认。逐版本原冻结/代码/验收commit尚未从完整历史逐一核出，记UNKNOWN，不补造。
- 最新接受为scripts/tools metadata门ACCEPT/CLOSED；末binding SOURCE_ONLY门NOT_ACCEPTED/CLOSED，见[近期账快照](knowledge/published/CH5_WORK_ACCEPTANCE_LEDGER_MANUAL_HANDOFF_20261011_140603Z.md)。这些旧stage不是迁移后新版本。
- 各历史执行/复盘资料未全量覆盖，若需要立版必须按具体问题核原件。备份≠验收，自测≠最终验收，验收≠发布。

## 第二阶段执行端交接（不登记为新版本）

[Codex实时交接](CH5_ASTRA_CODEX_EXECUTION_HANDOFF_CURRENT.md)及[Owner手工启动Prompt](CH5_ASTRA_CODEX_NEW_SESSION_PROMPT_CURRENT.md)补充本地封存状态。发布基线3ec76075c90f823ed83ca6e0a8c385a61f79ef85；本次文档提交以发布回执及分支fresh-fetch为准。本地代码HEAD不移动；迁移后首版NOT_STARTED，等待Owner第三阶段。交接文件准备完成不等于新会话已实际接收。
