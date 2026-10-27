# CH5 TEMP31 工资—劳动—税收静态语义审计 R1 · 独立验收

TASK=CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027
CANDIDATE_COMMIT=9bdc9e83127d32e6e29a0a5895800fd97d92cd3a
REVIEW_VERDICT=PASS_BOUNDED_STATIC_SOURCE_SEMANTICS__SCIENTIFIC_ACCEPTANCE_BLOCKED
STAGE_A=COMPLETED_BOUNDED
STAGE_B=COMPLETED_BOUNDED_WITH_FINDINGS
STAGE_C=COMPLETED_BOUNDED
STOP=TRUE
AUTO_NEXT=FALSE

## 1. 提交、清单与原件硬门

- 固定候选: `9bdc9e83127d32e6e29a0a5895800fd97d92cd3a`
- 父提交: `ff85121748e4f101b83346c19a9fdadd4b9b998a`
- Root tree: `f7b14adfa596be415f612c0640c87d8f16925063`
- 固定任务: `a4476b1873b0950cf4fbd3d10122de41cd981dec`
- 候选分支HEAD与候选提交一致，治理HEAD在审阅期间为该任务固定提交。
- 与任务基线比较，仅有任务目录13份新报告，无科研源码变更。
- GitHub固定提交目录13份文件，manifest记录12份。独立读取12份payload并以UTF-8原始字节复算Git Blob/字节数/SHA-256，12/12全匹配；manifest自身单独确认Blob `e9b604d82518a27df4031f788283b75938dd2bc1`、大小8117B，不自引用。
- `source_excerpts.json`中116段摘录的文本SHA-256逐条重算，116/116全部匹配。哈希证明公开摘录内部字节身份，不等同于本地全部原源码已亲自重读。
- 独立读取本会话上传的`博士论文tex.zip`：284056B，SHA-256 `c0505aff92a87d2b7ca5670213cd4f3b48298d1bded4fa287960abadde8e7661`；成员`c5.tex`(102309B, SHA-256 `9193fd7aef06478f2bbf20f81bed0d14d42870dd924ff5b1cefc296cb18c6ae9`)与`c3.tex`(60071B, SHA-256 `df6ad15190bc34023a89cd9eef36732929b641f3b3a4d98fcfc05427199ffc57`)和报告一致。
- 独立读取`多省份HANK_matlab原版程序.zip`：1578316B，SHA-256 `ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755`；`wage_caculate.m`与`Lt_seperate.m`成员哈希均匹配；原式已经独立检查。
- GitHub固定提交上的Python同名源文件Blob不必等于执行者本地dirty/untracked工作树逐件哈希。例如`wage.py` Git Blob `48001b2e4ca64d81dda6174255f6ccf130e07004`，本地报告源码Git-style Blob `222c998544945e945d5e17d3a5bbef08896d43dd`。版本确实不同。审阅仅认可带SHA的本地候选静态摘录，不把它们假定成已经发布或合并的生产源。

## 2. 独立支持的主要经济学与实现发现

**F1 工作地/来源地税索引差异：PROVEN_STATIC_EXPRESSION_DIFFERENCE。** `wage_caculate.m:8`使用目的地`results{j}.tau`，`Lt_seperate.m:7`使用来源地`results{i}.tau`。当前本地Python `C_W:57-63`为目的地，`C_L:107-125`为来源地；隔离R3 `P3_L:113-131`和`P3_O:168-176`使用目的地。当前`C_RUN:235-240`仍按来源传参。R3不是全生产闭包。对于原论文全国统一tau的特例，两种索引可能数值相同；差异在省际异质tau情形才有实质影响。

**F2 重复工资税楔子：SUSPECTED_CONTRACT_DEFECT_CONDITIONAL。** `C_W:57-72`构造已含目的地tau和迁移楔子的来源家户综合`w`；`C_SS:153-168`写入下一轮state.w；`C_EMP:345-350`/`C_A:204-211`仍支持把非零tau与综合w一同送入HA，`C_HA:159-164`再次应用`1-tau-migration`。若输入`w`已净含同一工资税，此流形成重复税楔子风险。历史初始`state.w`是否税后未知；通用HA若接受税前工资，非零tau可以合法。HA劳动FOC与预算两处使用相同税后工资不等于重复扣税。R2 `P2_A`和`P2_EMP`局部`tau=0`修复不是已认证生产全链。当前corrected直接路径的state.w/state.tau→net_wage也有实际来源摘录，但跨分支/统一快照未被证明，不推断全生产故障已复现。

**F3 财政工资税基和版本差异：PROVEN_EXPRESSION_DIFFERENCE; DIMENSIONAL_ISSUE_SUSPECTED。** 原始`c5.tex:161`为`Ls^j*tau`，原MATLAB`HANK_firm.m:95`为`Lt*tau`，第三章`c3.tex:50`含`L*w*tau_w`。当tau按劳动收入比例征收时缺工资因子有量纲疑点，需Owner依据真实税基、归一化和财政对象决定，不能自行改式。原`c5.tex:161`对j求和内部公司税项仍为i下标，是另一处待独立经济学/索引裁决的问题。

**F4 综合工资幂次和偏好符号版本不一致：PROVEN_DIFF; ADOPTION_OPEN。** 原c5和当前/历史综合工资使用alphal负幂；隔离R1/R2候选用正幂。当前原`phi`使用正号，R2候选使用负号。版本标签及计算前的输入时序必须保留；候选不等于正式V010修订。

**F5 工资、劳动、人口变量不同：SUPPORTED_SOURCE_SEMANTICS。** 生产端wjt是给定模型有效劳动规模计算的劳动边际产出并可能裁切；来源家户综合w是带phi/sigma/tau和跨目的地加总的非线性系数。个体劳动l、`∫z l dg`、origin人口N、destination Lt_supply、corrected网格状态数N=800互不等同。当前分拆中由消费/旧企业工资/人口得到Lt_mat，未证明它与论文的分布有效劳动恒等对应。

**F6 NBS统计桥：27/27 NO DIRECT MATCH。** 三个xlsx是原始候选：2018非私营倾向均值31省，私营均值30省另西藏30隔离，城镇单位工资总额31省。未有NBS指标代码、原始导出链接/时间、共同vintage、与模型期对应、gross/net、工时/有效劳动、匹配分母、ID/数组连接或生产调用闭包。不得从工资总额除均值推就业、代入净工资或填充w/wjt、不得解释重复30为已知缺失码。历史2009单标量w/wjt/tau与真实31省2018观测不同。

## 3. 额外明确的审阅边界

- `validators/multi_province/mp4b_python_empirical.py`的固定历史Git源码首行标明其是`Validation-only one-shot calendar-2009 Python stationary entry`。候选台账有时将其中的调用点分类`PRODUCTION_CALLER`，此术语不应理解为正式已部署生产入口。这是来源分类措辞观察，必须按`validation-only`和真实生产闭包分别对待。
- 本会话无法直接访问Owner Windows下尚未提交的当前Python工作树。其SHA和公开摘录链为执行者核验并发布的有界版本证据；独立确认了原TeX、MATLAB原字节关键部分及Git固定提交上的不同源码Blob，不能宣称已独立读取执行者全部本地字节或动态验证。
- `source_excerpts.json`的116个摘录sha匹配，只说明报告内摘录身份，不证明摘要间所有调用关系在运行时接通。
- 13份报告里没有原始Excel、工资值面板、完整TeX或MATLAB档案。公开内容限研究必要摘录与元数据；隐私扫描有界。Codex前后dirty/untracked、index/refs不变为其自报保护证据，GPT不能独立复读其Windows工作树。
- `INDEPENDENT_COMPLETION_EVENT.json`在执行者交付中为UNKNOWN。GPT本轮的独立审阅报告不是运行者自证的执行完成事件。

## 4. 层级裁决

artifact_integrity=PASS_BOUNDED__GITHUB_12_OF_12_BYTES_BLOB_SHA256__MANIFEST_SEPARATE
source_identity=PASS_BOUNDED__THESIS_AND_MATLAB_ORIGINAL_ARCHIVES_INDEPENDENTLY_HASHED__CURRENT_PYTHON_UNCOMMITTED_PROVENANCE_LIMIT
numeric_review=NOT_RUN
implementation_review=PASS_BOUNDED_STATIC_SOURCE_TRACING_ONLY
scientific_review=PASS_BOUNDED_STATIC_SEMANTIC_RISK_IDENTIFICATION__FORMAL_MODEL_ACCEPTANCE_BLOCKED
privacy_review=PASS_BOUNDED_REPORT_SCOPE_ONLY
actual_terminal=STATIC_AUDIT_COMPLETE_WITH_GAPS__STOPPED
delivery=PASS_BOUNDED
cleanup=NO_SCIENTIFIC_EVIDENCE_CLEANUP; ONLY_TEMPORARY_ACCEPTANCE_REPORT_REMOVAL_AFTER_REMOTE_READBACK
not_completed=PRODUCTION_CALLBACK_AND_SNAPSHOT_CLOSURE;ORIGIN_DESTINATION_ID_ARRAY_JOIN;LABOR_UNIT_AND_MODEL_PERIOD_BRIDGE;TAX_GROSS_NET_CONTRACT;FISCAL_TAX_BASE;NBS_INDICATOR_AND_VINTAGE;COMBINED_R2_R3_IMPLEMENTATION;MODEL_AND_NUMERIC_ACCEPTANCE

## 5. Owner decision boundaries / next step

Current review task accepted, but no model repair is approved. Owner to decide among evidence-backed choices: preserve endogenous firm wjt while using statistical wage series as external reference; decide if/when composite wage w is net for specific consumers and how single-tax invariant is encoded; reconcile workplace-specific heterogeneous tau_j with thesis' uniform tau assumption; decide the labor/effective-hours unit and fiscal tax base. Any actual repair, integration, testing or source adoption requires a separate task.

ACTIVE_TASK=NONE
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_NEXT=FALSE

This is an independent source-limited verdict, not scientific acceptance or permission to modify/run V010/V011.
